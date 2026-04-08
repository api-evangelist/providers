---
aid: power-platform
url: https://raw.githubusercontent.com/api-evangelist/power-platform/refs/heads/main/apis.yml
apis:
- name: Power Apps API
  description: REST API for creating, managing, and deploying Power Apps applications including canvas apps and model-driven apps.
  image: https://powerplatform.microsoft.com/images/powerapps-logo.png
  baseURL: https://api.powerapps.com
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  tags:
  - Applications
  - Canvas Apps
  - Model-Driven Apps
  - Power Apps
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: OpenAPI
    url: https://api.powerapps.com/openapi/v1
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits
  - type: Pricing
    url: https://powerapps.microsoft.com/pricing/
  - type: Power Platform API Reference
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/powerapps/apps
  contact:
  - type: Support
    url: https://powerapps.microsoft.com/support/
- name: Dataverse API (Common Data Service)
  description: OData v4.0 compliant Web API for Microsoft Dataverse, providing RESTful data storage, business logic, and entity management capabilities across the Power Platform.
  image: https://powerplatform.microsoft.com/images/dataverse-logo.png
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  tags:
  - CDS
  - Data Platform
  - Database
  - Dataverse
  - OData
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
  - type: OData
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/authenticate-web-api
  - type: SDKs
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/developer-tools
  - type: Web API Service Documents
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-service-documents
  - type: Operations
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api
  contact:
  - type: Support
    url: https://powerapps.microsoft.com/support/
- name: Power Automate API
  description: API for creating, managing, and running automated cloud flows and desktop flows. Cloud flows are stored in Dataverse and can be managed via the Dataverse Web API.
  image: https://powerplatform.microsoft.com/images/powerautomate-logo.png
  baseURL: https://api.flow.microsoft.com
  humanURL: https://learn.microsoft.com/en-us/power-automate/web-api
  tags:
  - Automation
  - Desktop Flows
  - Flow
  - Power Automate
  - RPA
  - Workflow
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-automate/web-api
  - type: OpenAPI
    url: https://api.flow.microsoft.com/openapi/v1
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-automate/web-api
  - type: Connectors
    url: https://learn.microsoft.com/en-us/connectors/
  - type: Pricing
    url: https://powerautomate.microsoft.com/pricing/
  - type: Cloud Flows Code Management
    url: https://learn.microsoft.com/en-us/power-automate/manage-flows-with-code
  - type: Desktop Flow APIs
    url: https://learn.microsoft.com/en-us/power-automate/developer/desktop-flow-public-apis
  - type: Power Platform API Reference
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/powerautomate/flow-runs/list-flow-runs
  contact:
  - type: Support
    url: https://powerautomate.microsoft.com/support/
- name: Power BI REST API
  description: REST API for embedding, managing, and interacting with Power BI reports, datasets, dashboards, and workspaces for embedded analytics and automation.
  image: https://powerplatform.microsoft.com/images/powerbi-logo.png
  baseURL: https://api.powerbi.com
  humanURL: https://learn.microsoft.com/en-us/rest/api/power-bi/
  tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Embedded Analytics
  - Power BI
  - Reporting
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/power-bi/
  - type: OpenAPI
    url: https://api.powerbi.com/v1.0/myorg/swagger.json
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-tokens
  - type: SDKs
    url: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/
  - type: Embedding
    url: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embedding
  - type: Pricing
    url: https://powerbi.microsoft.com/pricing/
  - type: Developer Documentation
    url: https://learn.microsoft.com/en-us/power-bi/developer/
  - type: Admin API
    url: https://learn.microsoft.com/en-us/rest/api/power-bi/admin
  - type: Report Server API
    url: https://learn.microsoft.com/en-us/rest/api/power-bi-report/
  contact:
  - type: Support
    url: https://powerbi.microsoft.com/support/
- name: Microsoft Copilot Studio API (formerly Power Virtual Agents)
  description: API for building, managing, and deploying AI agents and conversational chatbots. Power Virtual Agents has been rebranded to Microsoft Copilot Studio with expanded AI agent capabilities.
  image: https://powerplatform.microsoft.com/images/pva-logo.png
  baseURL: https://api.powerva.microsoft.com
  humanURL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
  tags:
  - AI Agents
  - Chatbots
  - Conversational AI
  - Copilot Studio
  - Power Virtual Agents
  - Virtual Agents
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
  - type: Authentication
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/configuration-end-user-authentication
  - type: Agent Quarantine API
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-api-quarantine
  - type: Agent Delete API
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-api-delete
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio#pricing
  - type: Web App
    url: https://copilotstudio.microsoft.com
  contact:
  - type: Support
    url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
- name: Power Platform Admin API
  description: API for administrative operations across Power Platform environments including environment management, governance, capacity, and licensing via the BAP (Business Application Platform) endpoint.
  image: https://powerplatform.microsoft.com/images/admin-logo.png
  baseURL: https://api.bap.microsoft.com
  humanURL: https://learn.microsoft.com/en-us/power-platform/admin/admin-documentation
  tags:
  - Administration
  - Environments
  - Governance
  - Licensing
  - Management
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/admin/admin-documentation
  - type: PowerShell
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerapps-powershell
  - type: CLI
    url: https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction
  - type: Governance
    url: https://learn.microsoft.com/en-us/power-platform/admin/governance-considerations
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
  - type: Environment Management
    url: https://learn.microsoft.com/en-us/power-platform/admin/list-environments
  - type: Service Principal
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-create-service-principal
  contact:
  - type: Support
    url: https://admin.powerplatform.microsoft.com/support
- name: Power Platform Connectors API
  description: API for custom and certified connectors that extend Power Platform capabilities across Power Apps, Power Automate, Logic Apps, and Copilot Studio.
  image: https://powerplatform.microsoft.com/images/connectors-logo.png
  baseURL: https://api.connectors.microsoft.com
  humanURL: https://learn.microsoft.com/en-us/connectors/
  tags:
  - Connectors
  - Custom Connectors
  - Integration
  - OpenAPI
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/connectors/
  - type: Custom Connectors
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/
  - type: Connector Certification
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/submit-certification
  - type: OpenAPI Support
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/define-openapi-definition
  - type: CLI
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/paconn-cli
  - type: GitHub
    url: https://github.com/microsoft/PowerPlatformConnectors
  contact:
  - type: Support
    url: https://powerapps.microsoft.com/support/
- name: Power Platform Unified API
  description: Unified RESTful API surface for all Power Platform administrative capabilities including licensing, app management, environment management, and governance. Provides a single endpoint at api.powerplatform.com.
  image: https://powerplatform.microsoft.com/images/power-platform-logo.png
  baseURL: https://api.powerplatform.com
  humanURL: https://learn.microsoft.com/en-us/rest/api/power-platform/
  tags:
  - Administration
  - App Management
  - Governance
  - Licensing
  - Power Platform API
  - Unified API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
  - type: Versioning
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-versioning-support
  - type: Permissions Reference
    url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-permission-reference
  - type: App Management
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/appmanagement/applications
  - type: OpenAPI
    url: openapi/power-platform-api-openapi.json
  - type: .NET SDK
    url: https://www.nuget.org/packages/Microsoft.PowerPlatform.Management
  contact:
  - type: Support
    url: https://admin.powerplatform.microsoft.com/support
- name: Power Pages Web API
  description: Web API for Power Pages (formerly Power Apps Portals) enabling CRUD operations on Microsoft Dataverse tables from portal webpages for richer user experiences.
  image: https://powerplatform.microsoft.com/images/power-platform-logo.png
  baseURL: https://[site].powerappsportals.com/_api
  humanURL: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
  tags:
  - Dataverse
  - Portals
  - Power Pages
  - Web API
  - Websites
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
  - type: Read Operations
    url: https://learn.microsoft.com/en-us/power-pages/configure/read-operations
  - type: Write Operations
    url: https://learn.microsoft.com/en-us/power-pages/configure/write-update-delete-operations
  - type: How-To Guide
    url: https://learn.microsoft.com/en-us/power-pages/configure/webapi-how-to
  - type: Developer Overview
    url: https://learn.microsoft.com/en-us/power-pages/configure/developer-overview
  - type: Portal Documentation
    url: https://learn.microsoft.com/en-us/power-pages/
  contact:
  - type: Support
    url: https://powerapps.microsoft.com/support/
name: Microsoft Power Platform APIs
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
type: Contract
image: https://powerplatform.microsoft.com/images/power-platform-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Microsoft Power Platform services including Power Apps, Power Automate, Power BI, Copilot Studio, Power Pages, and Dataverse.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

