# Learning Protocol

**Precommitted:** 2026-08-08  
**Purpose:** Define, before sufficient outcomes exist, what will count as evidence that the persistent agent is learning a better predictive world model rather than merely producing new narratives.

## 1. Primary question

Does a later vintage of the persistent market model make better out-of-sample probabilistic forecasts than earlier vintages and fixed simple benchmarks, without achieving apparent improvement by becoming vaguer, changing the scoring rules, using future information, or selectively forgetting failures?

## 2. Unit of evaluation

Every forecast must be created before its outcome, carry an immutable ID and evidence cutoff, specify a resolution rule, and be associated with the model version that generated it. Resolved forecasts remain permanently auditable.

Evaluation is performed separately by target and horizon where sample size permits. Aggregated scores may also be reported, but must not conceal poor subgroups.

## 3. Fixed benchmark families

Where applicable, forecasts are compared against benchmarks fixed independently of the agent's current narrative:

1. Historical unconditional/base-rate forecast.
2. No-change / random-walk forecast.
3. Simple recent-trend forecast.
4. Timestamped external consensus when a stable, auditable consensus series is available.

A benchmark may be added later only with a dated changelog entry; historical comparisons must continue to report the original benchmarks.

## 4. Primary metrics

### Binary/probability forecasts
- Mean Brier score.
- Log loss when probabilities are bounded away from exact 0 and 1.
- Calibration/reliability by probability bins once sample size is adequate.
- Resolution/discrimination: whether probabilities meaningfully differ between events that occur and do not occur.

### Point forecasts
- Mean absolute error.
- Error relative to no-change and other fixed benchmarks.

### Interval forecasts
- Empirical coverage versus nominal coverage.
- Mean interval width / sharpness.
- Coverage must never be interpreted without sharpness: wider intervals are not learning by themselves.

### Ranking forecasts
- Precommitted hit rate or rank score appropriate to the forecast definition.

## 5. Forecast skill

Where a benchmark score is available, report forecast skill in a form such as:

`Skill = 1 - (model loss / benchmark loss)`

Positive skill means the model beats the benchmark under that loss; zero means parity; negative means worse.

No single metric is sufficient to establish learning.

## 6. Model-vintage comparison

The repository must preserve the model version associated with each forecast. Once enough forecasts resolve, compare:

- earliest eligible vintage/window,
- most recent eligible vintage/window,
- lifetime performance,
- fixed benchmarks over the same dates and targets.

Default rolling comparison window: 20 resolved forecasts when at least 40 reasonably comparable forecasts exist. Also report larger windows as the sample grows.

Do not compare windows with materially different target/horizon composition without stratification or an explicit adjustment.

## 7. Minimum evidence thresholds

Before 30 resolved forecasts: **insufficient evidence to assess learning**. Descriptive scores may be reported only.

At 30–49 resolved forecasts: **preliminary learning assessment**. Any conclusion must be explicitly labeled fragile.

At 50+ resolved forecasts: formal vintage/benchmark comparisons begin, subject to target/horizon sample adequacy.

At 100+ resolved forecasts: calibration and subgroup analyses become substantially more informative, though uncertainty remains mandatory.

These thresholds are not declarations of statistical significance; they prevent premature claims from tiny samples.

## 8. Evidence for learning

The agent may report **evidence consistent with learning** only when, over comparable out-of-sample forecasts:

1. Proper scoring performance improves versus earlier vintages; and
2. Performance improves or remains positively skilled versus at least one meaningful fixed benchmark; and
3. Calibration does not materially deteriorate; and
4. Interval sharpness does not deteriorate merely to obtain better coverage; and
5. The improvement persists across more than one evaluation window or is supported by a sufficiently large sample; and
6. The result is not obviously explained by a single favorable regime, target-mix change, data leakage, or scoring-rule change.

Stronger claims require broader and more persistent evidence.

## 9. Evidence against learning

Report **no demonstrated learning** when later vintages fail to improve on earlier vintages or benchmarks after adequate samples.

Report **evidence of deterioration** when later comparable vintages show persistently worse proper scores or calibration, especially after model revisions intended to improve those forecasts.

Failure is a valid experimental result and must not trigger deletion or redefinition of the test.

## 10. Causal learning audit

Prediction accuracy alone does not establish that the causal world model improved. Every material model revision must therefore be linked to:

- the evidence or forecast error motivating it,
- the causal claim changed,
- predictions expected to improve if the change is useful,
- subsequent forecasts generated under the revised claim.

Friday reviews should periodically ask: **Did this model change improve the predictions it was supposed to improve?**

Retrospective causal stories that generated no precommitted discriminating prediction receive no credit as causal learning.

## 11. Anti-Goodhart safeguards

The agent must not improve apparent performance by:

- widening intervals without penalty,
- clustering probabilities near 0.5 solely to avoid large errors,
- dropping difficult targets,
- changing horizons after outcomes,
- excluding failed predictions,
- redefining resolution rules after creation,
- choosing benchmarks after seeing results,
- treating post-outcome explanations as predictions,
- using information published after the forecast evidence cutoff,
- increasing forecast volume with highly correlated trivial predictions to inflate sample size.

Material protocol changes must be prospective, dated, justified, and must not rewrite historical evaluation.

## 12. Regime-change analysis

Markets are nonstationary. Friday and monthly reviews should distinguish:

- model learning,
- temporary regime fit,
- regime change that invalidates old relationships,
- luck/noise.

When enough data exist, report performance by identified regime as well as overall. Regime labels must not be retroactively optimized solely to make performance look better.

## 13. Friday learning report

Every substantive Friday review should include, when data exist:

- total and newly resolved forecast count,
- lifetime score(s),
- recent-window score(s),
- benchmark score(s) and forecast skill,
- calibration summary,
- interval coverage and sharpness,
- best and worst resolved forecast,
- model changes tested by subsequent outcomes,
- evidence for/against learning,
- sample-size warning,
- next highest-information discriminating prediction.

Before the minimum thresholds are reached, explicitly say that learning cannot yet be inferred.

## 14. Long-run success criterion

The proof of concept will be considered successful as a persistent predictive-learning system if later model vintages demonstrate sustained, out-of-sample improvement over early vintages and useful fixed benchmarks while maintaining calibration and forecast sharpness, with an auditable chain connecting at least some improvements to prior prediction errors and explicit model revisions.

Profitability is not the success criterion.

## 15. Scientific integrity rule

If the experiment does not demonstrate learning, record that result plainly. The purpose of this repository is to discover whether persistent model revision works, not to prove in advance that it does.
