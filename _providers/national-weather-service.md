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
  name: National Weather Service Agentic Access
  operation_count: 65
  slug: national-weather-service-agentic-access
  summary_line: 65 operations
api_count: 13
apis:
- description: The Alerts API from National Weather Service — 8 operation(s) for alerts.
  name: National Weather Service Alerts API
  slug: national-weather-service-alerts-api
- description: The Aviation API from National Weather Service — 7 operation(s) for aviation.
  name: National Weather Service Aviation API
  slug: national-weather-service-aviation-api
- description: The Glossary API from National Weather Service — 1 operation(s) for glossary.
  name: National Weather Service Glossary API
  slug: national-weather-service-glossary-api
- description: The Gridpoints API from National Weather Service — 4 operation(s) for gridpoints.
  name: National Weather Service Gridpoints API
  slug: national-weather-service-gridpoints-api
- description: The Icons API from National Weather Service — 3 operation(s) for icons.
  name: National Weather Service Icons API
  slug: national-weather-service-icons-api
- description: The Offices API from National Weather Service — 8 operation(s) for offices.
  name: National Weather Service Offices API
  slug: national-weather-service-offices-api
- description: The Points API from National Weather Service — 3 operation(s) for points.
  name: National Weather Service Points API
  slug: national-weather-service-points-api
- description: The Products API from National Weather Service — 9 operation(s) for products.
  name: National Weather Service Products API
  slug: national-weather-service-products-api
- description: The Radar API from National Weather Service — 7 operation(s) for radar.
  name: National Weather Service Radar API
  slug: national-weather-service-radar-api
- description: The Radio API from National Weather Service — 1 operation(s) for radio.
  name: National Weather Service Radio API
  slug: national-weather-service-radio-api
- description: The Stations API from National Weather Service — 7 operation(s) for stations.
  name: National Weather Service Stations API
  slug: national-weather-service-stations-api
- description: The Thumbnails API from National Weather Service — 1 operation(s) for thumbnails.
  name: National Weather Service Thumbnails API
  slug: national-weather-service-thumbnails-api
- description: The Zones API from National Weather Service — 6 operation(s) for zones.
  name: National Weather Service Zones API
  slug: national-weather-service-zones-api
artifact_total: 20
collections:
- collection_type: open
  name: weather.gov API
  slug: open-national-weather-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-weather-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-weather-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-weather-service-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weather-gov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/noaa-nws
- group: company
  title: ''
  type: Website
  url: https://www.weather.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.weather.gov/documentation/services-web-api
created: '2024-01-01'
description: The National Weather Service (NWS) is a government agency within the National Oceanic and Atmospheric Administration (NOAA) that is responsible for providing weather forecasts, warnings, and other meteorological information to the public, government agencies, and private industries.
finops:
- name: National Weather Service Finops
  service_category: API
  slug: national-weather-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-weather-service.png
layout: provider
modified: '2026-05-19'
name: National Weather Service
nav: Providers
network: true
overview: 'National Weather Service publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Aviation API, Glossary API, and 10 more. Tagged areas include Federal Government, Forecasting, and Weather.


  National Weather Service''s developer surface includes authentication, developer portal, and 5 more developer resources.'
plans:
- name: National Weather Service Plans Pricing
  plan_count: 3
  slug: national-weather-service-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: National Weather Service Rate Limits
  slug: national-weather-service-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.7
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-weather-service/refs/heads/main/screenshots/national-weather-service-2026-06-20T190047.png
security:
- kind: authentication
  name: National Weather Service Authentication
  slug: national-weather-service-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: National Weather Service Domain Security
  slug: national-weather-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-weather-service
tags:
- Federal Government
- Forecasting
- Weather
website: https://www.weather.gov/
---
