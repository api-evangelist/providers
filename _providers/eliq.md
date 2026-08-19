---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The Eliq Auth API authenticates client applications and issues access tokens used to call the Insights, Data Management, and Intelligence APIs. It supports the credential flows required for utility-si
  name: Eliq Auth API
  slug: auth
- description: The Eliq Data Management API ingests and manages customer, location, and meter data inside the Eliq system. Clients use it to provision users and locations, post energy consumption readings, attach me
  name: Eliq Data Management API
  slug: data-management
- description: The Eliq Insights API delivers analytics and presentation-ready data for end-user energy applications. It exposes consumption aggregates by day, week, month, and year, trends, cost, CO2 footprint, day
  name: Eliq Insights API
  slug: insights
- description: The Eliq Intelligence API provides customer-level analytics designed for utility service, operations, and growth teams. It supports customer segmentation, behavioral classification, and personalized r
  name: Eliq Intelligence API
  slug: intelligence
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eliq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetEliq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eliq
- group: company
  title: ''
  type: Website
  url: https://eliq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eliq.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eliq.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://eliq.com/api/
- group: company
  title: ''
  type: Blog
  url: https://eliq.com/insights
created: '2025-05-02'
description: Eliq provides energy data and analytics APIs for utilities and energy app developers. The platform combines a decade of analytics and machine learning trained on millions of homes to deliver consumption insights, disaggregation, forecasting, peak detection, tariff comparison, and customer segmentation.
finops:
- name: Eliq Finops
  service_category: API
  slug: eliq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eliq.png
layout: provider
modified: '2026-04-28'
name: Eliq
nav: Providers
network: true
overview: 'Eliq publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Analytics, and Sustainability.


  Eliq''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Eliq Plans Pricing
  plan_count: 3
  slug: eliq-plans-pricing
random_paper: 129
rate_limits:
- limit_count: 5
  name: Eliq Rate Limits
  slug: eliq-rate-limits
score:
  band: emerging
  composite: 12.7
  delta: -0.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eliq/refs/heads/main/screenshots/eliq-2026-06-20T180608.png
security:
- kind: domain-security
  name: Eliq Domain Security
  slug: eliq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eliq
tags:
- Energy
- Utilities
- Analytics
- Sustainability
website: https://eliq.com
---
