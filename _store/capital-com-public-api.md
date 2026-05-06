---
aid: capital-com-public-api
url: https://raw.githubusercontent.com/api-evangelist/capital-com-public-api/refs/heads/main/apis.yml
name: Capital.com Public API
description: Capital.com is a European trading platform offering CFDs across shares, indices, commodities, forex, and cryptocurrencies. The Capital.com Public API provides direct access to the trading engine for automated strategies, giving programmatic control of positions, working orders, account preferences, and historical and streaming market data. A companion WebSocket API streams real-time prices and OHLC candles for up to 40 concurrent instruments.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CFD
  - Commodities
  - Cryptocurrency
  - Financial
  - Forex
  - Indices
  - Market Data
  - Shares
  - Streaming
  - Trading
  - WebSocket
created: '2024-12-03'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: capital-com-public-api:capital-com-rest-api
    name: Capital.com REST API
    description: The Capital.com REST API provides programmatic access to positions, working orders, deal confirmations, account information, account switching, transaction history, preferences (leverage, hedging mode), market navigation, instrument details, historical prices, watchlists, and client sentiment data. Authentication uses an API key plus login credentials to create a session that returns CST and X-SECURITY-TOKEN headers, which expire after 10 minutes of inactivity.
    humanURL: https://open-api.capital.com
    tags:
      - CFD
      - Financial
      - Market Data
      - Trading
    properties:
      - type: Documentation
        url: https://open-api.capital.com
      - type: Base URL
        url: https://api-capital.backend-capital.com/
      - type: Sandbox
        url: https://demo-api-capital.backend-capital.com/
      - type: Authentication
        url: https://open-api.capital.com
    x-features:
      - Session-based authentication with CST and X-SECURITY-TOKEN
      - API key plus login credentials to create sessions
      - 10-minute inactivity session expiry
      - Position management (open, update, close)
      - Working orders (limit and stop)
      - Deal confirmations and execution tracking
      - Account switching across multiple accounts
      - Transaction and activity history
      - Leverage and hedging-mode preferences
      - Demo account balance adjustment for testing
      - Market navigation hierarchy
      - Instrument details and search
      - Historical price data (OHLC)
      - Client sentiment data
      - Watchlist management
    x-use-cases:
      - Building automated CFD trading strategies
      - Algorithmic execution across shares, forex, commodities, indices, and crypto
      - Copy-trading and signal-provider applications
      - Portfolio and risk dashboards
      - Backtesting against historical price data
      - Sentiment-driven trading signals
      - Demo-account integration testing before going live
  - aid: capital-com-public-api:capital-com-websocket-api
    name: Capital.com WebSocket API
    description: The Capital.com WebSocket API streams real-time market data, supporting up to 40 concurrent instruments and OHLC candlestick subscriptions for low-latency trading applications.
    humanURL: https://open-api.capital.com
    tags:
      - Market Data
      - Streaming
      - Trading
      - WebSocket
    properties:
      - type: Documentation
        url: https://open-api.capital.com
    x-features:
      - Real-time price streaming via WebSocket
      - Up to 40 concurrent instrument subscriptions
      - OHLC candlestick streaming
      - Low-latency market data for trading systems
    x-use-cases:
      - Low-latency automated trading execution
      - Real-time market dashboards
      - Streaming-data backtesting and replay
common:
  - type: Website
    url: https://capital.com/
  - type: Documentation
    url: https://open-api.capital.com
  - type: Sandbox
    url: https://demo-api-capital.backend-capital.com/
  - type: Privacy Policy
    url: https://capital.com/privacy-policy
  - type: Terms of Service
    url: https://capital.com/terms-and-conditions
  - type: Support
    url: https://capital.com/help
  - type: Blog
    url: https://capital.com/news-and-analysis
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
