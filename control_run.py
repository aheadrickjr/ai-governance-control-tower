# src/control_run.py

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_OUTPUT_FILE = "output/control_run_result.json"

# Adjust this list only if the sample_controls.csv schema changes.
REQUIRED_FIELDS = [
    "control_id",
    "control_name",
    "expected_evidence",
]


def inspect_csv(file_path: Path) -> Dict[str, Any]:
    with file_path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = reader.fieldnames or []
        rows = list(reader)

    return {
        "columns": columns,
        "rows": rows,
        "row_count": len(rows),
        "column_count": len(columns),
    }


def validate_required_fields(rows: List[Dict[str, str]], required_fields: List[str]) -> List[str]:
    errors: List[str] = []

    for row_number, row in enumerate(rows, start=2):  # CSV header is row 1
        for field in required_fields:
            if field not in row:
                errors.append(f"Missing required column: {field}")
                continue

            value = row.get(field, "")
            if value is None or str(value).strip() == "":
                errors.append(f"Row {row_number}: Missing required value for '{field}'")

    return errors


def calculate_dq_score(error_count: int) -> Dict[str, Any]:
    score = max(0, 100 - (error_count * 10))

    if score >= 90:
        severity = "LOW"
    elif score >= 70:
        severity = "MEDIUM"
    else:
        severity = "HIGH"

    return {
        "score": score,
        "severity": severity,
        "error_count": error_count,
    }


def build_audit_record(
    source_file: Path,
    csv_profile: Dict[str, Any],
    errors: List[str],
    dq_result: Dict[str, Any],
) -> Dict[str, Any]:
    validation_status = "PASSED" if not errors else "FAILED"

    return {
        "audit_type": "control_run_result",
        "control_tower": "AI Governance Control Tower",
        "source_file": str(source_file),
        "validation_status": validation_status,
        "error_count": len(errors),
        "errors": errors,
        "dq_score": dq_result["score"],
        "dq_severity": dq_result["severity"],
        "metadata": {
            "file_name": source_file.name,
            "file_path": str(source_file),
            "row_count": csv_profile["row_count"],
            "column_count": csv_profile["column_count"],
            "columns": csv_profile["columns"],
            "source_system": "AI Governance Control Tower",
        },
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def write_json_output(audit_record: Dict[str, Any], output_file: str) -> Path:
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(audit_record, json_file, indent=2)

    return output_path


def run_control(source_file: str, output_file: str = DEFAULT_OUTPUT_FILE) -> Dict[str, Any]:
    source_path = Path(source_file)

    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    if not source_path.is_file():
        raise ValueError(f"Source path is not a file: {source_path}")

    csv_profile = inspect_csv(source_path)
    errors = validate_required_fields(csv_profile["rows"], REQUIRED_FIELDS)
    dq_result = calculate_dq_score(len(errors))

    audit_record = build_audit_record(
        source_file=source_path,
        csv_profile=csv_profile,
        errors=errors,
        dq_result=dq_result,
    )

    output_path = write_json_output(audit_record, output_file)

    return {
        "audit_record": audit_record,
        "output_path": str(output_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run an integrated AI Governance Control Tower validation flow."
    )

    parser.add_argument(
        "source_file",
        help="Path to the source CSV file to validate.",
    )

    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help="Path to write the JSON audit output.",
    )

    args = parser.parse_args()

    result = run_control(args.source_file, args.output)
    audit_record = result["audit_record"]

    print("CONTROL RUN COMPLETE")
    print(f"Source file: {audit_record['source_file']}")
    print(f"Validation status: {audit_record['validation_status']}")
    print(f"Error count: {audit_record['error_count']}")
    print(f"DQ score: {audit_record['dq_score']}")
    print(f"DQ severity: {audit_record['dq_severity']}")
    print(f"Output file: {result['output_path']}")

    if audit_record["errors"]:
        print("Errors:")
        for error in audit_record["errors"]:
            print(f"- {error}")


if __name__ == "__main__":
    main()