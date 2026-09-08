# Current Market State

**Model version:** 0.2.14  
**Status:** Tuesday Sep. 8 post-close cycle; P000003/P000006/P000007/P000009 resolved; P000008 held pending its dated FRED observation; no weight or causal-graph change; P000028 frozen prospectively  
**Evidence cutoff:** 2026-09-08T17:50:37-04:00

## Auditor
Forecasts were resolved before post-Sep. 7 evidence was used for model revision.

- **P000003 — SPX one-month distribution:** Sep. 8 close **7,673.52**, below the frozen 7,757.64 starting close, so the 0.54 up-event resolved **FALSE**. Brier **0.2916**, log loss **0.776529**. The 7,820 point missed by **146.48** versus **84.12** for frozen no-change; the 7,215-8,380 80% interval covered. This is a probability and point-forecast miss, not an interval-tail miss.
- **P000006 — U.S. 10-year CMT:** official Sep. 8 Treasury 10-year constant-maturity yield **4.80%**. The 4.62% point missed by **0.18 pp** versus **0.16 pp** for frozen no-change; the 4.30%-4.95% 80% interval covered.
- **P000007 — WTI:** front-month NYMEX WTI settled **$93.03/bbl**. The frozen $78.00 point missed by **$15.03** versus **$14.85** for no-change, and the $68-$91 80% interval **missed**. This is a genuine tail/distribution miss and is preserved without retroactive widening.
- **P000009 — sector leadership:** the frozen Information Technology top-three call resolved **FALSE**. Dividend-adjusted sector-ETF total-return data as of Sep. 8 show Energy **+11.41%**, Health Care **+3.48%**, and Financials **+0.87%**, all above Technology **-0.37%** over the one-month window. Because this uses sector ETFs as a total-return proxy rather than a direct S&P sector-index table, the source-layer limitation is preserved; the ordering is nevertheless sufficient to establish that Technology was not top three.
- **P000008 — HY OAS:** **not yet resolved.** At this cutoff FRED's BAMLH0A0HYM2 page shows the latest dated observation as Sep. 7 at **2.68%**, updated Sep. 8, with the next release Sep. 9. The original rule targets Sep. 8 or the nearest available observation. Because the exact Sep. 8 observation is expected to publish on Sep. 9, using the Sep. 7 carry-forward now would create avoidable timing ambiguity; resolution is deferred until the dated source is available.

Lifetime **probability** scoring is now **n=19**, mean Brier **0.213674**, mean log loss **0.617075**. The precommitted 30-resolution threshold remains unmet; **learning cannot yet be inferred**. Strict record-level interval coverage is now **17/19 = 89.47%** among resolved forecasts with explicit intervals. That remains a small sample and does not justify widening or narrowing intervals after today's WTI miss.

## Observations — evidence first available after 2026-09-07T17:28:05-04:00

- **OBSERVATION:** Reuters reported further Middle East escalation on Sep. 8, including Houthi attacks on Saudi energy facilities. Brent settled **$97.92** and WTI **$93.03**, with WTI at a six-week high.
- **OBSERVATION:** The New York Fed's August Survey of Consumer Expectations, reported Sep. 8, showed one-year inflation expectations steady at **3.6%**, five-year expectations steady at **3.0%**, and three-year expectations edging down to **3.2%**. Expectations of higher unemployment rose sharply and confidence in finding a new job worsened.
- **OBSERVATION:** The official Sep. 8 10-year Treasury constant-maturity yield was **4.80%**. The S&P 500 closed **0.58% lower at 7,673.52**. These are market endpoints and are not treated as unique evidence for any one causal mechanism.
- **OBSERVATION:** BLS schedules the first August PPI release for Sep. 10 at 08:30 ET. A timestamped Investing.com calendar snapshot at this cutoff shows a **0.4% m/m** headline-final-demand consensus versus July's first-release **0.0%**.

## Inference
The physical energy-supply-risk branch remains material and P000007 demonstrates that the original Aug. 8 commodity distribution understated the realized tail. But the same-day New York Fed survey does **not** show a corresponding unanchoring of medium-term inflation expectations; its labor/financial expectations instead preserve a growth-negative pathway. The Sep. 8 10-year yield and equity decline are multiply determined downstream endpoints. Therefore the new evidence does not justify treating the oil tail miss as proof of H003's broader core-inflation regime.

September's escalation is also outside the August PPI/CPI reference period. It may affect later inflation, household income and policy expectations, but it must not be leaked backward into P000023 or P000028 as if it were an August price observation.

## Hypothesis weights
- **H001 Soft landing: 0.35** (unchanged)
- **H002 Late-cycle recession: 0.15** (unchanged)
- **H003 Fiscal/inflation regime: 0.38** (unchanged)
- **H004 Productivity boom: 0.12** (unchanged)

No reweighting is made. H003 receives direct support from persistent physical energy disruption, but stable medium-term survey inflation expectations and worsening consumer labor/financial expectations are meaningful counterevidence. A weight move before the Sep. 10-11 inflation releases would overfit a commodity/market shock whose pass-through remains unresolved.

## Skeptic
**Attack on leading H003:** The strongest contrary evidence is that a large oil move has not yet produced broader inflation-expectation unanchoring. Three- and five-year New York Fed expectations are stable-to-lower, while consumers report worsening labor-market and financial expectations. The oil shock can become growth-negative through household purchasing power rather than persistently inflationary in core prices. The 4.80% 10-year yield and weaker S&P are ambiguous endpoints and cannot identify which path dominates.

**Response:** Physical infrastructure/shipping risk is real and the WTI tail miss is material evidence that commodity-risk variance was understated in the original vintage. But one 80% interval miss is expected occasionally in a calibrated system and is not, by itself, grounds to retune the causal model or interval widths. The next useful discrimination comes from producer/consumer inflation and subsequent real-demand/labor evidence.

**What would surprise the current model:** benign PPI/CPI despite persistent energy stress would favor H001 over the immediate H003 pass-through story; broad underlying inflation strength would favor H003; sustained energy stress followed by clear labor/consumer deterioration would strengthen H002.

## Material model changes
**None.** Model v0.2.14 remains current. Today's largest error, P000007, is a distributional/tail miss in a pathway already present in the causal graph. Retuning the graph or interval process after one 80% miss would be hindsight fitting; no `MODEL_CHANGELOG.md` entry is warranted. P000003 also lost to no-change on both event and point components, but an equity endpoint remains too causally ambiguous to justify a structural revision by itself.

No new Universal transfer candidate is added. The methodological response to today's failures is already covered by the existing anti-hindsight, baseline-relative, discriminating-measurement, longitudinal-learning, and threshold-versus-distribution safeguards.

## Learning status
Probability metrics: **n=19**, mean Brier **0.213674**, mean log loss **0.617075**. The new P000003 probability resolution worsened the lifetime averages from the n=18 snapshot. This is preserved as negative evidence, but n=19 remains below the precommitted minimum and the target mix is heterogeneous/dependent. No learning claim is permitted.

## Open forecasts
- **P000008:** HY OAS one-month interval; held for the Sep. 8 dated FRED observation or an unambiguous nearest-observation application under its original rule.
- **P000023:** 54% probability first-release August core CPI is >=0.3% m/m on Sep. 11; point 0.3%, 80% interval 0.1%-0.4%; remains frozen.
- **P000027:** 58% probability the FOMC raises both bounds of the federal-funds target range by at least 25 bp at the Sep. 15-16 meeting; remains frozen.
- **P000028:** 53% probability first-release August headline final-demand PPI is >=0.4% m/m on Sep. 10; point 0.4%, 80% interval -0.2%-0.9%; evidence cutoff 2026-09-08T17:50:37-04:00.

## New forecast
**P000028** is frozen from unchanged model v0.2.14. Its 0.4% point deliberately matches the timestamped external consensus, so a good absolute result will **not** be treated as evidence of information beyond consensus. The probability is only modestly above even because August energy conditions were firmer than July's steep producer-energy decline, while July final-demand PPI was flat and the producer-price distribution remains volatile. The much larger Sep. 5-8 oil escalation is excluded from the August observation window.

## Most important watch
**Friday Sep. 11 first-release August core CPI.** PPI on Sep. 10 is an upstream check, but the already-frozen P000023 core-CPI forecast remains the cleaner near-term discriminator between H001 disinflation-with-resilience and H003 persistent-underlying-inflation/policy constraint.