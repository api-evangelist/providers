---
name: Amazon Kinesis Data Firehose
description: Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. It can capture, transform, and deliver streaming data to Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and any custom HTTP endpoint. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/kinesis/data-firehose/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Kinesis Data Firehose API
    description: The Amazon Kinesis Data Firehose API provides the easiest way to reliably load streaming data into data lakes, data stores, and analytics services. The API allows you to create and manage delivery streams, configure data transformations using AWS Lambda, set up destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and custom HTTP endpoints, and put records into delivery streams. It automatically scales to match your data throughput with no ongoing administration required.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/kinesis/data-firehose/
    baseURL: https://firehose.amazonaws.com
    tags:
      - Analytics
      - AWS
      - Data Delivery
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/firehose/
      - type: OpenAPI
        url: openapi/amazon-kinesis-firehose-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/kinesis/data-firehose/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/data-firehose/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/data-firehose/faqs/
      - type: JSONSchema
        url: json-schema/amazon-kinesis-firehose-delivery-stream-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-firehose-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/kinesis/data-firehose/
  - type: Documentation
    url: https://docs.aws.amazon.com/firehose/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/firehose/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: Zero Administration
        description: Fully managed service that automatically scales to match data throughput with no ongoing administration.
      - name: Data Transformation
        description: Transform streaming data using AWS Lambda before delivering to destinations.
      - name: Multiple Destinations
        description: Deliver data to Amazon S3, Redshift, OpenSearch Service, Splunk, Datadog, and custom HTTP endpoints.
      - name: Format Conversion
        description: Automatically convert data formats such as JSON to Apache Parquet or Apache ORC before storing in S3.
      - name: Data Compression
        description: Compress data using GZIP, ZIP, or Snappy before delivering to S3 to reduce storage costs.
  - type: UseCases
    data:
      - name: Log Analytics
        description: Stream application and infrastructure logs to Amazon OpenSearch Service for real-time analysis.
      - name: Clickstream Analytics
        description: Capture website clickstream data and deliver to data lakes for behavioral analysis.
      - name: IoT Data Ingestion
        description: Ingest IoT device telemetry into S3 or Redshift for analytics and reporting.
      - name: Security Analytics
        description: Stream security events and logs to SIEM systems like Splunk for threat detection.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Deliver streaming data to S3 buckets as the primary data lake destination.
      - name: Amazon Redshift
        description: Load streaming data into Redshift data warehouse for SQL analytics.
      - name: Amazon OpenSearch Service
        description: Index streaming data in OpenSearch for real-time search and visualization.
      - name: AWS Lambda
        description: Transform and enrich streaming data using Lambda functions before delivery.
      - name: Splunk
        description: Send streaming data to Splunk for security and operational analytics.
  - type: SpectralRules
    url: rules/amazon-kinesis-firehose-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-kinesis-firehose-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-kinesis-firehose-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Analytics
  - AWS
  - Data Delivery
  - Streaming
---
