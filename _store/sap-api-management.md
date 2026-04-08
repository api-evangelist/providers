---
aid: sap-api-management
url: https://raw.githubusercontent.com/api-evangelist/sap-api-management/refs/heads/main/apis.yml
apis:
- aid: sap-api-management:sap-api-management
  name: SAP API Management API
  description: The SAP API Management API provides programmatic access to manage APIs, API products, developer portal settings, and access control through the SAP API Management platform on SAP Business Technology Platform.
  humanURL: https://help.sap.com/docs/sap-api-management
  tags:
  - API Management
  - Developer Portal
  - SAP BTP
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/sap-api-management
  - type: Reference
    url: https://api.sap.com/package/APIMgmt/overview
  - type: Getting Started
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/what-is-api-management
  - type: Authentication
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/user-authentication
- aid: sap-api-management:sap-api-management-api-portal
  name: SAP API Management API Portal API
  description: The SAP API Management API Portal API provides RESTful endpoints for programmatically managing API proxies, API products, applications, developers, policies, and key-value maps within the SAP API Management platform. It is used by administrators and developers to automate the full API lifecycle including creation, versioning, and publishing of APIs.
  humanURL: https://help.sap.com/docs/sap-api-management/sap-api-management/build-apis
  tags:
  - API Lifecycle
  - API Portal
  - API Proxy
  - REST
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/build-apis
  - type: Reference
    url: https://api.sap.com/api/APIMgmt/overview
  - type: GitHubRepository
    url: https://github.com/SAP/apibusinesshub-api-recipes
- aid: sap-api-management:sap-api-business-hub-enterprise
  name: SAP API Business Hub Enterprise API
  description: The SAP API Business Hub Enterprise (also called API Management Developer Portal) API enables programmatic management of the self-service developer portal. It supports managing API catalog content, developer registrations, application subscriptions, and portal customizations for consumer-facing API discovery and consumption.
  humanURL: https://help.sap.com/docs/sap-api-management/sap-api-management/consume-apis
  tags:
  - API Catalog
  - Developer Portal
  - SAP BTP
  - Self Service
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/consume-apis
  - type: Reference
    url: https://api.sap.com/api/APIMgmtDevPortal/overview
- aid: sap-api-management:sap-api-management-analytics
  name: SAP API Management Analytics API
  description: The SAP API Management Analytics API provides access to API usage metrics, performance statistics, error rates, and traffic analytics for APIs managed on the SAP API Management platform. It supports building custom dashboards and monitoring integrations using aggregated and raw usage data.
  humanURL: https://help.sap.com/docs/sap-api-management/sap-api-management/analyze-apis
  tags:
  - Analytics
  - Metrics
  - Monitoring
  - Reporting
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/analyze-apis
  - type: Reference
    url: https://api.sap.com/api/APIMgmtAnalytics/overview
name: SAP API Management
tags:
- API Management
- Developer Portal
- Enterprise
- SAP
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP API Management is an API platform that enables organizations to design, import, publish, secure, and monitor APIs. It provides a self-service developer portal (API Business Hub Enterprise), OpenAPI-based API design tools, policy management, and access to the SAP Business Accelerator Hub for discovering and consuming SAP and partner APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

