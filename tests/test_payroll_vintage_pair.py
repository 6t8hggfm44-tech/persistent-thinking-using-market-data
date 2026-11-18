import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from tools import payroll_vintage_pair as trial


class PayrollPairTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1]
        for folder in (trial.BASE, Path("meta/hypothesis_weights")):
            shutil.copytree(source / folder, self.root / folder)
        (self.root / "evidence").mkdir()
        (self.root / "evidence/packet.md").write_text("test evidence")
        self.now = trial.timestamp("2026-11-24T22:01:00Z")
        self.draft = dict(reference_month="2026-11", id="P999999", live_model_version="0.2.21",
                          source_commit="a"*40, evidence_cutoff="2026-11-24T22:00:00Z",
                          evidence=[dict(path="evidence/packet.md", available_at="2026-11-23T22:00:00Z")],
                          conditional_probabilities=dict(H001=0.7, H002=0.1, H003=0.6, H004=0.5),
                          conditional_rationale={h: "fixture only" for h in trial.HYPOTHESES},
                          live_rationale="fixture", surprising_if=["fixture surprise"])

    def test_common_inputs_and_distinct_arms(self):
        files = trial.prepare(self.root, self.draft, self.now)
        pair = files[trial.BASE / "P999999.json"]
        canonical = files[Path("predictions/open/P999999.json")]
        self.assertEqual(pair["evidence_cutoff"], canonical["evidence_cutoff"])
        self.assertEqual(pair["created_at"], canonical["created_at"])
        self.assertEqual(pair["target"], "US_NONFARM_PAYROLL_MOM_NOV_2026_FIRST_RELEASE")
        self.assertEqual(pair["arms"]["current"]["probability"], 0.577)
        self.assertEqual(pair["arms"]["previous"]["probability"], 0.555)
        self.assertEqual(pair["arms"]["benchmark"]["probability"], 5/6)
        self.assertEqual(canonical["forecast"]["probability"], 0.577)
        self.assertEqual(canonical["forecast"]["event_threshold_jobs_gte"], 100000)

    def test_later_live_model_preserves_both_vintages(self):
        draft = dict(self.draft, live_model_version="0.2.22", live_probability=0.43)
        files = trial.prepare(self.root, draft, self.now)
        self.assertEqual(files[Path("predictions/open/P999999.json")]["forecast"]["probability"], 0.43)
        self.assertEqual(files[trial.BASE / "P999999.json"]["arms"]["current"]["probability"], 0.577)

    def test_excludes_outside_window_future_input_and_retrofit(self):
        for date in ("2026-11-18T22:01:00Z", "2026-12-04T15:00:00Z"):
            with self.assertRaisesRegex(ValueError, "window"):
                trial.prepare(self.root, self.draft, trial.timestamp(date))
        late = copy.deepcopy(self.draft)
        late["evidence"][0]["available_at"] = "2026-11-24T22:00:01Z"
        with self.assertRaisesRegex(ValueError, "after the common cutoff"):
            trial.prepare(self.root, late, self.now)
        (self.root / "predictions/open").mkdir(parents=True)
        (self.root / "predictions/open/P000001.json").write_text(
            '{"target":"US_NONFARM_PAYROLL_MOM_NOV_2026_FIRST_RELEASE"}')
        with self.assertRaisesRegex(ValueError, "retrofit"):
            trial.prepare(self.root, self.draft, self.now)

    def test_one_observation_ties_and_coverage(self):
        self.draft["conditional_probabilities"] = dict.fromkeys(trial.HYPOTHESES, 0.4)
        files = trial.prepare(self.root, self.draft, self.now)
        pair = files[trial.BASE / "P999999.json"]
        self.assertEqual(pair["arms"]["current"]["probability"], 0.4)
        self.assertEqual(pair["arms"]["previous"]["probability"], 0.4)
        pending = list(trial.opportunities(self.root, trial.timestamp("2026-11-18T12:00:00Z")))
        self.assertEqual(len(pending), 12)
        self.assertTrue(all(row["state"] == "upcoming" for row in pending))
        closed = list(trial.opportunities(self.root, trial.timestamp("2026-11-28T12:00:00Z")))
        self.assertEqual(closed[0]["state"], "unaccounted")
