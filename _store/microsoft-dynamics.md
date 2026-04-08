---
aid: microsoft-dynamics
url: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics/refs/heads/main/apis.yml
apis:
- aid: microsoft-dynamics:business-central-api
  name: Microsoft Dynamics 365 Business Central API
  tags:
  - Business Central
  - ERP
  - Finance
  humanURL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
  properties:
  - url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
    type: Documentation
  - url: openapi/microsoft-dynamics-business-central-openapi.yml
    type: OpenAPI
  - url: json-schema/customer.json
    type: JSONSchema
  - url: json-schema/vendor.json
    type: JSONSchema
  - url: json-schema/item.json
    type: JSONSchema
  - url: json-schema/sales-order.json
    type: JSONSchema
  - url: json-schema/sales-invoice.json
    type: JSONSchema
  - url: json-schema/employee.json
    type: JSONSchema
  - url: json-ld/microsoft-dynamics-context.jsonld
    type: JSONLD
  description: The Microsoft Dynamics 365 Business Central API (v2.0) provides a RESTful OData v4 interface for integrating with Business Central. It exposes standard business entities including companies, customers, vendors, items, sales orders, sales invoices, purchase orders, purchase invoices, journals, general ledger entries, accounts, and employees. The API supports both cloud (SaaS) and on-premises deployments, authenticated via Microsoft Entra ID.
- aid: microsoft-dynamics:dataverse-web-api
  name: Microsoft Dynamics 365 Dataverse Web API
  tags:
  - CRM
  - Customer Engagement
  - Sales
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  properties:
  - url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
    type: Documentation
  - url: openapi/microsoft-dynamics-dataverse-openapi.yml
    type: OpenAPI
  - url: json-schema/account.json
    type: JSONSchema
  - url: json-schema/contact.json
    type: JSONSchema
  - url: json-schema/lead.json
    type: JSONSchema
  - url: json-schema/opportunity.json
    type: JSONSchema
  - url: json-ld/microsoft-dynamics-context.jsonld
    type: JSONLD
  description: The Microsoft Dynamics 365 Dataverse Web API provides a RESTful OData v4 endpoint for Dynamics 365 Sales, Customer Service, Field Service, and other customer engagement applications. It supports CRUD operations on core CRM entities such as accounts, contacts, leads, opportunities, cases (incidents), and activities. Authentication is handled via Microsoft Entra ID (Azure AD).
- aid: microsoft-dynamics:finance-operations-api
  name: Microsoft Dynamics 365 Finance & Operations Data API
  tags:
  - ERP
  - Finance
  - Supply Chain
  humanURL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata
  properties:
  - url: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata
    type: Documentation
  - url: openapi/microsoft-dynamics-finance-operations-openapi.yml
    type: OpenAPI
  - url: json-ld/microsoft-dynamics-context.jsonld
    type: JSONLD
  description: The Microsoft Dynamics 365 Finance & Operations Data API exposes business data entities via OData v4 RESTful endpoints. It provides access to finance, supply chain, manufacturing, and human resources data including customers, vendors, released products, sales order headers, purchase order headers, general journal entries, and workers. The API supports cross- company queries and is authenticated via Microsoft Entra ID.
name: Microsoft Dynamics
tags:
- CRM
- ERP
- Microsoft Dynamics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: 'Microsoft Dynamics 365 is a suite of enterprise resource planning (ERP) and customer relationship management (CRM) applications. It provides APIs across three main platforms: Business Central for small and mid-sized business ERP, Dataverse Web API for CRM and customer engagement, and Finance & Operations for enterprise-grade ERP covering finance, supply chain, manufacturing, and human resources. All APIs use OData v4 conventions and authenticate via Microsoft Entra ID.'
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

