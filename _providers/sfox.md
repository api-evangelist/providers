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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: REST API for trading, order management, RFQ, account balances and transactions, transfers/deposits/withdrawals, custody (sFOX SAFE), staking, post-trade settlement, market data, and reporting. Bearer-
  name: sFOX REST API
  slug: sfox-rest-api
- description: Real-time streaming API for market data (order book, trades, ticker) and private account data (open orders, trades, balances, post-trade settlement). Authenticate then subscribe to feeds.
  name: sFOX WebSocket API
  slug: sfox-websocket-api
- description: 'White-label REST + WebSocket API for businesses: end-user management, KYC/KYB and Enhanced Due Diligence, bank-account linking (Plaid), ACH (Dwolla) and wire payments, withdrawals, transfers, monetiza'
  name: sFOX Connect API
  slug: sfox-connect-api
artifact_total: 8
asyncapis:
- description: 'Real-time streaming API for sFOX. Clients connect over WSS, authenticate with their API key (for private feeds), then subscribe/unsubscribe to feeds via a JSON control message: { "type": "subscribe", '
  name: sFOX WebSocket API
  slug: sfox-websocket-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sfox.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sfox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sfox.com/rest-api/rest-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sfox.com/introduction/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.sfox.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.sfox.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://trade.sfox.com/signup
- group: start
  title: ''
  type: Login
  url: https://trade.sfox.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sfox.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sfox.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sfox-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sfox-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sfox-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sfox-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sfox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sfox-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sfox-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sfox-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sfox-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sfox-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sfox-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sfox-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sfox-changelog.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sfox-websocket-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sfox-websocket-asyncapi.yml
created: '2026-07-17'
description: sFOX is a unified crypto prime brokerage and infrastructure platform for professional and institutional investors — asset managers, hedge funds, family offices, and financial institutions. It aggregates liquidity from 30+ providers across 80+ markets for smart-routed best execution, and combines that with bankruptcy-remote custody (sFOX SAFE, via SAFE Trust Company), staking, credit, and post-trade settlement in one platform. sFOX exposes a REST API, a WebSocket streaming API, and a FIX API for trading, account management, RFQ, transfers, custody, staking, market data, and reporting; a separate white-label "Connect" API covers end-user onboarding, KYC/KYB, bank linking (Plaid/Dwolla), payments, withdrawals, and SSO for businesses building crypto products.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sfox.png
layout: provider
mcp_servers:
- description: ''
  name: sfox-mcp.yml
  slug: sfox-mcpyml
modified: '2026-07-21'
name: Sfox
nav: Providers
network: true
overview: 'Sfox publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API and WebSocket API. Tagged areas include Company, Cryptocurrency, Prime Brokerage, Trading, and Digital Asset Custody.


  The Sfox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sfox''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 100
rate_limits:
- limit_count: 2
  name: Sfox Rate Limits
  slug: sfox-rate-limits
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.3
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 49.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Sfox Authentication
  slug: sfox-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sfox Domain Security
  slug: sfox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sfox
tags:
- Company
- Cryptocurrency
- Prime Brokerage
- Trading
- Digital Asset Custody
- Liquidity
- Staking
- Institutional
- Financial Services
- Market Data
- WebSocket
- FIX
website: https://www.sfox.com/api/
---
