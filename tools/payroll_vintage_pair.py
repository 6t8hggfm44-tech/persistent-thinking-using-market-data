#!/usr/bin/env python3
"""Stage prospective Market records. Publish both files together using the normal checkpoint procedure."""
import argparse
import calendar
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo

BASE = Path("evaluations/vintage_pairs")
EASTERN = ZoneInfo("America/New_York")
HYPOTHESES = ("H001", "H002", "H003", "H004")


def read(path):
    return json.loads(path.read_bytes())


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamp requires an explicit UTC offset")
    return parsed.astimezone(timezone.utc)


def iso(value):
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def target(month):
    year, number = month.split("-")
    return f"US_NONFARM_PAYROLL_MOM_{calendar.month_abbr[int(number)].upper()}_{year}_FIRST_RELEASE"


def probability(value, interior=False):
    if type(value) not in (int, float):
        raise ValueError("Probability must be a JSON number")
    value = Decimal(str(value))
    if not value.is_finite() or not 0 <= value <= 1 or (interior and value in (0, 1)):
        raise ValueError("Probability is outside the permitted bounds")
    return value


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing {label}")
    return value


def opportunities(root, now):
    design = read(root / BASE / "design.json")
    dates = read(root / BASE / "calendar.json")
    lower, upper = design["window_calendar_days_before_release"]
    registrations = {}
    for file in (root / BASE).glob("P*.json"):
        record = read(file)
        month = record["reference_month"]
        if month in registrations or file.stem != record["id"]:
            raise ValueError(f"Conflicting registrations for {month}")
        registrations[month] = record["id"]

    for month, release in dates.items():
        days = (timestamp(release).astimezone(EASTERN).date() - now.astimezone(EASTERN).date()).days
        missed = root / BASE / "missed" / (month + ".json")
        if month in registrations and missed.exists():
            raise ValueError(f"Month is both registered and missed: {month}")
        if month in registrations:
            state = "registered"
        elif missed.exists():
            state = "missed"
        elif days > upper:
            state = "upcoming"
        elif days < lower:
            state = "unaccounted"
        else:
            state = "in_window"
        yield {"reference_month": month, "scheduled_release_at": release, "state": state,
               "forecast_id": registrations.get(month)}


def input_manifest(root, inputs, cutoff):
    if not isinstance(inputs, list) or not inputs:
        raise ValueError("A frozen evidence packet is required")
    manifest = []
    for item in inputs:
        path = Path(item["path"])
        if path.is_absolute() or ".." in path.parts or path.parts[:1] != ("evidence",):
            raise ValueError("Evidence paths must be within the primary evidence directory")
        if not (root / path).resolve().is_relative_to((root / "evidence").resolve()):
            raise ValueError("Evidence resolves outside the primary evidence directory")
        available = timestamp(item["available_at"])
        if available > cutoff:
            raise ValueError("Evidence became available after the common cutoff")
        manifest.append({"path": path.as_posix(), "available_at": iso(available),
                         "sha256": hashlib.sha256((root / path).read_bytes()).hexdigest()})
    return manifest


def prepare(root, draft, now):
    design = read(root / BASE / "design.json")
    month = draft["reference_month"]
    window = {row["reference_month"]: row for row in opportunities(root, now)}.get(month)
    if not window or window["state"] != "in_window":
        raise ValueError("No open prospective issuance window for this month")
    cutoff = timestamp(draft["evidence_cutoff"])
    if (cutoff > now or cutoff.astimezone(EASTERN).date() != now.astimezone(EASTERN).date()
            or cutoff.astimezone(EASTERN).hour < 16 or now.astimezone(EASTERN).weekday() > 4):
        raise ValueError("Use the actual current post-close occurrence and common cutoff")
    prediction_id = draft["id"]
    if not re.fullmatch(r"P[0-9]{6}", prediction_id):
        raise ValueError("Expected canonical forecast ID Pnnnnnn")
    event_target = target(month)
    for folder in ("open", "resolved"):
        for path in (root / "predictions" / folder).glob("P*.json"):
            record = read(path)
            original = record.get("original_forecast", record)
            if path.stem == prediction_id or original.get("target") == event_target:
                raise ValueError(f"Existing ID or payroll target at {path}; never retrofit a pair")
    if not re.fullmatch(r"[0-9a-f]{40}", draft["source_commit"]):
        raise ValueError("Provide the immutable source snapshot commit")
    manifest = input_manifest(root, draft["evidence"], cutoff)
    conditional = draft["conditional_probabilities"]
    reasoning = draft["conditional_rationale"]
    if set(conditional) != set(HYPOTHESES) or set(reasoning) != set(HYPOTHESES):
        raise ValueError("Provide exactly one probability and rationale for each hypothesis")
    for key in HYPOTHESES:
        nonempty(reasoning[key], key + " rationale")
    probabilities = {key: probability(conditional[key]) for key in HYPOTHESES}

    arms = {}
    for role, vintage in design["weight_records"].items():
        weights = read(root / vintage["path"])["weights_after"]
        if weights != vintage["weights_after"] or sum(Decimal(str(v)) for v in weights.values()) != 1:
            raise ValueError(f"Weight record differs from the frozen {role} vintage")
        total = sum(probabilities[h] * Decimal(str(weights[h])) for h in HYPOTHESES)
        arms[role] = {"model_version": vintage["version"], "probability": float(total)}
        probability(arms[role]["probability"], interior=True)
    benchmark = design["benchmark"]
    series = [jobs for year in benchmark["first_release_by_year"].values() for jobs in year]
    hits = sum(jobs * 1000 >= design["threshold_jobs"] for jobs in series)
    if (hits, len(series)) != (30, 36):
        raise ValueError("Historical benchmark no longer matches the frozen 30/36")
    arms["benchmark"] = {"method": benchmark["method"], "probability": hits / len(series)}

    version = draft["live_model_version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid canonical model version")
    live = next((arm["probability"] for arm in (arms["current"], arms["previous"])
                 if arm["model_version"] == version), None)
    if live is None:
        live = float(probability(draft["live_probability"], interior=True))
    elif "live_probability" in draft and probability(draft["live_probability"]) != Decimal(str(live)):
        raise ValueError("Supplied live probability disagrees with the frozen vintage")
    surprises = draft["surprising_if"]
    if not isinstance(surprises, list) or not surprises:
        raise ValueError("Supply at least one observable surprise condition")
    for surprise in surprises:
        nonempty(surprise, "surprise condition")
    rationale = nonempty(draft["live_rationale"], "live rationale")
    release = window["scheduled_release_at"]
    common = {"id": prediction_id, "created_at": iso(now), "evidence_cutoff": iso(cutoff),
              "target": event_target}
    event = (f"First published seasonally adjusted change in U.S. total nonfarm payrolls for "
             f"{month} is at least 100,000 jobs over the previous month.")
    rule = (f"Use the first BLS Employment Situation release reporting the {month} seasonally "
            "adjusted total nonfarm establishment payroll one-month change. TRUE iff the "
            "published change is >=100000 jobs, including equality. If delayed, wait for first "
            "actual publication. If absent, keep pending. Exclude private-only, household, "
            "subsequent revisions and changes computed from later-vintage levels.")
    pair = {**common, "schema_version": 1, "experiment": design["experiment"],
            "reference_month": month, "scheduled_release_at": release, "arms": arms,
            "conditional_probabilities": conditional, "conditional_rationale": reasoning,
            "source_commit": draft["source_commit"], "evidence": manifest}
    canonical = {**common, "model_version": version, "forecast_type": "binary_probability",
                 "horizon": f"{(timestamp(release).astimezone(EASTERN).date() - cutoff.astimezone(EASTERN).date()).days}d",
                 "resolution_at": release, "resolution_rule": rule,
                 "forecast": {"event": event, "event_threshold_jobs_gte": 100000, "probability": live},
                 "benchmarks": [{"name": benchmark["method"], "probability": arms["benchmark"]["probability"],
                                 "source": benchmark["source"]}],
                 "rationale": [rationale], "surprising_if": surprises, "status": "open",
                 "hypothesis_links": list(HYPOTHESES), "paired_registration": str(BASE / (prediction_id + ".json"))}
    return {Path("predictions/open") / (prediction_id + ".json"): canonical,
            BASE / (prediction_id + ".json"): pair}


def stage(directory, files):
    directory.mkdir()  # exclusive, any interrupted private staging directory is discarded
    for path, payload in files.items():
        dest = directory / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("status")
    make = commands.add_parser("prepare")
    make.add_argument("draft", type=Path)
    make.add_argument("new_output_directory", type=Path)
    miss = commands.add_parser("miss")
    miss.add_argument("reference_month")
    miss.add_argument("reason")
    miss.add_argument("new_output_directory", type=Path)
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    try:
        if args.action == "status":
            print(json.dumps(list(opportunities(args.root, now)), indent=2))
        elif args.action == "prepare":
            stage(args.new_output_directory, prepare(args.root, read(args.draft), now))
        else:
            rows = {row["reference_month"]: row for row in opportunities(args.root, now)}
            row = rows[args.reference_month]
            if row["state"] != "unaccounted":
                raise ValueError("Only closed, unregistered windows can be marked missed")
            record = {"reference_month": row["reference_month"], "scheduled_release_at": row["scheduled_release_at"],
                      "experiment": read(args.root / BASE / "design.json")["experiment"],
                      "recorded_at": iso(now), "reason": nonempty(args.reason, "reason")}
            stage(args.new_output_directory, {BASE / "missed" / (row["reference_month"] + ".json"): record})
    except (KeyError, ValueError, OSError, TypeError) as exc:
        parser.exit(2, f"{exc}\n")


if __name__ == "__main__":
    main()
