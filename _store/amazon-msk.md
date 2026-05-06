---
aid: amazon-msk
name: Amazon MSK
description: Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data, with the infrastructure management handled by AWS.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-msk/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-msk:msk-api
    name: Amazon MSK API
    description: Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data, with the infrastructure management handled by AWS.
    humanURL: https://aws.amazon.com/msk/
    baseURL: http://kafka.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/msk/
      - type: OpenAPI
        url: openapi/amazon-msk-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/msk/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/msk/pricing/
      - type: FAQ
        url: https://aws.amazon.com/msk/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/msk/
  - type: Documentation
    url: https://docs.aws.amazon.com/msk/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/msk/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-msk-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-msk-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-msk-media-workflow.yaml
  - type: Features
    data:
      - name: Fully Managed Kafka
        description: Automatically provisions, configures, and maintains Apache Kafka clusters without operational overhead.
      - name: High Durability
        description: Multi-AZ deployments with automatic replication and failover for data durability.
      - name: MSK Serverless
        description: Serverless cluster mode that automatically scales capacity to match streaming demand.
      - name: MSK Connect
        description: Fully managed Kafka Connect to stream data to and from databases and other services.
      - name: Tiered Storage
        description: Offload older data to low-cost Amazon S3 storage while keeping recent data on brokers.
      - name: Schema Registry
        description: Manage and enforce schemas for Kafka topics with AWS Glue Schema Registry integration.
  - type: UseCases
    data:
      - name: Real-Time Data Streaming
        description: Build real-time data pipelines for clickstream analytics, log aggregation, and metrics.
      - name: Event Sourcing
        description: Implement event sourcing patterns with durable, ordered Kafka topics.
      - name: Stream Processing
        description: Process streaming data with Apache Flink, Spark Streaming, or custom consumers.
      - name: Database Change Data Capture
        description: Stream database changes to downstream systems using Debezium and MSK Connect.
  - type: Integrations
    data:
      - name: Amazon Kinesis Data Analytics
        description: Process MSK streams with Kinesis Data Analytics for Apache Flink.
      - name: AWS Lambda
        description: Trigger Lambda functions from MSK topics for serverless stream processing.
      - name: Amazon S3
        description: Use MSK Connect to sink data from Kafka topics to S3 buckets.
      - name: Amazon CloudWatch
        description: Monitor cluster and broker metrics with CloudWatch dashboards and alarms.
      - name: AWS IAM
        description: Authenticate Kafka clients using IAM roles for MSK cluster access control.
      - name: AWS Glue Schema Registry
        description: Enforce data schemas for Kafka producers and consumers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
