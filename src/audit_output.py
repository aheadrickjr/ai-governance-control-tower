# src/audit_output.py

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_OUTPUT_FILE = "output/validation_result_sample.json"


def build_validation_audit_record(
    source_file: str,
    validation_status: str,
    errors: List[str],
    dq_score: int,
    dq_severity: str,
    metadata: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Build a local audit record for a validation run.
    This creates evidence that a source file was checked, scored, and timestamped.
    """

    return {
        "audit_type": "validation_result",
        "control_tower": "AI Governance Control Tower",
        "source_file": source_file,
        "validation_status": validation_status,
        "error_count": len(errors),
        "errors": errors,
        "dq_score": dq_score,
        "dq_severity": dq_severity,
        "metadata": metadata or {},
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def write_audit_json(audit_record: Dict[str, Any], output_file: str = DEFAULT_OUTPUT_FILE) -> Path:
    """
    Write the audit record to a local JSON file.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(audit_record, json_file, indent=2)

    return output_path


def main() -> None:
    sample_errors = [
        "Row 3: Missing required value for 'expected_evidence'"
    ]

    sample_metadata = {
        "file_name": "sample_neg_controls.csv",
        "row_count": 3,
        "column_count": 5,
        "source_system": "AI Governance Control Tower"
    }

    audit_record = build_validation_audit_record(
        source_file="data/sample_neg_controls.csv",
        validation_status="FAILED",
        errors=sample_errors,
        dq_score=90,
        dq_severity="LOW",
        metadata=sample_metadata,
    )

    output_path = write_audit_json(audit_record)

    print("AUDIT JSON OUTPUT COMPLETE")
    print(f"File written: {output_path}")


if __name__ == "__main__":
    main()