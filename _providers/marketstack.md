---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://marketstack.com/pricing
  - https://marketstack.com/signup/free
  trial: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Real-time, intraday and historical market data API with 45 endpoints spanning end-of-day bars, intraday bars, real-time stock prices, commodities, company ratings, splits, dividends, tickers, indexes,
  name: Marketstack API v2
  slug: marketstack-api-v2
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://marketstack.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apilayer.com/marketstack
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/marketstack/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://marketstack.com/documentation_v2
- group: start
  title: ''
  type: GettingStarted
  url: https://marketstack.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://marketstack.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://marketstack.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://marketstack.com/signup/free
- group: start
  title: ''
  type: Login
  url: https://marketstack.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketstack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marketstack.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.marketstack.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apilayer
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/feed/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketstack-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/marketstack-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/marketstack-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketstack-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/marketstack-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/marketstack-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marketstack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marketstack-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketstack-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marketstack-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marketstack-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketstack-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marketstack-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-28'
description: Marketstack is a real-time, intraday, and historical stock market data API from APILayer, delivering JSON data for tickers across 70+ global stock exchanges. The REST API covers end-of-day and intraday prices, real-time stock prices, splits, dividends, commodities, company ratings, market indexes, bonds, ETF holdings, currencies, timezones, and SEC EDGAR company filings and facts, all authenticated with a simple access_key query parameter.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketstack.png
layout: provider
mcp_servers:
- description: ''
  name: marketstack-mcp.yml
  slug: marketstack-mcpyml
modified: '2026-07-22'
name: Marketstack
nav: Providers
network: true
overview: 'Marketstack publishes 1 API on the [APIs.io](https://apis.io/) network: API v2. Tagged areas include Finance, Stock Market, Market Data, End-of-Day Data, and Intraday Data.


  Marketstack''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 22 more developer resources.'
plans:
- name: Marketstack Plans
  plan_count: 5
  slug: marketstack-plans
random_paper: 98
rate_limits:
- limit_count: 5
  name: Marketstack Rate Limits
  slug: marketstack-rate-limits
score:
  band: developing
  composite: 55.4
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 46.3
    developer_ergonomics: 66.8
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 55.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marketstack/refs/heads/main/screenshots/marketstack-2026-06-20T184956.png
security:
- kind: authentication
  name: Marketstack Authentication
  slug: marketstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marketstack Domain Security
  slug: marketstack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: marketstack
tags:
- Finance
- Stock Market
- Market Data
- End-of-Day Data
- Intraday Data
- Commodities
- Bonds
- ETFs
- SEC EDGAR
- Dividends
website: https://marketstack.com
---
