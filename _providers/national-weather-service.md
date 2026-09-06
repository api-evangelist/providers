---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Weather Service Agentic Access
  operation_count: 65
  slug: national-weather-service-agentic-access
  summary_line: 65 operations
api_count: 1
apis:
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Alerts API from National Weather Service — 8 operation(s) for alerts.
  name: National Weather Service Alerts API
  slug: national-weather-service-alerts-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Aviation API from National Weather Service — 7 operation(s) for aviation.
  name: National Weather Service Aviation API
  slug: national-weather-service-aviation-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Glossary API from National Weather Service — 1 operation(s) for glossary.
  name: National Weather Service Glossary API
  slug: national-weather-service-glossary-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Gridpoints API from National Weather Service — 4 operation(s) for gridpoints.
  name: National Weather Service Gridpoints API
  slug: national-weather-service-gridpoints-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Icons API from National Weather Service — 3 operation(s) for icons.
  name: National Weather Service Icons API
  slug: national-weather-service-icons-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Offices API from National Weather Service — 8 operation(s) for offices.
  name: National Weather Service Offices API
  slug: national-weather-service-offices-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Points API from National Weather Service — 3 operation(s) for points.
  name: National Weather Service Points API
  slug: national-weather-service-points-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Products API from National Weather Service — 9 operation(s) for products.
  name: National Weather Service Products API
  slug: national-weather-service-products-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Radar API from National Weather Service — 7 operation(s) for radar.
  name: National Weather Service Radar API
  slug: national-weather-service-radar-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Radio API from National Weather Service — 1 operation(s) for radio.
  name: National Weather Service Radio API
  slug: national-weather-service-radio-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Stations API from National Weather Service — 7 operation(s) for stations.
  name: National Weather Service Stations API
  slug: national-weather-service-stations-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Thumbnails API from National Weather Service — 1 operation(s) for thumbnails.
  name: National Weather Service Thumbnails API
  slug: national-weather-service-thumbnails-api
- baseURL: https://api.weather.gov/
  baseurl_source: declared
  description: The Zones API from National Weather Service — 6 operation(s) for zones.
  name: National Weather Service Zones API
  slug: national-weather-service-zones-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: weather.gov Alerts API
  slug: open-national-weather-service-alerts-api
- collection_type: open
  name: weather.gov Alerts Aviation API
  slug: open-national-weather-service-aviation-api
- collection_type: open
  name: weather.gov Alerts Glossary API
  slug: open-national-weather-service-glossary-api
- collection_type: open
  name: weather.gov Alerts Gridpoints API
  slug: open-national-weather-service-gridpoints-api
- collection_type: open
  name: weather.gov Alerts Icons API
  slug: open-national-weather-service-icons-api
- collection_type: open
  name: weather.gov Alerts Offices API
  slug: open-national-weather-service-offices-api
- collection_type: open
  name: weather.gov Alerts Points API
  slug: open-national-weather-service-points-api
- collection_type: open
  name: weather.gov Alerts Products API
  slug: open-national-weather-service-products-api
- collection_type: open
  name: weather.gov Alerts Radar API
  slug: open-national-weather-service-radar-api
- collection_type: open
  name: weather.gov Alerts Radio API
  slug: open-national-weather-service-radio-api
- collection_type: open
  name: weather.gov Alerts Stations API
  slug: open-national-weather-service-stations-api
- collection_type: open
  name: weather.gov Alerts Thumbnails API
  slug: open-national-weather-service-thumbnails-api
- collection_type: open
  name: weather.gov Alerts Zones API
  slug: open-national-weather-service-zones-api
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
overview: 'National Weather Service publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Aviation API, Glossary API, and 10 more. Tagged areas include Federal-Government, Forecasting, and Weather.


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
  composite: 28.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Federal-Government
- Forecasting
- Weather
website: https://www.weather.gov/
---
