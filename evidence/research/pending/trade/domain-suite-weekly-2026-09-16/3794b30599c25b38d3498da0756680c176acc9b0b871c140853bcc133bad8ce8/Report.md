# Global trade and China

## Summary

**OBSERVATION:** The WTO's 9 September 2026 Goods Trade Barometer placed the July global index at 102.0, up 0.3 point from April's 101.7 and above the 100 trend baseline. Five of six components were above trend; electronics was strongest at 104.9, while container shipping was the exception at 99.6.

**INFERENCE:** Merchandise-trade momentum appears positive but uneven. The signal is broader than electronics alone, yet the 2.9-point electronics premium and 3.2-point air/container divergence warn against reading the composite as a uniform final-demand or ocean-shipping boom.

**ASSUMPTION:** Component distances from their shared 100 baseline are descriptively comparable. They are not treated as equally weighted contributions.

**SPECULATION:** If export orders stay strong while container throughput remains below trend, later releases could show electronics- and air-freight-led resilience alongside weaker container channels. This is a testable next-release hypothesis, not a market forecast.

## Coverage

The evidence window is April through July 2026, using the official WTO barometer published 9 September. Coverage is global, not China-only. No fresh China NBS or customs table was acquired.

The configured China NBS, Korea Customs, Taiwan MOF and Port of Los Angeles captures remained under preserved weekly cooldowns and their bodies were absent from this runtime. The due Eurostat source was reserved and attempted once; DNS resolution failed and its cooldown advanced. Those sources contribute no economic observations here.

## Hypotheses and tests

1. **Broad strengthening — qualified support.** Five of six components exceeded 100; the six-component mean was 102.483 and the non-electronics mean 102.0. The overall barometer rose 0.3 point.
2. **Electronics concentration — support, but not electronics-only.** Electronics exceeded the non-electronics mean by 2.9 points; four of five non-electronics components were still above trend.
3. **Transport divergence — support.** Air freight was 102.8 versus container shipping at 99.6, a 3.2-point gap. Cargo mix, modal substitution, route effects and uneven demand remain competing explanations.
4. **Scenario sensitivity.** WTO repeated a 1.9% 2026 baseline and 1.4% high-energy scenario, while sustained AI investment could add 0.5 percentage point. These scenarios are not realized data or mechanically additive.

The calculation used `extracted-data.csv` and `calculate.py`. A period-key bug in the first development run was caught, corrected and rerun before freezing; the final April-to-July difference is +0.3 point.

## Limitations

- The WTO barometer is a composite leading indicator, not a causal estimate, probability, China-only series or direct final-demand measure.
- Component inputs differ in sources and cargo/product coverage and are not six independent replications.
- Economy-level quantities, unit values, working-day adjustments, bilateral destinations and alternate-port comparators were unavailable.
- Imported hashes establish capture identity, not cloud access to prior bodies or reviewed content.
- Eurostat failed at DNS resolution after one authorized attempt; no retry or cooldown evasion occurred.

## Sources

- World Trade Organization, *Goods Trade Barometer*, 9 September 2026: https://www.wto.org/english/news_e/news_docs/Goods_Trade_Barometer_September_2026.pdf
- China NBS, Korea Customs, Taiwan MOF and Port of Los Angeles: metadata/cooldown audit only; no claims from unavailable bodies.
- Eurostat industry overview: access-attempt record only; no economic claim.

## Next decisive evidence

The next decisive test is a matched set of current China physical output/customs quantities, Korea working-day-adjusted exports, Taiwan electronics quantum or unit-value detail, and comparable loaded-container data across more than one port. It should distinguish broad quantities from electronics mix, route substitution and timing. Existing source cooldowns must expire or a separately permitted official alternative must be reserved first.
