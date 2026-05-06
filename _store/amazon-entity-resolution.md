---
name: Amazon Entity Resolution
description: Amazon Entity Resolution is a service that helps you match and link related records across multiple applications, channels, and data stores using machine learning and configurable matching techniques to identify and consolidate records that refer to the same entity.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/entity-resolution/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Data Integration
  - Data Matching
  - Entity Resolution
  - Machine Learning
apis:
  - name: Amazon Entity Resolution API
    description: API for creating and managing matching workflows, schema mappings, and ID mapping tables for matching and linking related records across data sources.
    humanURL: https://aws.amazon.com/entity-resolution/
    baseURL: https://entityresolution.amazonaws.com
    tags:
      - Data Integration
      - Data Matching
      - Entity Resolution
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/entityresolution/latest/userguide/
      - type: OpenAPI
        url: openapi/amazon-entity-resolution-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/entityresolution/latest/apireference/
      - type: GettingStarted
        url: https://aws.amazon.com/entity-resolution/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/entity-resolution/pricing/
      - type: FAQ
        url: https://aws.amazon.com/entity-resolution/faqs/
      - type: JSONSchema
        url: json-schema/amazon-entity-resolution-access-denied-exception-schema.json
      - type: JSONSchema
        url: json-schema/amazon-entity-resolution-attribute-matching-model-schema.json
      - type: JSONSchema
        url: json-schema/amazon-entity-resolution-attribute-name-schema.json
      - type: JSONLD
        url: json-ld/amazon-entity-resolution-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/entity-resolution/
  - type: Documentation
    url: https://docs.aws.amazon.com/entity-resolution/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/entityresolution/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/entity-resolution/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/entity-resolution
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-entity-resolution-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-entity-resolution-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-entity-resolution-vocabulary.yaml
  - type: Features
    data:
      - name: ML-Based Matching
        description: Use machine learning models to match records across disparate datasets
      - name: Rule-Based Matching
        description: Configure deterministic matching rules for exact and fuzzy matching
      - name: ID Mapping
        description: Create and manage identity graphs linking records across data sources
      - name: Schema Mapping
        description: Map input data schemas to standardized formats for consistent matching
      - name: Third-Party Data Providers
        description: Enrich records with data from LiveRamp, Unified ID 2.0, and others
  - type: UseCases
    data:
      - name: Customer Data Unification
        description: Create a single customer view by matching records across CRM, marketing, and transaction systems
      - name: Data Deduplication
        description: Identify and remove duplicate records from databases and data lakes
      - name: Identity Resolution for Advertising
        description: Link user identities across devices and channels for targeted advertising
      - name: Healthcare Record Matching
        description: Match patient records across different healthcare providers and systems
  - type: Integrations
    data:
      - name: AWS Glue
        description: Use Glue Data Catalog to discover and access input data sources
      - name: Amazon S3
        description: Store matching job input and output data in S3
      - name: Amazon Athena
        description: Query matching results using Athena SQL
      - name: LiveRamp
        description: Access LiveRamp identity data through the third-party provider integration
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
