# Research Receipt Supplement — 2026-09-25

Actual Market receipt time for all four entries: **2026-09-25T21:16:11Z**.

This supplement exists because the connected write path would not safely perform a read-modify-write of the existing cumulative `evidence/research/INDEX.md` during this run. It does not backdate receipt to staging time. Future reconciliation should merge these rows into the cumulative index without changing the receipt timestamp.

| Domain | Delivery key | Version | Canonical report | Intake | Supersedes | Intake note |
|---|---|---:|---|---|---|---|
| freight | `freight:freight-suite-weekly-2026-09-23-v2:fd6c1df93afbd9d51281af5795a4e82a7b2df9245753d92f6f782525eb1f192b` | 2 | `freight/freight-suite-weekly-2026-09-23-v2/fd6c1df93afbd9d51281af5795a4e82a7b2df9245753d92f6f782525eb1f192b/Report.md` | same directory `intake.json` | v1 `89afb712...` | Provenance-only correction; no fresh observation; Port LA evidence deduplicated. |
| agriculture | `agriculture:agriculture-suite-weekly-2026-09-24:99e93496782e391e767c52ee60ca21bf83cfbbb882b84955716983e607b8a13d` | 1 | `agriculture/agriculture-suite-weekly-2026-09-24/99e93496782e391e767c52ee60ca21bf83cfbbb882b84955716983e607b8a13d/Report.md` | same directory `intake.json` | — | Final evidence gap; zero fresh observations and no crop-balance finding. |
| geopolitics | `geopolitics:geopolitics-suite-weekly-2026-09-24:94e9dd480510acb1e8ad45693fb4c054118ef28505f075d6b695a5e7c01946e2` | 1 | `geopolitics/geopolitics-suite-weekly-2026-09-24/94e9dd480510acb1e8ad45693fb4c054118ef28505f075d6b695a5e7c01946e2/Report.md` | same directory `intake.json` | — | Final evidence gap; no current-window original event document verified. |
| energy | `energy:energy-suite-weekly-2026-09-24:44062e355c41c431ce1e8deff78bc52309ecee1b5c0af8050f25311d8cdc4139` | 1 | `energy/energy-suite-weekly-2026-09-24/44062e355c41c431ce1e8deff78bc52309ecee1b5c0af8050f25311d8cdc4139/Report.md` | same directory `intake.json` | — | No-new-release result; prior Energy evidence unchanged. |
