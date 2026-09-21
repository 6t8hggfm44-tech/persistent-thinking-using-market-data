# Original Energy hypothesis test report — 14–20 September 2026

Run ID: energy-weekly-2026-09-21 · Version: 1 · Status: complete negative/inconclusive report

Generated at: 2026-09-21T18:19:15Z · Evidence cutoff: 2026-09-21T18:12:56Z · Requested event week: 2026-09-14T00:00:00Z to 2026-09-21T00:00:00Z

Workflow and scientific code: public Energy commit `28ea17c51a61f97e17aea6a4ac044a19a434fd98` · Independent Energy freeze: recorded with this package · Prior exposure: the current GEV report was known to be an evidence-gap report and the suite Energy petroleum summary was visible in this conversation; neither was used to select this case or calculate its results.

## Finding and decision relevance

**OBSERVATION:** the deterministic screen registered no anomaly across the twelve configured U.S. EIA petroleum series at the predeclared absolute robust-z threshold of 3.5. The latest analyzable weekly endpoints were 5–11 September 2026, not the requested 14–20 September calendar week, because the source series are reported with a lag.

**OBSERVATION:** gasoline stocks were 207,732 thousand barrels, 4.56% below a year earlier, and distillate stocks were 107,859 thousand barrels, 13.49% below a year earlier. Both nevertheless built during the latest week: gasoline by 794 thousand barrels and distillate by 1,585 thousand barrels. Their seasonally matched robust z-scores were -2.22 and -1.47, below the registered threshold.

**OBSERVATION:** refinery crude input was 17,330 thousand barrels per day and utilization 96.8%; both remained above year-earlier levels despite small weekly declines. Crude production was 13,944 thousand barrels per day and flat on the week. Crude exports rose 41.4% week over week to 4,831 thousand barrels per day, but their seasonal robust z-score was only +1.04.

**INFERENCE:** these data do not support a broad new petroleum scarcity anomaly. Below-year-ago product inventories merit monitoring, but weekly builds, strong refining, ordinary product-supplied measures, and sub-threshold seasonal scores are contrary evidence.

**INFERENCE:** the large export move is not sufficient to explain inventories. A deliberately incomplete flow diagnostic implied -8,113 thousand barrels for the week versus the observed commercial-crude change of -640 thousand barrels. Adjustments, transfers, refinery gains, timing and other balance components are missing, so no accounting or causal claim is made.

**ASSUMPTION:** the restored database is an adequate representation of the collector snapshot for the twelve normalized EIA series because its exact Git-stored bytes, manifest identity, SQLite integrity and row counts were verified. This does not establish first-release vintages or verify every raw source body.

**SPECULATION:** no price, margin, inflation, growth, transport or geopolitical consequence is inferred. Those would require separate matched evidence.

## Scope, source vintage and actual coverage

The current private snapshot manifest was created at 2026-09-20T18:29:34.066667Z from collector state commit `313312f2f78776ca63b8c68beff88674eba91557`. The bounded 20 September collector attempt reported 12 successful Energy requests and zero failed requests. The exact 909,312-byte `energy.sqlite` object was materialized through the authorized private Git route, matched SHA-256 `849240af1fa5728793c63e9c5ccafad228667dd0ce5c6b31de3cfea40b37af53`, passed SQLite `integrity_check`, and independently reproduced 73 capture rows and 3,432 observation rows.

The latest values analyzed were first observed in this archive on 17 September 2026 and refer to periods ending 11 September. Each of the twelve series had 55 seasonally matched baseline observations, with available history from 26 March 2021. No duplicate event date was found. A later capture of historical observations is not proof of first-release vintage, so revision-sensitive claims remain limited.

Measured coverage is twelve U.S. EIA petroleum series. GIE EU gas storage was not enabled because the required authorized credentials and validated live adapter were absent. ALSI LNG and electricity are unimplemented. Gas, LNG and electricity therefore remained untested, and this report is not a global energy assessment.

The private Actions artifact reference could not be materialized in this runtime (HTTP 403). The authorized alternate private Git transport supplied the exact database bytes and manifest but not the full raw-object fileset. Thus this worker did not rehash all 72 raw bodies or reproduce the complete 134-file archive bundle.

## Shortlist and selected case

The shortlist comprised product-inventory tightness, unusually strong refining, crude trade-flow volatility and the possibility of a measurement/revision mix. The strongest defensible case was the negative test: **lower product inventories coexist with weekly builds and strong supply-side activity, without a registered seasonal anomaly**. This selection preserves contrary evidence and does not force a positive finding.

## Measurements

| Series (latest week ending 11 Sep) | Level | Week change | Year change | Seasonal robust z |
|---|---:|---:|---:|---:|
| Commercial crude stocks | 423,429 kb | -640 kb (-0.15%) | +1.94% | -0.05 |
| Gasoline stocks | 207,732 kb | +794 kb (+0.38%) | -4.56% | -2.22 |
| Distillate stocks | 107,859 kb | +1,585 kb (+1.49%) | -13.49% | -1.47 |
| Strategic Petroleum Reserve | 284,957 kb | -403 kb (-0.14%) | -29.77% | -1.76 |
| Refinery crude input | 17,330 kb/d | -256 kb/d (-1.46%) | +5.52% | +1.29 |
| Refinery utilization | 96.8% | -1.0 percentage point | +3.75% | +1.35 |
| Crude production | 13,944 kb/d | 0 | +3.43% | +1.16 |
| Crude imports | 7,058 kb/d | +234 kb/d (+3.43%) | +24.0% | +1.34 |
| Crude exports | 4,831 kb/d | +1,414 kb/d (+41.4%) | -8.45% | +1.04 |
| Gasoline product supplied | 8,798 kb/d | +247 kb/d (+2.89%) | -0.14% | -0.24 |
| Distillate product supplied | 3,501 kb/d | -177 kb/d (-4.81%) | -3.31% | -1.05 |
| Jet-fuel product supplied | 1,800 kb/d | +15 kb/d (+0.84%) | +10.91% | +0.86 |

Product supplied is a market-flow proxy, not measured end-user consumption. Inventory and flow units are not mixed in any claimed balance.

## Hypotheses and verdicts

| Hypothesis | Prediction / falsifier | Executed tests | Verdict |
|---|---|---|---|
| H01 broad petroleum scarcity | Low stocks coincide with unusual draws and weak supply | Seasonal screen, weekly/yearly comparisons | Not supported: product stocks were low year over year, but built weekly; no score crossed 3.5 |
| H02 strong supply with ordinary demand | Refining/production/imports remain strong while product supplied is ordinary | Level, weekly, yearly and seasonal comparisons | Partly supported, descriptive only |
| H03 trade/revision/measurement mix | Flow volatility or incomplete balances explain apparent tension | Trade comparison, incomplete balance diagnostic, duplicate-date audit | Supported as caution; not a causal finding |
| H04 weather or cross-domain driver | Matched weather/GEV exposure and timing discriminate the case | Counterpart input audit | Untested: both counterpart reports contained no measurement finding |

## Executed and blocked tests

**Deterministic threshold screen.** The pinned public code screened twelve series over seven requested days and produced zero candidates. Threshold choice was predeclared at absolute robust z 3.5; the strongest score was gasoline stocks at -2.22.

**Independent number check.** Levels, weekly differences, year-over-year comparisons, baseline counts and duplicate event dates were recomputed directly from the restored SQLite database rather than copied from prose. The complete normalized observation table had 3,432 rows.

**Balance sensitivity.** Production plus imports minus refinery input and exports equaled -1,159 thousand barrels per day, or -8,113 thousand barrels for seven days, far from the -640-thousand-barrel commercial-stock change. This falsifies using that reduced expression as an accounting identity.

**Vintage/revision audit.** Capture ancestry and first-observed times were retained. Exact first-release values and later revisions could not be separated from the available current-vintage history, so no revision-resilient surprise is claimed.

**Requested-week coverage.** No configured series had an endpoint inside the 14–20 September requested event week. The report therefore labels its latest measured week separately and makes no claim that it observed the full requested week.

**Gas, LNG, electricity, weather and GEV controls.** Blocked or unimplemented. The contemporaneous Weather and GEV reports are complete evidence-gap reports, not confirming negatives, so no cross-domain linkage test was possible.

## P01–P12 execution record

P01–P03 preserved the question, provenance and registered twelve-series roster. P04–P05 established archive identity, source lag, units, vintages and actual coverage. P06–P07 shortlisted competing explanations and selected the strongest feasible negative case. P08 predeclared H01–H04 and T01–T06 before the final calculations were assembled. P09–P10 executed the deterministic screen, independent database checks, seasonal comparisons, balance sensitivity and vintage/coverage audit. P11 froze the independent Energy conclusion before using complete counterpart envelopes. P12 records the final conclusion, limits, corrections and next decisive evidence here and in the structured package.

## Reconciliation

The complete current GEV and Weather envelopes were hash-audited as inputs. Both reports are evidence gaps: GEV lacked readable current review exports, and Weather lacked readable measurement values. Neither supplies an event, exposure, sign or magnitude that can be aligned to the petroleum observations. No causal, corroboration or contradiction claim follows. The suite Energy report uses the same EIA ancestry, so any overlap is one source family rather than independent confirmation.

## Corrections, limitations and next decisive evidence

No correction was required to a prior version because this is version 1. Key limitations are the source lag, current-vintage rather than historical-release-vintage observations, absent raw-object verification in this worker, missing gas/LNG/electricity coverage, and unavailable measured Weather/GEV controls.

The next decisive evidence would be the subsequent EIA release with a comparable pre-period baseline, verified historical-release vintages for revision analysis, and readable matched gas/electricity/weather inputs. Those belong to a future separately admitted occurrence; this report creates no retry or catch-up authority.

## Frozen conclusion and handoff

The independent conclusion is frozen as: **no registered U.S. petroleum anomaly was found; gasoline and distillate stocks were below year-ago levels but built during the latest week, while refining and production remained comparatively strong. The latest source week ended 11 September, so the requested 14–20 September week remains unobserved.**

Only this reviewed report, its safe envelope and transport packet may be staged for Market. Staging is not canonical receipt or forecast adoption. Raw collector bodies, private checkpoints and operational identifiers remain private.

