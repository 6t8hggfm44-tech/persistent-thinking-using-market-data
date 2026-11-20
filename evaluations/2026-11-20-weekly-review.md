# Friday November 20, 2026 — weekly market model and learning self-critique

**Source:** primary repository `d9752cdad8e138121c942d0c7351de2cdd157f98` before this cycle. Prior evidence cutoff 2026-11-19T22:53:24Z; Friday cutoff 2026-11-20T22:41:00.478Z; current v0.2.21. No due forecast or reclassified outcome. Connector-side deterministic recomputation, not full native Repo B Python execution. Companion should bind its derived validation to the final primary commit, not this prepublication snapshot.

## 1. Auditor first — preserved sample

34 resolved unique records, **30** scored binary probabilities, four historical nonbinary records P000006–P000009 excluded solely from the binary score, not erased. No forecast became due since Thursday; P000037 first November 25 BEA core-PCE and P000005 August 2027 still open. The frozen primary ledger `evaluations/prediction_scores.csv` blob `ef002f36a14df05d5311ee4269b62975995c7125` remains unchanged. Connector-side fresh extraction of all 30 raw probabilities and events recomputed Brier/log loss with **zero deterministic discrepancies** at 1e-9 Brier / 0.00000051 log tolerance. This does not execute the named native Repo B validator or certify unsupported point schemas.

## 2. Proper scores, benchmarks and descriptive learning

Cumulative mean Brier **0.220443333**, mean log loss **0.631256948**, 14 TRUE/30. Mechanical p=.50: Brier **.25**, log **.693147**; descriptive neutral skill **+11.82% Brier**, **+8.93% log**, not a meaningful domain consensus/base-rate advantage. Model probabilities cluster near .5. Appropriate benchmark-relative performance is **mixed and frequently poor**: across eight S&P 500 point forecasts model MAE **87.54125** versus same-event frozen no-change **66.44500**, skill **−31.75%** (mixed horizons, descriptive); Nov13 P000036 PPI point missed .1pp while frozen last-release no-change was exact; Oct CPI P000035 point tied its frozen prior/consensus; FOMC P000027 Brier .1764 versus frozen market-implied .1521. Do not pool the mixed-unit generic `benchmark_score` field.

Six earliest/latest resolution-order binary Brier **.227400/.229217** (log .647876/.647965); ten earliest/latest **.214740/.233260** (log .621654/.657840). Later windows look worse, but target, horizon, event difficulty and economic regime mix differ; these **are not matched vintage comparisons**. No eligible 20-of-40 matched window. Prior November 17 Converge case-mix guard remains applicable and cannot retrospectively fix an incomparable sample.

## 3. Calibration, interval width, uncertainty, anti-Goodhart

Mean assigned p **.4890**, realized event rate **.4667**; 22/30 forecasts in [.4,.6]. Reliability bins, p mean / observed rate: (.2,.4] **n7 .337/.143**; (.4,.6] **n21 .525/.571**; (.6,.8] **n2 .640/.500**; other bins n0. Sparse bins cannot show conditional reliability. Strict 80% interval flags covered **27/30=90%**, but no reward for overcoverage without sharpness. SPX one-day interval widths **271,245,400,295** points, one-week **660,555**; payroll P000034 missed despite 200,000-job width; P000036 PPI .9-percentage-point width covered. No cross-unit mean width. Prior unchanged Nov13 descriptive row-bootstrap Brier 95% **[.19156,.24956]**, creation-date-cluster **[.18626,.24964]** (25 clusters), not fresh independent data, formal confidence in improvement or full dependence adjustment.

Potential Goodhart patterns: moderate-probability compression, wide intervals, target/horizon heterogeneity, selection of relatively easy binary events and shared-date forecast dependence; no evidence of intentional gaming, but positive neutral Brier is no proof of useful discrimination. All negative cases preserved: best P000026 Brier .0529, worst P000030 .3844; P000025 binary success hid 124K payroll magnitude miss; P000034 +105K payroll magnitude miss and interval miss; P000004 three-month S&P missed by 365.06 versus no-change 207.70. No new outcomes change this audit.

## 4. Model-change efficacy

Manufacturing regional-to-national correction has one favorable subsequent ISM point test (P000024), insufficient repeated matched success. Labor net-payroll proxy changes suffered P000025 and P000034 magnitude failures. v0.2.21's later two probability outcomes P000035 (.09 Brier) and P000036 (.3136) concern **inflation**, not its motivating labor-reweighting target. Neither establishes causal-learning benefit or failure of the specific payroll revision. The precommitted prospective payroll comparison will compare frozen v0.2.20 and v0.2.21 hypothesis weight mixtures on the **same** four conditional probabilities, event >=100K nonfarm jobs, first BLS publication; 12 predeclared months November 2026–October 2027, **0 registered/0 resolved/0 missed/12 upcoming**. Earliest legal issuance is existing post-close occurrence November 24–27, before the December 4 08:30 EST release. This run is outside that window; **no early forecast**.

## 5. Friday new economic evidence, Skeptic and model disposition

Michigan final November headline sentiment 51.5 vs October 48, below the survey's 4.8-point significance threshold for one-month changes; inflation expectations declined, per November 20 official/attributed sources. Friday SPX fell 3.7% to AP 6910.39, weekly −8.6%, >10% off its high; price revaluation does not directly measure GDP or labor. A valuation shock, policy constraint, and genuine slowdown remain rival causal channels. See `evidence/2026-11-20-cycle.md` and `meta/SKEPTIC_2026-11-20.md`. After Skeptic, **NO causal-edge, weight, or version change:** H001 soft landing **.39**, H002 recession **.10**, H003 fiscal/inflation **.39**, H004 productivity **.12**, v0.2.21. No post-outcome credit, no day-specific regime fit.

## 6. Highest-information test and learning verdict

Next registered outcome P000037: first November 25 BEA October **core PCE monthly >=+.4%**, frozen **p=.40**, point **+.3%**, nominal 80% **[+.1%,+.5%]**, source cutoff November 13, frozen September no-change and dated external point benchmarks; retain original rule. One event distinguishes inflation persistence partially but cannot uniquely identify H001/H003. More direct **learning** discriminator is the prospective paired payroll-vintage cohort, which isolates the hypothesis-weight revision under matched target/cutoff/conditionals and frozen base-rate 30/36.

**Learning verdict: PRELIMINARY/UNPROVEN at n30.** There is no sufficiently matched evidence of improved proper scores across vintages versus informative fixed baselines without worse calibration/sharpness. The large Friday equity drawdown is new information, not a scored demonstration of success/failure of preexisting P000005 or P000037. Avoid claims of learning due to persistence, more reports, candidate reweighting, or isolated successful binary forecasts.

## 7. Companion, intake and governance limits

- Primary 86 research + 8 GEV canonical intake Git paths match 86+8 index links; 279 older pending files are transport, not newly received reports. **Native** `tools/check_intake_index.py` against a complete repository snapshot was NOT executed because the current GitHub connector provides objects without a full runnable checkout. No verified new complete upstream intake.
- Native Repo B `src/validate_forecasts.py`, `src/vintage_pairs.py` and point/interval adapters were NOT executed, so source-bound connector arithmetic is **partial**, not a completed companion certification. P000034/P000036 unsupported structured formats remain a known risk.
- No new universal lesson promoted: case-mix, role/source distinction and ambiguous market-price identification already exist in Market/Universal. No direct Universal truth write; no trades.
