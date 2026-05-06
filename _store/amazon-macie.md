---
aid: amazon-macie
name: Amazon Macie
description: Amazon Macie is a data security service that discovers sensitive data by using machine learning and pattern matching, provides visibility into data security risks, and enables automated protection against those risks. Macie automates the discovery of sensitive data, such as personally identifiable information (PII) and financial data, to provide you with a better understanding of the data that your organization stores in Amazon S3.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Security
  - Sensitive Data
  - Privacy
  - Compliance
  - Machine Learning
  - S3
url: https://raw.githubusercontent.com/api-evangelist/amazon-macie/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-macie:amazon-macie-api
    name: Amazon Macie API
    description: The Amazon Macie API provides programmatic access to create and manage the resources, data, and activities for discovering, classifying, and protecting sensitive data stored in Amazon S3 buckets. Covers 54 paths and 79 operations for findings management, classification jobs, bucket security, custom identifiers, multi-account administration, and allow lists.
    humanURL: https://aws.amazon.com/macie/
    baseURL: https://macie2.amazonaws.com
    tags:
      - Data Security
      - Sensitive Data
      - Privacy
      - Compliance
      - S3
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html
      - type: OpenAPI
        url: openapi/amazon-macie-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/macie/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/macie/pricing/
      - type: FAQ
        url: https://aws.amazon.com/macie/faq/
      - type: JSONSchema
        url: json-schema/amazon-macie-finding-schema.json
      - type: JSONStructure
        url: json-structure/amazon-macie-finding-structure.json
      - type: JSON-LD
        url: json-ld/amazon-macie-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/macie/
  - type: Documentation
    url: https://docs.aws.amazon.com/macie/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/macie/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-macie-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-macie-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-security-operations.yaml
  - type: Features
    data:
      - name: Automated Sensitive Data Discovery
        description: Automatically discovers and classifies sensitive data in S3 using ML and pattern matching.
      - name: PII and Financial Data Detection
        description: Detects personally identifiable information (PII), financial data, and credentials in S3 objects.
      - name: Custom Data Identifiers
        description: Create custom regex patterns to detect organization-specific sensitive data types.
      - name: Data Security Findings
        description: Generates detailed findings with severity ratings for all detected sensitive data exposures.
      - name: S3 Bucket Security Posture
        description: Provides visibility into bucket configurations, encryption status, and public access settings.
      - name: Multi-Account Support
        description: Manage Macie across multiple AWS accounts from a central administrator account.
      - name: Allow Lists
        description: Define allow lists to suppress false positives for known acceptable sensitive data patterns.
  - type: UseCases
    data:
      - name: GDPR and Privacy Compliance
        description: Discover and inventory personal data across S3 to support GDPR data mapping and compliance reporting.
      - name: PCI-DSS Compliance
        description: Detect credit card numbers and financial data stored in S3 to maintain PCI-DSS compliance.
      - name: Data Loss Prevention
        description: Identify sensitive data stored in public or insufficiently protected S3 buckets.
      - name: Security Incident Response
        description: Quickly determine if sensitive data was exposed in an S3 bucket involved in a security incident.
      - name: Data Governance
        description: Build a data inventory and understand where sensitive data lives across the organization.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Scans S3 buckets to discover and classify sensitive data objects.
      - name: AWS Security Hub
        description: Sends findings to Security Hub for centralized security posture management.
      - name: Amazon EventBridge
        description: Publishes findings events to EventBridge for automated remediation workflows.
      - name: AWS Organizations
        description: Integrates with Organizations for multi-account sensitive data discovery.
      - name: Amazon CloudWatch
        description: Publishes metrics and logs to CloudWatch for monitoring and alerting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
