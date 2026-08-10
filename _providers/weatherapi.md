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
- acting_count: 1
  human_in_the_loop: 0
  name: Weatherapi Agentic Access
  operation_count: 12
  slug: weatherapi-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 7
apis:
- description: Government weather alerts
  name: WeatherAPI Alerts API
  slug: weatherapi-alerts-api
- description: Long-range future weather (14–300 days)
  name: WeatherAPI Future API
  slug: weatherapi-future-api
- description: Location, IP lookup, timezone, astronomy
  name: WeatherAPI Geo API
  slug: weatherapi-geo-api
- description: Historical weather data
  name: WeatherAPI History API
  slug: weatherapi-history-api
- description: Marine and sailing weather
  name: WeatherAPI Marine API
  slug: weatherapi-marine-api
- description: Upcoming sports events
  name: WeatherAPI Sports API
  slug: weatherapi-sports-api
- description: Real-time and forecast weather endpoints
  name: WeatherAPI Weather API
  slug: weatherapi-weather-api
arazzos:
- description: Resolve a location, then fetch current and forecast weather with air quality and pollen enabled.
  name: WeatherAPI Current and Forecast Air Quality
  slug: weatherapi-air-quality-workflow
- description: Retrieve current weather for many locations in a single bulk request.
  name: WeatherAPI Bulk Current Weather
  slug: weatherapi-bulk-current-weather-workflow
- description: Resolve a location, pull a multi-day forecast, then enrich it with astronomy for the same date.
  name: WeatherAPI Forecast with Astronomy
  slug: weatherapi-forecast-with-astronomy-workflow
- description: Resolve a location, then fetch the long-range future forecast for a date 14-300 days out.
  name: WeatherAPI Future Weather
  slug: weatherapi-future-weather-workflow
- description: Resolve a location, then fetch historical weather for a past date.
  name: WeatherAPI Historical Weather
  slug: weatherapi-historical-weather-workflow
- description: Geolocate an IP address, then fetch current weather and a forecast for that point.
  name: WeatherAPI IP Geolocated Weather
  slug: weatherapi-ip-geolocated-weather-workflow
- description: Resolve a coastal location, then fetch its marine and tide forecast.
  name: WeatherAPI Marine Forecast
  slug: weatherapi-marine-forecast-workflow
- description: Resolve a location with autocomplete search, then fetch sun and moon data for a date.
  name: WeatherAPI Search to Astronomy
  slug: weatherapi-search-to-astronomy-workflow
- description: Resolve a location with autocomplete search, then fetch its current weather.
  name: WeatherAPI Search to Current Weather
  slug: weatherapi-search-to-current-workflow
- description: Resolve a location, list its upcoming sports events, then fetch current weather context.
  name: WeatherAPI Sports Events with Weather
  slug: weatherapi-sports-events-weather-workflow
- description: Resolve a location, read its timezone and local time, then fetch current weather.
  name: WeatherAPI Timezone and Local Conditions
  slug: weatherapi-timezone-localtime-workflow
- description: Build a full travel briefing for a destination — current, forecast, astronomy, and alerts.
  name: WeatherAPI Travel Briefing
  slug: weatherapi-travel-briefing-workflow
- description: Resolve a location, probe its forecast for alerts, then branch to pull full alert detail.
  name: WeatherAPI Weather Alerts Check
  slug: weatherapi-weather-alerts-workflow
artifact_total: 144
collections:
- collection_type: postman
  name: WeatherAPI.com
  slug: postman-weatherapi-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weatherapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weatherapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weatherapi-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/weatherapi/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-air-quality-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-bulk-current-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-forecast-with-astronomy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-future-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-historical-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-ip-geolocated-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-marine-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-search-to-astronomy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-search-to-current-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-sports-events-weather-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-timezone-localtime-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-travel-briefing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/weatherapi-weather-alerts-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.weatherapi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.weatherapi.com/docs/
- group: start
  title: ''
  type: Portal
  url: https://www.weatherapi.com/my/
- group: start
  title: ''
  type: Signup
  url: https://www.weatherapi.com/signup.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weatherapi.com/pricing.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weatherapi.com/terms.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weatherapi.com/privacy.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.weatherapi.com/contact.aspx
- group: company
  title: ''
  type: Blog
  url: https://blog.weatherapi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weatherapicom
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: MCP Server (Official)
  type: Tools
  url: https://github.com/weatherapicom/weatherapi-mcp
- group: build
  title: weatherapi-mcp on npm
  type: Tools
  url: https://www.npmjs.com/package/weatherapi-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/weatherapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weatherapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weatherapi-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/weatherapi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weatherapi-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/weatherapi-context.jsonld
created: '2026-05-28'
description: WeatherAPI.com provides real-time, forecast, historical, marine, future, astronomy, air quality, pollen, sports, IP lookup, time zone, and geolocation data via a JSON/XML REST API. Trusted by 850,000+ developers worldwide with an average ~200ms response time.
examples:
- key_count: 8
  name: Weatherapi Air Quality Example
  slug: weatherapi-air-quality-example
- key_count: 13
  name: Weatherapi Alert Example
  slug: weatherapi-alert-example
- key_count: 2
  name: Weatherapi Alerts Response Example
  slug: weatherapi-alerts-response-example
- key_count: 8
  name: Weatherapi Astro Element Example
  slug: weatherapi-astro-element-example
- key_count: 2
  name: Weatherapi Astronomy Response Example
  slug: weatherapi-astronomy-response-example
- key_count: 2
  name: Weatherapi Bulk Location Example
  slug: weatherapi-bulk-location-example
- key_count: 1
  name: Weatherapi Bulk Request Example
  slug: weatherapi-bulk-request-example
- key_count: 1
  name: Weatherapi Bulk Response Example
  slug: weatherapi-bulk-response-example
- key_count: 3
  name: Weatherapi Condition Example
  slug: weatherapi-condition-example
- key_count: 33
  name: Weatherapi Current Weather Example
  slug: weatherapi-current-weather-example
- key_count: 2
  name: Weatherapi Current Weather Response Example
  slug: weatherapi-current-weather-response-example
- key_count: 5
  name: Weatherapi Forecast Day Entry Example
  slug: weatherapi-forecast-day-entry-example
- key_count: 21
  name: Weatherapi Forecast Day Example
  slug: weatherapi-forecast-day-example
- key_count: 4
  name: Weatherapi Forecast Weather Response Example
  slug: weatherapi-forecast-weather-response-example
- key_count: 39
  name: Weatherapi Hour Forecast Example
  slug: weatherapi-hour-forecast-example
- key_count: 15
  name: Weatherapi Ip Lookup Response Example
  slug: weatherapi-ip-lookup-response-example
- key_count: 8
  name: Weatherapi Location Example
  slug: weatherapi-location-example
- key_count: 6
  name: Weatherapi Marine Forecast Day Example
  slug: weatherapi-marine-forecast-day-example
- key_count: 8
  name: Weatherapi Marine Hour Example
  slug: weatherapi-marine-hour-example
- key_count: 2
  name: Weatherapi Marine Weather Response Example
  slug: weatherapi-marine-weather-response-example
- key_count: 7
  name: Weatherapi Pollen Example
  slug: weatherapi-pollen-example
- key_count: 7
  name: Weatherapi Search Location Example
  slug: weatherapi-search-location-example
- key_count: 6
  name: Weatherapi Sport Event Example
  slug: weatherapi-sport-event-example
- key_count: 3
  name: Weatherapi Sports Response Example
  slug: weatherapi-sports-response-example
- key_count: 3
  name: Weatherapi Tide Example
  slug: weatherapi-tide-example
- key_count: 1
  name: Weatherapi Timezone Response Example
  slug: weatherapi-timezone-response-example
features:
- description: Current conditions refreshed every 10–15 minutes for any global location.
  name: Real-time Weather
- description: Daily and hourly forecast covering up to 14 days ahead (15-minute interval on Enterprise).
  name: 14-Day Forecast
- description: Past weather data from January 1, 2010 onwards.
  name: Historical Weather
- description: Long-range forecasts from 14 to 300 days ahead (Pro+ and above).
  name: Future Weather
- description: Wave height, swell direction, and tide tables for coastal and ocean locations.
  name: Marine Weather
- description: Sunrise, sunset, moonrise, moonset, moon phase, and illumination.
  name: Astronomy
- description: US EPA and UK DEFRA indices plus pollen data with current and forecast endpoints.
  name: Air Quality and Pollen
- description: Government-issued warnings worldwide (USA, UK, Europe, and global).
  name: Weather Alerts
- description: Upcoming football, cricket, and golf events tied to a location.
  name: Sports Events
- description: Location search/autocomplete, IP lookup, and time zone resolution.
  name: Geo Services
- description: POST /current.json#bulk accepts up to 50 locations per call (Pro+ and above).
  name: Bulk Requests
- description: Condition descriptions in 40+ languages via the `lang` parameter.
  name: Multilingual Conditions
- description: Every endpoint supports `.json` and `.xml` response variants.
  name: JSON and XML Responses
- description: Drop-in Model Context Protocol server for Claude Desktop, Cursor, and other agents.
  name: Official MCP Server
finops:
- name: Weatherapi Finops
  service_category: Weather Data & Geolocation
  slug: weatherapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weatherapi.png
integrations:
- description: Drop-in MCP server (weatherapi-mcp) registered in claude_desktop_config.json.
  name: Claude Desktop
- description: MCP integration via .cursor/mcp.json.
  name: Cursor
- description: OpenAPI spec carries `x-microcks-operation` extensions for one-command mocking.
  name: Microcks
- description: Spec is also published on SwaggerHub under WeatherAPI.com / WeatherAPI.
  name: SwaggerHub
- description: Sibling product providing AI-summarised weather narrative.
  name: WeatherAI.io
- description: Sibling product for air-quality analytics.
  name: Miing.com
- description: Sibling product for solar forecasting.
  name: Azuce.com
json_schemas:
- name: AirQuality
  property_count: 8
  slug: weatherapi-air-quality
- name: Alert
  property_count: 13
  slug: weatherapi-alert
- name: AlertsResponse
  property_count: 2
  slug: weatherapi-alerts-response
- name: AstroElement
  property_count: 8
  slug: weatherapi-astro-element
- name: AstronomyResponse
  property_count: 2
  slug: weatherapi-astronomy-response
- name: BulkLocation
  property_count: 2
  slug: weatherapi-bulk-location
- name: BulkRequest
  property_count: 1
  slug: weatherapi-bulk-request
- name: BulkResponse
  property_count: 1
  slug: weatherapi-bulk-response
- name: Condition
  property_count: 3
  slug: weatherapi-condition
- name: CurrentWeatherResponse
  property_count: 2
  slug: weatherapi-current-weather-response
- name: CurrentWeather
  property_count: 33
  slug: weatherapi-current-weather
- name: ForecastDayEntry
  property_count: 5
  slug: weatherapi-forecast-day-entry
- name: ForecastDay
  property_count: 21
  slug: weatherapi-forecast-day
- name: ForecastWeatherResponse
  property_count: 4
  slug: weatherapi-forecast-weather-response
- name: HourForecast
  property_count: 39
  slug: weatherapi-hour-forecast
- name: IpLookupResponse
  property_count: 15
  slug: weatherapi-ip-lookup-response
- name: Location
  property_count: 8
  slug: weatherapi-location
- name: MarineForecastDay
  property_count: 6
  slug: weatherapi-marine-forecast-day
- name: MarineHour
  property_count: 8
  slug: weatherapi-marine-hour
- name: MarineWeatherResponse
  property_count: 2
  slug: weatherapi-marine-weather-response
- name: Pollen
  property_count: 7
  slug: weatherapi-pollen
- name: SearchLocation
  property_count: 7
  slug: weatherapi-search-location
- name: SportEvent
  property_count: 6
  slug: weatherapi-sport-event
- name: SportsResponse
  property_count: 3
  slug: weatherapi-sports-response
- name: Tide
  property_count: 3
  slug: weatherapi-tide
- name: TimezoneResponse
  property_count: 1
  slug: weatherapi-timezone-response
json_structures:
- name: Weatherapi Air Quality Structure
  property_count: 8
  slug: weatherapi-air-quality-structure
- name: Weatherapi Alert Structure
  property_count: 13
  slug: weatherapi-alert-structure
- name: Weatherapi Alerts Response Structure
  property_count: 2
  slug: weatherapi-alerts-response-structure
- name: Weatherapi Astro Element Structure
  property_count: 8
  slug: weatherapi-astro-element-structure
- name: Weatherapi Astronomy Response Structure
  property_count: 2
  slug: weatherapi-astronomy-response-structure
- name: Weatherapi Bulk Location Structure
  property_count: 2
  slug: weatherapi-bulk-location-structure
- name: Weatherapi Bulk Request Structure
  property_count: 1
  slug: weatherapi-bulk-request-structure
- name: Weatherapi Bulk Response Structure
  property_count: 1
  slug: weatherapi-bulk-response-structure
- name: Weatherapi Condition Structure
  property_count: 3
  slug: weatherapi-condition-structure
- name: Weatherapi Current Weather Response Structure
  property_count: 2
  slug: weatherapi-current-weather-response-structure
- name: Weatherapi Current Weather Structure
  property_count: 33
  slug: weatherapi-current-weather-structure
- name: Weatherapi Forecast Day Entry Structure
  property_count: 5
  slug: weatherapi-forecast-day-entry-structure
- name: Weatherapi Forecast Day Structure
  property_count: 21
  slug: weatherapi-forecast-day-structure
- name: Weatherapi Forecast Weather Response Structure
  property_count: 4
  slug: weatherapi-forecast-weather-response-structure
- name: Weatherapi Hour Forecast Structure
  property_count: 39
  slug: weatherapi-hour-forecast-structure
- name: Weatherapi Ip Lookup Response Structure
  property_count: 15
  slug: weatherapi-ip-lookup-response-structure
- name: Weatherapi Location Structure
  property_count: 8
  slug: weatherapi-location-structure
- name: Weatherapi Marine Forecast Day Structure
  property_count: 6
  slug: weatherapi-marine-forecast-day-structure
- name: Weatherapi Marine Hour Structure
  property_count: 8
  slug: weatherapi-marine-hour-structure
- name: Weatherapi Marine Weather Response Structure
  property_count: 2
  slug: weatherapi-marine-weather-response-structure
- name: Weatherapi Pollen Structure
  property_count: 7
  slug: weatherapi-pollen-structure
- name: Weatherapi Search Location Structure
  property_count: 7
  slug: weatherapi-search-location-structure
- name: Weatherapi Sport Event Structure
  property_count: 6
  slug: weatherapi-sport-event-structure
- name: Weatherapi Sports Response Structure
  property_count: 3
  slug: weatherapi-sports-response-structure
- name: Weatherapi Tide Structure
  property_count: 3
  slug: weatherapi-tide-structure
- name: Weatherapi Timezone Response Structure
  property_count: 1
  slug: weatherapi-timezone-response-structure
jsonld:
- class_count: 29
  name: Weatherapi Context
  property_count: 151
  slug: weatherapi-context
layout: provider
modified: '2026-05-28'
name: WeatherAPI
nav: Providers
network: true
overview: 'WeatherAPI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Future API, Geo API, and 4 more. Tagged areas include Weather, Forecast, History, Marine, and Astronomy.


  The WeatherAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WeatherAPI''s developer surface includes authentication, getting-started guide, developer portal, signup flow, pricing, support, engineering blog, and 29 more developer resources.'
plans:
- name: Weatherapi Plans Pricing
  plan_count: 5
  slug: weatherapi-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 7
  name: Weatherapi Rate Limits
  slug: weatherapi-rate-limits
rules:
- name: WeatherAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: weatherapi-jsonschema-spectral-rules
- name: WeatherAPI API Rules
  rule_count: 37
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 21
  slug: weatherapi-rules
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 74.4
    developer_ergonomics: 41.3
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weatherapi/refs/heads/main/screenshots/weatherapi-2026-06-20T201311.png
security:
- kind: authentication
  name: Weatherapi Authentication
  slug: weatherapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weatherapi Domain Security
  slug: weatherapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: weatherapi
solutions:
- description: 100K calls/month, 3-day forecast, 1-day history — for evaluation and hobby use.
  name: Free Tier
- description: 3M calls/month, 7-day forecast and history — small production workloads.
  name: Starter ($7/mo)
- description: 5M calls/month, marine weather, bulk requests, 365-day rolling history.
  name: Pro+ ($25/mo)
- description: 10M calls/month, 14-day forecast, marine with tides, IP allow/block lists, 99.9% SLA.
  name: Business ($65/mo)
- description: 15-minute intervals, full historical archives, 100% uptime SLA with contract.
  name: Enterprise (custom)
tags:
- Weather
- Forecast
- History
- Marine
- Astronomy
- Geolocation
- Sports
- Alerts
- Public APIs
use_cases:
- description: Power mobile and web weather apps with global coverage and 200ms response times.
  name: Consumer Weather Apps
- description: Show forecast, alerts, marine, and astronomy data for trip destinations.
  name: Travel & Trip Planning
- description: Avoid weather disruptions on routes using forecast and alerts endpoints.
  name: Logistics & Fleet Routing
- description: Drive thermostats, sprinklers, and shades from real-time and forecast data.
  name: Smart Home & IoT
- description: Use rainfall, evapotranspiration, and forecast data to plan irrigation and harvest.
  name: Agriculture
- description: Solar irradiance, wind, and temperature inputs for renewable-energy generation models.
  name: Energy Forecasting
- description: Historical archives for claims investigation and parametric weather insurance.
  name: Insurance & Risk
- description: Schedule outdoor events around forecast windows and alerts.
  name: Sports & Events
- description: Wave, swell, and tide data for coastal and ocean operations.
  name: Maritime & Shipping
- description: Give Claude and other LLM agents live weather context via the official MCP server.
  name: AI Agents
website: https://www.weatherapi.com/
---
