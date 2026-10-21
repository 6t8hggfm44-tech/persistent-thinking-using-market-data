# Persistence and validation health check — 2026-10-21

This is an operational health receipt, not a market-model cycle, evidence intake, forecast, score resolution, or hypothesis update.

## GitHub persistence
- Primary repository create/read/delete health check succeeded.
- Primary health-check create commit: `769f7831afeae1c2e11bc32e1007e88ac781fe5c`.
- Primary health-check delete commit: `46855b5846740279a353fc1d9bb73d80aa652e91`.
- Market Repo B create/read/delete health check succeeded.
- Repo B health-check create commit: `f99f7f5293603192823bfeb60c87fcaf9c37b709`.
- Repo B health-check delete commit: `edcac4b69eb1b564aa487a783441347440f2df54`.

## Validation
Against primary snapshot `46855b5846740279a353fc1d9bb73d80aa652e91`, the live Repo B parsing/scoring rules were reproduced from the canonical ledger:
- 25 parseable probability forecasts
- mean Brier 0.214144
- mean log loss 0.6186174413
- event rate 0.44
- mean assigned probability 0.4968
- Brier skill vs fixed 0.5 comparator 0.143424
- stored-vs-recomputed score mismatches: 0
- excluded non-probability rows: P000006, P000007, P000009, P000008

This is a deterministic port of the current Repo B validator logic, not literal execution of the Python file in its repository. The execution sandbox has no GitHub filesystem/network mount.

## Intake checker
The complete native Python intake checker was not literally executed. A full live-envelope sweep was attempted but exceeded the connector's per-call ceiling before every canonical intake JSON could be reread. Prior parity checks remain historical evidence only; future cycles must still run the required checker when an execution environment with the full snapshot is available.

## Historical gaps
The exact original Oct. 19–20 output packages remain unavailable. They must not be reconstructed from later summaries because that would create hindsight-contaminated pseudo-originals.

## Going forward
The live operating protocol already requires exact-byte output checkpoints before canonical publication. Future cycles must follow that checkpoint procedure and preserve the exact denial diagnostics if any write is blocked.
