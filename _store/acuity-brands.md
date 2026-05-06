---
aid: acuity-brands
url: https://raw.githubusercontent.com/api-evangelist/acuity-brands/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - aid: acuity-brands:acuity-brands-api
    name: Acuity Brands API
    tags:
      - Lighting
      - B2B
      - Inventory
      - Order Management
      - Building Controls
    properties:
      - type: HumanURL
        url: https://api-docs.acuitybrands.com/
      - type: BaseURL
        url: https://api.acuitybrands.com/v1
      - type: OpenAPI
        url: openapi/acuity-brands.json
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: Examples
        url: examples/
    description: B2B REST APIs for Acuity Brands distributors covering inventory availability, order status tracking, product catalog, and web content. Enables integration of Acuity Brands data into distributor ERP, e-commerce, and ordering systems.
common:
  - type: Website
    url: https://www.acuity-brands.com
  - type: Portal
    url: https://api-docs.acuitybrands.com/
  - type: Documentation
    url: https://api-docs.acuitybrands.com/docs/intro/
  - type: GitHubOrganization
    url: https://github.com/acuitybrands
  - type: SpectralRules
    url: rules/acuity-brands-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/acuity-brands-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/distributor-integration.yaml
  - type: JSONLD
    url: json-ld/acuity-brands-context.jsonld
description: Acuity Brands is a provider of lighting, lighting controls, building management systems, and location-aware applications for commercial, industrial, institutional, and residential markets.
features:
  - name: Inventory Availability
    description: Real-time inventory availability by product number and warehouse location with estimated ship dates.
    tags:
      - Inventory
      - Lighting
  - name: Order Status Tracking
    description: Full order status data including estimated and actual ship dates, line item status, and order totals.
    tags:
      - Orders
      - B2B
  - name: Shipment Tracking
    description: Carrier name, PRO number, and tracking URLs for all shipments associated with an order.
    tags:
      - Shipments
      - Logistics
  - name: Product Catalog
    description: Search and retrieve Acuity Brands product catalog with specifications, certifications, pricing, and images.
    tags:
      - Catalog
      - Products
  - name: Web Content
    description: Product and category web pages with metadata and content for distributor e-commerce integration.
    tags:
      - Web Content
      - E-Commerce
  - name: Multi-Brand Coverage
    description: APIs cover all major Acuity Brands brands including Lithonia Lighting, Holophane, nLight, Juno, and Distech Controls.
    tags:
      - Brands
      - Lighting
useCases:
  - name: ERP Integration
    description: Sync inventory and order data into distributor ERP systems for automated stock management and order tracking.
    tags:
      - ERP
      - Integration
  - name: E-Commerce Product Feeds
    description: Pull product catalog, images, specs, and pricing into distributor e-commerce storefronts.
    tags:
      - E-Commerce
      - Catalog
  - name: Order Status Automation
    description: Automatically surface order status and shipment tracking to customers without manual ADC lookups.
    tags:
      - Orders
      - Automation
  - name: Inventory Availability Checks
    description: Check real-time stock availability before quoting or placing orders for Acuity Brands products.
    tags:
      - Inventory
      - Quoting
integrations:
  - name: SAP
    description: Integrate Acuity Brands inventory and order data into SAP ERP for automated purchasing workflows.
    tags:
      - SAP
      - ERP
  - name: Salesforce
    description: Surface product availability and order status within Salesforce CRM for distributor sales reps.
    tags:
      - Salesforce
      - CRM
  - name: Epicor
    description: Connect Acuity Brands order status to Epicor distribution ERP systems.
    tags:
      - Epicor
      - ERP
solutions:
  - name: Distributor API Access
    description: API access available to authorized Acuity Brands distributors via request through the developer portal.
    tags:
      - Distributor
      - Access
  - name: B2B Digital Integration
    description: Enable fully digital order-to-shipment workflows between Acuity Brands and electrical distributors.
    tags:
      - B2B
      - Digital
---
