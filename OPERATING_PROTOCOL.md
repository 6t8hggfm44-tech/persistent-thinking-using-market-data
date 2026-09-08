# Operating Protocol

## Standard cycle

### Phase 0 — Validation companion initialization
Before domain work, access `6t8hggfm44-tech/market-repo-B` and read its current `VALIDATION_PROTOCOL.md` plus the validation code/configuration required for the present run.

Market Repo B is the required independent statistical-validation companion for this project. The primary repository remains authoritative for forecast creation, timestamps, evidence cutoffs, outcomes, resolution rules, model versions, hypothesis weights, causal-model changes, and the immutable forecast record. Market Repo B must not rewrite or silently repair those primary records.

For every cycle:
- identify the exact primary-repository commit/snapshot being validated;
- use Market Repo B to recompute/check applicable scores and diagnostics from the frozen primary records;
- flag score or provenance discrepancies rather than silently correcting history;
- use only comparable benchmark losses when computing benchmark-relative skill;
- preserve sample sizes, exclusions, target/horizon composition, and uncertainty;
- treat Market Repo B outputs as derived validation results, not as authority to alter a forecast after creation.

If Market Repo B is unavailable, inaccessible, or cannot execute the required validation, record that failure explicitly. The cycle may still preserve objectively due forecast resolutions and genuinely material evidence in the primary repository, but it must not claim validated calibration, forecast skill, benchmark outperformance, or learning until the companion validation is completed.

### Phase 1 — Auditor
Resolve all forecasts whose horizons have expired.

For each:
- collect the objective outcome,
- apply the forecast's precommitted resolution rule,
- calculate the relevant score,
- move/copy the resolved record to `predictions/resolved/`,
- update `evaluations/prediction_scores.csv`,
- make no model changes yet.

After the primary resolution ledger is updated, run the applicable Market Repo B validation against that frozen ledger before interpreting the result. Any discrepancy between primary and independently recomputed scores must be documented and investigated without altering the original forecast content.

### Phase 2 — Evidence intake
Record material new observations since the previous cycle.

For every evidence item include:
- timestamp available to the agent,
- source,
- observation,
- affected variables/hypotheses,
- whether the evidence was expected under each major hypothesis.

### Phase 3 — Skeptic
Attack the current highest-weight hypothesis.
Identify:
- strongest contrary evidence,
- hidden assumptions,
- alternative explanations,
- predictions that would distinguish the leading models.

### Phase 4 — Modeler
Update:
- `world_model/CURRENT_STATE.md`
- `world_model/CAUSAL_GRAPH.md`
- hypothesis weights
- `meta/MODEL_CHANGELOG.md`

The Modeler must explicitly state which resolved forecast errors caused any material update.

Market Repo B may diagnose statistical performance, calibration, target/horizon mix, benchmark skill, regime sensitivity, and whether prior model changes improved subsequent forecasts. It may inform the Modeler's interpretation, but it must not independently rewrite the primary world model or hypothesis weights.

### Phase 5 — Forecaster
Create new forecasts from the *already updated* model.

Every forecast must include:
- unique ID,
- creation timestamp,
- resolution timestamp/horizon,
- target variable,
- point estimate or probability,
- uncertainty interval when applicable,
- benchmark,
- resolution rule,
- model rationale,
- conditions that would count as surprising.

Commit these records before later information is used.

New forecasts are created only in the primary repository. Market Repo B does not create competing forecasts unless a future protocol change explicitly establishes a separately labeled benchmark model prospectively.

### Phase 6 — Validation record
After the primary run is committed, use Market Repo B to record the validation analysis for the exact primary commit/snapshot when there is new resolved data or when the cadence requires a learning/calibration review.

At minimum, as applicable, validate:
- Brier score and log loss for probability forecasts;
- point-error metrics and paired benchmark losses;
- interval coverage and sharpness jointly;
- calibration/reliability with bin counts when sample size permits;
- forecast skill versus frozen comparable benchmarks;
- vintage/subgroup performance by target and horizon where sample size permits;
- uncertainty around aggregate performance;
- anti-Goodhart indicators including probability compression, interval widening, target substitution, duplication/correlation, benchmark switching, and post-hoc regime partitioning;
- whether model changes receive genuine prospective predictive credit or failure evidence.

The validation output must identify both the primary source commit/snapshot and the Market Repo B analysis-code commit.

## Cadence

Recommended POC cadence:
- Weekdays: one post-close cycle for short-horizon forecasts and resolution, with Market Repo B validation whenever forecasts resolve or validation-relevant state changes.
- Friday: expanded weekly model review plus required Market Repo B learning audit and benchmark/vintage comparison.
- Month-end: calibration and model-comparison review with deeper Market Repo B subgroup, uncertainty, regime-sensitivity, and anti-Goodhart analysis.

## Friday learning review
The Friday review must use Market Repo B as the independent statistical-validation layer for all claims about learning, calibration, benchmark outperformance, interval quality, and model-change effectiveness.

It must explicitly compare recent out-of-sample performance with earlier vintages and fixed benchmarks using proper scoring rules, calibration, interval coverage/sharpness, and forecast skill; distinguish genuine improvement from luck, regime change, increased vagueness, target-mix change, or hindsight/model drift; identify which model changes improved or worsened subsequent forecasts; and preserve versioned metrics suitable for longitudinal comparison.

Follow the precommitted learning thresholds in `LEARNING_PROTOCOL.md` and the companion requirements in Market Repo B. Do not promote a favorable p-value, bootstrap interval, short run, or aggregate score into a learning claim when sample size/comparability remains inadequate.

## Benchmarks

At minimum compare against:
- unconditional historical base rate,
- “no change” forecast where applicable,
- simple recent-trend forecast,
- consensus forecast when a timestamped consensus is available.

The AI must beat useful benchmarks, not merely its own earlier prose.

Benchmark-relative statistics produced in Market Repo B are valid only when the benchmark loss uses the same target, horizon, resolution, and loss units as the model forecast. Never pool unlike quantities merely because they occupy the same ledger column.
