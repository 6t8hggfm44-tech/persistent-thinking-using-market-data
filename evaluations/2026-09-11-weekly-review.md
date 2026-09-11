# Weekly Learning Review — 2026-09-11

**Evidence cutoff:** 2026-09-11T17:11:19-04:00  
**Timing:** Final Friday post-CPI / post-close review; supersedes the same-day pre-CPI snapshot while preserving it in Git history  
**Current model:** v0.2.14  
**Newly resolved probability components since Sep. 4 review:** 3  
**Lifetime resolved probability components:** 21  
**Learning status:** **INSUFFICIENT EVIDENCE TO ASSESS LEARNING**

## 1. Auditor results since the prior Friday review

All resolutions were scored under frozen rules before post-outcome interpretation. Original forecast content, thresholds, probabilities, intervals, benchmarks, rationales, and surprise conditions were preserved.

### Probability-bearing resolutions

- **P000003 — one-month S&P 500:** p(up)=0.54 resolved **FALSE** at 7,673.52. Brier **0.2916**, log loss **0.776529**. Point estimate 7,820 missed by **146.48** index points versus **84.12** for frozen no-change. The 80% interval covered. Negative probability and point evidence without a tail miss.
- **P000028 — August final-demand PPI:** p(PPI >=0.4% m/m)=0.53 resolved **TRUE** exactly at **0.4%**. Brier **0.2209**, log loss **0.634878**. Point error **0.0 pp**, exactly tying the frozen external-consensus point of 0.4%; frozen no-change missed by 0.4 pp. Interval covered. Proper-score success does not establish point information beyond consensus.
- **P000023 — August core CPI:** p(core CPI >=0.3% m/m)=0.54 resolved **TRUE exactly at 0.3%**. Brier **0.2116**, log loss **0.616186**. Point error **0.0 pp**, beating frozen July no-change (0.1 pp error) and frozen June-July mean (0.2 pp error). The 0.1%-0.4% interval covered. A later Reuters consensus of 0.2% is not retrofitted because no stable timestamped consensus was frozen at the Aug. 28 forecast cutoff.

The three probability resolutions added since Sep. 4 average **Brier 0.241367** and **log loss 0.675864**, only modestly better than neutral-0.50 losses of 0.25 and 0.693147. Three observations remain far too few for inference.

### Non-probability / ranking resolutions this week

- **P000006 — one-month 10-year Treasury:** 4.80% outcome; point error **18 bp** versus **16 bp** frozen no-change; interval covered.
- **P000007 — one-month WTI:** $93.03 outcome; point error **$15.03** versus **$14.85** frozen no-change; the $68-$91 80% interval **missed**.
- **P000009 — one-month sector leadership:** Information Technology failed to finish top three under the frozen proxy resolution; categorical miss.
- **P000008 — one-month HY OAS:** 2.67% outcome; point error **0.38 pp** versus **0.17 pp** for the explicitly stale frozen baseline; interval covered.

The Aug. 8 one-month batch remains materially weak on point/ranking benchmarks. That negative batch is preserved alongside the probability aggregate.

## 2. Lifetime proper scores and fixed neutral benchmark

Across **21** resolved probability forecasts:

- Mean Brier: **0.213919**
- Mean log loss: **0.617880**
- Neutral-0.50 Brier: **0.250000**
- Descriptive Brier skill vs neutral: **+0.1443**
- Neutral-0.50 log loss: **0.693147**
- Descriptive log-loss skill vs neutral: **+0.1086**

Market Repo B's deterministic iid bootstrap, 20,000 resamples, gives descriptive 95% intervals of approximately:

- mean Brier: **0.1827 to 0.2438**
- Brier skill vs neutral: **+0.0249 to +0.2690**
- mean log loss: **0.5526 to 0.6798**
- log-loss skill vs neutral: **+0.0193 to +0.2027**

These intervals are **not** formal learning evidence. Forecasts are heterogeneous and dependent, share macro shocks and causal ancestry, and often target different quantities/horizons. Neutral 0.50 is also not the strongest empirical benchmark for every target.

## 3. Vintage comparison: is recent performance actually better?

### Equal 10-resolution windows

- **First 10:** Brier **0.214740**, log loss **0.621654**
- **Last 10:** Brier **0.210480**, log loss **0.608561**
- Last-minus-first Brier difference: **-0.004260**
- Last-minus-first log-loss difference: **-0.013093**

A descriptive iid bootstrap that resamples the windows separately gives roughly:

- Brier difference 95% interval: **-0.0698 to +0.0589**
- log-loss difference 95% interval: **-0.1510 to +0.1178**

The intervals comfortably include meaningful improvement and deterioration. Target/horizon composition also differs, so this is not a clean causal estimate of learning.

### Six-resolution snapshots

- Earliest 6: Brier **0.227400**, log loss **0.647876**
- Latest 6: Brier **0.175967**, log loss **0.536558**

The latest six are numerically better, but small six-resolution windows have already reversed direction across previous reviews. The newest window also mixes claims, payroll, one-month equities, PPI, and CPI. It remains descriptive only.

### Conclusion on vintages

There is still **no stable longitudinal learning pattern**. The broadest equal-count comparison is only modestly favorable and highly uncertain; the visually stronger six-outcome comparison is too small and composition-sensitive to override that.

## 4. Calibration and discrimination

Across 21 probability forecasts:

- mean assigned event probability: **47.57%**
- observed event frequency: **38.10% (8/21)**
- aggregate forecast-minus-frequency gap: **+9.48 percentage points**
- mean probability when the event occurred: **52.75%**
- mean probability when the event did not occur: **44.38%**

The 8.37-point event/non-event probability separation is descriptively consistent with some discrimination but is not stable calibration evidence at n=21.

Coarse fixed bins:

| Probability bin | n | Mean p | Event frequency |
|---|---:|---:|---:|
| 0.20-0.30 | 1 | 0.230 | 0.000 |
| 0.30-0.40 | 4 | 0.358 | 0.000 |
| 0.40-0.50 | 5 | 0.468 | 0.200 |
| 0.50-0.60 | 11 | 0.545 | 0.636 |

Counts remain too sparse for a recalibration rule.

## 5. Interval coverage and sharpness

Strict record-level 80% interval coverage is now **20/22 = 90.91%** among resolved records with explicit interval outcomes. P000007 WTI and P000025's multi-component labor forecast remain the two strict misses; P000023 covered.

Coverage above the nominal 80% rate is not automatically success. The system may be conservative. Raw interval widths cannot be pooled because units differ radically, and no claim of improved sharpness is made. No interval was widened after seeing an outcome.

## 6. Point-forecast benchmark audit

### S&P 500 matched no-change record

The seven resolved S&P point forecasts still have:

- model MAE: **47.896 index points**
- matched no-change MAE: **46.266 points**
- point skill vs no-change: **-0.0352**

This remains negative after P000003's one-month miss. The four S&P forecasts with a frozen recent-trend benchmark still show positive descriptive skill, but no recent-trend benchmark is retrofitted to P000003.

### P000028 PPI

The model's 0.4% point exactly tied the frozen 0.4% external consensus. It earns no demonstrated added-information credit versus that consensus.

### P000023 core CPI

The 0.3% point exactly matched the outcome and beat both frozen recent-observation baselines. Reuters later reported a 0.2% economist consensus, but because it was not frozen at the forecast cutoff it is contextual only and receives no benchmark status.

### One-month batch warning

P000003, P000006, P000007, and P000008 lost their relevant point comparisons; P000009 missed its categorical target. This cluster remains negative evidence about broad one-month predictive accuracy and is not averaged away by the probability ledger.

## 7. Model-change attribution

### v0.2.8 — regional-to-national manufacturing bridge

P000024 remains the sole direct post-change national-manufacturing test and was positive: 54.4 forecast versus 54.6 actual, outperforming frozen point benchmarks. **One direct success remains insufficient for learning credit.**

### v0.2.13 — inflation/policy discriminator

P000023 is one modest positive prospective test. The >=0.3% core-CPI event occurred and the point beat frozen simple recent-observation baselines. But the realization was exactly the event threshold rather than the >=0.5% precommitted strong-persistence surprise, and no stable external consensus was frozen. **Positive evidence is recorded, but broad causal-learning credit is not.**

### v0.2.14 — labor measurement bridge

No later monthly payroll forecast generated under v0.2.14 has resolved. Claims test separation flow, not the monthly CES net-payroll magnitude the bridge was designed to improve. **Predictive-learning credit remains zero.**

### Treasury announcement vs realized-flow distinction

Long yields remain high after enlarged buybacks entered their realized-flow phase, but concurrent inflation, oil, policy expectations, deficits and duration supply prevent causal identification. **No predictive-learning credit is assigned.**

No model revision yet shows repeated, benchmark-relative improvement in the forecasts it was meant to improve.

## 8. Post-cutoff evidence and hypothesis review

After P000023 was scored, the model admitted only information first available after the Sep. 10 17:41 ET cutoff:

- BLS: headline CPI +0.4% m/m / +3.4% y/y; core +0.3% m/m / +2.4% y/y; energy +2.1%, gasoline +3.9%, shelter +0.3%.
- University of Michigan: preliminary September sentiment **47.8**, Current Conditions 50.9, Expectations 45.8; Reuters reported one-year inflation expectations **4.6%** and five-year expectations **3.4%**.
- Reuters: Brent **$104.61** and WTI **$100.05**, lower Friday but up more than 8% on the week.
- Reuters: S&P 500 **7,656.98 (+0.86%)**; market-implied Sep. 16 hike probability nearly **90%**; 10-year yield briefly near 5%.

**INFERENCE:** P000023 and higher inflation expectations directionally support H003, while weak sentiment and the contractionary side of the energy/rate shock preserve H002/H001 alternatives. Market prices and Fed odds are downstream beliefs and share causal ancestry with the CPI/energy state, so they are not independent confirmations.

Weights remain:

| Hypothesis | Sep. 4 | Sep. 11 final | Change |
|---|---:|---:|---:|
| H001 Soft landing | 0.35 | **0.35** | 0.00 |
| H002 Late-cycle recession | 0.15 | **0.15** | 0.00 |
| H003 Fiscal/inflation regime | 0.38 | **0.38** | 0.00 |
| H004 Productivity boom | 0.12 | **0.12** | 0.00 |

The Skeptic blocks reweighting because the core result was threshold-adjacent, core y/y eased, headline inflation was energy-heavy, sentiment weakened sharply, and the same energy shock can raise prices while damaging real demand. Coarse one-point changes would imply more precision than this joint evidence warrants.

## 9. Is the system learning?

**No learning claim is permitted: n=21, below the precommitted threshold of 30.** Effective sample size is lower because forecasts are heterogeneous and correlated.

Evidence that could superficially look positive:

- lifetime Brier/log loss beat neutral 0.50 descriptively;
- latest-six scores are numerically better than earliest-six;
- P000024 is one successful prospective test of the manufacturing safeguard;
- P000023 is one modest positive prospective inflation-state discriminator;
- probability assignments are somewhat higher on realized events than non-events.

Evidence against claiming improvement:

- first 10 versus last 10 proper scores remain close with wide uncertainty;
- the three probability resolutions added since Sep. 4 are only modestly better than neutral as a group;
- S&P point skill versus no-change is slightly negative;
- the one-month Aug. 8 batch broadly underperformed point/ranking benchmarks;
- interval coverage remains above nominal and sharpness cannot yet be compared cleanly;
- small recent windows have repeatedly changed direction;
- v0.2.14's key labor-bridge correction has not yet received a direct post-change payroll test;
- neutral 0.50 is not a strong target-specific benchmark and cannot substitute for external consensus/no-change where those exist;
- shared macro shocks and overlapping targets reduce independence.

**Assessment:** the experiment demonstrates disciplined error preservation and prospective self-correction, but **longitudinal out-of-sample predictive improvement has not been demonstrated**. This remains exactly the distinction required by the Universal longitudinal-learning safeguard.

## 10. Highest-information discriminating forecast and new forecasts

**P000027 is now the highest-information discriminator.** It remains frozen at **58%** probability that the FOMC raises both bounds of the federal-funds target range by at least 25 bp at the Sep. 15-16 meeting. Today's near-90% market-implied probability is post-forecast evidence and does not rewrite P000027.

**No new forecast is issued.** A new FOMC/rates call after CPI would be highly correlated with P000027 and would inflate nominal n. No unrelated near-term target has enough discriminating value at this cutoff to justify manufacturing activity.

P000004 (three-month S&P) and P000005 (one-year S&P) also remain unresolved under their original rules.

## 11. Transferability review

No new Universal transfer candidate is added. The key lessons from this cycle are already covered by existing safeguards: longitudinal OOS evidence before learning claims, baseline-relative attribution, coarse-event versus magnitude separation, ambiguous downstream endpoints, and causal-ancestry/pseudo-replication controls. Duplicating them would not add independent evidence.

## 12. Most important watch

**The Sep. 16 FOMC decision resolving P000027.** It is the next frozen test of whether the model's inflation/policy-constraint state maps into actual policy action rather than merely market repricing.
