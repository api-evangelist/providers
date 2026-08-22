---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'Token-authenticated HTTPS query API for financial market tick data. Twelve operations across three base paths: /quote-stock-b-api for Hong Kong, US and A-share equities, /quote-b-api for forex, crypto'
  name: AllTick REST/HTTP Query API
  slug: alltick-resthttp-query-api
- description: Token-authenticated WebSocket streaming API for real-time market data. Two endpoints — wss://quote.alltick.co/quote-stock-b-ws-api for equities and wss://quote.alltick.co/quote-b-ws-api for forex, cry
  name: AllTick WebSocket Streaming API
  slug: alltick-websocket-streaming-api
artifact_total: 8
asyncapis:
- description: ''
  name: Alltick Api Event Surface
  slug: alltick-api-event-surface
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alltick-api-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.alltick.co/en
- group: docs
  title: ''
  type: Documentation
  url: https://en.apis.alltick.co/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.alltick.co/en/api-reference/stock/kline
- group: start
  title: ''
  type: GettingStarted
  url: https://en.apis.alltick.co/integration-process/process-description
- group: operate
  title: ''
  type: Support
  url: https://alltick.co/#contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://alltick.co/faqs
- group: company
  title: ''
  type: Blog
  url: https://blog.alltick.co/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.alltick.co/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alltick
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api
- group: commercial
  title: ''
  type: Pricing
  url: https://alltick.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://alltick.co/register
- group: start
  title: ''
  type: Login
  url: https://alltick.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alltick.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alltick.co/policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alltick.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/alltick-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alltick-api-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alltick-api-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alltick-api-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alltick-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alltick-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alltick-api-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alltick-api-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/alltick-api-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alltick-api-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alltick-api-llms.txt
created: '2026-08-18'
description: AllTick (AllTick PTE. LTD., Singapore) sells real-time and historical financial market tick data through a token-authenticated HTTPS query API and two WebSocket streams, covering forex, Hong Kong / US / A-share equities, indices, precious metals, crude oil and cryptocurrencies across roughly 100,000 symbols. The HTTP surface returns candlesticks (1-minute through monthly, with ex-rights and forward-adjusted variants), latest trade ticks, order-book depth, equity reference data and SSE/NYSE/NASDAQ trading-halt listings; the WebSocket surface pushes tick-by-tick trades and order-book updates. Sold self-serve in USDT on a per-symbol-basket or whole-market basis, with a permanent free tier limited to ten demo symbols. Built for exchanges, brokers, quantitative teams, trading platforms and fintech developers.
image: https://alltick.co/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: alltick-api-mcp.yml
  slug: alltick-api-mcpyml
modified: '2026-08-18'
name: AllTick API
nav: Providers
network: true
overview: 'AllTick API publishes 1 API on the [APIs.io](https://apis.io/) network: AllTick REST/HTTP Query API. Tagged areas include financial-market-data, real-time-data, stock-market-data, forex-data, and cryptocurrency-data.


  The AllTick API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AllTick API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Alltick Api Plans Pricing
  plan_count: 8
  slug: alltick-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 13
  name: Alltick Api Rate Limits
  slug: alltick-api-rate-limits
score:
  band: strong
  composite: 59.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 58.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Alltick Api Authentication
  slug: alltick-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alltick Api Domain Security
  slug: alltick-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alltick-api
tags:
- financial-market-data
- real-time-data
- stock-market-data
- forex-data
- cryptocurrency-data
- commodities-data
- tick-data
- websocket-streaming
- fintech
- quantitative-trading
- market-data-api
- trading-halts
website: https://apis.alltick.co/en
---
