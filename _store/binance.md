---
aid: binance
url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/apis.yml
modified: '2026-04-21'
apis:
  - aid: binance:spot-trading-api
    name: Binance Spot Trading API
    tags:
      - Cryptocurrency
      - Exchange
      - Market Data
      - Spot
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
    properties:
      - url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
        type: Documentation
      - url: openapi/binance-spot-trading-openapi.yml
        type: OpenAPI
    description: The Binance Spot Trading REST API provides programmatic access to the Binance spot exchange, the world's largest cryptocurrency trading platform by volume. Developers can place and manage orders, query account balances, retrieve real-time and historical market data, and manage trading pairs. The API supports limit, market, stop-loss, and other order types, along with account and trade history endpoints. Authentication uses HMAC SHA256 signed requests with API key and secret key credentials.
  - aid: binance:spot-websocket-api
    name: Binance Spot WebSocket API
    tags:
      - Cryptocurrency
      - Market Data
      - Real-Time
      - Streaming
      - WebSocket
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: wss://ws-api.binance.com
    humanURL: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api
    properties:
      - url: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api
        type: Documentation
      - url: asyncapi/binance-spot-websocket-api-asyncapi.yml
        type: AsyncAPI
    description: The Binance Spot WebSocket API provides an alternative way to access spot trading functionality through persistent WebSocket connections. It is functionally equivalent to the REST API, accepting the same parameters and returning the same status and error codes, but offers lower latency for time-sensitive trading operations.
  - aid: binance:spot-websocket-streams
    name: Binance Spot WebSocket Streams
    tags:
      - Cryptocurrency
      - Market Data
      - Real-Time
      - Streaming
      - WebSocket
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: wss://stream.binance.com
    humanURL: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
    properties:
      - url: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
        type: Documentation
      - url: asyncapi/binance-spot-websocket-streams-asyncapi.yml
        type: AsyncAPI
    description: Binance Spot WebSocket Streams deliver real-time market data updates via persistent WebSocket connections. Developers can subscribe to individual symbol ticker streams, aggregate trade streams, kline and candlestick data, depth-of-book updates, and mini-ticker streams. The service supports both single and combined stream subscriptions, enabling efficient consumption of live market data for trading bots, dashboards, and analytics applications without polling the REST API.
  - aid: binance:usds-margined-futures-api
    name: Binance USD-S Margined Futures API
    tags:
      - Cryptocurrency
      - Derivatives
      - Futures
      - Trading
      - USDT
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://fapi.binance.com
    humanURL: https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info
    properties:
      - url: https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info
        type: Documentation
      - url: openapi/binance-usds-margined-futures-openapi.yml
        type: OpenAPI
    description: The Binance USD-S Margined Futures API enables trading of USDT and BUSD margined perpetual and delivery futures contracts. Developers can place leveraged long and short positions, manage margin and leverage settings, query funding rates, and access futures-specific market data including mark price, index price, and open interest. The API supports advanced order types such as trailing stop and take-profit/stop-loss orders for sophisticated derivatives trading strategies.
  - aid: binance:coin-margined-futures-api
    name: Binance COIN-M Futures API
    tags:
      - Coin Margined
      - Cryptocurrency
      - Derivatives
      - Futures
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://dapi.binance.com
    humanURL: https://developers.binance.com/docs/derivatives/coin-margined-futures/general-info
    properties:
      - url: https://developers.binance.com/docs/derivatives/coin-margined-futures/general-info
        type: Documentation
      - url: openapi/binance-coin-margined-futures-openapi.yml
        type: OpenAPI
    description: The Binance COIN-M Futures API provides access to coin-margined perpetual and delivery futures contracts, where the margin and settlement currency is the base cryptocurrency rather than a stablecoin. This allows traders to use BTC, ETH, and other cryptocurrencies as collateral for leveraged positions. The API supports order placement, position management, margin adjustments, and market data retrieval for coin-margined derivatives products.
  - aid: binance:european-options-api
    name: Binance European Options API
    tags:
      - Cryptocurrency
      - Derivatives
      - Options
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://eapi.binance.com
    humanURL: https://developers.binance.com/docs/derivatives/option/general-info
    properties:
      - url: https://developers.binance.com/docs/derivatives/option/general-info
        type: Documentation
      - url: openapi/binance-european-options-openapi.yml
        type: OpenAPI
    description: The Binance European Options API provides access to European-style cryptocurrency options contracts. Developers can trade call and put options on assets like BTC and ETH, query options chains with various strike prices and expiration dates, and retrieve options-specific market data including implied volatility and Greeks. The API enables programmatic options trading strategies such as hedging, income generation, and directional bets on cryptocurrency price movements.
  - aid: binance:portfolio-margin-api
    name: Binance Portfolio Margin API
    tags:
      - Cryptocurrency
      - Margin
      - Portfolio
      - Risk Management
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://papi.binance.com
    humanURL: https://developers.binance.com/docs/derivatives/portfolio-margin/general-info
    properties:
      - url: https://developers.binance.com/docs/derivatives/portfolio-margin/general-info
        type: Documentation
      - url: openapi/binance-portfolio-margin-openapi.yml
        type: OpenAPI
    description: The Binance Portfolio Margin API enables cross-margining across spot, futures, and options positions under a unified margin account. This risk-based margining system calculates margin requirements based on the overall portfolio risk rather than individual positions, allowing more capital-efficient trading. Developers can manage portfolio margin accounts, query unified account balances, and execute trades across multiple product types through a single API interface.
  - aid: binance:margin-trading-api
    name: Binance Margin Trading API
    tags:
      - Borrowing
      - Cryptocurrency
      - Leverage
      - Margin
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/margin_trading/general-info
    properties:
      - url: https://developers.binance.com/docs/margin_trading/general-info
        type: Documentation
      - url: openapi/binance-margin-trading-openapi.yml
        type: OpenAPI
    description: The Binance Margin Trading API allows developers to programmatically access cross-margin and isolated-margin trading functionality. Users can borrow assets, place leveraged trades, repay loans, and manage margin account balances. The API provides endpoints for transferring assets between spot and margin accounts, querying interest rates and borrow limits, and monitoring margin level and liquidation thresholds for risk management purposes.
  - aid: binance:wallet-api
    name: Binance Wallet API
    tags:
      - Account
      - Cryptocurrency
      - Deposits
      - Wallet
      - Withdrawals
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/wallet/introduction
    properties:
      - url: https://developers.binance.com/docs/wallet/introduction
        type: Documentation
      - url: openapi/binance-wallet-openapi.yml
        type: OpenAPI
    description: The Binance Wallet API provides endpoints for managing cryptocurrency deposits, withdrawals, and account balances. Developers can query deposit and withdrawal history, retrieve deposit addresses, initiate withdrawals, check asset balances across all wallets, and access network and fee information for supported coins. The API also supports dust conversion, asset transfers between accounts, and querying system-wide asset details.
  - aid: binance:sub-account-api
    name: Binance Sub-Account API
    tags:
      - Account Management
      - Cryptocurrency
      - Enterprise
      - Sub-Account
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/sub_account/general-info
    properties:
      - url: https://developers.binance.com/docs/sub_account/general-info
        type: Documentation
      - url: openapi/binance-sub-account-openapi.yml
        type: OpenAPI
    description: The Binance Sub-Account API enables institutional and enterprise users to manage multiple sub-accounts under a master account. Developers can create and manage sub-accounts, transfer assets between them, set trading permissions, query sub-account balances and transaction histories, and configure API keys for individual sub-accounts. This API is essential for fund managers, trading firms, and businesses that need to segregate assets and trading activity across multiple accounts.
  - aid: binance:simple-earn-api
    name: Binance Simple Earn API
    tags:
      - Cryptocurrency
      - Earn
      - Savings
      - Staking
      - Yield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/simple_earn/general-info
    properties:
      - url: https://developers.binance.com/docs/simple_earn/general-info
        type: Documentation
      - url: openapi/binance-simple-earn-openapi.yml
        type: OpenAPI
    description: The Binance Simple Earn API provides programmatic access to flexible and locked savings and staking products. Developers can subscribe to and redeem earn products, query available products and their interest rates, check subscription records and earned interest, and manage auto-subscribe settings. The API supports both flexible products that allow instant redemption and locked products that offer higher yields for fixed-term commitments.
  - aid: binance:mining-api
    name: Binance Mining API
    tags:
      - Cryptocurrency
      - Hash Rate
      - Mining
      - Pool
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/mining/general-info
    properties:
      - url: https://developers.binance.com/docs/mining/general-info
        type: Documentation
      - url: openapi/binance-mining-openapi.yml
        type: OpenAPI
    description: The Binance Mining API provides access to Binance Pool mining services. Developers can retrieve mining algorithms, available coins for mining, detailed miner statistics, earnings and revenue data, and hashrate resale information. The API enables mining operators and pools to programmatically monitor worker status, track mining profitability, and manage hashrate allocation across different mining algorithms and coins.
  - aid: binance:copy-trading-api
    name: Binance Copy Trading API
    tags:
      - Copy Trading
      - Cryptocurrency
      - Social Trading
      - Trading
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/copy_trading/general-info
    properties:
      - url: https://developers.binance.com/docs/copy_trading/general-info
        type: Documentation
      - url: openapi/binance-copy-trading-openapi.yml
        type: OpenAPI
    description: The Binance Copy Trading API allows developers to interact with the copy trading platform where users can automatically replicate the trades of experienced lead traders. The API provides endpoints for managing copy trading positions, querying lead trader portfolios and performance metrics, and configuring copy trading parameters such as investment amount and risk limits. It supports both futures copy trading for automated portfolio mirroring.
  - aid: binance:convert-api
    name: Binance Convert API
    tags:
      - Convert
      - Cryptocurrency
      - Exchange
      - Swap
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/convert/general-info
    properties:
      - url: https://developers.binance.com/docs/convert/general-info
        type: Documentation
      - url: openapi/binance-convert-openapi.yml
        type: OpenAPI
    description: The Binance Convert API provides a simple interface for converting between cryptocurrencies and fiat currencies at quoted prices. Unlike order-book trading, the Convert API offers instant swaps with price quotes that are valid for a limited time window. Developers can request price quotes for asset pairs, accept quotes to execute conversions, and query conversion history. This API is well-suited for applications that need simple asset exchange without managing order books.
  - aid: binance:pay-api
    name: Binance Pay API
    tags:
      - Commerce
      - Cryptocurrency
      - Merchant
      - Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://bpay.binanceapi.com
    humanURL: https://developers.binance.com/docs/binance-pay/introduction
    properties:
      - url: https://developers.binance.com/docs/binance-pay/introduction
        type: Documentation
      - url: openapi/binance-pay-openapi.yml
        type: OpenAPI
      - url: asyncapi/binance-pay-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Binance Pay API enables merchants and businesses to accept cryptocurrency payments from Binance users. Developers can create payment orders, query payment status, process refunds, and manage merchant accounts. The API supports QR code payments, in-app payments, and online checkout flows for e-commerce integration. It also provides webhook notifications for real-time payment status updates and profit-sharing capabilities for platform businesses.
  - aid: binance:algo-trading-api
    name: Binance Algo Trading API
    tags:
      - Algorithmic Trading
      - Cryptocurrency
      - TWAP
      - VWAP
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/algo/general-info
    properties:
      - url: https://developers.binance.com/docs/algo/general-info
        type: Documentation
      - url: openapi/binance-algo-trading-openapi.yml
        type: OpenAPI
    description: The Binance Algo Trading API provides access to algorithmic order execution strategies such as TWAP (Time-Weighted Average Price) and volume participation algorithms. Developers can place large orders that are automatically broken into smaller child orders and executed over time to minimize market impact.
  - aid: binance:auto-invest-api
    name: Binance Auto-Invest API
    tags:
      - Auto-Invest
      - Cryptocurrency
      - DCA
      - Recurring
      - Savings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/auto_invest/general-info
    properties:
      - url: https://developers.binance.com/docs/auto_invest/general-info
        type: Documentation
      - url: openapi/binance-auto-invest-openapi.yml
        type: OpenAPI
    description: The Binance Auto-Invest API enables developers to create and manage recurring cryptocurrency purchase plans, also known as dollar-cost averaging (DCA) strategies. Users can set up automated investment plans that periodically buy specified cryptocurrencies at regular intervals. The API provides endpoints for creating, modifying, and querying investment plans, viewing purchase history, and managing portfolio index-linked plans that automatically rebalance across multiple assets.
  - aid: binance:crypto-loan-api
    name: Binance Crypto Loan API
    tags:
      - Borrowing
      - Collateral
      - Cryptocurrency
      - Lending
      - Loans
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/crypto_loan/general-info
    properties:
      - url: https://developers.binance.com/docs/crypto_loan/general-info
        type: Documentation
      - url: openapi/binance-crypto-loan-openapi.yml
        type: OpenAPI
    description: The Binance Crypto Loan API provides programmatic access to cryptocurrency-collateralized lending services. Developers can borrow assets by pledging cryptocurrency as collateral, repay outstanding loans, adjust collateral amounts, and query loan orders and repayment history. The API supports both flexible and fixed-term loan products with varying interest rates and loan-to-value ratios, enabling applications that need liquidity without selling underlying crypto holdings.
  - aid: binance:gift-card-api
    name: Binance Gift Card API
    tags:
      - Cryptocurrency
      - Gift Card
      - Rewards
      - Voucher
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/gift_card/general-info
    properties:
      - url: https://developers.binance.com/docs/gift_card/general-info
        type: Documentation
      - url: openapi/binance-gift-card-openapi.yml
        type: OpenAPI
    description: The Binance Gift Card API allows developers to create, redeem, and verify cryptocurrency gift cards programmatically. Businesses can integrate gift card creation into rewards programs, promotional campaigns, and gifting platforms. The API supports creating gift cards with specific cryptocurrency denominations, verifying card validity, redeeming cards to user accounts, and querying creation and redemption history for reconciliation purposes.
  - aid: binance:nft-api
    name: Binance NFT API
    tags:
      - Collectibles
      - Cryptocurrency
      - Digital Assets
      - NFT
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/nft/general-info
    properties:
      - url: https://developers.binance.com/docs/nft/general-info
        type: Documentation
      - url: openapi/binance-nft-openapi.yml
        type: OpenAPI
    description: The Binance NFT API provides endpoints for interacting with the Binance NFT marketplace programmatically. Developers can query NFT transaction history, deposit and withdrawal records, and asset information for non-fungible tokens held on the platform. The API supports retrieving NFT metadata, managing NFT deposits and withdrawals across supported blockchain networks, and accessing transaction history for tracking NFT portfolio activity.
  - aid: binance:fiat-api
    name: Binance Fiat API
    tags:
      - Cryptocurrency
      - Currency
      - Deposits
      - Fiat
      - Withdrawals
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.binance.com
    humanURL: https://developers.binance.com/docs/fiat/general-info
    properties:
      - url: https://developers.binance.com/docs/fiat/general-info
        type: Documentation
      - url: openapi/binance-fiat-openapi.yml
        type: OpenAPI
    description: The Binance Fiat API provides access to fiat currency deposit and withdrawal operations on the Binance platform. Developers can query fiat deposit and withdrawal order history, check available fiat payment methods, and retrieve transaction details for fiat-to-crypto and crypto-to-fiat conversions. The API supports multiple fiat currencies and payment channels, enabling applications that bridge traditional finance and cryptocurrency markets.
common:
  - type: Portal
    url: https://developers.binance.com/
  - type: Documentation
    url: https://developers.binance.com/docs/binance-spot-api-docs/
  - type: GettingStarted
    url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
  - type: GitHubOrganization
    url: https://github.com/binance
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/rules/binance-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/vocabulary/binance-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/capabilities/spot-trading.yaml
  - type: Features
    data:
      - name: Spot Trading
        description: Buy and sell 500+ cryptocurrency pairs with limit, market, and stop-loss orders.
      - name: USD-M Futures
        description: Trade perpetual and delivery futures contracts settled in USDT.
      - name: Coin-M Futures
        description: Trade perpetual and delivery futures contracts settled in cryptocurrency.
      - name: Margin Trading
        description: Trade on margin with up to 10x leverage using borrowed assets.
      - name: Algo Trading
        description: Place algorithmic orders using TWAP, VP, and other execution strategies.
      - name: WebSocket Streams
        description: Real-time market data streams for price, depth, and trade updates.
      - name: Wallet Management
        description: Manage deposits, withdrawals, and asset transfers between wallets.
      - name: Simple Earn
        description: Earn interest on idle cryptocurrency assets through flexible and locked products.
  - type: UseCases
    data:
      - name: Algorithmic Trading
        description: Build automated trading bots using Binance REST and WebSocket APIs.
      - name: Portfolio Management
        description: Track and rebalance cryptocurrency portfolios programmatically.
      - name: Market Data Aggregation
        description: Aggregate real-time price and order book data for analysis or display.
      - name: DeFi Integration
        description: Bridge centralized Binance liquidity into DeFi protocols.
      - name: Arbitrage Trading
        description: Exploit price differences across Binance spot, futures, and margin markets.
  - type: Integrations
    data:
      - name: TradingView
        description: Connect Binance to TradingView for charting and automated alert-based trading.
      - name: MetaTrader
        description: Use MetaTrader bridge adapters to trade Binance from MT4/MT5.
      - name: Telegram
        description: Receive Binance trade notifications and alerts via Telegram bot.
      - name: AWS Lambda
        description: Run serverless trading bots triggered by events on AWS Lambda.
      - name: Python CCXT
        description: Access Binance through the CCXT unified cryptocurrency exchange library.
description: Binance is the world's largest cryptocurrency exchange by trading volume, providing APIs for spot trading, futures, margin, wallet management, and market data across 19+ specialized REST APIs and WebSocket streams.
name: Binance
type: Contract
access: 3rd-Party
position: Consuming
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cryptocurrency
  - Exchange
  - Trading
  - Blockchain
  - Finance
  - DeFi
  - Market Data
created: '2025-01-01'
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
