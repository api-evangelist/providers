---
aid: target
url: https://raw.githubusercontent.com/api-evangelist/target/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
description: Target Corporation is one of the largest retailers in the United States, offering a wide assortment of general merchandise and food through more than 1,900 stores and digital channels. Target's technology platform powers partner integrations, internal services, and open-source tooling across their retail operations.
apis:
  - aid: target:target-api
    name: Target API
    tags:
      - E-Commerce
      - Inventory
      - Orders
      - Products
      - Retail
      - Stores
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.target.com
    humanURL: https://developer.target.com/
    properties:
      - url: https://developer.target.com/
        type: Documentation
      - url: openapi/target-target-api-openapi.yml
        type: OpenAPI
      - url: rules/target-spectral-rules.yml
        type: SpectralRules
      - url: capabilities/shared/target-api.yaml
        type: NaftikoCapability
    description: Target provides partner APIs for product catalog access, inventory availability, order management, and store information. These APIs enable technology partners and affiliates to integrate with Target's retail platform. The Redsky aggregation platform powers client-managed REST APIs built on GraphQL queries covering product, price, promotion, and fulfillment data.
  - aid: target:target-redsky-api
    name: Target Redsky API
    tags:
      - E-Commerce
      - GraphQL
      - Products
      - Retail
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://redsky.target.com
    humanURL: https://tech.target.com/blog/empowering-clients-api
    properties:
      - url: https://tech.target.com/blog/empowering-clients-api
        type: Documentation
    description: Redsky is Target's internal aggregation API platform that converts GraphQL queries into client-managed REST APIs. It serves product data, pricing, promotions, and fulfillment information for Target.com and mobile applications. The platform manages 200+ unique APIs across 30 clients backed by 50+ integrations.
  - aid: target:target-partner-api
    name: Target Partner API
    tags:
      - E-Commerce
      - Inventory
      - Partners
      - Retail
      - Suppliers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.target.com
    humanURL: https://developer.target.com/
    properties:
      - url: https://developer.target.com/
        type: Documentation
    description: Target's partner API program enables technology vendors, affiliates, and supply chain partners to integrate with Target's retail operations including product catalog, inventory management, order fulfillment, and store data.
common:
  - type: Website
    url: https://www.target.com
  - type: Developer Portal
    url: https://developer.target.com/
  - type: Blog
    url: https://tech.target.com
  - type: GitHub Org
    url: https://github.com/target
  - type: Open Source
    url: https://tech.target.com/open-source
  - type: Status
    url: https://status.target.com
  - type: JSONSchema
    url: json-schema/target-product-schema.json
  - type: JSONSchema
    url: json-schema/target-store-schema.json
  - type: JSONStructure
    url: json-structure/target-product-structure.json
  - type: JSONLD
    url: json-ld/target-context.jsonld
  - type: Vocabulary
    url: vocabulary/target-vocabulary.yml
  - type: NaftikoCapability
    url: capabilities/retail-integration.yaml
tags:
  - E-Commerce
  - Retail
  - Products
  - Inventory
  - Fortune 100
  - Stores
  - Orders
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
