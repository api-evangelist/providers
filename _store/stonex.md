---
aid: stonex
name: StoneX
description: StoneX Group is a global financial services organization that provides execution, risk management, market intelligence, and post-trade services across asset classes and markets to institutional, commercial, and retail clients. StoneX offers REST APIs for payments, clearing, and futures trading with OAuth 2.0 authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Financial Services
  - Payments
  - Clearing
  - Futures
  - Trading
  - Risk Management
url: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stonex:stonex-payments
    name: StoneX Payments API
    description: The StoneX Payments REST API enables cross-border payment processing in 140+ currencies with local currency acceptance and settlement. Uses Bearer token authentication over HTTPS with TLS 1.3. Available in sandbox and production environments.
    humanURL: https://docs.payments.stonex.io/
    tags:
      - Payments
      - Cross-Border Payments
      - FX
      - REST
    properties:
      - type: Documentation
        url: https://docs.payments.stonex.io/
      - type: Getting Started
        url: https://docs.payments.stonex.io/docs/quickstart-guide-1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/openapi/stonex-payments-openapi.yml
  - aid: stonex:stonex-clearing
    name: StoneX Clearing API
    description: The StoneX Clearing REST API provides programmatic access to accounts, trading, and document management for clearing clients. Supports OAuth 2.0 authentication with JWT tokens. Available in UAT (api.clearing.uat.stonex.com) and production (api.clearing.stonex.com).
    humanURL: https://docs.clearing.stonex.com/
    tags:
      - Clearing
      - Trading
      - Accounts
      - REST
    properties:
      - type: Documentation
        url: https://docs.clearing.stonex.com/docs
      - type: Getting Started
        url: https://docs.clearing.stonex.com/docs/getting-started/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/openapi/stonex-clearing-openapi.yml
  - aid: stonex:stonex-gf-api
    name: StoneX GF Futures API
    description: The StoneX GF (GAIN Futures) API provides institutional-grade access to futures trading including market data, order management, account and position tracking, margin calculations, contract lookup, and real-time price feeds for futures contracts.
    humanURL: https://futures-media.stonex.com/gfapi/index.html
    tags:
      - Futures
      - Trading
      - Market Data
      - Institutional
    properties:
      - type: Documentation
        url: https://futures-media.stonex.com/gfapi/index.html
  - aid: stonex:stonex-developer-portal
    name: StoneX Developer Portal
    description: The StoneX Developer Storefront provides access to all StoneX API products with subscription keys, documentation, and developer resources for integrating with StoneX financial services.
    humanURL: https://developer.stonex.com/
    tags:
      - Developer Portal
      - API Management
    properties:
      - type: Documentation
        url: https://developer.stonex.com/documentation
      - type: Products
        url: https://developer.stonex.com/products
common:
  - type: Website
    url: https://www.stonex.com
  - type: Developer Portal
    url: https://developer.stonex.com/
  - type: Documentation
    url: https://developer.stonex.com/documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
