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
  name: Stormglass Agentic Access
  operation_count: 10
  slug: stormglass-agentic-access
  summary_line: 10 operations
api_count: 7
apis:
- description: Solar and lunar astronomical data including sunrise, sunset, moon phases
  name: Stormglass Astronomy API
  slug: stormglass-astronomy-api
- description: Biological and oceanographic data including chlorophyll and nutrients
  name: Stormglass Bio API
  slug: stormglass-bio-api
- description: Global elevation and bathymetry data
  name: Stormglass Elevation API
  slug: stormglass-elevation-api
- description: Marine environment data including waves, currents, and water temperature
  name: Stormglass Marine API
  slug: stormglass-marine-api
- description: Solar radiation and UV index data
  name: Stormglass Solar API
  slug: stormglass-solar-api
- description: Tidal data including extremes, sea level, and tide station listings
  name: Stormglass Tides API
  slug: stormglass-tides-api
- description: Point weather forecasts and historical weather data
  name: Stormglass Weather API
  slug: stormglass-weather-api
artifact_total: 23
collections:
- collection_type: open
  name: Stormglass API
  slug: open-stormglass
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stormglass-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stormglass-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stormglass-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stormglassio
- group: start
  title: ''
  type: Portal
  url: https://stormglass.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stormglass.io/
- group: start
  title: ''
  type: Signup
  url: https://stormglass.io/register
- group: commercial
  title: ''
  type: Pricing
  url: https://stormglass.io/pricing
- group: company
  title: ''
  type: Website
  url: https://stormglass.io/
- group: company
  title: ''
  type: Blog
  url: https://stormglass.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stormglass.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stormglass.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stormglass
created: '2025-05-02'
description: Stormglass provides a global marine and weather API delivering high-resolution forecasts, historical data, and environmental measurements for any coordinate on Earth. The platform aggregates data from multiple authoritative sources including NOAA, ECMWF, DWD, and others to provide weather point forecasts, marine data, tidal information, solar and astronomical data, biological oceanographic data, and elevation/bathymetry data. Used widely for maritime navigation, renewable energy forecasting, outdoor activity planning, and environmental monitoring applications.
examples:
- key_count: 2
  name: Stormglass Get Astronomy Point Example
  slug: stormglass-get-astronomy-point-example
- key_count: 2
  name: Stormglass Get Tide Extremes Example
  slug: stormglass-get-tide-extremes-example
- key_count: 2
  name: Stormglass Get Weather Point Example
  slug: stormglass-get-weather-point-example
finops:
- name: Stormglass Finops
  service_category: API
  slug: stormglass-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stormglass.png
json_schemas:
- name: Tide Extremes Response
  property_count: 2
  slug: stormglass-tide-extremes
- name: Weather Point Response
  property_count: 2
  slug: stormglass-weather-point
json_structures:
- name: Stormglass Weather Point Structure
  property_count: 0
  slug: stormglass-weather-point-structure
jsonld:
- class_count: 16
  name: Stormglass Context
  property_count: 19
  slug: stormglass-context
layout: provider
modified: '2026-05-19'
name: Stormglass
nav: Providers
network: true
overview: 'Stormglass publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Astronomy API, Bio API, Elevation API, and 4 more. Tagged areas include Astronomy, Bio, Climate, Elevation, and Forecasting.


  The Stormglass catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stormglass'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Stormglass Plans Pricing
  plan_count: 3
  slug: stormglass-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Stormglass Rate Limits
  slug: stormglass-rate-limits
rules:
- name: Stormglass API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: stormglass-jsonschema-spectral-rules
- name: Stormglass API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: stormglass-rules
score:
  band: developing
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.9
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 58.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stormglass/refs/heads/main/screenshots/stormglass-2026-06-20T194607.png
security:
- kind: authentication
  name: Stormglass Authentication
  slug: stormglass-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stormglass Domain Security
  slug: stormglass-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stormglass
tags:
- Astronomy
- Bio
- Climate
- Elevation
- Forecasting
- Marine
- Ocean
- Solar
- Tides
- Weather
- Wind
website: https://stormglass.io/
---
