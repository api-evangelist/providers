---
aid: coingecko
url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/apis.yml
name: CoinGecko
tags:
  - Aggregator
  - Blockchain
  - Cryptocurrency
  - Decentralized Exchanges
  - DeFi
  - DEX
  - Exchanges
  - Liquidity Pools
  - Market Data
  - NFTs
  - Onchain Data
  - Prices
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-20'
modified: '2026-04-28'
position: Consumer
description: 'CoinGecko is a cryptocurrency data aggregator providing market data, analytics, and information on thousands of crypto assets, exchanges, derivatives, NFTs, and on-chain decentralized markets worldwide. The CoinGecko Developer Platform exposes three primary APIs: the public Crypto Market Data API (Demo plan and free tier), the commercial Pro API for higher rate limits and exclusive endpoints, and the Onchain DEX API powered by GeckoTerminal for decentralized exchange data across 250+ networks. Authentication uses x-cg-demo-api-key (Demo) or x-cg-pro-api-key (Pro) headers, with rate limits ranging from 30 calls per minute on Demo to 1,000 calls per minute on top Pro tiers.'
apis:
  - aid: coingecko:crypto-market-data-api
    name: CoinGecko Crypto Market Data API
    tags:
      - Blockchain
      - Cryptocurrency
      - Exchanges
      - Market Data
      - NFTs
      - Prices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.coingecko.com/api/v3
    humanURL: https://docs.coingecko.com
    properties:
      - url: https://docs.coingecko.com
        type: Documentation
      - url: https://www.coingecko.com/en/api/pricing
        type: Pricing
      - url: https://www.coingecko.com/en/api
        type: Landing Page
      - type: OpenAPI
        url: openapi/coingecko-crypto-market-data-api-openapi.yml
    description: The CoinGecko Crypto Market Data API provides comprehensive and reliable cryptocurrency price and market data through RESTful JSON endpoints. It offers over 70 endpoints covering real-time and historical prices, trading volumes, market capitalization, OHLCV data, exchange information, NFT metrics, derivatives data, and public treasury holdings for over 18,000 coins.
    x-features:
      - 70+ REST endpoints in a single normalized API
      - Real-time and historical price feeds
      - OHLCV chart data for charting and analysis
      - Exchange, derivatives, and NFT metrics
      - Public company treasury holdings
      - Demo plan free tier with x-cg-demo-api-key auth
    x-use-cases:
      - Power crypto pricing widgets and tickers
      - Backtest strategies against historical OHLCV
      - Display NFT collection floor prices
      - Compute portfolio valuations across many assets
  - aid: coingecko:pro-api
    name: CoinGecko Pro API
    tags:
      - Commercial
      - Cryptocurrency
      - Enterprise
      - Market Data
      - Prices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pro-api.coingecko.com/api/v3
    humanURL: https://docs.coingecko.com/reference/introduction
    properties:
      - url: https://docs.coingecko.com/reference/introduction
        type: Documentation
      - url: https://www.coingecko.com/en/api/pricing
        type: Pricing
      - type: OpenAPI
        url: openapi/coingecko-pro-api-openapi.yml
    description: The CoinGecko Pro API provides the same comprehensive cryptocurrency market data as the standard API but with enhanced performance, higher rate limits of up to 1,000 calls per minute, and faster data updates with prices cached every 30 seconds. It includes exclusive endpoints for advanced analytics, detailed market data, and historical granularity that are not available on the free Demo plan.
    x-features:
      - Up to 1,000 calls per minute (top Pro tier)
      - 30-second price cache for fresher data
      - Exclusive endpoints (e.g., circulating supply chart, hourly OHLC)
      - Higher historical depth than Demo
      - Authenticated via x-cg-pro-api-key
      - Commercial usage allowed under Pro license
    x-use-cases:
      - Run commercial pricing engines and trading services
      - Power exchange and brokerage dashboards
      - Stream high-frequency analytics into BI tools
      - Operate research products with full historical depth
  - aid: coingecko:onchain-dex-api
    name: CoinGecko Onchain DEX API
    tags:
      - Blockchain
      - Decentralized Exchanges
      - DeFi
      - DEX
      - Liquidity Pools
      - Onchain Data
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.coingecko.com/api/v3/onchain
    humanURL: https://www.coingecko.com/en/api/dex
    properties:
      - url: https://docs.coingecko.com/reference/endpoint-overview
        type: Documentation
      - url: https://www.coingecko.com/en/api/dex
        type: Landing Page
      - type: OpenAPI
        url: openapi/coingecko-onchain-dex-api-openapi.yml
    description: The CoinGecko Onchain DEX API, powered by GeckoTerminal, provides access to real-time decentralized exchange data across over 250 blockchain networks, 1,800 DEXes, and 30 million tokens. It offers more than 20 endpoints for querying liquidity pools, token data by contract address, OHLCV chart data, trending pools, and pool search functionality.
    x-features:
      - 250+ blockchain networks supported
      - 1,800+ DEXes and 30M+ tokens
      - Lookup tokens by contract address
      - Trending and search endpoints for discovery
      - Pool-level OHLCV chart data
    x-use-cases:
      - Track new and trending DEX pools
      - Display on-chain prices for long-tail tokens
      - Analyze liquidity and volume across networks
      - Monitor wallet exposure to DeFi pools
common:
  - type: Portal
    url: https://www.coingecko.com/en/api
  - type: Documentation
    url: https://docs.coingecko.com
  - type: Pricing
    url: https://www.coingecko.com/en/api/pricing
  - type: Website
    url: https://www.coingecko.com
  - type: Blog
    url: https://blog.coingecko.com
  - type: Support
    url: https://support.coingecko.com
  - type: Login
    url: https://www.coingecko.com/en/developers/dashboard
  - type: Status
    url: https://status.coingecko.com/
  - type: Terms of Service
    url: https://www.coingecko.com/en/terms
  - type: Privacy Policy
    url: https://www.coingecko.com/en/privacy
  - type: JSONSchema
    url: json-schema/coingecko-coin-schema.json
  - type: JSONSchema
    url: json-schema/coingecko-pool-schema.json
  - type: JSON-LD
    url: json-ld/coingecko-context.jsonld
  - type: Spectral Ruleset
    url: rules/coingecko-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/coingecko-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
