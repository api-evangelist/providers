---
aid: power-query
url: https://raw.githubusercontent.com/api-evangelist/power-query/refs/heads/main/apis.yml
apis:
- name: Power Query REST API
  description: REST API for executing Power Query mashups and managing data transformations.
  baseURL: https://api.powerquery.microsoft.com/v1.0
  humanURL: https://docs.microsoft.com/en-us/power-query/power-query-rest-api
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-query/power-query-rest-api
  - type: OpenAPI
    url: https://api.powerquery.microsoft.com/swagger/v1/swagger.json
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-query/authentication
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query
  contact:
  - type: Support
    url: https://powerbi.microsoft.com/support/
  tags:
  - Data Query
  - Mashup Engine
  - REST API
- name: Power Query M Formula Language
  description: API and language reference for the M formula language used in Power Query.
  baseURL: https://docs.microsoft.com/powerquery-m/
  humanURL: https://docs.microsoft.com/en-us/powerquery-m/
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/powerquery-m/
  - type: Language Reference
    url: https://docs.microsoft.com/en-us/powerquery-m/power-query-m-language-specification
  - type: Function Reference
    url: https://docs.microsoft.com/en-us/powerquery-m/power-query-m-function-reference
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/powerquery-m/quick-tour-of-the-power-query-m-formula-language
  - type: Type System
    url: https://learn.microsoft.com/en-us/powerquery-m/power-query-m-type-system
  tags:
  - Formula Language
  - Functions
  - M Language
- name: Power Query Connectors API
  description: API for building and managing custom data connectors for Power Query.
  baseURL: https://github.com/Microsoft/DataConnectors
  humanURL: https://docs.microsoft.com/en-us/power-query/connectors/
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-query/installingsdk
  - type: SDK
    url: https://aka.ms/powerquerysdk
  - type: GitHub Repository
    url: https://github.com/Microsoft/DataConnectors
  - type: Connector Reference
    url: https://docs.microsoft.com/en-us/power-query/connectors/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-query/handling-authentication
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-query/creating-first-connector
  - type: Certification
    url: https://learn.microsoft.com/en-us/power-query/connector-certification
  tags:
  - Connectors
  - Data Sources
  - SDK
- name: Power Query Dataflows API
  description: API for managing and executing Power Query dataflows in Power Platform.
  baseURL: https://api.powerbi.com/v1.0/myorg/groups/{groupId}/dataflows
  humanURL: https://docs.microsoft.com/en-us/power-query/dataflows/
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service
  - type: REST API Reference
    url: https://docs.microsoft.com/en-us/rest/api/power-bi/dataflows
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service
  contact:
  - type: Support
    url: https://powerbi.microsoft.com/support/
  tags:
  - Dataflows
  - Power Platform
  - Self-Service ETL
- name: Power Query SDK
  description: Development toolkit for building custom Power Query connectors using Visual Studio Code, including project scaffolding, testing, and packaging of .mez connector files.
  baseURL: https://learn.microsoft.com/en-us/power-query/power-query-sdk-vs-code
  humanURL: https://learn.microsoft.com/en-us/power-query/install-sdk
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-query/power-query-sdk-vs-code
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-query/install-sdk
  - type: VS Code Extension
    url: https://marketplace.visualstudio.com/items?itemName=PowerQuery.vscode-powerquery-sdk
  - type: GitHub Repository
    url: https://github.com/microsoft/vscode-powerquery-sdk
  - type: Test Framework
    url: https://learn.microsoft.com/en-us/power-query/sdk-testframework/1-set-up
  tags:
  - Connector Development
  - SDK
  - Tooling
  - VS Code
- name: Power Query Language Services
  description: Libraries providing intellisense, parsing, formatting, and other language services for the Power Query M language, used in VS Code extensions and other tooling.
  baseURL: https://github.com/microsoft/powerquery-language-services
  humanURL: https://github.com/microsoft/powerquery-language-services
  properties:
  - type: Documentation
    url: https://github.com/microsoft/powerquery-language-services
  - type: GitHub Repository
    url: https://github.com/microsoft/powerquery-language-services
  - type: Parser
    url: https://github.com/microsoft/powerquery-parser
  - type: Formatter
    url: https://github.com/microsoft/powerquery-formatter
  - type: VS Code Extension
    url: https://marketplace.visualstudio.com/items?itemName=PowerQuery.vscode-powerquery
  tags:
  - Formatter
  - Intellisense
  - Language Services
  - Parser
  - Tooling
- name: Fabric Power Query Programmatic API
  description: REST API for programmatically executing Power Query M transformations in Microsoft Fabric, enabling integration with Spark notebooks, pipelines, and external applications.
  baseURL: https://learn.microsoft.com/en-us/fabric/data-factory/
  humanURL: https://blog.fabric.microsoft.com/en-US/blog/execute-power-query-programmatically-in-microsoft-fabric/
  properties:
  - type: Documentation
    url: https://blog.fabric.microsoft.com/en-US/blog/execute-power-query-programmatically-in-microsoft-fabric/
  - type: Pipeline REST API
    url: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-rest-api
  - type: Pipeline REST API Capabilities
    url: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-rest-api-capabilities
  tags:
  - Microsoft Fabric
  - Pipelines
  - Programmatic Execution
  - REST API
  - Spark
name: Power Query
tags:
- Business Intelligence
- Data Integration
- Data Transformation
- ETL
- Microsoft
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Power Query is a data transformation and mashup engine used across Microsoft products including Excel, Power BI, and Azure. This API collection provides programmatic access to Power Query functionality for data connectivity, transformation, and integration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

