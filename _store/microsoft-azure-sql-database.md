---
aid: microsoft-azure-sql-database
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-sql-database/refs/heads/main/apis.yml
name: Azure SQL Database
description: Azure SQL Database is a fully managed relational database service built on the SQL Server engine with built-in intelligence, high availability, and elastic scaling.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - SQL
  - Relational Database
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-sql-database:rest-api
    name: Azure SQL Database API
    description: The Azure SQL Database REST API provides management operations for SQL databases, elastic pools, servers, failover groups, and firewall rules. It supports database creation, scaling, backup management, auditing configuration, threat detection, and transparent data encryption through Azure Resource Manager.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/sql/
    baseURL: https://management.azure.com/
    tags:
      - Database
      - SQL
      - Elastic Pools
      - Failover Groups
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/sql/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-flows-app-scenarios
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-sql/database/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/azure-sql-database/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-sql-database
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
