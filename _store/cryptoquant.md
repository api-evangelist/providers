---
aid: cryptoquant
url: https://raw.githubusercontent.com/api-evangelist/cryptoquant/refs/heads/main/apis.yml
x-type: company
name: CryptoQuant
description: CryptoQuant is a blockchain data analytics platform providing real-time and historical on-chain, exchange flow, miner, derivatives, and stablecoin metrics for Bitcoin, Ethereum, and other major cryptocurrencies. The API delivers time-series data used by traders, funds, and researchers to gauge market sentiment and capital flows.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - Cryptocurrency
  - On-Chain Analytics
  - Market Data
  - Derivatives
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
created: '2025-02-12'
modified: '2026-04-28'
apis:
  - aid: cryptoquant:cryptoquant-api
    name: CryptoQuant API
    description: The CryptoQuant API exposes on-chain, exchange flow, market, miner, and stablecoin metrics for major cryptocurrencies via a versioned REST interface. Authentication uses an API key passed as a bearer token.
    humanURL: https://cryptoquant.com/docs
    baseURL: https://api.cryptoquant.com/v1
    tags:
      - On-Chain Analytics
      - Exchange Flows
      - Miner Flows
      - Market Data
      - Stablecoins
    properties:
      - url: https://cryptoquant.com/docs
        type: Documentation
      - url: https://cryptoquant.com/products/api
        type: Pricing
      - url: openapi/cryptoquant-openapi.yml
        type: OpenAPI
      - url: json-schema/cryptoquant-timeseries-schema.json
        type: JSONSchema
      - url: json-ld/cryptoquant-context.jsonld
        type: JSONLDContext
features:
  - name: Exchange Flows
    description: Inflow, outflow, and reserve metrics for major exchanges (Binance, Coinbase, Kraken, etc.).
  - name: Miner Flows
    description: Miner reserve, outflow, and position index for Bitcoin mining pools.
  - name: Network Indicators
    description: SOPR, MVRV, NVT, and other on-chain valuation indicators.
  - name: Market and Derivatives
    description: OHLCV, open interest, funding rate, and basis metrics.
  - name: Stablecoin Metrics
    description: Reserve, supply, and SSR metrics for USDT, USDC, DAI, BUSD.
  - name: Multiple Resolutions
    description: Time-series available at min, hour, day, and block-level windows.
  - name: Bearer Token Auth
    description: API key authentication via Authorization bearer header.
useCases:
  - name: Trading Signals
    description: Quantitative traders use exchange flow and SOPR data as inputs to trading models.
  - name: Risk Management
    description: Funds monitor exchange reserve trends to assess sell-pressure risk.
  - name: Miner Behavior Analysis
    description: Researchers track miner outflow and reserve trends to anticipate sell-side pressure.
  - name: Macro Crypto Research
    description: Analysts publish reports based on stablecoin and on-chain valuation indicators.
  - name: Compliance and Surveillance
    description: Surveillance teams detect anomalies and suspicious flow patterns across exchanges.
common:
  - url: https://cryptoquant.com/
    name: CryptoQuant Website
    type: Website
  - url: https://cryptoquant.com/docs
    name: API Documentation
    type: Documentation
  - url: https://cryptoquant.com/products/api
    name: API Plans
    type: Pricing
  - url: openapi/cryptoquant-openapi.yml
    type: OpenAPI
  - url: json-schema/cryptoquant-timeseries-schema.json
    type: JSONSchema
  - url: json-ld/cryptoquant-context.jsonld
    type: JSONLDContext
  - url: rules/cryptoquant-rules.yml
    type: SpectralRules
  - url: vocabulary/cryptoquant-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
