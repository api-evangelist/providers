---
aid: shopify
url: https://raw.githubusercontent.com/api-search/commerce/main/_apis/shopify/apis.md
apis:
  - aid: shopify:shopify-api
    name: Shopify Admin REST API
    tags:
      - Admin
      - Commerce
      - Ecommerce
      - REST
      - Retail
    humanURL: https://shopify.dev/docs/api/admin-rest
    properties:
      - url: openapi/shopify-api-openapi.yml
        type: OpenAPI
      - url: openapi/shopify-admin-rest-api-openapi.yml
        type: OpenAPI
      - url: json-schema/shopify-product-schema.json
        type: JSONSchema
      - url: json-schema/shopify-customer-schema.json
        type: JSONSchema
      - url: json-schema/shopify-order-schema.json
        type: JSONSchema
      - url: json-schema/shopify-collection-schema.json
        type: JSONSchema
      - url: json-schema/shopify-inventory-item-schema.json
        type: JSONSchema
      - url: json-schema/shopify-fulfillment-schema.json
        type: JSONSchema
      - url: json-structure/shopify-product-structure.json
        type: JSONStructure
      - url: json-structure/shopify-order-structure.json
        type: JSONStructure
      - url: json-ld/shopify-context.jsonld
        type: JSONLD
      - url: examples/shopify-create-product-example.json
        type: Example
      - url: examples/shopify-list-orders-example.json
        type: Example
      - url: vocabulary/shopify-vocabulary.yml
        type: Vocabulary
      - url: rules/shopify-rules.yml
        type: SpectralRules
      - url: capabilities/shared/admin-rest.yaml
        type: NaftikoCapability
      - url: capabilities/commerce-management.yaml
        type: NaftikoCapability
      - url: https://shopify.dev/docs/api/admin-rest
        type: Documentation
    description: The Shopify Admin REST API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillments, and webhooks for managing all aspects of a Shopify store.
  - aid: shopify:graphql-admin-api
    name: Shopify GraphQL Admin API
    tags:
      - Admin
      - Commerce
      - GraphQL
    humanURL: https://shopify.dev/docs/api/admin-graphql
    properties:
      - url: https://shopify.dev/docs/api/admin-graphql
        type: Documentation
      - url: https://shopify.dev/docs/api/usage/api-exploration/admin-graphiql-explorer
        type: Documentation
      - url: https://shopify.dev/docs/api/admin-graphql/latest
        type: Reference
    description: The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, and more. GraphQL is the recommended API for all new Shopify app development.
  - aid: shopify:storefront-api
    name: Shopify Storefront API
    tags:
      - Commerce
      - GraphQL
      - Headless
      - Storefronts
    humanURL: https://shopify.dev/docs/api/storefront
    properties:
      - url: https://shopify.dev/docs/api/storefront
        type: Documentation
      - url: https://shopify.dev/docs/storefronts/headless/building-with-the-storefront-api
        type: GettingStarted
      - url: https://shopify.dev/docs/api/storefront/latest
        type: Reference
    description: The Storefront API is a GraphQL API that provides commerce primitives to build custom, scalable, and performant shopping experiences on any platform, including the web, apps, and games. It enables customers to view products and collections, add products to a cart, and check out.
  - aid: shopify:customer-account-api
    name: Shopify Customer Account API
    tags:
      - Accounts
      - Commerce
      - Customers
      - GraphQL
    humanURL: https://shopify.dev/docs/api/customer
    properties:
      - url: https://shopify.dev/docs/api/customer
        type: Documentation
      - url: https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/getting-started
        type: GettingStarted
    description: The Customer Account API offers a secure way to access private customer-scoped data, enabling you to build personalized, customer-authenticated experiences in your custom storefronts or apps. Customers can view their orders, manage their profile, and more.
  - aid: shopify:partner-api
    name: Shopify Partner API
    tags:
      - Commerce
      - GraphQL
      - Partners
    humanURL: https://shopify.dev/docs/api/partner
    properties:
      - url: https://shopify.dev/docs/api/partner
        type: Documentation
    description: The Partner API provides access to data in the Partners Dashboard, including transactions that impact your earnings, app events, and for participating partners, Experts Marketplace opportunities. It is a GraphQL API that enables Shopify Partners to automate operations.
  - aid: shopify:payments-apps-api
    name: Shopify Payments Apps API
    tags:
      - Commerce
      - GraphQL
      - Payments
    humanURL: https://shopify.dev/docs/api/payments-apps
    properties:
      - url: https://shopify.dev/docs/api/payments-apps
        type: Documentation
      - url: https://shopify.dev/docs/apps/build/payments
        type: GettingStarted
    description: The Payments Apps API enables approved Shopify Payments Partners to access their Shopify Payments account and payments app configuration data. It provides access to payment sessions and allows building custom payment processing extensions for Shopify checkout.
  - aid: shopify:ajax-api
    name: Shopify Ajax API
    tags:
      - Commerce
      - REST
      - Themes
    humanURL: https://shopify.dev/docs/api/ajax
    properties:
      - url: openapi/shopify-ajax-api-openapi.yml
        type: OpenAPI
      - url: https://shopify.dev/docs/api/ajax
        type: Documentation
      - url: https://shopify.dev/docs/api/ajax/reference
        type: Reference
    description: The Ajax API provides a suite of lightweight REST API endpoints for development of Shopify themes. It is an unauthenticated API used to add products to the cart, display product recommendations, and suggest products during search within Shopify-hosted storefronts.
  - aid: shopify:liquid-api
    name: Shopify Liquid API
    tags:
      - Commerce
      - Templates
      - Themes
    humanURL: https://shopify.dev/docs/api/liquid
    properties:
      - url: https://shopify.dev/docs/api/liquid
        type: Documentation
    description: Liquid is a template language created by Shopify and available as an open source project on GitHub. The Liquid reference documents the tags, filters, and objects that you can use to build Shopify themes and customize the storefront experience.
  - aid: shopify:functions-api
    name: Shopify Functions API
    tags:
      - Commerce
      - Serverless
      - WebAssembly
    humanURL: https://shopify.dev/docs/api/functions
    properties:
      - url: https://shopify.dev/docs/api/functions
        type: Documentation
      - url: https://shopify.dev/docs/apps/build/functions
        type: GettingStarted
    description: Shopify Functions allow developers to customize the backend logic that powers parts of Shopify. Functions are compiled to WebAssembly and enable custom discounts, payment customizations, delivery customizations, cart transforms, and order validation.
  - aid: shopify:discount-function-api
    name: Shopify Discount Function API
    tags:
      - Commerce
      - Discounts
      - Functions
    humanURL: https://shopify.dev/docs/api/functions/latest/discount
    properties:
      - url: https://shopify.dev/docs/api/functions/latest/discount
        type: Documentation
    description: The Discount Function API enables developers to create a single discount that applies to cart lines, order subtotals, and shipping rates. It replaces the previous separate Product, Order, and Shipping Discount Function APIs.
  - aid: shopify:webhooks-api
    name: Shopify Webhooks API
    tags:
      - Commerce
      - Events
      - Webhooks
    humanURL: https://shopify.dev/docs/api/webhooks
    properties:
      - url: openapi/shopify-webhooks-api-openapi.yml
        type: OpenAPI
      - url: https://shopify.dev/docs/api/webhooks
        type: Documentation
      - url: https://shopify.dev/docs/apps/build/webhooks
        type: GettingStarted
    description: Shopify webhooks enable apps to receive notifications about particular events in a shop. They are useful for keeping your app in sync with Shopify data or as a trigger to perform additional actions after events occur, providing a performant alternative to continuously polling for changes.
  - aid: shopify:app-bridge
    name: Shopify App Bridge
    tags:
      - Commerce
      - Embedded Apps
      - UI
    humanURL: https://shopify.dev/docs/api/app-bridge
    properties:
      - url: https://shopify.dev/docs/api/app-bridge
        type: Documentation
      - url: https://shopify.dev/docs/api/app-bridge-library
        type: Documentation
    description: Shopify App Bridge enables apps to render UI in the Shopify app home surface and seamlessly integrate with the Shopify admin. It provides APIs for navigation menus, save bars, title bars, toast notifications, resource pickers, and more.
  - aid: shopify:app-home-api
    name: Shopify App Home API
    tags:
      - Apps
      - Commerce
      - UI
    humanURL: https://shopify.dev/docs/api/app-home
    properties:
      - url: https://shopify.dev/docs/api/app-home
        type: Documentation
      - url: https://shopify.dev/docs/api/app-home/polaris-web-components
        type: Reference
    description: The App Home API provides the surface where apps render their main UI within the Shopify admin. It supports Polaris web components for building consistent, accessible interfaces that integrate seamlessly with the Shopify admin experience.
  - aid: shopify:checkout-ui-extensions-api
    name: Shopify Checkout UI Extensions API
    tags:
      - Checkout
      - Commerce
      - Extensions
    humanURL: https://shopify.dev/docs/api/checkout-ui-extensions
    properties:
      - url: https://shopify.dev/docs/api/checkout-ui-extensions
        type: Documentation
    description: Checkout UI extensions let app developers build custom functionality that merchants can install at defined points in the checkout flow, including product information, shipping, payment, order summary, and Shop Pay steps. Extensions for information, shipping, and payment steps are available to Shopify Plus stores.
  - aid: shopify:multipass-api
    name: Shopify Multipass API
    tags:
      - Authentication
      - Commerce
      - SSO
    humanURL: https://shopify.dev/docs/api/multipass
    properties:
      - url: openapi/shopify-multipass-api-openapi.yml
        type: OpenAPI
      - url: https://shopify.dev/docs/api/multipass
        type: Documentation
    description: Multipass login is for store owners who have a separate website and a Shopify store, enabling seamless single sign-on by redirecting users and automatically logging them in. Requires a Shopify Plus plan. Tokens are valid for 15 minutes and can only be used once.
  - aid: shopify:pos-ui-extensions-api
    name: Shopify POS UI Extensions API
    tags:
      - Commerce
      - Extensions
      - Point of Sale
    humanURL: https://shopify.dev/docs/api/pos-ui-extensions
    properties:
      - url: https://shopify.dev/docs/api/pos-ui-extensions
        type: Documentation
      - url: https://shopify.dev/docs/apps/build/pos
        type: Getting Started
    description: POS UI extensions enable app developers to build custom functionality for Shopify Point of Sale. Extensions can add functionality to the cart, post- purchase, and other POS surfaces for in-person retail experiences.
  - aid: shopify:admin-extensions-api
    name: Shopify Admin Extensions API
    tags:
      - Admin
      - Commerce
      - Extensions
    humanURL: https://shopify.dev/docs/api/admin-extensions
    properties:
      - url: https://shopify.dev/docs/api/admin-extensions
        type: Documentation
      - url: https://shopify.dev/docs/apps/build/admin
        type: Getting Started
    description: Admin UI extensions allow developers to extend the Shopify admin with custom UI components. Extensions can render in product details, order details, customer details, and other admin surfaces.
  - aid: shopify:hydrogen
    name: Shopify Hydrogen
    tags:
      - Commerce
      - Framework
      - Headless
      - React
    humanURL: https://shopify.dev/docs/storefronts/headless/hydrogen
    properties:
      - url: https://shopify.dev/docs/storefronts/headless/hydrogen
        type: Documentation
      - url: https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started
        type: Getting Started
    description: Hydrogen is Shopify's React-based framework for building custom storefronts powered by the Storefront API. It provides commerce-optimized components, hooks, and utilities for building fast, dynamic headless commerce experiences.
  - aid: shopify:polaris
    name: Shopify Polaris
    tags:
      - Commerce
      - Components
      - Design System
      - UI
    humanURL: https://shopify.dev/docs/api/polaris
    properties:
      - url: https://shopify.dev/docs/api/polaris
        type: Documentation
      - url: https://shopify.dev/docs/apps/design
        type: Reference
    description: Polaris is Shopify's unified UI framework built on web components for delivering a consistent experience across the platform. It provides a library of UI components, tokens, and icons that developers use to build app interfaces that match the Shopify admin design system.
  - aid: shopify:shopify-cli
    name: Shopify CLI
    tags:
      - CLI
      - Commerce
      - Development Tools
    humanURL: https://shopify.dev/docs/api/shopify-cli
    properties:
      - url: https://shopify.dev/docs/api/shopify-cli
        type: Documentation
    description: Shopify CLI is a command-line tool that helps developers create Shopify apps, themes, and custom storefronts. It accelerates development with scaffolding, local development servers, and deployment tools.
name: Shopify
tags:
  - Commerce
  - Ecommerce
  - Payments
  - Retail
  - Shopping Cart
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://shopify.dev/docs
    name: Shopify developer documentation
    type: Documentation
    description: 'null'
  - url: https://shopify.dev/docs/api/usage/versioning
    name: About Shopify API versioning
    type: Versioning
    description: 'null'
  - url: https://shopify.dev/docs/api/usage/authentication
    name: Shopify API authentication
    type: Authentication
    description: 'null'
  - url: https://shopify.dev/docs/api/shopify-cli
    name: Shopify CLI
    type: CLI
    description: 'null'
  - url: https://shopify.dev/docs/api
    name: Shopify API, libraries, and tools
    type: Documentation
    description: 'null'
  - url: https://shopify.dev
    type: Portal
  - url: https://shopify.dev/docs/api/admin-rest/resources/sdk
    type: SDKs
  - url: https://shopify.dev/docs/api/usage/rate-limits
    type: Rate Limits
  - url: https://shopify.dev/changelog
    type: Changelog
  - url: https://shopify.dev/docs/api/usage/versioning
    type: API Versioning
  - url: https://www.shopifystatus.com
    type: Status
  - url: https://shopify.dev/docs/api/usage/support
    type: Support
  - url: https://www.shopify.com/legal/api-terms
    type: Terms of Service
  - url: https://www.shopify.com/legal/privacy
    type: Privacy Policy
  - url: https://partners.shopify.com/signup
    type: SignUp
  - url: https://shopify.dev/docs/apps/build/webhooks
    type: Webhooks
  - url: https://shopify.dev/docs/apps/build/authentication-authorization
    type: Security
  - url: https://shopify.dev/docs/api/usage/access-scopes
    type: Access Scopes
  - url: https://community.shopify.dev/
    type: Forum
  - url: https://github.com/Shopify
    type: GitHub Organization
  - url: https://shopify.engineering/
    type: Blog
  - url: https://shopify.dev/docs/storefronts/headless
    type: Headless
  - url: https://shopify.dev/docs/api/polaris
    type: Design System
  - url: https://shopify.dev/docs/api/app-bridge
    type: App Bridge
  - url: https://apps.shopify.com
    type: Application Marketplace
  - url: https://www.shopify.com/partners
    type: Partner Program
  - url: https://www.youtube.com/@shopifydevs
    type: YouTube
  - url: https://shopify.dev/docs/apps/build
    type: Getting Started
  - url: https://shopify.dev/docs/apps/build/app-extensions
    type: Extensions
  - url: https://shopify.dev/docs/themes
    type: Themes
  - url: https://stackoverflow.com/questions/tagged/shopify
    type: Stack Overflow
  - url: https://www.shopify.com
    type: Website
  - url: https://accounts.shopify.com
    type: Login
  - url: https://community.shopify.dev/
    type: Community
  - url: https://shopify.dev/docs/api/release-notes
    type: Change Log
  - url: https://github.com/Shopify/shopify-app-js
    type: SDKs
  - url: https://shopify.dev/docs/storefronts/headless/additional-sdks
    type: SDKs
  - type: Features
    data:
      - REST Admin API with leaky-bucket throttling (40 req/app/store)
      - GraphQL Admin API with cost-based throttling (1,000 pts on Standard, 2,000 on Plus)
      - Storefront API for headless commerce
      - 'Plans: Basic ($29), Grow ($79), Advanced ($299), Plus ($2,300)'
      - Online card transaction fees from 2.25% (Plus) to 2.9% (Basic)
      - Third-party gateway fees from 0% (Plus) to 2% (Basic)
      - AI assistant for commerce included on all plans
      - Up to 200 POS Pro locations on Plus
      - B2B / wholesale on Plus
      - Customizable checkout on Plus
      - Bulk operations for large data exports without rate-limit hits
      - Webhooks for order, customer, inventory, and product events
      - OAuth 2.0 app authentication
      - Shopify Functions for backend customization
      - Shopify Markets for region-specific currencies and pricing
    sources:
      - https://www.shopify.com/pricing
    updated: '2026-05-04'
created: '2024-04-14'
modified: '2026-05-04'
position: Consuming
description: Shopify is a complete commerce platform that lets you start, grow, and manage a business. The Shopify API lets you build apps and integrations that extend Shopify functionality for merchants.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - name: Shopify
    email: api@shopify.com
    url: https://www.shopify.com
specificationVersion: '0.19'
image: https://cdn.shopify.com/shopifycloud/brochure/assets/brand-assets/shopify-logo.png
---
