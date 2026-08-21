# Causal Graph

This is a human-readable causal map. Arrows are hypotheses, not facts.

```text
growth ──> earnings ──> equity cash-flow expectations ──> equity prices
   │
   └──> labor demand ──> hiring flow ──> income / consumer demand ──> real activity / growth
             │              │
             │              └──> re-employment speed / continued-claims duration
             └──> separation / layoff flow ──> initial jobless claims

income / consumer demand ──> earnings / cash-flow expectations ──> equity prices
income / consumer demand ──> inflation pressure ──> expected policy path ──> discount rates ──> equity prices

strong nominal activity ──> inflation persistence / policy constraint ──> expected policy path / long yields
weak labor demand ──> expected policy path ──> short/intermediate yields
weak consumer demand ──> expected policy path ──> yields

fiscal impulse ──> growth
fiscal impulse ──> Treasury issuance ──> duration supply / term premium ──> long yields ──> financial conditions
Treasury debt-management / liquidity-support buybacks ──> long-end liquidity & net duration absorption ──> term premium / long yields ──> financial conditions

AI / corporate capex financing ──> corporate bond issuance ──> private duration supply ──> investor absorption cost / corporate spreads ──> financing conditions
private duration supply ──> cross-market duration competition ──> long yields / financial conditions
AI / capex / defense demand ──> business-equipment & high-tech output ──> aggregate industrial production
household-demand weakness ──> consumer-goods / auto output
housing financial conditions ──> residential construction activity

regional manufacturing surveys ──(noisy aggregation / composition bridge)──> national manufacturing activity
inventory behavior / supply disruption ──> manufacturing orders & output
services demand ──> composite activity / services hiring

credit stress ──> financial conditions ──> growth
liquidity ──> risk appetite / valuation

geopolitical shocks ──> commodity prices ──> inflation expectations ──> long yields / policy constraint
commodity shocks ──> retail energy prices / input costs ──(lagged, state-dependent)──> measured inflation
commodity shocks ──> real household purchasing power / consumer demand
commodity shocks ──> margins

positioning ──> short-horizon price response
```

## State-dependent interaction added 2026-08-10

Weak labor does not imply falling long yields mechanically. The Aug. 10 evidence reinforced a competing path in which commodity/inflation risk and Treasury-supply/term-premium pressure can offset or dominate the easier-policy channel. This interaction should be tested prospectively rather than treated as proved from one session.

## Timing refinement added 2026-08-12

A spot commodity shock is not a contemporaneous one-for-one CPI shock. Pass-through depends on timing, retail gasoline/refining dynamics, inventories, substitution, and indirect input-cost transmission. July CPI showed falling monthly energy prices even though spot oil moved sharply higher in August. Therefore July CPI cannot be used retroactively as a clean falsification of an August oil-shock channel; the channel must be tested prospectively in later price data and market inflation expectations.

## Opposing-channel consumer-demand refinement added 2026-08-14

A negative consumer-demand shock can affect equities through **opposing causal channels**. Weaker demand can lower expected earnings/cash flows, which is equity-negative, while also lowering the expected policy path and discount rates, which can be equity-positive. The Aug. 14 combination of unexpectedly weak retail/control-group sales, lower Treasury yields, and only a modest S&P decline illustrates why index price alone cannot identify the dominant growth mechanism. Future model discrimination should prefer joint observations across growth, yields, credit, labor, and earnings breadth rather than inferring macro strength directly from a resilient index.

Retail sales are nominal, goods-heavy, revision-prone, and sensitive to timing effects; the demand node therefore should be updated from repeated evidence rather than one release.

## Private-duration supply refinement added 2026-08-17; confidence raised 2026-08-21

The model distinguishes **Treasury duration supply** from potentially material **private corporate duration supply**. The Aug. 17 version was explicitly provisional and low-confidence because the only support was market commentary plus a long-yield move that could have had many causes.

Post-cutoff evidence on Aug. 21 materially strengthens the existence of the channel. Reuters, citing BNP Paribas data, reported **$220 billion** of 2026 AI-hyperscaler debt issuance as of Aug. 10 versus **$12.5 billion** in the comparable prior-year period; technology investment-grade spreads were about **89 bp**, 9 bp wider than the overall investment-grade market, and recent deals required larger concessions. This is direct evidence that repeated AI-related issuance is imposing an observable absorption cost in corporate credit.

The edge is therefore upgraded from **low** to **moderate confidence** as a private-financing mechanism. It is still not legitimate to assign a specific Treasury-yield move to AI issuance alone. Fiscal supply, inflation expectations, growth, Fed policy expectations, global duration supply, and Treasury debt-management remain competing explanations. The proper prospective test is whether periods of unusually heavy private duration supply are associated with higher relative concessions/spreads and long-end pressure after accounting qualitatively for those rivals.

## Composition-sensitive activity refinement added 2026-08-18

Aggregate industrial production is treated explicitly as a **mixture of potentially opposing sector channels**, not a sufficient statistic for broad demand. July 2026 total IP rose 0.2% while consumer-goods output fell 0.4%, business-equipment output rose 0.8%, and high-tech/defense categories were strong; housing simultaneously weakened sharply.

This means an AI/capex/defense boom can keep aggregate industrial output positive while household-sensitive activity deteriorates. Conversely, weak consumer categories do not establish broad contraction if investment-linked production is expanding. H001/H002/H004 discrimination should therefore use the aggregate jointly with sector composition, housing, labor, credit, and earnings breadth. This is a direct market application of the existing Universal ambiguous-endpoint safeguard rather than a new causal law.

## Treasury debt-management / liquidity-support refinement added 2026-08-19; persistence narrowed 2026-08-21

Treasury's Aug. 19 announcement that long-duration nominal-coupon liquidity-support buybacks will rise from $2 billion to at least $4 billion per operation added an explicit **policy/liquidity pathway into the long end of the curve**. Treasury's official CMT curve fell from 4.71% to 4.65% at 10 years and from 5.28% to 5.19% at 30 years between Aug. 18 and Aug. 19.

The Aug. 21 rebound to roughly **4.73% / 5.266%** on the 10-/30-year shows that the initial relief was not persistent. The model therefore reclassifies this channel as a **tactical liquidity/duration buffer**, not a durable structural override. Buybacks can alter market functioning, net duration absorption, and term premium at the margin, but their effect can be overwhelmed by growth, inflation, fiscal supply, private duration, or policy expectations.

This refinement weakens any inference that either the initial rally or subsequent selloff uniquely identifies the buyback mechanism. It remains an application of Universal UL-0004 / FM-006.

## Labor-flow asymmetry refinement added 2026-08-20

Initial jobless claims are treated specifically as a **separation/layoff-flow indicator**, not as a sufficient statistic for total labor demand. P000017 prospectively tested whether prior household/housing weakness had already transmitted into layoffs; the event failed at 206,000 claims. At the same time, continued claims rose to 1.799 million and contemporary labor commentary characterized the environment as low-hire/low-fire.

The model therefore separates at least two labor-demand pathways: weaker demand can first reduce hiring and slow re-employment while layoffs remain low, or it can progress into rising separations/initial claims. Low initial claims should reduce H002's **immediate layoff-transmission** probability but should not erase a slowdown hypothesis if hiring, continued claims, payroll breadth, vacancies, or household demand weaken. Conversely, a later synchronized rise in initial claims plus credit stress would be much stronger H002 evidence than low hiring alone.

## Growth-sign ambiguity refinement added 2026-08-21

Strong activity is no longer mapped mechanically into H001. The same growth observation has different implications depending on the inflation/rate state:

- **Strong activity + easing price pressure + falling policy expectations / sustainably lower long yields** favors H001.
- **Strong activity + persistent price pressure + firmer policy expectations / elevated long yields** favors H003.
- **Weak activity + easing rates** may favor H002 rather than H001 if the rate relief is caused by deteriorating demand.

This prevents the model from treating “growth beat” as synonymous with “soft landing.” It is another application of opposing-path / ambiguous-endpoint discipline.

## Regional-to-national manufacturing aggregation refinement added 2026-08-21

P000019 forecast the August flash national manufacturing PMI at 54.2 with 56% probability of >=54.0 after very strong Empire State and Philadelphia headline readings. The first national flash release was **53.2**, below the frozen 53.7 consensus and 53.9 July no-change benchmarks, while services accelerated sharply.

The forecast error indicates that regional headline surveys should not be linearly extrapolated into a national manufacturing index. Regional geography, sector weights, inventories, supply disruptions, survey construction, and the distinction between current-activity headlines and orders/output components can all matter. Future national-manufacturing forecasts should use a multi-signal bridge rather than treating two strong regional headlines as quasi-replicates.

This change is linked to a preserved out-of-sample forecast error and is intended to improve later national-activity forecasts; it should receive no learning credit until those later forecasts resolve.

Every material edge should eventually carry sign, expected lag, confidence, evidence, and known failure conditions.
