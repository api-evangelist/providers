---
aid: azure-synapse
name: Azure Synapse Analytics
description: Azure Synapse Analytics is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. It brings together SQL technologies, Spark technologies, Data Explorer, and integrated pipelines for data integration and ETL/ELT.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Apache Spark
  - Big Data
  - Data Warehouse
  - ETL
  - SQL
url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-synapse:azure-synapse-rest-api
    name: Azure Synapse REST API
    description: REST API for managing Azure Synapse Analytics workspaces, SQL pools, Spark pools, and pipelines.
    humanURL: https://docs.microsoft.com/en-us/rest/api/synapse/
    baseURL: https://management.azure.com
    tags:
      - Management
      - REST API
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/synapse/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/synapse.json
      - type: Authentication
        url: https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
  - aid: azure-synapse:azure-synapse-pipeline-api
    name: Azure Synapse Pipeline API
    description: API for creating and managing data integration pipelines.
    humanURL: https://docs.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Integration
      - ETL
      - Pipeline
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/openapi/azure-synapse-openapi.yaml
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://docs.microsoft.com/en-us/azure/synapse-analytics/
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/bg-p/AzureSynapseAnalyticsBlog
  - type: GitHub Organization
    url: https://github.com/Azure/azure-synapse-analytics
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/rules/azure-synapse-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/vocabulary/azure-synapse-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/json-ld/azure-synapse-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/capabilities/azure-synapse-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/capabilities/shared/azure-synapse.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
