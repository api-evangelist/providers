---
aid: amazon-monitron
name: Amazon Monitron
description: Amazon Monitron is an end-to-end system that uses machine learning to detect abnormal behavior in industrial machinery. It includes sensors, a gateway, and the Monitron mobile app to enable predictive maintenance and reduce unplanned downtime.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-monitron/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-monitron:monitron-api
    name: Amazon Monitron API
    description: Amazon Monitron is an end-to-end system that uses machine learning to detect abnormal behavior in industrial machinery. It includes sensors, a gateway, and the Monitron mobile app to enable predictive maintenance and reduce unplanned downtime.
    humanURL: https://aws.amazon.com/monitron/
    baseURL: https://monitron.us-east-1.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/monitron/
      - type: OpenAPI
        url: openapi/amazon-monitron-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/monitron/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/monitron/pricing/
      - type: FAQ
        url: https://aws.amazon.com/monitron/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/monitron/
  - type: Documentation
    url: https://docs.aws.amazon.com/monitron/
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
    url: https://console.aws.amazon.com/monitron/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-monitron-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-monitron-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-monitron-media-workflow.yaml
  - type: Features
    data:
      - name: ML-Based Anomaly Detection
        description: Machine learning models trained on industrial machinery data to detect abnormal behavior automatically.
      - name: Project Management
        description: Organize machine monitoring deployments into projects with access control.
      - name: End-to-End System
        description: Integrated hardware sensors, gateway, cloud processing, and mobile app in one solution.
      - name: Predictive Maintenance
        description: Identify potential equipment failures before they occur to schedule proactive maintenance.
      - name: User Access Control
        description: Manage project administrators and user associations with fine-grained permissions.
  - type: UseCases
    data:
      - name: Industrial Equipment Monitoring
        description: Monitor motors, pumps, fans, and compressors for early signs of failure.
      - name: Predictive Maintenance Programs
        description: Build data-driven maintenance schedules based on actual equipment health.
      - name: Downtime Reduction
        description: Reduce unplanned production downtime by catching issues before equipment fails.
      - name: Plant-Wide Monitoring
        description: Deploy sensors across entire manufacturing facilities for comprehensive asset health.
  - type: Integrations
    data:
      - name: AWS IoT Core
        description: Monitron gateway connects to the cloud via AWS IoT Core.
      - name: Amazon Kinesis
        description: Stream Monitron measurement data to Kinesis for real-time analytics.
      - name: Amazon S3
        description: Export historical sensor data to S3 for long-term analysis.
      - name: AWS IAM
        description: Control API access and project permissions with IAM policies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
