# Transfer Candidates for Universal Review

These are provisional lessons surfaced by the market experiment. They are not universal truth and should be evaluated by the Universal reconciler under `UNIVERSAL_CONSTITUTION.md`.

## TC-2026-001 — Proper-score success is not the same as benchmark-relative information

**Status:** Provisional; one clean live example.

**Observation:** P000012 assigned 0.55 probability to July 2026 headline CPI being <=3.4% YoY. The event resolved true and received a favorable Brier/log score, but 3.4% was also the timestamped published consensus point and the first-release outcome was exactly 3.4%.

**Methodological inference:** A forecast can score reasonably on an absolute proper score while adding no demonstrated information beyond a strong external benchmark. Calibration/proper-score quality, benchmark-relative forecast skill, and hypothesis discrimination should therefore be tracked as distinct quantities.

**Why it may transfer:** In any domain with an external baseline, a result can look successful merely because it tracks an already-informative benchmark. Evaluations should ask both “was the forecast probabilistically coherent?” and “did it improve on information already available?”

**Failure/scope condition:** Some domains lack an objective external benchmark; in those settings absolute calibration or internal baseline comparisons may be the only meaningful option. A single market example is not enough to promote the lesson without broader support or a direct cross-domain test.

**Provenance:** `predictions/resolved/P000012.json`; `evaluations/prediction_scores.csv`; model version 0.2.2.
