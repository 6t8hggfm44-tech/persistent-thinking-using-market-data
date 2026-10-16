"""Synthetic persistence tests only; no market data, network or validator runs."""
import base64
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('checkpoint', Path(__file__).parents[1]/'tools/market_checkpoint.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root/'source'
        self.source.mkdir()
        (self.source/'a.txt').write_bytes(b'first\r\nsecond\n\x00\xff')
        (self.source/'b.json').write_bytes('{"synthetic":"\u03b2"}\n'.encode())
        self.raw = c.prepare(self.source, ['a.txt','b.json'], 'synthetic-1', 'a'*40, 'synthetic-test')

    def changed(self, mutate):
        doc = json.loads(self.raw)
        mutate(doc)
        return json.dumps(doc).encode()

    def test_round_trip_remote_identity_and_quarantine(self):
        local = self.root/'checkpoint.json'
        c.write_new(local, self.raw)
        identity = c.verify_remote(local.read_bytes(), c.git_blob(self.raw), len(self.raw))
        self.assertEqual(identity['sha256'], c.digest(self.raw))
        dest = self.root/'restored'
        receipt = c.recover(local.read_bytes(), dest)
        self.assertEqual(receipt['file_count'], 2)
        for name in ('a.txt','b.json'):
            self.assertEqual((dest/'payload'/name).read_bytes(), (self.source/name).read_bytes())
        self.assertTrue((dest/'RECOVERY_COMPLETE.json').exists())

    def test_duplicate_write_never_overwrites(self):
        dest = self.root/'checkpoint.json'
        c.write_new(dest, self.raw)
        with self.assertRaises(FileExistsError): c.write_new(dest, b'different')
        self.assertEqual(dest.read_bytes(), self.raw)

    def test_existing_recovery_never_overwrites(self):
        dest = self.root/'restore'
        dest.mkdir()
        (dest/'sentinel').write_text('preserve')
        with self.assertRaises(FileExistsError): c.recover(self.raw, dest)
        self.assertEqual((dest/'sentinel').read_text(), 'preserve')

    def test_bad_remote_identity_and_size(self):
        for sha, size in [('0'*40,len(self.raw)), (c.git_blob(self.raw),len(self.raw)+1)]:
            with self.assertRaises(ValueError): c.verify_remote(self.raw, sha, size)

    def test_corruption_missing_payload_and_duplicate_path(self):
        mutations = [lambda d:d['files'][0].update(base64='!!!'),
                     lambda d:d['files'][0].update(sha256='0'*64),
                     lambda d:d['files'][0].update(bytes=True),
                     lambda d:d.update(files=[]),
                     lambda d:d['files'].append(d['files'][0])]
        for mutate in mutations:
            with self.assertRaises(ValueError): c.decode(self.changed(mutate))

    def test_unsafe_paths(self):
        for name in ('../outside','/absolute','.git/config','x/../a','a//b','a\\b','a/./b','a/'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                c.decode(self.changed(lambda d:d['files'][0].update(path=name)))

    def test_prefix_collision(self):
        with self.assertRaises(ValueError):
            c.decode(self.changed(lambda d:d['files'][1].update(path='a.txt/child')))

    def test_input_symlink_rejected(self):
        (self.source/'link').symlink_to(self.source/'a.txt')
        with self.assertRaises(ValueError):
            c.prepare(self.source,['link'],'s','a'*40,'synthetic-test')

    def test_duplicate_json_keys_and_wrong_repository(self):
        with self.assertRaises(ValueError): c.decode(b'{"schema":1,"schema":2}')
        with self.assertRaises(ValueError): c.decode(self.changed(lambda d:d.update(repository='other')))

    def test_truncated_checkpoint(self):
        with self.assertRaises(ValueError): c.decode(self.raw[:-20])

    def test_interrupted_write_has_no_visible_partial_checkpoint(self):
        dest = self.root/'checkpoint.json'
        with patch.object(c.os,'fsync',side_effect=OSError('simulated disk failure')):
            with self.assertRaises(OSError): c.write_new(dest,self.raw)
        self.assertFalse(dest.exists())

    def test_interrupted_extraction_has_no_completion_receipt(self):
        dest = self.root/'restore'
        original = c.write_new
        calls = 0
        def fail_second(path, raw):
            nonlocal calls
            calls += 1
            if calls == 2: raise OSError('synthetic interrupted extraction')
            original(path, raw)
        with patch.object(c,'write_new',side_effect=fail_second):
            with self.assertRaises(OSError): c.recover(self.raw,dest)
        self.assertFalse((dest/'RECOVERY_COMPLETE.json').exists())
        with self.assertRaises(FileExistsError): c.recover(self.raw,dest)
        c.recover(self.raw,self.root/'new-attempt')

    def test_recovery_rejects_corruption_before_creating_destination(self):
        dest = self.root/'restore'
        with self.assertRaises(ValueError): c.recover(self.raw[:-1] + b'x', dest)
        self.assertFalse(dest.exists())

    def test_recovery_readback_failure_is_not_complete(self):
        dest = self.root/'restore'
        with patch.object(Path,'read_bytes',return_value=b'corrupt'):
            with self.assertRaises(ValueError): c.recover(self.raw,dest)
        self.assertFalse((dest/'RECOVERY_COMPLETE.json').exists())

    def test_deterministic_prepare_and_no_source_mutation(self):
        original = (self.source/'a.txt').read_bytes()
        other = c.prepare(self.source,['b.json','a.txt'],'synthetic-1','a'*40,'synthetic-test')
        self.assertEqual(other,self.raw)
        self.assertEqual((self.source/'a.txt').read_bytes(),original)

    def test_regular_bounded_inputs(self):
        with self.assertRaises(ValueError): c.read_bounded(self.source/'a.txt', 2)
        fifo = self.source/'fifo'
        os.mkfifo(fifo)
        with self.assertRaises(ValueError): c.read_bounded(fifo)
        with patch.object(c, 'LIMIT', 10):
            with self.assertRaises(ValueError):
                c.prepare(self.source,['a.txt','b.json'],'s','a'*40,'synthetic-test')

    def test_directory_sync_before_completion_marker(self):
        dest = self.root/'restore'
        events = []
        original_write, original_sync = c.write_new, c.sync_ancestors
        def write(path, raw):
            events.append(('write', str(path)))
            original_write(path, raw)
        def sync(path):
            events.append(('sync', str(path)))
            original_sync(path)
        with patch.object(c,'write_new',side_effect=write), patch.object(c,'sync_ancestors',side_effect=sync):
            c.recover(self.raw,dest)
        marker = events.index(('write', str(dest/'RECOVERY_COMPLETE.json')))
        self.assertIn(('sync', str(dest)), events[:marker])

    def test_link_failure_preserves_existing_and_no_partial_file(self):
        dest = self.root/'checkpoint.json'
        with patch.object(c.os,'link',side_effect=OSError('synthetic link failure')):
            with self.assertRaises(OSError): c.write_new(dest,self.raw)
        self.assertFalse(dest.exists())

    def test_nested_payload_roundtrip(self):
        (self.source/'nested'/'deep').mkdir(parents=True)
        (self.source/'nested'/'deep'/'a.txt').write_bytes(b'nested synthetic')
        raw = c.prepare(self.source,['nested/deep/a.txt'],'s','a'*40,'synthetic-test')
        c.recover(raw,self.root/'nested-restore')
        self.assertEqual((self.root/'nested-restore/payload/nested/deep/a.txt').read_bytes(), b'nested synthetic')

if __name__ == '__main__': unittest.main()
