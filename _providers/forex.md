---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Forex Agentic Access
  operation_count: 5
  slug: forex-agentic-access
  summary_line: 5 operations
api_count: 7
apis:
- description: Foreign exchange rates and currency conversion API.
  name: Fixer.io API
  slug: fixer
- description: Free currency conversion API with 161 currencies.
  name: ExchangeRate-API
  slug: exchangerate-api
- description: Accurate and reliable foreign exchange rates API.
  name: CurrencyAPI
  slug: currencyapi
- description: Free and open-source API for current and historical forex rates.
  name: Frankfurter API
  slug: frankfurter
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Account API from Forex — 1 operation(s) for account.
  name: Forex Account API
  slug: forex-account-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Rates API from Forex — 3 operation(s) for rates.
  name: Forex Rates API
  slug: forex-rates-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Reference API from Forex — 1 operation(s) for reference.
  name: Forex Reference API
  slug: forex-reference-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Exchange Rates Account API
  slug: open-forex-account-api
- collection_type: open
  name: Open Exchange Account Rates API
  slug: open-forex-rates-api
- collection_type: open
  name: Open Exchange Rates Account Reference API
  slug: open-forex-reference-api
- collection_type: open
  name: Open Exchange Rates API
  slug: open-forex
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/plans/forex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forex-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/rate-limits/forex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/forex-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/finops/forex-finops.yml
  title: ''
  type: FinOps
  url: finops/forex-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/agentic-access/forex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/forex-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/security/forex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forex-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/authentication/forex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forex-authentication.yml
created: '2024-01-15'
description: A collection of foreign exchange and currency conversion APIs.
finops:
- has_sources: false
  method: generated
  name: Forex Finops
  primary_unit: ''
  service_category: API
  slug: forex-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forex.png
layout: provider
modified: '2026-05-19'
name: Forex
nav: Providers
network: true
overview: 'Forex is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Rates API, Reference API, and 4 more. Tagged areas include Currency, Exchange Rates, Financial Data, Foreign Exchange, and Trading.


  Forex''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Forex Plans Pricing
  plan_count: 3
  slug: forex-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Forex Rate Limits
  slug: forex-rate-limits
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.0
    developer_ergonomics: 15.5
    discoverability: 62.5
    operational_transparency: 18.4
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/screenshots/forex-2026-06-20T181424.png
security:
- kind: authentication
  name: Forex Authentication
  slug: forex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Forex Domain Security
  slug: forex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: forex
tags:
- Currency
- Exchange Rates
- Financial Data
- Foreign Exchange
- Trading
---
