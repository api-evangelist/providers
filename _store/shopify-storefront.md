---
aid: shopify-storefront
name: Shopify Storefront API
description: The Shopify Storefront API is a GraphQL API that enables developers to build custom headless storefronts, purchasing flows, and commerce experiences using Shopify as a backend. The API provides programmatic access to products, collections, carts, checkout, customer accounts, and contextual pricing. It is designed for headless commerce architectures and powers the Shopify Hydrogen framework.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commerce
  - Ecommerce
  - Headless
  - GraphQL
  - Storefront
  - Products
  - Cart
  - Checkout
url: https://raw.githubusercontent.com/api-evangelist/shopify-storefront/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shopify-storefront:shopify-storefront-api
    name: Shopify Storefront API
    description: The Shopify Storefront API is a GraphQL API for building headless commerce experiences. It provides access to products, collections, cart, checkout, customer accounts, and contextual pricing. All requests use GraphQL over HTTPS and require a Storefront API access token. The Storefront API supports both unauthenticated (public) and customer-authenticated access patterns.
    humanURL: https://shopify.dev/docs/api/storefront
    baseURL: https://{store_name}.myshopify.com/api/2024-10/graphql.json
    tags:
      - Commerce
      - Ecommerce
      - Headless
      - GraphQL
      - Products
      - Cart
      - Checkout
    properties:
      - type: Documentation
        url: https://shopify.dev/docs/api/storefront
      - type: Reference
        url: https://shopify.dev/docs/api/storefront/latest
      - type: GettingStarted
        url: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/getting-started
      - type: Authentication
        url: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api/get-started-with-the-storefront-api
      - type: RateLimits
        url: https://shopify.dev/docs/api/usage/rate-limits
      - type: Versioning
        url: https://shopify.dev/docs/api/usage/versioning
      - type: OpenAPI
        url: openapi/shopify-storefront-openapi.yml
      - type: JSONSchema
        url: json-schema/shopify-storefront-product-schema.json
      - type: JSONSchema
        url: json-schema/shopify-storefront-cart-schema.json
      - type: JSONLD
        url: json-ld/shopify-storefront-context.jsonld
      - type: SpectralRules
        url: rules/shopify-storefront-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/headless-commerce.yaml
      - type: Vocabulary
        url: vocabulary/shopify-storefront-vocabulary.yml
    contact:
      - FN: Shopify Developer Support
        url: https://shopify.dev/
  - aid: shopify-storefront:shopify-hydrogen
    name: Shopify Hydrogen
    description: Hydrogen is Shopify's opinionated React-based framework for building headless storefronts powered by the Storefront API. Hydrogen provides components, hooks, and utilities optimized for commerce including streaming SSR, React Server Components, and built-in Shopify data fetching.
    humanURL: https://shopify.dev/docs/storefronts/headless/hydrogen
    tags:
      - Commerce
      - Headless
      - React
      - Framework
      - SSR
    properties:
      - type: Documentation
        url: https://shopify.dev/docs/storefronts/headless/hydrogen
      - type: GettingStarted
        url: https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started
      - type: SDK
        url: https://github.com/Shopify/hydrogen
  - aid: shopify-storefront:shopify-buy-sdk
    name: Shopify Buy SDK
    description: The Shopify JavaScript Buy SDK is a lightweight library that enables developers to integrate Shopify's storefront capabilities into any website or application. The SDK wraps the Storefront API and provides methods for fetching products, collections, and managing carts.
    humanURL: https://shopify.github.io/js-buy-sdk/
    tags:
      - Commerce
      - JavaScript
      - SDK
      - Cart
    properties:
      - type: Documentation
        url: https://shopify.github.io/js-buy-sdk/
      - type: SDK
        url: https://github.com/Shopify/js-buy-sdk
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
