---
aid: shopify-admin
name: Shopify Admin API
description: The Shopify Admin API provides programmatic access to manage Shopify store administration. It enables app developers and merchants to manage products, customers, orders, inventory, shipping, fulfillment, collections, webhooks, and store settings. The Admin API is available in both REST and GraphQL formats. Shopify is transitioning from REST to GraphQL as the primary API, with GraphQL recommended for all new development.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commerce
  - Ecommerce
  - Admin
  - Products
  - Orders
  - Customers
url: https://raw.githubusercontent.com/api-evangelist/shopify-admin/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shopify-admin:shopify-admin-rest-api
    name: Shopify Admin REST API
    description: 'The Shopify Admin REST API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, shipping, and store configuration. All requests require a valid Shopify access token generated through OAuth. Note: Shopify is deprecating the REST Admin API in favor of GraphQL; new development should use the GraphQL Admin API.'
    humanURL: https://shopify.dev/docs/api/admin-rest
    baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
    tags:
      - Commerce
      - Ecommerce
      - Admin
      - REST
      - Products
      - Orders
      - Customers
    properties:
      - type: Documentation
        url: https://shopify.dev/docs/api/admin-rest
      - type: Reference
        url: https://shopify.dev/docs/api/admin-rest/latest
      - type: Authentication
        url: https://shopify.dev/docs/apps/auth/get-access-tokens
      - type: RateLimits
        url: https://shopify.dev/docs/api/usage/rate-limits
      - type: Versioning
        url: https://shopify.dev/docs/api/usage/versioning
      - type: OpenAPI
        url: openapi/shopify-admin-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/shopify-admin-product-schema.json
      - type: JSONSchema
        url: json-schema/shopify-admin-order-schema.json
      - type: JSONSchema
        url: json-schema/shopify-admin-customer-schema.json
      - type: JSONStructure
        url: json-structure/shopify-admin-product-structure.json
      - type: JSONLDContext
        url: json-ld/shopify-admin-context.jsonld
      - type: SpectralRules
        url: rules/shopify-admin-rules.yml
      - type: Capabilities
        url: capabilities/store-management.yaml
      - type: Vocabulary
        url: vocabulary/shopify-admin-vocabulary.yml
    contact:
      - FN: Shopify Developer Support
        url: https://shopify.dev/
        email: api@shopify.com
  - aid: shopify-admin:shopify-admin-graphql-api
    name: Shopify Admin GraphQL API
    description: The Shopify Admin GraphQL API is the recommended API for building Shopify apps and integrations. It provides access to all Shopify admin resources including products, customers, orders, inventory, fulfillment, and analytics. GraphQL enables efficient data fetching with precise field selection, real-time subscriptions, and access to advanced platform features not available in REST.
    humanURL: https://shopify.dev/docs/api/admin-graphql
    baseURL: https://{store_name}.myshopify.com/admin/api/2024-10/graphql.json
    tags:
      - Commerce
      - Ecommerce
      - Admin
      - GraphQL
      - Products
      - Orders
      - Customers
    properties:
      - type: Documentation
        url: https://shopify.dev/docs/api/admin-graphql
      - type: Reference
        url: https://shopify.dev/docs/api/admin-graphql/latest
      - type: GettingStarted
        url: https://shopify.dev/docs/api/usage/graphql
      - type: Explorer
        url: https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer
      - type: Authentication
        url: https://shopify.dev/docs/apps/auth/get-access-tokens
      - type: RateLimits
        url: https://shopify.dev/docs/api/usage/rate-limits
    contact:
      - FN: Shopify Developer Support
        url: https://shopify.dev/
  - aid: shopify-admin:shopify-webhooks
    name: Shopify Webhooks
    description: Shopify webhooks allow apps to subscribe to specific events that occur in a store. When an event occurs, Shopify sends an HTTP POST request with a JSON payload to the configured endpoint. Webhooks can be configured for events across all major Shopify resources including orders, products, customers, inventory, fulfillment, and app-specific events.
    humanURL: https://shopify.dev/docs/api/webhooks
    tags:
      - Commerce
      - Ecommerce
      - Webhooks
      - Events
    properties:
      - type: Documentation
        url: https://shopify.dev/docs/api/webhooks
      - type: Reference
        url: https://shopify.dev/docs/api/webhooks/2024-10
    contact:
      - FN: Shopify Developer Support
        url: https://shopify.dev/
common:
  - type: Website
    url: https://shopify.dev/
  - type: Documentation
    url: https://shopify.dev/docs/api
  - type: Authentication
    url: https://shopify.dev/docs/apps/auth/get-access-tokens
  - type: RateLimits
    url: https://shopify.dev/docs/api/usage/rate-limits
  - type: Versioning
    url: https://shopify.dev/docs/api/usage/versioning
  - type: ChangeLog
    url: https://shopify.dev/changelog
  - type: Blog
    url: https://shopify.dev/blog
  - type: GitHub
    url: https://github.com/Shopify
  - type: JSONSchema
    url: json-schema/shopify-admin-product-schema.json
  - type: JSONSchema
    url: json-schema/shopify-admin-order-schema.json
  - type: JSONSchema
    url: json-schema/shopify-admin-customer-schema.json
  - type: JSONStructure
    url: json-structure/shopify-admin-product-structure.json
  - type: JSONLDContext
    url: json-ld/shopify-admin-context.jsonld
  - type: Examples
    url: examples/shopify-admin-list-products-example.json
  - type: Examples
    url: examples/shopify-admin-create-order-example.json
  - type: Vocabulary
    url: vocabulary/shopify-admin-vocabulary.yml
  - type: SpectralRules
    url: rules/shopify-admin-rules.yml
  - type: Capabilities
    url: capabilities/store-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
