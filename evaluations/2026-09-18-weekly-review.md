# Weekly Learning Review — 2026-09-18

**Evidence cutoff:** 2026-09-18T22:01:14Z  
**Current model:** v0.2.14  
**Newly resolved probability forecasts since Sep. 11 review:** 1 (P000027, resolved Sep. 16)  
**Lifetime resolved probability forecasts:** 22  
**Learning status:** **INSUFFICIENT EVIDENCE TO ASSESS LEARNING**

## 1. Scoring and benchmark audit

No forecast resolved today, so Friday metrics carry forward the independently validated Sep. 16 ledger unchanged. Since last Friday, P000027 resolved TRUE when the FOMC raised both target-range bounds 25 bp. Its frozen p=0.58 scored Brier **0.176400** and log loss **0.544727**. It beat neutral p=0.50 but lost to both frozen contemporaneous market probabilities: p=0.61 (Brier 0.152100 / log loss 0.494296) and p=0.584 (0.173056 / 0.537854). This is favorable directional evidence for the policy-reaction mapping, not evidence of information beyond the market.

Across 22 probability forecasts:

- mean Brier **0.212214**; neutral-0.50 skill **+0.151145**;
- mean log loss **0.614555**; neutral-0.50 skill **+0.113384**;
- Repo B descriptive iid-bootstrap 95% ranges: mean Brier **0.182573–0.241437**, Brier skill vs neutral **+0.034253–+0.269710**, mean log loss **0.552484–0.675119**.

These intervals are descriptive only: forecasts share macro states, causal ancestry and overlapping target families. Neutral 0.50 is not the strongest target-specific benchmark.

The seven resolved S&P point forecasts remain a negative benchmark result: model MAE **47.896** index points versus **46.266** for matched no-change, point skill **-0.0352**. The weak Aug. 8 one-month batch remains preserved rather than averaged away.

## 2. Vintage comparison

Equal-count proper-score windows are numerically better recently:

- first 10: Brier **0.214740**, log loss **0.621654**;
- last 10: Brier **0.196760**, log loss **0.580935**;
- earliest six: Brier **0.227400**, log loss **0.647876**;
- latest six: Brier **0.175967**, log loss **0.536558**.

This does **not** establish learning. Target/horizon composition differs materially; effective sample size is smaller than 22 because observations share macro shocks; six-outcome windows have reversed direction in earlier reviews; and the precommitted minimum is 30 resolved probability forecasts before even a preliminary assessment.

## 3. Calibration, coverage and sharpness

The probability ledger remains broadly centered near even odds and the most recent validated diagnostics show some event/non-event discrimination, but the sample is too small and heterogeneous for a recalibration rule. P000027 was a correctly above-even event but was less sharp than two frozen market comparators.

Strict 80% interval coverage remains **20/22 = 90.9%**. This is above nominal and therefore a **conservatism warning**, not a success claim. Aggregate interval width is not meaningful because targets use incompatible units. No historical interval is widened after resolution.

## 4. Error diagnosis and model-change attribution

- **v0.2.8 regional-to-national manufacturing safeguard:** P000024 remains one direct favorable post-change test. One success is insufficient for learning credit.
- **v0.2.7 sticky-reemployment formulation:** P000020 remains direct negative prospective evidence; the formulation was narrowed rather than forgotten.
- **v0.2.13 inflation/policy discriminator:** P000023 was a modest favorable inflation-state test exactly at its 0.3% event threshold; P000027 was a favorable policy-direction test but lost to frozen market benchmarks. This is mixed-positive mechanism evidence, not repeated benchmark-relative superiority.
- **v0.2.14 net-payroll measurement bridge:** still has **no direct later monthly payroll forecast resolution** generated under the revised bridge. It receives zero predictive-learning credit.
- **Treasury realized-flow distinction and AI/productivity distinction:** no clean prospective outcome currently identifies either mechanism; no learning credit.

No model revision has yet demonstrated repeated improvement on the forecasts it was designed to improve.

## 5. New evidence and world-model review

The Suite Energy v1 report became canonical only at Market receipt this cycle. Its Sep. 4 petroleum baseline found stocks below year-ago levels but no unusually sharp broad four-week draw; refinery throughput was high while product-supplied proxies were lower. The 12 petroleum series are one EIA evidence family and are not independent votes.

Fresh Sep. 18 evidence shows more direct transmission from the current Middle East shock: U.S. diesel is at a record national average, farm/freight costs are materially higher, Hormuz commodity-vessel traffic remains far below its recent average, and Saudi Red Sea export disruption is affecting October planning. Countervailing evidence is also real: oil fell Friday, Saudi Arabia is expanding alternative Gulf/Oman shipment routes, China is attempting diplomatic mitigation, and partial East-West pipeline restoration is being pursued.

**Skeptic:** H003 can explain persistent inflation pressure, but a supply shock plus record diesel does not uniquely identify a durable inflation regime. Costs may be absorbed in margins/contracts; the pre-shock EIA baseline was not acutely drawing; restoration/rerouting could truncate the shock; and the same fuel/rate pressure can weaken real demand. The 10-year near 5% is a multiply determined downstream endpoint.

Weights therefore remain **H001 0.35 / H002 0.15 / H003 0.38 / H004 0.12**. No structural edge is added because v0.2.14 already represents both lagged energy/input-cost inflation pass-through and the opposing purchasing-power/margin channel.

## 6. Is the system learning?

**No claim is permitted at n=22.** The experiment is showing useful scientific behavior—immutable failures, benchmark comparisons, error-linked revisions, source-ancestry controls—but that is not the same as improved predictive accuracy.

Evidence that looks encouraging is descriptive: positive lifetime skill versus neutral, better last-10/latest-six proper scores, P000024's direct post-change success, and two favorable inflation/policy-direction outcomes. Evidence against a learning claim remains substantial: recent windows are small and composition-changing; S&P point skill is slightly negative; the one-month batch was weak; interval coverage is probably conservative; P000027 lost to market benchmarks; and the key v0.2.14 labor correction still lacks a direct post-change monthly payroll test.

The correct conclusion is **insufficient evidence to assess learning**, not “learning” and not “no learning.”

## 7. Highest-information forecast

Created **P000029**: p=**0.66** that first-release September headline CPI is **>= +0.4% m/m**, point **+0.5%**, 80% interval **+0.1% to +0.9%**, resolving on the BLS Oct. 14 release. The August +0.4% point is frozen as the no-change benchmark and neutral 0.50 as the probability comparator. This is preferable to another oil-price/rates call because it prospectively tests whether the observed energy/input-cost shock reaches official consumer inflation.

P000004 and P000005 remain frozen and unresolved.

## 8. Transferability review

No new Universal transfer candidate is added. The relevant safeguards—observation/inference separation, adversarial review, shared-ancestry control, baseline-relative attribution, immutable failure preservation and longitudinal out-of-sample learning standards—are already represented in active Universal material.

## 9. Most important watch

**Whether the September energy shock actually appears in official consumer inflation, with East-West/Yanbu restoration and Hormuz normalization as the upstream persistence controls.** P000029 is now the cleanest registered test of that pass-through channel.
