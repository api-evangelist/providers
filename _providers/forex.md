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
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
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
- description: The Account API from Forex — 1 operation(s) for account.
  name: Forex Account API
  slug: forex-account-api
- description: The Rates API from Forex — 3 operation(s) for rates.
  name: Forex Rates API
  slug: forex-rates-api
- description: The Reference API from Forex — 1 operation(s) for reference.
  name: Forex Reference API
  slug: forex-reference-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Exchange Rates API
  slug: open-forex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forex-authentication.yml
created: '2024-01-15'
description: A collection of foreign exchange and currency conversion APIs.
finops:
- name: Forex Finops
  service_category: API
  slug: forex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forex.png
layout: provider
modified: '2026-05-19'
name: Forex
nav: Providers
network: true
overview: 'Forex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Rates API, and Reference API. Tagged areas include Currency, Exchange Rates, Financial Data, Forex, and Trading.


  Forex''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Forex Plans Pricing
  plan_count: 3
  slug: forex-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Forex Rate Limits
  slug: forex-rate-limits
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
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
- Forex
- Trading
---
