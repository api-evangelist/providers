---
name: SAP Commerce Cloud
description: SAP Commerce Cloud (formerly Hybris) provides enterprise e-commerce and omnichannel customer experience management capabilities including product content management, order management, personalization, and assisted service for B2B and B2C commerce scenarios.
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
url: https://www.sap.com/products/crm/commerce-cloud.html
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - B2B
  - B2C
  - Commerce
  - Customer Experience
  - Ecommerce
  - Omnichannel
  - Retail
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
common:
  - type: Portal
    url: https://api.sap.com/
  - type: Getting Started
    url: https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/0996ba68e5794b8ab51db8d25d4c9f8c/
  - type: Authentication
    url: https://help.sap.com/docs/SAP_COMMERCE/d0224eca81e249cb821f2cdf45a82ace/627c92dbdb7648449c840c07dd9cac7b.html
  - type: Support
    url: https://support.sap.com/
  - type: Community
    url: https://community.sap.com/topics/commerce-cloud
  - type: Terms of Service
    url: https://www.sap.com/about/legal/terms-of-use.html
  - type: Privacy Policy
    url: https://www.sap.com/about/legal/privacy.html
  - type: Status
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-commerce-web-services-openapi.yml
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-assisted-service-openapi.yml
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-integration-openapi.yml
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-admin-openapi.yml
  - type: OpenAPI
    url: openapi/sap-commerce-cloud-product-content-management-openapi.yml
  - type: JSON-LD
    url: json-ld/sap-commerce-cloud-context.jsonld
  - type: JSONSchema
    url: json-schema/sap-commerce-cloud-product-schema.json
  - type: JSONSchema
    url: json-schema/sap-commerce-cloud-order-schema.json
  - type: JSONSchema
    url: json-schema/sap-commerce-cloud-cart-schema.json
  - type: JSONSchema
    url: json-schema/sap-commerce-cloud-customer-schema.json
  - type: JSONStructure
    url: json-structure/sap-commerce-cloud-product-structure.json
  - type: JSONStructure
    url: json-structure/sap-commerce-cloud-order-structure.json
  - type: SpectralRules
    url: rules/sap-commerce-cloud-rules.yml
  - type: NaftikoCapability
    url: capabilities/shopping-and-checkout.yaml
  - type: NaftikoCapability
    url: capabilities/catalog-and-content-management.yaml
  - type: Vocabulary
    url: vocabulary/sap-commerce-cloud-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
