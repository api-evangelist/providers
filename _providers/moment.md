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
    agent_skills: derived
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
  score: 40.8
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST and WebSocket API for fixed-income reference data, evaluated pricing, order books, analytics, order/RFQ execution, and portfolio optimization.
  name: Moment Fixed Income API
  slug: moment-fixed-income-api
artifact_total: 5
asyncapis:
- description: ''
  name: Moment Realtime Webhooks
  slug: moment-realtime-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moment.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moment.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moment.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moment.com/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moment.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@withmoment.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moment.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moment-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/moment-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moment-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moment-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/moment-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moment-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moment-realtime-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moment-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moment-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moment-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moment-lifecycle.yml
created: '2026-07-17'
description: Moment is the AI operating system for investment management and the fixed-income infrastructure that powers bond data, pricing, and trading for digital wealth platforms, RIAs, and brokerages. Through simple REST and WebSocket APIs it delivers institutional-grade reference data on 500,000+ (1M+ global) fixed-income securities — corporates, treasuries, agencies, municipals, CDs, ABS/MBS and structured products — plus real-time and historical evaluated pricing, live top-of-order-book and full order books, and advanced analytics (yield conversion, markups, duration, spreads, liquidity scores, implied default). Its execution management system covers orders, RFQs, smart order routing, allocations, block trades, corporate actions, portfolio optimization, model and asset-allocation management, and account, risk-control, and cash-raise operations. Moment works with wealth firms overseeing more than $10 trillion in assets across 60,000+ advisors.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moment.png
layout: provider
mcp_servers:
- description: ''
  name: moment-mcp.yml
  slug: moment-mcpyml
modified: '2026-07-20'
name: Moment
nav: Providers
network: true
overview: 'Moment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fixed Income, Bonds, Trading, and Market Data.


  The Moment catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moment''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 14 more developer resources.'
random_paper: 86
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.2
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Moment Authentication
  slug: moment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moment Domain Security
  slug: moment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moment
tags:
- Company
- Fixed Income
- Bonds
- Trading
- Market Data
- Reference Data
- Investment Management
- Wealth Management
- Brokerage
- Financial Services
- Fintech
website: https://moment.com
---
