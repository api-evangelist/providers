---
aid: microsoft-fabric
name: Microsoft Fabric
description: Microsoft Fabric is a unified analytics platform that brings together data engineering, data science, real-time analytics, and business intelligence. It provides REST APIs for managing workspaces, lakehouses, warehouses, data pipelines, notebooks, and other Fabric items.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Analytics
  - Data Engineering
  - Data Platform
  - Lakehouse
  - Microsoft
url: https://raw.githubusercontent.com/api-evangelist/microsoft-fabric/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
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
common:
  - type: Portal
    url: https://app.fabric.microsoft.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-fabric
  - type: Documentation
    url: https://learn.microsoft.com/en-us/fabric/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/fabric/get-started/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/fabric/security/permission-model
  - type: Blog
    url: https://blog.fabric.microsoft.com/
  - type: Community
    url: https://community.fabric.microsoft.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Status
    url: https://status.fabric.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
