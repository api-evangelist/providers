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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: Entity statistics, trending entities, entity search, and entity metadata.
  name: MarketAux Entities API
  slug: marketaux-entities-api
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: Financial and market news feeds, similar-article lookup, and article retrieval by UUID.
  name: MarketAux News API
  slug: marketaux-news-api
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: News source metadata usable in news feed filters.
  name: MarketAux Sources API
  slug: marketaux-sources-api
artifact_total: 13
collections:
- collection_type: open
  name: Marketaux API
  slug: open-marketaux
common:
- group: other
  href: https://artifacts.apis.io/marketaux/overlays/marketaux-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/marketaux-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/marketaux/mcp/marketaux-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/marketaux-mcp.yml
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
  href: https://artifacts.apis.io/marketaux/authentication/marketaux-authentication.yml
  title: ''
  type: Authentication
  url: authentication/marketaux-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/marketaux/plans/marketaux-plans.yml
  title: ''
  type: Plans
  url: plans/marketaux-plans.yml
- group: operate
  href: https://artifacts.apis.io/marketaux/rate-limits/marketaux-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/marketaux-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/marketaux/errors/marketaux-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/marketaux-problem-types.yml
- group: design
  href: https://artifacts.apis.io/marketaux/conventions/marketaux-conventions.yml
  title: ''
  type: Conventions
  url: conventions/marketaux-conventions.yml
- group: design
  href: https://artifacts.apis.io/marketaux/lifecycle/marketaux-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/marketaux-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/marketaux/conformance/marketaux-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marketaux-conformance.yml
- group: design
  href: https://artifacts.apis.io/marketaux/data-model/marketaux-data-model.yml
  title: ''
  type: DataModel
  url: data-model/marketaux-data-model.yml
- group: build
  href: https://artifacts.apis.io/marketaux/examples/marketaux-examples.yml
  title: ''
  type: Examples
  url: examples/marketaux-examples.yml
- group: build
  href: https://artifacts.apis.io/marketaux/packages/marketaux-packages.yml
  title: ''
  type: Packages
  url: packages/marketaux-packages.yml
- group: agent
  href: https://artifacts.apis.io/marketaux/well-known/marketaux-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/marketaux-well-known.yml
- group: agent
  href: https://artifacts.apis.io/marketaux/llms/marketaux-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/marketaux-llms.txt
- group: agent
  href: https://artifacts.apis.io/marketaux/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/marketaux/security/marketaux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marketaux-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Marketaux is a global financial and stock market news API that pairs every article with entity recognition and sentiment analysis. It aggregates 5,000+ news sources in 30+ languages, tracking 200,000+ entities — equities, indices, ETFs, mutual funds, currencies, and cryptocurrencies — across 80+ markets. Beyond filtered news feeds, it provides entity statistics time series, aggregations, and trending-entity endpoints for identifying the best and worst performing entities in the news, with a free self-serve tier.
finops:
- has_sources: true
  method: derived
  name: Marketaux Finops
  primary_unit: subscription
  service_category: ''
  slug: marketaux-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketaux.png
layout: provider
modified: '2026-07-22'
name: MarketAux
nav: Providers
network: true
overview: 'MarketAux publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Entities API, News API, and Sources API. Tagged areas include News, Financial News, Stock Market, Sentiment Analysis, and Market Data.


  MarketAux''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, FAQ, and 21 more developer resources.'
plans:
- name: Marketaux Plans
  plan_count: 10
  slug: marketaux-plans
- name: Marketaux Price Estimates
  plan_count: 0
  slug: marketaux-price-estimates
random_paper: 18
rate_limits:
- limit_count: 6
  name: Marketaux Rate Limits
  slug: marketaux-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 17.0
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/marketaux/marketaux-2026-06-20T184952.png
security:
- kind: authentication
  name: Marketaux Authentication
  slug: marketaux-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marketaux Domain Security
  slug: marketaux-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 3
skills:
- name: Build an entity-filtered market news feed
  slug: marketaux-build-entity-news-feed
- name: Find trending entities in the news
  slug: marketaux-find-trending-entities
- name: Monitor entity sentiment over time
  slug: marketaux-monitor-entity-sentiment
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
