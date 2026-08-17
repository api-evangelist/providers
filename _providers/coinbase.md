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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Coinbase Agentic Access
  operation_count: 95
  slug: coinbase-agentic-access
  summary_line: 95 operations · 32 acting
api_count: 29
apis:
- description: The Coinbase Wallet SDK allows developers to integrate Coinbase Wallet connectivity into decentralized applications. It provides a streamlined interface for users to connect their wallets, sign transa
  name: Coinbase Wallet SDK
  slug: wallet-sdk
- description: The Coinbase Data API provides developers with access to cryptocurrency market data, blockchain analytics, and pricing information. It delivers real-time and historical data for a wide range of digita
  name: Coinbase Data API
  slug: data-api
- description: Coinbase AgentKit is a toolkit that enables AI agents to interact with blockchain networks through secure wallet management and comprehensive onchain capabilities. Built on the Coinbase Developer Plat
  name: Coinbase AgentKit
  slug: agentkit
- description: Manage user accounts and retrieve account information including balances and holds.
  name: Coinbase Accounts API
  slug: coinbase-accounts-api
- description: View activity history for portfolios including trades, transfers, and other events.
  name: Coinbase Activities API
  slug: coinbase-activities-api
- description: Manage approved withdrawal addresses in the address book.
  name: Coinbase Address Book API
  slug: coinbase-address-book-api
- description: View and manage order allocations across sub-portfolios.
  name: Coinbase Allocations API
  slug: coinbase-allocations-api
- description: Retrieve information about supported assets and products.
  name: Coinbase Assets API
  slug: coinbase-assets-api
- description: Retrieve portfolio balance information across all assets.
  name: Coinbase Balances API
  slug: coinbase-balances-api
- description: Endpoints for discovering buy options, generating buy quotes, and retrieving buy configuration for fiat-to-crypto purchases.
  name: Coinbase Buy API
  slug: coinbase-buy-api
- description: Create and manage payment charges. A charge represents a request for cryptocurrency payment from a customer.
  name: Coinbase Charges API
  slug: coinbase-charges-api
- description: Create and manage reusable checkout pages for accepting recurring or standardized payments.
  name: Coinbase Checkouts API
  slug: coinbase-checkouts-api
- description: Convert between stablecoin currencies on the exchange.
  name: Coinbase Conversions API
  slug: coinbase-conversions-api
- description: Retrieve information about supported currencies on the exchange.
  name: Coinbase Currencies API
  slug: coinbase-currencies-api
- description: View deposit information and payment methods for funding exchange accounts.
  name: Coinbase Deposits API
  slug: coinbase-deposits-api
- description: Retrieve webhook events that track the lifecycle of charges, checkouts, and invoices.
  name: Coinbase Events API
  slug: coinbase-events-api
- description: Retrieve transaction summary and fee information for the authenticated user.
  name: Coinbase Fees API
  slug: coinbase-fees-api
- description: Create and manage invoices for billing customers with cryptocurrency payment options.
  name: Coinbase Invoices API
  slug: coinbase-invoices-api
- description: Access public market data including products, order books, trades, and candles without authentication.
  name: Coinbase Market Data API
  slug: coinbase-market-data-api
- description: Create, cancel, and manage trading orders including market, limit, and stop-limit order types.
  name: Coinbase Orders API
  slug: coinbase-orders-api
- description: Create and manage portfolios for organizing trading activity and asset allocation.
  name: Coinbase Portfolios API
  slug: coinbase-portfolios-api
- description: Retrieve product information, market trades, product books, and candle data for trading pairs.
  name: Coinbase Products API
  slug: coinbase-products-api
- description: Manage exchange profiles and transfer funds between them.
  name: Coinbase Profiles API
  slug: coinbase-profiles-api
- description: Endpoints for discovering sell options and generating sell quotes for crypto-to-fiat transactions.
  name: Coinbase Sell API
  slug: coinbase-sell-api
- description: Manage session tokens for embedded onramp widget authentication.
  name: Coinbase Session API
  slug: coinbase-session-api
- description: View and create transactions including withdrawals and transfers.
  name: Coinbase Transactions API
  slug: coinbase-transactions-api
- description: Manage users associated with a portfolio.
  name: Coinbase Users API
  slug: coinbase-users-api
- description: Manage wallets within a portfolio for different asset types.
  name: Coinbase Wallets API
  slug: coinbase-wallets-api
- description: Manage crypto withdrawals from exchange accounts to external addresses or Coinbase accounts.
  name: Coinbase Withdrawals API
  slug: coinbase-withdrawals-api
artifact_total: 146
asyncapis:
- description: The Coinbase Advanced Trade WebSocket API provides real-time market data streaming including heartbeats, ticker updates, candle data, market trades, level2 order book updates, and user order status ch
  name: Coinbase Advanced Trade WebSocket
  slug: coinbase-advanced-trade-asyncapi
- description: Coinbase Commerce sends webhook events to notify your application when charges are created, confirmed, delayed, pending, failed, or resolved. Each webhook event is signed with a SHA-256 HMAC signature
  name: Coinbase Commerce Webhooks
  slug: coinbase-commerce-webhooks-asyncapi
- description: The Coinbase Exchange WebSocket Feed provides real-time market data for the Exchange platform. It supports multiple channels including heartbeat, ticker, level2 order book, full order feed, and user o
  name: Coinbase Exchange WebSocket Feed
  slug: coinbase-exchange-asyncapi
collections:
- collection_type: postman
  name: Coinbase Advanced Trade Accounts API
  slug: postman-coinbase-accounts-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Activities API
  slug: postman-coinbase-activities-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Address Book API
  slug: postman-coinbase-address-book-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Allocations API
  slug: postman-coinbase-allocations-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Assets API
  slug: postman-coinbase-assets-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Balances API
  slug: postman-coinbase-balances-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Buy API
  slug: postman-coinbase-buy-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Charges API
  slug: postman-coinbase-charges-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Checkouts API
  slug: postman-coinbase-checkouts-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Conversions API
  slug: postman-coinbase-conversions-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Currencies API
  slug: postman-coinbase-currencies-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Deposits API
  slug: postman-coinbase-deposits-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Events API
  slug: postman-coinbase-events-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Fees API
  slug: postman-coinbase-fees-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Invoices API
  slug: postman-coinbase-invoices-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Market Data API
  slug: postman-coinbase-market-data-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Orders API
  slug: postman-coinbase-orders-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Portfolios API
  slug: postman-coinbase-portfolios-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Products API
  slug: postman-coinbase-products-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Profiles API
  slug: postman-coinbase-profiles-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Sell API
  slug: postman-coinbase-sell-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Session API
  slug: postman-coinbase-session-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Transactions API
  slug: postman-coinbase-transactions-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Users API
  slug: postman-coinbase-users-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Wallets API
  slug: postman-coinbase-wallets-api
- collection_type: postman
  name: Coinbase Advanced Trade Accounts Withdrawals API
  slug: postman-coinbase-withdrawals-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coinbase Advanced Trade Accounts API
  slug: open-coinbase-accounts-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Activities API
  slug: open-coinbase-activities-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Address Book API
  slug: open-coinbase-address-book-api
- collection_type: open
  name: Coinbase Advanced Trade API
  slug: open-coinbase-advanced-trade
- collection_type: open
  name: Coinbase Advanced Trade Accounts Allocations API
  slug: open-coinbase-allocations-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Assets API
  slug: open-coinbase-assets-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Balances API
  slug: open-coinbase-balances-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Buy API
  slug: open-coinbase-buy-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Charges API
  slug: open-coinbase-charges-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Checkouts API
  slug: open-coinbase-checkouts-api
- collection_type: open
  name: Coinbase Commerce API
  slug: open-coinbase-commerce
- collection_type: open
  name: Coinbase Advanced Trade Accounts Conversions API
  slug: open-coinbase-conversions-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Currencies API
  slug: open-coinbase-currencies-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Deposits API
  slug: open-coinbase-deposits-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Events API
  slug: open-coinbase-events-api
- collection_type: open
  name: Coinbase Exchange API
  slug: open-coinbase-exchange
- collection_type: open
  name: Coinbase Advanced Trade Accounts Fees API
  slug: open-coinbase-fees-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Invoices API
  slug: open-coinbase-invoices-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Market Data API
  slug: open-coinbase-market-data-api
- collection_type: open
  name: Coinbase Onramp API
  slug: open-coinbase-onramp
- collection_type: open
  name: Coinbase Advanced Trade Accounts Orders API
  slug: open-coinbase-orders-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Portfolios API
  slug: open-coinbase-portfolios-api
- collection_type: open
  name: Coinbase Prime API
  slug: open-coinbase-prime
- collection_type: open
  name: Coinbase Advanced Trade Accounts Products API
  slug: open-coinbase-products-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Profiles API
  slug: open-coinbase-profiles-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Sell API
  slug: open-coinbase-sell-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Session API
  slug: open-coinbase-session-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Transactions API
  slug: open-coinbase-transactions-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Users API
  slug: open-coinbase-users-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Wallets API
  slug: open-coinbase-wallets-api
- collection_type: open
  name: Coinbase Advanced Trade Accounts Withdrawals API
  slug: open-coinbase-withdrawals-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coinbase/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coinbase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinbase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinbase
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.coinbase.com/developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cdp.coinbase.com/
- group: company
  title: ''
  type: Website
  url: https://www.coinbase.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coinbase.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coinbase
- group: start
  title: ''
  type: Login
  url: https://login.coinbase.com/
- group: operate
  title: ''
  type: Support
  url: https://help.coinbase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinbase.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinbase.com/legal/user-agreement
- group: design
  title: ''
  type: JSONLD
  url: json-ld/coinbase-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-charge-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/coinbase-product-schema.json
- group: design
  title: ''
  type: Spectral Ruleset
  url: rules/coinbase-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cdp.coinbase.com/llms.txt
created: '2026-03-20'
description: Coinbase is a leading cryptocurrency platform providing trading, custody, and payment infrastructure for individuals, businesses, and institutions. The Coinbase Developer Platform (CDP) exposes a wide product surface across retail trading (Advanced Trade), professional and institutional trading (Exchange and Prime), merchant payments (Commerce), fiat onboarding (Onramp), developer wallet integration (Wallet SDK), market and on-chain data (Data API), and AI agent toolkits (AgentKit). Authentication is performed using API keys with HMAC-SHA256 signatures (Advanced Trade, Exchange) or JWT bearer tokens (Prime, CDP), with WebSocket and FIX feeds available for low-latency market data and order management.
finops:
- name: Coinbase Finops
  service_category: Financial Services
  slug: coinbase-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Coinbase Developer Platform. Coinbase exposes its capabilities through REST APIs (Advanced Trade, Exchange, Prime, Commerce, Onramp) and Web
  name: Coinbase GraphQL Schema
  slug: coinbase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinbase.png
json_schemas:
- name: Account
  property_count: 11
  slug: coinbase-account
- name: Activity
  property_count: 8
  slug: coinbase-activity
- name: AddressBookEntry
  property_count: 5
  slug: coinbase-addressbookentry
- name: Allocation
  property_count: 10
  slug: coinbase-allocation
- name: Balance
  property_count: 2
  slug: coinbase-balance
- name: BuyConfig
  property_count: 1
  slug: coinbase-buyconfig
- name: BuyQuote
  property_count: 6
  slug: coinbase-buyquote
- name: BuyQuoteRequest
  property_count: 6
  slug: coinbase-buyquoterequest
- name: Candle
  property_count: 6
  slug: coinbase-candle
- name: Coinbase Commerce Charge
  property_count: 17
  slug: coinbase-charge
- name: Checkout
  property_count: 7
  slug: coinbase-checkout
- name: Conversion
  property_count: 6
  slug: coinbase-conversion
- name: CreateChargeRequest
  property_count: 7
  slug: coinbase-createchargerequest
- name: CreateCheckoutRequest
  property_count: 5
  slug: coinbase-createcheckoutrequest
- name: CreateInvoiceRequest
  property_count: 5
  slug: coinbase-createinvoicerequest
- name: CreateOrderRequest
  property_count: 4
  slug: coinbase-createorderrequest
- name: Currency
  property_count: 5
  slug: coinbase-currency
- name: Event
  property_count: 6
  slug: coinbase-event
- name: Fill
  property_count: 10
  slug: coinbase-fill
- name: Hold
  property_count: 5
  slug: coinbase-hold
- name: Invoice
  property_count: 11
  slug: coinbase-invoice
- name: LedgerEntry
  property_count: 6
  slug: coinbase-ledgerentry
- name: Coinbase Order
  property_count: 22
  slug: coinbase-order
- name: OrderBook
  property_count: 3
  slug: coinbase-orderbook
- name: Pagination
  property_count: 6
  slug: coinbase-pagination
- name: Payment
  property_count: 5
  slug: coinbase-payment
- name: PaymentCurrency
  property_count: 5
  slug: coinbase-paymentcurrency
- name: PaymentMethod
  property_count: 8
  slug: coinbase-paymentmethod
- name: Portfolio
  property_count: 4
  slug: coinbase-portfolio
- name: PortfolioBreakdown
  property_count: 3
  slug: coinbase-portfoliobreakdown
- name: PriceBook
  property_count: 4
  slug: coinbase-pricebook
- name: Coinbase Trading Product
  property_count: 20
  slug: coinbase-product
- name: Profile
  property_count: 6
  slug: coinbase-profile
- name: PurchaseCurrency
  property_count: 5
  slug: coinbase-purchasecurrency
- name: SellQuote
  property_count: 4
  slug: coinbase-sellquote
- name: SellQuoteRequest
  property_count: 5
  slug: coinbase-sellquoterequest
- name: Ticker
  property_count: 7
  slug: coinbase-ticker
- name: Trade
  property_count: 6
  slug: coinbase-trade
- name: Transaction
  property_count: 11
  slug: coinbase-transaction
- name: TransactionSummary
  property_count: 5
  slug: coinbase-transactionsummary
- name: Transfer
  property_count: 6
  slug: coinbase-transfer
- name: User
  property_count: 4
  slug: coinbase-user
- name: Wallet
  property_count: 5
  slug: coinbase-wallet
json_structures:
- name: Coinbase Structure
  property_count: 0
  slug: coinbase-structure
jsonld:
- class_count: 0
  name: Coinbase Context
  property_count: 9
  slug: coinbase-context
layout: provider
modified: '2026-05-19'
name: Coinbase
nav: Providers
network: true
overview: 'Coinbase publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Address Book API, and 23 more. Tagged areas include Blockchain, Cryptocurrency, Custody, Exchange, and Onramp.


  The Coinbase catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Coinbase''s developer surface includes authentication, documentation, engineering blog, GitHub presence, support, and 16 more developer resources.'
plans:
- name: Coinbase Plans Pricing
  plan_count: 11
  slug: coinbase-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 4
  name: Coinbase Rate Limits
  slug: coinbase-rate-limits
rules:
- name: Coinbase API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: coinbase-asyncapi-spectral-rules
- name: Coinbase API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: coinbase-jsonschema-spectral-rules
- name: Coinbase API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: coinbase-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 76.6
    developer_ergonomics: 39.1
    discoverability: 66.7
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 51.0
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
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinbase/refs/heads/main/screenshots/coinbase-2026-06-20T174726.png
security:
- kind: authentication
  name: Coinbase Authentication
  slug: coinbase-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Coinbase Domain Security
  slug: coinbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinbase Vulnerability Disclosure
  slug: coinbase-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coinbase
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
website: https://www.coinbase.com/
---
