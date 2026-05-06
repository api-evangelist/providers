---
aid: teradata
name: Teradata
description: Teradata provides enterprise analytics and data management solutions. The Teradata VantageCloud platform delivers connected multi-cloud data analytics with capabilities for data warehousing, advanced analytics, and machine learning at scale. Teradata offers REST APIs for managing QueryGrid data fabric connections, running SQL queries, and administering platform resources.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Cloud
  - Data Management
  - Data Warehousing
  - Database
  - Enterprise
  - Machine Learning
  - SQL
url: https://www.teradata.com
created: '2026-04-18'
modified: '2026-04-18'
specificationVersion: '0.19'
position: Consumer
access: 3rd-Party
apis:
  - aid: teradata:querygrid-manager-api
    name: Teradata QueryGrid Manager API
    description: REST API for centralized administration and monitoring of Teradata QueryGrid, the data fabric that enables seamless cross-system analytics. Manage data centers, systems, bridges, connectors, links, fabrics, networks, and node configurations. Perform diagnostic checks, software installations, and query monitoring across connected systems.
    humanURL: https://github.com/Teradata/querygrid-apidocs
    baseURL: https://querygrid.teradata.com/api/v1
    tags:
      - Configuration
      - Data Fabric
      - Diagnostics
      - Monitoring
      - QueryGrid
    properties:
      - type: Documentation
        url: https://github.com/Teradata/querygrid-apidocs
      - type: OpenAPI
        url: openapi/teradata-querygrid-manager-api.yaml
  - aid: teradata:query-service-api
    name: Teradata Query Service API
    description: REST API for executing SQL queries against Teradata Vantage systems. Provides HTTP-based access to run queries, retrieve results, and manage sessions for application integration and browser-based query tools.
    humanURL: https://docs.teradata.com
    baseURL: https://vantage.teradata.com/api/query/v1
    tags:
      - Query
      - REST
      - SQL
      - Vantage
    properties:
      - type: Documentation
        url: https://docs.teradata.com
      - type: OpenAPI
        url: openapi/teradata-query-service-api.yaml
common:
  - type: Portal
    url: https://developer.teradata.com
  - type: Documentation
    url: https://docs.teradata.com
  - type: GettingStarted
    url: https://quickstarts.teradata.com
  - type: GitHubOrganization
    url: https://github.com/Teradata
  - type: Support
    url: https://support.teradata.com
  - type: Blog
    url: https://www.teradata.com/blog
  - type: Training
    url: https://www.teradata.com/University
  - type: TermsOfService
    url: https://www.teradata.com/Legal/Terms-of-Use
  - type: PrivacyPolicy
    url: https://www.teradata.com/Legal/Privacy
  - type: SDK
    url: https://pypi.org/project/teradatasql/
    title: Python SQL Driver
  - type: SDK
    url: https://www.npmjs.com/package/teradatasql
    title: Node.js SQL Driver
  - type: SDK
    url: https://github.com/Teradata/r-driver
    title: R SQL Driver
  - type: SDK
    url: https://github.com/Teradata/teradatarustapi
    title: Rust API
  - type: SDK
    url: https://github.com/Teradata/gosql-driver
    title: Go SQL Driver
  - type: SDK
    url: https://github.com/Teradata/jdbc-driver
    title: JDBC Driver
  - type: CLI
    url: https://github.com/Teradata/teradata-vscode-sql-extension
    title: VS Code SQL Extension
  - type: Tools
    url: https://github.com/Teradata/teradata-mcp-server
    title: MCP Server
  - type: Tools
    url: https://github.com/Teradata/teradata-qg-mcp-server
    title: QueryGrid MCP Server
  - type: Integrations
    data:
      - name: dbt
        description: dbt adapter for Teradata Vantage enabling data transformations using dbt workflows.
      - name: Apache Airflow
        description: Airflow provider for orchestrating Teradata data pipeline workflows.
      - name: Dagster
        description: Dagster integration for Teradata data orchestration and observability.
      - name: Airbyte
        description: Airbyte connector for ELT data pipelines to and from Teradata.
      - name: Fivetran
        description: Fivetran destination connector for automated data loading into Teradata.
      - name: MuleSoft
        description: MuleSoft connector for integrating Teradata with enterprise application networks.
      - name: Dataiku
        description: Dataiku plugin for running analytics within the Teradata Vantage environment.
      - name: LangChain
        description: LangChain integration for using Teradata as a vector store and data source in AI applications.
      - name: Apache Iceberg
        description: Teradata support for Apache Iceberg open table format for lakehouse analytics.
  - type: Features
    data:
      - name: VantageCloud
        description: Cloud-native analytics platform available on AWS, Azure, and Google Cloud.
      - name: ClearScape Analytics
        description: Advanced analytics engine with machine learning, graph analytics, and AI capabilities built into Vantage.
      - name: QueryGrid
        description: Data fabric for multi-system analytics enabling queries across Teradata, Hadoop, Spark, and cloud object storage.
      - name: ModelOps
        description: Model lifecycle management for deploying, monitoring, and governing machine learning models.
      - name: AI Unlimited
        description: On-demand AI and ML engine for exploratory analytics without infrastructure management.
      - name: Open Table Formats
        description: Support for Apache Iceberg and open table formats for lakehouse analytics.
  - type: UseCases
    data:
      - name: Enterprise Data Warehousing
        description: Centralized data warehousing with petabyte-scale analytics for enterprise reporting and BI.
      - name: Advanced Analytics
        description: In-database machine learning, statistical analysis, and predictive modeling at scale.
      - name: Multi-Cloud Analytics
        description: Connected analytics across AWS, Azure, and Google Cloud with data fabric integration.
      - name: AI and ML Operations
        description: End-to-end machine learning model lifecycle management with ModelOps.
      - name: Real-Time Data Integration
        description: Real-time data ingestion and analytics with QueryGrid cross-system query federation.
  - type: SpectralRules
    url: rules/teradata-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/teradata-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-fabric-management.yaml
    title: Data Fabric Management
  - type: NaftikoCapability
    url: capabilities/query-and-analytics.yaml
    title: Query and Analytics
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
