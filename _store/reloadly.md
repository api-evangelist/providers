---
aid: reloadly
name: Reloadly
description: Reloadly is a global digital rewards and payments platform providing APIs for sending digital gift cards, airtime top-ups, and data bundles worldwide. The platform connects businesses to 3,000+ gift card brands across 14,000+ products in 140+ countries and 800+ mobile operators in 170+ countries. Reloadly's REST APIs use OAuth 2.0 client credentials authentication with separate sandbox and production environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Gift Cards
  - Payments
  - Airtime
  - Mobile Top-Up
  - Rewards
  - Incentives
url: https://raw.githubusercontent.com/api-evangelist/reloadly/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reloadly:gift-cards
    name: Reloadly Gift Cards API
    description: Order and manage digital gift cards across 3,000+ global brands including Amazon, Apple, Netflix, Spotify, and Uber. Supports 14,000+ products in 140+ countries with multi-currency payouts and real-time fulfillment.
    humanURL: https://www.reloadly.com/products/gift-card-api
    baseURL: https://giftcards.reloadly.com
    tags:
      - Gift Cards
      - Rewards
      - Payments
    properties:
      - type: Documentation
        url: https://docs.reloadly.com/gift-cards
      - type: OpenAPI
        url: openapi/reloadly-gift-cards-openapi.yml
      - type: Authentication
        url: https://docs.reloadly.com/gift-cards/tag/Authentication
  - aid: reloadly:airtime
    name: Reloadly Airtime API
    description: Send mobile airtime top-ups and data bundles to phones across 170+ countries and 800+ mobile operators. Supports auto-detection of mobile operators from phone numbers with real-time fulfillment and FX conversion.
    humanURL: https://www.reloadly.com/products/airtime-api
    baseURL: https://topups.reloadly.com
    tags:
      - Airtime
      - Mobile Top-Up
      - Data Bundles
    properties:
      - type: Documentation
        url: https://docs.reloadly.com/airtime
      - type: OpenAPI
        url: openapi/reloadly-airtime-openapi.yml
common:
  - type: Website
    url: https://www.reloadly.com
  - type: Documentation
    url: https://docs.reloadly.com
  - type: Authentication
    url: https://auth.reloadly.com/oauth/token
  - type: Dashboard
    url: https://dashboard.reloadly.com
  - type: GitHub Organization
    url: https://github.com/reloadly
  - type: Support
    url: https://support.reloadly.com
  - type: Pricing
    url: https://www.reloadly.com/pricing
  - type: Sign Up
    url: https://www.reloadly.com/register
  - type: LinkedIn
    url: https://www.linkedin.com/company/reloadly
  - type: Twitter
    url: https://twitter.com/reloadly
features:
  - name: OAuth 2.0 Authentication
    description: Client credentials grant with separate sandbox and production tokens
  - name: Sandbox Environment
    description: Full sandbox for development with test credentials
  - name: Multi-Currency Support
    description: Payouts in USD, EUR, CAD, and GBP
  - name: Real-Time Fulfillment
    description: Instant gift card delivery and airtime top-up processing
  - name: Global Coverage
    description: Gift cards in 140+ countries, airtime in 170+ countries
  - name: SDK Support
    description: Official SDKs for Node.js, PHP, Python, Go, Java, C#
solutions:
  - name: Employee Rewards
    description: Send digital gift cards as employee recognition rewards and incentives across a global distributed workforce.
  - name: Customer Loyalty Programs
    description: Power loyalty point redemption with instant digital gift card delivery to customers in 140+ countries.
  - name: Crypto Exchange Utilities
    description: Enable cryptocurrency holders to convert digital assets to airtime or gift cards for real-world utility.
  - name: Remittance Alternatives
    description: Provide mobile airtime top-ups as a remittance alternative for supporting family members in emerging markets.
  - name: Bulk Gifting Campaigns
    description: Run large-scale gifting campaigns with bulk gift card orders for marketing, promotions, and B2B incentive programs.
useCases:
  - name: Gift Card Order Automation
    description: Automate gift card delivery for loyalty programs, employee rewards, and customer promotions via REST API.
  - name: Airtime Top-Up Service
    description: Build mobile wallet applications or remittance services that send airtime top-ups to phones worldwide.
  - name: Digital Rewards Platform
    description: Integrate Reloadly into an existing rewards platform to offer global gift card and airtime redemption options.
integrations:
  - name: WordPress Plugin
    description: Gift card integration for WordPress e-commerce sites
  - name: Shopify Plugin
    description: Gift card integration for Shopify stores
  - name: WooCommerce Plugin
    description: Gift card integration for WooCommerce-powered stores
  - name: Node.js SDK
    description: Official Node.js client library
  - name: PHP SDK
    description: Official PHP client library
  - name: Python SDK
    description: Official Python client library
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
