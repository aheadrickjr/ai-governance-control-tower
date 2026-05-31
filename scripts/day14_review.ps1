# scripts/day14_review.ps1

$OutputFile = "output/day14_review_output.txt"

"DAY 14 SPRINT REVIEW RUN" | Out-File $OutputFile
"Generated: $(Get-Date -Format o)" | Out-File $OutputFile -Append
"" | Out-File $OutputFile -Append

function Run-Step {
    param (
        [string]$Title,
        [string]$Command
    )

    "==================================================" | Out-File $OutputFile -Append
    $Title | Out-File $OutputFile -Append
    "Command: $Command" | Out-File $OutputFile -Append
    "--------------------------------------------------" | Out-File $OutputFile -Append

    cmd /c $Command 2>&1 | Out-File $OutputFile -Append

    "" | Out-File $OutputFile -Append
}

Run-Step "Run positive validation sample" "python src/rules_engine.py"
Run-Step "Run negative validation sample" "python src/rules_engine.py data/sample_neg_controls.csv"
Run-Step "Run data quality scoring" "python src/dq_score.py"
Run-Step "Run metadata capture" "python src/metadata.py"
Run-Step "Run audit JSON output" "python src/audit_output.py"
Run-Step "Display generated audit JSON" "type output\validation_result_sample.json"

"DAY 14 REVIEW COMPLETE" | Out-File $OutputFile -Append