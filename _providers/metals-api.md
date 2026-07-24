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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metals Api Agentic Access
  operation_count: 9
  slug: metals-api-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: Time series, fluctuation, and OHLC analytics.
  name: Metals-API Analytics API
  slug: metals-api-analytics-api
- description: Currency and metal conversion endpoints.
  name: Metals-API Conversion API
  slug: metals-api-conversion-api
- description: Real-time and historical precious metals rates.
  name: Metals-API Rates API
  slug: metals-api-rates-api
- description: Symbols and reference data.
  name: Metals-API Reference API
  slug: metals-api-reference-api
artifact_total: 11
collections:
- collection_type: open
  name: Metals-API
  slug: open-metals-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metals-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metals-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metals-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zyla-labs
- group: start
  title: ''
  type: Portal
  url: https://metals-api.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://metals-api.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://metals-api.com/signup
created: '2025-03-01'
description: Metals-API provides a free, simple, and lightweight JSON API for current and historical precious metals rates and currency conversion. It supports real-time and historical data for gold, silver, platinum, palladium, and other metals in 170 world currencies.
finops:
- name: Metals Api Finops
  service_category: API
  slug: metals-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metals-api.png
layout: provider
modified: '2026-05-19'
name: Metals-API
nav: Providers
network: true
overview: 'Metals-API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Conversion API, Rates API, and 1 more. Tagged areas include Currency, Financial Data, Gold, Precious Metals, and Silver.


  Metals-API''s developer surface includes authentication, developer portal, pricing, signup flow, and 3 more developer resources.'
plans:
- name: Metals Api Plans Pricing
  plan_count: 3
  slug: metals-api-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Metals Api Rate Limits
  slug: metals-api-rate-limits
score:
  band: thin
  composite: 38.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.6
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metals-api/refs/heads/main/screenshots/metals-api-2026-06-20T185245.png
security:
- kind: authentication
  name: Metals Api Authentication
  slug: metals-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metals Api Domain Security
  slug: metals-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: metals-api
tags:
- Currency
- Financial Data
- Gold
- Precious Metals
- Silver
website: https://metals-api.com/
---
