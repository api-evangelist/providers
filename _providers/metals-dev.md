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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metals Dev Agentic Access
  operation_count: 6
  slug: metals-dev-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: Usage and quota information.
  name: Metals.Dev Account API
  slug: metals-dev-account-api
- description: Authority pricing from LBMA, LME, MCX, and IBJA.
  name: Metals.Dev Authority API
  slug: metals-dev-authority-api
- description: Currency rates and conversions.
  name: Metals.Dev Currency API
  slug: metals-dev-currency-api
- description: Latest and historical metal and currency rates.
  name: Metals.Dev Rates API
  slug: metals-dev-rates-api
- description: Spot pricing for individual metals.
  name: Metals.Dev Spot Prices API
  slug: metals-dev-spot-prices-api
artifact_total: 12
collections:
- collection_type: open
  name: Metals.Dev API
  slug: open-metals-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metals-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metals-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metals-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetalsDev
- group: start
  title: ''
  type: Portal
  url: https://metals.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://metals.dev/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://metals.dev/status
- group: start
  title: ''
  type: Signup
  url: https://metals.dev/sign-up
created: '2025-03-01'
description: Metals.Dev provides a developer-friendly JSON API for spot prices of precious metals, industrial metals, and currency conversion rates. It offers real-time prices from leading authorities including LBMA, LME, MCX, and IBJA, plus 5+ years of historical data.
finops:
- name: Metals Dev Finops
  service_category: API
  slug: metals-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metals-dev.png
layout: provider
modified: '2026-05-19'
name: Metals.Dev
nav: Providers
network: true
overview: 'Metals.Dev publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authority API, Currency API, and 2 more. Tagged areas include Financial Data, Gold, Precious Metals, Silver, and Spot Prices.


  Metals.Dev''s developer surface includes authentication, developer portal, pricing, signup flow, and 4 more developer resources.'
plans:
- name: Metals Dev Plans Pricing
  plan_count: 3
  slug: metals-dev-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Metals Dev Rate Limits
  slug: metals-dev-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metals-dev/refs/heads/main/screenshots/metals-dev-2026-06-20T185246.png
security:
- kind: authentication
  name: Metals Dev Authentication
  slug: metals-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metals Dev Domain Security
  slug: metals-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: metals-dev
tags:
- Financial Data
- Gold
- Precious Metals
- Silver
- Spot Prices
website: https://metals.dev/
---
