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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Electricity Maps Agentic Access
  operation_count: 12
  slug: electricity-maps-agentic-access
  summary_line: 12 operations
api_count: 6
apis:
- description: Carbon intensity (gCO2eq/kWh) signals.
  name: Electricity Maps CarbonIntensity API
  slug: electricity-maps-carbonintensity-api
- description: Power production and consumption breakdown by source.
  name: Electricity Maps ElectricityMix API
  slug: electricity-maps-electricitymix-api
- description: Total load, net load, and electricity flows between zones.
  name: Electricity Maps GridMetrics API
  slug: electricity-maps-gridmetrics-api
- description: Day-ahead electricity pricing.
  name: Electricity Maps Pricing API
  slug: electricity-maps-pricing-api
- description: Renewable and carbon-free percentage signals.
  name: Electricity Maps Renewables API
  slug: electricity-maps-renewables-api
- description: Discover available zones and locate them by coordinates or data center.
  name: Electricity Maps Zones API
  slug: electricity-maps-zones-api
artifact_total: 13
collections:
- collection_type: open
  name: Electricity Maps API
  slug: open-electricity-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/electricity-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electricity-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/electricity-maps-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electricitymaps
- group: company
  title: ''
  type: Website
  url: https://www.electricitymaps.com
- group: other
  title: ''
  type: Application
  url: https://app.electricitymaps.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.electricitymaps.com/api-pricing
- group: docs
  title: ''
  type: Documentation
  url: https://app.electricitymaps.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.electricitymaps.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/electricitymaps
created: '2025-05-02'
description: Electricity Maps tracks the carbon intensity and electricity mix of power grids around the world. Their commercial API delivers real-time, historical, and forecasted signals for carbon intensity, power source breakdown, renewable and carbon-free percentages, electricity flows, grid load, and day-ahead pricing across hundreds of geographic zones, enabling data centers, software platforms, and sustainability teams to make emissions-aware decisions.
finops:
- name: Electricity Maps Finops
  service_category: API
  slug: electricity-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electricity-maps.png
layout: provider
modified: '2026-05-19'
name: Electricity Maps
nav: Providers
network: true
overview: 'Electricity Maps publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CarbonIntensity API, ElectricityMix API, GridMetrics API, and 3 more. Tagged areas include Energy, Electricity, Carbon Intensity, Sustainability, and Climate.


  Electricity Maps'' developer surface includes authentication, pricing, documentation, engineering blog, GitHub presence, and 5 more developer resources.'
plans:
- name: Electricity Maps Plans Pricing
  plan_count: 3
  slug: electricity-maps-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Electricity Maps Rate Limits
  slug: electricity-maps-rate-limits
score:
  band: thin
  composite: 42.2
  delta: 3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electricity-maps/refs/heads/main/screenshots/electricity-maps-2026-06-20T180603.png
security:
- kind: authentication
  name: Electricity Maps Authentication
  slug: electricity-maps-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Electricity Maps Domain Security
  slug: electricity-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electricity-maps
tags:
- Energy
- Electricity
- Carbon Intensity
- Sustainability
- Climate
- Grid Data
website: https://www.electricitymaps.com
---
