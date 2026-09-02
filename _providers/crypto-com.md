---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: WebSocket API for the Crypto.com Exchange, split into a Market Data stream (public channels for book, ticker, trade, candlestick, index, mark price, settlement, funding and open interest) and a User A
  name: Crypto.com Exchange WebSocket API v1
  slug: cryptocom-exchange-websocket-api-v1
- description: FIX 4.4-based API for institutional order entry, market data and drop copy on the Crypto.com Exchange, with tags borrowed from later FIX versions. Covers Logon/Logout, NewOrderSingle, MassOrder, Order
  name: Crypto.com Exchange FIX API
  slug: cryptocom-exchange-fix-api
- description: Merchant payments API for accepting cryptocurrency payments, issuing refunds, running subscriptions and recurring invoices, managing customers, products and sub-merchants, and reading transaction hist
  name: Crypto.com Pay API
  slug: cryptocom-pay-api
- description: On-chain developer platform service API for Cronos EVM and Cronos zkEVM, exposing native and ERC-20 token balances and transfers, smart contract ABI and bytecode lookup, transaction and block queries,
  name: Crypto.com Developer Platform API
  slug: cryptocom-developer-platform-api
- description: 'Retrieve real-time and historical snapshots of wallet balances, open positions, margin requirements, and collateral status. Use these endpoints to monitor account health, risk exposure, and available '
  name: Crypto.com Account Balance and Positions API
  slug: crypto-com-account-balance-and-positions-api
- description: 'Advanced Order Management provides trigger orders and multi-leg execution strategies beyond basic LIMIT and MARKET orders. Use these endpoints for conditional order execution based on price triggers. '
  name: Crypto.com Advanced Order Management API
  slug: crypto-com-advanced-order-management-api
- description: Manages the user's wallet. Most of the endpoints are only available at master account level. Some endpoints requires Withdrawal setting to be enabled for your API Key. If you do not see the option whe
  name: Crypto.com Crypto Wallet API
  slug: crypto-com-crypto-wallet-api
- description: Manages the user's fiat wallet. Most of the endpoints are only available at master account level. Some endpoints requires Withdrawal setting to be enabled for your API Key. If you do not see the optio
  name: Crypto.com Fiat Wallet API
  slug: crypto-com-fiat-wallet-api
- description: OTC RFQ (Request For Quote) enables takers to request block trade quotes from multiple liquidity providers, evaluate received quotes, and execute trades at the best available price. This workflow is d
  name: Crypto.com OTC RFQ for Taker API
  slug: crypto-com-otc-rfq-for-taker-api
- description: Reference and market data endpoints provide public, unauthenticated access to instrument metadata, real-time market data, and historical pricing information. These endpoints form the foundation for pr
  name: Crypto.com Reference and Market Data API
  slug: crypto-com-reference-and-market-data-api
- description: 'Stake crypto assets on-chain to earn rewards directly from the Exchange. Staking locks your tokens for a period, during which you earn periodic rewards. Liquid staking tokens (e.g., CDCETH) allow you '
  name: Crypto.com Staking API
  slug: crypto-com-staking-api
- description: Private trading endpoints manage order placement and lifecycle. All order operations (create, amend, cancel) are asynchronous — the REST response confirms the request was received, but order lifecycle
  name: Crypto.com Trading API
  slug: crypto-com-trading-api
- description: 'Manage automated trading bots including DCA (Dollar-Cost Averaging), TWAP (Time-Weighted Average Price), GRID, and Funding Arbitrage strategies. ## Bot Types | Type | Description | |------|-----------'
  name: Crypto.com Trading Bot API
  slug: crypto-com-trading-bot-api-api
- description: History will be stored for recent 6 months record only. For records over 6 months, please contact our support team.
  name: Crypto.com Transaction History API
  slug: crypto-com-transaction-history-api
artifact_total: 23
asyncapis:
- description: ''
  name: Crypto Com Event Surface
  slug: crypto-com-event-surface
collections:
- collection_type: open
  name: Crypto.com Exchange API v1
  slug: open-crypto-com-exchange
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/crypto-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crypto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crypto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://exchange-developer.crypto.com/exchange/v1
- group: docs
  title: ''
  type: Documentation
  url: https://exchange-developer.crypto.com/exchange/v1/docs/api/rest-introduction
- group: docs
  title: ''
  type: APIReference
  url: https://exchange-developer.crypto.com/exchange/v1/docs/api/rest/crypto-com-exchange-api-v-1
- group: start
  title: ''
  type: GettingStarted
  url: https://exchange-developer.crypto.com/exchange/v1/docs/api/rest-common-api-reference
- group: operate
  title: ''
  type: Support
  url: https://help.crypto.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.crypto.com/en/
- group: company
  title: ''
  type: Blog
  url: https://crypto.com/en/product-news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crypto-com
- group: commercial
  title: ''
  type: Pricing
  url: https://crypto.com/exchange/fee
- group: start
  title: ''
  type: SignUp
  url: https://crypto.com/exchange/signup
- group: start
  title: ''
  type: Login
  url: https://crypto.com/exchange/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crypto.com/exchange/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crypto.com/en/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crypto.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crypto-com-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://exchange-developer.crypto.com/exchange/v1/docs/api/rest-breaking-change-schedule
- group: auth
  title: ''
  type: Security
  url: https://help.crypto.com/en/articles/9154034-vulnerability-disclosure-and-bug-bounty
- group: auth
  title: ''
  type: Compliance
  url: https://crypto.com/en/security
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/crypto-com-exchange-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crypto-com-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/crypto-com-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/crypto-com-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/crypto-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crypto-com-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crypto-com-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crypto-com-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crypto-com-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/crypto-com-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crypto-com-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crypto-com-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crypto-com-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crypto-com-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crypto-com-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crypto-com-event-surface.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crypto-com-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crypto-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://crypto.com/en/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crypto-com-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crypto-com-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crypto-com-exchange-overlay.yaml
created: '2026-08-11'
description: 'Crypto.com is a cryptocurrency exchange, brokerage and payments company serving retail and institutional customers across spot, margin and derivatives trading, staking, custody, card and payment acceptance, and on-chain development on the Cronos EVM and Cronos zkEVM networks. Its public developer surface spans four programmable products: the Crypto.com Exchange API v1 (REST, WebSocket and FIX 4.4) for market data, order entry, advanced OCO/OTO/OTOCO orders, trading bots, portfolio, wallet and staking operations; the Crypto.com Pay API for merchant payment acceptance, refunds, subscriptions and invoicing with webhooks and idempotent refunds; the Crypto.com Developer Platform API for Cronos tokens, contracts, transactions, blocks, wallets, CronosID and DeFi; and an agent layer consisting of a published MCP server, an agent-first Rust CLI, and provider-authored Agent Skills for trading through the Crypto.com App and Exchange.'
image: https://crypto.com/images/meta-og/listing.png
layout: provider
mcp_servers:
- description: ''
  name: Crypto.com MCP Server
  slug: cryptocom-mcp-server
modified: '2026-08-11'
name: Crypto.com
nav: Providers
network: true
overview: 'Crypto.com publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account Balance and Positions API, Advanced Order Management API, Crypto Wallet API, and 7 more. Tagged areas include Cryptocurrency, Crypto Exchange, Trading, Derivatives, and Market Data.


  The Crypto.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crypto.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Crypto Com Plans Pricing
  plan_count: 0
  slug: crypto-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 11
  name: Crypto Com Rate Limits
  slug: crypto-com-rate-limits
score:
  band: exemplar
  composite: 68.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 60.4
    developer_ergonomics: 85.7
    discoverability: 51.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 69.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 70.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crypto-com/refs/heads/main/screenshots/crypto-com-2026-08-17T080411.png
security:
- kind: authentication
  name: Crypto Com Authentication
  slug: crypto-com-authentication
  summary_line: apiKey/http/custom-hmac · 6 schemes
- kind: domain-security
  name: Crypto Com Domain Security
  slug: crypto-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crypto Com Vulnerability Disclosure
  slug: crypto-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Crypto Com Trust Center
  slug: crypto-com-trust-center
  summary_line: ISO 27001, PCI DSS
slug: crypto-com
tags:
- Cryptocurrency
- Crypto Exchange
- Trading
- Derivatives
- Market Data
- Digital Assets
- Payments
- Merchant Payments
- Blockchain
- cronos
- DeFi
- Staking
- Fintech
- MCP
- agent-native
website: https://crypto.com/
---
