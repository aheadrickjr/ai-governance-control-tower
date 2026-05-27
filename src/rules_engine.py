# filename: src/rules_engine.py

import csv
import sys
from pathlib import Path


DEFAULT_DATA_FILE = Path("data/sample_controls.csv")

REQUIRED_FIELDS = [
    "control_id",
    "control_name",
    "domain",
    "expected_evidence",
    "status",
]

VALID_STATUSES = {
    "Not Started",
    "In Progress",
    "Complete",
    "Blocked",
}


def validate_file_exists(file_path: Path) -> list[str]:
    if not file_path.exists():
        return [f"Data file not found: {file_path}"]

    if not file_path.is_file():
        return [f"Path is not a file: {file_path}"]

    return []


def validate_required_headers(headers: list[str]) -> list[str]:
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in headers:
            errors.append(f"Missing required column: {field}")

    return errors


def validate_required_values(row: dict, row_number: int) -> list[str]:
    errors = []

    for field in REQUIRED_FIELDS:
        value = row.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"Row {row_number}: Missing required value for '{field}'")

    return errors


def validate_status(row: dict, row_number: int) -> list[str]:
    errors = []

    status = str(row.get("status", "")).strip()

    if status and status not in VALID_STATUSES:
        errors.append(
            f"Row {row_number}: Invalid status '{status}'. "
            f"Expected one of: {sorted(VALID_STATUSES)}"
        )

    return errors


def validate_csv(file_path: Path) -> list[str]:
    errors = []

    errors.extend(validate_file_exists(file_path))

    if errors:
        return errors

    try:
        with file_path.open("r", newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)

            if reader.fieldnames is None:
                return ["CSV file has no header row."]

            errors.extend(validate_required_headers(reader.fieldnames))

            rows = list(reader)

    except Exception as error:
        return [f"Could not read CSV file: {error}"]

    if not rows:
        errors.append(f"CSV file contains no data rows: {file_path}")
        return errors

    for row_number, row in enumerate(rows, start=2):
        errors.extend(validate_required_values(row, row_number))
        errors.extend(validate_status(row, row_number))

    return errors


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1].strip():
        data_file = Path(sys.argv[1])
    else:
        data_file = DEFAULT_DATA_FILE

    errors = validate_csv(data_file)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED")
    print(f"File: {data_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())