---
aid: block
url: https://raw.githubusercontent.com/api-evangelist/block/refs/heads/main/apis.yml
name: Block
description: Block, Inc. is a global technology company building economic empowerment tools through a family of products including Square (commerce and payments), Cash App (personal finance and investing), Afterpay (buy now pay later), TIDAL (music streaming), and Spiral (open-source Bitcoin development). The Square API enables developers to build commerce applications with payment processing, order management, catalog, customer engagement, and business operations capabilities.
tags:
  - Commerce
  - Cryptocurrency
  - eCommerce
  - Fintech
  - Payments
  - Point Of Sale
  - Square
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-09-27'
modified: '2026-04-19'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: block:block-square-api
    name: Square API
    description: RESTful API for building commerce applications on the Square platform. Provides payment processing, order management, catalog management, customer profiles, loyalty programs, invoicing, and merchant operations. Supports OAuth 2.0 and personal access token authentication. Available in sandbox and production environments.
    humanURL: https://developer.squareup.com/
    tags:
      - Commerce
      - eCommerce
      - Payments
      - Point Of Sale
      - Square
    properties:
      - type: Documentation
        url: https://developer.squareup.com/docs
      - type: OpenAPI
        url: openapi/block-square-api-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/block-square-commerce.yaml
      - type: SpectralRules
        url: rules/block-spectral-rules.yml
      - type: Vocabulary
        url: vocabulary/block-vocabulary.yaml
common:
  - type: Website
    url: https://www.block.xyz
  - type: Documentation
    url: https://developer.squareup.com/docs
  - type: GettingStarted
    url: https://developer.squareup.com/docs/get-started
  - type: Pricing
    url: https://squareup.com/us/en/payments/our-rates
  - type: StatusPage
    url: https://www.issquareup.com/
  - type: Support
    url: https://developer.squareup.com/forums
  - type: GitHubOrganization
    url: https://github.com/square
  - type: TermsOfService
    url: https://squareup.com/us/en/legal/developer
  - type: PrivacyPolicy
    url: https://squareup.com/us/en/legal/privacy
  - type: Login
    url: https://developer.squareup.com/apps
  - type: SDK
    url: https://developer.squareup.com/docs/sdks
    title: Square SDKs
  - type: SpectralRules
    url: rules/block-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/block-square-commerce.yaml
  - type: Vocabulary
    url: vocabulary/block-vocabulary.yaml
  - type: Features
    data:
      - name: Payment Processing
        description: Accept card-present and card-not-present payments using Square hardware, web, or mobile SDKs with OAuth 2.0 or access token authentication.
      - name: Order Management
        description: Create, update, and fulfill orders with line items, discounts, taxes, and service charges across online and in-person channels.
      - name: Catalog Management
        description: Manage a unified product catalog with items, variations, modifiers, categories, taxes, and discounts synchronized across all locations.
      - name: Customer Engagement
        description: Build customer profiles, loyalty programs, gift cards, and marketing campaigns to drive repeat business and customer retention.
      - name: Multi-Location Support
        description: Manage multiple business locations with location-specific inventory, pricing, staff permissions, and reporting.
      - name: Webhook Events
        description: Subscribe to real-time webhook events for payments, orders, inventory changes, customer activity, and subscription lifecycle events.
      - name: Sandbox Environment
        description: Full sandbox environment with test card numbers, merchant accounts, and simulated hardware for development and testing.
  - type: UseCases
    data:
      - name: Point of Sale Integration
        description: Retailers and restaurants build custom POS applications using Square's payment, catalog, and order APIs.
      - name: eCommerce Checkout
        description: Online stores integrate Square's Web Payments SDK and Orders API to accept payments and manage fulfillment.
      - name: Marketplace Payments
        description: Multi-seller marketplaces use Square Connect to route payments to sellers and manage fees through the Payouts API.
      - name: Subscription Billing
        description: SaaS and service businesses use Square Subscriptions API for automated recurring billing and invoice management.
      - name: Loyalty and Rewards
        description: Businesses implement custom loyalty programs using the Loyalty API to track points, tiers, and reward redemptions.
  - type: Integrations
    data:
      - name: WooCommerce
        description: Official Square extension for WooCommerce synchronizes inventory, products, and payments between WordPress stores and Square.
      - name: BigCommerce
        description: Square integration for BigCommerce enables omnichannel selling with synchronized catalog and unified payment processing.
      - name: Xero
        description: Square-Xero integration automatically syncs sales transactions and payments to Xero accounting for reconciliation.
      - name: QuickBooks
        description: Square connector for QuickBooks Online syncs sales, refunds, and fees to QuickBooks for financial reporting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
