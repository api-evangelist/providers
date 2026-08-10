---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Renewable Energy Laboratory Agentic Access
  operation_count: 5
  slug: national-renewable-energy-laboratory-agentic-access
  summary_line: 5 operations
api_count: 8
apis:
- description: Locate alternative fuel stations across the United States with filters for fuel type, location, status, and access.
  name: Alternative Fuel Stations
  slug: alternative-fuel-stations
- description: Estimate the energy production and cost of grid-connected photovoltaic energy systems for any location.
  name: PVWatts
  slug: pvwatts
- description: Average commercial, industrial, and residential utility rates by US location.
  name: Utility Rates
  slug: utility-rates
- description: Average direct normal, global horizontal, and tilt at latitude irradiance for a US location.
  name: Solar Resource Data
  slug: solar-resource-data
- description: The Alt Fuel Stations API from National Renewable Energy Laboratory — 2 operation(s) for alt fuel stations.
  name: National Renewable Energy Laboratory Alt Fuel Stations API
  slug: national-renewable-energy-laboratory-alt-fuel-stations-api
- description: The Pvwatts API from National Renewable Energy Laboratory — 1 operation(s) for pvwatts.
  name: National Renewable Energy Laboratory Pvwatts API
  slug: national-renewable-energy-laboratory-pvwatts-api
- description: The Solar API from National Renewable Energy Laboratory — 1 operation(s) for solar.
  name: National Renewable Energy Laboratory Solar API
  slug: national-renewable-energy-laboratory-solar-api
- description: The Utility Rates API from National Renewable Energy Laboratory — 1 operation(s) for utility rates.
  name: National Renewable Energy Laboratory Utility Rates API
  slug: national-renewable-energy-laboratory-utility-rates-api
artifact_total: 14
collections:
- collection_type: open
  name: NREL Developer Network APIs
  slug: open-national-renewable-energy-laboratory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-renewable-energy-laboratory-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-renewable-energy-laboratory-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NREL
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-renewable-energy-laboratory
- group: company
  title: ''
  type: Website
  url: https://www.nrel.gov/
- group: start
  title: ''
  type: Portal
  url: https://developer.nrel.gov/
- group: start
  title: ''
  type: Signup
  url: https://developer.nrel.gov/signup/
created: '2025-05-02'
description: The National Renewable Energy Laboratory (NREL) developer network provides a catalog of public APIs that give developers access to renewable energy, alternative fuel, electricity, building, climate, solar, wind, and transportation data and analysis services produced by NREL.
finops:
- name: National Renewable Energy Laboratory Finops
  service_category: Open Data / Public Sector / Energy
  slug: national-renewable-energy-laboratory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-renewable-energy-laboratory.png
layout: provider
modified: '2026-05-19'
name: National Renewable Energy Laboratory
nav: Providers
network: true
overview: 'National Renewable Energy Laboratory publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alt Fuel Stations API, Pvwatts API, Solar API, and 1 more. Tagged areas include Energy, Renewable Energy, Federal Government, Climate, and Research.


  National Renewable Energy Laboratory''s developer surface includes authentication, developer portal, signup flow, and 4 more developer resources.'
plans:
- name: National Renewable Energy Laboratory Plans Pricing
  plan_count: 2
  slug: national-renewable-energy-laboratory-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 3
  name: National Renewable Energy Laboratory Rate Limits
  slug: national-renewable-energy-laboratory-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: National Renewable Energy Laboratory Authentication
  slug: national-renewable-energy-laboratory-authentication
  summary_line: apiKey · 1 scheme
slug: national-renewable-energy-laboratory
tags:
- Energy
- Renewable Energy
- Federal Government
- Climate
- Research
website: https://www.nrel.gov/
---
