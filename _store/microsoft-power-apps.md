---
aid: microsoft-power-apps
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-apps/refs/heads/main/apis.yml
apis:
- name: Power Apps API
  description: Core API for managing Power Apps applications, including creating, updating, and deleting apps.
  image: https://powerplatform.microsoft.com/images/power-apps-icon.png
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  baseURL: https://api.powerapps.com
  tags:
  - Applications
  - Development
  - Low-Code
  - Power Platform
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference
  - type: OpenAPI
    url: https://docs.microsoft.com/en-us/connectors/powerappsforappmakers/
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/authenticate
  - type: Rate Limits
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/api-limits
  - type: REST API Reference
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/powerapps/apps
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
- name: Dataverse API (Common Data Service)
  description: RESTful API for interacting with Microsoft Dataverse (formerly Common Data Service) for data storage and management.
  image: https://powerplatform.microsoft.com/images/dataverse-icon.png
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  baseURL: https://[organization].api.crm.dynamics.com/api/data/v9.2
  tags:
  - CRM
  - Data Platform
  - Database
  - REST API
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: OpenAPI
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/openapi
  - type: OData
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api
  - type: Authentication
    url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
  - type: Web API Reference
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
  - type: Web API Operations
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api
  - type: Web API Types and Operations
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
  - type: Custom APIs
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api
  - type: OpenAPI Artifact
    url: openapi/microsoft-power-apps-dataverse-web-api-openapi.yml
  - type: JSON Schema Artifact
    url: json-schema/microsoft-power-apps-entity-schema.json
  - type: JSON-LD Context Artifact
    url: json-ld/microsoft-power-apps-context.jsonld
  - type: Security Roles
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/security-roles
  - type: Training
    url: https://learn.microsoft.com/en-us/training/modules/dataverse-web-api/
- name: Power Apps Management API
  description: API for administrative tasks including environment management, app sharing, and user permissions.
  image: https://powerplatform.microsoft.com/images/admin-icon.png
  humanURL: https://docs.microsoft.com/en-us/power-platform/admin/programmability-admin-center
  baseURL: https://api.bap.microsoft.com
  tags:
  - Administration
  - Environments
  - Governance
  - Management
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-platform/admin/programmability-admin-center
  - type: PowerShell
    url: https://docs.microsoft.com/en-us/power-platform/admin/powershell-getting-started
  - type: CLI
    url: https://docs.microsoft.com/en-us/power-platform/developer/cli/introduction
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
  - type: Environment Management
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/environmentmanagement/environment-management-settings
  - type: Governance
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/environmentmanagement/environment-managed-governance/enable-managed-environment
- name: Power Apps Connectors API
  description: API for working with custom and standard connectors to integrate external services and data sources.
  image: https://powerplatform.microsoft.com/images/connectors-icon.png
  humanURL: https://docs.microsoft.com/en-us/connectors/custom-connectors/
  baseURL: https://api.powerapps.com/providers/Microsoft.PowerApps
  tags:
  - Connectors
  - Custom Connectors
  - Integration
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/connectors/custom-connectors/create-web-api-connector
  - type: Connector Reference
    url: https://docs.microsoft.com/en-us/connectors/connector-reference/
  - type: Custom Connectors
    url: https://docs.microsoft.com/en-us/connectors/custom-connectors/
  - type: List Connectors API
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/connectivity/connectors/list-connectors
- name: Power Apps Canvas Apps API
  description: API specific to Canvas Apps for creating pixel-perfect user interfaces with drag-and-drop functionality.
  image: https://powerplatform.microsoft.com/images/canvas-apps-icon.png
  humanURL: https://docs.microsoft.com/en-us/power-apps/maker/canvas-apps/
  baseURL: https://api.powerapps.com
  tags:
  - Canvas Apps
  - Low-Code
  - Mobile
  - UI
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/maker/canvas-apps/dev-enterprise-intro
  - type: Formula Reference
    url: https://docs.microsoft.com/en-us/power-platform/power-fx/formula-reference
  - type: App Lifecycle
    url: https://docs.microsoft.com/en-us/power-apps/maker/canvas-apps/application-lifecycle-management
  - type: Power Fx Overview
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/overview
  - type: Power Fx Formula Reference
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-canvas-apps
- name: Power Apps Model-driven Apps API
  description: API for Model-driven Apps that automatically generate UI based on data model and business logic.
  image: https://powerplatform.microsoft.com/images/model-driven-icon.png
  humanURL: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/
  baseURL: https://[organization].crm.dynamics.com
  tags:
  - Business Logic
  - Forms
  - Model-Driven Apps
  - Views
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/overview
  - type: Client API
    url: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference
  - type: Customization
    url: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/customize-entity-forms
  - type: Power Fx Formula Reference
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-model-driven-apps
- name: Power Apps Component Framework (PCF) API
  description: Framework API for professional developers to create reusable code components for model-driven and canvas apps using TypeScript and web technologies.
  image: https://powerplatform.microsoft.com/images/power-apps-icon.png
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview
  baseURL: https://api.powerapps.com
  tags:
  - Code Components
  - Component Framework
  - Custom Controls
  - PCF
  - TypeScript
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript
  - type: Create and Build Components
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf
  - type: Agent APIs
    url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/bring-intelligence-using-agent-apis
- name: Power Platform REST API
  description: Unified RESTful API for Power Platform administration including environment management, governance, licensing, app management, and capacity reporting.
  image: https://powerplatform.microsoft.com/images/power-apps-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/power-platform/
  baseURL: https://api.powerplatform.com
  tags:
  - Administration
  - Environments
  - Governance
  - Licensing
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
  - type: App Management
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/appmanagement/applications
  - type: Environment Management
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/environmentmanagement/environment-management-settings
  - type: Connectors
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/connectivity/connectors/list-connectors
- name: Power Pages Web API
  description: Web API for Power Pages (formerly Power Apps Portals) enabling CRUD operations on Dataverse tables from external-facing portal web pages.
  image: https://powerplatform.microsoft.com/images/power-apps-icon.png
  humanURL: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
  baseURL: https://[site-url]/_api
  tags:
  - CRUD
  - External Users
  - Portals
  - Power Pages
  - Web API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
  - type: Read Operations
    url: https://learn.microsoft.com/en-us/power-pages/configure/read-operations
  - type: Write Operations
    url: https://learn.microsoft.com/en-us/power-pages/configure/write-update-delete-operations
  - type: Tutorial
    url: https://learn.microsoft.com/en-us/power-apps/maker/portals/webapi-tutorial
  - type: Power Fx Formula Reference
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-power-pages
- name: Dataverse Organization Service SDK
  description: .NET SDK providing strongly-typed access to Microsoft Dataverse through the IOrganizationService interface for server-side development and plugins.
  image: https://powerplatform.microsoft.com/images/dataverse-icon.png
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/overview
  baseURL: https://[organization].api.crm.dynamics.com
  tags:
  - .NET
  - Organization Service
  - Plugins
  - SDK
  - Server-Side
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/overview
  - type: IOrganizationService Interface
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/iorganizationservice-interface
  - type: SDK Messages
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/use-messages
  - type: ServiceClient Reference
    url: https://learn.microsoft.com/en-us/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient
  - type: Dataverse Developer Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/
- name: Power Apps Code Apps API
  description: API and SDK for building code-first Power Apps using popular frameworks like React and Vue, developed in any code-first IDE and deployed to Power Apps.
  image: https://powerplatform.microsoft.com/images/power-apps-icon.png
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview
  baseURL: https://api.powerapps.com
  tags:
  - Code Apps
  - Code-First
  - Pro Developer
  - React
  - Vue
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/
  - type: Overview
    url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview
  - type: Architecture
    url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/architecture
  - type: ALM
    url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/alm
  - type: Content Security Policy
    url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy
name: Microsoft Power Apps
tags:
- Business Applications
- Cloud
- Enterprise
- Low-Code
- Microsoft
- No-Code
- Power Platform
- SaaS
type: Contract
image: https://powerplatform.microsoft.com/images/power-apps-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Microsoft Power Apps platform enabling low-code application development, automation, and data connectivity.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

