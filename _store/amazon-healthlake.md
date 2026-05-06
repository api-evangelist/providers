---
aid: amazon-healthlake
name: Amazon HealthLake
description: Amazon HealthLake is a HIPAA-eligible service that gives healthcare providers, health insurance companies, and pharmaceutical companies the ability to store, transform, query, and analyze health data at scale in the cloud. It uses the Fast Healthcare Interoperability Resources (FHIR) standard.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - FHIR
  - Health Data
  - Healthcare
  - HIPAA
  - Cloud Computing
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthlake/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-healthlake:amazon-healthlake-api
    name: Amazon HealthLake API
    description: The Amazon HealthLake API provides programmatic access to create and manage FHIR datastores, import and export health data, and run analytics on FHIR-formatted health records.
    humanURL: https://aws.amazon.com/healthlake/
    baseURL: https://healthlake.amazonaws.com
    tags:
      - FHIR
      - Health Data
      - Healthcare
      - HIPAA
      - Datastores
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/healthlake/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-healthlake-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/healthlake/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/healthlake/pricing/
      - type: FAQ
        url: https://aws.amazon.com/healthlake/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/healthlake/latest/APIReference/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/healthlake/latest/APIReference/CommonParameters.html
      - type: JSONSchema
        url: json-schema/healthlake-create-fhir-datastore-request-schema.json
      - type: JSONLD
        url: json-ld/amazon-healthlake-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/healthlake/
  - type: Documentation
    url: https://docs.aws.amazon.com/healthlake/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/industries/healthcare/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/healthlake/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SDK
    url: https://aws.amazon.com/developer/tools/
  - type: CLI
    url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html
  - type: Features
    data:
      - name: FHIR Compliance
        description: Fully compliant with the FHIR R4 standard for healthcare data interoperability.
      - name: HIPAA-Eligible
        description: HIPAA-eligible service for storing and processing protected health information.
      - name: Integrated Data Import
        description: Bulk import FHIR-formatted health data from Amazon S3 with automated validation.
      - name: Data Export
        description: Export FHIR health data to Amazon S3 for analytics, archiving, or migration.
      - name: Integrated Search
        description: Query FHIR resources using standard FHIR search operations for clinical workflows.
      - name: Automated De-identification
        description: Built-in de-identification capabilities for removing PHI from health data.
      - name: Analytics Integration
        description: Integrated analytics with Amazon Comprehend Medical and other AWS analytics services.
  - type: UseCases
    data:
      - name: Clinical Data Repository
        description: Create a centralized FHIR-compliant repository for clinical data from multiple sources.
      - name: Health Data Exchange
        description: Enable interoperable health data exchange between healthcare providers and payers.
      - name: Population Health Management
        description: Analyze aggregated health data to identify trends and manage population health programs.
      - name: AI-Powered Clinical Insights
        description: Apply machine learning to FHIR data to generate clinical insights and predictions.
      - name: Research Data Platform
        description: Create de-identified research datasets from FHIR health records for clinical studies.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Import and export FHIR health data using S3 as the data source and destination.
      - name: AWS IAM
        description: Control access to HealthLake resources using IAM roles and policies.
      - name: Amazon CloudWatch
        description: Monitor HealthLake operations and performance metrics through CloudWatch.
      - name: Amazon Comprehend Medical
        description: Extract medical entities from unstructured health data using Comprehend Medical.
      - name: Amazon SageMaker
        description: Apply SageMaker ML models to FHIR data for predictive health analytics.
      - name: AWS Glue
        description: Transform and catalog FHIR health data for analytics using AWS Glue.
  - type: SpectralRules
    url: rules/amazon-healthlake-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-healthlake-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-healthlake-health-data-operations.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
