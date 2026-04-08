---
aid: microsoft-dynamics-365
url: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/apis.yml
apis:
- name: Dynamics 365 Sales API
  description: API for managing sales processes, leads, opportunities, accounts, and contacts in Dynamics 365 Sales.
  image: https://dynamics.microsoft.com/assets/sales-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/sales/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - CRM
  - Leads
  - Opportunities
  - Sales
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/sales/developer/developer-guide
  - type: OpenAPI
    url: https://[org].api.crm.dynamics.com/api/data/v9.2/$metadata
  - type: Authentication
    url: https://docs.microsoft.com/powerapps/developer/data-platform/authenticate
  - type: Rate Limits
    url: https://docs.microsoft.com/powerapps/developer/data-platform/api-limits
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
    url: https://support.microsoft.com/dynamics365
- name: Dynamics 365 Customer Service API
  description: API for managing customer service cases, knowledge articles, queues, and service level agreements.
  image: https://dynamics.microsoft.com/assets/service-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/customer-service/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Cases
  - Customer Service
  - Knowledge Base
  - Support
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/customer-service/developer/developer-guide
  - type: OpenAPI
    url: https://[org].api.crm.dynamics.com/api/data/v9.2/$metadata
  - type: Webhooks
    url: https://docs.microsoft.com/powerapps/developer/data-platform/use-webhooks
- name: Dynamics 365 Finance & Operations API
  description: API for managing financial operations, accounting, budgeting, and enterprise resource planning.
  image: https://dynamics.microsoft.com/assets/finance-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/finance/
  baseURL: https://[org].operations.dynamics.com/data
  tags:
  - Accounting
  - ERP
  - Finance
  - Operations
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities
  - type: OData
    url: https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/odata
  - type: Authentication
    url: https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/services-home-page
  - type: API Reference
    url: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/api-reference
  - type: Data Management REST API
    url: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-api
- name: Dynamics 365 Marketing API
  description: API for managing marketing campaigns, customer journeys, email marketing, and lead scoring.
  image: https://dynamics.microsoft.com/assets/marketing-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/marketing/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Campaigns
  - Email Marketing
  - Lead Scoring
  - Marketing
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/marketing/developer/marketing-developer-guide
  - type: API Reference
    url: https://docs.microsoft.com/dynamics365/marketing/developer/extend-marketing-api
- name: Dynamics 365 Supply Chain Management API
  description: API for managing inventory, warehouse operations, procurement, and supply chain processes.
  image: https://dynamics.microsoft.com/assets/supply-chain-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/supply-chain/
  baseURL: https://[org].operations.dynamics.com/data
  tags:
  - Inventory
  - Procurement
  - Supply Chain
  - Warehouse
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/supply-chain/dev-itpro/
  - type: Data Entities
    url: https://docs.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/data-entities-data-packages
- name: Dynamics 365 Business Central API
  description: API for managing small to medium business operations including finance, sales, service, and operations.
  image: https://dynamics.microsoft.com/assets/business-central-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/business-central/
  baseURL: https://api.businesscentral.dynamics.com/v2.0/[tenant]/[environment]/api/v2.0
  tags:
  - Business Management
  - Finance
  - Operations
  - SMB
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/business-central/dev-itpro/api-reference/v2.0/
  - type: OpenAPI
    url: https://docs.microsoft.com/dynamics365/business-central/dev-itpro/api-reference/v2.0/openapi
  - type: Getting Started
    url: https://docs.microsoft.com/dynamics365/business-central/dev-itpro/api-reference/v2.0/enabling-apis-for-dynamics-nav
  - type: Webhooks
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/dynamics-subscriptions
  - type: Custom API Development
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-develop-custom-api
  - type: API Endpoints
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/endpoints-apis-for-dynamics
  - type: REST API Overview
    url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/api-overview
- name: Dynamics 365 Commerce API
  description: API for managing e-commerce operations, retail stores, omnichannel commerce, and customer experiences.
  image: https://dynamics.microsoft.com/assets/commerce-icon.png
  humanURL: https://docs.microsoft.com/dynamics365/commerce/
  baseURL: https://[org].commerce.dynamics.com/api
  tags:
  - E-Commerce
  - Omnichannel
  - POS
  - Retail
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/dynamics365/commerce/e-commerce-extensibility/overview
  - type: Retail Server API
    url: https://docs.microsoft.com/dynamics365/commerce/dev-itpro/retail-server-architecture
- name: Microsoft Dataverse Web API
  description: RESTful web service API implementing OData v4.0 for interacting with data in Microsoft Dataverse, the underlying data platform for Dynamics 365 and Power Platform applications.
  humanURL: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Data Platform
  - Dataverse
  - OData
  - Power Platform
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
  - type: OpenAPI
    url: openapi/microsoft-dynamics-365-dataverse-web-api-openapi.yml
  - type: JSONSchema
    url: json-schema/microsoft-dynamics-365-account-schema.json
  - type: JSONLD
    url: json-ld/microsoft-dynamics-365-context.jsonld
  - type: Web API Types and Operations
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-types-operations
  - type: Web API Service Documents
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/web-api-service-documents
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits
  - type: Developer Guide
    url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/overview
- name: Dynamics 365 Customer Insights Data API
  description: API for building applications based on unified customer data, enabling customer data unification, segmentation, and enrichment through programmatic access.
  humanURL: https://learn.microsoft.com/en-us/dynamics365/customer-insights/
  baseURL: https://api.ci.ai.dynamics.com/
  tags:
  - Analytics
  - CDP
  - Customer Data
  - Customer Insights
  - Segmentation
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/apis
  - type: API Management
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/apis-manage
  - type: Dataverse APIs
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/dv-odata
  - type: Developer Portal
    url: https://developer.ci.ai.dynamics.com/
- name: Dynamics 365 Customer Insights Journeys API
  description: API for managing real-time customer journeys, segments, and event-driven marketing interactions programmatically.
  humanURL: https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Events
  - Journeys
  - Marketing Automation
  - Real-Time Marketing
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/
  - type: Segment API
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/real-time-marketing-api-segment
  - type: Events API
    url: https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/developer/using-rtm-events-api
- name: Dynamics 365 Field Service API
  description: API for managing field service operations including work orders, scheduling, resource availability, and work hour calendars.
  humanURL: https://learn.microsoft.com/en-us/dynamics365/field-service/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Field Service
  - Resource Management
  - Scheduling
  - Work Orders
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/field-service/
  - type: Resource Availability API
    url: https://learn.microsoft.com/en-us/dynamics365/field-service/search-resource-availability-api
  - type: Work Hours Calendar API
    url: https://learn.microsoft.com/en-us/dynamics365/field-service/field-service-work-hours-calendar-api
  - type: Entity Reference
    url: https://learn.microsoft.com/en-us/dynamics365/field-service/developer/reference/about-entity-reference
- name: Dynamics 365 Human Resources API
  description: API for managing human resources operations including employee data, payroll integration, applicant tracking, and benefits administration.
  humanURL: https://learn.microsoft.com/en-us/dynamics365/human-resources/
  baseURL: https://[org].operations.dynamics.com/data
  tags:
  - HR
  - Human Resources
  - Payroll
  - Recruiting
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-developer-overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-developer-api-authentication
  - type: Payroll Integration API
    url: https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-admin-integration-payroll-api-introduction
  - type: Applicant Tracking API
    url: https://learn.microsoft.com/en-us/dynamics365/human-resources/hr-admin-integration-ats-api-introduction
- name: Dynamics 365 Project Operations API
  description: API for managing project operations including project scheduling, resource management, time and expense tracking, and project financials.
  humanURL: https://learn.microsoft.com/en-us/dynamics365/project-operations/
  baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  tags:
  - Project Accounting
  - Project Management
  - Resource Management
  - Time Tracking
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dynamics365/project-operations/
  - type: Schedule API
    url: https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/schedule-api-preview
  - type: Schedule API with Power Automate
    url: https://learn.microsoft.com/en-us/dynamics365/project-operations/project-management/scheduling-apis-powerautomate
name: Microsoft Dynamics 365
tags:
- Business Applications
- Cloud
- CRM
- Enterprise
- ERP
- Microsoft
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Dynamics 365 is a cloud-based suite of business applications that unify CRM and ERP capabilities to help organizations manage sales, marketing, customer service, finance, operations, and commerce.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

