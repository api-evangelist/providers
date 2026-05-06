---
aid: microsoft-power-apps
name: Microsoft Power Apps
description: Collection of APIs for Microsoft Power Apps platform enabling low-code application development, automation, and data connectivity.
image: https://powerplatform.microsoft.com/images/power-apps-logo.png
created: '2024'
modified: '2026-04-18'
artifacts:
  openapi:
    - name: Microsoft Dataverse Web API OpenAPI Specification
      path: openapi/microsoft-power-apps-dataverse-web-api-openapi.yml
      version: 3.1.0
      description: OpenAPI 3.1.0 specification for the Dataverse Web API v9.2 covering accounts, contacts, and entity definitions with full CRUD operations and OData query support
  jsonSchema:
    - name: Microsoft Power Apps Dataverse Entity Schema
      path: json-schema/microsoft-power-apps-entity-schema.json
      version: draft/2020-12
      description: JSON Schema defining core Dataverse entity types (Account, Contact, Entity) with property types, constraints, and enum values based on the Microsoft.Dynamics.CRM namespace
  jsonLd:
    - name: Microsoft Power Apps JSON-LD Context
      path: json-ld/microsoft-power-apps-context.jsonld
      version: '1.1'
      description: JSON-LD context mapping Dataverse entity properties to Schema.org, Dublin Core, OData, and vCard vocabularies for semantic interoperability
specificationVersion: '0.19'
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
      - type: RateLimits
        url: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/api-limits
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/power-platform/powerapps/apps
      - type: GettingStarted
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api
      - type: OpenAPI
        url: openapi/microsoft-power-apps-dataverse-web-api-openapi.yml
      - type: JSONSchema
        url: json-schema/microsoft-power-apps-entity-schema.json
      - type: JSONLD
        url: json-ld/microsoft-power-apps-context.jsonld
      - type: Security
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
      - type: SDK
        url: https://docs.microsoft.com/en-us/power-platform/admin/powershell-getting-started
      - type: CLI
        url: https://docs.microsoft.com/en-us/power-platform/developer/cli/introduction
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-platform/environmentmanagement/environment-management-settings
      - type: Documentation
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
      - type: Documentation
        url: https://docs.microsoft.com/en-us/connectors/connector-reference/
      - type: Documentation
        url: https://docs.microsoft.com/en-us/connectors/custom-connectors/
      - type: APIReference
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
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-platform/power-fx/formula-reference
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-apps/maker/canvas-apps/application-lifecycle-management
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-platform/power-fx/overview
      - type: Documentation
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
      - type: APIReference
        url: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference
      - type: Documentation
        url: https://docs.microsoft.com/en-us/power-apps/developer/model-driven-apps/customize-entity-forms
      - type: Documentation
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/implementing-controls-using-typescript
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/component-framework/create-custom-controls-using-pcf
      - type: Documentation
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
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/power-platform/admin/powerplatform-api-getting-started
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-platform/appmanagement/applications
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-platform/environmentmanagement/environment-management-settings
      - type: Documentation
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
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-pages/configure/read-operations
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-pages/configure/write-update-delete-operations
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/power-apps/maker/portals/webapi-tutorial
      - type: Documentation
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/iorganizationservice-interface
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/org-service/use-messages
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient
      - type: Documentation
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
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/architecture
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/alm
      - type: Security
        url: https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy
common:
  - type: DeveloperPortal
    url: https://docs.microsoft.com/en-us/power-apps/developer/
  - type: Community
    url: https://powerusers.microsoft.com/
  - type: Blog
    url: https://powerapps.microsoft.com/blog/
  - type: Pricing
    url: https://powerapps.microsoft.com/pricing/
  - type: StatusPage
    url: https://status.powerplatform.microsoft.com/
  - type: Support
    url: https://powerapps.microsoft.com/support/
  - type: Training
    url: https://docs.microsoft.com/en-us/learn/powerplatform/power-apps
  - type: GitHubRepository
    url: https://github.com/microsoft/PowerApps-Samples
  - type: TermsOfService
    url: https://www.microsoft.com/licensing/terms/productoffering/MicrosoftPowerApps
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/alm/
    title: ALM Documentation
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/alm/pipelines
    title: Pipelines
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/developer/
    title: Power Platform Developer Documentation
  - type: CLI
    url: https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/pipeline
  - type: Security
    url: https://learn.microsoft.com/en-us/power-platform/admin/wp-security
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/overview
    title: Power Fx Overview
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-platform/power-fx/formula-reference-overview
    title: Power Fx Formula Reference
  - type: Training
    url: https://learn.microsoft.com/en-us/training/paths/simplify-power-platform-deployments/
    title: Deployment Training
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave1/power-apps/planned-features
  - type: Features
    data:
      - name: Low-Code Development
        description: Visual drag-and-drop app building with Power Fx formulas and pre-built templates.
      - name: Microsoft Dataverse
        description: Built-in data platform with security, business logic, and integration capabilities.
      - name: Custom Connectors
        description: Connect to any external API through standard and custom connector definitions.
      - name: Model-Driven Apps
        description: Automatically generated UIs based on data model and business logic configuration.
      - name: Component Framework
        description: Professional code components using TypeScript for custom controls in canvas and model-driven apps.
  - type: UseCases
    data:
      - name: Business Process Automation
        description: Digitize paper-based processes and manual workflows with custom business applications.
      - name: Customer Portal
        description: Build external-facing portals using Power Pages with Dataverse Web API integration.
      - name: Field Service Apps
        description: Create mobile applications for field workers with offline capabilities and data sync.
      - name: Data Management
        description: Build CRUD applications on Dataverse for managing business data with role-based security.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Native integration with Teams, SharePoint, Outlook, and Excel for productivity workflows.
      - name: Dynamics 365
        description: Shared Dataverse platform with Dynamics 365 CRM and ERP modules for unified data.
      - name: Power Automate
        description: Trigger automated flows from Power Apps for cross-system process automation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Business Applications
  - Cloud
  - Enterprise
  - Low-Code
  - Microsoft
  - No-Code
  - Power Platform
  - SaaS
---
