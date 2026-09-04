# Current Market State

**Model version:** 0.2.14  
**Status:** Friday post-close weekly review; P000025 resolved/scored before evidence intake; Sep. 4 evidence ingested; labor-measurement bridge revised; P000027 issued  
**Evidence cutoff:** 2026-09-04T17:21:38-04:00

## Auditor
P000025 resolved against the first 2026-09-04 BLS Employment Situation release. August nonfarm payrolls rose **162,000** and unemployment was **4.1%**, so the precommitted joint event `payrolls <=25K AND unemployment >=4.2%` was **FALSE**.

P000025 probability score: **Brier 0.1024**, **log loss 0.385662**. The binary probability beat a neutral 0.50 comparator, but the continuous payroll forecast failed materially: the 38K point missed by **124K** and the realized value was outside the -45K to 130K 80% interval. Both frozen external payroll points were closer (45K error 117K; 65K error 97K); the model did beat the -23K no-change payroll point (185K error). The 4.2% unemployment point missed by 0.1 pp and its 4.0%-4.4% interval covered. The forecast's precommitted surprising condition—payrolls >=125K with unemployment <=4.1%—occurred.

Lifetime probability scoring is now **n=18**, mean Brier **0.209344**, mean log loss **0.608217**. The precommitted 30-resolution threshold remains unmet; **learning cannot yet be inferred**.

## Observations
- BLS reported August payrolls **+162K**, unemployment **4.1%**, participation **61.6%**, household employment +569K, average hourly earnings **+0.3% m/m / +3.1% y/y**, and upward June/July payroll revisions totaling **55K** versus the prior release.
- Payroll gains were concentrated: food services/drinking places +59K and local-government education +42K; information lost 23K.
- Reuters reported Brent at **$92.68** and WTI at **$91.48** at Friday settlement, up **7.6%** and nearly **10%** on the week amid renewed U.S.-Iran fighting.
- Reuters reported Fed-funds futures pricing about a **61%** probability of a September rate hike after the jobs release, up from 52% beforehand. This is a market benchmark, not a Fed decision.
- U.S. equities closed modestly lower after the jobs report; this endpoint is retained as context and is not used as a clean causal identifier.

## Inference
The labor state must be narrowed. The **low-layoff** leg remains well supported by claims, but the stronger claim that weak JOLTS/ADP/survey hiring signals implied very weak near-term BLS net payroll growth failed its direct prospective test. The monthly payroll stock change is not interchangeable with any one gross-hiring proxy; it depends jointly on hires, separations, sector composition, establishment coverage/seasonality, and later revisions. The model therefore changes from **low-hire/low-fire** as a near-term payroll characterization to **low layoffs + mixed/asynchronous hiring indicators + stronger realized net payroll growth**.

The same employment release is not uniquely benign. Stable unemployment, higher participation, and moderate 3.1% wage growth support H001, while resilient labor combined with renewed energy pressure and a higher expected policy path supports H003's policy-constraint branch. The August CPI release remains the cleaner test of whether this resilience is compatible with continued underlying disinflation.

## Hypothesis weights
- **H001 Soft landing: 0.35** (from 0.34)
- **H002 Late-cycle recession: 0.15** (from 0.18)
- **H003 Fiscal/inflation regime: 0.38** (from 0.36)
- **H004 Productivity boom: 0.12** (unchanged)

The three-point H002 reduction is driven by the direct P000025 surprise plus the separately observed low-claims backdrop and upward prior-payroll revisions. One point moves to H001 because labor resilience with moderate wage growth is compatible with a soft landing; two points move to H003 because resilient demand now coincides with renewed energy pressure and a market-implied tighter policy path. H004 receives no weight from employment growth because the release does not measure productivity.

## Skeptic
**Attack on leading H003:** The employment headline is not clean inflation evidence. Wage growth is only 3.1% y/y, participation rose, and part of the payroll gain is concentrated in food services and local-government education. Oil is volatile and its pass-through to core CPI is lagged/state-dependent. A one-day shift in futures odds is a market reaction, not the Fed's decision. A single strong payroll print can also be revised and does not erase weak household/housing evidence or July JOLTS.

**Response:** The case for H003 does not rest on payrolls alone. The relevant joint observation is resilient labor plus previously strong services demand, renewed oil/input-cost pressure, and a Fed reaction function already focused on inflation. That combination makes a still-binding policy constraint more plausible than it was yesterday. The Skeptic prevents a larger H003 increase and leaves H001 close pending CPI.

**What would surprise the current model:** first-release August core CPI <=0.1% m/m alongside continued labor resilience and retreating energy/policy expectations would materially favor H001 over H003. Conversely, core CPI >=0.4% with labor still resilient would strengthen H003 substantially.

## Material model changes
**v0.2.14 — net-payroll measurement bridge refinement.** P000025's precommitted surprise showed that the prior model over-translated weak gross-hiring/proxy evidence into a weak BLS net-payroll point forecast. The causal graph now explicitly separates gross hiring, separations, and the BLS monthly net-payroll stock change, with sector composition/coverage/seasonality as a bridge. Initial claims remain evidence about separations; JOLTS hires remain evidence about gross hiring; neither alone is treated as a sufficient statistic for monthly CES net payroll growth. This change is error-linked and receives **zero learning credit** until forecasts generated under it resolve.

No change is made to the AI-investment/productivity separation, Treasury flow-timing correction, or household-demand branches.

## Learning status
Across 18 probability forecasts, lifetime mean Brier is **0.209344** and log loss **0.608217**, descriptively better than neutral-0.50 losses (Brier 0.25; log loss 0.693147). The latest six have mean Brier **0.177850** and log loss **0.539506**, versus earliest-six **0.227400 / 0.647876** and middle-six **0.222783 / 0.637268**. This numerical improvement is **not evidence sufficient to claim learning**: n=18 is below the precommitted 30 threshold, target/horizon composition is heterogeneous, outcomes are dependent, and the Aug. 28 review showed how a tiny recent window can reverse sign quickly.

Calibration remains too sparse for recalibration. Mean assigned event probability is about 0.466 versus an observed event frequency of 6/18 = 0.333. P000025 also breaks the prior perfect interval record on its payroll component: under a strict forecast-record rule requiring all component intervals to cover, interval coverage is now **15/16 = 93.75%**; the unemployment interval covered while the payroll interval did not. Cross-unit interval widths are not pooled, and coverage is not interpreted without sharpness.

The strongest positive evidence for a recent model change is P000024's successful post-v0.2.8 national-manufacturing forecast after the regional-to-national safeguard; it is only one test. P000026 supported the low-layoff separation branch, while P000025 contradicted the stronger low-hiring-to-net-payroll magnitude implication. The labor refinement therefore has **mixed** subsequent evidence rather than a clean success narrative.

## Open forecasts
- **P000023:** 54% probability first-release August core CPI is >=0.3% m/m on Sep. 11; point 0.3%, 80% interval 0.1%-0.4%. This remains the highest-information immediate H001-vs-H003 discriminator.
- **P000027:** 58% probability the FOMC raises the federal-funds target range by at least 25 bp at the Sep. 15-16 meeting; frozen Reuters/Fed-funds-futures comparator 61% at the Sep. 4 cutoff.
- Legacy P000003 and P000006-P000009 resolve Sep. 8 under their original rules.

## Most important watch
**First-release August core CPI on Sep. 11.** The labor branch has just moved sharply away from immediate recession. The next high-information question is whether resilient activity can coexist with benign underlying inflation (H001) or whether underlying inflation remains sticky enough to validate H003's policy-constraint lead. PPI on Sep. 10 is useful intermediate evidence, but P000023 remains frozen and will not be altered by it.
