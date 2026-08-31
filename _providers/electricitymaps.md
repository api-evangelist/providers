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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Electricitymaps Agentic Access
  operation_count: 10
  slug: electricitymaps-agentic-access
  summary_line: 10 operations
api_count: 1
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
- description: Carbon intensity (gCO2eq/kWh) signals.
  name: Electricity Maps Carbon Intensity API
  slug: electricitymaps-carbonintensity-api
- description: Power production and consumption breakdown by source.
  name: Electricity Maps Electricity Mix API
  slug: electricitymaps-electricitymix-api
- description: Total load, net load, and electricity flows between zones.
  name: Electricity Maps Grid Metrics API
  slug: electricitymaps-gridmetrics-api
- description: Day-ahead electricity pricing.
  name: Electricity Maps Pricing API
  slug: electricitymaps-pricing-api
- description: Renewable and carbon-free percentage signals.
  name: Electricity Maps Renewables API
  slug: electricitymaps-renewables-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Electricity Maps API
  slug: open-electricity-maps
- collection_type: open
  name: Electricity Maps Carbon Intensity API
  slug: open-electricitymaps-carbon-intensity-api
- collection_type: open
  name: Electricity Maps CarbonIntensity API
  slug: open-electricitymaps-carbonintensity-api
- collection_type: open
  name: Electricity Maps CarbonIntensity ElectricityMix API
  slug: open-electricitymaps-electricitymix-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Forecast API
  slug: open-electricitymaps-forecast-api
- collection_type: open
  name: Electricity Maps CarbonIntensity GridMetrics API
  slug: open-electricitymaps-gridmetrics-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Health API
  slug: open-electricitymaps-health-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Power Breakdown API
  slug: open-electricitymaps-power-breakdown-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Power Consumption API
  slug: open-electricitymaps-power-consumption-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Power Production API
  slug: open-electricitymaps-power-production-api
- collection_type: open
  name: Electricity Maps CarbonIntensity Pricing API
  slug: open-electricitymaps-pricing-api
- collection_type: open
  name: Electricity Maps CarbonIntensity Renewables API
  slug: open-electricitymaps-renewables-api
- collection_type: open
  name: Electricity Maps Carbon Intensity Zones API
  slug: open-electricitymaps-zones-api
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
overview: 'Electricity Maps publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Carbon Intensity API, Forecast API, Health API, and 9 more. Tagged areas include Energy, Carbon Intensity, Electricity, Grid, and Sustainability.


  Electricity Maps'' developer surface includes authentication, documentation, pricing, engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Electricitymaps Plans Pricing
  plan_count: 4
  slug: electricitymaps-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Electricitymaps Rate Limits
  slug: electricitymaps-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.9
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
