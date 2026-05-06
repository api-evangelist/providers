---
aid: td-ameritrade-holding
name: TD Ameritrade Holding
description: TD Ameritrade Holding Corporation was a brokerage firm that provided online brokerage and related services for individual investors. The company was acquired by Charles Schwab in 2020 and the TD Ameritrade platform was fully migrated to Charles Schwab in May 2024. TD Ameritrade offered a developer API for programmatic access to trading, account management, market data, and order management capabilities. The successor API is now the Charles Schwab Trader API at developer.schwab.com.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Brokerage
  - Trading
  - Market Data
  - Investment
  - Charles Schwab
  - Deprecated
created: '2026-03-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: td-ameritrade-holding:accounts-and-trading
    name: TD Ameritrade Accounts and Trading API
    description: The TD Ameritrade Accounts and Trading API provided programmatic access to account information, order management, watchlists, market data, and trading operations. Supported OAuth 2.0 authentication. Deprecated following the Charles Schwab acquisition with full migration completed in May 2024. The successor API is the Charles Schwab Trader API at developer.schwab.com.
    humanURL: https://developer.tdameritrade.com/
    baseURL: https://api.tdameritrade.com/v1
    tags:
      - Accounts
      - Trading
      - Orders
      - Market Data
      - Watchlists
    properties:
      - type: Documentation
        url: https://developer.tdameritrade.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/openapi/td-ameritrade-accounts-trading-openapi.yml
    contact:
      - FN: Charles Schwab (Successor)
        url: https://developer.schwab.com
common:
  - type: Website
    url: https://www.tdameritrade.com
  - type: Documentation
    name: TD Ameritrade Developer Portal (Archived)
    description: Original developer portal, now redirecting to Schwab.
    url: https://developer.tdameritrade.com/
  - type: Documentation
    name: Charles Schwab Trader API (Successor)
    description: The successor API following TD Ameritrade acquisition by Charles Schwab.
    url: https://developer.schwab.com
  - type: OpenAPI
    name: TD Ameritrade Accounts and Trading OpenAPI Specification
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/openapi/td-ameritrade-accounts-trading-openapi.yml
  - type: Vocabulary
    name: TD Ameritrade Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/vocabulary/td-ameritrade-vocabulary.yml
  - type: JSONSchema
    name: Order Schema
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/json-schema/td-ameritrade-order-schema.json
  - type: JSONLDContext
    name: TD Ameritrade JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/json-ld/td-ameritrade-context.jsonld
  - type: SpectralRules
    name: TD Ameritrade Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/rules/td-ameritrade-rules.yml
  - type: NaftikoCapabilities
    name: TD Ameritrade Trading and Portfolio Capability
    url: https://raw.githubusercontent.com/api-evangelist/td-ameritrade-holding/refs/heads/main/capabilities/trading-and-portfolio.yaml
  - type: Authentication
    name: OAuth 2.0
    description: TD Ameritrade API used OAuth 2.0 token-based authentication.
    url: https://api.tdameritrade.com/v1/oauth2/token
features:
  - name: Account Management
    description: Access account balances, positions, and account-level information.
  - name: Order Management
    description: Place, modify, cancel, and retrieve orders for brokerage accounts.
  - name: Watchlist Management
    description: Create, update, and manage stock and security watchlists.
  - name: Market Data
    description: Access real-time and historical market data, quotes, and price history.
  - name: Options Chain
    description: Retrieve option chains for optionable symbols.
  - name: Instrument Search
    description: Search for securities by symbol, CUSIP, or fundamental data.
  - name: Transaction History
    description: Access account transaction history and activity.
  - name: Market Hours
    description: Query market hours and status for different exchanges.
  - name: Market Movers
    description: Retrieve top movers by value or percentage for market indices.
  - name: OAuth 2.0 Authentication
    description: Secure API access via OAuth 2.0 with offline access for refresh tokens.
useCases:
  - name: Automated Trading
    description: Build automated trading systems using order placement and market data APIs.
  - name: Portfolio Monitoring
    description: Track account balances, positions, and performance programmatically.
  - name: Market Data Integration
    description: Pull quotes and price history into custom analytics platforms.
  - name: Options Trading
    description: Access option chains for options strategy automation.
  - name: Watchlist Automation
    description: Programmatically manage and update stock watchlists.
integrations:
  - name: Charles Schwab Trader API
    description: Successor API following acquisition and migration completion in May 2024.
    url: https://developer.schwab.com
solutions:
  - name: Retail Brokerage Automation
    description: Enabled retail investors to automate trading and account management workflows.
  - name: Algorithmic Trading
    description: Supported quantitative and algorithmic trading through market data and order APIs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
