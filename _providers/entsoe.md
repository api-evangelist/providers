---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Synchronous RESTful interface for accessing European electricity market data including load, generation, transmission, balancing, outages, congestion management, and system operations datasets. Authen
  name: ENTSO-E Transparency Platform REST API
  slug: entso-e-transparency-platform-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entsoe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.entsoe.eu/
- group: other
  title: ''
  type: TransparencyPlatform
  url: https://transparency.entsoe.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
- group: other
  title: ''
  type: KnowledgeBase
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EnergieID/entsoe-py
- group: docs
  title: ''
  type: PostmanDocumentation
  url: https://documenter.getpostman.com/view/7009892/2s93JtP3F6
- group: other
  title: ''
  type: Registration
  url: https://transparency.entsoe.eu/usrm/user/createPublicUser
- group: operate
  title: ''
  type: Contact
  url: https://www.entsoe.eu/contact/
- group: company
  title: ''
  type: About
  url: https://www.entsoe.eu/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
- group: other
  title: ''
  type: Email
  url: mailto:transparency@entsoe.eu
description: European Network of Transmission System Operators for Electricity (ENTSO-E) provides the Transparency Platform REST API, a synchronous RESTful interface for accessing pan-European electricity market data. The API delivers datasets covering load forecasts, actual generation per type and per plant, installed generation capacity, day-ahead prices, cross-border flows, scheduled exchanges, transfer capacities, balancing data, hydro storage, outage information, and congestion management data. Data is collected from Transmission System Operators, power exchanges, and qualified third-party providers across Europe in compliance with EU Regulation 543/2013.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.entsoe.eu/assets/images/entsoe-logo.png
layout: provider
modified: '2026-06-13'
name: ENTSO-E
nav: Providers
network: true
overview: 'ENTSO-E publishes 1 API on the [APIs.io](https://apis.io/) network: Transparency Platform REST API. Tagged areas include Energy, Electricity, European Union, Transparency, and Market Data.


  ENTSO-E''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 80
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 16.6
  delta: -3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/entsoe/refs/heads/main/screenshots/entsoe-2026-06-20T180732.png
security:
- kind: domain-security
  name: Entsoe Domain Security
  slug: entsoe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: entsoe
tags:
- Energy
- Electricity
- European Union
- Transparency
- Market Data
- Generation
- Transmission
- Load Forecasting
- Day-Ahead Prices
- Cross-Border Flows
website: https://www.entsoe.eu/
---
