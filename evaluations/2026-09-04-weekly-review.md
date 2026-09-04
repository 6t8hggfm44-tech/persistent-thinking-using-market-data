# Weekly Learning Review — 2026-09-04

**Evidence cutoff:** 2026-09-04T17:21:38-04:00  
**Current model after review:** v0.2.14  
**Newly resolved since the prior Friday review:** 3 binary-probability components  
**Lifetime resolved binary-probability components:** 18

## 1. Auditor results this week

All outcomes were resolved and scored under their original rules before post-outcome model revision. No original probability, threshold, interval, benchmark, rationale or surprise condition was rewritten.

- **P000024 — August ISM Manufacturing:** `p(PMI >=55.0)=0.42` resolved **FALSE** at **54.6**. Brier **0.1764**, log loss **0.544727**. Point forecast 54.4 missed by 0.2 and beat the frozen July no-change, current-calendar consensus and FactSet consensus point benchmarks. Interval covered. This is the first positive prospective test of the v0.2.8 regional-to-national manufacturing safeguard, but one result is not learning evidence.
- **P000026 — weekly initial claims:** `p(claims >=215K)=0.23` resolved **FALSE** at **206K**. Brier **0.0529**, log loss **0.261365**. Point forecast 207K missed by 1K, beating no-change, tying the frozen 205K calendar point and losing to the frozen 205.5K four-week-average point. Interval covered. This supports the low-layoff/separation-flow branch.
- **P000025 — August Employment Situation:** `p(payroll <=25K AND unemployment >=4.2%)=0.32` resolved **FALSE** at **+162K payrolls / 4.1% unemployment**. Brier **0.1024**, log loss **0.385662**. The binary probability beat neutral, but the payroll point forecast **missed by 124K**, both frozen external payroll points were closer, and the realized payroll value was outside the -45K to 130K 80% interval. Unemployment was inside its 4.0%-4.4% interval. The forecast's precommitted surprise condition—payrolls >=125K with unemployment <=4.1%—occurred. This is negative out-of-sample evidence for the prior near-term low-hiring-to-net-payroll magnitude mapping.

The three newly resolved probability components have mean **Brier 0.110567** and mean **log loss 0.397251**. That is a strong descriptive week, but it is only three outcomes and all three binary events resolved FALSE. It is not a learning result.

## 2. Lifetime scores and benchmark skill

Across all **18** resolved probability forecasts:

- Mean Brier: **0.209344**
- Mean log loss: **0.608217**
- Neutral-0.50 Brier comparator: **0.250000**
- Descriptive Brier skill vs neutral: **+0.1626**
- Neutral-0.50 log loss: **0.693147**
- Descriptive log-loss skill vs neutral: **+0.1225**

These targets are heterogeneous and dependent. Neutral 0.50 is a fixed comparator, not an empirical base rate and not proof of generalized skill.

### Six-resolution vintage snapshots

Using resolution order rather than retrospectively selected regimes:

- **Earliest 6:** Brier **0.227400**, log loss **0.647876**
- **Middle 6:** Brier **0.222783**, log loss **0.637268**
- **Latest 6:** Brier **0.177850**, log loss **0.539506**

The latest six are numerically better. This is **not enough to infer learning**. The Aug. 28 review showed the opposite short-window pattern at n=15, the target mix has changed materially, several forecasts are correlated, and the latest six contain multiple low-probability FALSE events. The direction of a six-observation comparison is therefore demonstrably unstable.

### S&P point benchmark record

No new S&P point forecast resolved this week. The frozen six-forecast summary therefore remains:

- model MAE **31.465 S&P points**;
- matched no-change MAE **39.957**;
- descriptive point skill vs no-change **+0.2125**.

Across the four S&P forecasts with a frozen recent-trend benchmark, descriptive point skill remains **+0.2566**. No new credit is assigned this week.

### P000025 benchmark lesson

P000025 illustrates why proper-score and magnitude evaluation must remain separate. Its binary probability was useful on the realized FALSE event, but its 38K payroll point was much worse than both frozen external points (45K and 65K). A favorable threshold score therefore does not validate the continuous causal/magnitude model that generated the forecast.

## 3. Calibration, coverage and sharpness

Across all 18 probability forecasts, mean assigned event probability is about **0.4656** while observed event frequency is **6/18 = 0.3333**. The system has assigned more event probability than has occurred so far, but the targets are too heterogeneous and n too small for a stable calibration curve.

Coarse bins:

| Probability bin | n | Mean forecast p | Event frequency |
|---|---:|---:|---:|
| 0.20–0.30 | 1 | 0.230 | 0/1 = 0.000 |
| 0.30–0.40 | 4 | 0.358 | 0/4 = 0.000 |
| 0.40–0.50 | 5 | 0.468 | 1/5 = 0.200 |
| 0.50–0.60 | 8 | 0.548 | 5/8 = 0.625 |

No probability recalibration is justified from these counts.

The previous perfect interval streak is broken. Before P000025, 15 interval-bearing resolved forecast records had all covered. P000025's unemployment interval covered but its payroll interval did not. For the longitudinal record, a multi-component forecast is counted as a record-level hit only when **all** its precommitted component intervals cover; strict record-level coverage is therefore now **15/16 = 93.75%**. Component results remain separately preserved in the resolved record.

This is healthier diagnostically than protecting a 100% coverage streak. It also shows why coverage cannot be read without sharpness. The payroll interval width was 175K, unemployment 0.4 pp, P000026 claims 26K and P000024 PMI 6.5 index points; cross-unit widths are not pooled into a fake aggregate sharpness measure.

## 4. Error diagnosis and model-change audit

### v0.2.7 — labor-flow asymmetry
The broad separation-vs-hiring distinction now has **mixed** prospective evidence:

- P000026 strongly supported the low-layoff leg: initial claims remained 206K.
- P000025 strongly contradicted the stronger near-term implication that weak JOLTS/ADP/hiring signals would produce very weak BLS net payroll growth. Payrolls were +162K and outside the model interval.

The result is a narrower model, not a reversal to treating every labor series as interchangeable. Initial claims still measure separations more directly; JOLTS still measures gross flows; BLS CES net payroll growth is a distinct monthly stock-change measure. v0.2.14 adds an explicit bridge rather than deleting the asynchronous-labor insight.

### v0.2.8 — regional-to-national manufacturing safeguard
P000024 is the first direct post-change national-manufacturing test and performed well both probabilistically and against the frozen point benchmarks. This is **one positive OOS result**, not demonstrated learning. More comparable national-activity forecasts are required.

### v0.2.9 — Treasury announcement versus realized buyback flow
The enlarged realized-flow channel does not begin until Sept. 10 under the repository's prior evidence. No pre-Sept. 10 yield result receives realized-flow credit. The methodological correction still has no direct predictive-learning score.

### v0.2.10 — household/housing weakness
The strong August jobs report is contrary to an immediate generalized downturn but does not erase housing/household weakness. This branch now functions more clearly as a **delayed downside pathway**, not a current labor-collapse claim.

### v0.2.11 — AI investment versus realized productivity
Still no direct productivity discriminator has resolved. Strong investment, semiconductor demand or payroll growth cannot count as productivity proof. **Zero predictive-learning credit remains appropriate.**

### v0.2.13 — Warsh reaction-function state
The Sep. 4 labor result is consistent with the idea that employment does not constrain the Fed from focusing on inflation, but the next decisive test is policy behavior after CPI. P000027 is now the prospective reaction-function test; no credit is assigned before it resolves.

## 5. Material model change: v0.2.14

**Error-linked change:** P000025's precommitted surprise exposed a proxy-to-target bridge failure. The model had correctly separated layoffs from hiring, but then still mapped weak gross-hiring/proxy evidence too directly into a weak monthly net-payroll point estimate.

The revised causal model separates:

- gross hiring flow;
- separation/layoff flow;
- monthly CES net payroll change;
- household employment/unemployment/participation;
- sector composition, survey coverage, timing and seasonal adjustment as bridge variables.

The state description changes from **“low-hire/low-fire”** as a near-term monthly payroll characterization to **“low layoffs + mixed/asynchronous hiring indicators + stronger realized net payroll growth.”** This refinement is recorded in `world_model/CAUSAL_GRAPH.md` and receives **zero learning credit until later forecasts generated under v0.2.14 resolve**.

## 6. Hypothesis-weight review

| Hypothesis | Aug. 28 | Sep. 4 | Change |
|---|---:|---:|---:|
| H001 Soft landing | 0.34 | **0.35** | +0.01 |
| H002 Late-cycle recession | 0.18 | **0.15** | -0.03 |
| H003 Fiscal/inflation regime | 0.36 | **0.38** | +0.02 |
| H004 Productivity boom | 0.12 | **0.12** | 0.00 |

The employment report is strong H002 contrary evidence. It does not cleanly choose H001 over H003. Stable unemployment, higher participation and only 3.1% y/y wage growth support H001; resilient activity combined with renewed energy pressure and a higher expected policy path supports H003. H003 therefore remains the leader, but only by three points.

### Skeptic against H003
The strongest contrary case is that the payroll headline is not itself inflation. Wage growth is moderate, participation improved, gains were sector-concentrated, oil pass-through is uncertain and lagged, and futures pricing is a market opinion rather than a Fed action. One strong payroll release can be revised and does not erase weak housing evidence.

The response is that H003's current lead rests on a **joint state**—resilient labor/services plus energy/input-cost risk plus an inflation-focused reaction function—not on any single endpoint. The Skeptic prevents a larger weight increase and makes core CPI the next necessary discriminator.

## 7. Is the system learning?

**Conclusion: insufficient evidence to assess learning; n=18.** The precommitted protocol forbids even a preliminary learning assessment before **30 resolved forecasts**. The project is only 60% of the way to that threshold, and effective sample size is lower because forecasts are heterogeneous and partly dependent.

Evidence that might tempt an overclaim:

- lifetime Brier/log loss are better than neutral 0.50;
- this week's three probability forecasts scored well;
- the latest six are numerically better than the first and middle six;
- P000024 is a successful first test of an error-linked manufacturing safeguard.

Why this is not yet learning:

- six-outcome windows have already changed sign from one Friday to the next;
- target/horizon composition differs across vintages;
- multiple recent FALSE events reward conservative below-even probabilities;
- neutral 0.50 is not a strong empirical benchmark for every target;
- the labor model has mixed evidence: P000026 helped one branch while P000025 exposed a large magnitude error;
- several important model revisions have not yet generated enough later comparable forecasts;
- calibration bins are sparse and interval sharpness is not yet comparable across targets.

The correct statement remains: **the system is preserving mistakes and making auditable error-linked revisions, while longitudinal out-of-sample improvement has not yet been demonstrated.**

## 8. New forecasts and highest-information discriminator

### Highest-information immediate forecast — P000023
P000023 remains frozen at **54%** probability that first-release **August core CPI is >=0.3% m/m** on Sep. 11, point 0.3%, 80% interval 0.1%-0.4%. It remains the cleanest near-term H001-vs-H003 test. It is not altered by today's jobs report or by any PPI information that arrives before CPI.

### New P000027 — September FOMC hike
From the already-updated v0.2.14 model, P000027 assigns **58%** probability that the FOMC raises both bounds of the federal-funds target range by at least 25 bp at the Sep. 15-16 meeting. Reuters market snapshots at the Sep. 4 cutoff reported approximately **61%** and **58.4%**; both are frozen as external comparators rather than choosing one later. The forecast is deliberately a little less hawkish than the 61% snapshot because wage growth is moderate and CPI remains unresolved.

P000027 is not a duplicate of P000023: CPI tests the inflation state; the FOMC forecast tests the policy reaction mapping after the full data set arrives.

## 9. Transferability review

A new provisional transfer candidate is recorded for Universal review: **coarse-event success can conceal a serious magnitude/distribution miss**. P000025's binary event score was favorable, yet the payroll point missed by 124K and its interval failed. The candidate argues that where a continuous target exists, threshold-probability success should not be allowed to validate the broader magnitude model by itself. This is likely a refinement of existing baseline/proxy-scope safeguards rather than a new universal law, and the Saturday reconciler should decide whether it adds anything genuinely distinct.

## 10. Most important watch

**First-release August core CPI on September 11.** After the strong labor report, immediate recession risk is lower. The highest-information question is whether resilient activity is accompanied by sufficiently benign underlying inflation to favor H001, or whether core inflation stays sticky enough to support H003 and the new P000027 hike probability.
