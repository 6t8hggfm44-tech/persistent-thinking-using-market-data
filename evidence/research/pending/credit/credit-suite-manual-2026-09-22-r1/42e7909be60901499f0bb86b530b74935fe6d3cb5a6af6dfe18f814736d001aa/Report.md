# Credit and financial stress — manual investigation, September 22, 2026

## Summary

**INFERENCE — Mixed asset-quality evidence; broad latest-quarter deterioration is not supported by the measured rates.** Total delinquency fell, while the longer comparison reveals pockets of deterioration. This is a limited quarterly descriptive result, not a current funding-stress assessment or a causal finding about borrower repayment capacity.

This independent manual investigation consumes no scheduled occurrence and supersedes no frozen report. Evidence cutoff: September 22, 2026, 18:31:32 UTC. Source periods: 2024 Q2, 2025 Q2, 2026 Q1 and Q2; all values use the currently retrieved vintage. No counterpart domain findings or market-price outcomes informed this investigation.

## Coverage

**OBSERVATION —** The Federal Reserve's all-bank, seasonally adjusted table supplies 24 selected cells. Its methodology defines delinquency as delinquent loan dollars divided by outstanding loan dollars in the corresponding category, using quarterly Call Reports.

| Category | 2026 Q2 rate (%) | Quarter change (bp) | Year change (bp) | Two-year change (bp) |
|---|---:|---:|---:|---:|
| Real estate, all | 1.68 | -2 | +1 | +12 |
| Consumer, all | 2.62 | -2 | -13 | -10 |
| Leases | 1.19 | +3 | +9 | +1 |
| Commercial and industrial | 1.27 | -6 | -2 | +12 |
| Agriculture | 1.10 | -2 | -6 | +16 |
| Total loans and leases | 1.42 | -3 | -7 | -6 |

Rates and calculations above derive from the [Fed delinquency table](https://www.federalreserve.gov/releases/chargeoff/delallsa.htm). Loan-dollar denominators, charge-offs, bankruptcies, repo volumes, corporate spreads, regional-bank exposures, SLOOS supply/demand and funding-rate comparisons remain unmeasured in this run. Historical raw captures were unavailable; their metadata was not treated as data.

## Hypotheses and tests

Three leads were considered: credit supply versus demand, funding repricing, and asset-quality breadth. The last was selected because compatible quarterly cells passed the measurement gate. The plan is explicitly exploratory: values were seen before selection and plan freeze.

1. **Latest-quarter broad deterioration — contradicted within this table.** The predeclared descriptive criterion required a rising total and increases in a majority of five broad classes. Only one class rose; four fell. Nested residential/card components were excluded from the breadth count, and the total was assessed separately.
2. **Short-window improvement masks longer divergence — supported with limits.** Two classes rose over one year, four over two years. The total still fell at both horizons. The result rejects a uniform improvement story without establishing economy-wide distress. These overlapping comparisons are sensitivity checks, not independent replications or calibrated probabilities.
3. **Denominator/mix rather than fewer delinquent dollars — untested.** A declining ratio can reflect its denominator or portfolio composition. Matched delinquent-dollar amounts and fixed-population loan balances are needed to discriminate this mechanism.

Actual calculations use current minus comparator, multiplied by 100 to obtain basis points. All 18 differences were recomputed using a separate integer-hundredths method and matched. The package preserves exact inputs, extraction locators, script and input hashes. No missing values were filled and no seasonal adjustment was newly estimated.

## Limitations

The source is a derived web representation; its original publisher bytes were not verified. Publication instant and first-release revision history remain unknown. The methodology page is longstanding documentation, not a new 2026 observation. Same-vintage comparisons reduce one source of inconsistency but cannot reconstruct historical knowledge. The five classes are correlated and not an exhaustive fixed bank panel. No causal control for lending composition, forbearance, policy or borrower income was executed. The quarterly result cannot establish a change during the requested week.

**ASSUMPTION —** Published category definitions are sufficiently compatible across the four displayed quarters for this bounded descriptive comparison. **SPECULATION —** Translation into borrower spending, bank credit supply or market prices is withheld pending matched evidence.

## Sources

- Federal Reserve, [all-bank seasonally adjusted delinquency rates](https://www.federalreserve.gov/releases/chargeoff/delallsa.htm), retrieved September 22, 2026; table rows 2026 Q2/Q1 and 2025/2024 Q2. Upstream ancestry: FFIEC Call Reports.
- Federal Reserve, [method of calculation](https://www.federalreserve.gov/releases/chargeoff/about.htm), retrieved September 22, 2026. Same source family; not independent corroboration. Exact extraction hashes and source locators are retained privately.

## Next decisive evidence

Match quarter-end delinquent dollars and outstanding balances by category and a fixed bank population; then add charge-offs and the relevant credit-demand/standards vintage. Separate any financing or labor transmission test from these independently frozen descriptive findings. No new monitoring or acquisition schedule is created.


## Version 2 — transport metadata correction

This version preserves every original numerical finding, calculation, source
period and evidence cutoff above. It supersedes version 1 only to make the
public handoff's transport limitations explicit. The original packet omitted
that metadata field; its report and envelope already described the evidence
limits. No new evidence was collected and no scientific test was rerun.

The corrected packet carries exact UTF-8 report/envelope bytes. Its underlying
evidence consists of permitted reviewed extracts; original publisher-body byte
identity and hidden provider traffic were not verified. The private evidence
package is referenced, not published. Staging establishes no Market receipt or
canonical acceptance. This is a correction to the same manual investigation,
not another independent contribution or a scheduled occurrence.
