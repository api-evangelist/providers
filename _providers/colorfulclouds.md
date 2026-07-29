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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Colorfulclouds Agentic Access
  operation_count: 8
  slug: colorfulclouds-agentic-access
  summary_line: 8 operations
api_count: 6
apis:
- description: Real-time pollutant readings and AQI values under CHN and USA standards.
  name: ColorfulClouds Air Quality API
  slug: colorfulclouds-air-quality-api
- description: Severe-weather alerts published by the China Meteorological Administration.
  name: ColorfulClouds Alerts API
  slug: colorfulclouds-alerts-api
- description: Minute-level, hourly, and daily forecast endpoints.
  name: ColorfulClouds Forecast API
  slug: colorfulclouds-forecast-api
- description: Radar + nowcast precipitation map raster for live overlays.
  name: ColorfulClouds Precipitation Map API
  slug: colorfulclouds-precipitation-map-api
- description: Real-time weather conditions at the requested location.
  name: ColorfulClouds Realtime API
  slug: colorfulclouds-realtime-api
- description: Combined weather envelope returning realtime, minutely, hourly, daily, and alerts in one call.
  name: ColorfulClouds Weather API
  slug: colorfulclouds-weather-api
artifact_total: 147
collections:
- collection_type: open
  name: Caiyun Weather API
  slug: open-colorfulclouds-caiyun-weather
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/colorfulclouds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/colorfulclouds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/colorfulclouds-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://caiyunapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.caiyunapp.com/weather-api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.caiyunapp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caiyunapp
- group: build
  title: MCP Server (Caiyun Weather)
  type: Tools
  url: https://github.com/caiyunapp/mcp-caiyun-weather
- group: build
  title: Claude Code Skills (Caiyun Weather)
  type: Tools
  url: https://github.com/caiyunapp/skills
- group: build
  title: AQI Hub (Air Quality Index Calculator)
  type: Tools
  url: https://github.com/caiyunapp/aqi-hub
- group: build
  title: cyeva (Forecast Accuracy Evaluation Toolkit)
  type: Tools
  url: https://github.com/caiyunapp/cyeva
- group: commercial
  title: ''
  type: Plans
  url: plans/colorfulclouds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/colorfulclouds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/colorfulclouds-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/colorfulclouds-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/colorfulclouds-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/colorfulclouds-context.jsonld
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: ColorfulClouds Tech (彩云科技, Beijing-based) operates the Caiyun Weather API (api.caiyunapp.com), a hyperlocal weather + air quality forecasting service with minute-level precipitation, hourly forecasts up to 360 hours, daily forecasts up to 15 days, real-time AQI/pollutant readings, severe-weather alerts, and a precipitation map raster. The v2.6 platform powers consumer apps (Amap, Sina Weather) and enterprise weather integrations across China and globally, billed via tiered token plans on the Open Platform.
examples:
- key_count: 8
  name: Caiyun Weather Air Quality Realtime Example
  slug: caiyun-weather-air-quality-realtime-example
- key_count: 10
  name: Caiyun Weather Air Quality Realtime Response Example
  slug: caiyun-weather-air-quality-realtime-response-example
- key_count: 2
  name: Caiyun Weather Alert Adcode Example
  slug: caiyun-weather-alert-adcode-example
- key_count: 15
  name: Caiyun Weather Alert Content Item Example
  slug: caiyun-weather-alert-content-item-example
- key_count: 3
  name: Caiyun Weather Alert Example
  slug: caiyun-weather-alert-example
- key_count: 10
  name: Caiyun Weather Alert Response Example
  slug: caiyun-weather-alert-response-example
- key_count: 2
  name: Caiyun Weather Aqi Desc Dual Example
  slug: caiyun-weather-aqi-desc-dual-example
- key_count: 2
  name: Caiyun Weather Aqi Value Dual Example
  slug: caiyun-weather-aqi-value-dual-example
- key_count: 2
  name: Caiyun Weather Daily Air Quality Example
  slug: caiyun-weather-daily-air-quality-example
- key_count: 4
  name: Caiyun Weather Daily Aqi Item Example
  slug: caiyun-weather-daily-aqi-item-example
- key_count: 3
  name: Caiyun Weather Daily Astro Item Example
  slug: caiyun-weather-daily-astro-item-example
- key_count: 1
  name: Caiyun Weather Daily Astro Time Example
  slug: caiyun-weather-daily-astro-time-example
- key_count: 21
  name: Caiyun Weather Daily Example
  slug: caiyun-weather-daily-example
- key_count: 3
  name: Caiyun Weather Daily Life Index Entry Example
  slug: caiyun-weather-daily-life-index-entry-example
- key_count: 5
  name: Caiyun Weather Daily Life Index Example
  slug: caiyun-weather-daily-life-index-example
- key_count: 4
  name: Caiyun Weather Daily Min Max Avg Item Example
  slug: caiyun-weather-daily-min-max-avg-item-example
- key_count: 5
  name: Caiyun Weather Daily Precipitation Item Example
  slug: caiyun-weather-daily-precipitation-item-example
- key_count: 10
  name: Caiyun Weather Daily Response Example
  slug: caiyun-weather-daily-response-example
- key_count: 2
  name: Caiyun Weather Daily Skycon Item Example
  slug: caiyun-weather-daily-skycon-item-example
- key_count: 4
  name: Caiyun Weather Daily Wind Item Example
  slug: caiyun-weather-daily-wind-item-example
- key_count: 2
  name: Caiyun Weather Daily Wind Property Example
  slug: caiyun-weather-daily-wind-property-example
- key_count: 2
  name: Caiyun Weather Date Time Value Pair Example
  slug: caiyun-weather-date-time-value-pair-example
- key_count: 9
  name: Caiyun Weather Envelope Base Example
  slug: caiyun-weather-envelope-base-example
- key_count: 2
  name: Caiyun Weather Hourly Air Quality Example
  slug: caiyun-weather-hourly-air-quality-example
- key_count: 2
  name: Caiyun Weather Hourly Aqi Item Example
  slug: caiyun-weather-hourly-aqi-item-example
- key_count: 13
  name: Caiyun Weather Hourly Example
  slug: caiyun-weather-hourly-example
- key_count: 2
  name: Caiyun Weather Hourly Pm25 Item Example
  slug: caiyun-weather-hourly-pm25-item-example
- key_count: 3
  name: Caiyun Weather Hourly Precipitation Item Example
  slug: caiyun-weather-hourly-precipitation-item-example
- key_count: 10
  name: Caiyun Weather Hourly Response Example
  slug: caiyun-weather-hourly-response-example
- key_count: 2
  name: Caiyun Weather Hourly Skycon Item Example
  slug: caiyun-weather-hourly-skycon-item-example
- key_count: 3
  name: Caiyun Weather Hourly Wind Item Example
  slug: caiyun-weather-hourly-wind-item-example
- key_count: 2
  name: Caiyun Weather Life Index Item Example
  slug: caiyun-weather-life-index-item-example
- key_count: 6
  name: Caiyun Weather Minutely Example
  slug: caiyun-weather-minutely-example
- key_count: 10
  name: Caiyun Weather Minutely Response Example
  slug: caiyun-weather-minutely-response-example
- key_count: 2
  name: Caiyun Weather Precipitation Example
  slug: caiyun-weather-precipitation-example
- key_count: 3
  name: Caiyun Weather Precipitation Local Example
  slug: caiyun-weather-precipitation-local-example
- key_count: 3
  name: Caiyun Weather Precipitation Nearest Example
  slug: caiyun-weather-precipitation-nearest-example
- key_count: 13
  name: Caiyun Weather Realtime Example
  slug: caiyun-weather-realtime-example
- key_count: 2
  name: Caiyun Weather Realtime Life Index Example
  slug: caiyun-weather-realtime-life-index-example
- key_count: 10
  name: Caiyun Weather Realtime Response Example
  slug: caiyun-weather-realtime-response-example
- key_count: 7
  name: Caiyun Weather Result Example
  slug: caiyun-weather-result-example
- key_count: 10
  name: Caiyun Weather Weather Response Example
  slug: caiyun-weather-weather-response-example
- key_count: 2
  name: Caiyun Weather Wind Example
  slug: caiyun-weather-wind-example
finops:
- name: Colorfulclouds Finops
  service_category: Weather & Geospatial Data
  slug: colorfulclouds-finops
image: https://caiyunapp.com/static/img/logo.png
json_schemas:
- name: AirQualityRealtimeResponse
  property_count: 0
  slug: caiyun-weather-air-quality-realtime-response
- name: AirQualityRealtime
  property_count: 8
  slug: caiyun-weather-air-quality-realtime
- name: AlertAdcode
  property_count: 2
  slug: caiyun-weather-alert-adcode
- name: AlertContentItem
  property_count: 15
  slug: caiyun-weather-alert-content-item
- name: AlertResponse
  property_count: 0
  slug: caiyun-weather-alert-response
- name: Alert
  property_count: 3
  slug: caiyun-weather-alert
- name: AQIDescDual
  property_count: 2
  slug: caiyun-weather-aqi-desc-dual
- name: AQIValueDual
  property_count: 2
  slug: caiyun-weather-aqi-value-dual
- name: DailyAirQuality
  property_count: 2
  slug: caiyun-weather-daily-air-quality
- name: DailyAQIItem
  property_count: 4
  slug: caiyun-weather-daily-aqi-item
- name: DailyAstroItem
  property_count: 3
  slug: caiyun-weather-daily-astro-item
- name: DailyAstroTime
  property_count: 1
  slug: caiyun-weather-daily-astro-time
- name: DailyLifeIndexEntry
  property_count: 3
  slug: caiyun-weather-daily-life-index-entry
- name: DailyLifeIndex
  property_count: 5
  slug: caiyun-weather-daily-life-index
- name: DailyMinMaxAvgItem
  property_count: 4
  slug: caiyun-weather-daily-min-max-avg-item
- name: DailyPrecipitationItem
  property_count: 5
  slug: caiyun-weather-daily-precipitation-item
- name: DailyResponse
  property_count: 0
  slug: caiyun-weather-daily-response
- name: Daily
  property_count: 21
  slug: caiyun-weather-daily
- name: DailySkyconItem
  property_count: 2
  slug: caiyun-weather-daily-skycon-item
- name: DailyWindItem
  property_count: 4
  slug: caiyun-weather-daily-wind-item
- name: DailyWindProperty
  property_count: 2
  slug: caiyun-weather-daily-wind-property
- name: DateTimeValuePair
  property_count: 2
  slug: caiyun-weather-date-time-value-pair
- name: EnvelopeBase
  property_count: 9
  slug: caiyun-weather-envelope-base
- name: HourlyAirQuality
  property_count: 2
  slug: caiyun-weather-hourly-air-quality
- name: HourlyAQIItem
  property_count: 2
  slug: caiyun-weather-hourly-aqi-item
- name: HourlyPM25Item
  property_count: 2
  slug: caiyun-weather-hourly-pm25-item
- name: HourlyPrecipitationItem
  property_count: 3
  slug: caiyun-weather-hourly-precipitation-item
- name: HourlyResponse
  property_count: 0
  slug: caiyun-weather-hourly-response
- name: Hourly
  property_count: 13
  slug: caiyun-weather-hourly
- name: HourlySkyconItem
  property_count: 2
  slug: caiyun-weather-hourly-skycon-item
- name: HourlyWindItem
  property_count: 3
  slug: caiyun-weather-hourly-wind-item
- name: LifeIndexItem
  property_count: 2
  slug: caiyun-weather-life-index-item
- name: MinutelyResponse
  property_count: 0
  slug: caiyun-weather-minutely-response
- name: Minutely
  property_count: 6
  slug: caiyun-weather-minutely
- name: PrecipitationLocal
  property_count: 3
  slug: caiyun-weather-precipitation-local
- name: PrecipitationNearest
  property_count: 3
  slug: caiyun-weather-precipitation-nearest
- name: Precipitation
  property_count: 2
  slug: caiyun-weather-precipitation
- name: RealtimeLifeIndex
  property_count: 2
  slug: caiyun-weather-realtime-life-index
- name: RealtimeResponse
  property_count: 0
  slug: caiyun-weather-realtime-response
- name: Realtime
  property_count: 13
  slug: caiyun-weather-realtime
- name: Result
  property_count: 7
  slug: caiyun-weather-result
- name: SkyCon
  property_count: 0
  slug: caiyun-weather-sky-con
- name: WeatherResponse
  property_count: 0
  slug: caiyun-weather-weather-response
- name: Wind
  property_count: 2
  slug: caiyun-weather-wind
json_structures:
- name: Caiyun Weather Air Quality Realtime Response Structure
  property_count: 0
  slug: caiyun-weather-air-quality-realtime-response-structure
- name: Caiyun Weather Air Quality Realtime Structure
  property_count: 8
  slug: caiyun-weather-air-quality-realtime-structure
- name: Caiyun Weather Alert Adcode Structure
  property_count: 2
  slug: caiyun-weather-alert-adcode-structure
- name: Caiyun Weather Alert Content Item Structure
  property_count: 15
  slug: caiyun-weather-alert-content-item-structure
- name: Caiyun Weather Alert Response Structure
  property_count: 0
  slug: caiyun-weather-alert-response-structure
- name: Caiyun Weather Alert Structure
  property_count: 3
  slug: caiyun-weather-alert-structure
- name: Caiyun Weather Aqi Desc Dual Structure
  property_count: 2
  slug: caiyun-weather-aqi-desc-dual-structure
- name: Caiyun Weather Aqi Value Dual Structure
  property_count: 2
  slug: caiyun-weather-aqi-value-dual-structure
- name: Caiyun Weather Daily Air Quality Structure
  property_count: 2
  slug: caiyun-weather-daily-air-quality-structure
- name: Caiyun Weather Daily Aqi Item Structure
  property_count: 4
  slug: caiyun-weather-daily-aqi-item-structure
- name: Caiyun Weather Daily Astro Item Structure
  property_count: 3
  slug: caiyun-weather-daily-astro-item-structure
- name: Caiyun Weather Daily Astro Time Structure
  property_count: 1
  slug: caiyun-weather-daily-astro-time-structure
- name: Caiyun Weather Daily Life Index Entry Structure
  property_count: 3
  slug: caiyun-weather-daily-life-index-entry-structure
- name: Caiyun Weather Daily Life Index Structure
  property_count: 5
  slug: caiyun-weather-daily-life-index-structure
- name: Caiyun Weather Daily Min Max Avg Item Structure
  property_count: 4
  slug: caiyun-weather-daily-min-max-avg-item-structure
- name: Caiyun Weather Daily Precipitation Item Structure
  property_count: 5
  slug: caiyun-weather-daily-precipitation-item-structure
- name: Caiyun Weather Daily Response Structure
  property_count: 0
  slug: caiyun-weather-daily-response-structure
- name: Caiyun Weather Daily Skycon Item Structure
  property_count: 2
  slug: caiyun-weather-daily-skycon-item-structure
- name: Caiyun Weather Daily Structure
  property_count: 21
  slug: caiyun-weather-daily-structure
- name: Caiyun Weather Daily Wind Item Structure
  property_count: 4
  slug: caiyun-weather-daily-wind-item-structure
- name: Caiyun Weather Daily Wind Property Structure
  property_count: 2
  slug: caiyun-weather-daily-wind-property-structure
- name: Caiyun Weather Date Time Value Pair Structure
  property_count: 2
  slug: caiyun-weather-date-time-value-pair-structure
- name: Caiyun Weather Envelope Base Structure
  property_count: 9
  slug: caiyun-weather-envelope-base-structure
- name: Caiyun Weather Hourly Air Quality Structure
  property_count: 2
  slug: caiyun-weather-hourly-air-quality-structure
- name: Caiyun Weather Hourly Aqi Item Structure
  property_count: 2
  slug: caiyun-weather-hourly-aqi-item-structure
- name: Caiyun Weather Hourly Pm25 Item Structure
  property_count: 2
  slug: caiyun-weather-hourly-pm25-item-structure
- name: Caiyun Weather Hourly Precipitation Item Structure
  property_count: 3
  slug: caiyun-weather-hourly-precipitation-item-structure
- name: Caiyun Weather Hourly Response Structure
  property_count: 0
  slug: caiyun-weather-hourly-response-structure
- name: Caiyun Weather Hourly Skycon Item Structure
  property_count: 2
  slug: caiyun-weather-hourly-skycon-item-structure
- name: Caiyun Weather Hourly Structure
  property_count: 13
  slug: caiyun-weather-hourly-structure
- name: Caiyun Weather Hourly Wind Item Structure
  property_count: 3
  slug: caiyun-weather-hourly-wind-item-structure
- name: Caiyun Weather Life Index Item Structure
  property_count: 2
  slug: caiyun-weather-life-index-item-structure
- name: Caiyun Weather Minutely Response Structure
  property_count: 0
  slug: caiyun-weather-minutely-response-structure
- name: Caiyun Weather Minutely Structure
  property_count: 6
  slug: caiyun-weather-minutely-structure
- name: Caiyun Weather Precipitation Local Structure
  property_count: 3
  slug: caiyun-weather-precipitation-local-structure
- name: Caiyun Weather Precipitation Nearest Structure
  property_count: 3
  slug: caiyun-weather-precipitation-nearest-structure
- name: Caiyun Weather Precipitation Structure
  property_count: 2
  slug: caiyun-weather-precipitation-structure
- name: Caiyun Weather Realtime Life Index Structure
  property_count: 2
  slug: caiyun-weather-realtime-life-index-structure
- name: Caiyun Weather Realtime Response Structure
  property_count: 0
  slug: caiyun-weather-realtime-response-structure
- name: Caiyun Weather Realtime Structure
  property_count: 13
  slug: caiyun-weather-realtime-structure
- name: Caiyun Weather Result Structure
  property_count: 7
  slug: caiyun-weather-result-structure
- name: Caiyun Weather Sky Con Structure
  property_count: 0
  slug: caiyun-weather-sky-con-structure
- name: Caiyun Weather Weather Response Structure
  property_count: 0
  slug: caiyun-weather-weather-response-structure
- name: Caiyun Weather Wind Structure
  property_count: 2
  slug: caiyun-weather-wind-structure
jsonld:
- class_count: 36
  name: Colorfulclouds Context
  property_count: 87
  slug: colorfulclouds-context
layout: provider
modified: '2026-05-30'
name: ColorfulClouds
nav: Providers
network: true
overview: 'ColorfulClouds publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Air Quality API, Alerts API, Forecast API, and 3 more. Tagged areas include Weather, Forecasting, Air Quality, Precipitation, and Hyperlocal.


  The ColorfulClouds catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ColorfulClouds'' developer surface includes authentication, documentation, tooling, and 15 more developer resources.'
plans:
- name: Colorfulclouds Plans Pricing
  plan_count: 3
  slug: colorfulclouds-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Colorfulclouds Rate Limits
  slug: colorfulclouds-rate-limits
rules:
- name: ColorfulClouds API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: colorfulclouds-jsonschema-spectral-rules
- name: ColorfulClouds API Rules
  rule_count: 39
  severity_counts:
    error: 12
    hint: 0
    info: 5
    warn: 22
  slug: colorfulclouds-rules
score:
  band: developing
  composite: 48.9
  delta: -7.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 28.3
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/colorfulclouds/refs/heads/main/screenshots/colorfulclouds-2026-06-20T174759.png
security:
- kind: authentication
  name: Colorfulclouds Authentication
  slug: colorfulclouds-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Colorfulclouds Domain Security
  slug: colorfulclouds-domain-security
  summary_line: TLSv1.3
slug: colorfulclouds
tags:
- Weather
- Forecasting
- Air Quality
- Precipitation
- Hyperlocal
- Geospatial
- China
website: https://caiyunapp.com/
---
