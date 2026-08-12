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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Airvisual Agentic Access
  operation_count: 9
  slug: airvisual-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: List supported cities and retrieve city air quality data
  name: IQAir AirVisual Cities API
  slug: airvisual-cities-api
- description: List supported countries
  name: IQAir AirVisual Countries API
  slug: airvisual-countries-api
- description: City air quality rankings
  name: IQAir AirVisual Rankings API
  slug: airvisual-rankings-api
- description: List supported states within a country
  name: IQAir AirVisual States API
  slug: airvisual-states-api
- description: List monitoring stations and retrieve station data
  name: IQAir AirVisual Stations API
  slug: airvisual-stations-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airvisual-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airvisual-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airvisual-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.iqair.com/us/air-pollution-data-api
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.iqair.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iqair.com/us/air-pollution-data-api
- group: company
  title: ''
  type: Blog
  url: https://www.iqair.com/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-iqair-group/
- group: other
  title: ''
  type: X
  url: https://x.com/IQAir
- group: commercial
  title: ''
  type: Plans
  url: plans/airvisual-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airvisual-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airvisual-finops.yml
created: '2026-06-13'
description: IQAir AirVisual provides a real-time air quality REST API delivering PM2.5, PM10, AQI, weather data, and pollution forecasts for cities and GPS coordinates worldwide. The API aggregates data from over 80,000 ground-based sensors, satellite sources, and regulatory monitors, validated with AI-driven machine learning.
examples:
- key_count: 4
  name: City Ranking
  slug: city-ranking
- key_count: 4
  name: Get City Air Quality
  slug: get-city-air-quality
- key_count: 4
  name: Get Nearest City
  slug: get-nearest-city
- key_count: 4
  name: List Countries
  slug: list-countries
finops:
- name: Airvisual Finops
  service_category: ''
  slug: airvisual-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airvisual.png
json_schemas:
- name: CityData
  property_count: 2
  slug: city-data
- name: StationData
  property_count: 2
  slug: station-data
jsonld:
- class_count: 33
  name: Airvisual Context
  property_count: 1
  slug: airvisual-context
layout: provider
modified: '2026-06-13'
name: IQAir AirVisual
nav: Providers
network: true
overview: 'IQAir AirVisual publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cities API, Countries API, Rankings API, and 2 more. Tagged areas include Air Quality, AQI, PM2.5, Weather, and Pollution.


  The IQAir AirVisual catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IQAir AirVisual''s developer surface includes authentication, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Airvisual Plans Pricing
  plan_count: 3
  slug: airvisual-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Airvisual Rate Limits
  slug: airvisual-rate-limits
rules:
- name: IQAir AirVisual API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: airvisual-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airvisual/refs/heads/main/screenshots/airvisual-2026-06-20T171441.png
security:
- kind: authentication
  name: Airvisual Authentication
  slug: airvisual-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airvisual Domain Security
  slug: airvisual-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airvisual
tags:
- Air Quality
- AQI
- PM2.5
- Weather
- Pollution
- Environmental Data
- Real-Time Data
website: https://www.iqair.com/us/air-pollution-data-api
---
