---
aid: azure-synapse
url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/apis.yml
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
name: Azure Synapse Analytics
tags:
- Analytics
- Apache Spark
- Big Data
- Data Warehouse
- ETL
- SQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Synapse Analytics is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. It brings together SQL technologies, Spark technologies, Data Explorer, and integrated pipelines for data integration and ETL/ELT.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

