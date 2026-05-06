---
aid: tradestation
name: TradeStation
description: TradeStation is a financial brokerage and trading platform offering a collection of RESTful brokerage and market data services for building trading applications for stocks, options, futures, and cryptocurrency. The API provides endpoints for account management, order placement and execution, real-time and historical market data, option chains, symbol information, and HTTP streaming for live market feeds. TradeStation supports advanced order types including bracket, OCO, OSO, and multi-leg options orders with OAuth2 authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Brokerage
  - Cryptocurrency
  - Finance
  - Futures
  - Market Data
  - Options
  - Stocks
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/tradestation/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tradestation:tradestation-api
    name: TradeStation API
    description: The TradeStation REST API provides brokerage and market data services for building trading applications. Covers account management, order placement and execution, real-time and historical market data, option chains, symbol information, and reference data. Supports stocks, options, futures, and cryptocurrency with OAuth2 authentication.
    humanURL: https://api.tradestation.com/docs/
    baseURL: https://api.tradestation.com
    tags:
      - Accounts
      - Brokerage
      - Cryptocurrency
      - Market Data
      - Options
      - Order Execution
      - Stocks
      - Trading
    properties:
      - type: Documentation
        url: https://api.tradestation.com/docs/
      - type: OpenAPI
        url: openapi/tradestation-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/tradestation-streaming-asyncapi.yml
      - type: JSONSchema
        url: json-schema/tradestation-order-schema.json
      - type: JSONStructure
        url: json-structure/tradestation-order-structure.json
      - type: JSONLd
        url: json-ld/tradestation-context.jsonld
      - type: SpectralRules
        url: rules/tradestation-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/trading-and-market-data.yaml
      - type: Vocabulary
        url: vocabulary/tradestation-vocabulary.yml
      - type: GitHubOrg
        url: https://github.com/tradestation
      - type: APISpecification
        url: https://tradestation.github.io/api-docs/
  - aid: tradestation:tradestation-streaming
    name: TradeStation Streaming API
    description: The TradeStation Streaming API provides real-time HTTP streaming endpoints using chunked transfer encoding with newline-delimited JSON for market data and brokerage events. Streams deliver live quote updates, bar chart data, and order status changes with minimal latency.
    humanURL: https://api.tradestation.com/docs/
    baseURL: https://api.tradestation.com
    tags:
      - Bar Charts
      - Cryptocurrency
      - Market Data
      - Options
      - Order Status
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://api.tradestation.com/docs/
      - type: AsyncAPI
        url: asyncapi/tradestation-streaming-asyncapi.yml
common:
  - type: Website
    url: https://www.tradestation.com
  - type: Developer
    url: https://developer.tradestation.com
  - type: Documentation
    url: https://api.tradestation.com/docs/
  - type: Authentication
    url: https://api.tradestation.com/docs/fundamentals/authentication/
  - type: GitHub
    url: https://github.com/tradestation
  - type: RateLimiting
    url: https://api.tradestation.com/docs/fundamentals/rate-limiting/
  - type: TermsOfService
    url: https://www.tradestation.com/important-information/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
