---
aid: power-query
name: Power Query
description: Power Query is a data transformation and mashup engine used across Microsoft products including Excel, Power BI, and Azure. This API collection provides programmatic access to Power Query functionality for data connectivity, transformation, and integration using the M formula language and connector SDK.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/power-query/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Business Intelligence
  - Data Integration
  - Data Transformation
  - ETL
  - Microsoft
apis:
  - aid: power-query:rest-api
    name: Power Query REST API
    description: REST API for executing Power Query mashups and managing data transformations programmatically.
    humanURL: https://docs.microsoft.com/en-us/power-query/power-query-rest-api
    baseURL: https://api.powerquery.microsoft.com/v1.0
    tags:
      - Data Query
      - Mashup Engine
      - REST
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-query/power-query-rest-api
      - type: Authentication
        url: https://docs.microsoft.com/en-us/power-query/authentication
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query
  - aid: power-query:m-language
    name: Power Query M Formula Language
    description: API and language reference for the M formula language used in Power Query for data transformation expressions and custom functions.
    humanURL: https://docs.microsoft.com/en-us/powerquery-m/
    baseURL: https://docs.microsoft.com/powerquery-m/
    tags:
      - Formula Language
      - Functions
      - M Language
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/powerquery-m/
      - type: APIReference
        url: https://docs.microsoft.com/en-us/powerquery-m/power-query-m-function-reference
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/powerquery-m/quick-tour-of-the-power-query-m-formula-language
  - aid: power-query:connectors-api
    name: Power Query Connectors API
    description: API for building and managing custom data connectors for Power Query using the M language and Connector SDK.
    humanURL: https://docs.microsoft.com/en-us/power-query/connectors/
    baseURL: https://github.com/Microsoft/DataConnectors
    tags:
      - Connectors
      - Data Sources
      - SDK
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-query/installingsdk
      - type: SDK
        url: https://aka.ms/powerquerysdk
      - type: GitHubRepository
        url: https://github.com/Microsoft/DataConnectors
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-query/creating-first-connector
  - aid: power-query:dataflows-api
    name: Power Query Dataflows API
    description: API for managing and executing Power Query dataflows in Power Platform and Power BI for self-service ETL workflows.
    humanURL: https://docs.microsoft.com/en-us/power-query/dataflows/
    baseURL: https://api.powerbi.com/v1.0/myorg/groups/{groupId}/dataflows
    tags:
      - Dataflows
      - Power Platform
      - Self-Service ETL
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service
      - type: APIReference
        url: https://docs.microsoft.com/en-us/rest/api/power-bi/dataflows
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service
  - aid: power-query:sdk
    name: Power Query SDK
    description: Development toolkit for building custom Power Query connectors using Visual Studio Code, including project scaffolding, testing, and packaging of .mez connector files.
    humanURL: https://learn.microsoft.com/en-us/power-query/install-sdk
    baseURL: https://learn.microsoft.com/en-us/power-query/power-query-sdk-vs-code
    tags:
      - Connector Development
      - SDK
      - Tooling
      - VS Code
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-query/power-query-sdk-vs-code
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-query/install-sdk
      - type: GitHubRepository
        url: https://github.com/microsoft/vscode-powerquery-sdk
  - aid: power-query:fabric-api
    name: Fabric Power Query Programmatic API
    description: REST API for programmatically executing Power Query M transformations in Microsoft Fabric, enabling integration with Spark notebooks, pipelines, and external applications.
    humanURL: https://blog.fabric.microsoft.com/en-US/blog/execute-power-query-programmatically-in-microsoft-fabric/
    baseURL: https://learn.microsoft.com/en-us/fabric/data-factory/
    tags:
      - Microsoft Fabric
      - Pipelines
      - Programmatic Execution
      - REST
    properties:
      - type: Documentation
        url: https://blog.fabric.microsoft.com/en-US/blog/execute-power-query-programmatically-in-microsoft-fabric/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-rest-api
common:
  - type: Portal
    url: https://app.powerbi.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-query/
  - type: GettingStarted
    url: https://www.microsoft.com/en-us/power-platform/products/power-bi/getting-started-with-power-bi
  - type: Blog
    url: https://powerbi.microsoft.com/blog/
  - type: GitHubOrganization
    url: https://github.com/MicrosoftDocs/powerquery-docs
  - type: Support
    url: https://powerbi.microsoft.com/en-us/support/
  - type: Pricing
    url: https://powerbi.microsoft.com/pricing/
  - type: StatusPage
    url: https://support.fabric.microsoft.com/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/servicesagreement/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SignUp
    url: https://www.microsoft.com/en-us/power-platform/products/power-bi/landing/free-account
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/powerquery
  - type: YouTube
    url: https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-change-log
  - type: Features
    data:
      - name: Data Transformation Engine
        description: Powerful M formula language for complex data transformations including filtering, pivoting, merging, and custom functions.
      - name: Custom Connector Development
        description: Build custom data connectors using the Power Query SDK for connecting to any data source.
      - name: Self-Service ETL
        description: Dataflows provide self-service ETL capabilities for business users without IT dependency.
      - name: 300+ Built-In Connectors
        description: Pre-built connectors for databases, cloud services, files, and web APIs.
      - name: Incremental Refresh
        description: Efficient data loading with incremental refresh policies for large datasets.
      - name: Microsoft Fabric Integration
        description: Execute Power Query transformations programmatically in Microsoft Fabric pipelines.
  - type: UseCases
    data:
      - name: Data Preparation
        description: Clean, transform, and shape data from multiple sources for analytics and reporting.
      - name: Custom Data Connectors
        description: Build reusable connectors for proprietary or specialized data sources.
      - name: Automated Data Pipelines
        description: Create scheduled dataflows for automated data refresh and transformation workflows.
      - name: Cross-Platform Data Integration
        description: Integrate data across Power BI, Excel, Azure Data Factory, and Microsoft Fabric.
      - name: Data Quality Management
        description: Implement data quality rules and transformations for consistent enterprise data.
  - type: Integrations
    data:
      - name: Power BI
        description: Native integration with Power BI for data preparation and visualization workflows.
      - name: Microsoft Excel
        description: Built-in Power Query editor in Excel for spreadsheet-based data transformation.
      - name: Azure Data Factory
        description: Mapping data flows using Power Query transformations in Azure Data Factory.
      - name: Microsoft Fabric
        description: Programmatic execution of Power Query in Fabric notebooks and pipelines.
      - name: SQL Server
        description: Direct connectivity and query folding optimization for SQL Server databases.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
