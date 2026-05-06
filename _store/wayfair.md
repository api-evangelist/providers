---
aid: wayfair
name: Wayfair
description: Wayfair Inc. is one of the world's largest online destinations for home goods and furniture, serving over 20 million customers and 10,000+ suppliers. Wayfair's Developer Portal provides GraphQL-based APIs enabling suppliers to manage purchase orders, inventory updates, product catalog management, advanced shipment notifications, and returns. The platform is built on federated GraphQL architecture using domain-oriented microservices, allowing suppliers to request only the data they need.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/wayfair/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - E-Commerce
  - Furniture
  - Home Goods
  - Retail
  - Suppliers
  - GraphQL
created: '2025-03-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wayfair:wayfair-supplier-api
    name: Wayfair Supplier API
    description: GraphQL-based API for Wayfair suppliers to manage orders, inventory, product catalogs, shipping notifications, and returns. Provides access to purchase orders, inventory updates, catalog management, and advanced shipment notifications via a unified GraphQL endpoint at api.wayfair.com/v1/graphql.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.wayfair.com/docs/
    baseURL: https://api.wayfair.com/v1/graphql
    tags:
      - Catalog
      - E-Commerce
      - GraphQL
      - Inventory
      - Orders
      - Shipping
      - Suppliers
    properties:
      - type: Documentation
        url: https://developer.wayfair.com/docs/
      - type: Documentation
        url: https://developer.wayfair.io/posts/graphQL
        title: GraphQL Documentation
      - type: OpenAPI
        url: openapi/wayfair-supplier-api.yml
      - type: JSONSchema
        url: json-schema/wayfair-graph-ql-request-schema.json
        title: GraphQL Request Schema
      - type: JSONSchema
        url: json-schema/wayfair-graph-ql-response-schema.json
        title: GraphQL Response Schema
      - type: JSONSchema
        url: json-schema/wayfair-token-request-schema.json
        title: Token Request Schema
      - type: JSONSchema
        url: json-schema/wayfair-token-response-schema.json
        title: Token Response Schema
      - type: JSONStructure
        url: json-structure/wayfair-graph-ql-request-structure.json
        title: GraphQL Request Structure
      - type: JSONStructure
        url: json-structure/wayfair-graph-ql-response-structure.json
        title: GraphQL Response Structure
      - type: Example
        url: examples/wayfair-graph-ql-request-example.json
        title: GraphQL Request Example
      - type: Example
        url: examples/wayfair-token-request-example.json
        title: Token Request Example
common:
  - type: Portal
    url: https://developer.wayfair.com/docs/
    title: Developer Portal
  - type: Portal
    url: https://developer.wayfair.io/posts/introduction
    title: Developer Portal (Introduction)
  - type: Documentation
    url: https://developer.wayfair.io/posts/graphQL
    title: GraphQL Documentation
  - type: Documentation
    url: https://developer.wayfair.io/posts/api-testing
    title: Sandbox API Testing
  - type: Website
    url: https://www.wayfair.com/
    title: Wayfair Website
  - type: About
    url: https://www.aboutwayfair.com/
    title: About Wayfair
  - type: GitHubOrganization
    url: https://github.com/wayfair
    title: Wayfair GitHub Organization
  - type: SpectralRules
    url: rules/wayfair-spectral-rules.yml
    title: Wayfair Spectral Rules
  - type: NaftikoCapability
    url: capabilities/supplier-operations.yaml
    title: Supplier Operations Capability
  - type: Vocabulary
    url: vocabulary/wayfair-vocabulary.yml
    title: Wayfair Vocabulary
  - type: JSON-LD
    url: json-ld/wayfair-context.jsonld
    title: Wayfair JSON-LD Context
  - type: Features
    data:
      - name: GraphQL Supplier API
        description: Unified GraphQL endpoint enabling suppliers to query and mutate data across orders, inventory, catalog, and shipping with precise data fetching.
      - name: Purchase Order Management
        description: Suppliers retrieve, acknowledge, and manage purchase orders from Wayfair buyers through the GraphQL API.
      - name: Inventory Management
        description: Real-time inventory updates and stock level management for the Wayfair marketplace catalog.
      - name: Product Catalog Management
        description: Suppliers manage product listings, pricing, descriptions, and attributes through the Product Catalog Update API.
      - name: Advanced Shipment Notifications
        description: Suppliers submit ASN (Advanced Shipment Notification) data to notify Wayfair of pending shipments, carrier details, and tracking numbers.
      - name: Sandbox Testing Environment
        description: Full sandbox environment at sandbox.api.wayfair.com/v1/graphql for integration testing without affecting production orders.
      - name: OAuth2 Token Authentication
        description: Client credentials flow authentication issuing temporary access tokens for secure API access.
  - type: UseCases
    data:
      - name: Order Fulfillment Automation
        description: Suppliers automate purchase order retrieval, acknowledgment, and fulfillment workflows to reduce manual processing time.
      - name: Inventory Synchronization
        description: Real-time synchronization of warehouse inventory levels with the Wayfair marketplace to prevent overselling.
      - name: Product Catalog Updates
        description: Batch and real-time updates to product listings, pricing, and attributes in the Wayfair catalog.
      - name: Shipping Notification Automation
        description: Automated submission of ASN data and tracking information when orders are shipped from supplier warehouses.
  - type: Integrations
    data:
      - name: Wayfair Sandbox
        description: Full sandbox environment for integration testing before deploying to the production Wayfair platform.
      - name: Apollo GraphQL Federation
        description: Wayfair's federated GraphQL architecture enables domain-oriented microservices composition behind a unified supplier API.
      - name: OAuth2 Authentication
        description: Standard OAuth2 client credentials flow for secure supplier application authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
