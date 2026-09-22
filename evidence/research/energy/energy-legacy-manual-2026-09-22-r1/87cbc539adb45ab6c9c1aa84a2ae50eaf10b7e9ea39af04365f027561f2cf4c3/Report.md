# Original Energy hypothesis test results — lagged petroleum week and sensitivity limits

Report ID: energy-legacy-manual-2026-09-22-r1 · Version: 1 · Status: completed negative/inconclusive investigation. Authorized manual dress rehearsal; no scheduled occurrence consumed.

Requested week: 15–21 September 2026 UTC, ending 22 September exclusive. Knowledge cutoff: 2026-09-22T18:32:18.824529+00:00. Generated: 2026-09-22T19:06:12.920892+00:00. Actual latest source week: **5–11 September 2026**, with week-ending dates rather than invented measurement instants. Workflow and scientific code: `28ea17c51a61f97e17aea6a4ac044a19a434fd98`, version 1.0.0. Supersedes: none.

## Findings and economic relevance

No series crossed the registered absolute robust-z threshold of 3.5 among the twelve U.S. EIA petroleum series. **This is a lagged, threshold-dependent descriptive result, not evidence that the requested week was normal or that scarcity is absent.** All latest endpoints are 11 September; none lies in 15–21 September.

Gasoline stocks are the strongest inventory lead: 207,732 thousand barrels, with primary seasonal score −2.22 and a weekly build of 794 thousand barrels. A narrower ±21-day seasonal band produces z = −3.26, crossing the predeclared sensitivity threshold 3.0 but not the original 3.5 threshold. This weakens any blanket reassurance from “zero flags.” Distillate stocks also built by 1,585 thousand barrels; refinery input remained 17,330 thousand barrels/day and utilization 96.8%. These are contrary evidence to an unsupported broad new supply-collapse story, while specific disruptions or demand effects remain untested.

The source is the [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/) family and its official historical series. Multiple series and the separate suite Energy producer share EIA ancestry; they do not provide independent confirmation. No price, margin, inflation, growth, transport, military or trading conclusion is established.

## Actual coverage and vintages

| Source / scope | Actual evidence | Vintage and coverage limit |
|---|---|---|
| Twelve EIA U.S. petroleum series | 286 weekly values each, 26 March 2021–11 September 2026; latest nominal reporting week 5–11 September | Zero requested-week endpoints; 11-day age at cutoff; stocks are end-period levels, rates retain kb/day units |
| Saved captures | 85 records: 84 successful, one historical failed attempt; captures 14 September 13:59:36Z–21 September 20:16:43Z | All 84 successful raw bodies pass verification; a daily check does not create daily observations |
| Latest normalized value versions | First seen on 17 September, 19:31:41Z–19:32:41Z | Original publication time and provider vintage are null/unknown, not inferred from capture or period date |
| GIE EU gas | Disabled in the effective configuration | Authorized credential/live validation not established in this round; no values analyzed |
| ALSI LNG and electricity | Not implemented in this pilot | Unobservable here, not zero activity |

The normalized archive has 3,432 rows and 3,432 distinct source-period keys, with no retained multi-value revision sequence. Each series has complete retained weekly spacing in the analyzed history; the 20,000-row input and 1,000-capture-register caps were not reached. This does not recover overwritten vintages before collection began. Worldwide official lead discovery was not performed outside the saved U.S. pilot. No fresh provider request, collector or credential operation occurred.

The pinned CLI conservatively serializes the evidence cutoff to `2026-09-22T18:32:18Z`, omitting the final 0.824529 seconds. No capture falls in that interval; the declared original cutoff is preserved and no evidence was refreshed after it.

## Shortlist and measurements

The fixed twelve-series roster and seasonal ranking were registered before either domain's archive calculations. Gasoline's largest absolute primary score, product inventory consistency and trade-flow volatility form the feasible shortlist. The selected case is gasoline inventory tightness under alternative seasonal bands, with supply/demand context and contrary weekly builds. It is exploratory, not a prospective surprise or held-out confirmation.

All levels below refer to the week ending **11 September**. Changes use an actual observation exactly seven days earlier, **4 September**. kb means thousand barrels.

| Series | Latest level | Weekly change | Unit | Primary robust z |
|---|---:|---:|---|---:|
| Commercial crude stocks | 423,429.0 | -640.0 | kb | -0.05 |
| Gasoline stocks | 207,732.0 | +794.0 | kb | -2.22 |
| Distillate stocks | 107,859.0 | +1,585.0 | kb | -1.47 |
| Strategic petroleum reserve crude stocks | 284,957.0 | -403.0 | kb | -1.76 |
| Refinery crude input | 17,330.0 | -256.0 | kb/day | 1.29 |
| Refinery utilization | 96.8 | -1.0 | percent; change in percentage points | 1.35 |
| Crude production | 13,944.0 | -3.0 | kb/day | 1.16 |
| Crude imports | 7,058.0 | +234.0 | kb/day | 1.34 |
| Crude exports | 4,831.0 | +1,414.0 | kb/day | 1.04 |
| Gasoline product supplied | 8,798.0 | +247.0 | kb/day | -0.24 |
| Distillate product supplied | 3,501.0 | -177.0 | kb/day | -1.05 |
| Jet fuel product supplied | 1,800.0 | +15.0 | kb/day | 0.86 |

The [gasoline inventory history](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WGTSTUS1&f=W) supports the selected stock case. The [crude production history](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCRFPUS2&f=W) supports the exact −3 kb/day correction discussed below. Product supplied is a disposition-based proxy; it is not direct measured end-user consumption.

## Hypotheses and executed tests

The original plan was registered at 18:33:57.373049Z on 22 September. All selection rules and test parameters were fixed then. The same analyst subsequently authored and froze Weather before reading Energy data; its limited negative weather screen is therefore known background, not an untouched independent-blind condition. No Weather values, GEV findings or Market outcomes were joined to these calculations or used to alter the Energy plan. That prior exposure limits claims of analyst blindness; deterministic energy-only calculation and predeclared selection remain intact.

| Hypothesis | Prediction / falsifier | Actual test and verdict |
|---|---|---|
| E-H1: physical supply constraint | Coherent stock draws and weak supply plus independent outage evidence; contrary supply/stock evidence weakens it | E-T3/4 show product builds and no 3.5 flag. Broad scarcity interpretation weakened; specific outage causation untested. |
| E-H2: demand change | Product proxies align with independently measured end demand after controls; contrary independent demand falsifies it | Proxies move differently by product. Independent demand absent: inconclusive. |
| E-H3: ordinary seasonal operations, maintenance, weather or trade | Matched controls explain a movement; persistent controlled deviation contradicts it | Seasonal bands tested, other controls absent. Plausible alternative, not established cause. |
| E-H4: timing, estimation or revision explains apparent deviation | Source-period/vintage mismatch changes interpretation; stable aligned independent evidence weakens it | Lag and incomplete balances verified. First-release revision explanation remains untested. |

**E-T1, integrity and replay:** SQLite integrity and all 84 successful raw-object SHA-256 checks passed. Both actual CLI report runs passed their three-member manifests, and all scientific output fields agree after excluding actual generation timestamps. This verifies reproducibility, not causal truth.

**E-T2/3, independent calculations:** a separate read-only SQL and arithmetic path exactly matches all 12 latest levels, weekly changes, primary baseline counts and robust scores. A separate HTML cell parser matches all 24 latest/previous values against the latest captured official bodies. The primary ±35-day seasonal baseline has 55 observations per series and excludes event dates on or after **5 September**, before the actual analyzed week. Score = (value − median)/(1.4826 × median absolute deviation). This is an uncalibrated current-vintage comparison, not a tail probability.

**Sensitivity:** ±21, ±35 and ±49-day bands have 33, 55 and 77 observations per series. Gasoline scores are −3.26, −2.22 and −1.75. Only gasoline in the narrow band crosses |z| = 3.0; none of the 36 series-band comparisons crosses 3.5 or 4.0. Related series and repeated bands are dependent. Missing holiday and maintenance controls prevent treating the sensitivity result as a causal demand or supply finding.

**E-T4, incomplete balance diagnostic:** 7 × (production + imports − exports − refinery input) = **−8,113 kb**, versus observed commercial crude stock change **−640 kb**. The residual, observed minus diagnostic, is **+7,473 kb**. Inputs share the same week, but adjustment and other balance components are omitted. The mismatch rejects using this reduced expression as an accounting identity; it cannot identify which omitted component caused it. Export growth of 1,414 kb/day alone does not explain stocks.

**E-T5, vintages and correction:** no source-period has multiple retained value versions, so this archive cannot test a first-release revision path. Unknown does not mean unrevised. Direct SQL and raw HTML show production of 13,944 kb/day versus 13,947 the prior week: **−3 kb/day (−0.02151%)**, rather than exactly flat. The former report's zero-change wording is an arithmetic/reporting correction; no retained revision sequence supports blaming a provider revision.

**Blocked tests:** independent outage/operator reports, holiday/maintenance matching, measured final demand, full-release vintage history, weather adjustment, GEV cargo/transport verification and downstream economic effects. No failed or planned test is counted as a completed causal test.

## Physical interpretation and reconciliation boundary

Stocks, refining, production, imports/exports and product-supplied proxies describe different parts of the petroleum system. Refinery utilization is a percentage of operable capacity, not a volume. Strategic reserve changes need not indicate commercial market tightness. The data retain these distinctions; no forced stock-flow equality or national weather weighting was applied.

No cross-domain linkage test ran before this Energy freeze. National petroleum volumes require compatible exposure weights and operational outcomes; a few weather grid points or a trajectory cannot establish national demand or cargo quantities. Current GEV and suite Energy report content has not been read. Reconciliation will be a separately hashed artifact with the exact frozen counterpart versions, compatible source periods, controls and shared ancestry; original reports remain unchanged.

## Changes, decisive evidence and handoff

Compared with `energy-weekly-2026-09-21`, report hash `bd9cd24980b0fe56c95966311808e0bda6fc416a2d6e148233f575b18d55aff8`, the latest measured week and levels remain the same. The new round adds complete raw verification, actual replay, declared seasonal sensitivity and the exact production-change correction. It does not turn an unchanged weekly observation into new independent evidence, and it does not rewrite the older report's availability. No year-over-year calculation from prior prose is used as a new test here.

The next decisive evidence is the next genuinely new EIA weekly endpoint with the same pre-period seasonal rules, plus independent operator/demand evidence and full balance components. A later authorized report should test whether gasoline remains below its seasonal median and whether any new departure crosses the unchanged 3.5 primary threshold. No directional forecast is issued for that unseen release. This report creates no collection, retry, extra Market cycle or schedule.

The finished private package binds the original plan, source register, exact commands, screen/replay verification, independent audit, coverage, competing hypotheses and correction record. Effective config SHA-256: `89d10ce0ac27f14af370c7fee4c9bcb9da91c362ea4b410f4113450f4ed1cc2c`; workflow SHA-256: `bc458b17415a8b133cf2c1a9dcdb971ec7cee69df07dbdb8cc3d12a1d7c7d41b`. Source queries and raw-body hashes are preserved privately, with the [EIA source family](https://www.eia.gov/petroleum/supply/weekly/) identifying the common measurement origin.

Final hashes and the actual domain freeze timestamp are in the envelope/freeze record. Immutable persistence, staging and actual receiver acknowledgment belong to the external delivery ledger; this frozen report claims no receipt. Only approved final prose and safe transport metadata enter the Market handoff. The existing regular Market cycle retains its own as-of and validation rules.
