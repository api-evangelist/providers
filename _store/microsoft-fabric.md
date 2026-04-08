---
aid: microsoft-fabric
url: https://raw.githubusercontent.com/api-evangelist/microsoft-fabric/refs/heads/main/apis.yml
apis:
- aid: microsoft-fabric:rest-api
  name: Microsoft Fabric REST API
  description: The Microsoft Fabric REST API provides programmatic access to the unified analytics platform. Developers can manage workspaces, lakehouses, warehouses, data pipelines, notebooks, and other Fabric items. The API supports data engineering, data science, real-time analytics, and business intelligence workloads in a single platform.
  humanURL: https://learn.microsoft.com/en-us/rest/api/fabric/
  baseURL: https://api.fabric.microsoft.com/v1/
  tags:
  - Data Analytics
  - Data Engineering
  - Data Platform
  - Lakehouse
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/fabric/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/fabric/get-started/
- aid: microsoft-fabric:sql-connection-api
  name: Microsoft Fabric SQL Connection
  description: Microsoft Fabric provides SQL connectivity to lakehouses and data warehouses through TDS endpoints. Developers can query Fabric data using standard SQL tools, JDBC/ODBC drivers, and client libraries, enabling integration with existing SQL-based applications and reporting tools.
  humanURL: https://learn.microsoft.com/en-us/fabric/data-warehouse/connectivity
  baseURL: https://{workspace}.datawarehouse.fabric.microsoft.com/
  tags:
  - Data Warehouse
  - Lakehouse
  - SQL
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/fabric/data-warehouse/connectivity
name: Microsoft Fabric
tags:
- Data Analytics
- Data Engineering
- Data Platform
- Lakehouse
- Microsoft
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Fabric is a unified analytics platform that brings together data engineering, data science, real-time analytics, and business intelligence. It provides REST APIs for managing workspaces, lakehouses, warehouses, data pipelines, notebooks, and other Fabric items.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

