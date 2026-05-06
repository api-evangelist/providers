---
aid: airbyte
url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/apis.yml
apis:
  - aid: airbyte:airbyte
    name: Airbyte
    tags:
      - Data Integration
      - ETL
      - ELT
      - Open Source
      - Data Pipeline
      - Connectors
    humanURL: https://airbyte.com
    properties:
      - url: https://docs.airbyte.com
        type: Documentation
      - url: https://reference.airbyte.com/reference/getting-started
        type: APIReference
      - url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/openapi/airbyte-openapi.yml
        type: OpenAPI
      - url: https://docs.airbyte.com/api-documentation
        type: Authentication
      - url: https://github.com/airbytehq/airbyte-api-python-sdk
        type: SDK
        title: Python SDK
      - url: https://github.com/airbytehq/airbyte-api-java-sdk
        type: SDK
        title: Java SDK
      - url: https://pypi.org/project/airbyte-api/
        type: SDK
        title: Python SDK PyPI
      - url: https://github.com/airbytehq/terraform-provider-airbyte
        type: SDK
        title: Terraform Provider
    description: Airbyte is an open-source data integration platform that enables businesses to move and consolidate data from various sources into centralized destinations. The Airbyte API provides programmatic control over sources, destinations, connections, jobs, workspaces, and organizations for both Airbyte Cloud and self-managed deployments.
    baseURL: https://api.airbyte.com/v1
name: Airbyte
tags:
  - Data Integration
  - ETL
  - ELT
  - Open Source
  - Data Pipeline
  - Connectors
  - Data
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://airbyte.com
    type: Portal
  - url: https://cloud.airbyte.io
    type: Console
  - url: https://cloud.airbyte.io
    type: SignUp
  - url: https://airbyte.com/pricing
    type: Pricing
  - url: https://github.com/airbytehq
    type: GitHubOrganization
  - url: https://github.com/airbytehq/airbyte
    type: GitHubRepository
  - url: https://docs.airbyte.com
    type: GettingStarted
  - url: https://status.airbyte.com
    type: StatusPage
  - url: https://airbyte.com/blog
    type: Blog
  - url: https://airbyte.com/tutorials
    type: Tutorials
  - url: https://support.airbyte.com/hc/en-us
    type: Support
  - url: https://airbyte.com/company/privacy-policy
    type: PrivacyPolicy
  - url: https://airbyte.com/company/terms
    type: TermsOfService
  - url: https://airbyte.com/community/newsletter
    type: Newsletter
  - url: https://docs.airbyte.com/category/release-notes/
    type: ChangeLog
  - url: https://github.com/orgs/airbytehq/projects/37/views/1
    type: RoadMap
  - url: https://airbyte.com/connectors
    type: Integrations
  - url: https://github.com/airbytehq/PyAirbyte
    type: SDK
    title: PyAirbyte
  - url: https://github.com/airbytehq/abctl
    type: CLI
    title: Airbyte CLI (abctl)
  - url: https://github.com/airbytehq/airbyte-python-cdk
    type: SDK
    title: Python Connector CDK
  - url: https://github.com/airbytehq/airbyte-agent-sdk
    type: SDK
    title: Agent SDK
  - url: https://artifacthub.io/packages/helm/airbyte/airbyte
    type: SDK
    title: Helm Chart
  - type: Features
    data:
      - 'Core: free open-source self-managed'
      - 'Standard from $10/mo: fully managed, volume-based'
      - 'Plus: bulk-credit discounts, accelerated support'
      - 'Pro: Data Workers capacity pricing, SSO, RBAC'
      - 'Enterprise Flex: custom limits, dedicated SA'
      - 600+ pre-built connectors
      - Public API at 60 req/min/workspace
      - OAuth 2.0 + workspace API keys
      - Webhooks for sync events
      - Connector Builder for custom sources
      - dbt Cloud integration for transformations
      - Multiple workspaces (Pro+)
      - SSO and RBAC (Pro+)
      - Self-hosted Enterprise option
      - Bring your own custom connector
      - Data Activation (Reverse ETL) capabilities
    sources:
      - https://airbyte.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Data Warehouse Loading
        description: Sync operational data to Snowflake, BigQuery, Redshift, or other warehouses.
      - name: Data Lake Ingestion
        description: Land raw data into S3, GCS, or Azure data lakes.
      - name: Analytics Pipelines
        description: Build ELT pipelines for business intelligence and analytics.
      - name: AI/ML Data Preparation
        description: Aggregate training data from multiple sources for machine learning.
      - name: API Data Sync
        description: Pull data from SaaS APIs (Salesforce, HubSpot, Stripe) into your data stack.
      - name: Database Replication
        description: Replicate relational databases with CDC change data capture.
      - name: Vector Database Population
        description: Load and embed data into vector stores for AI search and retrieval.
  - type: Integrations
    data:
      - name: Apache Airflow
        description: Orchestrate Airbyte syncs from Airflow DAGs.
      - name: dbt
        description: Transform data after Airbyte syncs with dbt models.
      - name: Snowflake
        description: Load data into Snowflake data warehouse.
      - name: BigQuery
        description: Sync data to Google BigQuery.
      - name: Redshift
        description: Load data into Amazon Redshift.
      - name: Databricks
        description: Ingest data into Databricks lakehouse.
      - name: Terraform
        description: Infrastructure-as-code support for Airbyte resources.
      - name: Kubernetes / Helm
        description: Deploy Airbyte on Kubernetes using official Helm charts.
  - url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/rules/airbyte-spectral-rules.yml
    type: SpectralRules
    title: Airbyte Spectral Rules
  - url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/capabilities/data-pipeline-management.yaml
    type: NaftikoCapability
    title: Data Pipeline Management
  - url: https://raw.githubusercontent.com/api-evangelist/airbyte/refs/heads/main/vocabulary/airbyte-vocabulary.yaml
    type: Vocabulary
    title: Airbyte Vocabulary
created: '2025-01-08'
modified: '2026-05-04'
position: Consumer
description: Airbyte is an open-source data integration platform that enables businesses to easily and efficiently move and consolidate their data from various sources into one centralized location. With Airbyte, organizations can seamlessly connect and synchronize data from sources such as databases, APIs, and other third-party applications, allowing for real-time insights and analysis. Airbyte offers both self-hosted and cloud-hosted options, with a catalog of hundreds of pre-built connectors.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
