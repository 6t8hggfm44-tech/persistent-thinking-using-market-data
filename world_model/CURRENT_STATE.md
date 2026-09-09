# Current Market State

**Model version:** 0.2.14  
**Status:** Wednesday Sep. 9 post-close cycle; P000008 resolved; no hypothesis-weight or causal-graph change; no new forecast added because P000028 and P000023 already provide the next inflation tests  
**Evidence cutoff:** 2026-09-09T17:17:44-04:00

## Auditor
Forecast resolution occurred before post-cutoff evidence was used for model revision.

- **P000008 — HY OAS one-month interval:** FRED/ICE BofA now reports the exact Sep. 8 BAMLH0A0HYM2 observation at **2.67%**. The frozen 3.05% point missed by **0.38 percentage point**, versus **0.17 point** for the explicitly stale frozen 2.84% baseline. The 2.55%-3.85% 80% interval **covered**. This is interval coverage without point-forecast skill; no probability score is manufactured.

Lifetime **probability** scoring is unchanged at **n=19**, mean Brier **0.213674**, mean log loss **0.617075**. The precommitted 30-resolution threshold remains unmet, so **learning cannot yet be inferred**. Strict record-level interval coverage becomes **18/20 = 90.0%** among resolved forecasts with explicit intervals. Target units are heterogeneous, so aggregate interval width is not interpreted as sharpness.

## Observations — evidence first available after 2026-09-08T17:50:37-04:00

- **OBSERVATION:** The exact Sep. 8 ICE BofA U.S. High Yield OAS observation became available at **2.67%**, allowing P000008 resolution.
- **OBSERVATION:** Reuters reported Sep. 9 Brent settlement **$101.21/bbl** and WTI **$96.05/bbl**, both the highest closes since May 22, amid intensified attacks on shipping and sharply reduced Strait of Hormuz flows.
- **OBSERVATION:** Treasury announced a Sep. 10 liquidity-support buyback of up to **$6 billion** in 10- to 20-year bonds. Benchmark 10-year yields rose after the announcement to an intraday **4.8528%**, with Reuters noting that some investors had expected a larger operation.
- **OBSERVATION:** A Sep. 4-9 Reuters poll found **65 of 93 economists** expected the FOMC to hold next week, while Reuters reported market pricing near **60%** for a hike. This is new evidence but not a retroactive benchmark for P000027.
- **OBSERVATION:** The S&P 500 closed **0.48% lower at 7,636.46**; Energy was the only S&P sector to advance.

## Inference
The persistent, physically linked energy shock strengthens H003's forward input-cost and policy-constraint pathway. However, P000008's relatively tight 2.67% HY OAS outcome shows that the one-month credit-spread point forecast overstated stress, and the Reuters economist poll preserves substantial policy uncertainty. Equity and Treasury-price reactions remain multiply determined downstream endpoints.

The Sep. 9 energy escalation occurred after the August PPI/CPI reference period. It updates the forward world state but is not leaked backward into P000028 or P000023.

## Hypothesis weights
- **H001 Soft landing: 0.35** (unchanged)
- **H002 Late-cycle recession: 0.15** (unchanged)
- **H003 Fiscal/inflation regime: 0.38** (unchanged)
- **H004 Productivity boom: 0.12** (unchanged)

No reweighting is made. H003 receives additional support from energy-supply persistence, but the new evidence still does not establish broad core-price persistence, credit deterioration, or the September policy outcome. Moving weights immediately before the already-frozen PPI/CPI tests would overfit a highly visible commodity shock.

## Skeptic
**Attack on leading H003:** The strongest contrary evidence is that high-yield credit spreads remained tight at 2.67% on Sep. 8 and the point forecast expecting wider spreads lost materially to its stale baseline. In addition, roughly 70% of economists in the Sep. 9 Reuters poll still expected a September hold. Oil above $100 can be a supply shock that compresses household purchasing power and future demand without producing persistent core inflation or immediate policy tightening. The S&P decline and higher long yields cannot identify H003 uniquely.

**Response:** The energy disruption is materially more persistent and physical than a transient spot-price move, so H003's inflation-risk pathway remains the narrow leader. But the model requires the already-frozen PPI/CPI and later demand/labor evidence to determine whether pass-through broadens or instead becomes growth-negative.

**What would surprise the current model:** a benign producer/consumer inflation sequence despite persistent energy stress would favor H001; broad underlying price strength would favor H003; sustained energy stress followed by widening credit spreads and clear labor/consumer deterioration would strengthen H002.

## Material model changes
**None.** Model v0.2.14 remains current. P000008 is a point-level miss with interval coverage and does not reveal a new causal edge beyond the existing credit-stress/financial-conditions branch. The Sep. 9 Treasury announcement response is consistent with the already-recorded distinction between announcement expectations and realized purchase flows; no new graph edge is added.

No new Universal transfer candidate is added. The relevant methodological lessons are already represented by anti-hindsight controls, baseline-relative attribution, ambiguous-endpoint discipline, and longitudinal out-of-sample learning criteria.

## Open forecasts
- **P000023:** 54% probability first-release August core CPI is >=0.3% m/m on Sep. 11; point 0.3%, 80% interval 0.1%-0.4%; frozen.
- **P000027:** 58% probability the FOMC raises both bounds by at least 25 bp at the Sep. 15-16 meeting; frozen. The Sep. 9 Reuters poll is new evidence, not a forecast rewrite or retroactive benchmark.
- **P000028:** 53% probability first-release August headline final-demand PPI is >=0.4% m/m on Sep. 10; point 0.4%, 80% interval -0.2%-0.9%; frozen at the Sep. 8 cutoff.

## New forecast
**None.** P000028 resolves the next morning and P000023 the following morning. Adding another highly correlated near-term inflation forecast would increase forecast count without adding enough independent discriminating information.

## Most important watch
**Friday Sep. 11 first-release August core CPI.** Sep. 10 PPI is the immediate upstream checkpoint, but P000023 remains the cleaner discriminator between H001 disinflation-with-resilience and H003 persistent underlying inflation/policy constraint.
