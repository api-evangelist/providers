---
access_model:
  confidence: high
  label: Freemium (3-day free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: 'Read-only REST API for real-time and historical market data: last quotes/trades, OHLCV aggregates, and snapshots for US and global stocks, forex, crypto, CFD indices and ETFs, plus fundamentals (finan'
  name: Finage Market Data API
  slug: finage-market-data-api
- description: Real-time streaming trades and quotes for US stocks, global stocks, forex, crypto, CFD indices, and ETFs over per-customer WebSocket URLs (assigned subdomain and port on finage.ws, socket-key token au
  name: Finage WebSocket Market Data Stream
  slug: finage-websocket-market-data-stream
artifact_total: 8
asyncapis:
- description: 'Finage streams real-time market prices (US stocks, global stocks, forex, crypto, CFD indices, and ETFs) over WebSocket. Each customer is assigned a dedicated WebSocket URL (subdomain + port) shown in '
  name: Finage WebSocket Market Data Stream
  slug: finage-websocket-asyncapi
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/finage-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finage.co.uk
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: Packages
  url: packages/finage-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finage-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finage-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/finage-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finage-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finage-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/finage-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finage-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/finage-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finage-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/finage-websocket-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Portal
  url: https://moon.finage.co.uk
- group: start
  title: ''
  type: SignUp
  url: https://moon.finage.co.uk/register
- group: docs
  title: ''
  type: Documentation
  url: https://finage.co.uk/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://finage.co.uk/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://finage.co.uk/pricing
- group: company
  title: ''
  type: Blog
  url: https://finage.co.uk/blog
- group: operate
  title: ''
  type: Support
  url: https://finage.co.uk/company/frequently-asked-questions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinageLTD
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finage.co.uk/company/privacy-policy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finage.co.uk/company/privacy-policy/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finageltd/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/finageltd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCRUuqo17XKUVxPODKLsRvmA
created: '2026-05-28'
description: Finage is a London-based real-time and historical market data provider covering US and global stocks, forex, cryptocurrencies, CFD indices, ETFs, bonds, and company fundamentals. Data is delivered through a read-only REST API (api.finage.co.uk, API-key auth, 72 documented endpoints spanning quotes, trades, OHLCV aggregates, snapshots, financial statements, calendars, news, and technical indicators), dedicated per-customer WebSocket streams on finage.ws for real-time trades and quotes, and embeddable website widgets served from cdn.finage.co.uk. Plans range from a free 1,000 request/month tier through Basic API packages to Professional unlimited WebSocket feeds, with a 3-day free trial across all markets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finage.png
layout: provider
mcp_servers:
- description: ''
  name: finage-mcp.yml
  slug: finage-mcpyml
modified: '2026-07-22'
name: Finage
nav: Providers
network: true
overview: 'Finage publishes 2 APIs on the [APIs.io](https://apis.io/) network: Market Data API and WebSocket Market Data Stream. Tagged areas include Finance, Market Data, Stocks, Forex, and Cryptocurrency.


  The Finage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finage''s developer surface includes authentication, developer portal, signup flow, documentation, API reference, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Finage Plans
  plan_count: 23
  slug: finage-plans
random_paper: 6
rate_limits:
- limit_count: 3
  name: Finage Rate Limits
  slug: finage-rate-limits
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 55.6
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 53.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finage/refs/heads/main/screenshots/finage-2026-06-20T181209.png
security:
- kind: authentication
  name: Finage Authentication
  slug: finage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Finage Domain Security
  slug: finage-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finage
tags:
- Finance
- Market Data
- Stocks
- Forex
- Cryptocurrency
- ETFs
- Indices
- Fundamentals
- Real-Time Data
- Public APIs
website: https://finage.co.uk
---
