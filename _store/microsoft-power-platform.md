---
aid: microsoft-power-platform
name: Microsoft Power Platform
description: Microsoft Power Platform is a suite of low-code development tools including Power Apps, Power Automate, Power BI, and Power Virtual Agents. It provides APIs for accessing Dataverse, managing environments, and integrating with external services through connectors.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Dataverse
  - Low-Code
  - Microsoft
  - Power Apps
  - Power Automate
  - Power BI
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-platform/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
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
        type: GettingStarted
    description: Power Platform Connectors provide pre-built integrations with hundreds of external services and enable developers to create custom connectors using OpenAPI definitions. Connectors abstract API authentication and data access, making external services available to Power Apps, Power Automate, and Logic Apps.
common:
  - type: Portal
    url: https://make.powerapps.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/
  - type: Pricing
    url: https://powerapps.microsoft.com/en-us/pricing/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
  - type: Blog
    url: https://powerplatform.microsoft.com/en-us/blog/
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: StatusPage
    url: https://status.powerplatform.microsoft.com/
  - type: Features
    url: https://powerplatform.microsoft.com/en-us/what-is-power-platform/
  - type: UseCases
    url: https://powerplatform.microsoft.com/en-us/customer-stories/
  - type: Integrations
    url: https://learn.microsoft.com/en-us/connectors/overview
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
