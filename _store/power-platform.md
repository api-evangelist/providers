---
name: Microsoft Power Platform APIs
description: Collection of APIs for Microsoft Power Platform services including Power Apps, Power Automate, Power BI, Copilot Studio, Power Pages, and Dataverse.
image: https://powerplatform.microsoft.com/images/power-platform-logo.png
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.18'
url: https://powerplatform.microsoft.com/apis.json
tags:
  - Business Applications
  - Copilot Studio
  - Dataverse
  - Low-Code
  - Microsoft
  - No-Code
  - Power Pages
  - Power Platform
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
      - type: RateLimits
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits
      - type: Pricing
        url: https://powerapps.microsoft.com/pricing/
      - type: APIReference
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
        title: OData Types and Operations
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/authenticate-web-api
      - type: SDK
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/developer-tools
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
      - type: Integrations
        url: https://learn.microsoft.com/en-us/connectors/
        title: Connectors
      - type: Pricing
        url: https://powerautomate.microsoft.com/pricing/
      - type: APIReference
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
      - type: SDK
        url: https://learn.microsoft.com/en-us/javascript/api/overview/powerbi/
      - type: Pricing
        url: https://powerbi.microsoft.com/pricing/
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
      - type: Pricing
        url: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio#pricing
      - type: Console
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
      - type: CLI
        url: https://learn.microsoft.com/en-us/power-platform/developer/cli/introduction
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
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
      - type: Documentation
        url: https://learn.microsoft.com/en-us/connectors/custom-connectors/
        title: Custom Connectors
      - type: CLI
        url: https://learn.microsoft.com/en-us/connectors/custom-connectors/paconn-cli
      - type: GitHubRepository
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
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
      - type: Versioning
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-versioning-support
      - type: OpenAPI
        url: openapi/power-platform-api-openapi.json
      - type: SDK
        url: https://www.nuget.org/packages/Microsoft.PowerPlatform.Management
        title: .NET SDK
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
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-pages/configure/webapi-how-to
    contact:
      - type: Support
        url: https://powerapps.microsoft.com/support/
common:
  - type: DeveloperPortal
    url: https://learn.microsoft.com/en-us/power-platform/developer/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/
  - type: Blog
    url: https://www.microsoft.com/en-us/power-platform/blog/
  - type: GitHubOrganization
    url: https://github.com/microsoft/powerplatform
  - type: Training
    url: https://learn.microsoft.com/en-us/training/powerplatform/
  - type: StatusPage
    url: https://status.cloud.microsoft/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/privacystatement
  - type: TermsOfService
    url: https://www.microsoft.com/licensing/terms/
  - type: APIReference
    url: https://learn.microsoft.com/en-us/rest/api/power-platform/
  - type: Support
    url: https://admin.powerplatform.microsoft.com/
  - type: Features
    data:
      - name: Low-Code App Development
        description: Build custom business applications with drag-and-drop canvas and model-driven app builders without writing code.
      - name: Workflow Automation
        description: Automate repetitive business processes with cloud flows, desktop flows, and AI-powered process mining.
      - name: Business Intelligence
        description: Create interactive dashboards and reports with Power BI for data-driven decision making across the organization.
      - name: AI-Powered Chatbots
        description: Build conversational AI agents with Copilot Studio that integrate with Teams, websites, and other channels.
      - name: Custom Connectors
        description: Extend platform capabilities by creating custom connectors to any REST API or third-party service.
      - name: Dataverse Data Platform
        description: Store and manage business data in a secure, scalable cloud database with built-in business logic and security.
      - name: Environment Management
        description: Manage isolated environments for development, testing, and production with governance policies and access controls.
      - name: Embedded Analytics
        description: Embed Power BI reports and dashboards directly into custom applications and portals.
  - type: UseCases
    data:
      - name: Citizen Developer Apps
        description: Enable business users to build departmental applications without IT involvement using low-code tools.
      - name: Process Automation
        description: Automate approval workflows, data collection, notifications, and integrations across Microsoft 365 and third-party services.
      - name: Enterprise Reporting
        description: Consolidate data from multiple sources into unified dashboards and self-service analytics for executive decision-making.
      - name: Customer Service Bots
        description: Deploy AI-powered virtual agents for customer support, HR inquiries, and IT helpdesk automation.
      - name: Data Integration
        description: Connect and synchronize data across SaaS applications, on-premises systems, and cloud databases using connectors and Dataverse.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Deep integration with Outlook, Teams, SharePoint, OneDrive, and Excel for seamless productivity workflows.
      - name: Microsoft Azure
        description: Connect to Azure services including Azure Active Directory, Azure SQL, Azure Functions, and Cognitive Services.
      - name: Dynamics 365
        description: Extend Dynamics 365 CRM and ERP applications with custom Power Apps and automated workflows.
      - name: SAP
        description: Connect to SAP ERP and S/4HANA through certified connectors for enterprise data integration.
      - name: Salesforce
        description: Integrate with Salesforce CRM data and workflows through the Salesforce connector.
      - name: ServiceNow
        description: Connect Power Platform workflows with ServiceNow ITSM and service management processes.
  - type: NaftikoCapability
    url: capabilities/platform-administration.yaml
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
