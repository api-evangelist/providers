---
name: Microsoft Dynamics NAV
description: API collection for Microsoft Dynamics NAV (formerly Navision), an enterprise resource planning (ERP) solution for small and medium-sized businesses. Dynamics NAV has evolved into Dynamics 365 Business Central, which provides modern REST, OData, and SOAP web services for business data integration.
image: https://example.com/navision-logo.png
created: '2024-01-20'
modified: '2026-04-18'
url: https://dynamics.microsoft.com/nav-overview/
specificationVersion: '0.19'
tags:
  - Business Management
  - Dynamics NAV
  - ERP
  - Finance
  - Inventory
  - Microsoft
  - Navision
apis:
  - name: Dynamics NAV Web Services API
    description: SOAP and OData web services for interacting with Dynamics NAV business data. Supports publishing pages, codeunits, and queries as web services for external system integration.
    image: https://example.com/nav-webservices-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics-nav/web-services
    baseURL: https://{server}:{port}/{instance}/api/{version}
    tags:
      - Enterprise Resource Planning
      - OData
      - SOAP
      - Web Services
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics-nav/microsoft-dynamics-nav-web-services-overview
      - type: OpenAPI
        url: https://example.com/openapi/nav-webservices.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/dynamics-nav/web-services-authentication
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-interacting-with-a-page-web-service--odata-
    contact:
      - FN: Microsoft Support
        email: support@microsoft.com
        url: https://support.microsoft.com/dynamics
  - name: Dynamics NAV OData API
    description: OData web services for querying and manipulating NAV business entities. Supports both OData v3 and v4 protocols for reading data and writing back to the Dynamics NAV database through exposed pages and queries.
    image: https://example.com/odata-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics-nav/odata-web-services
    baseURL: https://{server}:{port}/{instance}/OData/Company('{company}')
    tags:
      - Business Data
      - Data Integration
      - OData
      - Queries
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics-nav/odata-web-services
      - type: OpenAPI
        url: https://example.com/openapi/nav-odata.yaml
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-interacting-with-a-page-web-service--odata-
    contact:
      - FN: Microsoft Support
        email: support@microsoft.com
  - name: Dynamics NAV SOAP Web Services
    description: SOAP-based web services for legacy integrations and business logic operations in Dynamics NAV. Exposes pages and codeunits with built-in CRUD operations and supports extension codeunits for custom operations.
    image: https://example.com/soap-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics-nav/soap-web-services
    baseURL: https://{server}:{port}/{instance}/WS/{company}/
    tags:
      - Business Logic
      - Codeunits
      - Legacy Integration
      - SOAP
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics-nav/soap-web-service-uris
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-using-a-codeunit-web-service--soap-
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--registering-and-using-a-page-web-service--soap-
  - name: Business Central API v2.0
    description: Modern RESTful API for Dynamics 365 Business Central, the cloud evolution of Dynamics NAV. Provides a comprehensive set of endpoints for managing customers, items, accounts, sales orders, and other business entities.
    image: https://example.com/bc-api-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
    baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
    tags:
      - Business Central
      - Business Data
      - Cloud ERP
      - Connect Apps
      - REST API
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/endpoints-apis-for-dynamics
      - type: Authentication
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/authenticate-web-services-using-oauth
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-develop-connect-apps
      - type: ChangeLog
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
      - type: OpenAPI
        url: openapi/business-central-api-v2.yml
    contact:
      - FN: Microsoft Dynamics Support
        email: bcsupport@microsoft.com
        url: https://dynamics.microsoft.com/support/
  - name: Business Central Administration Center API
    description: REST API for programmatic administration of Business Central environments. Enables querying and managing production and sandbox environments, setting up notifications, and viewing tenant telemetry.
    image: https://example.com/bc-admin-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/administration-center-api
    baseURL: https://api.businesscentral.dynamics.com/admin/v2.28
    tags:
      - Administration
      - Cloud ERP
      - Environment Management
      - Tenant Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/administration-center-api
      - type: Authentication
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/
      - type: OpenAPI
        url: openapi/admin-center-api.yml
    contact:
      - FN: Microsoft Dynamics Support
        email: bcsupport@microsoft.com
        url: https://dynamics.microsoft.com/support/
  - name: Business Central Automation API
    description: API for automating company setup and tenant management in Business Central. Supports creating companies, installing extensions, assigning permissions, and applying RapidStart packages programmatically.
    image: https://example.com/bc-automation-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/itpro-introduction-to-automation-apis
    baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/microsoft/automation/v2.0
    tags:
      - Automation
      - Extension Management
      - Tenant Management
      - User Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/itpro-introduction-to-automation-apis
      - type: Authentication
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/automation-apis-using-s2s-authentication
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-develop-connect-apps
      - type: OpenAPI
        url: openapi/automation-api.yml
    contact:
      - FN: Microsoft Dynamics Support
        email: bcsupport@microsoft.com
        url: https://dynamics.microsoft.com/support/
  - name: Business Central REST API Web Services
    description: RESTful web services layer for Business Central that provides the preferred integration method. Includes built-in APIs, custom API pages and queries, and supports both on-premises and cloud deployments.
    image: https://example.com/bc-rest-icon.png
    humanURL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-overview
    baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api
    tags:
      - Business Central
      - Custom APIs
      - Data Integration
      - REST API
      - Web Services
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/endpoints-apis-for-dynamics
      - type: Authentication
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/authenticate-web-services-using-oauth
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
    contact:
      - FN: Microsoft Dynamics Support
        email: bcsupport@microsoft.com
        url: https://dynamics.microsoft.com/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://dynamics.microsoft.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/users-credential-types
  - type: Blog
    url: https://www.microsoft.com/en-us/dynamics-365/blog/product/dynamics-365-business-central/
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
  - type: Support
    url: https://support.microsoft.com/dynamics
  - type: SignUp
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/trial-signup
  - type: Pricing
    url: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing
  - type: TermsOfService
    url: https://www.microsoft.com/en/dynamics-365/business-applications/legal
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com
  - type: StatusPage
    url: https://status.cloud.microsoft
  - type: GitHubOrganization
    url: https://github.com/microsoft/BCApps
  - type: GitHubRepository
    url: https://github.com/christianbraeunlich/d365bc-api-postman
  - type: RateLimits
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/dynamics-rate-limits
  - type: Features
    data:
      - name: Financial Management
        description: General ledger, accounts payable/receivable, bank reconciliation, and financial reporting
      - name: Sales Order Management
        description: Create and manage sales orders, invoices, credit memos, and quotes
      - name: Purchase Order Management
        description: Manage purchase orders, invoices, and vendor relationships
      - name: Inventory Management
        description: Track items, stock levels, and inventory valuations
      - name: Environment Administration
        description: Programmatic management of production and sandbox environments
      - name: Tenant Automation
        description: Automate company setup, extension management, and user provisioning
  - type: UseCases
    data:
      - name: ERP Integration
        description: Connect external systems to Business Central for real-time business data sync
      - name: Multi-Company Management
        description: Automate company creation and configuration across Business Central tenants
      - name: Financial Reporting
        description: Extract general ledger entries and account data for custom reporting
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Deep integration with Excel, Outlook, and Teams for business workflows
      - name: Power Platform
        description: Connect to Power BI, Power Automate, and Power Apps
      - name: Shopify
        description: Sync orders, customers, and inventory with Shopify stores
  - type: SDK
    url: https://github.com/niclas-timm/laravel-dynamics-365-business-central
    title: Laravel SDK
  - type: SDK
    url: https://github.com/AgoraIO/agora-rest-client-go
    title: Go REST Client
  - type: CLI
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-command-line-tools
    title: AL Language CLI
  - type: JSONSchema
    url: json-schema/customer.json
    title: Customer Schema
  - type: JSONSchema
    url: json-schema/vendor.json
    title: Vendor Schema
  - type: JSONSchema
    url: json-schema/item.json
    title: Item Schema
  - type: JSONSchema
    url: json-schema/sales-order.json
    title: Sales Order Schema
  - type: JSONSchema
    url: json-schema/purchase-order.json
    title: Purchase Order Schema
  - type: JSONSchema
    url: json-schema/business-central-v2-customer-schema.json
    title: BC v2 Customer Schema
  - type: JSONSchema
    url: json-schema/business-central-v2-vendor-schema.json
    title: BC v2 Vendor Schema
  - type: JSONSchema
    url: json-schema/business-central-v2-item-schema.json
    title: BC v2 Item Schema
  - type: JSONSchema
    url: json-schema/business-central-v2-sales-order-schema.json
    title: BC v2 Sales Order Schema
  - type: JSONSchema
    url: json-schema/business-central-v2-purchase-order-schema.json
    title: BC v2 Purchase Order Schema
  - type: JSONSchema
    url: json-schema/admin-center-environment-schema.json
    title: Admin Center Environment Schema
  - type: JSONSchema
    url: json-schema/admin-center-environment-operation-schema.json
    title: Admin Center Environment Operation Schema
  - type: JSONSchema
    url: json-schema/automation-extension-schema.json
    title: Automation Extension Schema
  - type: JSONSchema
    url: json-schema/automation-user-schema.json
    title: Automation User Schema
  - type: JSONSchema
    url: json-schema/automation-automation-company-schema.json
    title: Automation Company Schema
  - type: JSONLD
    url: json-ld/context.jsonld
    title: JSON-LD Context
  - type: JSONLD
    url: json-ld/business-central-v2-context.jsonld
    title: Business Central v2 JSON-LD Context
  - type: JSONLD
    url: json-ld/admin-center-context.jsonld
    title: Admin Center JSON-LD Context
  - type: JSONLD
    url: json-ld/automation-context.jsonld
    title: Automation JSON-LD Context
  - type: Vocabulary
    url: vocabulary/navision-vocabulary.yaml
    title: Navision Vocabulary
  - type: Rules
    url: rules/navision-spectral-rules.yml
    title: Spectral Rules
  - type: Capabilities
    url: capabilities/business-operations.yaml
    title: Business Operations Workflow
  - type: Capabilities
    url: capabilities/platform-administration.yaml
    title: Platform Administration Workflow
  - type: Capabilities
    url: capabilities/shared/business-central-v2.yaml
    title: Business Central v2 Shared Capability
  - type: Capabilities
    url: capabilities/shared/admin-center.yaml
    title: Admin Center Shared Capability
  - type: Capabilities
    url: capabilities/shared/automation.yaml
    title: Automation Shared Capability
---
