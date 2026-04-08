---
aid: sap-commerce-cloud
url: https://raw.githubusercontent.com/api-evangelist/sap-commerce-cloud/refs/heads/main/apis.yml
apis:
- name: Commerce Web Services API
  description: RESTful API for commerce operations including product catalog, cart, checkout, and order management.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/9d346683b0084da2938be8a285c0c27a/
  baseURL: https://{tenant}.{region}.commercecloud.sap/occ/v2
  tags:
  - Cart
  - Checkout
  - Orders
  - Products
  - REST
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/8c19398686691014a8c0fd6c3e5d44a0.html
  - type: OpenAPI
    url: https://api.sap.com/api/commerce_web_services/overview
  - type: Authentication
    url: https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/627c92dbdb7648449c840c07dd9cac7b.html
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-commerce-web-services-openapi.yml
- name: Assisted Service Module API
  description: API for assisted service capabilities enabling customer service representatives to help customers with their shopping experience.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_COMMERCE/9d346683b0084da2938be8a285c0c27a/8b571515866910148fc18b9e59d3e084.html
  baseURL: https://{tenant}.{region}.commercecloud.sap/assistedservicewebservices
  tags:
  - Assisted Service
  - Customer Service
  - REST
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_COMMERCE/9d346683b0084da2938be8a285c0c27a/8b571515866910148fc18b9e59d3e084.html
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-assisted-service-openapi.yml
- name: Integration API
  description: OData-based integration API for data integration and synchronization with external systems.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/50c996852b32456c96d3161a95544cdb/
  baseURL: https://{tenant}.{region}.commercecloud.sap/odata2webservices
  tags:
  - Data Sync
  - Integration
  - OData
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/50c996852b32456c96d3161a95544cdb/8696c1e06fce461a862d7f0eb60cca7b.html
  - type: API Reference
    url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/b490bb4e85bc42a7aa09d513d0bcb18e/
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-integration-openapi.yml
- name: Admin API
  description: Administrative API for system configuration, maintenance, and monitoring.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/
  baseURL: https://{tenant}.{region}.commercecloud.sap/
  tags:
  - Admin
  - Configuration
  - Monitoring
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-admin-openapi.yml
- name: Product Content Management API
  description: API for managing product content including images, descriptions, and attributes.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/
  baseURL: https://{tenant}.{region}.commercecloud.sap/occ/v2
  tags:
  - Catalog
  - Content
  - Products
  - REST
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-product-content-management-openapi.yml
name: SAP Commerce Cloud
tags:
- B2B
- B2C
- Commerce
- Customer Experience
- Ecommerce
- Omnichannel
- Retail
type: Contract
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP Commerce Cloud (formerly Hybris) provides enterprise e-commerce and omnichannel customer experience management capabilities including product content management, order management, and personalization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

