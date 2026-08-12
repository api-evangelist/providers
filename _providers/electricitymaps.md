---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Electricitymaps Agentic Access
  operation_count: 10
  slug: electricitymaps-agentic-access
  summary_line: 10 operations
api_count: 7
apis:
- description: The Carbon Intensity API from Electricity Maps — 3 operation(s) for carbon intensity.
  name: Electricity Maps Carbon Intensity API
  slug: electricitymaps-carbon-intensity-api
- description: The Forecast API from Electricity Maps — 2 operation(s) for forecast.
  name: Electricity Maps Forecast API
  slug: electricitymaps-forecast-api
- description: The Health API from Electricity Maps — 1 operation(s) for health.
  name: Electricity Maps Health API
  slug: electricitymaps-health-api
- description: The Power Breakdown API from Electricity Maps — 3 operation(s) for power breakdown.
  name: Electricity Maps Power Breakdown API
  slug: electricitymaps-power-breakdown-api
- description: The Power Consumption API from Electricity Maps — 1 operation(s) for power consumption.
  name: Electricity Maps Power Consumption API
  slug: electricitymaps-power-consumption-api
- description: The Power Production API from Electricity Maps — 1 operation(s) for power production.
  name: Electricity Maps Power Production API
  slug: electricitymaps-power-production-api
- description: The Zones API from Electricity Maps — 1 operation(s) for zones.
  name: Electricity Maps Zones API
  slug: electricitymaps-zones-api
artifact_total: 15
collections:
- collection_type: open
  name: Electricity Maps API
  slug: open-electricity-maps
- collection_type: open
  name: Electricity Maps API
  slug: open-electricitymaps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/electricitymaps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electricitymaps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/electricitymaps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/electricitymaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electricitymaps
- group: company
  title: ''
  type: Website
  url: https://www.electricitymaps.com
- group: docs
  title: ''
  type: Documentation
  url: https://portal.electricitymaps.com/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/electricitymaps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/electricitymaps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/electricitymaps-finops.yml
- group: other
  title: ''
  type: Application
  url: https://app.electricitymaps.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.electricitymaps.com/api-pricing
- group: company
  title: ''
  type: Blog
  url: https://www.electricitymaps.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/electricitymaps
created: '2026-06-21'
description: Electricity Maps provides electricity grid data - carbon intensity and power production/consumption breakdown - for 200+ zones worldwide, in real time, as historical series, and as 24-72 hour forecasts. The REST API serves the same data behind the live electricity map at app.electricitymap.org, authenticated with an auth-token header.
finops:
- name: Electricitymaps Finops
  service_category: Analytics
  slug: electricitymaps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electricitymaps.png
layout: provider
modified: '2026-08-08'
name: Electricity Maps
nav: Providers
network: true
overview: 'Electricity Maps publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Carbon Intensity API, Forecast API, Health API, and 4 more. Tagged areas include Energy, Carbon Intensity, Electricity, Grid, and Sustainability.


  Electricity Maps'' developer surface includes authentication, documentation, pricing, engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Electricitymaps Plans Pricing
  plan_count: 4
  slug: electricitymaps-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 6
  name: Electricitymaps Rate Limits
  slug: electricitymaps-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electricitymaps/refs/heads/main/screenshots/electricitymaps-2026-07-25T213108.png
security:
- kind: authentication
  name: Electricitymaps Authentication
  slug: electricitymaps-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Electricitymaps Domain Security
  slug: electricitymaps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electricitymaps
tags:
- Energy
- Carbon Intensity
- Electricity
- Grid
- Sustainability
website: https://www.electricitymaps.com
---
