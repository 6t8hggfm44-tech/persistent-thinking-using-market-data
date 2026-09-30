#!/usr/bin/env python3
"""Read-only parity check for canonical intake records and their own indexes.

Run against a complete immutable repository snapshot. Pending packets and index
supplements are excluded: staging is not receipt, and a supplement cannot hide
a missing cumulative-index row. This checks bookkeeping, not report integrity,
receipt timing, scientific claims, or source access.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

KEY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*(?::[A-Za-z0-9][A-Za-z0-9._-]*)?:[0-9a-f]{64}")


def index_keys(path):
    """Read only Delivery key cells, never supersedes references or prose."""
    keys, errors, column = [], [], None
    if not path.is_file():
        return keys, ["missing index: " + str(path)]
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            # Historical index appends include blank lines between ledger rows.
            # Preserve the declared key column across prose/blank separators.
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if "Delivery key" in cells:
            column = cells.index("Delivery key")
            continue
        if column is None or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        key = cells[column].strip("`") if column < len(cells) else ""
        if not KEY.fullmatch(key):
            errors.append(f"invalid delivery key at {path}:{number}")
        else:
            keys.append(key)
    return keys, errors


def check(root):
    groups, errors = {}, []
    for name, relative, pattern in [
        ("research", "evidence/research", "*/*/*/intake.json"),
        ("gev", "evidence/gev-weekly", "*/*/intake.json"),
    ]:
        archive = root / relative
        canonical = []
        if not archive.is_dir():
            errors.append("missing archive: " + relative)
        for path in sorted(archive.glob(pattern)):
            parts = path.relative_to(archive).parts
            if name == "research" and parts[0] == "pending":
                continue
            expected = ":".join(parts[:-1])
            if name == "research" and parts[0] == "gev":
                errors.append("GEV record in research archive: " + str(path.relative_to(root)))
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                key = data.get("delivery_key")
                if not isinstance(key, str) or not KEY.fullmatch(key) or key != expected:
                    raise ValueError("delivery key does not match canonical path")
                canonical.append(key)
            except (OSError, UnicodeError, ValueError, AttributeError) as exc:
                errors.append(f"invalid intake {path.relative_to(root)}: {exc}")
        indexed, index_errors = index_keys(archive / "INDEX.md")
        errors.extend(index_errors)
        canonical_counts, index_counts = Counter(canonical), Counter(indexed)
        result = {
            "canonical_records": len(canonical),
            "index_rows": len(indexed),
            "missing_index_keys": sorted(canonical_counts.keys() - index_counts.keys()),
            "index_keys_without_canonical_record": sorted(index_counts.keys() - canonical_counts.keys()),
            "duplicate_index_keys": sorted(key for key, count in index_counts.items() if count > 1),
            "duplicate_canonical_keys": sorted(key for key, count in canonical_counts.items() if count > 1),
        }
        groups[name] = result
    passed = not errors and all(
        not values[field]
        for values in groups.values()
        for field in ("missing_index_keys", "index_keys_without_canonical_record",
                      "duplicate_index_keys", "duplicate_canonical_keys")
    )
    return {"schema_version": 1, "scope": "read_only_canonical_index_parity",
            "passed": passed, "archives": groups, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = check(args.repository.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
