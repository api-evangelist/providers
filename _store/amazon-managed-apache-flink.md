---
aid: amazon-managed-apache-flink
name: Amazon Managed Service for Apache Flink
description: Amazon Managed Service for Apache Flink is the easiest way to transform and analyze streaming data in real time with Apache Flink. It enables you to build sophisticated streaming analytics applications using Apache Flink with fully managed infrastructure and pay-as-you-go pricing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache Flink
  - AWS
  - Big Data
  - Real-Time Processing
  - Streaming Analytics
url: https://raw.githubusercontent.com/api-evangelist/amazon-managed-apache-flink/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-managed-apache-flink:aws-managed-flink-api
    name: Amazon Managed Service for Apache Flink API
    description: The Amazon Managed Service for Apache Flink API provides programmatic access to create and manage streaming applications, application versions, snapshots, and VPC configurations for Apache Flink workloads. Covers 31 paths and 31 operations.
    humanURL: https://aws.amazon.com/managed-service-apache-flink/
    baseURL: https://kinesisanalytics.amazonaws.com
    tags:
      - Apache Flink
      - Real-Time Processing
      - Streaming Analytics
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-managed-apache-flink-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/managed-service-apache-flink/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/managed-service-apache-flink/pricing/
      - type: FAQ
        url: https://aws.amazon.com/managed-service-apache-flink/faqs/
      - type: JSONSchema
        url: json-schema/amazon-managed-apache-flink-application-detail-schema.json
      - type: JSON-LD
        url: json-ld/amazon-managed-apache-flink-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/managed-service-apache-flink/
  - type: Documentation
    url: https://docs.aws.amazon.com/managed-flink/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/tag/amazon-managed-service-for-apache-flink/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/flink/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-managed-apache-flink-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-managed-apache-flink-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/streaming-analytics-workflow.yaml
  - type: Features
    data:
      - name: Fully Managed Apache Flink
        description: Run Apache Flink applications without managing infrastructure, patching, or capacity planning.
      - name: Auto Scaling
        description: Automatically scales application parallelism based on streaming data volume.
      - name: Application Snapshots
        description: Create point-in-time snapshots of application state for fault tolerance and version management.
      - name: VPC Integration
        description: Deploy Flink applications within a VPC for secure access to private data sources.
      - name: Multiple Input Sources
        description: Connect to Kinesis Data Streams, Kinesis Data Firehose, MSK, and S3 as data sources.
  - type: UseCases
    data:
      - name: Real-Time Analytics
        description: Build streaming analytics pipelines to analyze data as it arrives from IoT devices, logs, or transactions.
      - name: Event-Driven Processing
        description: Process and transform event streams for real-time dashboards and operational monitoring.
      - name: Anomaly Detection
        description: Detect anomalies in streaming data for fraud detection and security monitoring.
      - name: ETL Pipelines
        description: Build real-time ETL pipelines to transform and enrich streaming data before loading to destinations.
  - type: Integrations
    data:
      - name: Amazon Kinesis Data Streams
        description: Use Kinesis streams as input sources for Flink applications.
      - name: Amazon MSK
        description: Connect to managed Kafka clusters as input sources.
      - name: Amazon S3
        description: Read reference data from S3 and write output to S3 buckets.
      - name: Amazon CloudWatch
        description: Monitor application metrics and logs in CloudWatch.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
