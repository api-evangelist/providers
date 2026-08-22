---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
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
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Live stock market news with tagged tickers, per-entity sentiment and match scores, entity statistics and trending endpoints, delivered as a GET-only JSON API authenticated with an api_token query para
  name: MarketAux API
  slug: marketaux-api
artifact_total: 7
collections:
- collection_type: open
  name: Marketaux API
  slug: open-marketaux
common:
- group: company
  title: ''
  type: Website
  url: https://www.marketaux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.marketaux.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.marketaux.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.marketaux.com/documentation#introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marketaux.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.marketaux.com/register
- group: start
  title: ''
  type: Login
  url: https://www.marketaux.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.marketaux.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.marketaux.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marketaux.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marketaux.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketaux-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marketaux-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketaux-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marketaux-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marketaux-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marketaux-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marketaux-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marketaux-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/marketaux-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/marketaux-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marketaux-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketaux-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketaux-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Marketaux is a global financial and stock market news API that pairs every article with entity recognition and sentiment analysis. It aggregates 5,000+ news sources in 30+ languages, tracking 200,000+ entities — equities, indices, ETFs, mutual funds, currencies, and cryptocurrencies — across 80+ markets. Beyond filtered news feeds, it provides entity statistics time series, aggregations, and trending-entity endpoints for identifying the best and worst performing entities in the news, with a free self-serve tier.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketaux.png
layout: provider
mcp_servers:
- description: ''
  name: marketaux-mcp.yml
  slug: marketaux-mcpyml
modified: '2026-07-22'
name: MarketAux
nav: Providers
network: true
overview: 'MarketAux publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Financial News, Stock Market, Sentiment Analysis, and Market Data.


  MarketAux''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, FAQ, and 19 more developer resources.'
plans:
- name: Marketaux Plans
  plan_count: 6
  slug: marketaux-plans
random_paper: 12
rate_limits:
- limit_count: 6
  name: Marketaux Rate Limits
  slug: marketaux-rate-limits
score:
  band: developing
  composite: 45.3
  delta: 2.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 14.9
    developer_ergonomics: 47.0
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 43.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marketaux/refs/heads/main/screenshots/marketaux-2026-06-20T184952.png
security:
- kind: authentication
  name: Marketaux Authentication
  slug: marketaux-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marketaux Domain Security
  slug: marketaux-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: marketaux
tags:
- News
- Financial News
- Stock Market
- Sentiment Analysis
- Market Data
- Entity Recognition
- Public APIs
website: https://www.marketaux.com/
---
