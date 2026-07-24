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
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 39.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The El Dorado onramp/offramp trading API for converting between Latin American fiat currencies and crypto (USDT on Arbitrum). Create buy/sell quotes and orders, manage KYC, and fetch supported currenc
  name: El Dorado API
  slug: el-dorado-api
artifact_total: 5
asyncapis:
- description: ''
  name: Eldorado Webhooks
  slug: eldorado-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://eldorado.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.eldorado.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.eldorado.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.eldorado.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.eldorado.io/guides/quick-start
- group: start
  title: ''
  type: Sandbox
  url: https://api.eldorado.io/guides/sandbox
- group: company
  title: ''
  type: Blog
  url: https://eldorado.io/en/blog
- group: start
  title: ''
  type: SignUp
  url: https://eldorado.io/en/api
- group: operate
  title: ''
  type: Support
  url: mailto:api@eldorado.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/eldorado-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eldorado-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eldorado-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eldorado-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/eldorado-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eldorado-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eldorado-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eldorado-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eldorado-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eldorado-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eldorado-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eldorado-domain-security.yml
created: '2026-07-17'
description: El Dorado is a stablecoin-powered payments SuperApp for Latin America whose public API provides crypto onramp/offramp (buy and sell) infrastructure across Argentina, Brazil, Colombia, Peru, Bolivia, Panama, Paraguay, the Dominican Republic and more. The API lets partners create buy and sell quotes and orders that convert between local fiat currencies (USD, ARS, BRL, COP, PEN and others) and crypto (settled in USDT on Arbitrum), with built-in KYC verification, 80+ local payment methods, and an embeddable Exchange Widget for no-code or low-code integration. Authentication uses per-partner ClientID and ReferralID headers plus a JWT bearer token obtained via an OTP login flow. El Dorado is backed by Multicoin Capital, Coinbase Ventures and Berkeley SkyDeck and has surpassed 500,000 users.
image: https://api.eldorado.io/img/index/og_image.jpg
layout: provider
mcp_servers:
- description: ''
  name: eldorado-mcp.yml
  slug: eldorado-mcpyml
modified: '2026-07-19'
name: Eldorado
nav: Providers
network: true
overview: 'Eldorado publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Stablecoins, Payments, and Onramp.


  The Eldorado catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eldorado''s developer surface includes documentation, API reference, getting-started guide, sandbox, engineering blog, signup flow, support, and 15 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 33.9
  delta: 0.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.3
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Eldorado Authentication
  slug: eldorado-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Eldorado Domain Security
  slug: eldorado-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eldorado
tags:
- Company
- Crypto Web3
- Stablecoins
- Payments
- Onramp
- Offramp
- Cryptocurrency
- Latin America
- KYC
- Compliance
- Fintech
- Trading
website: https://eldorado.io
---
