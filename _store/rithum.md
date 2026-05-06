---
aid: rithum
name: Rithum
description: Rithum is a commerce operations platform providing dropship, marketplace, and supply chain integration solutions for retailers, brands, and suppliers. Formerly known as CommerceHub and ChannelAdvisor, Rithum connects brands and retailers to manage product listings, inventory, order workflows, and performance across ecommerce channels. The platform powers the Dsco API for dropship and marketplace integrations. In 2025, Rithum launched RithumIQ, an AI engine for automated commerce recommendations and operational insights.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commerce
  - Dropship
  - Marketplace
  - Ecommerce
  - Supply Chain
  - Retail
url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/apis.yml
created: '2025-02-12'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rithum:dsco-platform-api
    name: Dsco Platform API
    description: The Dsco Platform API v3 provides dropship and marketplace commerce integration for retailers and suppliers. It supports order management, catalog synchronization, inventory updates, shipment tracking, returns processing, and invoice workflows via streaming and batch endpoints. Authentication uses OAuth2 bearer tokens obtained from the token endpoint.
    humanURL: https://api.dsco.io/
    baseURL: https://api.dsco.io/api/v3
    tags:
      - Commerce
      - Dropship
      - Marketplace
      - Orders
      - Catalog
      - Inventory
    properties:
      - url: https://api.dsco.io/doc/v3/reference/
        type: Documentation
      - url: https://api.dsco.io/doc/v3/guides/standard-api-guide.html
        type: Guide
      - url: https://api.dsco.io/doc/v3/guides/dropship-api-guide.html
        type: Guide
      - url: https://api.dsco.io/doc/v3/guides/marketplace-api-guide.html
        type: Guide
      - url: https://knowledge.rithum.com/s/article/Getting-started-with-the-Rithum-V3-API
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/openapi/dsco-platform-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/rules/dsco-platform-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/capabilities/commerce-operations.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/json-schema/dsco-order-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/json-schema/dsco-catalog-item-schema.json
        type: JSONSchema
    contact:
      - FN: Rithum Support
        url: https://knowledge.rithum.com
    features:
      - Order Management
      - Catalog Synchronization
      - Inventory Updates
      - Shipment Tracking
      - Returns Processing
      - Invoice Workflows
      - Streaming Events
      - Batch Operations
      - Dropship Integration
      - Marketplace Integration
    useCases:
      - Retailer dropship order processing
      - Supplier catalog and inventory sync
      - Private marketplace management
      - Multi-channel commerce operations
    solutions:
      - Commerce Operations
      - Supply Chain Integration
      - Retail Dropship
    integrations:
      - ChannelAdvisor
      - Mirakl
      - Shopify
      - Salesforce Commerce Cloud
common:
  - type: Website
    url: https://www.rithum.com
  - type: Documentation
    url: https://api.dsco.io/doc/v3/reference/
  - type: Support
    url: https://knowledge.rithum.com
  - type: Blog
    url: https://www.rithum.com/blog/
  - type: PrivacyPolicy
    url: https://www.rithum.com/privacy-policy/
  - type: TermsOfService
    url: https://www.rithum.com/terms-of-service/
  - type: Status
    url: https://status.rithum.com
  - type: GitHub
    url: https://github.com/rithum
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/json-ld/rithum-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/vocabulary/rithum-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
