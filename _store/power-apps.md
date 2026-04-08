---
aid: power-apps
url: https://raw.githubusercontent.com/api-evangelist/power-apps/refs/heads/main/apis.yml
apis:
- name: Power Apps REST API
  description: The Power Apps REST API provides a unified endpoint to work with environments, apps, and related resources.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  baseURL: https://api.powerapps.com
  tags:
  - Apps
  - Connections
  - Environments
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: OpenAPI
    url: https://learn.microsoft.com/en-us/connectors/powerappsforappmakers/
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
- name: Microsoft Dataverse Web API
  description: The Web API for Dataverse provides a development experience that can be used across a wide variety of programming languages, platforms, and devices.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - CRUD Operations
  - Data Platform
  - Dataverse
  - OData
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: OpenAPI
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/openapi
  - type: Quick Start
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/quick-start-console-app-csharp
  - type: API Reference
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
  - type: Types and Operations
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
  - type: SDK
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/overview
  - type: Developer Portal
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/
- name: Power Apps Management API
  description: REST API for managing Power Apps environments, apps, flows, and connectors.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://docs.microsoft.com/en-us/powershell/module/microsoft.powerapps.administration.powershell/
  baseURL: https://api.bap.microsoft.com
  tags:
  - Administration
  - Governance
  - Management
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-platform/admin/programmability-authentication
  - type: PowerShell Module
    url: https://docs.microsoft.com/en-us/powershell/module/microsoft.powerapps.administration.powershell/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
- name: Power Apps Component Framework API
  description: APIs for building custom components using the Power Apps Component Framework (PCF).
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/component-framework/overview
  baseURL: https://pcf.tools
  tags:
  - Components
  - Custom Controls
  - PCF
  - UI Framework
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/component-framework/reference/
  - type: Samples
    url: https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework
  - type: Tutorial
    url: https://docs.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf
  - type: Canvas Apps Support
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps
- name: Microsoft Power Platform API
  description: The Power Platform API provides a unified REST endpoint at api.powerplatform.com for managing environments, licensing, app management, and tenant-level governance across the entire Power Platform.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://learn.microsoft.com/en-us/rest/api/power-platform/
  baseURL: https://api.powerplatform.com
  tags:
  - App Management
  - Environments
  - Governance
  - Licensing
  - Platform API
  - Tenant Administration
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
  - type: Programmability Overview
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-extensibility-overview
  - type: Connector
    url: https://learn.microsoft.com/en-us/connectors/powerplatformadminv2/
  - type: SDK
    url: https://www.nuget.org/packages/Microsoft.PowerPlatform.Management
- name: Model-Driven Apps Client API
  description: Client API reference for model-driven apps providing JavaScript libraries for form scripting, UI manipulation, data access, and the Xrm object model including Xrm.WebApi for data operations.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference
  baseURL: https://[org].api.crm.dynamics.com
  tags:
  - Client API
  - Form Scripting
  - JavaScript
  - Model-Driven Apps
  - Xrm Object Model
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/walkthrough-write-your-first-client-script
  - type: Client Scripting
    url: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/client-scripting
  - type: Web API (Client-Side)
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/get-started-web-api-client-side-javascript
- name: Custom Connectors API
  description: Custom connectors allow you to create wrappers around REST or SOAP APIs for use in Power Apps, Power Automate, Logic Apps, and Copilot Studio, enabling integration with services not available as prebuilt connectors.
  image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
  humanURL: https://learn.microsoft.com/en-us/connectors/custom-connectors/
  baseURL: https://[environment].api.powerapps.com
  tags:
  - Connectors
  - Custom Connectors
  - Integration
  - OpenAPI
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/
  - type: Tutorial
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/define-blank
  - type: Use in Power Apps
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/use-custom-connector-powerapps
  - type: Connector Reference
    url: https://learn.microsoft.com/en-us/connectors/connector-reference/
name: Microsoft Power Apps
tags:
- App Development
- Business Applications
- Cloud Platform
- Low-Code
- Microsoft
- No-Code
type: Contract
image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Power Apps is a suite of apps, services, and connectors, as well as a data platform, that provides a rapid development environment to build custom apps for your business needs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

