# Friday November 13, 2026 — expanded market model / learning review

**Primary Auditor snapshot:** `5b7336c4b3f0bfc165d213ea9222b45904870131`; **prior cutoff:** 2026-11-12T22:10:08Z; **new evidence cutoff:** 2026-11-13T22:18:40.858Z; **Repo B validation-code head at start:** `19ae50f35454e6c051f409235c1433442ade5188`; **original forecast preserved**. This is a connector-side deterministic calculation/review, **not an executed native Python full-checkout run**. Market Repo B's required follow-on derived report must cite the resulting primary commit.

## Auditor result before evidence/model updates
P000036, created November 10, first October 2026 PPI final demand less foods, energy and trade services >=+0.5% at p=.44: first BLS publication **+0.5% TRUE** November 13 08:30 ET. Brier **0.313600**, log loss **0.820981**, point .4 versus .5 **.1pp miss**, 80% [0,.9] **covered** (width .9pp). Frozen September no-change .5 **exact**, frozen two-month .4 ties model; neutral p=.5 Brier .25 wins. BLS: https://www.bls.gov/news.release/archives/ppi_11132026.htm. Immutable originals retained. Exact auditor source `evaluations/2026-11-13-auditor.md`, commit `5b7336c4b3f0bfc165d213ea9222b45904870131`.

**Cumulative:** 34 resolved records, 30 binary scores (14 TRUE); mean Brier **0.220443333**, mean log loss **0.631256948**; zero connector-side CSV score recomputation discrepancies across all 30. Compared with Nov12 n29 .217231 Brier/.624715 log, both worsened. 30–49 permits **fragile preliminary** assessment only; no demonstrated learning.

## Prospective-vintage/benchmark comparison
| Descriptive Brier, lower better | Early | Late |
|---|---:|---:|
| 6 resolution-order outcomes | 0.227400 | 0.229217 |
| 10 resolution-order outcomes | 0.214740 | 0.233260 |

Log loss: first/last six **0.647876/0.647965**; first/last ten **0.621654/0.657840**. The 6-window deteriorated slightly, the 10-window more; **targets, horizons, regimes, and prediction difficulty differ**. Not a matched later-vs-earlier causal test. The precommitted 20-of-40 comparable rolling test remains ineligible.

A mechanical p=.50 benchmark has Brier **0.250000**, log loss **0.693147**, giving descriptive neutral skill **0.1182** (Brier) and **0.0893** (log). This is **not an informative external economic base rate**, nor evidence of method learning. Across eight SPX point outcomes, model MAE **87.54125** index points versus frozen no-change **66.44500**, negative skill **-0.3175**; mixed forecast horizons mean this is descriptive only. P000036 binary and point both lose to a frozen appropriate baseline, and P000035's correct CPI point tied its frozen benchmark. P000027 FOMC p=.58 event TRUE (Brier .1764) lost to frozen market-implied .61 (Brier .1521). Avoid pooling generic benchmark_score across incompatible metrics.

## Calibration, coverage/sharpness and uncertainty
Mean p **0.4890**, realized event rate **0.4667**; 22/30 p in [.40,.60], so probability compression is material. Reliability bins (p>lower, p<=upper): (0,0.2] n=0 assigned=NA observed=NA; (0.2,0.4] n=7 assigned=0.337 observed=0.143; (0.4,0.6] n=21 assigned=0.525 observed=0.571; (0.6,0.8] n=2 assigned=0.640 observed=0.500; (0.8,1] n=0 assigned=NA observed=NA. Small bins make calibration uncertain; the mean equality is not sufficient to establish reliability/discrimination.

Ledger strict interval flag **27/30 = 90.0%** against nominal 80%; three misses remain recorded. **Widths are not pooled across units**: first four SPX 1-day widths [271,245,400,295] index points, one-week widths [660,555]; payroll P000034 interval **200,000 jobs** still missed; today's PPI interval width **.9pp** covered, despite a .1pp point error. Coverage cannot be credited as learning when targets/horizons and widths vary.

Deterministic 10,000-draw **row resampling** descriptive Brier 95% percentile range **[0.19156, 0.24956]**, and **creation-date cluster (n=25)** range **[0.18626, 0.24964]**. Not native Repo B/NumPy, not a hypothesis test, and neither handles all dependency, target-mix or regime variation. Results must not be read as statistically established learning.

## Error diagnosis / model-change accountability
- **Best binary:** P000026 Brier .0529 (low weekly claims). **Worst binary:** P000030 Brier .3844 (core-inflation target). Both kept.
- P000025 easy FALSE joint labor event Brier .1024 concealed **124K payroll magnitude error / interval miss**; original low-hire proxy inference previously corrected, but the source result remains.
- Post regional-to-national manufacturing correction P000024 did improve one subsequent ISM point outcome; not independently repeated enough for model-learning credit.
- P000034 (October payroll +165K): frozen model +60K, 105K miss and 80% interval fail; v0.2.14 net-payroll proxy repair and subsequent revisions remain under test, with no durable success established.
- P000004 August-origin three-month S&P forecast (resolved November 9) missed by 365.06 points versus no-change 207.70. Price/valuation mapping remains a liability.
- Version **0.2.21**, updated Nov6 after payroll, has only two later probability outcomes so far: P000035 Brier .09 and P000036 .3136. They concern **inflation**, not matched re-tests of the labor revision; cannot credit payroll change from them. New forecast P000037 does not resolve during this review.

**Anti-hindsight/Goodhart:** No forecast erased or redefined, no excluded failures, no post-hoc regime labels offered as validation. Forecast p values cluster near .5 and many intervals are broad; targets change across versions. Repo B is role-separated but shares the canonical source and is not an independent economy sample. P000034 and P000036 point schemas expose static native adapter coverage gaps; connector-side probability checks do not certify every field. Native Repo B Python validator and primary full-checkout intake checker not executed; name these as unfinished stages, not successes.

## Today's new evidence, Skeptic, and model disposition
BLS first October core-core PPI +.5% m/m, headline +.3%, annual core-core +4.9%; transportation/warehousing +2.0%, goods ex food/energy +.5, energy goods -.1. https://www.bls.gov/news.release/archives/ppi_11132026.htm. **OBSERVATION**, not yet evidence of November consumer-price pass-through. S&P 500 November 13 closed **7,561.67** (-.4%) according to AP, a pricing observation, not proof of an economic regime (https://apnews.com/article/12c1e8155fb85c3c7b09e058ed6d3c74). After Skeptic, both H001 (soft landing) and H003 (fiscal/inflation) remain plausible; one upstream cost surprise does not identify consumer inflation or recession. **No model or causal-graph change**: v0.2.21, H001 .39/H002 .10/H003 .39/H004 .12. A dated no-change record preserves the rationale.

**Highest-information next registered test: P000037**, first November 25 BEA October **core PCE m/m >=+0.4%**, frozen probability **.40**, point **+.3%**, nominal 80% **[+.1%,+.5%]**, first September no-change +.3% and Nov10 Conference Board +.3% external point benchmarks. https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026; https://www.conference-board.org/research/global-economy-briefs/cpi-insights-october-2026. This tests whether October consumer price persistence materializes in BEA's differently weighted index after today's producer-cost data; not a clean causal split on its own.

## Evidence/receipt and scope
Existing 86 research + 8 GEV canonical intake paths exactly matched their unique index paths under the pinned tree; zero orphan/missing; 279 historical pending packet files (93 triplets), latest Oct12, **no new complete Nov13 research receipt**. This is Git-path parity only, not native `python3 tools/check_intake_index.py`, packet-byte validation or scientific truth. No new upstream experiment invented, no trades, and no direct Universal writes.

**Learning verdict: PRELIMINARY / UNPROVEN, n=30.** A repeatable, prospective, target/horizon-matched shadow-baseline comparison after a material model revision remains the most discriminating test of longitudinal improvement. No rollout, new schedule, or retroactive paired forecasts authorized here.
