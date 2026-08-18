# Model Changelog

## 0.1.0 — Baseline
- Created repository architecture.
- Established four neutral competing macro-market hypotheses.
- No live market evidence had yet been ingested.
- No forecasts had yet been issued.

## 0.2.0 — First live baseline (2026-08-08)
- Initialized state using an evidence cutoff of 2026-08-08 10:30 ET.
- Set hypothesis weights: H001 0.30, H002 0.32, H003 0.27, H004 0.11.
- Explicitly flagged stale high-yield spread input.
- Created nine precommitted forecasts across SPX, rates, oil, credit, and sector leadership.
- Added independent Skeptic report.

## 0.2.1 — First scored update (2026-08-10)
- Resolved P000001 before ingesting new evidence. Outcome: SPX 7,753.11; Brier 0.2401; log loss 0.673345; point MAE 3.11; 80% interval hit; no-change MAE 4.53. This single forecast did not justify a model revision.
- Ingested only evidence available after the Aug. 8 cutoff: the Aug. 10 oil shock, higher long yields/issuance pressure, near-record equity resilience, and strong aggregate earnings.
- Ran the Skeptic against H002 before updating weights.
- Changed hypothesis weights to H001 0.31, H002 0.28, H003 0.30, H004 0.11.
- Reduced H002 because its expected credit/earnings confirmation is absent so far; increased H003 because the commodity/inflation/term-premium channel remained active despite weak labor; modestly increased H001 because earnings/risk assets remain resilient.
- Refined the causal graph to make explicit that weak labor can lower the expected policy path while commodity shocks and Treasury-supply/term-premium pressure simultaneously keep long yields elevated.
- No causal credit is assigned to P000001 for these changes; the revision is linked to post-cutoff evidence rather than the forecast outcome.

## 0.2.2 — CPI / credit cross-check update (2026-08-12)
- Resolved P000011 and P000012 before ingesting Aug. 12 model evidence. P000011: p(up)=0.52 resolved true at SPX 7,748.50; Brier 0.2304, log loss 0.653926, point MAE 8.50, 80% interval hit. P000012: p(CPI YoY <=3.4%)=0.55 resolved true at exactly 3.4%; Brier 0.2025, log loss 0.597837.
- Explicitly recorded that P000012's favorable proper score does not imply informational skill versus consensus because its threshold was the published 3.4% consensus point and the first-release outcome exactly matched consensus.
- Ingested only post-Aug. 11-cutoff evidence: July CPI composition, the newly published Aug. 11 HY OAS reading of 2.72%, the Aug. 12 Treasury/equity reaction, and WTI remaining near $83.27.
- Ran the Skeptic against H001 before revising weights. The Skeptic preserved H003's lagged oil-pass-through alternative and H002's unresolved labor-risk alternative.
- Changed weights from H001 0.31 / H002 0.28 / H003 0.30 / H004 0.11 to **0.35 / 0.25 / 0.29 / 0.11**.
- The main driver is fresh credit evidence: HY spreads remain tight and therefore fail to confirm the recession mechanism despite earlier labor weakness. Contained CPI modestly supports H001 over H003, but because it matched consensus and predates much of the latest oil shock, the inflation-regime weight is reduced only slightly.
- Added an explicit lag/state-dependence edge from commodity shocks through retail energy/input costs to measured inflation. This prevents the timing error of treating July CPI as a contemporaneous test of an August spot-oil shock.
- None of these model changes are credited to the mere fact that P000011/P000012 resolved correctly. The update is tied to the separately recorded post-cutoff evidence.

## 0.2.3 — Friday consumer-demand / learning review (2026-08-14)
- Resolved **P000013** and weekly **P000002** before ingesting post-Aug. 12 evidence. P000013: p(up)=0.51 resolved true at SPX 7,798.99; Brier 0.2401, log loss 0.673345, point MAE 43.99, interval hit; its point forecast beat no-change but lost to recent trend. P000002: p(up)=0.52 resolved true at SPX 7,785.76; Brier 0.2304, log loss 0.653926, point MAE 10.76, interval hit, and beat no-change.
- Friday scoring review: six binary-probability components have resolved, with mean Brier **0.227400** and mean log loss **0.647876**. Five S&P point forecasts have mean MAE **16.632** versus **25.670** for matched no-change benchmarks (descriptive MAE skill +0.352). Three observations with a precommitted recent-trend benchmark show descriptive MAE skill +0.277. All five S&P intervals covered, but observed coverage is uninterpretable at n=5 and ranges are broad. Under `LEARNING_PROTOCOL.md`, n=6 is far below the 30-resolution threshold: **no learning claim is permitted**.
- Ingested only evidence available after the Aug. 12 cutoff: July PPI below consensus, Aug. 8-week jobless claims, Aug. 13 market response, July retail/control-group sales, Aug. 14 yield response, renewed oil/geopolitical pressure, and the Aug. 14 weekly close.
- Ran the Skeptic against H001. The strongest countercase was that benign inflation/lower yields can be produced by weaker demand and are therefore not unique soft-landing evidence; record-adjacent equities can also be supported by lower discount rates and concentrated AI earnings. Fresh post-Aug. 11 credit data were not verified, so absence of newly observed spread widening was not treated as evidence.
- Changed weights from H001 0.35 / H002 0.25 / H003 0.29 / H004 0.11 to **0.34 / 0.29 / 0.26 / 0.11**. Retail/control-group weakness raises H002; benign PPI and lower yields reduce the near-term H003 path; H001 retains a narrow lead because layoffs remain low and the retail miss has identifiable timing distortions. H004 stays unchanged without direct productivity evidence.
- Added a consumer-demand branch to the causal graph. A demand shock can lower earnings/cash-flow expectations while also lowering policy-rate expectations and discount rates; therefore equity price alone is an ambiguous causal readout. Future discrimination should prefer joint evidence across growth, yields, credit, labor, and earnings breadth.
- P000013's loss to recent trend is recorded as a forecast-generation warning, not retroactively used to alter macro weights. No historical forecast content, benchmark, or resolution rule was changed.

## 0.2.4 — Credit resilience / private-duration refinement (2026-08-17)
- **No currently live forecast resolved in this cycle**, so lifetime scores were carried forward unchanged and no model update is attributed to forecast success or failure.
- Ingested only evidence newly available after the Aug. 14 17:25 ET cutoff: FRED's Aug. 17 publication of the Aug. 14 HY OAS close at **2.67%**; the Aug. 17 Empire State survey at **20.6** versus 12 consensus; the Aug. 17 S&P close and sector breadth; the renewed oil rise to Brent **$90.87** / WTI **$84.50**; and the Aug. 17 long-yield move to roughly **4.724%** on the 10-year and **5.3103%** on the 30-year.
- Ran the Skeptic against H001 before revision. The strongest countercase was that tight credit may lag a downturn, a single regional survey is noisy, and simultaneous oil/long-yield pressure could still derail a benign landing. Earlier national retail/labor weakness remains unresolved.
- Changed weights from H001 0.34 / H002 0.29 / H003 0.26 / H004 0.11 to **0.35 / 0.26 / 0.28 / 0.11**. Fresh tight credit and strong regional manufacturing reduce H002; renewed oil and long-end pressure raise H003; H001 gains only 0.01 because those H003 risks offset much of the credit/activity improvement.
- Added a **provisional private-duration supply path** from corporate capex financing through corporate bond issuance to long yields/financial conditions. Reuters/Barclays commentary on heavy AI-related corporate duration issuance motivated the refinement, but it is explicitly low-confidence and requires prospective confirmation rather than being treated as a one-day causal fact.
- Preserved the existing opposing-channel demand model: the Aug. 17 rise in long yields despite recent weak demand is evidence that the discount-rate channel can be offset, not proof of any single mechanism.

## 0.2.5 — Composition-sensitive activity update (2026-08-18)
- Resolved **P000015** and **P000016 before ingesting post-Aug. 17 evidence**. P000015: p(total IP <=0.0%)=0.57 resolved FALSE at **+0.2%**, Brier **0.3249**, log loss **0.843970**, worse than neutral Brier 0.25. P000016: p(10-year CMT >=4.70%)=0.58 resolved TRUE at **4.71%**, Brier **0.1764**, log loss **0.544727**, point MAE **0.01 pp**, 80% interval hit.
- Lifetime scoring is now n=8 binary-probability components, mean Brier **0.233213**, mean log loss **0.659494**. The score deterioration after P000015 is preserved; n=8 remains far below the 30-resolution threshold, so no learning claim is permitted.
- Ingested only evidence available after the Aug. 17 cutoff: the Fed's July G.17 release, July housing/pending-sales data, the Aug. 18 official Treasury CMT curve, oil persistence, and Aug. 18 market/sector response.
- Ran the Skeptic against H001. The strongest countercase is that positive aggregate industrial production was compositionally narrow: consumer-goods output fell and housing weakened sharply while AI-linked business equipment/high tech and defense supported production. Thus the aggregate sign cannot by itself identify a broad soft landing.
- Changed weights from H001 0.35 / H002 0.26 / H003 0.28 / H004 0.11 to **0.34 / 0.25 / 0.29 / 0.12**. H002 falls slightly because its precommitted aggregate contraction event failed; H003 rises slightly because elevated oil/long rates persisted through weak housing; H004 rises slightly on direct high-tech/business-equipment output evidence; H001 remains the leader but loses 0.01 because the economy looks more compositionally bifurcated than uniformly benign.
- Added a **composition-sensitive activity refinement** to the causal graph: AI/capex/defense demand can keep aggregate industrial production positive while household-sensitive consumer goods, autos, and housing weaken. Future H001/H002/H004 discrimination must use composition, labor, credit, and household-demand measures jointly with aggregate IP.
- P000016's success is not treated as proof of the private-duration-supply edge. The official 10-year CMT actually eased 1 bp from Aug. 17; the forecast establishes only that the >=4.70% event was correctly assigned above-even probability.
- No new Universal candidate was created because the composition lesson is an application of already-supported UL-0004 / FM-006 rather than a genuinely new transferable method.
