---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Noaa Agentic Access
  operation_count: 86
  slug: noaa-agentic-access
  summary_line: 86 operations
api_count: 17
apis:
- description: The NOAA Climate Data Online Web Services API v2 provides RESTful access to the CDO database of historical weather and climate data maintained by the National Centers for Environmental Information (NC
  name: Climate Data Online (CDO) API
  slug: climate-data-online-cdo-api
- description: The NOAA Center for Operational Oceanographic Products and Services (CO-OPS) Data Retrieval API provides access to water levels, tide predictions, currents, and meteorological observations from hundre
  name: CO-OPS Tides and Currents API
  slug: co-ops-tides-and-currents-api
- description: The Alerts API from NOAA — 8 operation(s) for alerts.
  name: NOAA Alerts API
  slug: noaa-alerts-api
- description: The Aviation API from NOAA — 7 operation(s) for aviation.
  name: NOAA Aviation API
  slug: noaa-aviation-api
- description: The Glossary API from NOAA — 1 operation(s) for glossary.
  name: NOAA Glossary API
  slug: noaa-glossary-api
- description: The Gridpoints API from NOAA — 4 operation(s) for gridpoints.
  name: NOAA Gridpoints API
  slug: noaa-gridpoints-api
- description: The Icons API from NOAA — 3 operation(s) for icons.
  name: NOAA Icons API
  slug: noaa-icons-api
- description: Decoded navigational information
  name: NOAA Navigational Data API
  slug: noaa-navigational-data-api
- description: The Offices API from NOAA — 8 operation(s) for offices.
  name: NOAA Offices API
  slug: noaa-offices-api
- description: The Points API from NOAA — 3 operation(s) for points.
  name: NOAA Points API
  slug: noaa-points-api
- description: The Products API from NOAA — 9 operation(s) for products.
  name: NOAA Products API
  slug: noaa-products-api
- description: The Radar API from NOAA — 8 operation(s) for radar.
  name: NOAA Radar API
  slug: noaa-radar-api
- description: The Radio API from NOAA — 1 operation(s) for radio.
  name: NOAA Radio API
  slug: noaa-radio-api
- description: The Stations API from NOAA — 7 operation(s) for stations.
  name: NOAA Stations API
  slug: noaa-stations-api
- description: The Thumbnails API from NOAA — 1 operation(s) for thumbnails.
  name: NOAA Thumbnails API
  slug: noaa-thumbnails-api
- description: Decoded weather information
  name: NOAA Weather Data API
  slug: noaa-weather-data-api
- description: The Zones API from NOAA — 6 operation(s) for zones.
  name: NOAA Zones API
  slug: noaa-zones-api
artifact_total: 38
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noaa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noaa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noaa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.noaa.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.weather.gov/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/NOAAGov
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/weather-gov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/noaa
- group: company
  title: ''
  type: Blog
  url: https://www.noaa.gov/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weather.gov/documentation/services-web-api
- group: operate
  title: ''
  type: StatusPage
  url: https://www.weather.gov/im/tecnews
- group: other
  title: ''
  type: X
  url: https://x.com/NWS
- group: commercial
  title: ''
  type: Plans
  url: plans/noaa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/noaa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/noaa-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/noaa-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/noaa-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/noaa-coops-tides-example.json
created: '2026-06-12'
description: The National Oceanic and Atmospheric Administration (NOAA) provides a suite of publicly accessible REST APIs delivering weather observations, forecasts, alerts, climate data, ocean conditions, and historical environmental records from the US federal government. The National Weather Service API (api.weather.gov) offers real-time forecasts, active alerts, radar data, and observations across the continental United States and territories. NOAA also publishes the Climate Data Online (CDO) API for access to historical climate and weather datasets, the CO-OPS Tides and Currents API for water level and oceanographic data, and the Aviation Weather API for aeronautical weather products. All NOAA APIs are free to use as open government data with no licensing restrictions.
examples:
- key_count: 2
  name: Noaa Aviation Metar Example
  slug: noaa-aviation-metar-example
- key_count: 2
  name: Noaa Coops Tides Example
  slug: noaa-coops-tides-example
- key_count: 4
  name: Noaa Nws Alert Example
  slug: noaa-nws-alert-example
- key_count: 3
  name: Noaa Nws Gridpoint Forecast Example
  slug: noaa-nws-gridpoint-forecast-example
finops:
- name: Noaa Finops
  service_category: ''
  slug: noaa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/noaa.png
json_schemas:
- name: AirSigmetJSON
  property_count: 0
  slug: noaa-aviation-airsigmetjson
- name: METARJSON
  property_count: 0
  slug: noaa-aviation-metarjson
- name: PIREPtext
  property_count: 0
  slug: noaa-aviation-pireptext
- name: TAFJSON
  property_count: 0
  slug: noaa-aviation-tafjson
- name: Alert
  property_count: 30
  slug: noaa-nws-alert
- name: AlertCollection
  property_count: 3
  slug: noaa-nws-alertcollection
- name: Observation
  property_count: 30
  slug: noaa-nws-observation
- name: Point
  property_count: 22
  slug: noaa-nws-point
- name: Zone
  property_count: 18
  slug: noaa-nws-zone
jsonld:
- class_count: 22
  name: Noaa Context
  property_count: 98
  slug: noaa-context
layout: provider
modified: '2026-06-12'
name: NOAA
nav: Providers
network: true
overview: 'NOAA publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Aviation API, Glossary API, and 12 more. Tagged areas include Weather, Climate, Forecast, Alerts, and Ocean.


  The NOAA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NOAA''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, and 13 more developer resources.'
plans:
- name: Noaa Plans Pricing
  plan_count: 1
  slug: noaa-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Noaa Rate Limits
  slug: noaa-rate-limits
rules:
- name: NOAA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: noaa-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noaa/refs/heads/main/screenshots/noaa-2026-06-20T190339.png
security:
- kind: authentication
  name: Noaa Authentication
  slug: noaa-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Noaa Domain Security
  slug: noaa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: noaa
tags:
- Weather
- Climate
- Forecast
- Alerts
- Ocean
- Tides
- Aviation Weather
- Government
- Open Data
- Environmental
website: https://www.noaa.gov
---
