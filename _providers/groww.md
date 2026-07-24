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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 84.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Groww Agentic Access
  operation_count: 20
  slug: groww-agentic-access
  summary_line: 20 operations · 5 acting
api_count: 6
apis:
- description: Access-token generation for API key + secret and TOTP flows.
  name: Groww Authentication API
  slug: groww-authentication-api
- description: Historical candle data.
  name: Groww Historical Data API
  slug: groww-historical-data-api
- description: Real-time LTP, quote, OHLC, option chain and greeks.
  name: Groww Live Data API
  slug: groww-live-data-api
- description: Available margin and per-order margin requirements.
  name: Groww Margin API
  slug: groww-margin-api
- description: Place, modify, cancel and track orders and trades.
  name: Groww Orders API
  slug: groww-orders-api
- description: Holdings and positions.
  name: Groww Portfolio API
  slug: groww-portfolio-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://groww.in/trade-api
- group: docs
  title: ''
  type: Documentation
  url: https://groww.in/trade-api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://groww.in/trade-api/docs/curl
- group: start
  title: ''
  type: GettingStarted
  url: https://groww.in/trade-api/docs/python-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://groww.in/trade-api
- group: start
  title: ''
  type: SignUp
  url: https://groww.in/trade-api/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groww.in/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groww.in/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://groww.in/help
- group: company
  title: ''
  type: Blog
  url: https://groww.in/blog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/groww-trade-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groww-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/groww-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groww-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/groww-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groww-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groww-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groww-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/groww-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groww-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groww-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groww-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/groww-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/groww-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/groww-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/groww-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groww-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groww-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/groww-trade-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://groww.in/
created: '2026-07-17'
description: Groww is an Indian fintech company offering investing and trading in stocks, futures & options, mutual funds, ETFs, IPOs and more through its consumer app and web platform. Backed by Iconiq Capital, Ribbit Capital and Y Combinator, Groww also operates the Groww Trading API — an official programmatic interface for algorithmic trading that covers order management (place/modify/cancel), portfolio holdings and positions, margin calculation, live market data (LTP, full quote, OHLC, option chain and greeks) and historical candle data across the CASH (equity) and FNO (derivatives) segments on Indian exchanges. Requests hit https://api.groww.in, are versioned with the X-API-VERSION header, and are authenticated with a daily Bearer access token generated via an API key + secret checksum, a TOTP flow, or an OAuth2 authorization-code flow.
image: https://groww.in/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: groww-mcp.yml
  slug: groww-mcpyml
modified: '2026-07-19'
name: Groww
nav: Providers
network: true
overview: 'Groww publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Historical Data API, Live Data API, and 3 more. Tagged areas include Company, Fintech, Trading, Investing, and Stock Broking.


  Groww''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 24 more developer resources.'
plans:
- name: Groww Plans
  plan_count: 1
  slug: groww-plans
random_paper: 5
rate_limits:
- limit_count: 7
  name: Groww Rate Limits
  slug: groww-rate-limits
scopes:
- name: Groww Scopes
  scope_count: 0
  slug: groww-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.1
  delta: 2.9
  facets:
    commercial_clarity: 65.8
    contract_quality: 56.6
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 57.2
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Groww Authentication
  slug: groww-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Groww Domain Security
  slug: groww-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: groww
tags:
- Company
- Fintech
- Trading
- Investing
- Stock Broking
- Market Data
- Algorithmic Trading
- India
website: https://groww.in/
---
