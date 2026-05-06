---
aid: coinapi
url: https://raw.githubusercontent.com/api-evangelist/coinapi/refs/heads/main/apis.yml
name: CoinAPI
tags:
  - Blockchain
  - Crypto Indexes
  - Crypto Metrics
  - Cryptocurrency
  - EMS
  - Execution Management
  - FIX
  - Market Data
  - Order Books
  - REST
  - WebSocket
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
description: CoinAPI is a financial data and execution platform delivering normalized real-time and historical cryptocurrency market data and trade execution across more than 350 exchanges. Its product family covers a Market Data API (REST, WebSocket, FIX, and flat-file S3 delivery) for trades, quotes, order books, OHLCV, exchange rates, and derivatives metrics; an EMS Trading API (Execution Management System) that lets users place, manage, and route orders across multiple venues through one normalized REST/WebSocket/FIX interface; and Index and Metrics APIs that aggregate cross-exchange data into reference indexes and risk metrics. FIX endpoints (fix.coinapi.io) use GeoDNS to route to the nearest datacenter for low-latency connectivity.
apis:
  - aid: coinapi:market-data-api
    name: CoinAPI Market Data API
    tags:
      - Crypto Metrics
      - Cryptocurrency
      - Exchange Rates
      - FIX
      - Market Data
      - OHLCV
      - Order Books
      - REST
      - WebSocket
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://rest.coinapi.io
    humanURL: https://www.coinapi.io/products/market-data-api
    properties:
      - url: https://docs.coinapi.io/market-data/
        type: Documentation
      - url: https://www.coinapi.io/products/market-data-api
        type: Landing Page
      - url: https://www.coinapi.io/products/market-data-api/faq
        type: FAQ
      - url: https://www.coinapi.io/products/market-data-api/docs/fix
        type: FIX Documentation
    description: Normalized cryptocurrency market data covering more than 350 exchanges and 28,000+ assets. Provides trades, quotes, order books, OHLCV time series, exchange rates, and derivatives metrics (funding rates, mark prices, liquidations, open interest, volumes). Delivered through REST for historical snapshots and lookups, WebSocket and FIX for real-time streaming, and S3 flat files for bulk historical analysis.
    x-features:
      - REST, WebSocket, and FIX delivery channels
      - S3 flat-file delivery for historical bulk data
      - Normalized symbol IDs across all exchanges
      - 350+ supported exchanges and 28,000+ assets
      - Derivatives metrics (funding, mark prices, OI, liquidations)
      - GeoDNS-routed FIX endpoints (fix.coinapi.io)
      - API-key authentication via X-CoinAPI-Key header
    x-use-cases:
      - Power trading dashboards with live order book data
      - Backtest strategies against full historical OHLCV
      - Compute reference rates from cross-exchange quotes
      - Monitor derivatives exposure (funding, OI) in real time
      - Feed BI/data lakes via daily S3 flat-file drops
  - aid: coinapi:ems-trading-api
    name: CoinAPI EMS Trading API
    tags:
      - Cryptocurrency
      - EMS
      - Execution Management
      - FIX
      - Order Management
      - REST
      - Trading
      - WebSocket
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.coinapi.io/products/ems-api
    properties:
      - url: https://www.coinapi.io/products/ems-api
        type: Landing Page
      - url: https://www.coinapi.io/products/ems-api/faq
        type: FAQ
      - url: https://www.coinapi.io/blog/maximize-trading-potential-ems-trading-api-guide
        type: Guide
    description: CoinAPI's Execution Management System (EMS) is a unified, multi-exchange crypto trading API that lets institutional traders, market makers, and builders place, modify, and cancel orders across many connected venues from a single normalized interface. Available over REST, WebSocket, and FIX, the EMS handles credential vaulting, order routing, position and balance retrieval, and execution reporting.
    x-features:
      - Single normalized order schema across many exchanges
      - REST, WebSocket, and FIX support
      - Credential vault for per-exchange API keys
      - Real-time order, fill, and position updates
      - Suitable for high-frequency and algorithmic strategies
    x-use-cases:
      - Aggregate liquidity across exchanges in a single trading client
      - Run smart-order-routing or arbitrage strategies
      - Centralize execution reporting and TCA across venues
      - Bridge legacy FIX trading systems to crypto markets
  - aid: coinapi:indexes-api
    name: CoinAPI Indexes API
    tags:
      - Aggregation
      - Benchmark
      - Cryptocurrency
      - Indexes
      - Reference Rates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.coinapi.io/products/indexes-api
    properties:
      - url: https://www.coinapi.io/products/indexes-api
        type: Landing Page
      - url: https://docs.coinapi.io/
        type: Documentation
    description: The Indexes API aggregates data from many exchanges to compute reference rates and benchmark indexes that summarize broad market conditions for a given asset. Useful for derivatives settlement, NAV computation, and research where a single, defensible price point is required across a fragmented market.
    x-features:
      - Cross-exchange aggregation methodology
      - Reference rates suitable for benchmarking and settlement
      - Real-time and historical index values
    x-use-cases:
      - Settle derivatives contracts against a defensible reference rate
      - Compute fund NAV and accounting marks
      - Provide retail apps with a single representative price
common:
  - type: Website
    url: https://www.coinapi.io/
  - type: Documentation
    url: https://docs.coinapi.io/
  - type: Pricing
    url: https://www.coinapi.io/pricing
  - type: Changelog
    url: https://docs.coinapi.io/general/changelog/
  - type: Status
    url: https://status.coinapi.io/
  - type: GitHub
    url: https://github.com/coinapi
  - type: Blog
    url: https://www.coinapi.io/blog
  - type: Privacy Policy
    url: https://www.coinapi.io/privacy-policy
  - type: Terms of Service
    url: https://www.coinapi.io/terms-of-service
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
