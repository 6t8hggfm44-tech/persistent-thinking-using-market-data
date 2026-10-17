# Market publication recovery — verified readback

- Recovery work began 2026-10-17T17:47:36Z. Canonical publication update returned success by 2026-10-17T17:51:42Z. Exact remote readback completed by 2026-10-17T17:52:23Z.
- Published commit: `05675e52029e17738d553ff513ff6b636b3b3a39`; parent `9d1e0da9dc5fa9fa5ab7533691e762082cb6142d`; tree `cabfbf429ac32ac87caa34c87071b366f8bca637`.
- Guarded main update used force=false and expected_sha equal to the fresh observed parent. Subsequent main read returned the published commit. Complete before/after trees show four intended changed paths and zero removed files.
- `predictions/resolved/P000029.json`: exact checkpoint bytes, 5029 bytes, SHA-256 `422b42bc7eef866f83794a00adad76ead198ec8fccfdbd4f4ceaf09fb37419fa`, blob `34b69d88da1370665040042e83d3b8db372806b4`.
- `evaluations/prediction_scores.csv`: exact checkpoint bytes, 14084 bytes, SHA-256 `65bb9318c278ad7dd5c44ec36ac517d8c184f2437eecc32c93ad4de300b69d4d`, blob `9aa983d2fbae06516ac6ec9e314c3714353937ef`. Existing CSV is exact prefix; only P000029 row appended.
- `world_model/CURRENT_STATE.md`: old October12 snapshot retained plus bounded recovery notice; exact readback equals prepared text, blob `2b563c623ec1320a04f5ef4d647e7b0331ae9827`.
- `persistence/2026-10-17-publication-recovery.json`: exact prepared receipt readback, blob `c32156d9efc345e5d1301f14330ff4f21fb7ef38`. Its preparation status is retained historically; this record establishes subsequent success.

Outcome: partial publication recovery complete. Canonical ledger has 29 resolved records including 25 probability scores. Independent Repo B validation is still outstanding; no validation/learning/skill claim is added. No new calculations, market-data fetches, domain cycle, validators, trades, permissions, schedules, or other-repository writes occurred.

P000032 remains a checkpointed candidate, not registered. The remaining seven original files stay checkpoint-only. No backdated forecast registration or model/learning promotion was performed. October13–15 missing original outputs are still unavailable. Publication time is October17; preserved resolved_at is the original October16 assessment time, not an assertion that canonical publication happened then.

Next bounded decision: the primary producer must address its existing intake/validation gates and prospectively decide the candidate's disposition before further model/forecast promotion. This recovery does not delegate independent Repo B work.
