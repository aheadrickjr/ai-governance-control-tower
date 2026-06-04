################################################

# Day 18 — S3 ObjectCreated Trigger Evidence
################################################

## Sprint Objective

Configure and confirm an Amazon S3 ObjectCreated event trigger that invokes the AWS Lambda validation function when a file lands in the governed S3 intake zone.
###################################################
## Starting State
###################################################
Day 16 completed the S3 landing bucket and folder convention.

Day 17 completed the Lambda S3 event metadata smoke test.

The current state entering Day 18 is:

```text
S3 event -> Lambda -> CloudWatch logging is working.

################################################
## Day 18 Test Result
################################################
The Day 18 test successfully confirmed that an uploaded CSV file in the governed S3 landing prefix invoked the Lambda function.

CloudWatch evidence showed:

```text
Record count: 1
S3 EVENT METADATA
bucket_name: tpd-ai-governance-landing-001
object_key: landing/sample_controls.csv
object_size: 327
event_name: ObjectCreated:Put