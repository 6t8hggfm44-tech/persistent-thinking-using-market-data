# Weekly Learning Review — 2026-08-21

**Evidence cutoff:** 2026-08-21T17:24:57-04:00  
**Current model after review:** v0.2.8  
**Newly resolved this week:** 6 binary-probability components  
**Lifetime resolved binary-probability components:** 12

## 1. Auditor results this cycle

Scoring was completed before post-Aug. 20 evidence intake and model revision.

- **P000014:** one-week S&P distribution from Aug. 14 to Aug. 21. p(up)=0.49 resolved FALSE at **7,674.37**. Brier **0.2401**; log loss **0.673345**; point MAE **105.63**; 80% interval hit. The point forecast modestly beat no-change MAE **111.39** and recent-trend MAE **139.51**.
- **P000019:** August flash U.S. Manufacturing PMI. p(PMI>=54.0)=0.56 resolved FALSE at **53.2**. Brier **0.3136**; log loss **0.820981**; point MAE **1.0**; 80% interval hit. It lost to the frozen 53.7 consensus point benchmark (**0.5** MAE), the 53.9 July no-change benchmark (**0.7** MAE), and neutral binary Brier 0.25.

No historical forecast content, benchmark, or resolution rule was changed.

## 2. Lifetime proper scores and benchmark skill

Across all **12** resolved binary-probability components:

- Mean Brier: **0.225092**
- Mean log loss: **0.642572**
- Descriptive neutral-0.50 Brier comparator: **0.250000**
- Descriptive Brier skill vs neutral: **+0.0996**
- Neutral-0.50 log loss: **0.693147**
- Descriptive log-loss skill vs neutral: **+0.0730**

These are heterogeneous targets, so the aggregate neutral comparison is descriptive rather than a proof of transferable forecasting skill.

### S&P point forecasts

Across six resolved S&P point forecasts:

- Mean model MAE: **31.465 points**
- Mean matched no-change MAE: **39.957 points**
- Descriptive MAE skill vs no-change: **+0.2125**

Across the four S&P forecasts carrying a frozen recent-trend point benchmark:

- Mean model MAE: **43.730 points**
- Mean recent-trend MAE: **58.823 points**
- Descriptive MAE skill vs recent trend: **+0.2566**

The S&P point skill versus no-change has **fallen** from +0.3521 at last Friday's n=5 review to +0.2125 at n=6 because P000014 had a large absolute error. Preserving that deterioration is important even though the forecast still beat its benchmarks on that one observation.

For non-S&P point forecasts, units differ and are not pooled. P000017 lost to the no-change claims point benchmark; P000018 beat its rate no-change/recent-trend benchmarks; P000019 lost to both PMI point benchmarks.

## 3. Recent window versus earlier window

For description only, splitting the 12 resolved probability components into the earliest six and latest six gives:

- **Earliest six:** mean Brier **0.227400**, mean log loss **0.647876**; Brier skill vs neutral **+0.0904**, log-loss skill **+0.0653**.
- **Latest six:** mean Brier **0.222783**, mean log loss **0.637268**; Brier skill vs neutral **+0.1089**, log-loss skill **+0.0806**.

The later six are numerically better by about **0.0046 Brier** and **0.0106 log loss**, but this is **not evidence of learning**. Each window has only six observations and the target composition changed materially: the early set is dominated by S&P direction plus CPI, while the later set includes industrial production, rates, claims, S&P, and PMI. A favorable regime/target mix or luck can easily explain the difference.

## 4. Calibration, discrimination, and vagueness check

Across the 12 probability forecasts, mean assigned event probability is **0.5008** while the observed event frequency is **5/12 = 0.4167**. Coarse bins are jagged and tiny: the 0.30–0.40 forecasts are 0/2, the 0.40–0.50 forecasts 0/3, and the 0.50–0.60 forecasts 5/7. These counts are far too small for a meaningful calibration curve.

The experiment has begun to use probabilities farther from 0.50 than in the first week, but P000019 shows the cost of misplaced discrimination: a 0.56 event probability produced one of the worst Brier scores to date. That is useful feedback, not grounds to retreat mechanically toward 0.50.

There is no current evidence that apparent score improvement was obtained merely by widening intervals. Ten resolved forecasts with intervals have all covered their outcomes (**10/10**), but n=10 is tiny and 100% coverage could itself signal conservative ranges. Sharpness must be evaluated within target units: S&P 1-day intervals remain about 303 points wide on average; the two weekly S&P intervals were 660 and 555 points; the rate intervals were each about 0.23 percentage point wide; P000017 claims width was 39,000; P000019 PMI width was 3.4 points. No cross-unit pooled width is reported.

## 5. Best and worst resolved forecasts

- **Best absolute Brier:** P000017, **0.1296**, for the below-even probability of a >=220,000 initial-claims jump. Its point estimate nevertheless lost to no-change, so the forecast receives no blanket skill label.
- **Worst absolute Brier:** P000015, **0.3249**, for the failed call that July industrial production would be <=0.0% m/m.
- **Second-worst:** P000019, **0.3136**, and it also lost to both point benchmarks. This is the clearest new error diagnosis this Friday.
- **Best apparent earlier score with benchmark caveat:** P000012 Brier 0.2025 matched an event threshold equal to the published CPI consensus and therefore did not demonstrate information beyond consensus.

## 6. Error diagnosis and model-change audit

### v0.2.3 — consumer-demand downside / opposing-channel refinement
The stronger recession-transmission interpretation performed poorly on P000015: total industrial production rose 0.2% rather than being nonpositive. That forecast loss led to the composition-sensitive activity refinement. The underlying methodological point that equities combine cash-flow and discount-rate effects remains useful, but it has not itself earned predictive credit.

### v0.2.4 — private-duration supply pathway
This pathway was initially low-confidence and generated no dedicated numeric forecast, so it receives **no causal-learning credit**. Subsequent Aug. 21 evidence does support the mechanism's existence: AI-hyperscaler issuance has reached $220 billion and tech spreads/new-issue concessions have widened. This is mechanistic support, not proof that the change improved predictions.

### v0.2.5 — composition-sensitive activity
The change prevented later aggregate activity from being read as uniform household strength. P000017's low-layoff outcome was consistent with the model's refusal to infer generalized contraction from household-sector weakness, but its point estimate lost to no-change. Evidence is mixed and too small for a performance attribution.

### v0.2.6 — Treasury debt-management pathway
P000018 scored well on the next-day <4.70% event and modestly beat point benchmarks, but the one-basis-point threshold margin could not identify the buyback mechanism. The Aug. 21 yield rebound shows the initial relief was short-lived. The model therefore narrows the claim to a tactical liquidity/duration buffer rather than a persistent long-yield suppressant.

### v0.2.7 — labor-flow asymmetry
No subsequent labor release has yet tested this revision. P000020 is now precommitted specifically to test low initial claims coexisting with sticky continuing claims. No credit is assigned before resolution.

### v0.2.8 — regional-to-national manufacturing aggregation safeguard
P000019's failure caused this change. Two strong regional headline surveys were over-weighted in the national PMI point forecast. Future national-manufacturing forecasts must use a multi-signal bridge that includes orders/output components, inventory behavior, supply disruptions, and national composition. This change has **zero** learning credit until future forecasts generated under it resolve.

## 7. Hypothesis-weight review

Weights moved from Aug. 20:

| Hypothesis | Aug. 20 | Aug. 21 | Change |
|---|---:|---:|---:|
| H001 Soft landing | 0.35 | 0.34 | -0.01 |
| H002 Late-cycle recession | 0.22 | 0.19 | -0.03 |
| H003 Fiscal/inflation regime | 0.31 | 0.35 | +0.04 |
| H004 Productivity boom | 0.12 | 0.12 | 0.00 |

Broad services/composite activity and hiring reduce H002. H003 becomes a **narrow leader** because strong activity now coexists with elevated energy prices, rebounding long yields, and direct evidence of costly private AI-duration absorption. H001 remains nearly tied because the real-side evidence is genuinely expansionary and later inflation pass-through is not yet observed. H004 is not raised merely because AI financing is huge; investment intensity is not productivity.

## 8. Is the system learning?

**Conclusion: insufficient evidence to assess learning.** The precommitted protocol forbids even a preliminary learning claim before 30 resolved forecasts; the sample is **n=12**.

There are encouraging descriptive facts: lifetime proper scores beat a neutral probability comparator, S&P point forecasts still beat no-change/recent-trend on average, and the latest six proper scores are slightly better than the earliest six. But none of these establishes learning. The apparent gain can plausibly come from luck, a favorable target mix, regime change during the Iran/energy shock, or the fact that many probabilities remain close enough to 0.50 to limit losses. The P000019 failure and decline in S&P point skill are direct evidence against telling a monotonic-improvement story.

Nor is there evidence yet that the model is improving by becoming vaguer: interval widths have not systematically widened, and the latest weekly S&P interval was narrower than the earlier weekly interval. But 10/10 interval coverage is itself too small and potentially too conservative to validate uncertainty quality.

The experiment therefore has **no demonstrated learning yet**, but it is generating auditable error-linked revisions. The key scientific question remains whether those revisions improve later out-of-sample forecasts relative to frozen benchmarks once the sample reaches the precommitted thresholds.

## 9. Highest-information next discriminating forecast

**P000020** is the highest-information new forecast: **57%** probability that the Aug. 27 first DOL release shows **initial claims <220,000 while continuing claims are >=1.800 million**. Point forecasts are 209,000 and 1.812 million with frozen no-change and external calendar point benchmarks.

This is a joint test of the v0.2.7 labor-flow split. The low-initial/high-continuing combination would support a low-fire / sticky-reemployment regime; a synchronized jump in both would favor H002; a material drop in both would favor a more benign H001 labor interpretation. A joint event is used rather than two correlated binary forecasts to avoid inflating the sample artificially.

For the new H003-vs-H001 lead contest, the highest-information evidence will be **later inflation expectations and price data that actually include the August energy shock**. July PCE largely predates the latest oil escalation, so this review does not manufacture a high-confidence H003 forecast around a temporally mismatched release merely to create activity.

## 10. Transferability review

No new Universal transfer candidate is added. Today's main lessons—benchmark-relative evaluation, ambiguous downstream endpoints, adversarial review, and joint measurements—are applications of already-supported Universal lessons UL-0002 through UL-0004 and failure modes FM-005/FM-006. The market-specific regional-to-national aggregation error is recorded locally and can be reconsidered by the Saturday reconciler only if it later proves genuinely cross-domain.
