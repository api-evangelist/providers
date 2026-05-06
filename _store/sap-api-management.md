---
aid: sap-api-management
name: SAP API Management
description: SAP API Management is an API platform that enables organizations to design, import, publish, secure, and monitor APIs. It provides a self-service developer portal (API Business Hub Enterprise), OpenAPI-based API design tools, policy management, and access to the SAP Business Accelerator Hub for discovering and consuming SAP and partner APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Developer Portal
  - Enterprise
  - SAP
url: https://raw.githubusercontent.com/api-evangelist/sap-api-management/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
x-profiled: 2026-05
specificationVersion: '0.19'
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
    description: 'The SAP API Management API Portal API provides RESTful endpoints for programmatically managing API proxies, API products, applications, developers, policies, and key-value maps within the SAP API Management platform. It is used by administrators and developers to automate the full API lifecycle including creation, versioning, and publishing of APIs. The API uses OData conventions with base URL: https://{tenant-url}/apiportal/api/1.0/Management.svc.'
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
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sap-api-management/refs/heads/main/openapi/sap-api-management-portal-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-api-management-api-proxy-schema.json
      - type: JSONSchema
        url: json-schema/sap-api-management-api-product-schema.json
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
common:
  - type: Portal
    url: https://api.sap.com/
  - type: Documentation
    url: https://help.sap.com/docs/sap-api-management
  - type: Website
    url: https://www.sap.com/products/technology-platform/api-management.html
  - type: Getting Started
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/what-is-api-management
  - type: Authentication
    url: https://help.sap.com/docs/sap-api-management/sap-api-management/user-authentication
  - type: Blog
    url: https://blogs.sap.com/tags/73554900100700002381/
  - type: Community
    url: https://community.sap.com/topics/api-management
  - type: Support
    url: https://support.sap.com/en/product/support-by-product/73554900100700002381.html
  - type: Status
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: GitHub Organization
    url: https://github.com/SAP-samples
  - type: GitHubRepository
    url: https://github.com/SAP/apibusinesshub-api-recipes
  - type: Terms of Service
    url: https://www.sap.com/about/agreements/policies/cloud-platform.html
  - type: Privacy Policy
    url: https://www.sap.com/about/legal/privacy.html
  - type: YouTube
    url: https://www.youtube.com/@SAPTechnology
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/sap-api-management
  - type: Vocabulary
    url: vocabulary/sap-api-management-vocabulary.yml
  - type: SpectralRules
    url: rules/sap-api-management-rules.yml
  - type: Capabilities
    url: capabilities/api-lifecycle-management.yaml
  - type: JSONLD
    url: json-ld/sap-api-management-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
