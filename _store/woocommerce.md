---
aid: woocommerce
name: WooCommerce
description: WooCommerce is the world's most popular open-source eCommerce platform, built on WordPress. It provides a comprehensive REST API for managing products, orders, customers, coupons, reports, webhooks, and store settings, plus a public-facing Store API for headless frontends. WooCommerce also delivers real-time events via webhooks for order, product, customer, and subscription lifecycle changes.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/woocommerce/refs/heads/main/apis.yml
tags:
  - eCommerce
  - Open Source
  - Orders
  - Products
  - WordPress
created: '2026-05-03'
modified: '2026-05-04'
specificationVersion: '0.19'
access: 3rd-Party
position: Consumer
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
apis:
  - aid: woocommerce:rest-api
    name: WooCommerce REST API
    description: The WooCommerce REST API is the primary server-side interface for reading and writing WooCommerce store data programmatically. It follows REST conventions, uses JSON, and is integrated with the WordPress REST API under /wp-json/wc/v3/. The API covers products, variations, categories, attributes, orders, customers, coupons, tax rates, shipping zones, payment gateways, settings, webhooks, reports, and system status. Authentication uses Consumer Key and Consumer Secret pairs via HTTP Basic Auth or OAuth 1.0a.
    humanURL: https://developer.woocommerce.com/docs/apis/rest-api/
    baseURL: https://example.com/wp-json/wc/v3
    tags:
      - eCommerce
      - Orders
      - Products
      - REST
    properties:
      - type: Documentation
        url: https://developer.woocommerce.com/docs/apis/rest-api/
      - type: APIReference
        url: https://woocommerce.github.io/woocommerce-rest-api-docs/
      - type: Authentication
        url: https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication
      - type: OpenAPI
        url: openapi/woocommerce-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/woocommerce-rest-api-order-schema.json
        title: Order Schema
      - type: JSONSchema
        url: json-schema/woocommerce-rest-api-product-schema.json
        title: Product Schema
      - type: JSONSchema
        url: json-schema/woocommerce-rest-api-customer-schema.json
        title: Customer Schema
      - type: JSONSchema
        url: json-schema/woocommerce-rest-api-coupon-schema.json
        title: Coupon Schema
  - aid: woocommerce:store-api
    name: WooCommerce Store API
    description: The WooCommerce Store API provides unauthenticated public REST endpoints for building customer-facing cart, checkout, and product functionality. Accessible under /wp-json/wc/store/v1/, it covers products, categories, attributes, tags, reviews, cart operations, checkout, and customer orders. Write operations require a nonce token from the cart response.
    humanURL: https://developer.woocommerce.com/docs/apis/store-api/
    baseURL: https://example.com/wp-json/wc/store/v1
    tags:
      - Cart
      - Checkout
      - eCommerce
      - Headless
      - Products
    properties:
      - type: Documentation
        url: https://developer.woocommerce.com/docs/apis/store-api/
      - type: OpenAPI
        url: openapi/woocommerce-store-api-openapi.yml
      - type: JSONSchema
        url: json-schema/woocommerce-store-api-cart-schema.json
        title: Cart Schema
      - type: JSONSchema
        url: json-schema/woocommerce-store-api-store-product-schema.json
        title: Store Product Schema
      - type: JSONSchema
        url: json-schema/woocommerce-store-api-checkout-schema.json
        title: Checkout Schema
  - aid: woocommerce:webhook-events
    name: WooCommerce Webhook Events
    description: WooCommerce delivers real-time event notifications via HTTP POST webhooks for orders, products, customers, coupons, and subscriptions lifecycle changes. Webhooks are configured in the WooCommerce admin or via the REST API and deliver JSON payloads signed with HMAC-SHA256.
    humanURL: https://woocommerce.com/document/webhooks/
    tags:
      - Events
      - Webhooks
    properties:
      - type: Documentation
        url: https://woocommerce.com/document/webhooks/
      - type: AsyncAPI
        url: asyncapi/woocommerce-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/woocommerce-rest-api-webhook-schema.json
        title: Webhook Schema
common:
  - type: Website
    url: https://woocommerce.com
  - type: DeveloperPortal
    url: https://developer.woocommerce.com
  - type: Documentation
    url: https://developer.woocommerce.com/docs/
  - type: GettingStarted
    url: https://developer.woocommerce.com/docs/getting-started/
  - type: GitHub
    url: https://github.com/woocommerce/woocommerce
  - type: GitHubOrganization
    url: https://github.com/woocommerce
  - type: Blog
    url: https://developer.woocommerce.com/blog/
  - type: Support
    url: https://woocommerce.com/support/
  - type: Forum
    url: https://wordpress.org/support/plugin/woocommerce/
  - type: ReleaseNotes
    url: https://developer.woocommerce.com/changelog/
  - type: StatusPage
    url: https://status.woocommerce.com
  - type: JSON-LD
    url: json-ld/woocommerce-context.jsonld
  - type: SpectralRules
    url: rules/woocommerce-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/store-management.yaml
    title: Store Management
  - type: NaftikoCapability
    url: capabilities/headless-commerce.yaml
    title: Headless Commerce
  - type: Vocabulary
    url: vocabulary/woocommerce-vocabulary.yaml
  - type: Tools
    url: https://github.com/woocommerce/woocommerce-rest-api-js-lib
    title: WooCommerce REST API JavaScript Library
  - type: Tools
    url: https://github.com/woocommerce/wc-api-php
    title: WooCommerce REST API PHP Library
  - type: Tools
    url: https://github.com/woocommerce/qit-mcp
    title: WooCommerce QIT MCP Server
  - type: Tools
    url: https://github.com/woocommerce/wc-mcp-ability
    title: WooCommerce MCP Ability Plugin
  - type: SDK
    url: https://www.npmjs.com/package/@woocommerce/woocommerce-rest-api
    title: WooCommerce REST API JS Library (npm)
  - type: Features
    data:
      - Free open-source WordPress plugin
      - 0% revenue share, no platform fees
      - 'Hosting: $25-$350/month from chosen provider'
      - 'Payment processing: ~2.50%-2.90% + $0.30 (gateway-dependent)'
      - 'Extensions: $29-$299/year each'
      - REST API at /wp-json/wc/v3/
      - OAuth 1.0a + WooCommerce Consumer Keys
      - Webhooks for order, customer, product events
      - Bulk operations up to 100 items/request
      - WordPress ecosystem of themes and plugins
      - WooCommerce Stripe, WooPayments, PayPal, Square gateways
      - WooCommerce Subscriptions for recurring billing
      - WooCommerce Shipping for label printing
      - WooCommerce Marketplace for extensions
      - Multilingual via WPML/Polylang
      - Run multiple gateways simultaneously
    sources:
      - https://woocommerce.com/pricing/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Headless Storefront
        description: Build custom React or Vue frontends using the Store API for products, cart, and checkout.
      - name: ERP Integration
        description: Sync orders and inventory with ERP systems via the REST API and webhooks.
      - name: Order Fulfillment
        description: Automate order fulfillment workflows using webhook notifications and REST API updates.
      - name: Product Catalog Sync
        description: Sync product catalog from a PIM system to WooCommerce via the REST API.
      - name: Analytics and Reporting
        description: Pull sales reports and customer data via the Reports API for BI tools.
  - type: Integrations
    data:
      - name: WordPress
        description: WooCommerce runs as a WordPress plugin and uses the WordPress REST API infrastructure.
      - name: PayPal
        description: Official PayPal payment gateway integration for WooCommerce.
      - name: Stripe
        description: Official Stripe payment gateway integration.
      - name: ShipStation
        description: Order fulfillment and shipping integration.
      - name: Mailchimp
        description: Email marketing integration for customer segmentation and abandoned cart.
      - name: Reddit Ads
        description: Official Reddit for WooCommerce integration for ad conversion tracking.
      - name: Pinterest
        description: Official Pinterest for WooCommerce integration for product sync.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
