# Friday market-model weekly review - 2026-10-23

Source head before this cycle: e8c94d6f7e7c8ea426d874507a8ffdf6206d0acc; as-of evidence cutoff: 2026-10-23T21:48:51.739Z; model v0.2.20 unchanged. Probability scoring calculated from the primary frozen ledger by a read-only port of Market Repo B's published parsing/scoring logic. A native GitHub checkout was unavailable, so neither original Python validator was literally executed. Repo B companion report must bind to the later actual primary publication commit; numeric statements below are DESCRIPTIVE, not independent-validator-certified learning claims.

## Auditor first: frozen resolution and scores
Open *unique* forecast IDs are P000004 (SPX November 9, 2026 close) and P000005 (SPX August 9, 2027 close). The legacy predictions/open directory also carries historical already-resolved copies; do not mistake those for live tests. No forecast horizon newly expired today; none re-resolved or changed.
Canonical resolved ledger: 29 records, 25 binary probability events, four non-probability records (P000006, P000007, P000008, P000009). All 25 stored Brier and log scores recomputed with zero discrepancies. Mean Brier 0.214144; mean log loss 0.618617; event rate 11/25=0.4400; mean assigned p 0.4968.
Best binary Brier P000026 = 0.0529, false weekly claims threshold; worst P000030 = 0.3844, false August core PCE >=0.3 despite p=.62. Positive score for P000029 (0.1156) is already in the canonical ledger and is not a new resolution.

## Prospective learning hypothesis: still not established
- Earliest six: Brier 0.227400, log 0.647876, 4/6 events; latest six: 0.215633, 0.623502, 5/6 events. A favorable event-mix shift can improve an aggregate without learning.
- Earliest ten: Brier 0.214740, log 0.621654; latest ten: 0.191710, 0.570929. Event rate 5/10 in both, but targets/horizons change and overlap between sliding windows does not ensure independent tests.
- Lifetime Brier vs arbitrary fixed p=.50: comparator Brier 0.25, descriptive score skill +14.34%. Not a useful economic historical base-rate or consensus proof.
- 20,000-draw iid bootstrap mean-Brier CI approximately [0.1840,0.2450]. Resampling whole creation-date clusters (21 groups) produces approximately [0.1807,0.2443], still neglecting dependence across dates/targets. Bootstrap confidence is descriptive and not proof of learning.
- SPX point forecast family (seven matched records): MAE 47.90 index points vs frozen no-change 46.27, skill -3.52%. The model still loses to the principal repeatable point baseline.
- P000027 Fed hike p=.58 Brier .1764 lost to frozen market-implied p=.61 Brier .1521. P000012 headline CPI success merely matched a frozen consensus at the threshold; P000028 PPI point tied frozen consensus. Do not pool the CSV benchmark_score field, which mixes MAE and Brier.
- Descriptive calibration: mean p .4968 vs observed .44; 0.4-0.6 bin n=18 mean p .5267 vs realized event frequency .5556; 0.2-0.4 bin n=5 mean p .332 vs event rate zero; 0.6-0.8 bin n=2 mean p .64 vs event rate .50. Forecasts that happened averaged p=.5482 versus .4564 for non-events. Each bin is sparse.
- Strict record-level 80% interval coverage 23/25=92%, versus 80% nominal. That may reflect overly broad intervals, not improved calibration; SPX widths vary sharply with horizon: 1d [245,271,295,400] points; 1w [555,660]; 1m [1165]. Payroll component width increased from 175K (P000025) to 220K (P000031), so coverage gain cannot be credited as sharpness improvement. WTI P000007 and payroll P000025 genuine misses remain preserved.
- Anti-Goodhart: correlations and target substitution exist; later six have event rate 5/6 vs earlier 4/6, increasing probability compression near .5 and heterogenous base rates prevent attribution; no ex-post regime relabeling, no forecast exclusion or retroactive benchmark change permitted.

## Error-linked model-change evaluation
- v0.2.8 national-manufacturing bridge: P000019 pre-change failure triggered a restraint; P000024 post-change ISM accuracy (Brier .1764; point 0.2) is one favorable prospective test. Not repeatable proof.
- v0.2.7 low-hire/low-fire separation logic: P000020 joint failure is negative; P000026 low-claims success was issued before v0.2.14 and cannot be credited to v0.2.14.
- v0.2.14 net-payroll bridge, motivated by P000025 124K point and 80% interval miss: later P000031 accurately anticipated weak September payroll event (Brier .1849), and its +90K point missed by 61K but beat frozen +95K consensus error 66K. Mixed weak positive, n=1 relevant direct payroll test; wider interval warns against vagueness.
- v0.2.15 through v0.2.20 reweightings do not yet have clean same-target, same-horizon replicate tests. P000029 (created September 18) cannot be credited to v0.2.20 (October 5); the gasoline-led CPI success does not identify persistent core inflation. P000030 remains negative core-PCE evidence.
- H004 AI productivity boom still lacks realized productivity-led discriminating outcomes; capex and shares are not enough.

## New evidence and Skeptic
See evidence/2026-10-23-cycle.md and meta/SKEPTIC_2026-10-23.md. October 23 flash composite 57.6 suggests expansion and price diffusion 59.8 warns about inflation. Brent $116.72 and low jobless claims 194K conflict with soft household sentiment 48 and September pending sales -7.3%. Inflation can be supply-driven while real demand slows; do not infer a unique macro regime from any one endpoint. Both H001 and H003 remain .37, H002 .14, H004 .12; causal graph unchanged.

## Next highest-information discrimination
P000033, registered prospectively only upon its actual canonical publication: 56% event probability for first-release September core PCE >=0.3% m/m on BEA October 29 08:30 ET, point 0.3%, 80% interval [0.1%,0.5%]. Frozen August core PCE first release 0.2% is the no-change point; neutral .5 is a deliberately weak binary comparator, not a consensus probability. This tests broad consumer-price persistence, not simply oil's mechanical headline CPI contribution. Old prepared October 16 P000032 is NOT an active forecast and must not be retroactively registered. No trades.

## Integrity and longitudinal status
The 94 canonical intake records matched 94 cumulative index rows in a complete connector-side parity-equivalent check (86 research + 8 legacy GEV), but the native Python checker could not be run on an unmounted checkout. No new staged upstream packet arrived after October 12. Exact original October 19-22 phase files remain unrecoverable; this cycle does not recreate them or claim prior canonical publication. All metrics are versioned in the learning ledger for prospective later comparison. Precommitted n<30 minimum means INSUFFICIENT EVIDENCE TO ASSESS LEARNING; likelihood of regime/luck/target-mix explanations remains material.
