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

## TC-2026-003 — Coarse-event success can conceal a magnitude/distribution miss

**Status:** Provisional; one live market example; likely refinement of existing Universal baseline/proxy-scope safeguards.

**Observation:** P000025 assigned 0.32 probability to the joint event that August first-release payroll growth would be <=25K and unemployment >=4.2%. The event resolved FALSE at +162K / 4.1%, so the probability earned a favorable Brier score of 0.1024. But the forecast's continuous payroll point was only 38K, missed by 124K, lost to both frozen external payroll points, and the realized payroll value lay outside the -45K to 130K 80% interval. The forecast's precommitted strong-labor surprise condition also occurred.

**Methodological inference:** Success on a thresholded/classification projection of a forecast should not automatically validate the underlying magnitude or distribution model. When a continuous target exists, preserve and score both the event probability and the magnitude/interval forecast; a coarse event can resolve correctly for many values that are far from the model's central expectation.

**Why it may transfer:** The same issue occurs in risk classification, scientific threshold tests, medical/engineering alarms, policy triggers, and decision systems. A model can correctly classify “above/below threshold” while substantially misestimating how far from the threshold the system actually is, which can matter for causal interpretation and downstream decisions.

**Failure/scope condition:** Not every binary forecast has a meaningful continuous latent target, and adding artificial point estimates merely to create another metric would be counterproductive. The lesson applies when the continuous magnitude is already part of the model or materially affects interpretation.

**Expected behavioral change:** Where practical, score the coarsened event and the underlying continuous forecast separately, and do not grant causal/model-learning credit from the event score when the magnitude forecast fails badly. Preserve precommitted surprise conditions as an additional check against this form of false reassurance.

**Provenance:** `predictions/resolved/P000025.json`; `evaluations/2026-09-04-weekly-review.md`; model version 0.2.14.

## TC-2026-004 — Register schema compatibility before calling a model validation complete

**Status:** Provisional; diagnosed from one concrete frozen Market source/companion adapter mismatch, no prospective error-rate test yet.

**OBSERVATION:** First-release October payroll P000034 was prospectively registered in `predictions/open/P000034.json` with `forecast.point_estimate_jobs` and `forecast.interval_80_jobs`; after resolution its immutable raw forecast and append-only ledger support direct proper-score/point/coverage calculations. However the current Market Repo B `src/structured_diagnostics.py` adapter (source `39f7e921bdaa3428bf88fe6d2b9d51a533d05fbb`) expects `point_estimate` with `lower_80/upper_80` for scalar outcomes or specifically `nonfarm_payroll_point`/`nonfarm_payroll_lower_80`/`nonfarm_payroll_upper_80` for joint components. The existing P000034 shape is not covered. A correct binary score ledger thus does not prove successful point/interval validation. No native full-checkout test was executed during this Friday cycle, so the directly identified code/schema mismatch is a **static compatibility finding** rather than a claimed observed validator-run error.

**INFERENCE / transfer proposal:** Before committing a newly registered structured forecast, check the validator's read-only schema contract against each forecast dimension (binary, magnitude, interval, frozen benchmark). Missing adapter support should be flagged while original forecast content remains immutable; repairs occur prospectively in the companion adapter with regression fixtures, never by editing old predictions. This transfers to any versioned system where a producer can emit apparently valid records that a downstream checker cannot fully interpret.

**Falsifiable test:** Seed frozen forecast records with supported and unsupported alternate schema paths; compare pre-registration contract checks versus ordinary score-only review on previously undetected validation blind spots, false rejects and net maintenance cost. Distinguish parser coverage from correct outcomes. Role separation alone cannot establish epistemic independence. **Scope/break point:** heterogeneous freeform forecasts can be valuable and stricter schemas may block novel useful tests; provide explicit adapters and defer only claims requiring unsupported fields, not the whole event record.

**Provenance:** `predictions/resolved/P000034.json`; `evaluations/2026-11-06-auditor.md`; Market Repo B `src/structured_diagnostics.py` at `39f7e921bdaa3428bf88fe6d2b9d51a533d05fbb`. Universal FM-002/FM-007/FM-009 already cover adjacent layer/scope/transition risks. Candidate only for Saturday reconciler; no direct Universal write.

### November 13, 2026 corroboration — P000036, not a new lesson ID

**OBSERVATION:** The newly resolved first-release October core-core PPI P000036 used `ppi_ex_food_energy_trade_sa_mom_percent` in its valid primary outcome, while the frozen Repo B structured adapter's scalar `OUTCOME_KEYS` (as inspected at code commit `19ae50f35454e6c051f409235c1433442ade5188`) did **not** include that field. The binary p=.44 event TRUE was arithmetically verifiable and the PPI point +.4% versus +.5% was directly scored, but the existing generic companion adapter cannot automatically treat this as validated scalar point/interval coverage. The previously recorded P000034 variant is another **schema shape**, not a prospective independent proof of the gate's efficacy. Do not repair primary forecasts. Candidate TC-2026-004's proposed pre-registration adapter acceptance test remains **unrun**. This is a dated refinement suitable for Saturday Universal evaluation, not direct Universal truth.
