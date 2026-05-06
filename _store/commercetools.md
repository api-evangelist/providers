---
aid: commercetools
url: https://raw.githubusercontent.com/api-evangelist/commercetools/refs/heads/main/apis.yml
name: commercetools
tags:
  - Commerce
  - Composable Commerce
  - E-Commerce
  - GraphQL
  - REST
  - SDK
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
x-type: company
created: '2025-09-15'
modified: '2026-05-04'
apis:
  - aid: commercetools:http-api
    name: Commercetools HTTP API
    tags:
      - Commerce
      - Composable Commerce
      - E-Commerce
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.{region}.commercetools.com
    humanURL: https://docs.commercetools.com/api
    properties:
      - url: https://docs.commercetools.com/api
        type: Documentation
      - url: openapi/commercetools-http-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/commercetools-subscriptions-asyncapi.yml
        type: AsyncAPI
    description: The commercetools HTTP API is the core REST interface for programmatic access to all data and functionality within a Composable Commerce project. It covers a broad range of commerce resources including products, product types, categories, carts, orders, customers, payments, discounts, inventory, shipping methods, stores, and business units. All resources follow RESTful conventions using standard HTTP verbs and return JSON responses.
  - aid: commercetools:graphql-api
    name: Commercetools GraphQL API
    tags:
      - Commerce
      - Composable Commerce
      - E-Commerce
      - GraphQL
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.{region}.commercetools.com
    humanURL: https://docs.commercetools.com/api/graphql
    properties:
      - url: https://docs.commercetools.com/api/graphql
        type: Documentation
    description: The commercetools GraphQL API provides a flexible, network-efficient alternative to the HTTP API for querying and mutating Composable Commerce resources. It exposes a single endpoint and allows clients to request exactly the data they need, reducing over-fetching and minimizing round trips. The GraphQL API uses the same API clients, authentication tokens, and project scopes as the HTTP API.
  - aid: commercetools:import-api
    name: Commercetools Import API
    tags:
      - Bulk Operations
      - Commerce
      - Data Migration
      - Import
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://import.{region}.commercetools.com
    humanURL: https://docs.commercetools.com/api/import-export/overview
    properties:
      - url: https://docs.commercetools.com/api/import-export/overview
        type: Documentation
      - url: openapi/commercetools-import-api-openapi.yml
        type: OpenAPI
    description: The commercetools Import API enables bulk importing of commerce data into a Composable Commerce project. It supports importing categories, product types, products, product variants, prices, inventory entries, orders, and customers. Imports are processed asynchronously through import containers, and the API provides endpoints for monitoring import operation status and handling validation errors.
  - aid: commercetools:change-history-api
    name: Commercetools Change History API
    tags:
      - Audit Log
      - Change History
      - Commerce
      - Compliance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://history.{region}.commercetools.com
    humanURL: https://docs.commercetools.com/api/history/overview
    properties:
      - url: https://docs.commercetools.com/api/history/overview
        type: Documentation
      - url: openapi/commercetools-change-history-api-openapi.yml
        type: OpenAPI
    description: The commercetools Change History API provides a queryable audit log of all changes made to resources within a Composable Commerce project. It records mutations applied to resources such as products, orders, customers, discounts, and carts, along with metadata about who made the change and when. The API is hosted on separate regional endpoints and supports filtering by resource type, date range, user, and client.
  - aid: commercetools:typescript-sdk
    name: Commercetools TypeScript SDK
    tags:
      - Commerce
      - JavaScript
      - SDK
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.commercetools.com/sdk/typescript-sdk
    properties:
      - url: https://docs.commercetools.com/sdk/typescript-sdk
        type: Documentation
    description: The commercetools TypeScript SDK is the official client library for interacting with the Composable Commerce HTTP API, Import API, and GraphQL API from JavaScript and TypeScript applications. It provides full type safety, IDE autocompletion, and a fluent domain-specific language for constructing valid API requests. The SDK handles OAuth 2.0 token management, request building, and response deserialization.
  - aid: commercetools:java-sdk
    name: Commercetools Java SDK
    tags:
      - Commerce
      - Java
      - JVM
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.commercetools.com/sdk/java-sdk
    properties:
      - url: https://docs.commercetools.com/sdk/java-sdk
        type: Documentation
    description: The commercetools Java SDK is the official client library for accessing the Composable Commerce APIs from Java applications. It provides strongly typed request builders, automatic OAuth 2.0 token management, and support for all HTTP API and Import API endpoints. The SDK is compatible with standard Java development toolchains and is distributed via Maven Central. It is commonly used in enterprise backend systems and microservices that require JVM-based integration with the commercetools platform.
  - aid: commercetools:checkout-api
    name: Commercetools Checkout API
    tags:
      - Checkout
      - Commerce
      - Embedded Components
      - Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.commercetools.com/checkout
    properties:
      - url: https://docs.commercetools.com/checkout
        type: Documentation
    description: The commercetools Checkout API provides programmatic control over Checkout application configurations within Composable Commerce. The Checkout Applications API allows developers to create, update, and manage Checkout applications without manual setup in the Merchant Center, enabling automated deployment and configuration across multiple stores, regions, and business units. Checkout integrates with payment connectors available through the Connect marketplace.
  - aid: commercetools:merchant-center-customizations-api
    name: Commercetools Merchant Center Customizations API
    tags:
      - Commerce
      - Customizations
      - Extensions
      - Merchant Center
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.commercetools.com/merchant-center-customizations/concepts/merchant-center-api
    properties:
      - url: https://docs.commercetools.com/merchant-center-customizations/concepts/merchant-center-api
        type: Documentation
    description: The commercetools Merchant Center Customizations API provides the programmatic interface for building custom applications and UI extensions within the Merchant Center. It exposes proxy endpoints to underlying REST and GraphQL APIs, allowing custom UIs to interact with Composable Commerce resources in a secure, scoped manner. Developers use this API when creating Custom Applications that extend the Merchant Center with business-specific tooling.
common:
  - type: Website
    url: https://commercetools.com/
  - type: Documentation
    url: https://docs.commercetools.com/
  - type: Pricing
    url: https://commercetools.com/pricing
  - type: Status
    url: https://status.commercetools.com/
  - type: GitHub
    url: https://github.com/commercetools
  - url: json-ld/commercetools-context.jsonld
    type: JSON-LD
  - url: json-schema/commercetools-order-schema.json
    type: JSONSchema
  - url: json-schema/commercetools-product-schema.json
    type: JSONSchema
  - url: json-schema/commercetools-subscription-message-schema.json
    type: JSONSchema
  - url: rules/commercetools-rules.yml
    type: Spectral
  - url: capabilities/commercetools-composable-commerce-capabilities.yml
    type: NaftikoCapabilities
  - type: Features
    data:
      - 'Core Commerce Edition: Composable Commerce APIs (custom price)'
      - 'Foundry Edition: includes Frontend + Checkout + Blueprints + Expert Services'
      - 'Premium Edition: unlimited SKUs, B2B APIs, Audit Log Premium'
      - Headless / API-first commerce
      - REST API at api.{region}.commercetools.com
      - GraphQL API at api.{region}.commercetools.com/{project}/graphql
      - 'REST API: 200 req/sec/project default'
      - 'Search (Product Projection): 100 req/sec'
      - 'Concurrent connections: 200/project'
      - Cart, Order, Customer, Catalog, Discount, Inventory APIs
      - OAuth 2.0 with scoped tokens
      - Subscription messages for async event delivery
      - Webhooks via HTTP destinations
      - 'Multi-region: AWS US/EU/Australia, GCP US/EU/Australia'
      - Custom Objects for extensibility
      - Composable Frontend (B2C2B Foundry)
    sources:
      - https://commercetools.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
description: commercetools is the leading composable, headless, API-first Commerce platform powering large-scale B2C, B2B, and marketplace digital commerce for enterprise brands. The platform exposes a broad API surface organized into the HTTP API (core REST interface), GraphQL API (flexible query and mutation alternative), Import API (bulk data ingestion), Change History API (audit log), Checkout API (managed checkout configuration), and Merchant Center Customizations API (custom UI extensions). It is complemented by official SDKs (TypeScript, Java, PHP, .NET, Python) and AsyncAPI-based subscriptions for event-driven integrations.
---
