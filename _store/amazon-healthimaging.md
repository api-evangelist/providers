---
aid: amazon-healthimaging
name: Amazon HealthImaging
description: AWS HealthImaging is a HIPAA-eligible service that helps healthcare providers and their software partners store, transform, and apply machine learning to medical images. It provides sub-second image retrieval and enables scaling from hundreds to millions of medical images.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Healthcare
  - HIPAA
  - Machine Learning
  - Medical Imaging
  - DICOM
url: https://raw.githubusercontent.com/api-evangelist/amazon-healthimaging/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-healthimaging:aws-healthimaging-api
    name: AWS HealthImaging API
    description: The AWS HealthImaging API provides programmatic access to create and manage datastores, image sets, and DICOM import jobs for storing and retrieving medical imaging data at scale. The API is HIPAA-eligible and supports sub-second image retrieval.
    humanURL: https://aws.amazon.com/healthimaging/
    baseURL: https://medical-imaging.us-east-1.amazonaws.com
    tags:
      - Healthcare
      - HIPAA
      - Medical Imaging
      - DICOM
      - Datastores
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/healthimaging/latest/devguide/API_Reference.html
      - type: OpenAPI
        url: openapi/amazon-healthimaging-openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/healthimaging/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/healthimaging/pricing/
      - type: FAQ
        url: https://aws.amazon.com/healthimaging/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/healthimaging/latest/devguide/API_Reference.html
      - type: Authentication
        url: https://docs.aws.amazon.com/healthimaging/latest/devguide/security-iam.html
      - type: JSONSchema
        url: json-schema/healthimaging-datastore-schema.json
      - type: JSONLD
        url: json-ld/amazon-healthimaging-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/healthimaging/
  - type: Documentation
    url: https://docs.aws.amazon.com/healthimaging/
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
    url: https://console.aws.amazon.com/healthimaging/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SDK
    url: https://aws.amazon.com/developer/tools/
  - type: CLI
    url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html
  - type: Features
    data:
      - name: HIPAA-Eligible Storage
        description: Fully HIPAA-eligible service for storing protected health information including medical images.
      - name: DICOM Support
        description: Native support for DICOM format, the standard for medical imaging data exchange and storage.
      - name: Sub-Second Retrieval
        description: Optimized storage architecture enabling sub-second retrieval of medical images at any scale.
      - name: Machine Learning Integration
        description: Built-in support for applying machine learning models to medical imaging data for analysis.
      - name: Scalable Datastores
        description: Create and manage datastores that scale from hundreds to millions of medical images.
      - name: Image Set Management
        description: Organize medical images into sets with comprehensive metadata management and versioning.
      - name: Bulk Import
        description: DICOM import jobs enable bulk import of medical imaging data from Amazon S3.
  - type: UseCases
    data:
      - name: Radiology Workflow
        description: Streamline radiology workflows by centralizing medical image storage and enabling rapid retrieval.
      - name: AI-Powered Diagnostics
        description: Apply machine learning models to medical images for automated diagnostic assistance.
      - name: Healthcare Data Archiving
        description: Archive medical imaging data in a HIPAA-eligible, scalable environment with long-term retention.
      - name: Multi-Site Imaging
        description: Centralize medical imaging data from multiple healthcare sites for unified access and analysis.
      - name: Clinical Research
        description: Support clinical research by providing scalable access to large medical imaging datasets.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Import medical imaging data from S3 buckets using DICOM import jobs.
      - name: AWS IAM
        description: Control access to HealthImaging resources using IAM roles and policies.
      - name: Amazon CloudWatch
        description: Monitor HealthImaging operations and performance metrics through CloudWatch.
      - name: AWS HealthLake
        description: Integrate with HealthLake for combining medical imaging with FHIR health records.
      - name: Amazon SageMaker
        description: Apply SageMaker ML models to medical images for AI-powered analysis and diagnostics.
  - type: SpectralRules
    url: rules/amazon-healthimaging-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-healthimaging-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-healthimaging-medical-imaging-operations.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
