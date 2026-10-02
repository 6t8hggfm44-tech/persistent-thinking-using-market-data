# Friday weekly review — 2026-10-02

Evidence cutoff: 2026-10-02T21:52:44Z.

## Resolution and score

P000031 resolved TRUE on first-release September payroll growth of +29,000 jobs. The frozen 0.57 probability scored Brier 0.1849 and log loss 0.562119. The +90K point missed by 61K, versus 66K for the frozen +95K external point and 133K for the frozen +162K prior-month no-change point. The -20K to +200K interval covered.

The probability ledger now has n=24. Mean Brier is 0.218250 and mean log loss is 0.627080. Direct arithmetic found zero stored-score mismatches.

## Learning audit

The experiment still has insufficient evidence to assess learning under the precommitted n<30 rule.

Vintage comparisons are non-monotonic. Earliest six versus latest six: Brier 0.227400 versus 0.244967 and log loss 0.647876 versus 0.683671, so the newest six are worse. Earliest ten versus latest ten: Brier 0.214740 versus 0.208240 and log loss 0.621654 versus 0.604880, so the newest ten are modestly better. The windows mix targets and horizons and are dependent.

Lifetime Brier skill versus a fixed 0.50 probability comparator is 12.7%. That comparator is not an empirical base rate or consensus. A 20,000-draw iid bootstrap gives mean-Brier 95% interval 0.188049 to 0.248892 and neutral-comparator Brier-skill interval 0.0044 to 0.2478. Creation-date cluster sensitivity gives Brier 0.184679 to 0.248525 across 20 creation-date clusters. These are descriptive only and do not resolve common-target or serial dependence.

Sparse calibration remains inadequate for a learning claim. Mean assigned probability is 0.490 versus an observed event rate of 0.4167. In the 0.4-0.6 bin, n=18, mean probability is 0.5267 and event rate 0.5556. Event forecasts average p=0.537 and non-events p=0.456, showing some descriptive discrimination, but sample counts are small.

Strict row-level interval coverage is 22/24 = 91.7%, above nominal. This is not automatically good: the P000031 payroll interval is 220K jobs wide, versus 175K for P000025's payroll component. The later payroll interval is therefore wider, so its coverage cannot be counted as learning through greater sharpness.

The seven resolved S&P point forecasts remain unchanged: model MAE 47.90 versus no-change MAE 46.27, skill -3.5%. The model still has no demonstrated point-forecast edge in that repeated family.

## Error and model-change attribution

P000020 remains negative evidence for the narrow sticky-reemployment formulation. P000025 exposed a serious payroll-magnitude failure despite a favorable coarse event score, which led to the v0.2.14 labor-flow bridge.

P000026 and now P000031 are favorable prospective tests of the distinction between separation pressure and net payroll growth. P000031 also modestly beats its frozen external payroll point, but it still misses by 61K and uses a wider interval. This is limited, mixed positive evidence, not proof that the bridge learned.

P000024 remains one favorable test of the regional-to-national manufacturing safeguard. P000027 beat neutral on the policy event but lost to stronger frozen market-implied comparators. P000030 is a recent negative result: its core-PCE probability lost to neutral and its point did not beat the frozen consensus. The October 1 model revision receives no predictive credit from P000031 because P000031 was created earlier.

## Evidence and model review

The September jobs report materially cools the labor picture: +29K payrolls, 4.2% unemployment, +0.1% monthly and +3.0% annual wage growth, and a combined -60K revision to July-August payrolls. Very low initial claims still argue against a broad layoff wave, so the evidence supports a low-layoff, weak-hiring state rather than an established recession.

The leading inflation-regime explanation was challenged before updating. The jobs report weakens its labor-pressure channel, but high manufacturing input-price readings and unresolved energy/supply risks keep inflation risk live. The current state therefore shifts toward softer growth without adding a new causal edge.

The Oct. 1 Energy packet was canonically received only in this cycle after exact byte/hash verification. Its new electricity evidence is lagged and its gas/petroleum evidence is older or reused, so source ancestry prevents duplicate current macro weight.

## Forecast design

No new forecast is added merely to increase sample size. P000029 remains the highest-information registered discriminator: 66% probability that first-release September headline CPI is at least +0.4% m/m on October 14, with a +0.5% point and +0.1% to +0.9% 80% interval.

No new Universal transfer candidate is warranted. This cycle reinforces existing rules on benchmark-relative attribution, proxy scope, source ancestry, interval sharpness and longitudinal out-of-sample learning.
