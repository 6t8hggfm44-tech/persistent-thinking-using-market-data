"""Regression coverage for the omitted September 25 index rows."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_intake_index", ROOT / "tools/check_intake_index.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
FIXTURE = json.loads((ROOT / "tests/fixtures/intake_index_regression.json").read_text())


class IntakeIndexRegression(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for archive, keys in [("research", FIXTURE["research_keys"]),
                              ("gev-weekly", [FIXTURE["gev_key"]])]:
            for key in keys:
                path = self.root / "evidence" / archive / Path(*key.split(":")) / "intake.json"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"delivery_key": key, "received_at_utc": FIXTURE["received_at_utc"]}))
        self.write_index("research", [])
        self.write_index("gev-weekly", [FIXTURE["gev_key"]])

    def write_index(self, archive, keys):
        # Repeated supersedes references must never become additional rows.
        text = "| Delivery key | Supersedes |\n|---|---|\n"
        text += "\n".join(f"| `{key}` | `{FIXTURE['research_keys'][0]}` |\n" for key in keys)
        (self.root / "evidence" / archive / "INDEX.md").write_text(text)

    def test_supplement_cannot_mask_four_omitted_rows(self):
        (self.root / "evidence/research/INDEX-2026-09-25-supplement.md").write_text("\n".join(FIXTURE["research_keys"]))
        result = checker.check(self.root)
        self.assertFalse(result["passed"])
        self.assertEqual(result["archives"]["research"]["missing_index_keys"], sorted(FIXTURE["research_keys"]))

    def test_reconciled_rows_pass_without_mutating_receipts_or_counting_pending(self):
        self.write_index("research", FIXTURE["research_keys"])
        pending = self.root / "evidence/research/pending/corporate/run/hash/intake.json"
        pending.parent.mkdir(parents=True)
        pending.write_text('{"delivery_key":"not-a-canonical-record"}')
        before = {str(path): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertTrue(checker.check(self.root)["passed"])
        self.assertEqual(before, {str(path): path.read_bytes() for path in self.root.rglob("*") if path.is_file()})

    def test_duplicate_index_entry_is_rejected(self):
        keys = FIXTURE["research_keys"]
        self.write_index("research", keys + [keys[0]])
        result = checker.check(self.root)
        self.assertFalse(result["passed"])
        self.assertEqual(result["archives"]["research"]["duplicate_index_keys"], [keys[0]])

    def test_gev_must_stay_in_its_own_index(self):
        self.write_index("research", FIXTURE["research_keys"] + [FIXTURE["gev_key"]])
        self.write_index("gev-weekly", [])
        result = checker.check(self.root)
        self.assertFalse(result["passed"])
        self.assertEqual(result["archives"]["gev"]["missing_index_keys"], [FIXTURE["gev_key"]])
        self.assertEqual(result["archives"]["research"]["index_keys_without_canonical_record"], [FIXTURE["gev_key"]])


if __name__ == "__main__":
    unittest.main()
