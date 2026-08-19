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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Waqi Agentic Access
  operation_count: 5
  slug: waqi-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Air quality feed endpoints for city, geo, and IP-based queries
  name: World Air Quality Index (WAQI) Feed API
  slug: waqi-feed-api
- description: Map tile and station boundary queries
  name: World Air Quality Index (WAQI) Map API
  slug: waqi-map-api
- description: Search for monitoring stations by keyword
  name: World Air Quality Index (WAQI) Search API
  slug: waqi-search-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: World Air Quality Index (WAQI) JSON Feed API
  slug: open-waqi-feed-api
- collection_type: open
  name: World Air Quality Index (WAQI) JSON Feed Map API
  slug: open-waqi-map-api
- collection_type: open
  name: World Air Quality Index (WAQI) JSON Feed Search API
  slug: open-waqi-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/waqi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waqi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waqi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://waqi.info/
- group: company
  title: ''
  type: Website
  url: https://aqicn.org/
- group: docs
  title: ''
  type: Documentation
  url: https://aqicn.org/json-api/doc/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/waqi-dev-community
- group: commercial
  title: ''
  type: Pricing
  url: https://aqicn.org/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/waqi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waqi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/waqi-finops.yml
created: '2026-06-13'
description: The World Air Quality Index (WAQI) REST API provides real-time air quality data, AQI readings, pollutant measurements, and station data for more than 12,000 monitoring stations worldwide. The API delivers city-level and station-level air quality index values for pollutants including PM2.5, PM10, NO2, CO, SO2, and Ozone, along with geo-location queries, weather conditions, and 3-8 day forecast data. Access is free for non-commercial use and requires a token obtained from the Air Quality Open Data Platform.
examples:
- key_count: 2
  name: City Feed Response
  slug: city-feed-response
- key_count: 2
  name: Map Bounds Response
  slug: map-bounds-response
- key_count: 2
  name: Search Response
  slug: search-response
finops:
- name: Waqi Finops
  service_category: ''
  slug: waqi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waqi.png
json_schemas:
- name: WAQI Feed Response
  property_count: 2
  slug: waqi-feed-response
jsonld:
- class_count: 3
  name: Waqi Context
  property_count: 44
  slug: waqi-context
layout: provider
modified: '2026-06-13'
name: World Air Quality Index (WAQI)
nav: Providers
network: true
overview: 'World Air Quality Index (WAQI) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Feed API, Map API, and Search API. Tagged areas include Air Quality, AQI, Environment, Pollution, and Real-Time Data.


  The World Air Quality Index (WAQI) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  World Air Quality Index (WAQI)''s developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Waqi Plans Pricing
  plan_count: 2
  slug: waqi-plans-pricing
random_paper: 136
rate_limits:
- limit_count: 2
  name: Waqi Rate Limits
  slug: waqi-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: World Air Quality Index (WAQI) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: waqi-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  delta: -2.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 65.1
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waqi/refs/heads/main/screenshots/waqi-2026-06-20T201226.png
security:
- kind: authentication
  name: Waqi Authentication
  slug: waqi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Waqi Domain Security
  slug: waqi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: waqi
tags:
- Air Quality
- AQI
- Environment
- Pollution
- Real-Time Data
- Weather
- IoT
- Open Data
website: https://waqi.info/
---
