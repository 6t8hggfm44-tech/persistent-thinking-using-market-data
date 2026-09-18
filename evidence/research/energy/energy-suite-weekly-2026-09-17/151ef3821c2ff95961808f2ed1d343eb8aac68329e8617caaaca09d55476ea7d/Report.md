# Energy supply, demand and physical stress

## Summary

This exploratory weekly investigation found lower year-over-year U.S. petroleum inventory levels but not an unusually sharp latest four-week draw. Commercial crude was 0.14% below its year-ago level, gasoline 5.94% lower, and distillate 11.91% lower for the week ending September 4, 2026. Yet their latest four-week changes ranked near the middle of the available current-vintage history (approximately the 53rd, 51st, and 49th percentiles), so the predeclared strict broad acute-tightness hypothesis was not supported.

Refinery crude input averaged 17.468 million barrels per day over the latest four weeks, 3.09% above the matched year-ago window, and utilization was 2.5 percentage points higher. In contrast, gasoline, distillate, and jet-fuel product supplied were 1.41%, 2.58%, and 2.30% lower. The registered stronger-activity conjunction therefore failed. Production rose by 435.75 thousand barrels per day year over year on the matched four-week basis, larger than the measured increases in imports (150.25 thousand b/d) and exports (236.75 thousand b/d), but this is descriptive context rather than a closed balance or causal result.

No new source requests were made. Natural-gas storage and electricity tests remained untested because their preserved source bodies/tables were unavailable and both sources were inside their collection intervals.

## Coverage

The run verified and used the private repository's preexisting petroleum bridge at commit `55513cafd11d32a8f3de3df4d15846c8c0d52084`, manifest SHA-256 `d4540aa7d28d2c4496872b75143d3b7705f2b67d2c3041e2f09eb346f2dbd383`. It contains 12 U.S. EIA weekly series and 3,420 observations (285 per series), covering week endings March 26, 2021 through September 4, 2026. All 16 manifest entries and all 3,420 original row hashes matched.

These are current-vintage histories first captured September 14, 2026. They do not reconstruct what earlier releases showed or when each historical value was originally published. All petroleum series share the `EIA_US_weekly_petroleum` source family and count as one dependent evidence family.

The full roster was reviewed: petroleum stocks, production, imports/exports, refinery input/utilization, and product-supplied proxies were testable. Gas storage, electricity demand/load, power prices/grid stress, and industrial-energy consumption were not testable from available bytes. The existing-energy final-report reuse test was also blocked because no eligible finalized parent report was available.

## Hypotheses and tests

**Inventory tightness — not supported under the strict rule.** OBSERVATION: all three tested stocks were below year-ago: commercial crude 424.069 million barrels (-0.14%), gasoline 206.938 million (-5.94%), and distillate 106.274 million (-11.91%). OBSERVATION: the corresponding latest four-week changes were -0.341 million, -1.752 million, and -0.875 million barrels, but each sat near the historical median rather than at or below the registered 10th-percentile threshold. INFERENCE: stock levels were relatively leaner, especially for distillate and gasoline, but the latest month did not show an exceptional broad draw in this dataset.

**Throughput/activity — mixed; stronger-activity conjunction failed.** OBSERVATION: refinery input rose 3.09% year over year and utilization rose 2.5 percentage points. OBSERVATION: gasoline, distillate, and jet-fuel product supplied declined 1.41%, 2.58%, and 2.30%. INFERENCE: high refinery throughput did not coincide with the registered broad product-supplied increase. ASSUMPTION: product supplied is treated only as an imperfect activity proxy; it is not final consumption.

**Supply context — production was the largest measured change.** OBSERVATION: matched four-week average production increased 435.75 thousand b/d, versus increases of 150.25 thousand b/d in imports and 236.75 thousand b/d in exports. The registered descriptive rule therefore classified production as the dominant measured supply change. INFERENCE: this does not explain the inventory pattern by itself because the analysis omits refinery yields, adjustment terms, product imports/exports, and other balance components.

**Gas and electricity — untested.** No claim was made about gas-storage abnormality, electricity demand, grid stress, power prices, or industrial activity. The collector correctly authorized zero requests because both expansion sources were not due, and prior capture bodies were unavailable.

## Limitations

- Historical release vintages and original publication timestamps are unknown; current history may include revisions.
- Raw EIA publisher bodies were not in the bridge. This run verified derived bytes, manifest entries, capture lineage, and row hashes, not a fresh raw-body parse.
- Petroleum categories are correlated and share one EIA methodology; they are not independent confirmations.
- Four-week and year-over-year comparisons are unadjusted for seasonality, weather, calendar effects, exports, outages, refinery yields, or category mix.
- Product supplied is not identical to end-user demand or economic output.
- The bridge is evidence, not a finalized inherited report. No prior final conclusion was reused.
- Gas/electricity missingness prevents a full-domain conclusion. This report should not be read as evidence that broader energy stress is absent.

## Sources

All measurements derive from the EIA weekly petroleum series listed in the source register: commercial crude and SPR stocks; gasoline and distillate stocks; crude production, imports, exports, and refinery input; refinery utilization; and gasoline, distillate, and jet-fuel product supplied. Exact EIA URLs, original capture hashes, retrieval times, units, bridge-table paths, and shared ancestry are preserved in `source-register.json`. Detailed executed values and formulas are preserved in `calculations/petroleum-bridge-tests.json` and `test-results.json`.

No external source was contacted during this run.

## Next decisive evidence

The next decisive evidence is a genuinely new, due WNGSR release with its dated storage table and comparators, plus selected matched EPM numeric tables when due. Those would allow the predeclared gas-storage and electricity tests without bypassing cooldowns. For petroleum, a later separately versioned bridge can test revisions prospectively; the current bridge must remain immutable and must not be recollected or counted as a second source family.
