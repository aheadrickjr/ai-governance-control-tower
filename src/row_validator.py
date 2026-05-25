# filename: src/row_validator.py

import csv
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT_FILE = BASE_DIR / "data" / "sample_controls.csv"

REQUIRED_COLUMNS = [
    "control_id",
    "control_name",
    "domain",
    "expected_evidence",
    "status",
]


def get_input_file() -> Path:
    """
    Get the input CSV file from the command line.
    If no filename is provided, use the default sample_controls.csv file.
    """
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

        if not input_path.is_absolute():
            input_path = BASE_DIR / input_path

        return input_path

    return DEFAULT_INPUT_FILE


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


def validate_required_values(rows: list[dict]) -> bool:
    """
    Validate that each row has values for all required columns.
    """
    all_rows_valid = True

    print("\nRow-level validation:")

    for row_number, row in enumerate(rows, start=1):
        control_id = row.get("control_id", f"ROW-{row_number}")
        missing_values = []

        for column in REQUIRED_COLUMNS:
            value = row.get(column)

            if value is None or value.strip() == "":
                missing_values.append(column)

        if missing_values:
            all_rows_valid = False
            print(f"FAIL: {control_id} is missing required values:")
            for column in missing_values:
                print(f" - {column}")
        else:
            print(f"PASS: {control_id}")

    return all_rows_valid


def validate_rows(rows: list[dict]) -> bool:
    """
    Run validation checks against the CSV rows.
    """
    print(f"Rows loaded: {len(rows)}")

    if not rows:
        return False

    print("\nColumns detected:")
    for column in rows[0].keys():
        print(f" - {column}")

    print("\nValidation checks:")
    columns_valid = validate_required_columns(rows)

    if not columns_valid:
        return False

    return validate_required_values(rows)


def main() -> None:
    input_file = get_input_file()

    print(f"Input file: {input_file}")

    rows = read_csv(input_file)
    validation_passed = validate_rows(rows)

    if validation_passed:
        print("\nOVERALL RESULT: PASS")
    else:
        print("\nOVERALL RESULT: FAIL")


if __name__ == "__main__":
    main()