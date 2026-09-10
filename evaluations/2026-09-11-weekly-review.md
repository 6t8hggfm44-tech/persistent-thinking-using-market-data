# Weekly Learning Review — 2026-09-11

**Evidence cutoff:** 2026-09-10T17:41:18-04:00  
**Timing:** Friday review run before the scheduled Sep. 11 08:30 ET CPI release  
**Current model:** v0.2.14  
**Newly resolved probability components since Sep. 4 review:** 2  
**Lifetime resolved probability components:** 20  
**Learning status:** **INSUFFICIENT EVIDENCE TO ASSESS LEARNING**

## 1. Auditor results since the prior Friday review

All resolutions were scored under their frozen rules before post-outcome interpretation. Original forecast content, thresholds, probabilities, intervals, benchmarks, rationales, and surprise conditions were preserved.

### Probability-bearing resolutions

- **P000003 — one-month S&P 500:** p(up)=0.54 resolved **FALSE** at 7,673.52. Brier **0.2916**, log loss **0.776529**. Point estimate 7,820 missed by **146.48** index points versus **84.12** for frozen no-change. The 80% interval covered. This is negative out-of-sample probability and point evidence without a tail miss.
- **P000028 — August final-demand PPI:** p(PPI >=0.4% m/m)=0.53 resolved **TRUE** exactly at **0.4%**. Brier **0.2209**, log loss **0.634878**. Point error **0.0 pp**, exactly tying the frozen external-consensus point of 0.4%; the frozen no-change 0.0% point missed by 0.4 pp. The 80% interval covered. This is a modest proper-score success versus neutral but **not demonstrated point information beyond consensus**.

The two newly resolved probability components have mean **Brier 0.256250** and mean **log loss 0.705704**, slightly worse than neutral-0.50 losses of 0.250000 and 0.693147. Two observations are far too few for inference, but the current week's additions do not support a simple monotonic-learning story.

### Non-probability / ranking resolutions

- **P000006 — one-month 10-year Treasury:** 4.80% outcome; point error **18 bp** versus **16 bp** frozen no-change; interval covered.
- **P000007 — one-month WTI:** $93.03 outcome; point error **$15.03** versus **$14.85** frozen no-change; the $68-$91 80% interval **missed**. The tail miss is preserved.
- **P000009 — one-month sector leadership:** Information Technology failed to finish top three under the frozen proxy resolution; categorical miss.
- **P000008 — one-month HY OAS:** 2.67% outcome; point error **0.38 pp** versus **0.17 pp** for the explicitly stale frozen baseline; interval covered.

Taken together, the one-month Aug. 8 forecast batch was weak on point/ranking performance: SPX, 10-year yield, WTI, HY OAS, and sector leadership all failed to beat or satisfy their relevant point/ranking comparator, although most intervals covered. This is important negative evidence against interpreting earlier short-horizon successes as broad model skill.

## 2. Lifetime proper scores and fixed neutral benchmark

Across **20** resolved probability forecasts:

- Mean Brier: **0.214035**
- Mean log loss: **0.617965**
- Neutral-0.50 Brier: **0.250000**
- Descriptive Brier skill vs neutral: **+0.1439**
- Neutral-0.50 log loss: **0.693147**
- Descriptive log-loss skill vs neutral: **+0.1085**

An iid bootstrap with 20,000 resamples gives descriptive 95% intervals of approximately:

- mean Brier: **0.1809 to 0.2456**
- Brier skill vs neutral: **+0.0175 to +0.2765**
- mean log loss: **0.5485 to 0.6833**
- log-loss skill vs neutral: **+0.0142 to +0.2087**

These intervals are **not** formal evidence of learning. Forecasts are heterogeneous, partly dependent, and often share macro releases or market states; neutral 0.50 is also not the strongest empirical benchmark for every target. The bootstrap therefore describes the ledger but likely overstates effective independent information.

## 3. Vintage comparison: is recent performance actually better?

### Equal 10-resolution windows

- **First 10:** Brier **0.214740**, log loss **0.621654**
- **Last 10:** Brier **0.213330**, log loss **0.614277**

The last 10 improve by only **0.00141 Brier** and **0.00738 log-loss** points — effectively parity at this sample size. A descriptive independent-window iid bootstrap for last-minus-first gives roughly:

- Brier difference 95% interval: **-0.0671 to +0.0610**
- log-loss difference 95% interval: **-0.1447 to +0.1222**

The intervals easily include substantial improvement and deterioration. More importantly, the target/horizon mix differs across the windows, so even these uncertainty ranges are not clean causal estimates of learning.

### Six-resolution snapshots

- Earliest 6: Brier **0.227400**, log loss **0.647876**
- Middle 6: Brier **0.222783**, log loss **0.637268**
- Latest 6: Brier **0.187517**, log loss **0.559697**

The latest six remain numerically better than the earliest six, but this statistic has already changed direction across prior Friday reviews as only a few outcomes entered or left the window. It therefore remains an unstable descriptive slice, not a learning measure.

### Conclusion on vintages

There is **no consistent monotonic improvement** visible yet. The broadest equal-count comparison available, first 10 versus last 10, is essentially flat. The recent-six improvement is too small-sample, target-mix-sensitive, and historically unstable to override that result.

## 4. Calibration and discrimination

Across 20 probability forecasts:

- mean assigned event probability: **47.25%**
- observed event frequency: **35.00% (7/20)**
- aggregate forecast-minus-frequency gap: **+12.25 percentage points**
- mean probability when the event occurred: **52.57%**
- mean probability when the event did not occur: **44.38%**

The latter 8.19-point separation is descriptively consistent with some discrimination, but n is too small and targets are too heterogeneous for a stable calibration claim.

Coarse fixed bins:

| Probability bin | n | Mean p | Event frequency |
|---|---:|---:|---:|
| 0.20-0.30 | 1 | 0.230 | 0.000 |
| 0.30-0.40 | 4 | 0.358 | 0.000 |
| 0.40-0.50 | 5 | 0.468 | 0.200 |
| 0.50-0.60 | 10 | 0.545 | 0.600 |

The lower-probability bins have realized fewer events than assigned so far, while the >0.50 bin is close in the opposite direction. Counts are too sparse to justify recalibration.

## 5. Interval coverage and sharpness

Strict record-level 80% interval coverage is now **19/21 = 90.48%** among resolved records with explicit interval outcomes. P000007 WTI and P000025's multi-component labor forecast are the two strict misses; P000028 covered.

Coverage above the nominal 80% rate is not automatically a success. The system may still be conservative. Cross-target interval widths cannot be pooled because units differ radically (index points, yields, dollars/barrel, jobs, percentages, PMI points). No claim of improved sharpness is made. P000028's interval width remained frozen at **1.1 percentage points**; no interval was widened after seeing an outcome.

## 6. Point-forecast benchmark audit

### S&P 500 matched no-change record

After adding the one-month P000003 resolution, the seven resolved S&P point forecasts have:

- model MAE: **47.896 index points**
- matched no-change MAE: **46.266 points**
- point skill vs no-change: **-0.0352**

This is a meaningful deterioration from the +0.2125 descriptive no-change skill reported on Sep. 4. One long-horizon miss erased the prior aggregate advantage. The four S&P forecasts carrying a frozen recent-trend benchmark still show +0.2566 descriptive skill versus that comparator, but P000003 had no comparable frozen recent-trend benchmark and is not retrofitted with one.

### P000028 PPI

The model's 0.4% point exactly tied the frozen 0.4% external consensus. It beat the 0.0% no-change point, but **adds no demonstrated point information beyond consensus**. Its favorable binary proper score is evaluated separately from point benchmark information.

### One-month batch warning

P000003, P000006, P000007, and P000008 all lost to their frozen no-change/latest point comparators; P000009 missed its categorical target. This cluster is negative evidence about broad one-month predictive accuracy and should not be averaged away by the probability ledger.

## 7. Model-change attribution

### v0.2.8 — regional-to-national manufacturing bridge

P000024 remains the sole direct post-change national-manufacturing test and was positive: 54.4 forecast versus 54.6 actual, outperforming frozen point benchmarks. **One direct success remains insufficient for learning credit.**

### v0.2.14 — labor measurement bridge

The revision was motivated by P000025's 124K payroll miss and explicitly separated gross hiring, separations, CES net payroll change, household employment, and timing/composition. No later **monthly payroll** forecast generated under v0.2.14 has yet resolved. Sep. 10 claims at 206K support only the low-separation leg and therefore do not validate the revised payroll bridge. **Predictive-learning credit remains zero.**

### v0.2.9 — Treasury announcement vs realized buyback flow

The enlarged buyback program is now in its realized-flow phase. Long yields rose despite the Sep. 10 operation, which is qualitatively consistent with the existing claim that liquidity-support buybacks need not dominate structural duration/inflation pressure. But no isolated, precommitted causal forecast attributes the same-day yield move to the buyback, and concurrent PPI, oil, policy pricing, deficits and duration supply prevent causal credit. **No predictive-learning credit is assigned.**

### Other changes

The household/housing branch remains a delayed downside pathway after August existing-home sales fell to a 14-month low. The AI-investment/productivity distinction still has no direct productivity discriminator. No structural model change is warranted from this week's outcomes.

## 8. Hypothesis-weight review and Skeptic

Weights remain:

| Hypothesis | Sep. 4 | Sep. 11 review | Change |
|---|---:|---:|---:|
| H001 Soft landing | 0.35 | **0.35** | 0.00 |
| H002 Late-cycle recession | 0.15 | **0.15** | 0.00 |
| H003 Fiscal/inflation regime | 0.38 | **0.38** | 0.00 |
| H004 Productivity boom | 0.12 | **0.12** | 0.00 |

H003 remains the narrow leader because resilient labor, firm producer prices, renewed energy stress, higher long yields and firmer hike pricing fit its policy-constraint state. The Skeptic blocks an upgrade because PPI merely matched consensus and was energy-heavy, housing remains weak, oil can reduce real demand, market prices are downstream beliefs, and the higher-information core-CPI discriminator is still pending. Reweighting aggressively hours before that frozen test would invite vivid-event overfitting.

## 9. Is the system learning?

**No learning claim is permitted: n=20, below the precommitted threshold of 30.** Effective sample size is smaller because forecasts are heterogeneous and correlated.

Evidence that could superficially look positive:

- lifetime Brier/log loss beat neutral 0.50;
- latest-six scores are numerically better than early-six scores;
- P000024 is one successful prospective test of an error-linked manufacturing safeguard;
- probability assignments are somewhat higher on realized events than non-events.

Evidence against claiming improvement:

- first 10 versus last 10 proper scores are essentially unchanged;
- the two probability resolutions added since Sep. 4 are slightly worse than neutral as a pair;
- S&P point skill versus no-change has moved from positive to slightly negative after P000003 resolved;
- the one-month Aug. 8 batch broadly underperformed its point/ranking benchmarks;
- interval coverage remains above nominal and sharpness cannot yet be compared cleanly, so vagueness/conservatism remains a live alternative explanation;
- recent windows have repeatedly changed direction as a few outcomes enter or leave;
- v0.2.14's key labor-bridge correction has not yet received a direct post-change payroll test;
- neutral 0.50 is not a strong target-specific benchmark and cannot substitute for external consensus/no-change where those exist;
- shared macro shocks and overlapping targets reduce independence.

**Assessment:** The experiment continues to demonstrate auditable self-correction and preservation of failure, but **longitudinal out-of-sample predictive improvement has not been demonstrated**. This week's broader evidence is actually useful because it weakens the temptation to infer learning from the favorable Sep. 4 snapshot.

## 10. Highest-information discriminating forecast and new forecasts

**P000023 remains the highest-information discriminator.** It is frozen at 54% probability that first-release August core CPI is >=0.3% m/m, point 0.3%, 80% interval 0.1%-0.4%, resolving Sep. 11 at 08:30 ET. It directly separates H001's benign-disinflation path from H003's underlying-inflation/policy-constraint path better than the energy-heavy PPI headline.

**No new forecast is issued.** P000023 resolves within hours of this cutoff and P000027 remains frozen for the Sep. 16 FOMC decision. Adding another highly correlated pre-CPI inflation or rate forecast would inflate activity and nominal sample size without enough independent information.

Longer-horizon P000004 (three-month S&P) and P000005 (one-year S&P) also remain unresolved under their original rules.

## 11. Transferability review

No new Universal transfer candidate is added. This week's lessons are already covered by TC-2026-001/003 and Universal safeguards on baseline-relative attribution, coarse-event versus magnitude evaluation, ambiguous downstream endpoints, and longitudinal out-of-sample learning. Writing a duplicate candidate would create pseudo-replication rather than genuinely new transferable evidence.

## 12. Most important watch

**August core CPI at 08:30 ET on Sep. 11.** The key question is whether underlying consumer inflation stays benign enough to preserve H001 despite the energy shock, or prints firmly enough to strengthen H003's policy-constraint interpretation before P000027 resolves at the Sep. 16 FOMC decision.
