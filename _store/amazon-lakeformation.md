---
name: AWS Lake Formation
description: AWS Lake Formation is a fully managed service that makes it easy to build, secure, and manage data lakes. It simplifies and automates many of the complex manual steps usually required to create data lakes, including collecting, cleansing, cataloging, and securely sharing data, with centralized governance and fine-grained access control across your analytics and machine learning services.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/lake-formation/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: AWS Lake Formation API
    description: The AWS Lake Formation API provides programmatic access to build and manage data lakes with centralized governance. It enables developers to register data sources, configure data permissions, manage data catalog resources, grant and revoke fine-grained access controls, and automate data ingestion and transformation workflows.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/lake-formation/
    baseURL: https://lakeformation.amazonaws.com
    tags:
      - Analytics
      - AWS
      - Data Lake
      - Governance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lake-formation/
      - type: OpenAPI
        url: openapi/amazon-lakeformation-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/lake-formation/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/lake-formation/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/lake-formation/faqs/
      - type: JSONSchema
        url: json-schema/amazon-lakeformation-database-schema.json
      - type: JSONSchema
        url: json-schema/amazon-lakeformation-data-cells-filter-schema.json
      - type: JSONLD
        url: json-ld/amazon-lakeformation-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/lake-formation/
  - type: Documentation
    url: https://docs.aws.amazon.com/lake-formation/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/lakeformation/
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
      - name: Data Lake Setup
        description: Set up a secure data lake in days with centralized governance and automated data ingestion.
      - name: Governed Tables
        description: ACID transactions, row-level security, and automatic compaction for governed tables.
      - name: Fine-Grained Access Control
        description: Column, row, and cell-level security policies enforced across analytics engines.
      - name: Blueprints
        description: Pre-built workflows to ingest data from common data sources into the data lake.
      - name: Data Sharing
        description: Share data across accounts and organizations with fine-grained permissions.
  - type: UseCases
    data:
      - name: Enterprise Data Lake
        description: Build a centralized data lake with governed access for analytics teams.
      - name: Data Mesh
        description: Implement a data mesh architecture with cross-account data sharing and governance.
      - name: Compliance Governance
        description: Enforce data access policies for GDPR, HIPAA, and other compliance requirements.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store and manage data lake content in S3 with Lake Formation governance.
      - name: AWS Glue
        description: Catalog data and run ETL jobs with Glue, governed by Lake Formation.
      - name: Amazon EMR
        description: Process large datasets with EMR Spark, respecting Lake Formation permissions.
      - name: Amazon QuickSight
        description: Visualize data lake content with QuickSight enforcing Lake Formation policies.
  - type: SpectralRules
    url: rules/amazon-lakeformation-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lakeformation-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lakeformation-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Analytics
  - AWS
  - Data Lake
  - Governance
---
