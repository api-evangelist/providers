---
aid: oracle-retail
name: Oracle Retail
description: Oracle Retail is a suite of cloud and on-premises applications for retailers spanning merchandising, pricing, supply chain, omnichannel order management, point of service, and store operations. Oracle Retail APIs provide REST, messaging, and integration services for managing the full retail lifecycle across digital and physical channels.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-retail/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Retail
  - Merchandising
  - Order Management
  - Pricing
  - Inventory
  - Point of Sale
  - Omnichannel
  - Oracle
apis:
  - name: Oracle Retail Merchandising Foundation Cloud Service API
    description: Oracle Retail Merchandising Foundation Cloud Service provides REST APIs for managing merchandise hierarchies, item setup, purchase orders, cost management, and inventory transactions across omnichannel retail operations.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/
    baseURL: https://{host}/MerchServices/MerchRes/v1
    tags:
      - Inventory
      - Merchandising
      - REST
      - Retail
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/
      - type: Reference
        url: https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmwrg/
      - type: OpenAPI
        url: openapi/oracle-retail-merchandising-openapi.yml
  - name: Oracle Retail Pricing Cloud Service API
    description: Oracle Retail Pricing Cloud Service provides REST APIs for regular price management, promotional pricing, competitive pricing, and clearance pricing across retail operations.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/retail/retail-pricing-cloud/latest/
    tags:
      - Pricing
      - Promotions
      - REST
      - Retail
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/retail/retail-pricing-cloud/latest/
  - name: Oracle Retail Integration Cloud Service API
    description: Oracle Retail Integration Cloud Service (RIB and BDI) provides messaging and bulk data integration APIs connecting Oracle Retail applications to third-party systems using enterprise messaging patterns.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/retail/retail-integration-cloud/latest/
    tags:
      - Integration
      - Middleware
      - REST
      - Retail
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/retail/retail-integration-cloud/latest/
  - name: Oracle Retail Order Management Suite Cloud Service API
    description: Oracle Retail Order Management Suite Cloud Service provides REST APIs for omnichannel order orchestration, fulfillment, sourcing, and customer service across digital and physical retail channels.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/retail/retail-oms-suite-cloud/26.1.101.0/
    tags:
      - Omnichannel
      - Order Management
      - REST
      - Retail
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/retail/retail-oms-suite-cloud/26.1.101.0/
      - type: OpenAPI
        url: openapi/oracle-retail-order-management-openapi.yml
  - name: Oracle Retail Xstore Point of Service API
    description: Oracle Retail Xstore Point of Service provides APIs for store operations including transactions, inventory lookup, customer management, and omnichannel fulfillment from retail store systems.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/retail/retail-xstore-point-of-service/25.0/
    tags:
      - Point of Sale
      - REST
      - Retail
      - Store Operations
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/retail/retail-xstore-point-of-service/25.0/
common:
  - type: Portal
    url: https://docs.oracle.com/en/industries/retail/
  - type: Documentation
    url: https://docs.oracle.com/en/industries/retail/
  - type: Website
    url: https://www.oracle.com/retail/
  - type: Support
    url: https://community.oracle.com/gbu/rgbu/
  - type: Blog
    url: https://blogs.oracle.com/retail/
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/privacy-policy/
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms/
  - type: GitHub Organization
    url: https://github.com/oracle
  - type: Developer Portal
    url: https://www.oracle.com/developer/
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: OpenAPI
    url: openapi/oracle-retail-merchandising-openapi.yml
  - type: OpenAPI
    url: openapi/oracle-retail-order-management-openapi.yml
  - type: JSON Schema
    url: json-schema/oracle-retail-item-schema.json
  - type: JSON Schema
    url: json-schema/oracle-retail-order-schema.json
  - type: JSON-LD Context
    url: json-ld/oracle-retail-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
