---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bitoasis Agentic Access
  operation_count: 23
  slug: bitoasis-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 7
apis:
- description: Authenticated account balances and registered banks.
  name: BitOasis Account API
  slug: bitoasis-account-api
- description: Digital-asset deposit history and address generation.
  name: BitOasis Coin Deposits API
  slug: bitoasis-coin-deposits-api
- description: Digital-asset withdrawal history, fees, and creation.
  name: BitOasis Coin Withdrawals API
  slug: bitoasis-coin-withdrawals-api
- description: Fiat deposit history.
  name: BitOasis Fiat Deposits API
  slug: bitoasis-fiat-deposits-api
- description: Fiat withdrawal history, creation, and cancellation.
  name: BitOasis Fiat Withdrawals API
  slug: bitoasis-fiat-withdrawals-api
- description: Public market data endpoints (no authentication required).
  name: BitOasis Market Data API
  slug: bitoasis-market-data-api
- description: Place, cancel, and read Pro exchange orders.
  name: BitOasis Orders API
  slug: bitoasis-orders-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://bitoasis.net/en/home
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bitoasis.net/doc/
- group: docs
  title: ''
  type: Documentation
  url: https://api.bitoasis.net/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://api.bitoasis.net/doc/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.bitoasis.net/en/support/solutions/articles/29000035643-api-documentation
- group: operate
  title: ''
  type: Support
  url: https://support.bitoasis.net/
- group: company
  title: ''
  type: Blog
  url: https://blog.bitoasis.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bit-oasis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitoasis.net/en/page/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitoasis.net/en/page/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://bitoasis.net/en/page/legal-and-compliance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitoasis-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitoasis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitoasis-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitoasis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitoasis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitoasis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitoasis-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitoasis-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitoasis-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitoasis-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitoasis-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitoasis-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitoasis-agentic-access.yml
created: '2026-07-17'
description: BitOasis is a Middle East and North Africa (MENA) cryptocurrency exchange, licensed as a Virtual Asset Service Provider by Dubai's Virtual Assets Regulatory Authority (VARA). It lets customers buy, sell, and trade Bitcoin, Ether, XRP, and other digital assets against the UAE Dirham (AED) and other fiat currencies. BitOasis exposes a public v1 Exchange REST API (https://api.bitoasis.net/v1) covering market data (markets, tickers, order books, trades) and authenticated account operations (balances, banks, Pro order placement and cancellation, and crypto and fiat deposits and withdrawals), authenticated with a Bearer API token. BitOasis also publishes an official open-source MCP server (bitoasis-mcp) that exposes the exchange as 23 tools for AI agents, over stdio or a hosted SSE endpoint. Originally added to the API Evangelist network as a pantera-capital portfolio lead, this profile has been enriched from BitOasis' first-party public developer surface.
image: https://bitoasis.net/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bitoasis-mcp.yml
  slug: bitoasis-mcpyml
modified: '2026-07-18'
name: BitOasis
nav: Providers
network: true
overview: 'BitOasis publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Coin Deposits API, Coin Withdrawals API, and 4 more. Tagged areas include Company, Crypto, Cryptocurrency, Exchange, and Trading.


  BitOasis'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 50.6
  delta: 2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.7
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 48.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Bitoasis Authentication
  slug: bitoasis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitoasis Domain Security
  slug: bitoasis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitoasis
tags:
- Company
- Crypto
- Cryptocurrency
- Exchange
- Trading
- Digital Assets
- Bitcoin
- MENA
- Fintech
- MCP
website: https://bitoasis.net/en/home
---
