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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Exchangerate Agentic Access
  operation_count: 7
  slug: exchangerate-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: API quota and account information
  name: ExchangeRate-API Account API
  slug: exchangerate-account-api
- description: Supported currency codes and metadata
  name: ExchangeRate-API Currencies API
  slug: exchangerate-currencies-api
- description: Real-time and historical currency exchange rate endpoints
  name: ExchangeRate-API Exchange Rates API
  slug: exchangerate-exchange-rates-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ExchangeRate Account API
  slug: open-exchangerate-account-api
- collection_type: open
  name: ExchangeRate Account Currencies API
  slug: open-exchangerate-currencies-api
- collection_type: open
  name: ExchangeRate Account Exchange Rates API
  slug: open-exchangerate-exchange-rates-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exchangerate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exchangerate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exchangerate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.exchangerate-api.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.exchangerate-api.com/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exchangerate-api.com/#pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.pingdom.com/qv69spvrz94m/8069768
- group: start
  title: ''
  type: Signup
  url: https://app.exchangerate-api.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.exchangerate-api.com/sign-in
- group: operate
  title: ''
  type: UptimePage
  url: https://www.exchangerate-api.com/product/uptime
- group: commercial
  title: ''
  type: Plans
  url: plans/exchangerate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exchangerate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/exchangerate-finops.yml
created: '2026-06-13'
description: ExchangeRate-API is a currency exchange rate REST API providing real-time and historical exchange rates for 165 currencies across 200 countries. Operating since 2010, the service delivers reliable currency conversion data via simple HTTP GET requests, supporting both URL-embedded and Bearer token authentication. It offers a free tier with 1,500 monthly requests and daily updates, plus paid plans with hourly or 5-minute update frequencies and higher quotas. The API features over 99.99% measured uptime backed by multi-AZ AWS infrastructure and Cloudflare CDN, with historical data available back to 1990.
examples:
- key_count: 2
  name: Error Response
  slug: error-response
- key_count: 9
  name: Latest Rates Response
  slug: latest-rates-response
- key_count: 11
  name: Pair Conversion Response
  slug: pair-conversion-response
- key_count: 4
  name: Supported Codes Response
  slug: supported-codes-response
finops:
- name: Exchangerate Finops
  service_category: ''
  slug: exchangerate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exchangerate.png
json_schemas:
- name: ExchangeRate-API Schemas
  property_count: 0
  slug: exchangerate
jsonld:
- class_count: 10
  name: Exchangerate Context
  property_count: 13
  slug: exchangerate-context
layout: provider
modified: '2026-06-13'
name: ExchangeRate-API
nav: Providers
network: true
overview: 'ExchangeRate-API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Currencies API, and Exchange Rates API. Tagged areas include Currency, Exchange Rates, Finance, Forex, and Financial Data.


  The ExchangeRate-API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ExchangeRate-API''s developer surface includes authentication, documentation, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Exchangerate Plans Pricing
  plan_count: 4
  slug: exchangerate-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Exchangerate Rate Limits
  slug: exchangerate-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ExchangeRate-API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: exchangerate-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 9.8
    contract_quality: 73.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exchangerate/refs/heads/main/screenshots/exchangerate-2026-06-20T180922.png
security:
- kind: authentication
  name: Exchangerate Authentication
  slug: exchangerate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exchangerate Domain Security
  slug: exchangerate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: exchangerate
tags:
- Currency
- Exchange Rates
- Finance
- Forex
- Financial Data
- Currency Conversion
website: https://www.exchangerate-api.com
---
