---
aid: coingecko
url: https://raw.githubusercontent.com/api-evangelist/coingecko/refs/heads/main/apis.yml
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
name: Coingecko
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CoinGecko is a cryptocurrency data aggregator that provides market data, analytics, and information on thousands of crypto assets and exchanges worldwide.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

