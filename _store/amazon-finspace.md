---
aid: amazon-finspace
name: Amazon FinSpace
description: Amazon FinSpace is a data management and analytics service built specifically for the financial services industry. It reduces the time you spend on time-consuming data preparation tasks and makes it easy for analysts to access and analyze petabytes of financial data with a few clicks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Capital Markets
  - Data Analytics
  - Data Management
  - Financial Services
url: https://raw.githubusercontent.com/api-evangelist/amazon-finspace/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-finspace:amazon-finspace-api
    name: Amazon FinSpace API
    description: The Amazon FinSpace API provides programmatic access to create and manage FinSpace environments, datasets, data views, and user access controls for financial data management and analytics.
    humanURL: https://aws.amazon.com/finspace/
    baseURL: https://finspace.amazonaws.com
    tags:
      - Data Analytics
      - Data Management
      - Financial Services
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/finspace/latest/management-api/fs-api-welcome.html
      - type: OpenAPI
        url: openapi/amazon-finspace-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-finspace-environment-schema.json
      - type: JSONSchema
        url: json-schema/amazon-finspace-kx-environment-schema.json
      - type: JSONSchema
        url: json-schema/amazon-finspace-kx-cluster-schema.json
      - type: JSONSchema
        url: json-schema/amazon-finspace-kx-database-schema.json
      - type: JSONSchema
        url: json-schema/amazon-finspace-kx-user-schema.json
      - type: JSONStructure
        url: json-structure/amazon-finspace-environment-structure.json
      - type: JSONStructure
        url: json-structure/amazon-finspace-kx-environment-structure.json
      - type: JSONStructure
        url: json-structure/amazon-finspace-kx-cluster-structure.json
      - type: JSONStructure
        url: json-structure/amazon-finspace-kx-database-structure.json
      - type: JSONStructure
        url: json-structure/amazon-finspace-kx-user-structure.json
      - type: Example
        url: examples/amazon-finspace-environment-example.json
      - type: Example
        url: examples/amazon-finspace-kx-environment-example.json
      - type: Example
        url: examples/amazon-finspace-kx-cluster-example.json
      - type: Example
        url: examples/amazon-finspace-kx-database-example.json
      - type: Example
        url: examples/amazon-finspace-kx-user-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/finspace/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/finspace/pricing/
      - type: FAQ
        url: https://aws.amazon.com/finspace/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/finspace/latest/management-api/fs-api-welcome.html
common:
  - type: Portal
    url: https://aws.amazon.com/finspace/
  - type: Website
    url: https://aws.amazon.com/finspace/
  - type: Documentation
    url: https://docs.aws.amazon.com/finspace/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/industries/financial-services/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/finspace/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-finspace
  - type: SpectralRules
    url: rules/amazon-finspace-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/finspace.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-finspace-financial-analytics.yaml
  - type: Vocabulary
    url: vocabulary/amazon-finspace-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-finspace-context.jsonld
  - type: Features
    data:
      - name: Managed kdb Environment
        description: Fully managed kdb+ (kdb+/q) compute infrastructure with HDB, RDB, Gateway, and Tickerplant cluster types.
      - name: Financial Analytics Workspace
        description: Isolated FinSpace environments with preconfigured tools for financial data ingestion, preparation, and analysis.
      - name: Petabyte-Scale Data
        description: Store and query petabytes of financial time-series data including tick, OHLCV, and alternative datasets.
      - name: kdb+ Cluster Autoscaling
        description: Configure auto-scaling policies for kdb clusters to match intraday compute demand.
      - name: Multi-AZ Clusters
        description: Deploy kdb clusters across multiple availability zones for high availability.
      - name: IAM-Integrated Users
        description: Map FinSpace kdb users to IAM roles for fine-grained permission control.
      - name: SageMaker Integration
        description: Access financial data from FinSpace environments directly within Amazon SageMaker Studio.
  - type: UseCases
    data:
      - name: Tick Data Management
        description: Ingest, store, and query high-frequency market tick data (trades, quotes, order books) using kdb+ clusters.
      - name: Risk Analytics
        description: Run intraday risk calculations and post-trade analytics on financial time-series data at low latency.
      - name: Quantitative Research
        description: Provide quants and data scientists with managed kdb environments for backtesting and strategy development.
      - name: Regulatory Reporting
        description: Aggregate and transform trade and order data for regulatory submissions and compliance.
      - name: Alternative Data Processing
        description: Ingest and correlate alternative datasets (news, satellite, ESG) with market data for signal generation.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store and retrieve kdb database snapshots and bulk financial data files.
      - name: AWS KMS
        description: Encrypt FinSpace environments and kdb databases with customer-managed KMS keys.
      - name: AWS IAM
        description: Control user and application access to FinSpace resources with IAM roles and policies.
      - name: Amazon SageMaker
        description: Access FinSpace datasets and kdb environments from SageMaker Studio notebooks.
      - name: Amazon CloudWatch
        description: Monitor kdb cluster health, query performance, and resource utilization metrics.
      - name: AWS Transit Gateway
        description: Connect kdb environments to on-premises networks and other VPCs via Transit Gateway.
      - name: Amazon VPC
        description: Deploy kdb clusters in isolated VPC networking with security group controls.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
