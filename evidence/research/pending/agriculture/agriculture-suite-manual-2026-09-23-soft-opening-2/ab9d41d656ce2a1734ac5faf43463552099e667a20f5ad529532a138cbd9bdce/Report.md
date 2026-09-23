# Agriculture: no fresh supply evidence; table test remains blocked

## Summary

This September 23 manual investigation finds no new evidence with which to attribute agricultural supply changes. The repaired table-first procedure is installed, but its live acceptance test remains blocked: the selected two-vintage U.S. corn balance has **0 of 14 required cells**. Existing source cooldowns were preserved, so this run made **zero publisher requests** and acquired **zero fresh numeric observations**.

The feasible work is an exploratory re-audit of eight reviewed cells retained from September 22. It reproduces the earlier source-quality discrepancy and adds no independent evidence contribution. This is a final evidence-gap report, not a finding that agricultural conditions were unchanged.

## Coverage

The selected economic question is whether supply, demand or bookkeeping explains a revision to the U.S. corn 2026/27 marketing-year balance between August and September WASDE releases. Neither retained WASDE nor NASS evidence contains the necessary numerical tables. The exact units, dated attachment destinations and compatible comparison cells therefore remain unverified.

The USDM retained observations concern September 15, 2026, with year-ago comparators and one prior-week comparison. They were retrieved September 22; they are not September 23 measurements. The run's evidence cutoff is 2026-09-23T01:04:32.974984+00:00. Publication times and original release vintages remain unknown.

| Mandate area | Available evidence and consequence |
|---|---|
| Crop progress, condition, acreage, yield and production | NASS discovery only; numerical outcomes unavailable |
| Drought and soil moisture | Selected historical point-well cells; no crop weights or crop-stage matching |
| Grain supply, use and stocks | No compatible balance cells; stocks-to-use and attribution uncomputed |
| Fertilizer, food/cold storage, livestock output and feed | Required measurement tables unavailable |
| Exports | FAS remains disabled; no realized shipment series |
| Disease | APHIS discovery only; no dated counts, removals or output |

## Hypotheses and tests

Supply-loss, rising-demand and beginning-stock/residual-revision explanations remain unresolved. The balance test needs beginning stocks, production, imports, domestic use, exports, total use and ending stocks in each compatible vintage. Missing cells were not set to zero; the balance calculator was not run on synthetic or incomplete economic inputs.

**OBSERVATION:** The retained USDM values yield the following descriptive differences; positive means greater depth below land surface.

| Point location | Current depth, feet | Year-ago depth, feet | Difference, feet |
|---|---:|---:|---:|
| St Croix | 25.85 | 18.62 | +7.23 |
| St John | 18.73 | 12.68 | +6.05 |
| St Thomas | 8.41 | 8.22 | +0.19 |

St Thomas's retained prior-week depth is 9.76 feet, yielding −1.35 feet. St John's retained narrative difference is 6.10 feet, exceeding the paired subtraction by 0.05 feet. Exact Decimal and independent integer-hundredths calculations agree.

**ASSUMPTION/SENSITIVITY:** If each displayed figure is rounded to the nearest 0.01 foot, the paired difference spans 6.040–6.060 and the stated difference spans 6.095–6.105 feet: at least 0.035 feet separates them. Allowing ±0.01 foot per figure still leaves a 0.02-foot gap. These sensitivity checks reproduce the prior quality concern; they do not verify the publisher's rounding convention or identify the error's cause.

**INFERENCE:** These point measurements cannot establish crop exposure, yield loss, national food availability or a price effect. Crop-weather attribution lacks acreage/irrigation weights, development stages and matched outcomes. Disease attribution lacks deduplicated detections, removals and output controls. Fertilizer/trade attribution lacks quantities and shipment histories. All four economic attribution recipes remain blocked. No causal adjustment, national extrapolation or calibrated probability was calculated.

## Limitations

Only permitted reviewed extracts were reused. Their exact file hashes are verified, but original publisher bodies and full prior tool representations are unavailable. WASDE, NASS and FAS share USDA inputs; USDM shares weather/field-report ancestry. Repeating this report must not create a second evidence vote for those inputs.

The prior Agriculture report and numeric outcomes were inspected before this run's plan, so the calculations are exploratory replication. No current counterpart-domain conclusions were consulted before freezing this report. No prior report is superseded. An installed route and passing offline arithmetic checks do not prove current table access, fresh measurements or a completed balance investigation.

## Sources

[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report), [NASS publications](https://www.nass.usda.gov/Publications/), [U.S. Drought Monitor](https://droughtmonitor.unl.edu/CurrentMap.aspx), and [APHIS H5N1](https://www.aphis.usda.gov/h5n1-hpai). Source use is limited to the exact reviewed extracts from `agriculture-suite-manual-2026-09-22-r1`, report SHA256 `0d33d9ffa2c5251ea020ec39dc650633a90390381037ca8158de18e821ead6ee`. The evidence package preserves the eight cells, source ancestry, original retrieval times, file hashes and reproducible calculations.

## Next decisive evidence

At a later authorized activity when restrictions permit, discover actual WASDE table URLs and retain the fourteen compatible cells before executing the two-vintage balance and stocks-to-use checks. Preserve release precision, residuals and shared USDA ancestry. Resolve the St John discrepancy against the publisher before substantive reuse. The crop, livestock and input/trade hypotheses additionally require the aligned exposure, quantity, outcome and control data identified above. No retry schedule or extra collection is created by this report.
