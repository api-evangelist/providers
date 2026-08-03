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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Provides up-to-hourly CO2 intensity and emissions data from the power sector for countries worldwide. Data is sourced from transmission system operators, market operators, and statistical agencies, co
  name: IEA Real-Time Emissions Factors API
  slug: iea-real-time-emissions-factors-api
- description: Programmatic access to IEA's suite of purchased data products including World Energy Balances, World Energy Statistics, Monthly Electricity Statistics, Energy Prices, and Emissions Factors. Uses beare
  name: IEA Data Products API
  slug: iea-data-products-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iea.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.iea.org/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/IEA-Paris
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/international-energy-agency
- group: company
  title: ''
  type: Blog
  url: https://www.iea.org/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iea.org/data-and-statistics/data-sets
- group: operate
  title: ''
  type: StatusPage
  url: https://www.iea.org/help-centre/accessing-iea-products-and-services
- group: other
  title: ''
  type: X
  url: https://x.com/IEA
- group: commercial
  title: ''
  type: Plans
  url: plans/iea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iea-finops.yml
created: '2026-06-13'
description: The International Energy Agency (IEA) provides a REST API for accessing global energy statistics, renewables data, CO2 emissions factors, monthly electricity generation data, oil market reports, and energy policy information. The IEA API enables programmatic access to authoritative energy data covering 150+ countries and offering up-to-hourly real-time emissions factors alongside comprehensive historical datasets.
finops:
- name: Iea Finops
  service_category: ''
  slug: iea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iea.png
layout: provider
modified: '2026-06-13'
name: International Energy Agency (IEA)
nav: Providers
network: true
overview: 'International Energy Agency (IEA) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electricity, CO2, Emissions, and Renewables.


  International Energy Agency (IEA)''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Iea Plans Pricing
  plan_count: 5
  slug: iea-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Iea Rate Limits
  slug: iea-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Iea Domain Security
  slug: iea-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iea
tags:
- Energy
- Electricity
- CO2
- Emissions
- Renewables
- Oil
- Statistics
- Climate
website: https://www.iea.org
---
