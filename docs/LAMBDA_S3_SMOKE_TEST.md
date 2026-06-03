# Lambda S3 Smoke Test

## Purpose

This document records the Day 17 Lambda smoke test for S3 event metadata.

The purpose of the test is to confirm that uploads to the S3 landing bucket can trigger a Lambda function and write S3 event metadata to CloudWatch Logs.

## Lambda Configuration

| Setting | Value |
|---|---|
| Function name | `tpd-s3-event-smoke-test` |
| Runtime | Python 3.14 |
| Region | `us-east-2` |
| Execution role | Basic Lambda execution role |
| Logging target | CloudWatch Logs |

## S3 Trigger Configuration

| Setting | Value |
|---|---|
| Source bucket | `tpd-ai-governance-landing-001` |
| Event type | ObjectCreated:Put |
| Prefix | `raw/` |
| Suffix | `.csv` |

## Smoke Test Result

A small CSV file was uploaded to:

```text
raw/sample_controls.csv