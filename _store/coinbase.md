---
aid: coinbase
url: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/apis.yml
name: Coinbase
tags:
  - Blockchain
  - Cryptocurrency
  - Custody
  - Exchange
  - Onramp
  - Payments
  - Trading
  - Wallet
  - Web3
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-20'
modified: '2026-04-28'
position: Consumer
description: Coinbase is a leading cryptocurrency platform providing trading, custody, and payment infrastructure for individuals, businesses, and institutions. The Coinbase Developer Platform (CDP) exposes a wide product surface across retail trading (Advanced Trade), professional and institutional trading (Exchange and Prime), merchant payments (Commerce), fiat onboarding (Onramp), developer wallet integration (Wallet SDK), market and on-chain data (Data API), and AI agent toolkits (AgentKit). Authentication is performed using API keys with HMAC-SHA256 signatures (Advanced Trade, Exchange) or JWT bearer tokens (Prime, CDP), with WebSocket and FIX feeds available for low-latency market data and order management.
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
    x-features:
      - Market, limit, and stop-limit order types
      - HMAC-SHA256 API key signatures
      - WebSocket feed for real-time order updates
      - Portfolio and account balance management
      - Public market data without authentication
    x-use-cases:
      - Build retail trading bots and automated strategies
      - Power portfolio dashboards with live balances
      - Run algorithmic strategies against advanced order types
      - Sync transaction history into accounting tooling
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
    x-features:
      - REST, FIX, and WebSocket interfaces
      - Sub-millisecond market data feeds
      - Direct order entry for institutional flow
      - Full order book and trade history access
    x-use-cases:
      - Run market-making and liquidity-providing strategies
      - Stream consolidated market data into trading systems
      - Connect legacy FIX trading stacks to crypto venues
      - Operate institutional execution and risk pipelines
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
    x-features:
      - Multi-portfolio and multi-entity account model
      - Cold and hot custody with whitelisted addresses
      - Order execution, allocation, and TWAP support
      - Transaction history and reporting endpoints
      - JWT-based authentication with per-entity scoping
    x-use-cases:
      - Operate prime brokerage flows on behalf of clients
      - Automate treasury and custody workflows
      - Allocate fills across sub-accounts and entities
      - Stream compliance and reporting data into back-office systems
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
    x-features:
      - One-click-buy URL generation
      - FundCard React component for embedded UX
      - Multiple fiat rails and payment methods
      - Onramp and offramp flows in a single API
    x-use-cases:
      - Embed fiat funding directly into a wallet or dapp
      - Enable users to cash out from on-chain holdings
      - Reduce KYC and PCI scope by leveraging Coinbase's stack
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
    x-features:
      - Charges, checkouts, invoices, and payment links
      - Webhook event delivery for charge state changes
      - Hosted checkout pages and embedded SDK options
      - Payouts in stablecoins and supported assets
    x-use-cases:
      - Accept crypto payments on e-commerce sites
      - Issue branded invoices payable in crypto
      - Trigger fulfillment workflows from charge webhooks
      - Pay vendors and contractors in stablecoins
  - aid: coinbase:wallet-sdk
    name: Coinbase Wallet SDK
    tags:
      - Cryptocurrency
      - DApps
      - SDK
      - Wallet
      - Web3
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.coinbase.com/developer-platform/products/wallet-sdk
    properties:
      - url: https://docs.cdp.coinbase.com/wallet-sdk/docs/welcome
        type: Documentation
    description: The Coinbase Wallet SDK allows developers to integrate Coinbase Wallet connectivity into decentralized applications. It provides a streamlined interface for users to connect their wallets, sign transactions, and interact with smart contracts across multiple blockchain networks. The SDK supports millions of Coinbase Wallet users and enables dapp developers to offer seamless wallet-based experiences for trading assets and managing NFTs.
    x-features:
      - EIP-1193 provider compatible with web3 libraries
      - Mobile and desktop wallet connection flows
      - Smart contract signing and transaction handling
      - NFT and asset management primitives
    x-use-cases:
      - Add Connect Wallet flows to dapps
      - Sign messages and transactions in mobile and web apps
      - Bridge web3 user identity to traditional UX patterns
  - aid: coinbase:data-api
    name: Coinbase Data API
    tags:
      - Analytics
      - Blockchain
      - Cryptocurrency
      - Market Data
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.coinbase.com/developer-platform/products/data-api
    properties:
      - url: https://www.coinbase.com/developer-platform/products/data-api
        type: Documentation
    description: The Coinbase Data API provides developers with access to cryptocurrency market data, blockchain analytics, and pricing information. It delivers real-time and historical data for a wide range of digital assets, enabling developers to build data-driven applications, dashboards, and research tools. The API supports queries for price feeds, trading volumes, and on-chain metrics across supported networks.
    x-features:
      - Real-time and historical price feeds
      - On-chain analytics and metrics
      - Trading volume and liquidity insights
    x-use-cases:
      - Power research dashboards and reports
      - Drive risk and pricing models with on-chain signals
      - Display market data in consumer apps
  - aid: coinbase:agentkit
    name: Coinbase AgentKit
    tags:
      - Agents
      - AI
      - Blockchain
      - SDK
      - Wallet
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cdp.coinbase.com/agent-kit/welcome
    properties:
      - url: https://docs.cdp.coinbase.com/agent-kit/welcome
        type: Documentation
    description: Coinbase AgentKit is a toolkit that enables AI agents to interact with blockchain networks through secure wallet management and comprehensive onchain capabilities. Built on the Coinbase Developer Platform SDK, it is framework-agnostic and wallet-agnostic, supporting EVM and Solana networks.
    x-features:
      - Framework-agnostic and wallet-agnostic agent toolkit
      - EVM and Solana network support
      - Gasless transactions via CDP Smart Wallets
      - LangChain, MCP, and other framework integrations
    x-use-cases:
      - Build autonomous AI agents that transact on-chain
      - Automate token swaps, transfers, and contract calls
      - Connect agentic frameworks to wallet primitives
common:
  - type: Developer Portal
    url: https://www.coinbase.com/developer-platform
  - type: Documentation
    url: https://docs.cdp.coinbase.com/
  - type: Website
    url: https://www.coinbase.com/
  - type: Blog
    url: https://www.coinbase.com/blog
  - type: GitHub
    url: https://github.com/coinbase
  - type: Login
    url: https://login.coinbase.com/
  - type: Support
    url: https://help.coinbase.com/
  - type: Privacy Policy
    url: https://www.coinbase.com/legal/privacy
  - type: Terms of Service
    url: https://www.coinbase.com/legal/user-agreement
  - type: JSON-LD
    url: json-ld/coinbase-context.jsonld
  - type: JSONSchema
    url: json-schema/coinbase-order-schema.json
  - type: JSONSchema
    url: json-schema/coinbase-charge-schema.json
  - type: JSONSchema
    url: json-schema/coinbase-product-schema.json
  - type: Spectral Ruleset
    url: rules/coinbase-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/coinbase-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
