---
aid: amazon-data-exchange
name: Amazon Data Exchange
description: AWS Data Exchange makes it easy to find, subscribe to, and use third-party data in the cloud. Qualified data providers can publish data products consisting of data sets with versioned revisions and assets including S3 snapshots, Redshift data shares, API Gateway APIs, and Lake Formation permissions. Subscribers can find and subscribe to data products directly in the AWS Management Console and use the Data Exchange API to load data into Amazon S3 for analysis with AWS analytics and machine learning services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Exchange
  - Data Marketplace
  - Third-Party Data
  - Analytics
  - Subscriptions
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-data-exchange:aws-data-exchange-api
    name: AWS Data Exchange API
    description: The AWS Data Exchange API enables programmatic access to find, subscribe to, and use third-party data products. It supports managing data sets, revisions, assets, jobs, and event actions for cloud-based data exchange workflows including S3 snapshot data, Redshift data shares, API Gateway APIs, and Lake Formation permissions.
    humanURL: https://aws.amazon.com/data-exchange/
    baseURL: https://dataexchange.amazonaws.com
    tags:
      - Data Marketplace
      - Data Products
      - Subscriptions
      - Analytics
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/data-exchange/latest/apireference/
      - type: OpenAPI
        url: openapi/amazon-data-exchange-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/dataexchange/2017-07-25/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/data-exchange/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/data-exchange/pricing/
      - type: FAQ
        url: https://aws.amazon.com/data-exchange/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/data-exchange/latest/apireference/
      - type: JSONSchema
        url: json-schema/data-set-schema.json
      - type: JSONSchema
        url: json-schema/revision-schema.json
      - type: JSONSchema
        url: json-schema/asset-schema.json
      - type: JSONSchema
        url: json-schema/job-schema.json
      - type: JSONSchema
        url: json-schema/event-action-schema.json
      - type: JSONLD
        url: json-ld/amazon-data-exchange-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/data-exchange/
  - type: DeveloperPortal
    url: https://aws.amazon.com/data-exchange/
  - type: Documentation
    url: https://docs.aws.amazon.com/data-exchange/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-data-exchange/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/dataexchange/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-data-exchange-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-data-exchange-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-marketplace-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/data-exchange.yaml
  - type: Features
    data:
      - name: Data Set Management
        description: Create, update, and manage data sets containing versioned collections of data available for subscription and distribution in the marketplace.
      - name: Revision Publishing
        description: Organize data into versioned revisions with comments, then finalize and publish them to make data available to subscribers automatically.
      - name: Multi-Format Asset Support
        description: Support for S3 snapshots, Redshift data shares, API Gateway APIs, Lake Formation permissions, and S3 data access as asset types.
      - name: Import and Export Jobs
        description: Asynchronous import/export jobs for transferring data between external sources (S3, Redshift) and Data Exchange revisions at scale.
      - name: Event-Driven Delivery
        description: Configurable event actions that automatically export revision data to S3 when a new revision is published, eliminating manual downloads.
      - name: AWS Marketplace Integration
        description: Seamlessly list and sell data products in AWS Marketplace with built-in billing, subscription management, and entitlement enforcement.
      - name: Fine-Grained Access Control
        description: Control access to data products using AWS IAM policies and resource- level permissions with ARN-based resource identification.
  - type: UseCases
    data:
      - name: Third-Party Data Acquisition
        description: Subscribe to curated third-party datasets from financial data providers, healthcare data aggregators, weather services, and market research firms.
      - name: Data Product Monetization
        description: Publish and sell proprietary datasets to other AWS customers via the marketplace with automated billing and subscription management.
      - name: Automated Data Pipelines
        description: Configure event actions to automatically deliver new data revisions to S3, enabling downstream analytics pipelines to process fresh data.
      - name: ML Training Data
        description: Access high-quality labeled datasets and specialized data products from Data Exchange to train and improve machine learning models.
      - name: Regulatory Compliance Data
        description: Subscribe to compliance reference data including sanctions lists, legal entity identifiers, and regulatory taxonomies via Data Exchange.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Primary storage integration for Data Exchange assets — used as both source for imports and destination for exports via job operations.
      - name: Amazon Redshift
        description: Share Redshift tables and views directly through Data Exchange without copying data, enabling live query access for subscribers.
      - name: AWS Lake Formation
        description: Distribute Lake Formation data permissions through Data Exchange, giving subscribers governed access to data lake resources.
      - name: Amazon API Gateway
        description: Expose API-based data products through Data Exchange, allowing subscribers to call APIs for real-time data access.
      - name: AWS Glue
        description: Catalog and transform Data Exchange S3 datasets using AWS Glue for ETL and data lake integration workflows.
      - name: Amazon Athena
        description: Query Data Exchange S3 snapshot data directly with SQL using Athena for serverless analytics on subscribed datasets.
      - name: Amazon SageMaker
        description: Use third-party datasets from Data Exchange as training data for machine learning models in Amazon SageMaker.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
