---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.7
  scored_at: '2026-08-17'
api_count: 5
apis:
- description: 'REST API for the Crypto.com Exchange covering public reference and market data (instruments, order book, candlesticks, trades, tickers, valuations, settlement prices, insurance fund, risk parameters) '
  name: Crypto.com Exchange REST API v1
  slug: cryptocom-exchange-rest-api-v1
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
artifact_total: 14
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
  name: crypto-com-mcp.yml
  slug: crypto-com-mcpyml
modified: '2026-08-11'
name: Crypto.com
nav: Providers
network: true
overview: 'Crypto.com publishes 1 API on the [APIs.io](https://apis.io/) network: Exchange REST API v1. Tagged areas include cryptocurrency, crypto-exchange, trading, derivatives, and market-data.


  The Crypto.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crypto.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Crypto Com Plans Pricing
  plan_count: 0
  slug: crypto-com-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 11
  name: Crypto Com Rate Limits
  slug: crypto-com-rate-limits
score:
  band: exemplar
  composite: 67.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.2
    developer_ergonomics: 87.0
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 94.7
  previous_composite: 67.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 70.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- cryptocurrency
- crypto-exchange
- trading
- derivatives
- market-data
- digital-assets
- payments
- merchant-payments
- blockchain
- cronos
- defi
- staking
- fintech
- mcp
- agent-native
website: https://crypto.com/
---
