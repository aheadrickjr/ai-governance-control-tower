# filename: src/validator.py

import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "sample_controls.csv"

REQUIRED_COLUMNS = [
    "control_id",
    "control_name",
    "domain",
    "expected_evidence",
    "status",
]


def read_csv(file_path: Path) -> list[dict]:
    """
    Read a CSV file and return rows as a list of dictionaries.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with file_path.open(mode="r", encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def validate_required_columns(rows: list[dict]) -> bool:
    """
    Validate that all required columns exist in the CSV.
    """
    if not rows:
        print("FAIL: CSV contains no data rows.")
        return False

    actual_columns = set(rows[0].keys())
    required_columns = set(REQUIRED_COLUMNS)

    missing_columns = required_columns - actual_columns

    if missing_columns:
        print("FAIL: Missing required columns:")
        for column in sorted(missing_columns):
            print(f" - {column}")
        return False

    print("PASS: Required columns present")
    return True


def validate_rows(rows: list[dict]) -> None:
    """
    Run validation checks against the CSV rows.
    """
    print(f"Rows loaded: {len(rows)}")

    if not rows:
        return

    print("\nColumns detected:")
    for column in rows[0].keys():
        print(f" - {column}")

    print("\nValidation checks:")
    validate_required_columns(rows)

    print("\nSample first row:")
    print(rows[0])


def main() -> None:
    rows = read_csv(INPUT_FILE)
    validate_rows(rows)


if __name__ == "__main__":
    main()