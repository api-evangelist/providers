---
access_model:
  confidence: high
  label: Self-serve freemium — Google login, free 200 req/day tier, in-browser playground
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://usebolsai.com/#pricing
  - https://usebolsai.com/#playground
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-09-16'
api_count: 3
apis:
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The admin API from Bolsai — 2 operation(s) for admin.
  name: Bolsai Admin API
  slug: bolsai-admin-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: Register and manage API keys (no auth required)
  name: Bolsai API Keys API
  slug: bolsai-api-keys-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The auth API from Bolsai — 5 operation(s) for auth.
  name: Bolsai Auth API
  slug: bolsai-auth-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The billing API from Bolsai — 3 operation(s) for billing.
  name: Bolsai Billing API
  slug: bolsai-billing-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Companies API from Bolsai — 5 operation(s) for companies.
  name: Bolsai Companies API
  slug: bolsai-companies-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Dividends API from Bolsai — 2 operation(s) for dividends.
  name: Bolsai Dividends API
  slug: bolsai-dividends-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The feedback API from Bolsai — 6 operation(s) for feedback.
  name: Bolsai Feedback API
  slug: bolsai-feedback-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Fiis API from Bolsai — 10 operation(s) for fiis.
  name: Bolsai Fiis API
  slug: bolsai-fiis-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Financials API from Bolsai — 2 operation(s) for financials.
  name: Bolsai Financials API
  slug: bolsai-financials-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Fundamentals API from Bolsai — 4 operation(s) for fundamentals.
  name: Bolsai Fundamentals API
  slug: bolsai-fundamentals-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The health API from Bolsai — 1 operation(s) for health.
  name: Bolsai Health API
  slug: bolsai-health-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Macro API from Bolsai — 5 operation(s) for macro.
  name: Bolsai Macro API
  slug: bolsai-macro-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: Screen stocks by fundamental metrics
  name: Bolsai Screener API
  slug: bolsai-screener-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The Stocks API from Bolsai — 13 operation(s) for stocks.
  name: Bolsai Stocks API
  slug: bolsai-stocks-api
- baseURL: https://api.usebolsai.com/api/v1
  baseurl_source: declared
  description: The oauth API from Bolsai — 7 operation(s) for oauth.
  name: Bolsai OAUTH API
  slug: bolsai-oauth-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/mcp/bolsai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bolsai-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/overlays/bolsai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bolsai-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.usebolsai.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/security/bolsai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolsai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/authentication/bolsai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bolsai-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/packages/bolsai-packages.yml
  title: ''
  type: Packages
  url: packages/bolsai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/well-known/bolsai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bolsai-well-known.yml
- group: company
  title: ''
  type: Blog
  url: https://usebolsai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usebolsai.com/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:vinicius.lazzari@usebolsai.com
created: '2026-07-06'
description: Brazilian financial-market data REST API serving equities, real-estate funds (FIIs), fundamentals, dividends, financial statements, and macroeconomic series sourced from official feeds (B3, CVM, BCB). Covers 350+ B3 stocks, 400+ FIIs and 40 years of price history, with an official MCP server (hosted OAuth endpoint and PyPI package) for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolsai.png
layout: provider
mcp_servers:
- description: Official Bolsai MCP server exposing Brazilian financial-market data (B3 stocks, FIIs, fundamentals, dividends, CVM financial statements, BCB macro series) to MCP clients. Available BOTH as a hosted re
  name: Bolsai MCP Server
  slug: bolsai-mcp-server
modified: '2026-09-03'
name: Bolsai
nav: Providers
network: true
overview: 'Bolsai publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Admin API, API Keys API, Auth API, and 12 more. Tagged areas include Finance, Financial Data, Market Data, Stocks/equities, and Real Estate Funds.


  Bolsai''s developer surface includes authentication, engineering blog, pricing, support, and 7 more developer resources.'
plans:
- name: Bolsai Plans Pricing
  plan_count: 3
  slug: bolsai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Bolsai Rate Limits
  slug: bolsai-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.9
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 47.9
    developer_ergonomics: 37.5
    discoverability: 81.5
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 33.8
  provenance:
    conformance: first-party
    contracts:
      callable: 46.7
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/screenshots/bolsai-2026-07-25T203539.png
security:
- kind: authentication
  name: Bolsai Authentication
  slug: bolsai-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Bolsai Domain Security
  slug: bolsai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bolsai
tags:
- Finance
- Financial Data
- Market Data
- Stocks/equities
- Real Estate Funds
- Dividends
- Fundamentals
- Macroeconomic Data
- Brazil
- Developer Tools
- MCP
- AI Agents
website: https://www.usebolsai.com/
---
