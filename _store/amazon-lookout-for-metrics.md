---
aid: amazon-lookout-for-metrics
name: Amazon Lookout for Metrics
description: Amazon Lookout for Metrics uses machine learning to automatically detect anomalies in business and operational metrics such as revenue performance, customer engagement, and user activity. It continuously monitors data from various sources including Amazon S3, CloudWatch, RDS, Redshift, Athena, and AppFlow, providing root cause analysis and alert notifications when anomalies are detected.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Anomaly Detection
  - AWS
  - Business Intelligence
  - Machine Learning
  - Metrics
  - Monitoring
url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-metrics/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-lookout-for-metrics:amazon-lookout-for-metrics-api
    name: Amazon Lookout for Metrics API
    description: The Amazon Lookout for Metrics API provides programmatic access to create and manage anomaly detectors, anomaly groups, alerts, and datasets for automated anomaly detection in business metrics. Supports detector lifecycle management, metric set configuration, alert creation, anomaly analysis, feedback collection, and resource tagging across 30 operations.
    humanURL: https://aws.amazon.com/lookout-for-metrics/
    baseURL: https://lookoutmetrics.amazonaws.com
    tags:
      - Anomaly Detection
      - Machine Learning
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lookoutmetrics/latest/api/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-lookout-for-metrics-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/lookout-for-metrics/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/lookout-for-metrics/pricing/
      - type: FAQ
        url: https://aws.amazon.com/lookout-for-metrics/faqs/
      - type: JSONSchema
        url: json-schema/amazon-lookout-for-metrics-activate-anomaly-detector-response-schema.json
      - type: JSONStructure
        url: json-structure/amazon-lookout-for-metrics-activate-anomaly-detector-response-structure.json
      - type: JSON-LD
        url: json-ld/amazon-lookout-for-metrics-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/lookout-for-metrics/
  - type: Documentation
    url: https://docs.aws.amazon.com/lookoutmetrics/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/tag/amazon-lookout-for-metrics/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/lookoutmetrics/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-lookout-for-metrics-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-lookout-for-metrics-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/anomaly-detection-operations.yaml
  - type: Features
    data:
      - name: Automated Anomaly Detection
        description: Uses ML to automatically detect anomalies in business and operational metrics without requiring ML expertise.
      - name: Root Cause Analysis
        description: Identifies the top contributors to each anomaly to help determine root causes quickly.
      - name: Multi-Source Data Ingestion
        description: Connects to Amazon S3, CloudWatch, RDS, Redshift, Athena, and AppFlow as data sources.
      - name: Continuous Monitoring
        description: Continuously monitors metrics and sends real-time alerts when anomalies are detected.
      - name: Alert Configuration
        description: Configure alerts via Amazon SNS, Lambda, or other AWS services when anomalies occur.
      - name: Anomaly Feedback
        description: Provide feedback on detected anomalies to improve future detection accuracy.
      - name: Resource Tagging
        description: Tag anomaly detectors and related resources for cost allocation and organization.
  - type: UseCases
    data:
      - name: Revenue Anomaly Detection
        description: Monitor revenue metrics and detect unexpected drops or spikes that could indicate fraud or system issues.
      - name: Customer Engagement Monitoring
        description: Track customer engagement metrics and alert teams when patterns deviate from expected ranges.
      - name: Operational Metrics Monitoring
        description: Monitor operational metrics such as system performance, error rates, and throughput for anomalies.
      - name: E-Commerce Performance
        description: Detect anomalies in e-commerce metrics like conversion rates, cart abandonment, and sales volume.
      - name: User Activity Analysis
        description: Analyze user activity patterns and detect unusual behavior that may indicate security incidents.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Use S3 buckets as a data source for metric data in CSV or JSON format.
      - name: Amazon CloudWatch
        description: Ingest CloudWatch metrics directly for anomaly detection.
      - name: Amazon RDS
        description: Connect to RDS databases to retrieve metric data for analysis.
      - name: Amazon Redshift
        description: Use Redshift data warehouse as a source for business metrics.
      - name: Amazon Athena
        description: Query Athena tables to feed metric data into anomaly detectors.
      - name: AWS AppFlow
        description: Use AppFlow connectors to ingest data from SaaS applications.
      - name: Amazon SNS
        description: Send alert notifications via SNS topics when anomalies are detected.
      - name: AWS Lambda
        description: Trigger Lambda functions in response to detected anomalies for custom workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
