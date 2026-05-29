# src/dq_score.py

def calculate_dq_score(error_count: int) -> dict:
    """
    Calculate a simple data quality score and severity level
    based on the number of validation errors.
    """
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
        "error_count": error_count
    }


if __name__ == "__main__":
    sample_error_count = 3
    result = calculate_dq_score(sample_error_count)

    print("DATA QUALITY SCORE")
    print(f"Score: {result['score']}")
    print(f"Severity: {result['severity']}")
    print(f"Error Count: {result['error_count']}")