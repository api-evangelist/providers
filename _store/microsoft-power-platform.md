---
aid: microsoft-power-platform
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-platform/refs/heads/main/apis.yml
apis:
- aid: microsoft-power-platform:dataverse-api
  name: Microsoft Dataverse Web API
  tags:
  - Data Platform
  - Dataverse
  - OData
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  properties:
  - url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
    type: Documentation
  description: The Microsoft Dataverse Web API provides OData v4 RESTful access to the Dataverse data platform that underpins Power Platform. Developers can perform CRUD operations on tables, execute actions and functions, manage metadata, and query data using standard OData conventions.
- aid: microsoft-power-platform:admin-api
  name: Power Platform Admin API
  tags:
  - Administration
  - Environments
  - Governance
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.bap.microsoft.com/
  humanURL: https://learn.microsoft.com/en-us/power-platform/admin/programmability-extensibility-overview
  properties:
  - url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-extensibility-overview
    type: Documentation
  description: The Power Platform Admin API enables programmatic management of Power Platform environments, connectors, data loss prevention policies, and tenant settings. Administrators can create and manage environments, configure security roles, and enforce governance policies across the organization.
- aid: microsoft-power-platform:connectors-api
  name: Power Platform Connectors
  tags:
  - Connectors
  - Custom Connectors
  - Integration
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/connectors/overview
  properties:
  - url: https://learn.microsoft.com/en-us/connectors/overview
    type: Documentation
  - url: https://learn.microsoft.com/en-us/connectors/custom-connectors/
    type: Getting Started
  description: Power Platform Connectors provide pre-built integrations with hundreds of external services and enable developers to create custom connectors using OpenAPI definitions. Connectors abstract API authentication and data access, making external services available to Power Apps, Power Automate, and Logic Apps.
name: Microsoft Power Platform
tags:
- Dataverse
- Low-Code
- Microsoft
- Power Apps
- Power Automate
- Power BI
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Power Platform is a suite of low-code development tools including Power Apps, Power Automate, Power BI, and Power Virtual Agents. It provides APIs for accessing Dataverse, managing environments, and integrating with external services through connectors.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

