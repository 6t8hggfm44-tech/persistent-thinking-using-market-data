# Operating Protocol

## Standard cycle

### Phase 1 — Auditor
Resolve all forecasts whose horizons have expired.

For each:
- collect the objective outcome,
- apply the forecast's precommitted resolution rule,
- calculate the relevant score,
- move/copy the resolved record to `predictions/resolved/`,
- update `evaluations/prediction_scores.csv`,
- make no model changes yet.

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

## Cadence

Recommended POC cadence:
- Weekdays: one post-close cycle for short-horizon forecasts and resolution.
- Friday: expanded weekly model review.
- Month-end: calibration and model-comparison review.

## Benchmarks

At minimum compare against:
- unconditional historical base rate,
- “no change” forecast where applicable,
- simple recent-trend forecast,
- consensus forecast when a timestamped consensus is available.

The AI must beat useful benchmarks, not merely its own earlier prose.
