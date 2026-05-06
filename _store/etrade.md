---
aid: etrade
name: Etrade
description: E*TRADE is an online brokerage firm that provides a platform for investors to trade stocks, options, futures, and bonds. The E*TRADE Developer Platform offers REST APIs for account management, real-time quotes, option chains, and order placement, secured by OAuth 1.0a. The APIs are available to E*TRADE customers who register through the developer portal and provide both a sandbox and production environment.
url: https://raw.githubusercontent.com/api-evangelist/etrade/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Bonds
  - Brokerage
  - Financial
  - Futures
  - Options
  - Stocks
  - Trading
apis:
  - aid: etrade:etrade
    name: E*TRADE API
    description: The E*TRADE REST API gives developers programmatic access to account lists, balances, portfolios, transactions, market quotes, option chains, and order placement. Authentication uses OAuth 1.0a with separate sandbox and production hosts.
    humanURL: https://developer.etrade.com/home
    baseURL: https://api.etrade.com/v1
    tags:
      - Bonds
      - Brokerage
      - Financial
      - Futures
      - Options
      - Stocks
      - Trading
    properties:
      - url: https://developer.etrade.com/home
        type: Documentation
      - url: https://developer.etrade.com/getting-started
        type: Getting Started
      - url: https://developer.etrade.com/home
        type: SignUp
      - url: openapi/etrade-openapi.yml
        type: OpenAPI
common:
  - url: https://us.etrade.com/
    type: Portal
  - url: https://developer.etrade.com/home
    type: Documentation
  - url: https://developer.etrade.com/home
    type: SignUp
  - url: https://us.etrade.com/etx/sd/legaldoc/customer-agreements
    type: Terms of Service
  - url: https://us.etrade.com/l/f/privacy/security-center
    type: Privacy Policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
