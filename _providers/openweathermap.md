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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Openweathermap Agentic Access
  operation_count: 42
  slug: openweathermap-agentic-access
  summary_line: 42 operations · 9 acting
api_count: 14
apis:
- description: Accumulated temperature and precipitation totals for agriculture.
  name: OpenWeatherMap Accumulated Parameters API
  slug: openweathermap-accumulated-parameters-api
- description: Current, forecast, and historical air pollution data with AQI.
  name: OpenWeatherMap Air Pollution API
  slug: openweathermap-air-pollution-api
- description: Current weather data for any geographic coordinates worldwide.
  name: OpenWeatherMap Current Weather API
  slug: openweathermap-current-weather-api
- description: Weather forecasts at multiple granularities and time horizons.
  name: OpenWeatherMap Forecast API
  slug: openweathermap-forecast-api
- description: Direct and reverse geocoding between location names and coordinates.
  name: OpenWeatherMap Geocoding API
  slug: openweathermap-geocoding-api
- description: Historical weather records by coordinate with hourly granularity.
  name: OpenWeatherMap History API
  slug: openweathermap-history-api
- description: Submit and retrieve aggregated weather station measurements.
  name: OpenWeatherMap Measurements API
  slug: openweathermap-measurements-api
- description: Unified timeline API with current, forecast, and historical weather plus alerts.
  name: OpenWeatherMap One Call API
  slug: openweathermap-one-call-api
- description: Route weather, road surface state, and alerts for a track of waypoints.
  name: OpenWeatherMap Road Risk API
  slug: openweathermap-road-risk-api
- description: Solar irradiance values for clear and cloudy sky models.
  name: OpenWeatherMap Solar Irradiance API
  slug: openweathermap-solar-irradiance-api
- description: Manage modeled locations and solar panel configurations and retrieve power output.
  name: OpenWeatherMap Solar Panels API
  slug: openweathermap-solar-panels-api
- description: Register, retrieve, update, and delete personal weather stations.
  name: OpenWeatherMap Stations API
  slug: openweathermap-stations-api
- description: Long-term statistical weather aggregates for any global location.
  name: OpenWeatherMap Statistical Weather API
  slug: openweathermap-statistical-weather-api
- description: Weather layer tile service for map overlays.
  name: OpenWeatherMap Weather Maps API
  slug: openweathermap-weather-maps-api
arazzos:
- description: Geocode a city name, then fetch current air pollution and its hourly forecast.
  name: OpenWeatherMap Air Quality By City
  slug: openweathermap-air-quality-by-city-workflow
- description: From raw coordinates, gather current weather, One Call current conditions, and air pollution.
  name: OpenWeatherMap Coordinate Weather And Air Snapshot
  slug: openweathermap-coordinate-weather-and-air-snapshot-workflow
- description: Geocode a city, then fetch historical air pollution for a window and the current reading.
  name: OpenWeatherMap Historical Air Pollution Window
  slug: openweathermap-historical-air-pollution-window-workflow
- description: Geocode a city name, then fetch current weather and a five day forecast for it.
  name: OpenWeatherMap Locate And Report Current Weather
  slug: openweathermap-locate-and-report-current-weather-workflow
- description: Geocode a city, then stack hourly, daily, and climatic forecasts for it.
  name: OpenWeatherMap Multi Horizon Forecast
  slug: openweathermap-multi-horizon-forecast-workflow
- description: Turn coordinates into a place name, then fetch current weather and One Call conditions.
  name: OpenWeatherMap Reverse Geocode Weather
  slug: openweathermap-reverse-geocode-weather-workflow
- description: Geocode a city, read its current weather, then fetch a matching weather map tile.
  name: OpenWeatherMap Weather Map Overlay Context
  slug: openweathermap-weather-map-overlay-context-workflow
- description: Resolve a zip or postal code to coordinates, then return five day and sixteen day forecasts.
  name: OpenWeatherMap Zip To Forecast
  slug: openweathermap-zip-to-forecast-workflow
artifact_total: 107
collections:
- collection_type: postman
  name: OpenWeatherMap Accumulated Parameters API
  slug: postman-openweathermap-accumulated-parameters
- collection_type: postman
  name: OpenWeatherMap Air Pollution API
  slug: postman-openweathermap-air-pollution
- collection_type: postman
  name: OpenWeatherMap Current Weather Data API
  slug: postman-openweathermap-current-weather
- collection_type: postman
  name: OpenWeatherMap Forecast APIs
  slug: postman-openweathermap-forecast
- collection_type: postman
  name: OpenWeatherMap Geocoding API
  slug: postman-openweathermap-geocoding
- collection_type: postman
  name: OpenWeatherMap Historical Weather API
  slug: postman-openweathermap-history
- collection_type: postman
  name: OpenWeatherMap One Call API 4.0
  slug: postman-openweathermap-one-call
- collection_type: postman
  name: OpenWeatherMap Road Risk API
  slug: postman-openweathermap-road-risk
- collection_type: postman
  name: OpenWeatherMap Solar Energy APIs
  slug: postman-openweathermap-solar
- collection_type: postman
  name: OpenWeatherMap Statistical Weather API
  slug: postman-openweathermap-statistical-weather
- collection_type: postman
  name: OpenWeatherMap Weather Maps 1.0 API
  slug: postman-openweathermap-weather-maps
- collection_type: postman
  name: OpenWeatherMap Weather Stations API
  slug: postman-openweathermap-weather-stations
- collection_type: open
  name: OpenWeatherMap Accumulated Parameters API
  slug: open-openweathermap-accumulated-parameters
- collection_type: open
  name: OpenWeatherMap Air Pollution API
  slug: open-openweathermap-air-pollution
- collection_type: open
  name: OpenWeatherMap Current Weather Data API
  slug: open-openweathermap-current-weather
- collection_type: open
  name: OpenWeatherMap Forecast APIs
  slug: open-openweathermap-forecast
- collection_type: open
  name: OpenWeatherMap Geocoding API
  slug: open-openweathermap-geocoding
- collection_type: open
  name: OpenWeatherMap Historical Weather API
  slug: open-openweathermap-history
- collection_type: open
  name: OpenWeatherMap One Call API 4.0
  slug: open-openweathermap-one-call
- collection_type: open
  name: OpenWeatherMap Road Risk API
  slug: open-openweathermap-road-risk
- collection_type: open
  name: OpenWeatherMap Solar Energy APIs
  slug: open-openweathermap-solar
- collection_type: open
  name: OpenWeatherMap Statistical Weather API
  slug: open-openweathermap-statistical-weather
- collection_type: open
  name: OpenWeatherMap Weather Maps 1.0 API
  slug: open-openweathermap-weather-maps
- collection_type: open
  name: OpenWeatherMap Weather Stations API
  slug: open-openweathermap-weather-stations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openweathermap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openweathermap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openweathermap-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openweathermap/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-air-quality-by-city-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-coordinate-weather-and-air-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-historical-air-pollution-window-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-locate-and-report-current-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-multi-horizon-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-reverse-geocode-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-weather-map-overlay-context-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openweathermap-zip-to-forecast-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://openweathermap.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openweathermap.org/api
- group: start
  title: ''
  type: GettingStarted
  url: https://openweathermap.org/guide
- group: docs
  title: ''
  type: APIReference
  url: https://openweathermap.org/api
- group: auth
  title: ''
  type: Authentication
  url: https://openweathermap.org/appid
- group: start
  title: ''
  type: Signup
  url: https://home.openweathermap.org/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://home.openweathermap.org/users/sign_in
- group: start
  title: ''
  type: Console
  url: https://dashboard.openweather.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://openweathermap.org/price
- group: commercial
  title: ''
  type: Plans
  url: plans/openweathermap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openweathermap-rate-limits.yml
- group: other
  title: ''
  type: Marketplace
  url: https://openweathermap.org/marketplace
- group: company
  title: ''
  type: Blog
  url: https://openweather.co.uk/blog
- group: operate
  title: ''
  type: FAQ
  url: https://openweathermap.org/faq
- group: operate
  title: ''
  type: Support
  url: https://openweathermap.org/support-centre
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openweather.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openweather.co.uk/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenWeatherMap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openweathermap
- group: design
  title: ''
  type: SpectralRules
  url: rules/openweathermap-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openweathermap-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/openweathermap-context.jsonld
- group: other
  title: ''
  type: KubernetesCRD
  url: ''
- group: build
  title: ''
  type: Tools
  url: ''
- group: build
  title: ''
  type: Packages
  url: packages/openweathermap-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openweathermap-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openweathermap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openweathermap-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/openweathermap-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openweathermap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openweathermap-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openweathermap-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openweathermap-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/openweathermap-components.yml
created: '2026-05-28'
description: OpenWeather (operating openweathermap.org) is a global weather data platform delivering current weather, multi-horizon forecasts, historical archives, climate statistics, air pollution, solar irradiance, road risk, geocoding, and weather map tiles. Data is sourced from satellites, weather models, radars, and a worldwide network of weather stations, served through REST APIs across a freemium, multi-tier, and pay-per-call commercial model.
examples:
- key_count: 3
  name: Accumulated Temperature Example
  slug: accumulated-temperature-example
- key_count: 3
  name: Air Pollution Current Example
  slug: air-pollution-current-example
- key_count: 3
  name: Current Weather Example
  slug: current-weather-example
- key_count: 3
  name: Forecast Five Day Example
  slug: forecast-five-day-example
- key_count: 3
  name: Geocoding Direct Example
  slug: geocoding-direct-example
- key_count: 3
  name: History City Example
  slug: history-city-example
- key_count: 3
  name: One Call Current Example
  slug: one-call-current-example
- key_count: 3
  name: Road Risk Example
  slug: road-risk-example
- key_count: 3
  name: Solar Irradiance Interval Example
  slug: solar-irradiance-interval-example
- key_count: 3
  name: Statistical Month Example
  slug: statistical-month-example
- key_count: 3
  name: Weather Maps Tile Example
  slug: weather-maps-tile-example
- key_count: 3
  name: Weather Stations Create Example
  slug: weather-stations-create-example
features:
- description: Real-time and forecast weather for any latitude/longitude on Earth.
  name: Global Weather Coverage
- description: Over 47 years of historical weather observations available via History, One Call 4.0, and Statistical APIs.
  name: Long-Range Historical Archive
- description: AQI plus eight pollutant concentrations covering current, forecast, and historical air pollution.
  name: Air Quality Telemetry
- description: GHI, DNI, DHI irradiance and per-panel power output predictions for solar projects.
  name: Solar Energy Modeling
- description: Direct integration with Leaflet, OpenLayers, and Google Maps via raster tile layers.
  name: Map Tile Overlays
- description: First 1,000 daily One Call requests free; additional calls billed per call for flexible cost control.
  name: Pay-Per-Call One Call 4.0
- description: Free, Startup, Developer, Professional, Expert, and Enterprise tiers tuned for varying volume and SLA.
  name: Multi-Tier Subscriptions
- description: Register stations, submit measurements, and retrieve aggregated readings.
  name: Personal Weather Stations
- description: Per-waypoint weather and road surface state with severity-tagged alerts for routing.
  name: Road and Route Risk
- description: Forecast and condition text returned in 40 plus languages.
  name: Multi-Lingual Output
finops:
- name: Openweathermap Finops
  service_category: API
  slug: openweathermap-finops
graphqls:
- description: 'This is a conceptual GraphQL schema for the OpenWeatherMap API surface. OpenWeatherMap does not publish a native GraphQL endpoint; this schema is a structured representation of the REST API resources '
  name: OpenWeatherMap GraphQL Schema
  slug: openweathermap-graphql
image: https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png
integrations:
- description: Weather Maps 1.0 tile layers render directly inside Leaflet maps.
  name: Leaflet
- description: Tile layers compatible with OpenLayers raster sources.
  name: OpenLayers
- description: Weather tiles can be added as overlays in Google Maps.
  name: Google Maps
- description: OpenWeather integration is a first-class weather provider in the Home Assistant ecosystem.
  name: Home Assistant
- description: Numerous community Node-RED nodes wrap the OpenWeather APIs.
  name: Node-RED
- description: REST connectors and community templates ingest OpenWeather data for analytics dashboards.
  name: Power BI and Tableau
- description: Multiple community MCP servers (NimbleBrainInc, robertn702, fgladisch, jezweb, SaintDoresh, tristau) expose OpenWeather data to MCP-compatible agents and Claude.
  name: Model Context Protocol Servers
- description: ForecastSkill and OpenWeather API Automation skills add weather capabilities to Claude Code workflows.
  name: Claude Code Skills
json_schemas:
- name: OpenWeatherMap Air Pollution
  property_count: 2
  slug: openweathermap-air-pollution
- name: OpenWeatherMap Current Weather
  property_count: 14
  slug: openweathermap-current-weather
- name: OpenWeatherMap Forecast Item
  property_count: 9
  slug: openweathermap-forecast
- name: OpenWeatherMap Geocoding Result
  property_count: 7
  slug: openweathermap-geocoding
- name: OpenWeatherMap Weather Station
  property_count: 9
  slug: openweathermap-station
json_structures:
- name: Openweathermap Air Pollution Structure
  property_count: 0
  slug: openweathermap-air-pollution-structure
- name: Openweathermap Current Weather Structure
  property_count: 0
  slug: openweathermap-current-weather-structure
- name: Openweathermap Geocoding Structure
  property_count: 0
  slug: openweathermap-geocoding-structure
jsonld:
- class_count: 32
  name: Openweathermap Context
  property_count: 12
  slug: openweathermap-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server (candidate)
  slug: mcp-server-candidate
modified: '2026-06-20'
name: OpenWeatherMap
nav: Providers
network: true
overview: 'OpenWeatherMap publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accumulated Parameters API, Air Pollution API, Current Weather API, and 11 more. Tagged areas include Weather, Forecast, Climate, Air Pollution, and Air Quality.


  The OpenWeatherMap catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  OpenWeatherMap''s developer surface includes authentication, getting-started guide, API reference, signup flow, developer console, pricing, engineering blog, and 37 more developer resources.'
plans:
- name: Openweathermap Plans Pricing
  plan_count: 7
  slug: openweathermap-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 12
  name: Openweathermap Rate Limits
  slug: openweathermap-rate-limits
rules:
- name: OpenWeatherMap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openweathermap-jsonschema-spectral-rules
- name: OpenWeatherMap API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 10
  slug: openweathermap-rules
score:
  band: exemplar
  composite: 73.5
  delta: 4.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 78.3
    developer_ergonomics: 63.0
    discoverability: 92.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 68.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openweathermap/refs/heads/main/screenshots/openweathermap-2026-06-20T191055.png
security:
- kind: authentication
  name: Openweathermap Authentication
  slug: openweathermap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openweathermap Domain Security
  slug: openweathermap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openweathermap
solutions:
- description: OpenWeather's geospatial platform for working with weather grids and time series.
  name: VANE Geospatial Platform
- description: OpenWeather's open-source multidimensional array storage engine used internally for weather time series.
  name: Deker Storage Engine
- description: Bulk history, forecast, solar, and tile downloads for analytics and ML pipelines.
  name: Marketplace Bulk Data
- description: Contractual SLAs with dedicated account management and data residency options.
  name: Enterprise SLAs
tags:
- Weather
- Forecast
- Climate
- Air Pollution
- Air Quality
- Solar
- Geocoding
- History
- Maps
- Road Risk
- Public APIs
use_cases:
- description: Power mobile and web weather apps with current, forecast, and alert data.
  name: Consumer Weather Apps
- description: Use Road Risk and forecast data to optimize fleet routing and arrival times.
  name: Logistics and Routing
- description: Forecast solar generation and demand with solar irradiance and panel energy prediction APIs.
  name: Energy and Utilities
- description: Use accumulated temperature and precipitation data to inform irrigation, planting, and harvest decisions.
  name: Agriculture
- description: Combine historical and statistical weather with air quality and road risk to underwrite and adjudicate claims.
  name: Insurance and Risk
- description: Surface AQI and pollutant concentrations in civic dashboards and citizen notification systems.
  name: Smart City and Air Quality
- description: Embed weather data in trip planning, ski resort, sailing, and outdoor recreation experiences.
  name: Outdoor and Travel
- description: Use high-frequency forecast and wind data for flight planning and marine operations.
  name: Aviation and Maritime
website: https://openweathermap.org/
---
