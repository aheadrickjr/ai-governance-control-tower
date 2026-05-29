# src/metadata.py

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any


DEFAULT_SOURCE_SYSTEM = "AI Governance Control Tower"


def calculate_file_hash(file_path: Path) -> str:
    """
    Calculate SHA-256 hash for a file.
    This helps detect whether the file content changed between runs.
    """
    sha256_hash = hashlib.sha256()

    with file_path.open("rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


def inspect_csv(file_path: Path) -> Dict[str, Any]:
    """
    Inspect a CSV file and return row count, column count, and column names.
    """
    with file_path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        columns: List[str] = reader.fieldnames or []
        row_count = sum(1 for _ in reader)

    return {
        "row_count": row_count,
        "column_count": len(columns),
        "columns": columns,
    }


def capture_metadata(file_path: str, source_system: str = DEFAULT_SOURCE_SYSTEM) -> Dict[str, Any]:
    """
    Capture operational metadata for a source file.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    csv_profile = inspect_csv(path)

    metadata = {
        "file_name": path.name,
        "file_path": str(path),
        "file_hash_sha256": calculate_file_hash(path),
        "row_count": csv_profile["row_count"],
        "column_count": csv_profile["column_count"],
        "columns": csv_profile["columns"],
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_system": source_system,
    }

    return metadata


def main() -> None:
    default_file = "data/sample_controls.csv"
    metadata = capture_metadata(default_file)

    print("METADATA CAPTURE COMPLETE")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()