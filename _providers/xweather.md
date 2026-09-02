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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xweather Agentic Access
  operation_count: 10
  slug: xweather-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: Air quality index and pollutant data
  name: Xweather Air Quality API
  slug: xweather-air-quality-api
- description: Severe weather alerts and warnings
  name: Xweather Alerts API
  slug: xweather-alerts-api
- description: Current and historical weather conditions
  name: Xweather Conditions API
  slug: xweather-conditions-api
- description: Wildfire data
  name: Xweather Fires API
  slug: xweather-fires-api
- description: Weather forecasts
  name: Xweather Forecasts API
  slug: xweather-forecasts-api
- description: Lightning strike data and nowcasts
  name: Xweather Lightning API
  slug: xweather-lightning-api
- description: Marine and ocean weather data
  name: Xweather Maritime API
  slug: xweather-maritime-api
- description: Weather station observations
  name: Xweather Observations API
  slug: xweather-observations-api
- description: Tropical cyclone and hurricane data
  name: Xweather Tropical API
  slug: xweather-tropical-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xweather Weather Air Quality API
  slug: open-xweather-air-quality-api
- collection_type: open
  name: Xweather Weather Air Quality Alerts API
  slug: open-xweather-alerts-api
- collection_type: open
  name: Xweather Weather Air Quality Conditions API
  slug: open-xweather-conditions-api
- collection_type: open
  name: Xweather Weather Air Quality Fires API
  slug: open-xweather-fires-api
- collection_type: open
  name: Xweather Weather Air Quality Forecasts API
  slug: open-xweather-forecasts-api
- collection_type: open
  name: Xweather Weather Air Quality Lightning API
  slug: open-xweather-lightning-api
- collection_type: open
  name: Xweather Weather Air Quality Maritime API
  slug: open-xweather-maritime-api
- collection_type: open
  name: Xweather Weather Air Quality Observations API
  slug: open-xweather-observations-api
- collection_type: open
  name: Xweather Weather Air Quality Tropical API
  slug: open-xweather-tropical-api
- collection_type: open
  name: Xweather Weather API
  slug: open-xweather-weather-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xweather-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xweather-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xweather-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vaisala-xweather
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xweather
- group: company
  title: ''
  type: Website
  url: https://xweather.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.xweather.com/docs/weather-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.xweather.com/docs/weather-api/endpoints
- group: auth
  title: ''
  type: Authentication
  url: https://www.xweather.com/docs/weather-api/getting-started/authentication
- group: start
  title: ''
  type: Signup
  url: https://www.xweather.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xweather.com/weather-api
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/openapi/xweather-weather-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-conditions-observation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-forecast-period-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-alert-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-lightning-strike-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-schema/xweather-air-quality-observation-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-structure/xweather-weather-api-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/json-ld/xweather-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/vocabulary/xweather-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/rules/xweather-rules.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-conditions-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-forecasts-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-alerts-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-lightning-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-air-quality-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-list-tropical-cyclones-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/examples/xweather-get-maritime-example.json
created: '2024-11-08'
description: Xweather, a Vaisala company, provides weather data APIs delivering science-backed, hyper-local weather intelligence for operational applications. The Xweather Weather API exposes current conditions, forecasts, severe weather alerts, lightning data, air quality, observations, wildfire information, tropical cyclone tracks, and maritime weather through a single REST API. Authentication uses a client_id and client_secret passed as query parameters or HTTP headers.
examples:
- key_count: 3
  name: Xweather Get Air Quality Example
  slug: xweather-get-air-quality-example
- key_count: 3
  name: Xweather Get Alerts Example
  slug: xweather-get-alerts-example
- key_count: 3
  name: Xweather Get Conditions Example
  slug: xweather-get-conditions-example
- key_count: 3
  name: Xweather Get Forecasts Example
  slug: xweather-get-forecasts-example
- key_count: 3
  name: Xweather Get Lightning Example
  slug: xweather-get-lightning-example
- key_count: 3
  name: Xweather Get Maritime Example
  slug: xweather-get-maritime-example
- key_count: 3
  name: Xweather List Tropical Cyclones Example
  slug: xweather-list-tropical-cyclones-example
features:
- description: Current surface weather observations for any location worldwide.
  name: Real-Time Conditions
- description: Forecast records out to 15 days with hourly and daily granularity.
  name: Hourly and Daily Forecasts
- description: Government-issued alerts, watches, and warnings with severity, urgency, and certainty.
  name: Severe Weather Alerts
- description: Cloud-to-ground and in-cloud lightning strike data from Vaisala's global detection network.
  name: Global Lightning Network
- description: Probabilistic short-term lightning threat used to drive stop-work and all-clear automation.
  name: Lightning Threat Nowcast
- description: AQI values, primary pollutant, and detailed pollutant breakdowns for monitoring and reporting.
  name: Air Quality
- description: Marine weather including waves, swell, sea-surface temperature, and sea state.
  name: Maritime Weather
- description: Active wildfire incident records and perimeters for situational awareness.
  name: Wildfire Data
- description: Active tropical cyclone tracks, intensity, and forecast cones.
  name: Tropical Cyclones
finops:
- name: Xweather Finops
  service_category: API
  slug: xweather-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xweather.png
integrations:
- description: Tile and overlay services for visualizing Xweather data on web and mobile maps.
  name: AerisWeather Mapping
- description: Underlying global lightning detection infrastructure feeding the Xweather lightning APIs.
  name: Vaisala Lightning Network
- description: Severe-weather alert payloads align with CAP severity, urgency, and certainty fields.
  name: Common Alerting Protocol
- description: Surface observations are derived from the international METAR observation standard.
  name: METAR
json_schemas:
- name: AirQualityObservation
  property_count: 5
  slug: xweather-air-quality-observation
- name: AirQualityResponse
  property_count: 0
  slug: xweather-air-quality-response
- name: Alert
  property_count: 6
  slug: xweather-alert
- name: AlertsResponse
  property_count: 0
  slug: xweather-alerts-response
- name: ConditionsObservation
  property_count: 26
  slug: xweather-conditions-observation
- name: ConditionsRecord
  property_count: 7
  slug: xweather-conditions-record
- name: ConditionsResponse
  property_count: 0
  slug: xweather-conditions-response
- name: FiresResponse
  property_count: 0
  slug: xweather-fires-response
- name: ForecastPeriod
  property_count: 20
  slug: xweather-forecast-period
- name: ForecastsResponse
  property_count: 0
  slug: xweather-forecasts-response
- name: LightningResponse
  property_count: 0
  slug: xweather-lightning-response
- name: LightningStrike
  property_count: 9
  slug: xweather-lightning-strike
- name: LightningThreatsResponse
  property_count: 0
  slug: xweather-lightning-threats-response
- name: Location
  property_count: 11
  slug: xweather-location
- name: MaritimeResponse
  property_count: 0
  slug: xweather-maritime-response
- name: ObservationsResponse
  property_count: 0
  slug: xweather-observations-response
- name: TropicalCyclonesResponse
  property_count: 0
  slug: xweather-tropical-cyclones-response
json_structures:
- name: Xweather Weather Api Structure
  property_count: 3
  slug: xweather-weather-api-structure
jsonld:
- class_count: 0
  name: Xweather Context
  property_count: 66
  slug: xweather-context
layout: provider
modified: '2026-05-19'
name: Xweather
nav: Providers
network: true
overview: 'Xweather publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Air Quality API, Alerts API, Conditions API, and 6 more. Tagged areas include Air Quality, Company, Data, Forecast, and Lightning.


  The Xweather catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Xweather''s developer surface includes authentication, documentation, API reference, signup flow, pricing, code examples, and 23 more developer resources.'
plans:
- name: Xweather Plans Pricing
  plan_count: 3
  slug: xweather-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Xweather Rate Limits
  slug: xweather-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Xweather API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: xweather-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Xweather API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 6
  slug: xweather-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 67.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xweather/refs/heads/main/screenshots/xweather-2026-06-20T201723.png
security:
- kind: authentication
  name: Xweather Authentication
  slug: xweather-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Xweather Domain Security
  slug: xweather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xweather
tags:
- Air Quality
- Company
- Data
- Forecast
- Lightning
- Maritime
- Observations
- Severe Weather
- Weather
use_cases:
- description: Automatically pause and resume outdoor construction work using lightning threat nowcasts.
  name: Construction Lightning Safety
- description: Drive ramp closures and re-openings around lightning, severe weather, and visibility thresholds.
  name: Aviation Ground Operations
- description: Manage stadium and event evacuations and re-entries based on lightning and severe weather.
  name: Outdoor Sports and Events
- description: Plan grid operations, crew dispatch, and storm restoration around forecasts and alerts.
  name: Energy and Utilities
- description: Optimize routing and dispatch decisions using maritime, road weather, and severe weather feeds.
  name: Logistics and Routing
- description: Use historical and real-time storm and lightning data for claims and underwriting.
  name: Insurance and Risk
- description: Aggregate AQI and pollutant feeds for ESG and regulatory reporting.
  name: Environmental Reporting
website: https://xweather.com
---
