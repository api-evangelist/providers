---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://intrinio.com/pricing
  - https://intrinio.com/mcp
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Intrinio's REST API for financial data — stock prices, options, fundamentals, estimates, ETFs, indices, corporate actions, and ESG — with API-key authentication, next_page cursor pagination, and swagg
  name: Intrinio Web API v2
  slug: intrinio-web-api-v2
artifact_total: 8
asyncapis:
- description: ''
  name: Intrinio Websockets
  slug: intrinio-websockets
common:
- group: company
  title: ''
  type: Website
  url: https://intrinio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://account.intrinio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intrinio.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.intrinio.com/documentation/api_v2
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.intrinio.com/documentation/api_v2/getting_started
- group: operate
  title: ''
  type: Support
  url: https://help.intrinio.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intrinio
- group: commercial
  title: ''
  type: Pricing
  url: https://intrinio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://account.intrinio.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.intrinio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.intrinio.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.intrinio.com
- group: company
  title: ''
  type: Blog
  url: https://intrinio.com/blog/rss.xml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: Packages
  url: packages/intrinio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intrinio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intrinio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intrinio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intrinio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/intrinio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/intrinio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intrinio-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/intrinio-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intrinio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intrinio-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intrinio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intrinio-plans.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intrinio-domain-security.yml
created: '2026-05-28'
description: Intrinio is a financial data platform delivering real-time, delayed, and historical US stock prices, options data with Greeks and implied volatility, standardized and as-reported company fundamentals, analyst estimates, ETF and mutual fund holdings, indices, corporate actions, and ESG data through a REST API, WebSocket streaming feeds, bulk files, Snowflake and S3 delivery, and an official hosted MCP server that connects Claude, ChatGPT, Cursor, and other AI assistants directly to its data catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intrinio.png
layout: provider
mcp_servers:
- description: ''
  name: intrinio-mcp.yml
  slug: intrinio-mcpyml
modified: '2026-07-22'
name: Intrinio
nav: Providers
network: true
overview: 'Intrinio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Financial Data, Market Data, Stocks, and Options.


  The Intrinio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Intrinio''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 21 more developer resources.'
plans:
- name: Intrinio Plans
  plan_count: 3
  slug: intrinio-plans
random_paper: 56
rate_limits:
- limit_count: 4
  name: Intrinio Rate Limits
  slug: intrinio-rate-limits
scopes:
- name: Intrinio Scopes
  scope_count: 1
  slug: intrinio-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.8
  delta: 6.5
  facets:
    commercial_clarity: 76.3
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 94.4
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/intrinio/refs/heads/main/screenshots/intrinio-2026-06-20T183509.png
security:
- kind: authentication
  name: Intrinio Authentication
  slug: intrinio-authentication
  summary_line: apiKey/http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Intrinio Domain Security
  slug: intrinio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: intrinio
tags:
- Finance
- Financial Data
- Market Data
- Stocks
- Options
- Fundamentals
- ETFs
- Real-Time Data
website: https://intrinio.com/
---
