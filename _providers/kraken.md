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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Kraken Agentic Access
  operation_count: 71
  slug: kraken-agentic-access
  summary_line: 71 operations · 45 acting
api_count: 24
apis:
- description: 'Real-time market data and private user data over WebSocket v2 using subscribe/unsubscribe semantics. Public channels include ticker (L1), book (L2), trade, ohlc, instrument, and admin frames (status, '
  name: Kraken Spot WebSocket API v2
  slug: kraken-spot-websocket-api-v2
- description: Legacy Kraken Spot WebSocket API. Continues to operate alongside v2 but v2 is the recommended path for new integrations. Public channels include ticker, book, trade, ohlc, spread; private channels inc
  name: Kraken Spot WebSocket API v1 (Legacy)
  slug: kraken-spot-websocket-api-v1-legacy
- description: Real-time market data and private user feeds for Kraken Futures over WebSocket. Public feeds include trade, book, ticker, ticker_lite, heartbeat; private feeds include fills, open_positions, open_orde
  name: Kraken Futures WebSocket API
  slug: kraken-futures-websocket-api
- description: FIX 4.4 / 5.0 SP2 protocol access for Kraken Spot and Futures, used by institutional and high-frequency clients. Provides order management (NewOrderSingle, OrderCancelRequest, OrderCancelReplaceReques
  name: Kraken FIX API
  slug: kraken-fix-api
- description: 'REST API for Kraken''s NFT marketplace surfaces: collections, asset lookups, listings, offers, watchlist, and user portfolio views. The NFT API is consumed alongside the Spot REST API using the same AP'
  name: Kraken NFT API
  slug: kraken-nft-api
- description: REST endpoints for Kraken Earn (staking, yield, rewards). Lists strategies, allocates funds to a strategy, deallocates funds, and surfaces allocation status and reward history.
  name: Kraken Earn API
  slug: kraken-earn-api
- description: B2B integration API enabling partners to embed Kraken trading, custody, and Earn capabilities into their own products. Provides user management, assets, deposits, withdrawals, quote-based and custom o
  name: Kraken Embed REST API
  slug: kraken-embed-rest-api
- description: OAuth 2.0 authorization surface allowing third-party applications to request scoped delegated access to a Kraken account holder's data and trading capabilities.
  name: Kraken OAuth REST API
  slug: kraken-oauth-rest-api
- description: Fiat on/off-ramp API surface that lets partner applications offer crypto purchase and conversion experiences powered by Kraken liquidity.
  name: Kraken Ramp REST API
  slug: kraken-ramp-rest-api
- description: Institutional custody API providing programmatic access to vaulting, sub-vaulting, wallet generation, transfers, and policy/governance configuration for assets held in Kraken Custody.
  name: Kraken Custody REST API
  slug: kraken-custody-rest-api
- description: Over-the-counter execution API for institutional clients to request quotes (RFQ), execute block trades, and retrieve OTC trade history.
  name: Kraken OTC REST API
  slug: kraken-otc-rest-api
- description: Prime brokerage API surface (REST, WebSocket, FIX) for institutional clients consolidating execution, custody, financing, and reporting under a single relationship.
  name: Kraken Prime REST + WebSocket + FIX API
  slug: kraken-prime-rest-websocket-fix-api
- description: Accounts, positions, orders, fills
  name: Kraken Account API
  slug: kraken-account-api
- description: Private endpoints returning account-scoped data
  name: Kraken Account Data API
  slug: kraken-account-data-api
- description: API key checks
  name: Kraken Auth API
  slug: kraken-auth-api
- description: OHLC candle data and analytics
  name: Kraken Charts API
  slug: kraken-charts-api
- description: Staking and yield allocation endpoints
  name: Kraken Earn API
  slug: kraken-earn-api
- description: Private endpoints for deposits, withdrawals, and transfers
  name: Kraken Funding API
  slug: kraken-funding-api
- description: Account, execution, order, trigger, and market history
  name: Kraken History API
  slug: kraken-history-api
- description: Public market data (no authentication required)
  name: Kraken Market Data API
  slug: kraken-market-data-api
- description: Subaccount creation and inter-account transfers
  name: Kraken Subaccounts API
  slug: kraken-subaccounts-api
- description: Order placement, edit, and cancellation
  name: Kraken Trading API
  slug: kraken-trading-api
- description: Wallet, margin, and subaccount transfers
  name: Kraken Transfers API
  slug: kraken-transfers-api
- description: Endpoints that mint tokens for private WebSocket subscriptions
  name: Kraken WebSocket API
  slug: kraken-websocket-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List open orders, amend one in place, then confirm the new terms.
  name: Kraken Amend an Open Order
  slug: kraken-amend-open-order-workflow
- description: Read the account balance and live ticker, then branch on funding before buying.
  name: Kraken Balance-Aware Spot Buy
  slug: kraken-balance-aware-buy-workflow
- description: Inspect an order, cancel it, then place a replacement order.
  name: Kraken Cancel and Replace a Spot Order
  slug: kraken-cancel-and-replace-order-workflow
- description: Pick an Earn strategy, allocate funds, then poll until the allocation settles.
  name: Kraken Allocate Earn Funds and Confirm
  slug: kraken-earn-allocate-and-confirm-workflow
- description: Check spot balance, transfer to the futures wallet, then confirm it landed.
  name: Kraken Fund the Futures Wallet from Spot
  slug: kraken-fund-futures-wallet-workflow
- description: Pull account balances, open positions, and recent fills for a futures risk view.
  name: Kraken Futures Account Snapshot
  slug: kraken-futures-account-snapshot-workflow
- description: Check instrument status and ticker, place a futures order, then confirm it is open.
  name: Kraken Place a Futures Order
  slug: kraken-place-futures-order-workflow
- description: Check system status and live ticker, place a spot order, then confirm it.
  name: Kraken Preflight and Place Spot Order
  slug: kraken-preflight-place-spot-order-workflow
- description: Pull trade history, drill into specific trades, then tie them to ledger entries.
  name: Kraken Reconcile Spot Trade History
  slug: kraken-reconcile-trade-history-workflow
- description: Check balance and withdrawal fees, withdraw to a saved address, then track status.
  name: Kraken Withdraw Funds with Fee Preview
  slug: kraken-withdraw-funds-workflow
artifact_total: 389
asyncapis:
- description: 'Public WebSocket API for the Kraken cryptocurrency exchange (Spot v2). Provides real-time market data through subscribe/unsubscribe semantics over JSON. Channels documented here are restricted to the '
  name: Kraken Spot WebSocket API v2
  slug: kraken-asyncapi
collections:
- collection_type: postman
  name: Kraken Futures REST API
  slug: postman-kraken-futures-rest
- collection_type: postman
  name: Kraken Spot REST API
  slug: postman-kraken-spot-rest
- collection_type: open
  name: Kraken Futures REST API
  slug: open-kraken-futures-rest
- collection_type: open
  name: Kraken Spot REST API
  slug: open-kraken-spot-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kraken-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kraken-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kraken-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kraken-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kraken-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kraken/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-amend-open-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-balance-aware-buy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-cancel-and-replace-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-earn-allocate-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-fund-futures-wallet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-futures-account-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-place-futures-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-preflight-place-spot-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-reconcile-trade-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kraken-withdraw-funds-workflow.yml
- group: build
  title: ''
  type: Packages
  url: packages/kraken-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kraken-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kraken-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kraken-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kraken-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kraken-spot-rest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kraken-futures-rest-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kraken-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kraken-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kraken-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kraken-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kraken-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kraken-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/kraken-cli.yml
- group: company
  title: ''
  type: Website
  url: https://www.kraken.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.kraken.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kraken.com/api/docs/guides/global-intro
- group: start
  title: ''
  type: Signup
  url: https://www.kraken.com/sign-up
- group: auth
  title: ''
  type: Authentication
  url: https://docs.kraken.com/api/docs/guides/spot-rest-auth
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kraken.com/features/fee-schedule
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kraken.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kraken.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.kraken.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kraken.com/
- group: operate
  title: ''
  type: Support
  url: https://support.kraken.com/
- group: operate
  title: ''
  type: FAQ
  url: https://support.kraken.com/categories/360001393671-Trading-Funding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krakenfx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CryptoFacilities
- group: build
  title: ''
  type: SDKs
  url: https://github.com/krakenfx/api-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/krakenfx/kraken-api-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/krakenfx/kraken-wsclient-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/REST-v3-Python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/REST-v3-Java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/REST-v3-CSharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/REST-v3-NodeJs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/REST-v3-kotlin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/WebSocket-v1-Python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/WebSocket-v1-CSharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CryptoFacilities/WebSocket-v1-Rust
- group: build
  title: ''
  type: CLI
  url: https://github.com/krakenfx/kraken-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/krakenfx/kraken-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/oilst/kraken-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/krakenfx/wallet
- group: design
  title: ''
  type: SpectralRules
  url: rules/kraken-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kraken-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kraken-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/kraken-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kraken-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kraken-finops.yml
created: '2026-05-28'
description: Kraken is one of the world's largest and longest-running cryptocurrency exchanges, founded in 2011 and headquartered in San Francisco. Kraken offers Spot and Futures trading, staking and yield through Kraken Earn, NFT marketplace access, OTC services, custody, prime brokerage, and a B2B Embed surface for partners. Kraken exposes a comprehensive set of APIs spanning REST, WebSocket, and FIX across the Spot exchange, Futures exchange (Kraken Futures, formerly Crypto Facilities), institutional services (Custody, OTC, Prime), and partner integration surfaces (Embed, Ramp, OAuth).
examples:
- key_count: 3
  name: Futures Rest Batch Order Futures 200 Example
  slug: futures-rest-batch-order-futures-200-example
- key_count: 3
  name: Futures Rest Cancel All Orders After Futures 200 Example
  slug: futures-rest-cancel-all-orders-after-futures-200-example
- key_count: 3
  name: Futures Rest Cancel All Orders Futures 200 Example
  slug: futures-rest-cancel-all-orders-futures-200-example
- key_count: 3
  name: Futures Rest Cancel Order Futures 200 Example
  slug: futures-rest-cancel-order-futures-200-example
- key_count: 3
  name: Futures Rest Check Api Key V3 200 Example
  slug: futures-rest-check-api-key-v3-200-example
- key_count: 3
  name: Futures Rest Edit Order Futures 200 Example
  slug: futures-rest-edit-order-futures-200-example
- key_count: 3
  name: Futures Rest Get Account Log 200 Example
  slug: futures-rest-get-account-log-200-example
- key_count: 4
  name: Futures Rest Get Accounts 200 Example
  slug: futures-rest-get-accounts-200-example
- key_count: 3
  name: Futures Rest Get Chart Candles 200 Example
  slug: futures-rest-get-chart-candles-200-example
- key_count: 3
  name: Futures Rest Get Fills 200 Example
  slug: futures-rest-get-fills-200-example
- key_count: 3
  name: Futures Rest Get Historical Executions 200 Example
  slug: futures-rest-get-historical-executions-200-example
- key_count: 3
  name: Futures Rest Get Historical Orders 200 Example
  slug: futures-rest-get-historical-orders-200-example
- key_count: 3
  name: Futures Rest Get Historical Triggers 200 Example
  slug: futures-rest-get-historical-triggers-200-example
- key_count: 4
  name: Futures Rest Get Instruments 200 Example
  slug: futures-rest-get-instruments-200-example
- key_count: 3
  name: Futures Rest Get Instruments Status 200 Example
  slug: futures-rest-get-instruments-status-200-example
- key_count: 3
  name: Futures Rest Get Market History 200 Example
  slug: futures-rest-get-market-history-200-example
- key_count: 3
  name: Futures Rest Get Notifications 200 Example
  slug: futures-rest-get-notifications-200-example
- key_count: 3
  name: Futures Rest Get Open Orders Futures 200 Example
  slug: futures-rest-get-open-orders-futures-200-example
- key_count: 3
  name: Futures Rest Get Open Positions Futures 200 Example
  slug: futures-rest-get-open-positions-futures-200-example
- key_count: 3
  name: Futures Rest Get Order Book Futures 200 Example
  slug: futures-rest-get-order-book-futures-200-example
- key_count: 3
  name: Futures Rest Get Ticker For Symbol 200 Example
  slug: futures-rest-get-ticker-for-symbol-200-example
- key_count: 4
  name: Futures Rest Get Tickers 200 Example
  slug: futures-rest-get-tickers-200-example
- key_count: 3
  name: Futures Rest Send Order 200 Example
  slug: futures-rest-send-order-200-example
- key_count: 3
  name: Futures Rest Transfer Futures 200 Example
  slug: futures-rest-transfer-futures-200-example
- key_count: 3
  name: Futures Rest Withdrawal Futures 200 Example
  slug: futures-rest-withdrawal-futures-200-example
- key_count: 2
  name: Spot Rest Account Transfer 200 Example
  slug: spot-rest-account-transfer-200-example
- key_count: 2
  name: Spot Rest Add Order 200 Example
  slug: spot-rest-add-order-200-example
- key_count: 2
  name: Spot Rest Add Order Batch 200 Example
  slug: spot-rest-add-order-batch-200-example
- key_count: 2
  name: Spot Rest Allocate Earn Funds 200 Example
  slug: spot-rest-allocate-earn-funds-200-example
- key_count: 2
  name: Spot Rest Amend Order 200 Example
  slug: spot-rest-amend-order-200-example
- key_count: 2
  name: Spot Rest Cancel All Orders 200 Example
  slug: spot-rest-cancel-all-orders-200-example
- key_count: 2
  name: Spot Rest Cancel All Orders After 200 Example
  slug: spot-rest-cancel-all-orders-after-200-example
- key_count: 2
  name: Spot Rest Cancel Order 200 Example
  slug: spot-rest-cancel-order-200-example
- key_count: 2
  name: Spot Rest Cancel Order Batch 200 Example
  slug: spot-rest-cancel-order-batch-200-example
- key_count: 2
  name: Spot Rest Cancel Withdrawal 200 Example
  slug: spot-rest-cancel-withdrawal-200-example
- key_count: 2
  name: Spot Rest Create Subaccount 200 Example
  slug: spot-rest-create-subaccount-200-example
- key_count: 2
  name: Spot Rest Deallocate Earn Funds 200 Example
  slug: spot-rest-deallocate-earn-funds-200-example
- key_count: 2
  name: Spot Rest Edit Order 200 Example
  slug: spot-rest-edit-order-200-example
- key_count: 2
  name: Spot Rest Get Account Balance 200 Example
  slug: spot-rest-get-account-balance-200-example
- key_count: 2
  name: Spot Rest Get Asset Info 200 Example
  slug: spot-rest-get-asset-info-200-example
- key_count: 2
  name: Spot Rest Get Closed Orders 200 Example
  slug: spot-rest-get-closed-orders-200-example
- key_count: 2
  name: Spot Rest Get Deposit Addresses 200 Example
  slug: spot-rest-get-deposit-addresses-200-example
- key_count: 2
  name: Spot Rest Get Deposit Methods 200 Example
  slug: spot-rest-get-deposit-methods-200-example
- key_count: 2
  name: Spot Rest Get Deposit Status 200 Example
  slug: spot-rest-get-deposit-status-200-example
- key_count: 2
  name: Spot Rest Get Earn Allocate Status 200 Example
  slug: spot-rest-get-earn-allocate-status-200-example
- key_count: 2
  name: Spot Rest Get Earn Deallocate Status 200 Example
  slug: spot-rest-get-earn-deallocate-status-200-example
- key_count: 2
  name: Spot Rest Get Extended Balance 200 Example
  slug: spot-rest-get-extended-balance-200-example
- key_count: 2
  name: Spot Rest Get Ledgers Info 200 Example
  slug: spot-rest-get-ledgers-info-200-example
- key_count: 2
  name: Spot Rest Get Ohlc Data 200 Example
  slug: spot-rest-get-ohlc-data-200-example
- key_count: 2
  name: Spot Rest Get Open Orders 200 Example
  slug: spot-rest-get-open-orders-200-example
- key_count: 2
  name: Spot Rest Get Open Positions 200 Example
  slug: spot-rest-get-open-positions-200-example
- key_count: 2
  name: Spot Rest Get Order Book 200 Example
  slug: spot-rest-get-order-book-200-example
- key_count: 2
  name: Spot Rest Get Recent Spreads 200 Example
  slug: spot-rest-get-recent-spreads-200-example
- key_count: 2
  name: Spot Rest Get Recent Trades 200 Example
  slug: spot-rest-get-recent-trades-200-example
- key_count: 2
  name: Spot Rest Get Server Time 200 Example
  slug: spot-rest-get-server-time-200-example
- key_count: 2
  name: Spot Rest Get System Status 200 Example
  slug: spot-rest-get-system-status-200-example
- key_count: 2
  name: Spot Rest Get Ticker Information 200 Example
  slug: spot-rest-get-ticker-information-200-example
- key_count: 2
  name: Spot Rest Get Tradable Asset Pairs 200 Example
  slug: spot-rest-get-tradable-asset-pairs-200-example
- key_count: 2
  name: Spot Rest Get Trade Balance 200 Example
  slug: spot-rest-get-trade-balance-200-example
- key_count: 2
  name: Spot Rest Get Trade Volume 200 Example
  slug: spot-rest-get-trade-volume-200-example
- key_count: 2
  name: Spot Rest Get Trades History 200 Example
  slug: spot-rest-get-trades-history-200-example
- key_count: 2
  name: Spot Rest Get Web Sockets Token 200 Example
  slug: spot-rest-get-web-sockets-token-200-example
- key_count: 2
  name: Spot Rest Get Withdrawal Info 200 Example
  slug: spot-rest-get-withdrawal-info-200-example
- key_count: 2
  name: Spot Rest Get Withdrawal Status 200 Example
  slug: spot-rest-get-withdrawal-status-200-example
- key_count: 2
  name: Spot Rest List Earn Allocations 200 Example
  slug: spot-rest-list-earn-allocations-200-example
- key_count: 2
  name: Spot Rest List Earn Strategies 200 Example
  slug: spot-rest-list-earn-strategies-200-example
- key_count: 2
  name: Spot Rest Query Ledgers 200 Example
  slug: spot-rest-query-ledgers-200-example
- key_count: 2
  name: Spot Rest Query Orders Info 200 Example
  slug: spot-rest-query-orders-info-200-example
- key_count: 2
  name: Spot Rest Query Trades Info 200 Example
  slug: spot-rest-query-trades-info-200-example
- key_count: 2
  name: Spot Rest Wallet Transfer 200 Example
  slug: spot-rest-wallet-transfer-200-example
- key_count: 2
  name: Spot Rest Withdraw Funds 200 Example
  slug: spot-rest-withdraw-funds-200-example
features:
- description: Spot trading on 200+ cryptocurrency pairs with limit, market, stop loss, take profit, stop-loss-limit, take-profit-limit, settle position, trailing stop, and iceberg order types.
  name: Spot Trading
- description: Margin trading on supported pairs with leverage up to 5x for eligible users in eligible jurisdictions.
  name: Margin Trading
- description: Perpetual and fixed-maturity futures on Bitcoin, Ethereum, and other major assets via Kraken Futures.
  name: Futures Trading
- description: On-chain and off-chain staking plus opt-in bonded yield strategies across supported proof-of-stake and DeFi assets.
  name: Kraken Earn (Staking and Yield)
- description: Browse, list, bid, and buy NFTs across Ethereum and Solana with gas-free transactions and fiat settlement.
  name: NFT Marketplace
- description: Logical subaccount creation and inter-account transfers for institutional and family-office structuring.
  name: Subaccounts
- description: White-label trading, custody, and Earn primitives that partners can embed into their own consumer or business products.
  name: Embed (B2B Integration)
- description: OAuth 2.0 surface enabling third-party apps to act on a user's behalf with scoped permissions.
  name: OAuth Delegated Access
- description: Colocation endpoints in London (colo-london.*) for ultra-low-latency access to Spot, Futures, FIX, and WebSocket surfaces.
  name: Co-located Connectivity
- description: FIX 4.4 / 5.0 SP2 connectivity for institutional execution and market data flows.
  name: FIX Connectivity
- description: Modern WebSocket v2 surface supporting subscribe/unsubscribe for market data and authenticated request/response trading methods.
  name: WebSocket v2 with Authenticated Trading
- description: Automatic cancellation of resting orders when the trading session terminates, protecting algorithmic strategies from runaway risk.
  name: Cancel on Disconnect
finops:
- name: Kraken Finops
  service_category: Cryptocurrency Exchange + Brokerage
  slug: kraken-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Kraken cryptocurrency exchange API. Kraken's public API is REST and WebSocket based (see the [Kraken REST API docs](https://docs.kraken.com/
  name: Kraken GraphQL Schema
  slug: kraken-graphql
image: https://assets.kraken.com/marketing/web/kraken-logo.svg
integrations:
- description: Kraken Futures uses the Crypto Facilities REST v3 and WebSocket v1 protocols, with public GitHub example clients in multiple languages.
  name: Crypto Facilities (Kraken Futures)
- description: Self-custody wallet that signs transactions locally; integrates with dApps and uses Kraken-published OAuth helpers.
  name: Kraken Wallet
- description: The Kraken CLI ships an embedded MCP server so any MCP-compatible agent runtime (Claude, Gemini, Cursor) can drive Kraken accounts.
  name: Model Context Protocol
- description: Kraken markets are available as a charting source on TradingView, and Kraken Pro embeds TradingView charts in its web client.
  name: TradingView
- description: Kraken Spot is supported as a first-class exchange adapter in the CCXT cryptocurrency exchange library.
  name: CCXT
json_schemas:
- name: Account
  property_count: 6
  slug: futures-rest-account
- name: AccountsResponse
  property_count: 0
  slug: futures-rest-accounts-response
- name: EditOrderFuturesRequest
  property_count: 7
  slug: futures-rest-edit-order-futures-request
- name: Instrument
  property_count: 10
  slug: futures-rest-instrument
- name: InstrumentsResponse
  property_count: 0
  slug: futures-rest-instruments-response
- name: SendOrderRequest
  property_count: 11
  slug: futures-rest-send-order-request
- name: Ticker
  property_count: 18
  slug: futures-rest-ticker
- name: TickersResponse
  property_count: 0
  slug: futures-rest-tickers-response
- name: Asset
  property_count: 8
  slug: kraken-asset
- name: BookData
  property_count: 5
  slug: kraken-book-data
- name: BookEnvelope
  property_count: 3
  slug: kraken-book-envelope
- name: Candle
  property_count: 10
  slug: kraken-candle
- name: InstrumentEnvelope
  property_count: 3
  slug: kraken-instrument-envelope
- name: OHLCEnvelope
  property_count: 3
  slug: kraken-ohlc-envelope
- name: Pair
  property_count: 16
  slug: kraken-pair
- name: PingRequest
  property_count: 2
  slug: kraken-ping-request
- name: PongResponse
  property_count: 8
  slug: kraken-pong-response
- name: PriceLevel
  property_count: 2
  slug: kraken-price-level
- name: SubscribeBookRequest
  property_count: 0
  slug: kraken-subscribe-book-request
- name: SubscribeInstrumentRequest
  property_count: 0
  slug: kraken-subscribe-instrument-request
- name: SubscribeOHLCRequest
  property_count: 0
  slug: kraken-subscribe-ohlc-request
- name: SubscribeRequestBase
  property_count: 2
  slug: kraken-subscribe-request-base
- name: SubscribeTickerRequest
  property_count: 0
  slug: kraken-subscribe-ticker-request
- name: SubscribeTradeRequest
  property_count: 0
  slug: kraken-subscribe-trade-request
- name: SubscriptionStatusResponse
  property_count: 8
  slug: kraken-subscription-status-response
- name: TickerEnvelope
  property_count: 3
  slug: kraken-ticker-envelope
- name: Ticker
  property_count: 12
  slug: kraken-ticker
- name: TradeEnvelope
  property_count: 3
  slug: kraken-trade-envelope
- name: Trade
  property_count: 7
  slug: kraken-trade
- name: UnsubscribeBookRequest
  property_count: 0
  slug: kraken-unsubscribe-book-request
- name: UnsubscribeInstrumentRequest
  property_count: 0
  slug: kraken-unsubscribe-instrument-request
- name: UnsubscribeOHLCRequest
  property_count: 0
  slug: kraken-unsubscribe-ohlc-request
- name: UnsubscribeRequestBase
  property_count: 2
  slug: kraken-unsubscribe-request-base
- name: UnsubscribeTickerRequest
  property_count: 0
  slug: kraken-unsubscribe-ticker-request
- name: UnsubscribeTradeRequest
  property_count: 0
  slug: kraken-unsubscribe-trade-request
- name: AccountTransferRequest
  property_count: 0
  slug: spot-rest-account-transfer-request
- name: AccountTransferResponse
  property_count: 0
  slug: spot-rest-account-transfer-response
- name: AddOrderBatchRequest
  property_count: 0
  slug: spot-rest-add-order-batch-request
- name: AddOrderBatchResponse
  property_count: 0
  slug: spot-rest-add-order-batch-response
- name: AddOrderRequest
  property_count: 0
  slug: spot-rest-add-order-request
- name: AddOrderResponse
  property_count: 0
  slug: spot-rest-add-order-response
- name: AmendOrderRequest
  property_count: 0
  slug: spot-rest-amend-order-request
- name: AmendOrderResponse
  property_count: 0
  slug: spot-rest-amend-order-response
- name: AssetInfoResponse
  property_count: 0
  slug: spot-rest-asset-info-response
- name: AssetInfo
  property_count: 6
  slug: spot-rest-asset-info
- name: AssetPair
  property_count: 20
  slug: spot-rest-asset-pair
- name: AssetPairsResponse
  property_count: 0
  slug: spot-rest-asset-pairs-response
- name: BalanceExResponse
  property_count: 0
  slug: spot-rest-balance-ex-response
- name: BalanceResponse
  property_count: 0
  slug: spot-rest-balance-response
- name: CancelAllAfterRequest
  property_count: 0
  slug: spot-rest-cancel-all-after-request
- name: CancelAllAfterResponse
  property_count: 0
  slug: spot-rest-cancel-all-after-response
- name: CancelAllResponse
  property_count: 0
  slug: spot-rest-cancel-all-response
- name: CancelOrderBatchRequest
  property_count: 0
  slug: spot-rest-cancel-order-batch-request
- name: CancelOrderBatchResponse
  property_count: 0
  slug: spot-rest-cancel-order-batch-response
- name: CancelOrderRequest
  property_count: 0
  slug: spot-rest-cancel-order-request
- name: CancelOrderResponse
  property_count: 0
  slug: spot-rest-cancel-order-response
- name: ClosedOrdersRequest
  property_count: 0
  slug: spot-rest-closed-orders-request
- name: ClosedOrdersResponse
  property_count: 0
  slug: spot-rest-closed-orders-response
- name: CreateSubaccountRequest
  property_count: 0
  slug: spot-rest-create-subaccount-request
- name: CreateSubaccountResponse
  property_count: 0
  slug: spot-rest-create-subaccount-response
- name: DepositAddressesRequest
  property_count: 0
  slug: spot-rest-deposit-addresses-request
- name: DepositAddressesResponse
  property_count: 0
  slug: spot-rest-deposit-addresses-response
- name: DepositMethodsResponse
  property_count: 0
  slug: spot-rest-deposit-methods-response
- name: DepositStatusRequest
  property_count: 0
  slug: spot-rest-deposit-status-request
- name: DepositStatusResponse
  property_count: 0
  slug: spot-rest-deposit-status-response
- name: EarnAllocateRequest
  property_count: 0
  slug: spot-rest-earn-allocate-request
- name: EarnAllocationsResponse
  property_count: 0
  slug: spot-rest-earn-allocations-response
- name: EarnSimpleResponse
  property_count: 0
  slug: spot-rest-earn-simple-response
- name: EarnStatusResponse
  property_count: 0
  slug: spot-rest-earn-status-response
- name: EarnStrategiesRequest
  property_count: 0
  slug: spot-rest-earn-strategies-request
- name: EarnStrategiesResponse
  property_count: 0
  slug: spot-rest-earn-strategies-response
- name: EarnStrategy
  property_count: 12
  slug: spot-rest-earn-strategy
- name: EditOrderRequest
  property_count: 0
  slug: spot-rest-edit-order-request
- name: EditOrderResponse
  property_count: 0
  slug: spot-rest-edit-order-response
- name: FundingTxn
  property_count: 11
  slug: spot-rest-funding-txn
- name: LedgerEntry
  property_count: 9
  slug: spot-rest-ledger-entry
- name: LedgersRequest
  property_count: 0
  slug: spot-rest-ledgers-request
- name: LedgersResponse
  property_count: 0
  slug: spot-rest-ledgers-response
- name: OHLCResponse
  property_count: 0
  slug: spot-rest-ohlc-response
- name: OpenOrdersRequest
  property_count: 0
  slug: spot-rest-open-orders-request
- name: OpenOrdersResponse
  property_count: 0
  slug: spot-rest-open-orders-response
- name: OpenPositionsRequest
  property_count: 0
  slug: spot-rest-open-positions-request
- name: OpenPositionsResponse
  property_count: 0
  slug: spot-rest-open-positions-response
- name: OrderBookResponse
  property_count: 0
  slug: spot-rest-order-book-response
- name: OrderBook
  property_count: 2
  slug: spot-rest-order-book
- name: OrderInfo
  property_count: 18
  slug: spot-rest-order-info
- name: Position
  property_count: 17
  slug: spot-rest-position
- name: QueryLedgersRequest
  property_count: 0
  slug: spot-rest-query-ledgers-request
- name: QueryLedgersResponse
  property_count: 0
  slug: spot-rest-query-ledgers-response
- name: QueryOrdersRequest
  property_count: 0
  slug: spot-rest-query-orders-request
- name: QueryOrdersResponse
  property_count: 0
  slug: spot-rest-query-orders-response
- name: QueryTradesRequest
  property_count: 0
  slug: spot-rest-query-trades-request
- name: QueryTradesResponse
  property_count: 0
  slug: spot-rest-query-trades-response
- name: RecentSpreadsResponse
  property_count: 0
  slug: spot-rest-recent-spreads-response
- name: RecentTradesResponse
  property_count: 0
  slug: spot-rest-recent-trades-response
- name: ServerTimeResponse
  property_count: 0
  slug: spot-rest-server-time-response
- name: SystemStatusResponse
  property_count: 0
  slug: spot-rest-system-status-response
- name: TickerResponse
  property_count: 0
  slug: spot-rest-ticker-response
- name: Ticker
  property_count: 9
  slug: spot-rest-ticker
- name: TradeBalanceRequest
  property_count: 0
  slug: spot-rest-trade-balance-request
- name: TradeBalanceResponse
  property_count: 0
  slug: spot-rest-trade-balance-response
- name: TradeInfo
  property_count: 13
  slug: spot-rest-trade-info
- name: TradeVolumeRequest
  property_count: 0
  slug: spot-rest-trade-volume-request
- name: TradeVolumeResponse
  property_count: 0
  slug: spot-rest-trade-volume-response
- name: TradesHistoryRequest
  property_count: 0
  slug: spot-rest-trades-history-request
- name: TradesHistoryResponse
  property_count: 0
  slug: spot-rest-trades-history-response
- name: WalletTransferRequest
  property_count: 0
  slug: spot-rest-wallet-transfer-request
- name: WalletTransferResponse
  property_count: 0
  slug: spot-rest-wallet-transfer-response
- name: WebSocketsTokenResponse
  property_count: 0
  slug: spot-rest-web-sockets-token-response
- name: WithdrawCancelRequest
  property_count: 0
  slug: spot-rest-withdraw-cancel-request
- name: WithdrawCancelResponse
  property_count: 0
  slug: spot-rest-withdraw-cancel-response
- name: WithdrawInfoRequest
  property_count: 0
  slug: spot-rest-withdraw-info-request
- name: WithdrawInfoResponse
  property_count: 0
  slug: spot-rest-withdraw-info-response
- name: WithdrawRequest
  property_count: 0
  slug: spot-rest-withdraw-request
- name: WithdrawResponse
  property_count: 0
  slug: spot-rest-withdraw-response
- name: WithdrawStatusRequest
  property_count: 0
  slug: spot-rest-withdraw-status-request
- name: WithdrawStatusResponse
  property_count: 0
  slug: spot-rest-withdraw-status-response
json_structures:
- name: Futures Rest Account Structure
  property_count: 6
  slug: futures-rest-account-structure
- name: Futures Rest Accounts Response Structure
  property_count: 0
  slug: futures-rest-accounts-response-structure
- name: Futures Rest Edit Order Futures Request Structure
  property_count: 7
  slug: futures-rest-edit-order-futures-request-structure
- name: Futures Rest Instrument Structure
  property_count: 10
  slug: futures-rest-instrument-structure
- name: Futures Rest Instruments Response Structure
  property_count: 0
  slug: futures-rest-instruments-response-structure
- name: Futures Rest Send Order Request Structure
  property_count: 11
  slug: futures-rest-send-order-request-structure
- name: Futures Rest Ticker Structure
  property_count: 18
  slug: futures-rest-ticker-structure
- name: Futures Rest Tickers Response Structure
  property_count: 0
  slug: futures-rest-tickers-response-structure
- name: Kraken Asset Structure
  property_count: 8
  slug: kraken-asset-structure
- name: Kraken Book Data Structure
  property_count: 5
  slug: kraken-book-data-structure
- name: Kraken Book Envelope Structure
  property_count: 3
  slug: kraken-book-envelope-structure
- name: Kraken Candle Structure
  property_count: 10
  slug: kraken-candle-structure
- name: Kraken Instrument Envelope Structure
  property_count: 3
  slug: kraken-instrument-envelope-structure
- name: Kraken Ohlc Envelope Structure
  property_count: 3
  slug: kraken-ohlc-envelope-structure
- name: Kraken Pair Structure
  property_count: 16
  slug: kraken-pair-structure
- name: Kraken Ping Request Structure
  property_count: 2
  slug: kraken-ping-request-structure
- name: Kraken Pong Response Structure
  property_count: 8
  slug: kraken-pong-response-structure
- name: Kraken Price Level Structure
  property_count: 2
  slug: kraken-price-level-structure
- name: Kraken Subscribe Book Request Structure
  property_count: 0
  slug: kraken-subscribe-book-request-structure
- name: Kraken Subscribe Instrument Request Structure
  property_count: 0
  slug: kraken-subscribe-instrument-request-structure
- name: Kraken Subscribe Ohlc Request Structure
  property_count: 0
  slug: kraken-subscribe-ohlc-request-structure
- name: Kraken Subscribe Request Base Structure
  property_count: 2
  slug: kraken-subscribe-request-base-structure
- name: Kraken Subscribe Ticker Request Structure
  property_count: 0
  slug: kraken-subscribe-ticker-request-structure
- name: Kraken Subscribe Trade Request Structure
  property_count: 0
  slug: kraken-subscribe-trade-request-structure
- name: Kraken Subscription Status Response Structure
  property_count: 8
  slug: kraken-subscription-status-response-structure
- name: Kraken Ticker Envelope Structure
  property_count: 3
  slug: kraken-ticker-envelope-structure
- name: Kraken Ticker Structure
  property_count: 12
  slug: kraken-ticker-structure
- name: Kraken Trade Envelope Structure
  property_count: 3
  slug: kraken-trade-envelope-structure
- name: Kraken Trade Structure
  property_count: 7
  slug: kraken-trade-structure
- name: Kraken Unsubscribe Book Request Structure
  property_count: 0
  slug: kraken-unsubscribe-book-request-structure
- name: Kraken Unsubscribe Instrument Request Structure
  property_count: 0
  slug: kraken-unsubscribe-instrument-request-structure
- name: Kraken Unsubscribe Ohlc Request Structure
  property_count: 0
  slug: kraken-unsubscribe-ohlc-request-structure
- name: Kraken Unsubscribe Request Base Structure
  property_count: 2
  slug: kraken-unsubscribe-request-base-structure
- name: Kraken Unsubscribe Ticker Request Structure
  property_count: 0
  slug: kraken-unsubscribe-ticker-request-structure
- name: Kraken Unsubscribe Trade Request Structure
  property_count: 0
  slug: kraken-unsubscribe-trade-request-structure
- name: Spot Rest Account Transfer Request Structure
  property_count: 0
  slug: spot-rest-account-transfer-request-structure
- name: Spot Rest Account Transfer Response Structure
  property_count: 0
  slug: spot-rest-account-transfer-response-structure
- name: Spot Rest Add Order Batch Request Structure
  property_count: 0
  slug: spot-rest-add-order-batch-request-structure
- name: Spot Rest Add Order Batch Response Structure
  property_count: 0
  slug: spot-rest-add-order-batch-response-structure
- name: Spot Rest Add Order Request Structure
  property_count: 0
  slug: spot-rest-add-order-request-structure
- name: Spot Rest Add Order Response Structure
  property_count: 0
  slug: spot-rest-add-order-response-structure
- name: Spot Rest Amend Order Request Structure
  property_count: 0
  slug: spot-rest-amend-order-request-structure
- name: Spot Rest Amend Order Response Structure
  property_count: 0
  slug: spot-rest-amend-order-response-structure
- name: Spot Rest Asset Info Response Structure
  property_count: 0
  slug: spot-rest-asset-info-response-structure
- name: Spot Rest Asset Info Structure
  property_count: 6
  slug: spot-rest-asset-info-structure
- name: Spot Rest Asset Pair Structure
  property_count: 20
  slug: spot-rest-asset-pair-structure
- name: Spot Rest Asset Pairs Response Structure
  property_count: 0
  slug: spot-rest-asset-pairs-response-structure
- name: Spot Rest Balance Ex Response Structure
  property_count: 0
  slug: spot-rest-balance-ex-response-structure
- name: Spot Rest Balance Response Structure
  property_count: 0
  slug: spot-rest-balance-response-structure
- name: Spot Rest Cancel All After Request Structure
  property_count: 0
  slug: spot-rest-cancel-all-after-request-structure
- name: Spot Rest Cancel All After Response Structure
  property_count: 0
  slug: spot-rest-cancel-all-after-response-structure
- name: Spot Rest Cancel All Response Structure
  property_count: 0
  slug: spot-rest-cancel-all-response-structure
- name: Spot Rest Cancel Order Batch Request Structure
  property_count: 0
  slug: spot-rest-cancel-order-batch-request-structure
- name: Spot Rest Cancel Order Batch Response Structure
  property_count: 0
  slug: spot-rest-cancel-order-batch-response-structure
- name: Spot Rest Cancel Order Request Structure
  property_count: 0
  slug: spot-rest-cancel-order-request-structure
- name: Spot Rest Cancel Order Response Structure
  property_count: 0
  slug: spot-rest-cancel-order-response-structure
- name: Spot Rest Closed Orders Request Structure
  property_count: 0
  slug: spot-rest-closed-orders-request-structure
- name: Spot Rest Closed Orders Response Structure
  property_count: 0
  slug: spot-rest-closed-orders-response-structure
- name: Spot Rest Create Subaccount Request Structure
  property_count: 0
  slug: spot-rest-create-subaccount-request-structure
- name: Spot Rest Create Subaccount Response Structure
  property_count: 0
  slug: spot-rest-create-subaccount-response-structure
- name: Spot Rest Deposit Addresses Request Structure
  property_count: 0
  slug: spot-rest-deposit-addresses-request-structure
- name: Spot Rest Deposit Addresses Response Structure
  property_count: 0
  slug: spot-rest-deposit-addresses-response-structure
- name: Spot Rest Deposit Methods Response Structure
  property_count: 0
  slug: spot-rest-deposit-methods-response-structure
- name: Spot Rest Deposit Status Request Structure
  property_count: 0
  slug: spot-rest-deposit-status-request-structure
- name: Spot Rest Deposit Status Response Structure
  property_count: 0
  slug: spot-rest-deposit-status-response-structure
- name: Spot Rest Earn Allocate Request Structure
  property_count: 0
  slug: spot-rest-earn-allocate-request-structure
- name: Spot Rest Earn Allocations Response Structure
  property_count: 0
  slug: spot-rest-earn-allocations-response-structure
- name: Spot Rest Earn Simple Response Structure
  property_count: 0
  slug: spot-rest-earn-simple-response-structure
- name: Spot Rest Earn Status Response Structure
  property_count: 0
  slug: spot-rest-earn-status-response-structure
- name: Spot Rest Earn Strategies Request Structure
  property_count: 0
  slug: spot-rest-earn-strategies-request-structure
- name: Spot Rest Earn Strategies Response Structure
  property_count: 0
  slug: spot-rest-earn-strategies-response-structure
- name: Spot Rest Earn Strategy Structure
  property_count: 12
  slug: spot-rest-earn-strategy-structure
- name: Spot Rest Edit Order Request Structure
  property_count: 0
  slug: spot-rest-edit-order-request-structure
- name: Spot Rest Edit Order Response Structure
  property_count: 0
  slug: spot-rest-edit-order-response-structure
- name: Spot Rest Funding Txn Structure
  property_count: 11
  slug: spot-rest-funding-txn-structure
- name: Spot Rest Ledger Entry Structure
  property_count: 9
  slug: spot-rest-ledger-entry-structure
- name: Spot Rest Ledgers Request Structure
  property_count: 0
  slug: spot-rest-ledgers-request-structure
- name: Spot Rest Ledgers Response Structure
  property_count: 0
  slug: spot-rest-ledgers-response-structure
- name: Spot Rest Ohlc Response Structure
  property_count: 0
  slug: spot-rest-ohlc-response-structure
- name: Spot Rest Open Orders Request Structure
  property_count: 0
  slug: spot-rest-open-orders-request-structure
- name: Spot Rest Open Orders Response Structure
  property_count: 0
  slug: spot-rest-open-orders-response-structure
- name: Spot Rest Open Positions Request Structure
  property_count: 0
  slug: spot-rest-open-positions-request-structure
- name: Spot Rest Open Positions Response Structure
  property_count: 0
  slug: spot-rest-open-positions-response-structure
- name: Spot Rest Order Book Response Structure
  property_count: 0
  slug: spot-rest-order-book-response-structure
- name: Spot Rest Order Book Structure
  property_count: 2
  slug: spot-rest-order-book-structure
- name: Spot Rest Order Info Structure
  property_count: 18
  slug: spot-rest-order-info-structure
- name: Spot Rest Position Structure
  property_count: 17
  slug: spot-rest-position-structure
- name: Spot Rest Query Ledgers Request Structure
  property_count: 0
  slug: spot-rest-query-ledgers-request-structure
- name: Spot Rest Query Ledgers Response Structure
  property_count: 0
  slug: spot-rest-query-ledgers-response-structure
- name: Spot Rest Query Orders Request Structure
  property_count: 0
  slug: spot-rest-query-orders-request-structure
- name: Spot Rest Query Orders Response Structure
  property_count: 0
  slug: spot-rest-query-orders-response-structure
- name: Spot Rest Query Trades Request Structure
  property_count: 0
  slug: spot-rest-query-trades-request-structure
- name: Spot Rest Query Trades Response Structure
  property_count: 0
  slug: spot-rest-query-trades-response-structure
- name: Spot Rest Recent Spreads Response Structure
  property_count: 0
  slug: spot-rest-recent-spreads-response-structure
- name: Spot Rest Recent Trades Response Structure
  property_count: 0
  slug: spot-rest-recent-trades-response-structure
- name: Spot Rest Server Time Response Structure
  property_count: 0
  slug: spot-rest-server-time-response-structure
- name: Spot Rest System Status Response Structure
  property_count: 0
  slug: spot-rest-system-status-response-structure
- name: Spot Rest Ticker Response Structure
  property_count: 0
  slug: spot-rest-ticker-response-structure
- name: Spot Rest Ticker Structure
  property_count: 9
  slug: spot-rest-ticker-structure
- name: Spot Rest Trade Balance Request Structure
  property_count: 0
  slug: spot-rest-trade-balance-request-structure
- name: Spot Rest Trade Balance Response Structure
  property_count: 0
  slug: spot-rest-trade-balance-response-structure
- name: Spot Rest Trade Info Structure
  property_count: 13
  slug: spot-rest-trade-info-structure
- name: Spot Rest Trade Volume Request Structure
  property_count: 0
  slug: spot-rest-trade-volume-request-structure
- name: Spot Rest Trade Volume Response Structure
  property_count: 0
  slug: spot-rest-trade-volume-response-structure
- name: Spot Rest Trades History Request Structure
  property_count: 0
  slug: spot-rest-trades-history-request-structure
- name: Spot Rest Trades History Response Structure
  property_count: 0
  slug: spot-rest-trades-history-response-structure
- name: Spot Rest Wallet Transfer Request Structure
  property_count: 0
  slug: spot-rest-wallet-transfer-request-structure
- name: Spot Rest Wallet Transfer Response Structure
  property_count: 0
  slug: spot-rest-wallet-transfer-response-structure
- name: Spot Rest Web Sockets Token Response Structure
  property_count: 0
  slug: spot-rest-web-sockets-token-response-structure
- name: Spot Rest Withdraw Cancel Request Structure
  property_count: 0
  slug: spot-rest-withdraw-cancel-request-structure
- name: Spot Rest Withdraw Cancel Response Structure
  property_count: 0
  slug: spot-rest-withdraw-cancel-response-structure
- name: Spot Rest Withdraw Info Request Structure
  property_count: 0
  slug: spot-rest-withdraw-info-request-structure
- name: Spot Rest Withdraw Info Response Structure
  property_count: 0
  slug: spot-rest-withdraw-info-response-structure
- name: Spot Rest Withdraw Request Structure
  property_count: 0
  slug: spot-rest-withdraw-request-structure
- name: Spot Rest Withdraw Response Structure
  property_count: 0
  slug: spot-rest-withdraw-response-structure
- name: Spot Rest Withdraw Status Request Structure
  property_count: 0
  slug: spot-rest-withdraw-status-request-structure
- name: Spot Rest Withdraw Status Response Structure
  property_count: 0
  slug: spot-rest-withdraw-status-response-structure
jsonld:
- class_count: 16
  name: Kraken Context
  property_count: 25
  slug: kraken-context
layout: provider
mcp_servers:
- description: ''
  name: kraken-mcp.yml
  slug: kraken-mcpyml
modified: '2026-06-20'
name: Kraken
nav: Providers
network: true
overview: 'Kraken publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Spot WebSocket API v2, Earn API, Account API, and 11 more. Tagged areas include Cryptocurrency, Exchange, Trading, Market Data, and Spot Trading.


  The Kraken catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Kraken''s developer surface includes authentication, sandbox, CLI, developer portal, getting-started guide, signup flow, pricing, and 58 more developer resources.'
plans:
- name: Kraken Plans Pricing
  plan_count: 8
  slug: kraken-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 16
  name: Kraken Rate Limits
  slug: kraken-rate-limits
rules:
- name: Kraken API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: kraken-asyncapi-spectral-rules
- name: Kraken API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kraken-jsonschema-spectral-rules
- name: Kraken API Rules
  rule_count: 35
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 17
  slug: kraken-rules
score:
  band: exemplar
  composite: 68.0
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 37.4
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 63.5
    operational_transparency: 52.6
  previous_composite: 68.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 83.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kraken/refs/heads/main/screenshots/kraken-2026-06-20T184148.png
security:
- kind: authentication
  name: Kraken Authentication
  slug: kraken-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kraken Domain Security
  slug: kraken-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kraken Vulnerability Disclosure
  slug: kraken-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kraken Trust Center
  slug: kraken-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: kraken
solutions:
- description: The simplified Kraken consumer app for buying, selling, sending, and staking crypto with a fixed 1.0% / 1.5% spread on instant and custom orders.
  name: Kraken
- description: The advanced trading platform with full Spot, Margin, and Futures surfaces, volume-tiered maker/taker fees from 0.25%/0.40% down to 0.00%/0.10% at $10M+ 30-day USD volume.
  name: Kraken Pro
- description: Institutional offering bundling Custody, OTC, Prime brokerage, colocation, FIX, and dedicated relationship management.
  name: Kraken Institutional
- description: B2B integration platform letting partners offer Kraken trading, custody, and Earn primitives inside their own products.
  name: Kraken Embed
tags:
- Cryptocurrency
- Exchange
- Trading
- Market Data
- Spot Trading
- Futures
- Derivatives
- Staking
- Earn
- NFT
- WebSocket
- FIX
- Custody
- OTC
- Prime Brokerage
- Embed
- OAuth
- Public APIs
use_cases:
- description: Build and operate automated trading strategies against Kraken Spot using REST for order management and WebSocket v2 for low-latency market data and execution streams.
  name: Algorithmic Spot Trading
- description: Use real-time order book and ticker feeds with low-latency colocation endpoints to power arbitrage strategies across Kraken and other venues.
  name: Cross-Exchange Arbitrage
- description: Run market-making strategies on Kraken Futures using batched order entry, WebSocket fills, and FIX for high-volume connectivity.
  name: Derivatives Market Making
- description: Manage corporate or fund treasury balances using Kraken Custody and programmatic transfers, deposits, and withdrawals.
  name: Treasury and Custody Operations
- description: Offer staking and yield products to end users via Kraken Earn allocation/deallocation endpoints, exposed through your own product.
  name: Staking-as-a-Service
- description: Partners (fintechs, neobanks, wallets) use Kraken Embed to add trading, conversion, and custody capabilities to their own apps without building exchange infrastructure.
  name: Embedded Crypto Brokerage
- description: Use the NFT API to power portfolio dashboards, valuation feeds, and collection-level analytics.
  name: NFT Portfolio Management
- description: Use the Kraken CLI's built-in MCP server (or the community oilst/kraken-mcp) to let LLM agents place orders, manage positions, and stream market data with tool-calling.
  name: AI Agent Trading
- description: Pull trades history, ledgers, deposits, and withdrawals to drive tax-lot accounting, regulatory reporting, and audit pipelines.
  name: Tax and Reporting Pipelines
website: https://www.kraken.com/
---
