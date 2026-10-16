#!/usr/bin/env python3
"""Offline exact-byte Market checkpoints. No network, canonical writes or validation.

prepare reads an explicit file list; verify checks a fetched checkpoint against
an independently fetched immutable Git blob identity; recover extracts to a new
quarantine directory only. Publication is a separately authorized connector step.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile

SCHEMA = 'market-output-checkpoint-v1'
REPO = '6t8hggfm44-tech/persistent-thinking-using-market-data'
LIMIT = 32 * 1024 * 1024


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def path_ok(value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('unsafe path')
    p = PurePosixPath(value)
    if p.is_absolute() or str(p) != value or any(x in ('.', '..') or x.startswith('.') for x in p.parts):
        raise ValueError('unsafe path')
    if not all(re.fullmatch(r'[A-Za-z0-9_-][A-Za-z0-9._-]*', x) for x in p.parts):
        raise ValueError('unsafe path')
    return value


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


def decode(raw):
    if len(raw) > LIMIT:
        raise ValueError('checkpoint too large')
    doc = json.loads(raw, object_pairs_hook=no_duplicates)
    if set(doc) != {'schema', 'repository', 'run_id', 'source_commit', 'kind', 'files'}:
        raise ValueError('unexpected checkpoint fields')
    if doc['schema'] != SCHEMA or doc['repository'] != REPO:
        raise ValueError('wrong checkpoint schema or repository')
    if not isinstance(doc['run_id'], str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,127}', doc['run_id']):
        raise ValueError('invalid run identity')
    if not isinstance(doc['source_commit'], str) or not re.fullmatch(r'[0-9a-f]{40}', doc['source_commit']):
        raise ValueError('immutable source commit required')
    if doc['kind'] not in ('original-output', 'synthetic-test'):
        raise ValueError('original bytes or explicit synthetic fixture required')
    if not isinstance(doc['files'], list) or not doc['files']:
        raise ValueError('nonempty explicit file inventory required')
    files = {}
    for row in doc['files']:
        if set(row) != {'path', 'bytes', 'sha256', 'base64'}:
            raise ValueError('unexpected file fields')
        path = path_ok(row['path'])
        if path in files:
            raise ValueError('duplicate path')
        body = base64.b64decode(row['base64'], validate=True)
        if type(row['bytes']) is not int or row['bytes'] != len(body) or row['sha256'] != digest(body):
            raise ValueError('payload digest or byte length mismatch')
        files[path] = body
    # Reject file/directory prefix collisions before extraction.
    for path in files:
        if any(str(p) in files for p in PurePosixPath(path).parents if str(p) != '.'):
            raise ValueError('file/directory collision')
    return doc, files


def read_bounded(path, limit=LIMIT):
    # Nonblocking open prevents a FIFO from hanging before the fstat rejection.
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise ValueError('regular file required')
        if info.st_size > limit:
            raise ValueError('input too large')
        body = stream.read(limit + 1)
        if len(body) > limit:
            raise ValueError('input too large')
        return body


def sync_ancestors(directory):
    # Sync all links, including newly created nested directories and root parent.
    for path in (Path(directory), *Path(directory).parents):
        fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)


def prepare(root, paths, run_id, source_commit, kind):
    root = Path(root).resolve(strict=True)
    rows = []
    total = 0
    for name in paths:
        path_ok(name)
        candidate = root / name
        # Reject links at every component, including links staying inside root.
        if any(p.is_symlink() for p in [candidate, *list(candidate.parents)[:len(PurePosixPath(name).parts)-1]]):
            raise ValueError('symlink input forbidden')
        candidate.resolve(strict=True).relative_to(root)
        body = read_bounded(candidate, LIMIT - total)
        total += len(body)
        rows.append({'path': name, 'bytes': len(body), 'sha256': digest(body),
                     'base64': base64.b64encode(body).decode('ascii')})
    raw = (json.dumps({'schema': SCHEMA, 'repository': REPO, 'run_id': run_id,
                       'source_commit': source_commit, 'kind': kind,
                       'files': sorted(rows, key=lambda x: x['path'])},
                      sort_keys=True, indent=2) + '\n').encode()
    decode(raw)
    return raw


def write_new(path, raw):
    """Atomic complete publication on one filesystem; never overwrite."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.checkpoint-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as out:
            out.write(raw)
            out.flush()
            os.fsync(out.fileno())
        os.link(tmp, path)  # fails closed if target exists, including a symlink
        sync_ancestors(path.parent)
    finally:
        os.unlink(tmp)


def verify_remote(raw, expected_blob, expected_bytes):
    decode(raw)
    if not re.fullmatch(r'[0-9a-f]{40}', expected_blob) or git_blob(raw) != expected_blob:
        raise ValueError('remote Git blob mismatch')
    if type(expected_bytes) is not int or len(raw) != expected_bytes:
        raise ValueError('remote tree byte length mismatch')
    return {'scope': 'checkpoint_byte_integrity_only', 'sha256': digest(raw),
            'git_blob_sha': expected_blob, 'bytes': len(raw)}


def recover(raw, destination):
    """Exclusive quarantine creation. Never promotes bytes to canonical paths.

Incomplete extractions remain marked by absence of RECOVERY_COMPLETE.json.
An existing destination is never overwritten or resumed automatically.
"""
    doc, files = decode(raw)
    destination = Path(destination)
    destination.mkdir()  # exclusive claim, no existing directory accepted
    for name, body in files.items():
        write_new(destination / 'payload' / name, body)
    for name, body in files.items():
        if (destination / 'payload' / name).read_bytes() != body:
            raise ValueError('recovery readback mismatch')
    sync_ancestors(destination)
    receipt = {'schema': SCHEMA, 'run_id': doc['run_id'], 'kind': doc['kind'],
               'checkpoint_sha256': digest(raw), 'file_count': len(files),
               'status': 'quarantine_bytes_verified_not_canonical_or_validated'}
    write_new(destination / 'RECOVERY_COMPLETE.json', (json.dumps(receipt, sort_keys=True, indent=2)+'\n').encode())
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--root', required=True)
    p.add_argument('--run-id', required=True)
    p.add_argument('--source-commit', required=True)
    p.add_argument('--kind', choices=['original-output', 'synthetic-test'], required=True)
    p.add_argument('--output', required=True)
    p.add_argument('paths', nargs='+')
    p = sub.add_parser('verify')
    p.add_argument('checkpoint')
    p.add_argument('--blob-sha', required=True)
    p.add_argument('--bytes', type=int, required=True)
    p = sub.add_parser('recover')
    p.add_argument('checkpoint')
    p.add_argument('destination')
    args = parser.parse_args()
    if args.command == 'prepare':
        raw = prepare(args.root, args.paths, args.run_id, args.source_commit, args.kind)
        write_new(args.output, raw)
        if Path(args.output).read_bytes() != raw:
            raise ValueError('local checkpoint readback mismatch')
        result = {'status': 'local_only_not_remotely_saved', 'sha256': digest(raw), 'bytes': len(raw)}
    elif args.command == 'verify':
        result = verify_remote(read_bounded(args.checkpoint), args.blob_sha, args.bytes)
    else:
        result = recover(read_bounded(args.checkpoint), args.destination)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
