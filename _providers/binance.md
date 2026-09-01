---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Binance Agentic Access
  operation_count: 180
  slug: binance-agentic-access
  summary_line: 180 operations · 64 acting
api_count: 19
apis:
- description: The Binance Spot WebSocket API provides an alternative way to access spot trading functionality through persistent WebSocket connections. It is functionally equivalent to the REST API, accepting the s
  name: Binance Spot WebSocket API
  slug: spot-websocket-api
- description: 'Binance Spot WebSocket Streams deliver real-time market data updates via persistent WebSocket connections. Developers can subscribe to individual symbol ticker streams, aggregate trade streams, kline '
  name: Binance Spot WebSocket Streams
  slug: spot-websocket-streams
- description: Account endpoints for COIN-M futures positions and balances.
  name: Binance Account API
  slug: binance-account-api
- description: Asset balance and information endpoints.
  name: Binance Assets API
  slug: binance-assets-api
- description: Auto-invest plan management and query endpoints.
  name: Binance Auto-Invest API
  slug: binance-auto-invest-api
- description: Endpoints for borrowing and repaying margin assets.
  name: Binance Borrow/Repay API
  slug: binance-borrow-repay-api
- description: Cryptocurrency conversion quote and trade endpoints.
  name: Binance Convert API
  slug: binance-convert-api
- description: Copy trading position and portfolio management endpoints.
  name: Binance Copy Trading API
  slug: binance-copy-trading-api
- description: Loan borrowing, repayment, and query endpoints.
  name: Binance Crypto Loan API
  slug: binance-crypto-loan-api
- description: Deposit-related endpoints for addresses and history.
  name: Binance Deposits API
  slug: binance-deposits-api
- description: Fiat deposit, withdrawal, and payment history endpoints.
  name: Binance Fiat API
  slug: binance-fiat-api
- description: Flexible savings products that allow instant redemption.
  name: Binance Flexible Products API
  slug: binance-flexible-products-api
- description: Futures algorithmic trading endpoints.
  name: Binance Futures Algo API
  slug: binance-futures-algo-api
- description: General endpoints for connectivity testing and exchange information.
  name: Binance General API
  slug: binance-general-api
- description: Gift card creation, redemption, and verification endpoints.
  name: Binance Gift Card API
  slug: binance-gift-card-api
- description: Locked savings products with fixed-term commitments.
  name: Binance Locked Products API
  slug: binance-locked-products-api
- description: Public market data endpoints for COIN-M futures.
  name: Binance Market Data API
  slug: binance-market-data-api
- description: Mining algorithms, coin info, worker stats, and earnings endpoints.
  name: Binance Mining API
  slug: binance-mining-api
- description: NFT transaction history, deposit, withdrawal, and asset endpoints.
  name: Binance NFT API
  slug: binance-nft-api
- description: Payment order management endpoints for creating, querying, and closing orders.
  name: Binance Orders API
  slug: binance-orders-api
- description: Batch payout and transfer endpoints.
  name: Binance Payouts API
  slug: binance-payouts-api
- description: Refund processing endpoints.
  name: Binance Refunds API
  slug: binance-refunds-api
- description: Spot algorithmic trading endpoints.
  name: Binance Spot Algo API
  slug: binance-spot-algo-api
- description: Endpoints for querying and transferring sub-account assets.
  name: Binance Sub-Account Assets API
  slug: binance-sub-account-assets-api
- description: Endpoints for creating and managing sub-accounts.
  name: Binance Sub-Account Management API
  slug: binance-sub-account-management-api
- description: Trading endpoints for COIN-M futures orders.
  name: Binance Trading API
  slug: binance-trading-api
- description: User data stream listen key management for COIN-M futures.
  name: Binance User Data Stream API
  slug: binance-user-data-stream-api
- description: Withdrawal endpoints for initiating and tracking withdrawals.
  name: Binance Withdrawals API
  slug: binance-withdrawals-api
artifact_total: 148
asyncapis:
- description: 'Binance Pay sends webhook notifications to merchants for real-time payment status updates. When a customer completes a payment or a refund is processed, Binance Pay sends an HTTPS POST request to the '
  name: Binance Pay Webhooks
  slug: binance-pay-webhooks-asyncapi
- description: The Binance Spot WebSocket API provides an alternative way to access spot trading functionality through persistent WebSocket connections. It is functionally equivalent to the REST API, accepting the s
  name: Binance Spot WebSocket API
  slug: binance-spot-websocket-api-asyncapi
- description: 'Binance Spot WebSocket Streams deliver real-time market data updates via persistent WebSocket connections. Developers can subscribe to individual symbol ticker streams, aggregate trade streams, kline '
  name: Binance Spot WebSocket Streams
  slug: binance-spot-websocket-streams-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Binance Algo Trading Account API
  slug: open-binance-account-api
- collection_type: open
  name: Binance Algo Trading API
  slug: open-binance-algo-trading
- collection_type: open
  name: Binance Algo Trading Account Assets API
  slug: open-binance-assets-api
- collection_type: open
  name: Binance Algo Trading Account Auto-Invest API
  slug: open-binance-auto-invest-api
- collection_type: open
  name: Binance Auto-Invest API
  slug: open-binance-auto-invest
- collection_type: open
  name: Binance Algo Trading Account Borrow/Repay API
  slug: open-binance-borrow-repay-api
- collection_type: open
  name: Binance COIN-M Futures API
  slug: open-binance-coin-margined-futures
- collection_type: open
  name: Binance Algo Trading Account Convert API
  slug: open-binance-convert-api
- collection_type: open
  name: Binance Convert API
  slug: open-binance-convert
- collection_type: open
  name: Binance Algo Trading Account Copy Trading API
  slug: open-binance-copy-trading-api
- collection_type: open
  name: Binance Copy Trading API
  slug: open-binance-copy-trading
- collection_type: open
  name: Binance Algo Trading Account Crypto Loan API
  slug: open-binance-crypto-loan-api
- collection_type: open
  name: Binance Crypto Loan API
  slug: open-binance-crypto-loan
- collection_type: open
  name: Binance Algo Trading Account Deposits API
  slug: open-binance-deposits-api
- collection_type: open
  name: Binance European Options API
  slug: open-binance-european-options
- collection_type: open
  name: Binance Algo Trading Account Fiat API
  slug: open-binance-fiat-api
- collection_type: open
  name: Binance Fiat API
  slug: open-binance-fiat
- collection_type: open
  name: Binance Algo Trading Account Flexible Products API
  slug: open-binance-flexible-products-api
- collection_type: open
  name: Binance Algo Trading Account Futures Algo API
  slug: open-binance-futures-algo-api
- collection_type: open
  name: Binance Algo Trading Account General API
  slug: open-binance-general-api
- collection_type: open
  name: Binance Algo Trading Account Gift Card API
  slug: open-binance-gift-card-api
- collection_type: open
  name: Binance Gift Card API
  slug: open-binance-gift-card
- collection_type: open
  name: Binance Algo Trading Account Locked Products API
  slug: open-binance-locked-products-api
- collection_type: open
  name: Binance Algo Trading Account Market Data API
  slug: open-binance-market-data-api
- collection_type: open
  name: Binance Algo Trading Account Mining API
  slug: open-binance-mining-api
- collection_type: open
  name: Binance Mining API
  slug: open-binance-mining
- collection_type: open
  name: Binance Algo Trading Account NFT API
  slug: open-binance-nft-api
- collection_type: open
  name: Binance NFT API
  slug: open-binance-nft
- collection_type: open
  name: Binance Algo Trading Account Orders API
  slug: open-binance-orders-api
- collection_type: open
  name: Binance Pay API
  slug: open-binance-pay
- collection_type: open
  name: Binance Algo Trading Account Payouts API
  slug: open-binance-payouts-api
- collection_type: open
  name: Binance Portfolio Margin API
  slug: open-binance-portfolio-margin
- collection_type: open
  name: Binance Algo Trading Account Refunds API
  slug: open-binance-refunds-api
- collection_type: open
  name: Binance Simple Earn API
  slug: open-binance-simple-earn
- collection_type: open
  name: Binance Algo Trading Account Spot Algo API
  slug: open-binance-spot-algo-api
- collection_type: open
  name: Binance Spot Trading API
  slug: open-binance-spot-trading
- collection_type: open
  name: Binance Algo Trading Account Sub-Account Assets API
  slug: open-binance-sub-account-assets-api
- collection_type: open
  name: Binance Algo Trading Account Sub-Account Management API
  slug: open-binance-sub-account-management-api
- collection_type: open
  name: Binance Sub-Account API
  slug: open-binance-sub-account
- collection_type: open
  name: Binance Algo Account Trading API
  slug: open-binance-trading-api
- collection_type: open
  name: Binance USD-S Margined Futures API
  slug: open-binance-usds-margined-futures
- collection_type: open
  name: Binance Algo Trading Account User Data Stream API
  slug: open-binance-user-data-stream-api
- collection_type: open
  name: Binance Wallet API
  slug: open-binance-wallet
- collection_type: open
  name: Binance Algo Trading Account Withdrawals API
  slug: open-binance-withdrawals-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/binance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/binance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/binance-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/binance
- group: start
  title: ''
  type: Portal
  url: https://developers.binance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.binance.com/docs/binance-spot-api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/binance
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/rules/binance-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/vocabulary/binance-vocabulary.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/binance/binance-skills-hub
created: '2025-01-01'
description: Binance is the world's largest cryptocurrency exchange by trading volume, providing APIs for spot trading, futures, margin, wallet management, and market data across 19+ specialized REST APIs and WebSocket streams.
features:
- description: Buy and sell 500+ cryptocurrency pairs with limit, market, and stop-loss orders.
  name: Spot Trading
- description: Trade perpetual and delivery futures contracts settled in USDT.
  name: USD-M Futures
- description: Trade perpetual and delivery futures contracts settled in cryptocurrency.
  name: Coin-M Futures
- description: Trade on margin with up to 10x leverage using borrowed assets.
  name: Margin Trading
- description: Place algorithmic orders using TWAP, VP, and other execution strategies.
  name: Algo Trading
- description: Real-time market data streams for price, depth, and trade updates.
  name: WebSocket Streams
- description: Manage deposits, withdrawals, and asset transfers between wallets.
  name: Wallet Management
- description: Earn interest on idle cryptocurrency assets through flexible and locked products.
  name: Simple Earn
finops:
- name: Binance Finops
  service_category: Financial Services / Trading
  slug: binance-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Binance API surface. Binance exposes its functionality through REST and WebSocket APIs. This schema models the same domain objects and opera
  name: Binance GraphQL Schema
  slug: binance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/binance.png
integrations:
- description: Connect Binance to TradingView for charting and automated alert-based trading.
  name: TradingView
- description: Use MetaTrader bridge adapters to trade Binance from MT4/MT5.
  name: MetaTrader
- description: Receive Binance trade notifications and alerts via Telegram bot.
  name: Telegram
- description: Run serverless trading bots triggered by events on AWS Lambda.
  name: AWS Lambda
- description: Access Binance through the CCXT unified cryptocurrency exchange library.
  name: Python CCXT
json_schemas:
- name: Binance Account
  property_count: 16
  slug: binance-account
- name: AccountTrade
  property_count: 13
  slug: binance-accounttrade
- name: AggTrade
  property_count: 8
  slug: binance-aggtrade
- name: Balance
  property_count: 3
  slug: binance-balance
- name: BookTicker
  property_count: 5
  slug: binance-bookticker
- name: CancelOrderResponse
  property_count: 15
  slug: binance-cancelorderresponse
- name: Error
  property_count: 2
  slug: binance-error
- name: ExchangeInfo
  property_count: 5
  slug: binance-exchangeinfo
- name: Fill
  property_count: 5
  slug: binance-fill
- name: FuturesAccount
  property_count: 19
  slug: binance-futuresaccount
- name: FuturesBalance
  property_count: 9
  slug: binance-futuresbalance
- name: FuturesOrder
  property_count: 23
  slug: binance-futuresorder
- name: FuturesOrderResponse
  property_count: 23
  slug: binance-futuresorderresponse
- name: FuturesSymbol
  property_count: 17
  slug: binance-futuressymbol
- name: FuturesTicker24hr
  property_count: 16
  slug: binance-futuresticker24hr
- name: FuturesTrade
  property_count: 6
  slug: binance-futurestrade
- name: MarkPrice
  property_count: 8
  slug: binance-markprice
- name: OcoOrderResponse
  property_count: 9
  slug: binance-ocoorderresponse
- name: Binance Order
  property_count: 27
  slug: binance-order
- name: OrderBook
  property_count: 3
  slug: binance-orderbook
- name: OrderResponse
  property_count: 16
  slug: binance-orderresponse
- name: PositionRisk
  property_count: 16
  slug: binance-positionrisk
- name: PriceTicker
  property_count: 2
  slug: binance-priceticker
- name: RateLimit
  property_count: 4
  slug: binance-ratelimit
- name: SymbolInfo
  property_count: 13
  slug: binance-symbolinfo
- name: Ticker24hr
  property_count: 21
  slug: binance-ticker24hr
- name: Binance Trade
  property_count: 14
  slug: binance-trade
json_structures:
- name: Binance Structure
  property_count: 0
  slug: binance-structure
jsonld:
- class_count: 0
  name: Binance Context
  property_count: 8
  slug: binance-context
layout: provider
modified: '2026-05-19'
name: Binance
nav: Providers
network: true
overview: 'Binance publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Spot WebSocket API, Spot WebSocket Streams, Account API, and 25 more. Tagged areas include Cryptocurrency, Exchange, Trading, Blockchain, and Finance.


  The Binance catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Binance''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 8 more developer resources.'
plans:
- name: Binance Plans Pricing
  plan_count: 4
  slug: binance-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Binance Rate Limits
  slug: binance-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Binance API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: binance-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Binance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: binance-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: Binance API Rules
  rule_count: 30
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 19
  slug: binance-spectral-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 66.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binance/refs/heads/main/screenshots/binance-2026-06-20T173243.png
security:
- kind: authentication
  name: Binance Authentication
  slug: binance-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Binance Domain Security
  slug: binance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Binance Vulnerability Disclosure
  slug: binance-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 14
skills:
- name: binance-agentic-wallet
  slug: binance-agentic-wallet
- name: binance-tokenized-securities-info
  slug: binance-tokenized-securities-info
- name: binance
  slug: binance
- name: crypto-market-rank
  slug: crypto-market-rank
- name: fiat
  slug: fiat
- name: meme-rush
  slug: meme-rush
- name: onchain-pay-open-api
  slug: onchain-pay-open-api
- name: p2p
  slug: p2p
- name: payment-assistant
  slug: payment-assistant
- name: query-address-info
  slug: query-address-info
- name: query-token-audit
  slug: query-token-audit
- name: query-token-info
  slug: query-token-info
- name: square-post
  slug: square-post
- name: trading-signal
  slug: trading-signal
slug: binance
tags:
- Cryptocurrency
- Exchange
- Trading
- Blockchain
- Finance
- DeFi
- Market Data
use_cases:
- description: Build automated trading bots using Binance REST and WebSocket APIs.
  name: Algorithmic Trading
- description: Track and rebalance cryptocurrency portfolios programmatically.
  name: Portfolio Management
- description: Aggregate real-time price and order book data for analysis or display.
  name: Market Data Aggregation
- description: Bridge centralized Binance liquidity into DeFi protocols.
  name: DeFi Integration
- description: Exploit price differences across Binance spot, futures, and margin markets.
  name: Arbitrage Trading
website: https://developers.binance.com/
---
