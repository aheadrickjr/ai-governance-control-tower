# Day 19 — Lambda Cloud Validation Evidence

## Sprint Objective

Move the local Python validation logic into AWS Lambda so S3-uploaded governance control files are validated automatically in the cloud.

## Starting State

Day 18 confirmed the event-driven pattern:

```text
S3 landing upload
-> ObjectCreated event
-> Lambda invocation
-> CloudWatch evidence