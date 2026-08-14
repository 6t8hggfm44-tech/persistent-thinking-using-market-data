# Transfer Candidates for Universal Review

These are provisional lessons surfaced by the market experiment. They are not universal truth and should be evaluated by the Universal reconciler under `UNIVERSAL_CONSTITUTION.md`.

## TC-2026-001 — Proper-score success is not the same as benchmark-relative information

**Status:** Provisional; one clean live example.

**Observation:** P000012 assigned 0.55 probability to July 2026 headline CPI being <=3.4% YoY. The event resolved true and received a favorable Brier/log score, but 3.4% was also the timestamped published consensus point and the first-release outcome was exactly 3.4%.

**Methodological inference:** A forecast can score reasonably on an absolute proper score while adding no demonstrated information beyond a strong external benchmark. Calibration/proper-score quality, benchmark-relative forecast skill, and hypothesis discrimination should therefore be tracked as distinct quantities.

**Why it may transfer:** In any domain with an external baseline, a result can look successful merely because it tracks an already-informative benchmark. Evaluations should ask both “was the forecast probabilistically coherent?” and “did it improve on information already available?”

**Failure/scope condition:** Some domains lack an objective external benchmark; in those settings absolute calibration or internal baseline comparisons may be the only meaningful option. A single market example is not enough to promote the lesson without broader support or a direct cross-domain test.

**Provenance:** `predictions/resolved/P000012.json`; `evaluations/prediction_scores.csv`; model version 0.2.2.

## TC-2026-002 — Opposing causal channels make a single downstream response weakly identifying

**Status:** Provisional; surfaced in the Aug. 14 consumer-demand review.

**Observation:** Unexpectedly weak July retail/control-group sales plausibly reduced expected earnings/cash flows while also lowering the expected policy path and Treasury yields. The S&P 500 therefore could remain resilient even if underlying demand weakened, because the cash-flow and discount-rate channels have opposing signs.

**Methodological inference:** When the same upstream observation reaches an outcome through multiple causal paths with opposing effects, the net downstream response is a weak discriminator among hypotheses. Prefer joint or intermediate measurements that separately expose the competing paths rather than inferring the cause from one aggregate endpoint.

**Why it may transfer:** This identification problem occurs outside markets whenever different mechanisms can cancel at a measured output—for example, physical systems with compensating effects, policy interventions with offsetting channels, or textual/historical evidence where multiple source processes generate the same surface feature.

**Failure/scope condition:** The lesson applies only when there is a defensible causal reason to expect opposing paths. Inventing extra pathways after an outcome would itself be hindsight assimilation. The competing channels and preferred discriminating measurements should be stated prospectively where possible.

**Provenance:** `evidence/2026-08-14-weekly-cycle.md`; `world_model/CAUSAL_GRAPH.md`; `evaluations/2026-08-14-weekly-review.md`; model version 0.2.3.
