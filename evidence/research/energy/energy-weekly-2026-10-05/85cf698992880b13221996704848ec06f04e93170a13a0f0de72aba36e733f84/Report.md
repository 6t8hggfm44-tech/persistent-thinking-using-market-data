# Original Energy hypothesis test report — 28 September–4 October 2026

Run ID: energy-weekly-2026-10-05 · Version: 1 · Status: complete negative/inconclusive report

Generated at: 2026-10-05T18:13:50Z · Evidence cutoff: 2026-10-05T18:12:24.206454245Z · Requested event week: 2026-09-28T00:00:00Z to 2026-10-05T00:00:00Z

Workflow and scientific code: public Energy commit `28ea17c51a61f97e17aea6a4ac044a19a434fd98`. Prior exposure: a prior original-Energy report was consulted only after the current calculations and case selection, as a formatting reference. Suite Energy was known to share the same EIA family; no suite conclusion was treated as independent evidence.

## Finding and decision relevance

**OBSERVATION:** the deterministic screen registered no anomaly across the twelve configured U.S. EIA petroleum series at the predeclared absolute robust-z threshold of 3.5. The latest analyzable weekly endpoints were 19–25 September 2026, not the requested 28 September–4 October calendar week.

**OBSERVATION:** gasoline stocks were 204,362 thousand barrels, down 1,684 thousand barrels on the week and 7.40% below the comparable year-earlier level. Distillate stocks were 105,180 thousand barrels, down 2,251 thousand barrels and 14.89% below year-earlier. Their seasonal robust z-scores were -2.33 and -1.50, below the registered threshold.

**OBSERVATION:** crude production was 13,955 thousand barrels per day (+16 kb/d weekly), refinery input 16,257 kb/d (-554), utilization 92.5% (-1.5 percentage points), imports 5,698 kb/d (-179), and exports 3,570 kb/d (+289). Commercial crude stocks built 922 thousand barrels.

**INFERENCE:** the evidence does not support a registered broad petroleum anomaly. Low gasoline and distillate inventories and weekly draws are contrary evidence worth preserving, but the full set of seasonal scores, production, refining, trade, and product-supplied measures does not isolate scarcity, demand, maintenance, logistics, or weather as the cause.

**ASSUMPTION:** the restored database adequately represents the selected collector snapshot because its outer artifact, receipt/control linkage, manifest, restored bytes, SQLite integrity, and normalized row counts were verified. This does not establish historical first-release vintages.

**SPECULATION:** no price, margin, inflation, growth, transport, geopolitical, or trading consequence is inferred.

## Scope, vintage, and actual coverage

The newest completed byte-verifiable archive available before cutoff was staged 2026-10-04T19:10:23.411378Z from private state commit `304bafe8768c5be1b1f71367ca35dfd0529d32b0`, workflow run 37227167510, artifact 11311859897. The 7,836,973-byte artifact matched SHA-256 `80e0dd8bcab44ca38eb07aae2fa152944db913f39ce56d5b87da24e80ea2d82a`; the inner snapshot manifest matched `ed1bfe6af9da9ae6d665d2ba6b9f59d7034197779564f1684087088e1f26ad6b`. The restored 958,464-byte database matched `e07da82499f2c296fe7a91bfd3542c953a3a067a1323537ec0f47d67cee8dd7e` and passed `PRAGMA integrity_check`.

Each series supplied 288 weekly observations from 26 March 2021 through 25 September 2026; 3,456 normalized observations were independently counted. All twelve selected series had successful collector captures on 4 October. Values for 25 September were first observed in this archive on 30 September. Publication timestamps and provider vintages are unknown; these are current-vintage histories, not a historical-release-vintage backtest.

Measured coverage is twelve U.S. EIA petroleum series. EU gas was disabled because an authorized validated credentialed adapter was unavailable; LNG and electricity were unimplemented. A disabled jet-fuel source ID (`WJFUPUS2`) is not the active configured kerosene-type jet-fuel series (`WKJUPUS2`) and contributes no observation. Current Weather and GEV occurrences did not yield usable reports or controls.

## Measurements

| Series (week ending 25 Sep) | Level | Week change | Year change | Seasonal robust z |
|---|---:|---:|---:|---:|
| Commercial crude stocks | 427,320 kb | +922 kb (+0.22%) | +2.59% | +0.69 |
| Gasoline stocks | 204,362 kb | -1,684 kb (-0.82%) | -7.40% | -2.33 |
| Distillate stocks | 105,180 kb | -2,251 kb (-2.10%) | -14.89% | -1.50 |
| Strategic Petroleum Reserve | 283,767 kb | -785 kb (-0.28%) | -30.23% | -2.72 |
| Refinery crude input | 16,257 kb/d | -554 kb/d (-3.30%) | +0.55% | +0.37 |
| Refinery utilization | 92.5% | -1.5 percentage points | +1.20% | +0.47 |
| Crude production | 13,955 kb/d | +16 kb/d (+0.11%) | +3.33% | +1.19 |
| Crude imports | 5,698 kb/d | -179 kb/d (-3.05%) | -2.31% | -1.22 |
| Crude exports | 3,570 kb/d | +289 kb/d (+8.81%) | -4.83% | -0.34 |
| Gasoline product supplied | 8,689 kb/d | -158 kb/d (-1.79%) | +2.01% | -0.40 |
| Distillate product supplied | 3,948 kb/d | -27 kb/d (-0.68%) | +9.15% | +0.24 |
| Jet-fuel product supplied | 1,809 kb/d | +159 kb/d (+9.64%) | +3.97% | +0.95 |

Product supplied is a market-flow proxy, not measured end-user consumption. Stock and flow units are not mixed in any claimed identity.

## Hypotheses and verdicts

| Hypothesis | Discriminating prediction | Executed evidence | Verdict |
|---|---|---|---|
| H1 supply-driven | Production or net imports explain material inventory change | Production, imports, exports, refinery input, stocks, reduced-balance sensitivity | Not supported as a causal explanation |
| H2 demand-driven | Product supplied moves with product stocks | Weekly/year comparisons for gasoline, distillate, and jet fuel | Mixed; not sufficient to isolate demand |
| H3 maintenance/logistics | Refinery utilization/input or dated constraints align with the movement | Utilization/input comparison; no validated outage dataset | Partly consistent with lower refining, but unproven |
| H4 weather-linked | Matched weather control covaries with signal | Counterpart availability audit | Blocked: no usable current matched control |
| H5 measurement/revision | Vintage or duplication explains apparent anomaly | Row-hash, duplicate-date, capture, and vintage audit | Reproducible current vintage; historical revision test blocked |

## Executed and blocked tests

The pinned screen produced zero candidates; the strongest absolute score was the SPR at 2.72, and the strongest commercial-product score was gasoline at -2.33. All twelve series had 55 seasonally matched baseline observations.

Levels, weekly differences, comparable-year differences, and duplicate dates were recomputed directly from SQLite. No duplicate source/event date was found. The reduced crude-flow expression—seven times production plus imports minus refinery input and exports—was -1,218 thousand barrels, versus a +922-thousand-barrel commercial-crude change. The disagreement confirms that omitted adjustments, transfers, timing, and other balance components prevent use as an accounting identity or causal test.

No configured series endpoint fell within the requested 28 September–4 October event week. Gas/LNG/electricity, matched Weather/GEV controls, operator outages, regional logistics, historical first-release vintages, and price effects remained blocked or outside verified coverage. Their absence is an evidence gap, not a negative result.

## P01–P12 execution record

P01–P03 preserved the question, current steering, archive provenance, and registered roster. P04–P05 verified transport, receipt/control linkage, manifest, restored database, units, geography, vintages, missingness, and source lag. P06–P07 shortlisted supply, demand, maintenance/logistics, weather, and measurement explanations and selected the strongest feasible negative/inconclusive case. P08 predeclared H1–H5 and controls before screening calculations. P09–P10 executed the pinned screen, direct-SQL checks, year and week comparisons, reduced-balance sensitivity, duplication audit, and coverage/vintage audit. P11 froze the independent conclusion before any cross-domain reconciliation. P12 records the final conclusion, limits, and next decisive evidence in this report and the structured package.

## Reconciliation

No current GEV or Weather report was available for reconciliation. Their failed current occurrences are not confirming negatives. Suite Energy overlaps this EIA family and therefore cannot independently confirm the observations. No causal, corroboration, contradiction, or market-impact claim was added.

## Corrections, limitations, and next evidence

This is version 1 and supersedes nothing. Key limitations are source lag, current-vintage rather than historical-release-vintage data, absent gas/LNG/electricity coverage, absent matched Weather/GEV controls, no validated outage/logistics dataset, correlated EIA series, and an uncalibrated screening threshold.

The next decisive evidence would be the subsequent EIA release covering a period closer to the requested week, verified historical-release vintages, and independently available matched gas, electricity, weather, and operator evidence. Those belong to a future separately admitted occurrence; this report creates no retry or catch-up authority.

## Frozen conclusion and handoff

The independent conclusion is frozen as: **no registered U.S. petroleum anomaly was found. Gasoline and distillate stocks were materially below year-earlier levels and drew during the latest week, but no seasonal score crossed 3.5 and the available supply, refining, trade, and product-supplied measures do not isolate a cause. The latest source week ended 25 September, so the requested 28 September–4 October week remains unobserved.**

Only this reviewed report, its safe envelope, and transport packet may be staged for Market. Staging is not canonical receipt or forecast adoption. Raw collector bodies, private checkpoints, and operational identifiers remain private.
