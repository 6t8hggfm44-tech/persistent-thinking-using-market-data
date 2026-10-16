# Market output checkpoints and recovery

Scope: preserve generated original output bytes before canonical publication. This is transport and recovery tooling, not forecast creation, scientific validation, canonical intake, or permission to run an occurrence. No schedule, credentials, external service, Repo B, or governance change is introduced.

## Producer path

1. Read the current Market protocol and obtain the existing occurrence authority. Resolve the live main commit. Work in a private, stable local directory; do not allow concurrent source-file or directory mutation during capture. The tool rejects links at inspection and the final opened file, but is not a hostile-filesystem sandbox.
2. As soon as a complete phase output exists, and before attempting its canonical writes, checkpoint its exact original files. Use a unique run/phase/revision identity. Explicitly list all intended changed files; preserve full resolution records, ledger payloads, evidence, Skeptic output, model/no-change records and final report when generated. Do not substitute a summary for these originals. Do not reconstruct missing October 13–15 files.
3. Example (replace placeholders with observed identifiers):

   python3 tools/market_checkpoint.py prepare --root PRIVATE_OUTPUT_DIRECTORY --run-id RUN_PHASE_REVISION --source-commit IMMUTABLE_MAIN_SHA --kind original-output --output PRIVATE_CHECKPOINT.json PATH_ONE PATH_TWO

   The output is LOCAL ONLY. Verify it exists and retain it. It contains exact file bytes (base64), per-file SHA-256 and lengths, run identity and original source commit. These hashes establish integrity, not origin authenticity or semantic completeness. Maximum serialized package is 32 MiB. The explicitly listed inventory must be checked against the phase deliverables by the producer. Do not include credentials, private unrelated data or executable files from untrusted sources.
4. Through the existing authorized GitHub connector, create a new checkpoint path under persistence/checkpoints/RUN_PHASE_REVISION.json. Preserve the entire current parent tree, create one commit with that fresh parent, and update main with force=false and expected_sha equal to the observed head. Never overwrite a checkpoint. If that path already exists, fetch and compare exact bytes: identical is idempotent; differing bytes are a conflict. If main advanced, reread and preserve intervening changes before making a new descendant. This procedure is deliberately manual at the connector boundary; this offline Python tool does not authenticate or publish.
5. Fetch the published checkpoint and its independent tree blob SHA/byte length at the immutable new commit. Compare exact bytes to the prepared local file, then run:

   python3 tools/market_checkpoint.py verify FETCHED_CHECKPOINT.json --blob-sha IMMUTABLE_TREE_BLOB_SHA --bytes IMMUTABLE_TREE_BYTE_LENGTH

   Record the actual commit, checkpoint SHA-256 and verified status. A created blob/tree/commit without a verified branch update is not saved on main. A branch update with failed readback is unverified; inspect before retrying. On any permission/security denial, stop that write and report its exact action/target/error; do not switch route, encode differently or split content to evade the gate.
6. Only then proceed with separately authorized canonical publication under the existing phase rules. Fresh-head guards, complete parent preservation and exact remote readback apply again. A checkpoint never resolves a forecast, updates scores, passes intake, validates the model, or authorizes replay. Preserve any required Repo B separation and index checks. This workflow grants no new authority for those steps.
7. If canonical publication fails, retain the verified checkpoint identity and report canonical publication as failed or unverified. If checkpoint publication fails, retain local bytes, report them as local-only, and pause the dependent canonical publication; do not report the cycle as durably saved. If the local runtime is then lost, recovery is not guaranteed. A different storage destination requires its own authority; this mechanism does not bypass a GitHub gate or provide independent backup against GitHub loss.

## Recovery path

- Fetch only the checkpoint at its immutable commit and independently verify its blob identity/length. Use the verify command above; integrity does not make arbitrary content trusted.
- Recover into a new private quarantine directory, never the repository or a canonical path:

  python3 tools/market_checkpoint.py recover FETCHED_CHECKPOINT.json NEW_QUARANTINE_DIRECTORY

- Recovery decodes exact bytes, refuses an existing destination, checks recovered bytes, syncs files/directory links and writes RECOVERY_COMPLETE.json last. An interrupted extraction may leave a partial quarantine; without that receipt it is incomplete. Inspect it and retry into a different new directory. Do not delete or overwrite the partial copy automatically.
- A completion receipt means only quarantine byte recovery. Review provenance, source commit, subsequent canonical commits and current authority before any promotion. The tool performs no canonical promotion, recomputation, validator run or execution of extracted files. Recovered files may be stale and must never overwrite newer canonical work.
- To diagnose a failed write, capture the exact non-secret tool action, target path/ref, expected head, returned error/denial class, known returned object IDs and read-only remote state. Do not infer a technical cause from a final-summary phrase such as “GitHub blocked writes.” Do not copy credential-bearing diagnostics.

## Established boundary

The October 16 tests and remote synthetic canary establish this bounded checkpoint/readback/quarantine path only. The ongoing product-managed Market producer has not yet been observed invoking it. The next already-authorized cycle must record a real original-output checkpoint and readback before unattended adoption can be claimed. No new cycle is launched by this repair. The original October 13–15 full payloads remain unavailable.

Run isolated tests with:

    python3 -m unittest discover -s tests -p test_market_checkpoint.py -v
