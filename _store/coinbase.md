---
aid: coinbase
url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/apis.yml
apis:
- aid: coinbase:advanced-trade-api
  name: Coinbase Advanced Trade API
  tags:
  - Automation
  - Cryptocurrency
  - Market Data
  - Orders
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.coinbase.com
  humanURL: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/rest-api
  properties:
  - url: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/rest-api
    type: Documentation
  - url: openapi/coinbase-advanced-trade-openapi.yml
    type: OpenAPI
  - url: asyncapi/coinbase-advanced-trade-asyncapi.yml
    type: AsyncAPI
  description: The Coinbase Advanced Trade API provides programmatic access to advanced trading features on the Coinbase platform. Developers can automate market, limit, and stop-limit orders, manage portfolios, retrieve real-time and historical market data, and monitor fees. The REST API is available at api.coinbase.com/api/v3/brokerage and supports authenticated access using API keys with HMAC SHA-256 signatures.
- aid: coinbase:exchange-api
  name: Coinbase Exchange API
  tags:
  - Cryptocurrency
  - Exchange
  - FIX
  - Market Data
  - Trading
  - WebSocket
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.exchange.coinbase.com
  humanURL: https://www.coinbase.com/developer-platform/products/exchange-api
  properties:
  - url: https://docs.cdp.coinbase.com/exchange/docs/welcome
    type: Documentation
  - url: openapi/coinbase-exchange-openapi.yml
    type: OpenAPI
  - url: asyncapi/coinbase-exchange-asyncapi.yml
    type: AsyncAPI
  description: The Coinbase Exchange API provides high-throughput access to real-time market data and order management for institutional and professional traders. It supports REST APIs, FIX protocol, and WebSocket feeds for direct order placement and live market data streaming. The API enables programmatic trading at scale with low-latency execution and is designed for high-volume trading operations on the Coinbase exchange.
- aid: coinbase:prime-api
  name: Coinbase Prime API
  tags:
  - Cryptocurrency
  - Custody
  - Institutional
  - Prime Brokerage
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.prime.coinbase.com
  humanURL: https://www.coinbase.com/developer-platform/products/prime-apis
  properties:
  - url: https://docs.cdp.coinbase.com/prime/docs/rest-requests
    type: Documentation
  - url: openapi/coinbase-prime-openapi.yml
    type: OpenAPI
  description: The Coinbase Prime API enables institutions to manage cryptocurrency trading and custody on behalf of their clients. It supports programmatic trading strategies, automated platform processes, portfolio management, and custodial operations. The REST API provides endpoints for order execution, account management, transaction history, and reporting, designed for institutional-grade workflows and compliance requirements.
- aid: coinbase:onramp-api
  name: Coinbase Onramp API
  tags:
  - Cryptocurrency
  - Fiat
  - Offramp
  - Onramp
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.developer.coinbase.com
  humanURL: https://www.coinbase.com/developer-platform/products/onramp
  properties:
  - url: https://docs.cdp.coinbase.com/onramp/docs/welcome
    type: Documentation
  - url: openapi/coinbase-onramp-openapi.yml
    type: OpenAPI
  description: The Coinbase Onramp API allows developers to integrate fiat-to-crypto purchasing directly into their applications. It provides a FundCard React component and REST APIs to create one-click-buy URLs that enable users to purchase cryptocurrency with minimal friction. The API supports multiple fiat currencies and payment methods, making it straightforward for developers to onboard users into the crypto ecosystem from any application.
- aid: coinbase:commerce-api
  name: Coinbase Commerce API
  tags:
  - Checkout
  - Commerce
  - Cryptocurrency
  - Invoices
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.commerce.coinbase.com
  humanURL: https://commerce.coinbase.com/docs
  properties:
  - url: https://commerce.coinbase.com/docs/api
    type: Documentation
  - url: openapi/coinbase-commerce-openapi.yml
    type: OpenAPI
  - url: asyncapi/coinbase-commerce-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Coinbase Commerce API enables merchants and developers to accept cryptocurrency payments globally. It supports payment links, payouts, invoices, and checkout flows that can be integrated into websites and applications. The API provides endpoints for creating charges, managing payments, handling webhooks for payment notifications, and automating financial workflows for businesses accepting crypto as a payment method.
- aid: coinbase:wallet-sdk
  name: Coinbase Wallet SDK
  tags:
  - Cryptocurrency
  - DApps
  - SDK
  - Wallet
  - Web3
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.coinbase.com/developer-platform/products/wallet-sdk
  properties:
  - url: https://docs.cdp.coinbase.com/wallet-sdk/docs/welcome
    type: Documentation
  description: The Coinbase Wallet SDK allows developers to integrate Coinbase Wallet connectivity into decentralized applications. It provides a streamlined interface for users to connect their wallets, sign transactions, and interact with smart contracts across multiple blockchain networks. The SDK supports millions of Coinbase Wallet users and enables dapp developers to offer seamless wallet-based experiences for trading assets and managing NFTs.
- aid: coinbase:data-api
  name: Coinbase Data API
  tags:
  - Analytics
  - Blockchain
  - Cryptocurrency
  - Market Data
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.coinbase.com/developer-platform/products/data-api
  properties:
  - url: https://www.coinbase.com/developer-platform/products/data-api
    type: Documentation
  description: The Coinbase Data API provides developers with access to cryptocurrency market data, blockchain analytics, and pricing information. It delivers real-time and historical data for a wide range of digital assets, enabling developers to build data-driven applications, dashboards, and research tools. The API supports queries for price feeds, trading volumes, and on-chain metrics across supported networks.
- aid: coinbase:agentkit
  name: Coinbase AgentKit
  tags:
  - Agents
  - AI
  - Blockchain
  - SDK
  - Wallet
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.cdp.coinbase.com/agent-kit/welcome
  properties:
  - url: https://docs.cdp.coinbase.com/agent-kit/welcome
    type: Documentation
  description: Coinbase AgentKit is a toolkit that enables AI agents to interact with blockchain networks through secure wallet management and comprehensive onchain capabilities. Built on the Coinbase Developer Platform SDK, it is framework-agnostic and wallet-agnostic, supporting EVM and Solana networks.
name: Coinbase
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Coinbase is a cryptocurrency exchange platform that enables users to buy, sell, transfer, and store digital assets such as Bitcoin and Ethereum.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

