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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: 'REST/JSON API for stock and options market data: quotes, history, options chains, unusual options activity, financials, analyst ratings, SEC filings, insider trades, calendar events, technical indicat'
  name: Mboum Stock & Options Data API
  slug: mboum-stock-options-data-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/rate-limits/mboum-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mboum-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/plans/mboum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mboum-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/conventions/mboum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mboum-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/authentication/mboum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mboum-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/lifecycle/mboum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mboum-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/errors/mboum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mboum-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/llms/mboum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mboum-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/packages/mboum-packages.yml
  title: ''
  type: Packages
  url: packages/mboum-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mboum/refs/heads/main/security/mboum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mboum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mboum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mboum.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mboum.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mboum.com/pages/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mboum.com/register
- group: start
  title: ''
  type: Login
  url: https://mboum.com/login
- group: company
  title: ''
  type: Blog
  url: https://mboum.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://mboum.com/pages/contact
- group: operate
  title: ''
  type: FAQ
  url: https://mboum.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mboum.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mboum.com/pages/privacy-policy
created: '2026-09-20'
description: Stock and options market data REST API providing intraday and end-of-day data including quotes, options chains, technical indicators, SEC filings, insider trades, earnings, dividends, and screeners.
layout: provider
modified: '2026-09-20'
name: Mboum
nav: Providers
network: true
overview: 'Mboum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Stocks, Stock Market, Options, options market, and Trading.


  Mboum''s developer surface includes authentication, documentation, API reference, pricing, signup flow, engineering blog, support, and 13 more developer resources.'
plans:
- name: Mboum Plans Pricing
  plan_count: 4
  slug: mboum-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Mboum Rate Limits
  slug: mboum-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    operational_transparency: 21.1
  previous_composite: 32.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mboum Authentication
  slug: mboum-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mboum Domain Security
  slug: mboum-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mboum
tags:
- Stocks
- Stock Market
- Options
- options market
- Trading
- Quotes
- Market Data
- Technical Indicators
- SEC Filings
- Insider Trading
- IPO
- Dividends
- Earnings
- Historical Data
- Screener
- Crypto
website: https://mboum.com
---
