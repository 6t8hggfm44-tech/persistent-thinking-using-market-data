# Weekly Learning Review — 2026-08-14

**Evidence cutoff:** 2026-08-14T17:25:18-04:00  
**Current model after review:** v0.2.3  
**Resolved binary-probability components:** 6  
**Resolved S&P direction/point/interval forecasts:** 5

## 1. Auditor results this cycle

- **P000013:** S&P 500 1-day distribution from Aug. 12 to Aug. 13. p(up)=0.51 resolved true at 7,798.99. Brier 0.2401; log loss 0.673345; point MAE 43.99; 80% interval hit. Point skill +0.1287 vs no-change but **-0.4571 vs recent trend**.
- **P000002:** S&P 500 1-week distribution from Aug. 8 to Aug. 14. p(up)=0.52 resolved true at 7,785.76. Brier 0.2304; log loss 0.653926; point MAE 10.76; 80% interval hit. Point skill +0.6174 vs no-change.

No historical forecast content or resolution rule was changed.

## 2. Lifetime descriptive scores

### Binary probabilities

Across all six resolved binary-probability components:
- Mean Brier: **0.227400**
- Mean log loss: **0.647876**

These targets are not fully homogeneous because one is a CPI event. For the five S&P direction forecasts only:
- Mean Brier: **0.232380**
- Mean log loss: **0.657884**
- Neutral 0.50 binary comparator Brier: **0.250000**
- Descriptive Brier skill vs 0.50 comparator: **+0.0705**
- Neutral 0.50 log loss: **0.693147**
- Descriptive log-loss skill vs 0.50 comparator: **+0.0509**

A historical unconditional S&P up-rate benchmark was not precommitted in the original records. It is therefore **not retroactively introduced** here to improve or worsen the result.

### Point forecasts

Across the five resolved S&P point forecasts:
- Mean model MAE: **16.632** points
- Mean matched no-change MAE: **25.670** points
- Descriptive MAE skill vs no-change: **+0.3521**

For the three forecasts carrying a precommitted recent-trend benchmark:
- Mean model MAE: **23.097** points
- Mean recent-trend MAE: **31.927** points
- Descriptive MAE skill vs recent trend: **+0.2766**

These results are encouraging as raw descriptions but statistically and compositionally far too small for a learning claim.

### Intervals

- S&P 80% interval coverage: **5/5 = 100%**
- Mean interval width across all five S&P forecasts: **374.2 points**
- Mean width for the four 1-day intervals: **302.75 points**
- Weekly P000002 interval width: **660 points**

Observed 100% coverage at n=5 is not evidence of superior uncertainty estimation. The intervals are broad and the sample is tiny; coverage must be judged jointly with sharpness as required by the Learning Protocol.

## 3. Calibration and discrimination

No meaningful calibration curve or probability-bin reliability estimate is possible. All five S&P direction probabilities lie between **0.47 and 0.52**, with average absolute distance from 0.50 of only **0.018**. Although every S&P probability happened to be on the ultimately correct side of 0.50, the probabilities contain very little discrimination and the streak can easily be luck.

This is an important anti-Goodhart point: a 5/5 directional-side record sounds much stronger than the proper scores actually indicate. Brier scores near 0.23 are only modestly better than an uninformative 0.25 comparator.

## 4. Vintage comparison

Comparable S&P-only results are too sparse for a valid learning curve, but the available vintages do **not** show monotonic improvement:

- **v0.2.0-generated S&P forecasts (P000001, P000002; n=2):** mean Brier 0.23525; mean log loss 0.66364; point MAE 6.935 vs no-change 16.325.
- **v0.2.1-generated S&P forecasts (P000010, P000011; n=2):** mean Brier 0.22565; mean log loss 0.64440; point MAE 12.65 vs no-change 22.605.
- **v0.2.2-generated S&P forecast resolved so far (P000013; n=1):** Brier 0.2401; log loss 0.67335; point MAE 43.99 vs no-change 50.49 and recent trend 30.19.

The v0.2.1 proper scores are numerically better than v0.2.0, but two observations per vintage are effectively anecdotal. Point error actually worsened from the early vintage, and P000013 lost to recent trend. There is no defensible evidence of a learning trend.

## 5. Best and worst resolved forecasts

- **Best absolute proper score:** P000012, Brier 0.2025. However, its CPI threshold exactly matched the timestamped consensus realization, so this is **not evidence of benchmark-relative information**.
- **Strongest point result versus recent trend:** P000011, descriptive point skill +0.812 versus its precommitted recent-trend benchmark.
- **Largest point error / clearest benchmark failure:** P000013, MAE 43.99 and descriptive skill **-0.457** versus recent trend.

Preserving both the good and bad benchmark comparisons prevents the 5/5 directional-side streak from dominating the narrative.

## 6. Did prior model changes help?

### v0.2.1 — oil / term-premium offset channel
The model added the possibility that weak labor could coexist with higher long yields when commodity and term-premium pressure dominate. Subsequent benign CPI/PPI and weaker retail data were accompanied by lower yields, so the *dominant H003 version* of that path has not received follow-through and H003 has since been reduced. The state-dependent causal edge is not falsified—it explicitly allows either channel to dominate—but it has **not yet earned predictive credit**.

### v0.2.2 — H001 increase on contained CPI + tight credit
The later PPI release was directionally consistent with the disinflation side of H001, but the July retail/control-group miss was contrary to the stronger growth-resilience version. P000013 and P000002 both resolved on the favored directional side, yet P000013's point forecast lost to recent trend and equity outcomes are causally ambiguous. Therefore this model change receives **mixed, not positive, causal-learning credit**.

### v0.2.3 — consumer-demand opposing-channel refinement
This change is new and has no subsequent out-of-sample test yet. Its intended improvement is conceptual identifiability: weak demand may reduce both cash flows and yields, so equity price alone should not decide between H001 and H002. The next forecasts deliberately include a real-activity release rather than only another index-direction call.

## 7. Error diagnosis

The clearest current weakness is **low discrimination**. Short-horizon S&P probabilities cluster extremely close to 0.50, which protects proper scores from large losses but supplies little information. This is not automatically a flaw—markets may genuinely be close to unpredictable at that horizon—but the project must not mistake safe near-neutral forecasts for learning.

A second weakness is that headline equity prices can fit several hypotheses through opposing discount-rate and cash-flow channels. The model should therefore increase the share of forecasts tied to causal discriminators—growth, credit, inflation/yield responses, and earnings breadth—without artificially inflating sample size with many correlated events.

## 8. Learning assessment

**Conclusion: insufficient evidence to assess learning.** The precommitted protocol prohibits even a preliminary learning claim before 30 resolved forecasts; only six binary-probability components have resolved. The current data show some descriptive skill versus no-change and neutral probability benchmarks, but no stable vintage improvement, no meaningful calibration sample, no subgroup robustness, and no proof that model revisions caused better subsequent predictions.

The apparent success could still be explained by luck, a favorable one-week regime, near-0.5 probabilities, broad intervals, or target mix. Nothing in this review supports changing the precommitted thresholds.

## 9. Highest-information next discriminating forecast

**P000015:** probability **0.57** that the initial Federal Reserve July 2026 industrial-production release is **<=0.0% m/m** on Aug. 18. This directly tests whether the retail/labor weakness is transmitting into real activity. A nonpositive print would favor H002 over the stronger H001/H004 growth-resilience versions; a strong positive print would weaken the new demand-downside interpretation. The forecast is committed separately with its resolution rule and evidence cutoff.

A separate weekly S&P forecast, P000014, remains useful for continuity and benchmark tracking but is intentionally not treated as the highest-information causal test.
