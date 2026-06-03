# S3 Landing Zone

## Purpose

This document records the Day 16 S3 landing zone setup for the AI Governance Control Tower sprint.

The S3 bucket provides a controlled cloud landing area for sample governance files before future validation, metadata capture, audit evidence generation, and Lambda event testing.

## Bucket Configuration

| Setting | Value |
|---|---|
| Bucket name | `tpd-ai-governace-leanding-001` |
| Bucket type | General purpose |
| Region | US East (Ohio) `us-east-2` |
| Public access | Block Public Access enabled |
| Default encryption | SSE-S3 enabled |
| Bucket Key | Enabled |
| Blocked encryption types | SSE-C |
| Test upload completed | Yes |
| Screenshots captured | Complete |

> Note: The bucket name above reflects the current bucket name documented in the uploaded draft. If the AWS bucket was actually recreated with corrected spelling, update the bucket name before committing.

## Folder Convention

The following S3 folder/prefix convention was created:

```text
landing/
raw/
processed/
rejected/
audit/
metadata/
```

## Folder Purpose

| Prefix | Purpose |
|---|---|
| `landing/` | General arrival zone / future intake placeholder |
| `raw/` | Source files exactly as received |
| `processed/` | Files after validation or transformation |
| `rejected/` | Failed or quarantined files |
| `audit/` | Validation evidence and audit outputs |
| `metadata/` | Metadata extracts, profiles, and hash records |

## Test Upload

A small sample control file was uploaded for testing.

```text
raw/sample_controls.csv
```

No production data, sensitive data, or large regulatory PDFs were uploaded.

## Guardrails

The bucket follows the Day 15 cost-control and security guardrails:

- AWS lab budget is active
- Dedicated IAM user used for sprint cloud work
- Root user avoided for normal build activity
- Block Public Access enabled
- Default server-side encryption enabled
- Small test file only
- No production or sensitive data uploaded
- No cross-region replication enabled
- No lifecycle automation enabled
- No paid downstream processing enabled yet

## Screenshots

The following screenshots support the S3 landing zone setup:

- Bucket overview: `docs/screenshots/s3-landing-zone/01-s3-bucket-overview.png`
- Block public access: `docs/screenshots/s3-landing-zone/02-s3-block-public-access.png`
- Default encryption: `docs/screenshots/s3-landing-zone/03-s3-default-encryption.png`
- Folder prefixes: `docs/screenshots/s3-landing-zone/04-s3-folder-prefixes.png`
- Raw file upload: `docs/screenshots/s3-landing-zone/05-s3-raw-upload-sample-controls.png`
- Bucket tags: `docs/screenshots/s3-landing-zone/06-s3-bucket-tags.png`

## Day 16 Status

Day 16 S3 landing zone setup is complete.

The bucket is ready for the Day 17 Lambda smoke test for S3 event metadata.
