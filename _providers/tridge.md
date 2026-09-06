---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Tridge advertises a commercial API for integrating its global agri-food price and trade data into a customer's own systems ("the most comprehensive and powerful API to allow you to integrate our globa
  name: Tridge Data & Analytics API
  slug: tridge-data-analytics-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tridge.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tridge.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://blog.tridge.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tridge.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.tridge.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tridge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tridge.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tridge-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tridge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tridge-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tridge-authentication.yml
coverage:
  checked: '2026-08-30'
  detail: Tridge markets a price-data API on its Data & Analytics pages but ships no developer portal, no API reference and no machine-readable contract; every "Get Started" route resolves to /contact-sales?category=DATA_PACKAGE, and the only anonymously reachable API surface (api.tridge.com/graphql) answers HTTP 403 "crc rejected" while robots.txt disallows /graphql and /api/ outright.
  evidence:
  - status: 200
    url: https://www.tridge.com/about/data-analytics/price
  - status: 200
    url: https://www.tridge.com/contact-sales
  - status: 403
    url: https://api.tridge.com/graphql
  - status: 404
    url: https://www.tridge.com/developers
  - status: 404
    url: https://api.tridge.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-08-30'
description: Tridge is a South Korea-headquartered global agri-food trade intelligence and sourcing platform. It combines a data layer of structured cross-border trade, price, production, seasonality and weather data (the company cites 682M+ trade data points and 65M+ price records across 200+ markets), a network layer of verified buyers and suppliers in 190+ countries, and an AI layer that runs trade workflows from discovery through deal closure. Products include Market Curations, Sourcing Hub, Data & Analytics, Tridge Eye (market intelligence) and Tridge Ark (AI-driven export sales outreach). Tridge advertises an API for integrating its global price and trade data into customer systems, but publishes no public developer portal, reference documentation or machine-readable contract — access is arranged through a sales conversation.
image: https://cdn-new.tridge.com/assets/SWDU73HM.jpg
layout: provider
modified: '2026-08-30'
name: Tridge
nav: Providers
network: true
overview: 'Tridge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Food, Trade, and Commodities.


  Tridge''s developer surface includes support, engineering blog, pricing, authentication, and 8 more developer resources.'
plans:
- name: Tridge Plans Pricing
  plan_count: 0
  slug: tridge-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Tridge Rate Limits
  slug: tridge-rate-limits
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tridge/refs/heads/main/screenshots/tridge-2026-09-02T164227.png
security:
- kind: authentication
  name: Tridge Authentication
  slug: tridge-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tridge Domain Security
  slug: tridge-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tridge
tags:
- Company
- Agriculture
- Food
- Trade
- Commodities
- Market Data
- Supply Chain
- Sourcing
- Analytics
- Price Data
- Intelligence
- Artificial Intelligence
website: https://www.tridge.com/
---
