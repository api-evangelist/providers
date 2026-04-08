---
aid: navision
url: https://raw.githubusercontent.com/api-evangelist/navision/refs/heads/main/apis.yml
apis:
- name: Dynamics NAV Web Services API
  description: SOAP and OData web services for interacting with Dynamics NAV business data. Supports publishing pages, codeunits, and queries as web services for external system integration.
  image: https://example.com/nav-webservices-icon.png
  humanUrl: https://learn.microsoft.com/en-us/dynamics-nav/web-services
  baseUrl: https://{server}:{port}/{instance}/api/{version}
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
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-interacting-with-a-page-web-service--odata-
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
    url: https://support.microsoft.com/dynamics
- name: Dynamics NAV OData API
  description: OData web services for querying and manipulating NAV business entities. Supports both OData v3 and v4 protocols for reading data and writing back to the Dynamics NAV database through exposed pages and queries.
  image: https://example.com/odata-icon.png
  humanUrl: https://learn.microsoft.com/en-us/dynamics-nav/odata-web-services
  baseUrl: https://{server}:{port}/{instance}/OData/Company('{company}')
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
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-interacting-with-a-page-web-service--odata-
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
- name: Dynamics NAV SOAP Web Services
  description: SOAP-based web services for legacy integrations and business logic operations in Dynamics NAV. Exposes pages and codeunits with built-in CRUD operations and supports extension codeunits for custom operations.
  image: https://example.com/soap-icon.png
  humanUrl: https://learn.microsoft.com/en-us/dynamics-nav/soap-web-services
  baseUrl: https://{server}:{port}/{instance}/WS/{company}/
  tags:
  - Business Logic
  - Codeunits
  - Legacy Integration
  - SOAP
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics-nav/soap-web-service-uris
  - type: Reference
    url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--creating-and-using-a-codeunit-web-service--soap-
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/dynamics-nav/walkthrough--registering-and-using-a-page-web-service--soap-
  - type: WSDL
    url: https://{server}:{port}/{instance}/WS/Services?wsdl
- name: Business Central API v2.0
  description: Modern RESTful API for Dynamics 365 Business Central, the cloud evolution of Dynamics NAV. Provides a comprehensive set of endpoints for managing customers, items, accounts, sales orders, and other business entities.
  image: https://example.com/bc-api-icon.png
  humanUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
  baseUrl: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
  tags:
  - Business Central
  - Business Data
  - Cloud ERP
  - Connect Apps
  - REST API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
  - type: Reference
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/endpoints-apis-for-dynamics
  - type: Authentication
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/authenticate-web-services-using-oauth
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-develop-connect-apps
  - type: Change Log
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
  - type: OpenAPI
    url: openapi/business-central-api-v2.yml
  - type: JSONSchema
    url: json-schema/customer.json
  - type: JSONSchema
    url: json-schema/vendor.json
  - type: JSONSchema
    url: json-schema/item.json
  - type: JSONSchema
    url: json-schema/sales-order.json
  - type: JSONSchema
    url: json-schema/purchase-order.json
  - type: JSONLDContext
    url: json-ld/context.jsonld
  contact:
  - FN: Microsoft Dynamics Support
    email: bcsupport@microsoft.com
    url: https://dynamics.microsoft.com/support/
- name: Business Central Administration Center API
  description: REST API for programmatic administration of Business Central environments. Enables querying and managing production and sandbox environments, setting up notifications, and viewing tenant telemetry.
  image: https://example.com/bc-admin-icon.png
  humanUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/administration-center-api
  baseUrl: https://api.businesscentral.dynamics.com/admin/v2.28
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
  - type: Getting Started
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
  humanUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/itpro-introduction-to-automation-apis
  baseUrl: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/microsoft/automation/v2.0
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
  - type: Getting Started
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
  humanUrl: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-overview
  baseUrl: https://api.businesscentral.dynamics.com/v2.0/{environment}/api
  tags:
  - Business Central
  - Custom APIs
  - Data Integration
  - REST API
  - Web Services
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/endpoints-apis-for-dynamics
  - type: Authentication
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/authenticate-web-services-using-oauth
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
  contact:
  - FN: Microsoft Dynamics Support
    email: bcsupport@microsoft.com
    url: https://dynamics.microsoft.com/support/
name: Microsoft Dynamics NAV
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
type: Contract
image: https://example.com/navision-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API collection for Microsoft Dynamics NAV (formerly Navision), an enterprise resource planning (ERP) solution for small and medium-sized businesses. Dynamics NAV has evolved into Dynamics 365 Business Central, which provides modern REST, OData, and SOAP web services for business data integration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

