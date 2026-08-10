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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Air Quality Programmatic Apis Agentic Access
  operation_count: 6
  slug: air-quality-programmatic-apis-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: The Air Quality Programmatic APIs Real Time Air Quality Tile API API from Air Quality Programmatic APIs — 1 operation(s) for air quality programmatic apis real time air quality tile api.
  name: Air Quality Programmatic APIs Air Quality Programmatic APIs Real Time Air Quality Tile API API
  slug: air-quality-programmatic-apis-air-quality-programmatic-apis-real-time-air-quality-tile-api-api
- description: The Cities API from Air Quality Programmatic APIs — 1 operation(s) for cities.
  name: Air Quality Programmatic APIs Cities API
  slug: air-quality-programmatic-apis-cities-api
- description: The Geolocation API from Air Quality Programmatic APIs — 2 operation(s) for geolocation.
  name: Air Quality Programmatic APIs Geolocation API
  slug: air-quality-programmatic-apis-geolocation-api
- description: The Map API from Air Quality Programmatic APIs — 1 operation(s) for map.
  name: Air Quality Programmatic APIs Map API
  slug: air-quality-programmatic-apis-map-api
- description: The Search API from Air Quality Programmatic APIs — 1 operation(s) for search.
  name: Air Quality Programmatic APIs Search API
  slug: air-quality-programmatic-apis-search-api
- description: The Stations API from Air Quality Programmatic APIs — 5 operation(s) for stations.
  name: Air Quality Programmatic APIs Stations API
  slug: air-quality-programmatic-apis-stations-api
artifact_total: 57
collections:
- collection_type: open
  name: Air Quality Programmatic APIs Real-time Air Quality Tile API
  slug: open-air-quality-programmatic-apis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/air-quality-programmatic-apis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/air-quality-programmatic-apis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/air-quality-programmatic-apis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USEPA
- group: operate
  title: ''
  type: FAQ
  url: https://aqicn.org/faq/
- group: auth
  title: ''
  type: Authentication
  url: https://aqicn.org/data-platform/token/
- group: start
  title: ''
  type: Portal
  url: https://aqicn.org/map/
- group: start
  title: ''
  type: Portal
  url: https://aqicn.org/data-platform/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aqicn.org/api/tos/
- group: design
  title: ''
  type: SpectralRules
  url: rules/aqicn-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aqicn-vocabulary.yaml
created: '2024-11-07'
description: Air Quality Programmatic APIs provide real-time and forecast air quality data from 11,000+ monitoring stations in 1,000+ cities worldwide. APIs deliver Air Quality Index (AQI) measurements for PM2.5, PM10, NO2, CO, SO2, and ozone pollutants. Provided by AQICN (World Air Quality Index project) in partnership with the US EPA and global environmental agencies. Data is available via JSON API and map tile API for visualization.
examples:
- key_count: 2
  name: Aqicn Aqi Station Example
  slug: aqicn-aqi-station-example
- key_count: 2
  name: Aqicn Attribution Example
  slug: aqicn-attribution-example
- key_count: 3
  name: Aqicn City Info Example
  slug: aqicn-city-info-example
- key_count: 1
  name: Aqicn Forecast Data Example
  slug: aqicn-forecast-data-example
- key_count: 4
  name: Aqicn Forecast Day Example
  slug: aqicn-forecast-day-example
- key_count: 4
  name: Aqicn Pollutant Data Example
  slug: aqicn-pollutant-data-example
- key_count: 4
  name: Aqicn Station Data Example
  slug: aqicn-station-data-example
- key_count: 2
  name: Aqicn Station Search Result Example
  slug: aqicn-station-search-result-example
- key_count: 3
  name: Aqicn Time Info Example
  slug: aqicn-time-info-example
features:
- description: Live air quality index readings from 11,000+ monitoring stations updated continuously.
  name: Real-Time AQI Data
- description: Data from 1,000+ cities worldwide including US EPA, China MEP, Europe EEA, and other monitoring networks.
  name: Global Coverage
- description: Pollutant-specific AQI for PM2.5, PM10, nitrogen dioxide, carbon monoxide, sulfur dioxide, and ozone.
  name: Multi-Pollutant Data
- description: 3-8 day air quality forecasts for major monitoring stations.
  name: Air Quality Forecasts
- description: Find nearest stations by latitude/longitude, city name, or IP-based geolocation.
  name: Geolocation Queries
- description: Raster map tiles for overlaying real-time AQI data on web maps (Leaflet, Google Maps, etc.).
  name: Map Tile API
- description: Search and discover monitoring stations by name or location within a geographic boundary.
  name: Station Search
- description: Current weather conditions co-located with air quality measurements.
  name: Weather Data
finops:
- name: Air Quality Programmatic Apis Finops
  service_category: API
  slug: air-quality-programmatic-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/air-quality-programmatic-apis.png
json_schemas:
- name: AQIStation
  property_count: 2
  slug: aqicn-aqi-station
- name: Attribution
  property_count: 2
  slug: aqicn-attribution
- name: CityInfo
  property_count: 3
  slug: aqicn-city-info
- name: ForecastData
  property_count: 1
  slug: aqicn-forecast-data
- name: ForecastDay
  property_count: 4
  slug: aqicn-forecast-day
- name: PollutantData
  property_count: 6
  slug: aqicn-pollutant-data
- name: StationData
  property_count: 7
  slug: aqicn-station-data
- name: StationSearchResult
  property_count: 2
  slug: aqicn-station-search-result
- name: TimeInfo
  property_count: 3
  slug: aqicn-time-info
json_structures:
- name: Aqicn Aqi Station Structure
  property_count: 2
  slug: aqicn-aqi-station-structure
- name: Aqicn Attribution Structure
  property_count: 2
  slug: aqicn-attribution-structure
- name: Aqicn City Info Structure
  property_count: 3
  slug: aqicn-city-info-structure
- name: Aqicn Forecast Data Structure
  property_count: 1
  slug: aqicn-forecast-data-structure
- name: Aqicn Forecast Day Structure
  property_count: 4
  slug: aqicn-forecast-day-structure
- name: Aqicn Pollutant Data Structure
  property_count: 6
  slug: aqicn-pollutant-data-structure
- name: Aqicn Station Data Structure
  property_count: 7
  slug: aqicn-station-data-structure
- name: Aqicn Station Search Result Structure
  property_count: 2
  slug: aqicn-station-search-result-structure
- name: Aqicn Time Info Structure
  property_count: 3
  slug: aqicn-time-info-structure
jsonld:
- class_count: 11
  name: Aqicn Context
  property_count: 24
  slug: aqicn-context
layout: provider
modified: '2026-05-19'
name: Air Quality Programmatic APIs
nav: Providers
network: true
overview: 'Air Quality Programmatic APIs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Air Quality Programmatic APIs Real Time Air Quality Tile API API, Cities API, Geolocation API, and 3 more. Tagged areas include Air Quality, Environment, EPA, Open Data, and Public Health.


  The Air Quality Programmatic APIs catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Air Quality Programmatic APIs'' developer surface includes authentication, FAQ, developer portal, and 8 more developer resources.'
plans:
- name: Air Quality Programmatic Apis Plans Pricing
  plan_count: 3
  slug: air-quality-programmatic-apis-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Air Quality Programmatic Apis Rate Limits
  slug: air-quality-programmatic-apis-rate-limits
rules:
- name: Air Quality Programmatic APIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: air-quality-programmatic-apis-jsonschema-spectral-rules
- name: Air Quality Programmatic APIs API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: air-quality-programmatic-apis-spectral-rules
- name: Air Quality Programmatic APIs API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: aqicn-spectral-rules
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.8
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/air-quality-programmatic-apis/refs/heads/main/screenshots/air-quality-programmatic-apis-2026-06-20T171420.png
security:
- kind: authentication
  name: Air Quality Programmatic Apis Authentication
  slug: air-quality-programmatic-apis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Air Quality Programmatic Apis Domain Security
  slug: air-quality-programmatic-apis-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: air-quality-programmatic-apis
tags:
- Air Quality
- Environment
- EPA
- Open Data
- Public Health
- IoT
- Government Data
- Real-Time Data
use_cases:
- description: Build apps that show users real-time air quality for their location with health recommendations.
  name: Air Quality Mobile Apps
- description: Create web dashboards visualizing air quality trends across cities and regions.
  name: Environmental Monitoring Dashboards
- description: Access historical and real-time air quality data for epidemiological and public health research.
  name: Public Health Research
- description: Integrate air quality data into smart city platforms and IoT systems for environmental management.
  name: Smart City Integration
- description: Provide air quality-based recommendations for outdoor activities in fitness and weather apps.
  name: Outdoor Activity Planning
website: https://aqicn.org/map/
---
