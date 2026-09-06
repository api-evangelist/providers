---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Meteo Agentic Access
  operation_count: 9
  slug: open-meteo-agentic-access
  summary_line: 9 operations
api_count: 9
apis:
- description: Converts place names and city searches into geographic coordinates and returns metadata such as country, timezone, population, and elevation to facilitate location lookup within weather application wo
  name: Geocoding API
  slug: geocoding-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Air Quality APIs API from Open-Meteo — 1 operation(s) for air quality apis.
  name: Open-Meteo Air Quality APIs API
  slug: open-meteo-air-quality-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Climate Change APIs API from Open-Meteo — 1 operation(s) for climate change apis.
  name: Open-Meteo Climate Change APIs API
  slug: open-meteo-climate-change-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Elevation API API from Open-Meteo — 1 operation(s) for elevation api.
  name: Open-Meteo Elevation API API
  slug: open-meteo-elevation-api-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Ensemble Forecast APIs API from Open-Meteo — 1 operation(s) for ensemble forecast apis.
  name: Open-Meteo Ensemble Forecast APIs API
  slug: open-meteo-ensemble-forecast-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Flood APIs API from Open-Meteo — 1 operation(s) for flood apis.
  name: Open-Meteo Flood APIs API
  slug: open-meteo-flood-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Historical Weather APIs API from Open-Meteo — 1 operation(s) for historical weather apis.
  name: Open-Meteo Historical Weather APIs API
  slug: open-meteo-historical-weather-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Marine Weather APIs API from Open-Meteo — 1 operation(s) for marine weather apis.
  name: Open-Meteo Marine Weather APIs API
  slug: open-meteo-marine-weather-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Seasonal Forecast APIs API from Open-Meteo — 1 operation(s) for seasonal forecast apis.
  name: Open-Meteo Seasonal Forecast APIs API
  slug: open-meteo-seasonal-forecast-apis-api
- baseURL: https://api.open-meteo.com
  baseurl_source: declared
  description: The Weather Forecast APIs API from Open-Meteo — 1 operation(s) for weather forecast apis.
  name: Open-Meteo Weather Forecast APIs API
  slug: open-meteo-weather-forecast-apis-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs API
  slug: open-open-meteo-air-quality-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Climate Change APIs API
  slug: open-open-meteo-climate-change-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Elevation API API
  slug: open-open-meteo-elevation-api-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Ensemble Forecast APIs API
  slug: open-open-meteo-ensemble-forecast-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Flood APIs API
  slug: open-open-meteo-flood-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Historical Weather APIs API
  slug: open-open-meteo-historical-weather-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Marine Weather APIs API
  slug: open-open-meteo-marine-weather-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Seasonal Forecast APIs API
  slug: open-open-meteo-seasonal-forecast-apis-api
- collection_type: open
  name: Open-Meteo Air Quality Air Quality APIs Weather Forecast APIs API
  slug: open-open-meteo-weather-forecast-apis-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-meteo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-meteo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open-meteo.com
- group: docs
  title: ''
  type: Documentation
  url: https://open-meteo.com/en/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/open-meteo
- group: company
  title: ''
  type: Blog
  url: https://openmeteo.substack.com
- group: commercial
  title: ''
  type: Pricing
  url: https://open-meteo.com/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.open-meteo.com
- group: other
  title: ''
  type: X
  url: https://x.com/open_meteo
- group: commercial
  title: ''
  type: Plans
  url: plans/open-meteo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-meteo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-meteo-finops.yml
created: '2026-06-13'
description: Open-Meteo is an open-source weather API that provides free global weather forecasts, historical reanalysis data, marine conditions, air quality indexes, and long-range climate projections through a simple REST interface requiring no API key for non-commercial use. The service aggregates data from over 30 weather models provided by 15+ national meteorological services including ECMWF, NOAA GFS, DWD ICON, Météo-France, and JMA, delivering resolutions from 1 km to 11 km updated every 1 to 6 hours. Historical data extends back to 1940 via ERA5 reanalysis, giving developers and researchers access to consistent long-term climate records alongside real-time forecasts. Commercial users who need dedicated server capacity, higher throughput, and access to extended APIs such as ensemble forecasts, seasonal outlooks, satellite radiation, and climate change projections can subscribe to paid plans priced at a flat monthly rate with no per-call overage charges. The entire server infrastructure
  is open-source under the AGPLv3 license and can be self-hosted, while the underlying weather data is released under CC BY 4.0.
examples:
- key_count: 9
  name: Open Meteo Air Quality Example
  slug: open-meteo-air-quality-example
- key_count: 1
  name: Open Meteo Elevation Example
  slug: open-meteo-elevation-example
- key_count: 2
  name: Open Meteo Geocoding Example
  slug: open-meteo-geocoding-example
- key_count: 9
  name: Open Meteo Weather Forecast Example
  slug: open-meteo-weather-forecast-example
finops:
- name: Open Meteo Finops
  service_category: ''
  slug: open-meteo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-meteo.png
json_schemas:
- name: Open-Meteo Air Quality Response
  property_count: 9
  slug: open-meteo-air-quality-response
- name: Open-Meteo Error Response
  property_count: 2
  slug: open-meteo-error-response
- name: Open-Meteo Weather Response
  property_count: 11
  slug: open-meteo-weather-response
jsonld:
- class_count: 10
  name: Open Meteo Context
  property_count: 59
  slug: open-meteo-context
layout: provider
modified: '2026-06-13'
name: Open-Meteo
nav: Providers
network: true
overview: 'Open-Meteo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Air Quality APIs API, Climate Change APIs API, Elevation API API, and 6 more. Tagged areas include Weather, Forecast, Historical Weather, Air Quality, and Marine.


  The Open-Meteo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open-Meteo''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Open Meteo Plans Pricing
  plan_count: 4
  slug: open-meteo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Open Meteo Rate Limits
  slug: open-meteo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Open-Meteo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: open-meteo-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 81.3
    catalog_earned_first_party: 0.0
    catalog_gap: 33.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 55.8
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-meteo/refs/heads/main/screenshots/open-meteo-2026-06-20T190840.png
security:
- kind: domain-security
  name: Open Meteo Domain Security
  slug: open-meteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-meteo
tags:
- Weather
- Forecast
- Historical Weather
- Air Quality
- Marine
- Climate
- Open-Source
- Free
website: https://open-meteo.com
---
