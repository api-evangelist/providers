---
aid: charles-schwab
name: Charles Schwab
description: Charles Schwab is a financial services company providing brokerage, banking, asset management, and financial advisory services to individual investors and independent investment advisors. The Schwab Developer Portal exposes Trader APIs that let registered applications access account balances, positions, and orders, place equity and option trades, and consume real-time and historical market data through OAuth 2.0-secured REST endpoints.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/charles-schwab/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Accounts
  - Banking
  - Brokerage
  - Financial Services
  - Investing
  - Market Data
  - OAuth 2.0
  - Orders
  - Trading
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: charles-schwab:trader-api
    name: Charles Schwab Trader API
    description: The Schwab Trader API provides authenticated access to retail brokerage accounts. Applications can list linked accounts, retrieve balances and positions, fetch and cancel orders, place new orders for equities and options, retrieve transactions, and stream account activity.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.schwab.com/products/trader-api--individual
    baseURL: https://api.schwabapi.com/trader/v1
    tags:
      - Accounts
      - Brokerage
      - Orders
      - Trading
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.schwab.com/products/trader-api--individual
      - type: GettingStarted
        url: https://developer.schwab.com/user-guides/get-started
      - type: Authentication
        url: https://developer.schwab.com/user-guides/get-started/authenticate-with-oauth
      - type: OpenAPI
        url: openapi/charles-schwab-trader-api-openapi.yml
      - type: Spectral
        url: spectral/charles-schwab-spectral.yml
  - aid: charles-schwab:market-data-api
    name: Charles Schwab Market Data API
    description: The Schwab Market Data API exposes real-time and historical quotes, option chains, price history, market hours, instrument metadata, and daily movers for the major US indices, supporting market analytics and trading decision tools.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.schwab.com/products/trader-api--individual
    baseURL: https://api.schwabapi.com/marketdata/v1
    tags:
      - Equities
      - Market Data
      - Options
      - Quotes
    properties:
      - type: Documentation
        url: https://developer.schwab.com/products/trader-api--individual
      - type: Authentication
        url: https://developer.schwab.com/user-guides/get-started/authenticate-with-oauth
      - type: OpenAPI
        url: openapi/charles-schwab-market-data-api-openapi.yml
common:
  - type: Website
    url: https://www.schwab.com
  - type: DeveloperPortal
    url: https://developer.schwab.com/
  - type: Documentation
    url: https://developer.schwab.com/user-guides
  - type: Authentication
    url: https://developer.schwab.com/user-guides/get-started/authenticate-with-oauth
  - type: SignUp
    url: https://developer.schwab.com/register
  - type: Dashboard
    url: https://developer.schwab.com/dashboard
  - type: Support
    url: https://developer.schwab.com/contact-us
  - type: TermsOfService
    url: https://developer.schwab.com/terms
  - type: PrivacyPolicy
    url: https://www.schwab.com/legal/online-privacy
  - type: JSONLD
    url: json-ld/charles-schwab-context.jsonld
  - type: JSONSchema
    url: json-schema/charles-schwab-account-schema.json
  - type: JSONSchema
    url: json-schema/charles-schwab-order-schema.json
  - type: JSONSchema
    url: json-schema/charles-schwab-quote-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
