---
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: JSON API for stock market and financial news data with filtering capabilities by ticker, date, sector, topic, and sentiment analysis.
  name: Stock News API
  slug: stock-news-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/rate-limits/stocknewsapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stocknewsapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/plans/stocknewsapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stocknewsapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/conventions/stocknewsapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stocknewsapi-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/authentication/stocknewsapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stocknewsapi-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/lifecycle/stocknewsapi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/stocknewsapi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/lifecycle/stocknewsapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stocknewsapi-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/llms/stocknewsapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stocknewsapi-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stocknewsapi/refs/heads/main/security/stocknewsapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stocknewsapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stocknewsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stocknewsapi.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://stocknewsapi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://stocknewsapi.com/status
- group: build
  title: ''
  type: Examples
  url: https://stocknewsapi.com/examples
- group: operate
  title: ''
  type: FAQ
  url: https://stocknewsapi.com/faq
- group: operate
  title: ''
  type: Forum
  url: https://stocknewsapi.com/forum
- group: operate
  title: ''
  type: Contact
  url: https://stocknewsapi.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://stocknewsapi.com/register
- group: start
  title: ''
  type: Login
  url: https://stocknewsapi.com/login
created: '2026-09-20'
description: StockNewsAPI provides a JSON API for stock market and financial news data. The service offers access to clean, relevant stock market news with advanced filtering capabilities including filtering by ticker, date, sector, topic, and more. The API allows developers to retrieve news for individual tickers, multiple tickers, general market news, and provides features like sentiment analysis, trending headlines, and historical data.
layout: provider
modified: '2026-09-20'
name: StockNewsAPI
nav: Providers
network: true
overview: 'StockNewsAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, News, Stocks, and Market Data.


  StockNewsAPI''s developer surface includes authentication, documentation, pricing, code examples, FAQ, signup flow, and 12 more developer resources.'
plans:
- name: Stocknewsapi Plans Pricing
  plan_count: 3
  slug: stocknewsapi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Stocknewsapi Rate Limits
  slug: stocknewsapi-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 26.2
    discoverability: 72.2
    operational_transparency: 55.3
  previous_composite: 31.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Stocknewsapi Authentication
  slug: stocknewsapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stocknewsapi Domain Security
  slug: stocknewsapi-domain-security
  summary_line: TLSv1.2
slug: stocknewsapi
tags:
- Company
- Finance
- News
- Stocks
- Market Data
website: https://stocknewsapi.com/
---
