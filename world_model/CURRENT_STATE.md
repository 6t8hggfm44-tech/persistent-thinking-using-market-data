# Current Market State

**Model version:** 0.2.8  
**Status:** Friday weekly state; twelve resolved binary-probability components; learning still unassessable by protocol threshold  
**Evidence cutoff:** 2026-08-21T17:24:57-04:00

## OBSERVATIONS

- P000014 resolved before model revision: the S&P 500 closed **7,674.37** on Aug. 21 versus the frozen Aug. 14 reference 7,785.76, so the weekly up-event was FALSE. Brier **0.2401**, log loss **0.673345**, point MAE **105.63**, 80% interval hit. The 7,780 point forecast modestly beat frozen no-change MAE **111.39** and recent-trend MAE **139.51**.
- P000019 resolved before model revision: August flash U.S. Manufacturing PMI was **53.2**, so the >=54.0 event was FALSE. Brier **0.3136**, log loss **0.820981**, point MAE **1.0**, 80% interval hit. The forecast lost to both the 53.7 published-consensus point benchmark (0.5 MAE) and 53.9 July no-change benchmark (0.7 MAE), and to neutral binary Brier 0.25.
- Across twelve resolved binary-probability components, lifetime mean Brier is **0.225092** and mean log loss **0.642572**. This remains far below the precommitted 30-resolution threshold; no learning claim is permitted.
- August flash Services PMI rose to **56.8** from 54.6 and Composite Output to **56.0** from 54.5; services hiring was reported at its strongest pace in 19 months. Manufacturing PMI eased to 53.2 and factory output/order momentum was softer.
- S&P Global reported that input and selling-price growth eased somewhat in August but remained elevated.
- Brent settled at **$94.39** and WTI at **$87.06**, up **6.39%** and **5.66%** for the week.
- U.S. Treasury yields rebounded after the earlier buyback-driven relief: Reuters reported the 10-year near **4.73%** and 30-year near **5.266%** on Aug. 21.
- Reuters, citing BNP Paribas data, reported **$220 billion** of 2026 AI-hyperscaler debt issuance as of Aug. 10 versus **$12.5 billion** in the comparable prior-year period. Technology investment-grade spreads were around **89 bp**, 9 bp wider than the overall IG market, and recent deals required larger concessions.
- No fresh post-Aug. 20 HY OAS observation was verified this cycle.

## INFERENCE

The national flash PMI materially weakens H002's current generalized-contraction branch. Services and composite activity accelerated, services hiring strengthened, and manufacturing remained above 50 even though it slowed.

P000019 is a useful negative forecast result: the model over-weighted strong Empire State and Philadelphia headline surveys as evidence that national manufacturing would hold above July/consensus. The error does **not** imply that manufacturing is weak in absolute terms; it implies that regional headline surveys need an explicit aggregation/sector bridge before being translated into a national PMI forecast.

The same strong activity data do not uniquely support H001. With price pressures still elevated, oil near $94 Brent, long yields rebounding, and private/public duration supply heavy, strong nominal demand can keep the policy and financing constraint binding. This is the leading H003 counter-interpretation.

The private-duration pathway receives stronger external support: AI-related bond issuance is large enough that investors are demanding wider spreads and new-issue concessions. This supports the **existence** of a supply-absorption channel but does not identify the magnitude of its causal contribution to Treasury yields.

The Treasury buyback pathway is refined rather than discarded. The Aug. 19 intervention produced a material short-run long-end rally, but the Aug. 21 rebound shows that the effect should be treated as a tactical liquidity/duration buffer, not a durable substitute for underlying fiscal, inflation, growth, or private-duration forces.

## Current regime

**Resilient late-cycle expansion with strong services activity, uneven manufacturing/household sectors, and a now-slightly-leading inflation/duration-policy constraint over the benign soft-landing interpretation.**

## Hypothesis weights

| Hypothesis | Weight |
|---|---:|
| H001 Soft landing | 0.34 |
| H002 Late-cycle recession | 0.19 |
| H003 Fiscal/inflation regime | 0.35 |
| H004 Productivity boom | 0.12 |

**Change from Aug. 20:** H001 -0.01, H002 -0.03, H003 +0.04, H004 unchanged. The broad PMI activity/hiring evidence lowers H002. H003 gains because strong demand coexists with persistent energy pressure, rebounding long yields, and newly documented private-duration absorption costs. H001 remains close because the same activity strength is genuine evidence against contraction, and later inflation pass-through is not yet observed.

## Skeptic result

The Skeptic attacked H001 before the update. Its strongest case is that **strong growth is sign-ambiguous between H001 and H003**: robust services can be benign if inflation and yields ease, but it can instead keep the Fed and long-rate constraint tight when energy and price pressure persist. P000019 further shows that regional manufacturing strength did not generalize cleanly to the national index. The energy shock, long-yield rebound, and AI debt supply therefore prevent the strong PMI from being mapped mechanically into a soft-landing upgrade.

The response is that H002 still loses substantial weight because composite/services activity and hiring are too strong for an already generalized contraction. The main contest shifts from H001-vs-H002 toward **H001-vs-H003**.

## Material causal changes

1. **Strong activity is now conditioned on the inflation/rate response.** Growth strength plus easing prices/yields favors H001; growth strength plus persistent price pressure/higher policy expectations/long yields favors H003.
2. **Regional-survey-to-national-manufacturing bridge added.** Empire/Philadelphia headlines are noisy and compositionally different from national PMI; future forecasts must use multiple regional components, national production composition, inventories/orders, and supply disruptions rather than linear headline extrapolation.
3. **Private AI-duration supply confidence raised from low to moderate.** The scale of issuance and observed spread/concession response establish a real absorption-cost channel, while causal attribution to Treasury yields remains uncertain.
4. **Treasury buybacks reclassified as a tactical buffer.** Debt-management actions can temporarily alter long-end liquidity and duration absorption, but one intervention cannot be assumed to suppress the structural clearing yield persistently.

## Most important causal claims

1. Weak labor demand can first show up as reduced hiring/re-employment without rising initial claims; initial and continued claims should be evaluated jointly.
2. Strong real/nominal activity is not automatically a soft-landing signal: the accompanying inflation, policy, and yield response determines whether it favors H001 or H003.
3. Regional manufacturing surveys are intermediate signals, not a direct substitute for national manufacturing measures.
4. Commodity/inflation risk, Treasury issuance/term premium, private corporate duration supply, and Treasury debt-management all affect long yields; one yield move remains weakly identifying.
5. AI/capex/defense demand can support aggregate activity while household-sensitive sectors weaken, but financing the AI buildout can itself tighten financial conditions.
6. Commodity shocks pass into measured inflation with lags and state dependence; the August oil shock must be tested in later inflation expectations and price data.

## What would surprise the model?

- Strong services/composite activity persists while both inflation expectations and long yields fall materially despite oil remaining near current levels; that would weaken H003 and favor H001.
- Initial claims stay near 200,000 while continued claims rise persistently and payroll/hiring measures weaken for several more weeks; that would imply a more durable low-fire/weak-reemployment regime than a simple soft-landing labor story.
- National manufacturing accelerates sharply next month while regional surveys remain volatile, suggesting P000019 was timing noise rather than evidence for an aggregation problem.
- AI-related corporate issuance remains exceptionally heavy but tech spreads/concessions and long-end yields normalize without offsetting policy changes, weakening the private-duration-supply edge.
- Oil remains near the current range but later inflation expectations and price data fail to firm, materially weakening H003's pass-through branch.

## Forecast-error linkage and update discipline

P000019 is the material forecast error informing this cycle's methodological model revision. Its loss to both consensus and no-change point benchmarks is specifically linked to the new regional-to-national aggregation safeguard. The model is **not** revised toward weaker broad growth solely because the manufacturing forecast missed; the same first flash release showed very strong services/composite activity.

P000014's weekly S&P outcome does not drive macro weights. The point forecast modestly beat its frozen benchmarks, but the equity endpoint is causally ambiguous and the large absolute move remains inside a broad interval.

No model change is credited merely because a post-hoc story can explain either outcome. All new causal updates are tied to separately recorded post-cutoff evidence and the prospectively frozen forecast errors above.
