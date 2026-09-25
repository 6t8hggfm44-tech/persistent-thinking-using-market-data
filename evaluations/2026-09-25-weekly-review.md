# Weekly Learning Review — 2026-09-25

**Evidence cutoff:** 2026-09-25T21:16:11Z
**Model before/after:** v0.2.14 / v0.2.15
**Forecasts resolved today:** none
**Lifetime resolved probability forecasts:** 22
**Learning status:** **INSUFFICIENT EVIDENCE TO ASSESS LEARNING**

## 1. Scoring before belief update

No open forecast had reached its precommitted resolution horizon before evidence intake. P000029 resolves October 14; P000004 and P000005 resolve later. No original forecast content, outcome, benchmark or resolution rule was altered.

The validated probability ledger therefore remains n=22, mean Brier 0.212214 and mean log loss 0.614555. A fresh Repo B record is required after the primary commit even though the ledger did not change.

## 2. Benchmark and calibration audit

Lifetime Brier skill versus neutral p=0.50 remains +0.1511 and log-loss skill +0.1134, but neutral 0.50 is not the strongest target-specific benchmark and the 22 forecasts share macro states and target families. The seven resolved S&P point forecasts retain mean model MAE 47.896 versus 46.266 for matched no-change, point skill -0.0352.

The probability vintage comparison is numerically favorable recently: first 10 Brier/log loss 0.214740 / 0.621654 versus last 10 0.196760 / 0.580935; earliest six 0.227400 / 0.647876 versus latest six 0.175967 / 0.536558. These windows differ in target/horizon mix and are strongly dependent, so they do not identify learning.

Strict record-level 80% interval coverage remains 20/22 = 90.9%, above nominal and therefore still a conservatism/sharpness warning. Cross-target interval width cannot be pooled because units differ.

## 3. Evidence intake and ancestry

Four complete pending packets were canonically received only in this cycle: Freight weekly v2, Agriculture weekly, Geopolitics weekly, and Suite Energy weekly. Exact staged bytes and hashes matched. All four are reused-evidence, evidence-gap, or no-new-release reports and add zero fresh macro observations. Port LA cells and EIA petroleum ancestry are explicitly deduplicated; access failure and missing tables are not converted into reassuring evidence.

Fresh post-cutoff observations are recorded in `evidence/2026-09-25-cycle.md`: initial claims 197K; August new-home sales 684K with July revised to 643K; core capital-goods orders +1.6% m/m; GDPNow 5.0% SAAR; final Michigan sentiment 48.1 with one-year inflation expectations 4.6%; official September 24 10-year Treasury par yield 5.18%; and Friday oil at Brent $104.32 / WTI $92.41.

## 4. Skeptic against H003

H003 remains the leading pre-update hypothesis, but the strongest contrary case is substantial:

1. Elevated yields and inflation expectations are downstream proxies and cannot by themselves identify fiscal impulse or realized inflation.
2. Oil fell Friday and WTI fell about 8% for the week; route normalization or diplomacy can truncate energy pass-through.
3. August new-home sales are noisy and still show 8.5 months of supply plus lower year-over-year median price; resilient sales do not establish broad housing strength.
4. Core capital-goods strength is concentrated in an AI/capex-heavy segment and is not realized economy-wide productivity.
5. Sentiment is extremely weak, so strong current spending/output can coexist with a later household slowdown.

The Skeptic therefore blocks a large H003 increase and blocks any new causal edge from these endpoints.

## 5. Model update

A small reweight is justified after scoring:

- H001 Soft landing: 0.35 -> 0.36
- H002 Late-cycle recession: 0.15 -> 0.12
- H003 Fiscal/inflation regime: 0.38 -> 0.40
- H004 Productivity boom: 0.12 -> 0.12

The H002 reduction is driven by multiple separate post-cutoff observations: 197K initial claims, the upward July new-home-sales revision plus August 684K sales, strong core capital-goods orders, and a 5.0% GDPNow nowcast. One point transfers to H001 because real-side resilience is compatible with a soft landing. Two points transfer to H003 because the same strong demand arrives with 5%+ long yields, higher consumer inflation expectations and still-elevated energy prices, keeping the policy/inflation constraint active.

Model v0.2.15 records a revision-awareness refinement: later official revisions can change present-state evidence weight, but they never alter a frozen forecast's original evidence set or first-release resolution rule. The July new-home-sales revision is the concrete trigger. No new causal-graph edge is added because the existing demand, housing, inflation, energy and rate channels are sufficient.

## 6. Error diagnosis and learning test

- v0.2.8 regional-to-national manufacturing safeguard: still one direct favorable post-change test, P000024, too little for learning credit.
- v0.2.7 sticky-reemployment formulation: P000020 remains direct negative evidence and stays narrowed.
- v0.2.13 inflation/policy discriminator: P000023 and P000027 remain mixed-positive; P000027 lost to frozen market comparators.
- v0.2.14 net-payroll bridge: still lacks a direct later monthly-payroll forecast generated under the bridge, so it receives zero predictive-learning credit.
- v0.2.15 revision-awareness is a state-integrity correction, not a predictive improvement claim.

At n=22, below the precommitted 30-resolution threshold, the system cannot claim learning. Better recent proper scores may reflect luck, target mix, regime change, dependence, or increasing conservatism. Negative S&P point skill and over-nominal interval coverage remain counterevidence to any broad performance claim.

## 7. Forecast decision

No new forecast is added to the public repository in this run. The model identified the September 30 first-release August core-PCE release as a high-information discriminator, but the connected write path rejected the attempted probabilistic forecast record. The run therefore does not pretend that a new forecast was durably registered. Existing P000029 remains the highest-information frozen near-term forecast.

## 8. Transferability review

No new Universal transfer candidate is added. Revision-vintage separation is already an application of active source-layer, workflow-state, hindsight and immutable-record safeguards rather than a new cross-domain principle.

## 9. Most important watch

September 30 core PCE is the next major discriminator for whether strong real-side activity is coexisting with sticky underlying inflation. Until a prospective forecast is durably registered, it is treated as a watch item rather than a scored prediction.
