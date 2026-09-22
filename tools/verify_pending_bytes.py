#!/usr/bin/env python3
"""Offline, deterministic pending-packet byte checks; never records receipt.

Input JSON: {"snapshot": "40-hex immutable Market commit", "files": [
  {"path": "evidence/research/pending/DOMAIN/RUN/HASH/Report.md",
   "content": "exact connector text", "git_blob_sha": "40-hex from that Git tree",
   "expected_git_bytes": 123}, ...]}.

Fetch tree identities independently from the same immutable snapshot. Preserve
the exact returned Unicode strings, including terminal newlines. This tool does
not authenticate connector provenance or evaluate report claims/eligibility.
"""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

NAMES = {'Report.md', 'report-envelope.json', 'packet.json'}

def sha256(body):
    return hashlib.sha256(body).hexdigest()

def verify(bundle):
    commit = bundle.get('snapshot', '')
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise ValueError('Exact immutable source commit required')
    groups, seen = {}, set()
    for row in bundle['files']:
        path = row['path']
        parts = PurePosixPath(path).parts
        if (len(parts) != 7 or parts[:3] != ('evidence', 'research', 'pending')
                or str(PurePosixPath(path)) != path or '\\' in path
                or not all(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', x) for x in parts[3:5])
                or not re.fullmatch(r'[0-9a-f]{64}', parts[5]) or parts[6] not in NAMES):
            raise ValueError('Unsafe or unexpected pending path')
        if path in seen:
            raise ValueError('Duplicate file path')
        seen.add(path)
        groups.setdefault('/'.join(parts[:-1]), []).append(row)
    if not groups:
        raise ValueError('No packet files supplied')
    results = []
    for path, rows in sorted(groups.items()):
        errors, files, bodies = [], [], {}
        if {PurePosixPath(r['path']).name for r in rows} != NAMES:
            errors.append('All three complete files required')
        for row in sorted(rows, key=lambda r: r['path']):
            name = PurePosixPath(row['path']).name
            body = row['content'].encode('utf-8', errors='strict')
            bodies[name] = body
            blob = hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()
            if not re.fullmatch(r'[0-9a-f]{40}', row.get('git_blob_sha', '')) or blob != row['git_blob_sha']:
                errors.append(name + ': immutable Git blob mismatch')
            if type(row.get('expected_git_bytes')) is not int or len(body) != row['expected_git_bytes']:
                errors.append(name + ': immutable tree byte count mismatch')
            files.append({'file': name, 'bytes': len(body), 'sha256': sha256(body), 'git_blob_sha': blob})
        key = None
        if NAMES <= bodies.keys():
            packet = json.loads(bodies['packet.json'])
            envelope = json.loads(bodies['report-envelope.json'])
            domain, run, report_hash = path.split('/')[-3:]
            key = ':'.join([run, report_hash] if domain == 'gev' else [domain, run, report_hash])
            for field, expected in [('domain', domain), ('run_id', run), ('report_sha256', report_hash), ('delivery_key', key)]:
                if packet.get(field) != expected:
                    errors.append('packet.' + field + ': identity mismatch')
                if field != 'delivery_key' and envelope.get(field) != expected:
                    errors.append('envelope.' + field + ': identity mismatch')
            if envelope.get('delivery_key', key) != key:
                errors.append('envelope.delivery_key: identity mismatch')
            for name, prefix in [('Report.md', 'report'), ('report-envelope.json', 'envelope')]:
                if packet.get(prefix + '_sha256') != sha256(bodies[name]):
                    errors.append(name + ': declared SHA-256 mismatch')
                if type(packet.get(prefix + '_bytes')) is not int or packet[prefix + '_bytes'] != len(bodies[name]):
                    errors.append(name + ': declared byte count mismatch')
            for field in ('received_at_utc', 'market_received_at_utc', 'acknowledged_at_utc', 'receipt_at_utc'):
                if packet.get(field) is not None:
                    errors.append('packet.' + field + ': producer must not prefill receiver state')
        results.append({'packet_path': path, 'delivery_key': key, 'integrity_verified': not errors,
                        'errors': errors, 'files': files})
    return {'schema_version': 1, 'source_snapshot': commit,
            'scope': 'integrity_only_not_receipt_acknowledgment_or_canonical_acceptance',
            'all_integrity_checks_pass': all(r['integrity_verified'] for r in results), 'packets': results}

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 tools/verify_pending_bytes.py exact-fetched-bundle.json')
    try:
        result = verify(json.loads(Path(sys.argv[1]).read_bytes()))
    except (ValueError, TypeError, KeyError, UnicodeError) as exc:
        result = {'scope': 'integrity_only_not_receipt_acknowledgment_or_canonical_acceptance',
                  'all_integrity_checks_pass': False, 'error': str(exc)}
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if result['all_integrity_checks_pass'] else 1

if __name__ == '__main__':
    sys.exit(main())
