---
name: Microsoft Power Apps
description: Microsoft Power Apps is a suite of apps, services, and connectors, as well as a data platform, that provides a rapid development environment to build custom apps for your business needs.
image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
url: https://powerapps.microsoft.com/
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
tags:
  - App Development
  - Business Applications
  - Cloud Platform
  - Low-Code
  - Microsoft
  - No-Code
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
      - type: Quickstart
        url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/quick-start-console-app-csharp
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
      - type: SDK
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/overview
      - type: DeveloperPortal
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
      - type: SDK
        url: https://docs.microsoft.com/en-us/powershell/module/microsoft.powerapps.administration.powershell/
      - type: GettingStarted
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
      - type: CodeExamples
        url: https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework
      - type: Tutorials
        url: https://docs.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf
      - type: Documentation
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
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-extensibility-overview
      - type: Documentation
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
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/walkthrough-write-your-first-client-script
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/client-scripting
      - type: Documentation
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
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/connectors/custom-connectors/define-blank
      - type: Documentation
        url: https://learn.microsoft.com/en-us/connectors/custom-connectors/use-custom-connector-powerapps
      - type: Documentation
        url: https://learn.microsoft.com/en-us/connectors/connector-reference/
common:
  - type: Portal
    url: https://make.powerapps.com
  - type: DeveloperPortal
    url: https://powerapps.microsoft.com/en-us/developers/
  - type: Support
    url: https://powerusers.microsoft.com/
  - type: Blog
    url: https://powerapps.microsoft.com/en-us/blog/
  - type: Pricing
    url: https://powerapps.microsoft.com/en-us/pricing/
  - type: Support
    url: https://powerapps.microsoft.com/en-us/support/
  - type: Training
    url: https://docs.microsoft.com/en-us/learn/powerplatform/power-apps
  - type: GitHubOrganization
    url: https://github.com/microsoft/PowerApps-Samples
  - type: StatusPage
    url: https://status.powerplatform.microsoft.com/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/power-platform/developer/get-started
  - type: Resources
    url: https://learn.microsoft.com/en-us/power-platform/alm/overview-alm
  - type: CLI
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/powerapps-cli
  - type: Resources
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/developer-tools
  - type: Resources
    url: https://learn.microsoft.com/en-us/power-platform/alm/devops-github-actions
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authentication
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-whats-new-changed
  - type: Resources
    url: https://learn.microsoft.com/en-us/connectors/connector-reference/
  - type: Training
    url: https://learn.microsoft.com/en-us/training/powerplatform/
  - type: Features
    data:
      - Low-code and no-code app development
      - Microsoft Dataverse data platform
      - Power Apps Component Framework (PCF)
      - Model-driven and canvas app types
      - Custom connectors for REST and SOAP APIs
      - Power Platform unified administration API
      - Client-side scripting with Xrm object model
      - AI Builder integration for intelligent apps
  - type: UseCases
    data:
      - Custom business application development
      - Data-driven enterprise app creation
      - Legacy system modernization
      - Citizen developer enablement
      - Mobile workforce applications
      - Process automation with Power Automate integration
  - type: Integrations
    data:
      - Microsoft 365
      - Microsoft Teams
      - Microsoft Azure
      - Power Automate
      - Power BI
      - Dynamics 365
      - SharePoint
      - SQL Server
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
