---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Accuweather Agentic Access
  operation_count: 21
  slug: accuweather-agentic-access
  summary_line: 21 operations
api_count: 21
apis:
- description: The Active Storms API from AccuWeather — 1 operation(s) for active storms.
  name: AccuWeather Active Storms API
  slug: accuweather-active-storms-api
- description: The Ads API from AccuWeather — 1 operation(s) for ads.
  name: AccuWeather Ads API
  slug: accuweather-ads-api
- description: The AirQuality API from AccuWeather — 1 operation(s) for airquality.
  name: AccuWeather AirQuality API
  slug: accuweather-airquality-api
- description: The Autocomplete API from AccuWeather — 1 operation(s) for autocomplete.
  name: AccuWeather Autocomplete API
  slug: accuweather-autocomplete-api
- description: The Current API from AccuWeather — 1 operation(s) for current.
  name: AccuWeather Current API
  slug: accuweather-current-api
- description: The Current Conditions API from AccuWeather — 1 operation(s) for current conditions.
  name: AccuWeather Current Conditions API
  slug: accuweather-current-conditions-api
- description: The Daily API from AccuWeather — 1 operation(s) for daily.
  name: AccuWeather Daily API
  slug: accuweather-daily-api
- description: The Daily Indices API from AccuWeather — 1 operation(s) for daily indices.
  name: AccuWeather Daily Indices API
  slug: accuweather-daily-indices-api
- description: The Favorite API from AccuWeather — 1 operation(s) for favorite.
  name: AccuWeather Favorite API
  slug: accuweather-favorite-api
- description: The Hourly API from AccuWeather — 1 operation(s) for hourly.
  name: AccuWeather Hourly API
  slug: accuweather-hourly-api
- description: The Hourlyaq API from AccuWeather — 1 operation(s) for hourlyaq.
  name: AccuWeather Hourlyaq API
  slug: accuweather-hourlyaq-api
- description: The Minutecast API from AccuWeather — 1 operation(s) for minutecast.
  name: AccuWeather Minutecast API
  slug: accuweather-minutecast-api
- description: The Partner API from AccuWeather — 1 operation(s) for partner.
  name: AccuWeather Partner API
  slug: accuweather-partner-api
- description: The Raine API from AccuWeather — 1 operation(s) for raine.
  name: AccuWeather Raine API
  slug: accuweather-raine-api
- description: The Resolve Location API from AccuWeather — 1 operation(s) for resolve location.
  name: AccuWeather Resolve Location API
  slug: accuweather-resolve-location-api
- description: The Resolve Location Redirect API from AccuWeather — 1 operation(s) for resolve location redirect.
  name: AccuWeather Resolve Location Redirect API
  slug: accuweather-resolve-location-redirect-api
- description: The StaticMap API from AccuWeather — 1 operation(s) for staticmap.
  name: AccuWeather StaticMap API
  slug: accuweather-staticmap-api
- description: The Storm API from AccuWeather — 1 operation(s) for storm.
  name: AccuWeather Storm API
  slug: accuweather-storm-api
- description: The Test API from AccuWeather — 1 operation(s) for test.
  name: AccuWeather Test API
  slug: accuweather-test-api
- description: The Tropical API from AccuWeather — 1 operation(s) for tropical.
  name: AccuWeather Tropical API
  slug: accuweather-tropical-api
- description: The Wintercast API from AccuWeather — 1 operation(s) for wintercast.
  name: AccuWeather Wintercast API
  slug: accuweather-wintercast-api
artifact_total: 216
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accuweather-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accuweather-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accuweather
- group: start
  title: ''
  type: Portal
  url: https://developer.accuweather.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accuweather.com/
- group: other
  title: ''
  type: BestPractices
  url: https://developer.accuweather.com/best-practices
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accuweather.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.accuweather.com/legal
- group: operate
  title: ''
  type: FAQ
  url: https://developer.accuweather.com/faq-page
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.accuweather.com/packages
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accuweather.com/en/privacy
- group: design
  title: AccuWeather Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
- group: design
  title: AccuWeather JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/json-ld/accuweather-context.jsonld
- group: design
  title: AccuWeather Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/vocabulary/accuweather-vocabulary.yaml
created: '2023-11-22'
description: AccuWeather provides the world's most sophisticated weather intelligence to make lives simpler, safer, and better. Their mission is to save lives and protect property through accurate weather forecasting and data. The AccuWeather One Platform API delivers current conditions, forecasts (hourly, daily, minutecast), air quality, storm tracking, lifestyle indices, and imagery to tens of billions of API calls daily.
examples:
- key_count: 8
  name: Accuweather Ad Data Example
  slug: accuweather-ad-data-example
- key_count: 5
  name: Accuweather Ad Example
  slug: accuweather-ad-example
- key_count: 3
  name: Accuweather Ad Info Example
  slug: accuweather-ad-info-example
- key_count: 0
  name: Accuweather Ad Page Info Example
  slug: accuweather-ad-page-info-example
- key_count: 12
  name: Accuweather Air Quality Example
  slug: accuweather-air-quality-example
- key_count: 10
  name: Accuweather Autocomplete Location Example
  slug: accuweather-autocomplete-location-example
- key_count: 0
  name: Accuweather Basin Id Example
  slug: accuweather-basin-id-example
- key_count: 3
  name: Accuweather Bid Example
  slug: accuweather-bid-example
- key_count: 3
  name: Accuweather Confidence Quantity Example
  slug: accuweather-confidence-quantity-example
- key_count: 5
  name: Accuweather Confidence Range Example
  slug: accuweather-confidence-range-example
- key_count: 15
  name: Accuweather Current Conditions Example
  slug: accuweather-current-conditions-example
- key_count: 10
  name: Accuweather Daily Forecast Example
  slug: accuweather-daily-forecast-example
- key_count: 4
  name: Accuweather Daily Index Example
  slug: accuweather-daily-index-example
- key_count: 0
  name: Accuweather Default App Page Options Example
  slug: accuweather-default-app-page-options-example
- key_count: 4
  name: Accuweather Device Info Example
  slug: accuweather-device-info-example
- key_count: 8
  name: Accuweather Event Confidence Example
  slug: accuweather-event-confidence-example
- key_count: 21
  name: Accuweather Extended Forecast Information Example
  slug: accuweather-extended-forecast-information-example
- key_count: 20
  name: Accuweather Favorite Location Example
  slug: accuweather-favorite-location-example
- key_count: 8
  name: Accuweather Half Day Forecast Example
  slug: accuweather-half-day-forecast-example
- key_count: 17
  name: Accuweather Hourly Forecast Example
  slug: accuweather-hourly-forecast-example
- key_count: 10
  name: Accuweather Index Day Example
  slug: accuweather-index-day-example
- key_count: 0
  name: Accuweather Index Type Example
  slug: accuweather-index-type-example
- key_count: 2
  name: Accuweather Landmark Reference Example
  slug: accuweather-landmark-reference-example
- key_count: 0
  name: Accuweather Lifestyle Category Example
  slug: accuweather-lifestyle-category-example
- key_count: 11
  name: Accuweather Location Settings Info Example
  slug: accuweather-location-settings-info-example
- key_count: 0
  name: Accuweather Location Sources Example
  slug: accuweather-location-sources-example
- key_count: 0
  name: Accuweather Measurement Display Type Example
  slug: accuweather-measurement-display-type-example
- key_count: 2
  name: Accuweather Minute Cast Forecast Example
  slug: accuweather-minute-cast-forecast-example
- key_count: 5
  name: Accuweather Minute Cast Minute Example
  slug: accuweather-minute-cast-minute-example
- key_count: 0
  name: Accuweather Minute Cast Style Example
  slug: accuweather-minute-cast-style-example
- key_count: 9
  name: Accuweather Ortb Content Example
  slug: accuweather-ortb-content-example
- key_count: 3
  name: Accuweather Ortb Data Example
  slug: accuweather-ortb-data-example
- key_count: 3
  name: Accuweather Ortb Publisher Example
  slug: accuweather-ortb-publisher-example
- key_count: 0
  name: Accuweather Ortb Relationship Type Example
  slug: accuweather-ortb-relationship-type-example
- key_count: 2
  name: Accuweather Ortb Segment Example
  slug: accuweather-ortb-segment-example
- key_count: 12
  name: Accuweather Ortb Site Example
  slug: accuweather-ortb-site-example
- key_count: 3
  name: Accuweather Page Info Example
  slug: accuweather-page-info-example
- key_count: 3
  name: Accuweather Partner Example
  slug: accuweather-partner-example
- key_count: 5
  name: Accuweather Pollutant Example
  slug: accuweather-pollutant-example
- key_count: 2
  name: Accuweather Polygon Example
  slug: accuweather-polygon-example
- key_count: 12
  name: Accuweather Prebid Timeout Out Vars Example
  slug: accuweather-prebid-timeout-out-vars-example
- key_count: 7
  name: Accuweather Precipitation Summary Example
  slug: accuweather-precipitation-summary-example
- key_count: 5
  name: Accuweather Quantity Range Estimate Example
  slug: accuweather-quantity-range-estimate-example
- key_count: 13
  name: Accuweather Raine Page View Example
  slug: accuweather-raine-page-view-example
- key_count: 13
  name: Accuweather Recent Location Example
  slug: accuweather-recent-location-example
- key_count: 3
  name: Accuweather Session Info Example
  slug: accuweather-session-info-example
- key_count: 21
  name: Accuweather Storm Example
  slug: accuweather-storm-example
- key_count: 0
  name: Accuweather Storm Icon Example
  slug: accuweather-storm-icon-example
- key_count: 29
  name: Accuweather Storm Position Example
  slug: accuweather-storm-position-example
- key_count: 0
  name: Accuweather Theme Type Example
  slug: accuweather-theme-type-example
- key_count: 8
  name: Accuweather User Info Example
  slug: accuweather-user-info-example
- key_count: 3
  name: Accuweather User Network Example
  slug: accuweather-user-network-example
- key_count: 4
  name: Accuweather Utm Info Example
  slug: accuweather-utm-info-example
- key_count: 2
  name: Accuweather Uv Index Example
  slug: accuweather-uv-index-example
- key_count: 0
  name: Accuweather Weather Event Type Example
  slug: accuweather-weather-event-type-example
- key_count: 1
  name: Accuweather Weather Info Example
  slug: accuweather-weather-info-example
- key_count: 0
  name: Accuweather Wind Direction Display Type Example
  slug: accuweather-wind-direction-display-type-example
features:
- description: Access weather data for 3.5 million+ locations worldwide with hyper-local precision pinpointed to exact latitude and longitude.
  name: Global Weather Coverage
- description: Proprietary minute-by-minute precipitation forecasts with start/stop timing for rain, snow, and ice at any location.
  name: MinuteCast Precipitation Forecasts
- description: Comprehensive data including RealFeel temperature, AccuLumen Brightness Index, 50+ lifestyle indices, and detailed atmospheric data.
  name: 250+ Weather Data Parameters
- description: Real-time and forecast air quality index (AQI) with pollutant breakdowns including PM2.5, PM10, ozone, NO2, SO2, and CO.
  name: Air Quality Monitoring
- description: Active storm tracking with positions, forecast tracks, and historical data for tropical cyclones in all global ocean basins.
  name: Tropical Storm Tracking
- description: Radar and satellite imagery maps in multiple resolutions (480x480, 640x480, 1024x1024) for integration into applications.
  name: Weather Imagery
finops:
- name: Accuweather Finops
  service_category: API
  slug: accuweather-finops
graphqls:
- description: 'This directory contains a conceptual GraphQL schema for the AccuWeather One Platform API. AccuWeather does not currently publish an official GraphQL endpoint; this schema is a translation of the REST '
  name: AccuWeather GraphQL
  slug: accuweather-graphql
image: /assets/icons/accuweather.png
integrations:
- description: AccuWeather data powers weather experiences on Apple platforms alongside native WeatherKit data.
  name: Apple WeatherKit
- description: Weather-based automation triggers in the Samsung SmartThings IoT ecosystem.
  name: Samsung SmartThings
- description: Weather data integration with Salesforce CRM for weather-aware sales and service workflows.
  name: Salesforce
- description: Azure Maps integration providing AccuWeather data within the Microsoft cloud ecosystem.
  name: Microsoft Azure
json_schemas:
- name: AdData
  property_count: 8
  slug: accuweather-ad-data
- name: AdInfo
  property_count: 3
  slug: accuweather-ad-info
- name: AdPageInfo
  property_count: 0
  slug: accuweather-ad-page-info
- name: Ad
  property_count: 5
  slug: accuweather-ad
- name: AirQuality
  property_count: 12
  slug: accuweather-air-quality
- name: AutocompleteLocation
  property_count: 10
  slug: accuweather-autocomplete-location
- name: BasinId
  property_count: 0
  slug: accuweather-basin-id
- name: Bid
  property_count: 3
  slug: accuweather-bid
- name: ConfidenceQuantity
  property_count: 3
  slug: accuweather-confidence-quantity
- name: ConfidenceRange
  property_count: 5
  slug: accuweather-confidence-range
- name: CurrentConditions
  property_count: 15
  slug: accuweather-current-conditions
- name: DailyForecast
  property_count: 10
  slug: accuweather-daily-forecast
- name: DailyIndex
  property_count: 4
  slug: accuweather-daily-index
- name: DefaultAppPageOptions
  property_count: 0
  slug: accuweather-default-app-page-options
- name: DeviceInfo
  property_count: 4
  slug: accuweather-device-info
- name: EventConfidence
  property_count: 8
  slug: accuweather-event-confidence
- name: ExtendedForecastInformation
  property_count: 21
  slug: accuweather-extended-forecast-information
- name: FavoriteLocation
  property_count: 20
  slug: accuweather-favorite-location
- name: HalfDayForecast
  property_count: 8
  slug: accuweather-half-day-forecast
- name: HourlyForecast
  property_count: 17
  slug: accuweather-hourly-forecast
- name: IndexDay
  property_count: 10
  slug: accuweather-index-day
- name: IndexType
  property_count: 0
  slug: accuweather-index-type
- name: LandmarkReference
  property_count: 2
  slug: accuweather-landmark-reference
- name: LifestyleCategory
  property_count: 0
  slug: accuweather-lifestyle-category
- name: LocationSettingsInfo
  property_count: 11
  slug: accuweather-location-settings-info
- name: LocationSources
  property_count: 0
  slug: accuweather-location-sources
- name: MeasurementDisplayType
  property_count: 0
  slug: accuweather-measurement-display-type
- name: MinuteCastForecast
  property_count: 2
  slug: accuweather-minute-cast-forecast
- name: MinuteCastMinute
  property_count: 5
  slug: accuweather-minute-cast-minute
- name: MinuteCastStyle
  property_count: 0
  slug: accuweather-minute-cast-style
- name: OrtbContent
  property_count: 9
  slug: accuweather-ortb-content
- name: OrtbData
  property_count: 3
  slug: accuweather-ortb-data
- name: OrtbPublisher
  property_count: 3
  slug: accuweather-ortb-publisher
- name: OrtbRelationshipType
  property_count: 0
  slug: accuweather-ortb-relationship-type
- name: OrtbSegment
  property_count: 2
  slug: accuweather-ortb-segment
- name: OrtbSite
  property_count: 12
  slug: accuweather-ortb-site
- name: PageInfo
  property_count: 3
  slug: accuweather-page-info
- name: Partner
  property_count: 3
  slug: accuweather-partner
- name: Pollutant
  property_count: 5
  slug: accuweather-pollutant
- name: Polygon
  property_count: 2
  slug: accuweather-polygon
- name: PrebidTimeoutOutVars
  property_count: 12
  slug: accuweather-prebid-timeout-out-vars
- name: PrecipitationSummary
  property_count: 7
  slug: accuweather-precipitation-summary
- name: QuantityRangeEstimate
  property_count: 5
  slug: accuweather-quantity-range-estimate
- name: RainePageView
  property_count: 13
  slug: accuweather-raine-page-view
- name: RecentLocation
  property_count: 13
  slug: accuweather-recent-location
- name: SessionInfo
  property_count: 3
  slug: accuweather-session-info
- name: StormIcon
  property_count: 0
  slug: accuweather-storm-icon
- name: StormPosition
  property_count: 29
  slug: accuweather-storm-position
- name: Storm
  property_count: 21
  slug: accuweather-storm
- name: ThemeType
  property_count: 0
  slug: accuweather-theme-type
- name: UserInfo
  property_count: 8
  slug: accuweather-user-info
- name: UserNetwork
  property_count: 3
  slug: accuweather-user-network
- name: UTMInfo
  property_count: 4
  slug: accuweather-utm-info
- name: UVIndex
  property_count: 2
  slug: accuweather-uv-index
- name: WeatherEventType
  property_count: 0
  slug: accuweather-weather-event-type
- name: WeatherInfo
  property_count: 1
  slug: accuweather-weather-info
- name: WindDirectionDisplayType
  property_count: 0
  slug: accuweather-wind-direction-display-type
json_structures:
- name: Accuweather Ad Data Structure
  property_count: 8
  slug: accuweather-ad-data-structure
- name: Accuweather Ad Info Structure
  property_count: 3
  slug: accuweather-ad-info-structure
- name: Accuweather Ad Page Info Structure
  property_count: 0
  slug: accuweather-ad-page-info-structure
- name: Accuweather Ad Structure
  property_count: 5
  slug: accuweather-ad-structure
- name: Accuweather Air Quality Structure
  property_count: 12
  slug: accuweather-air-quality-structure
- name: Accuweather Autocomplete Location Structure
  property_count: 10
  slug: accuweather-autocomplete-location-structure
- name: Accuweather Basin Id Structure
  property_count: 0
  slug: accuweather-basin-id-structure
- name: Accuweather Bid Structure
  property_count: 3
  slug: accuweather-bid-structure
- name: Accuweather Confidence Quantity Structure
  property_count: 3
  slug: accuweather-confidence-quantity-structure
- name: Accuweather Confidence Range Structure
  property_count: 5
  slug: accuweather-confidence-range-structure
- name: Accuweather Current Conditions Structure
  property_count: 15
  slug: accuweather-current-conditions-structure
- name: Accuweather Daily Forecast Structure
  property_count: 10
  slug: accuweather-daily-forecast-structure
- name: Accuweather Daily Index Structure
  property_count: 4
  slug: accuweather-daily-index-structure
- name: Accuweather Default App Page Options Structure
  property_count: 0
  slug: accuweather-default-app-page-options-structure
- name: Accuweather Device Info Structure
  property_count: 4
  slug: accuweather-device-info-structure
- name: Accuweather Event Confidence Structure
  property_count: 8
  slug: accuweather-event-confidence-structure
- name: Accuweather Extended Forecast Information Structure
  property_count: 21
  slug: accuweather-extended-forecast-information-structure
- name: Accuweather Favorite Location Structure
  property_count: 20
  slug: accuweather-favorite-location-structure
- name: Accuweather Half Day Forecast Structure
  property_count: 8
  slug: accuweather-half-day-forecast-structure
- name: Accuweather Hourly Forecast Structure
  property_count: 17
  slug: accuweather-hourly-forecast-structure
- name: Accuweather Index Day Structure
  property_count: 10
  slug: accuweather-index-day-structure
- name: Accuweather Index Type Structure
  property_count: 0
  slug: accuweather-index-type-structure
- name: Accuweather Landmark Reference Structure
  property_count: 2
  slug: accuweather-landmark-reference-structure
- name: Accuweather Lifestyle Category Structure
  property_count: 0
  slug: accuweather-lifestyle-category-structure
- name: Accuweather Location Settings Info Structure
  property_count: 11
  slug: accuweather-location-settings-info-structure
- name: Accuweather Location Sources Structure
  property_count: 0
  slug: accuweather-location-sources-structure
- name: Accuweather Measurement Display Type Structure
  property_count: 0
  slug: accuweather-measurement-display-type-structure
- name: Accuweather Minute Cast Forecast Structure
  property_count: 2
  slug: accuweather-minute-cast-forecast-structure
- name: Accuweather Minute Cast Minute Structure
  property_count: 5
  slug: accuweather-minute-cast-minute-structure
- name: Accuweather Minute Cast Style Structure
  property_count: 0
  slug: accuweather-minute-cast-style-structure
- name: Accuweather Ortb Content Structure
  property_count: 9
  slug: accuweather-ortb-content-structure
- name: Accuweather Ortb Data Structure
  property_count: 3
  slug: accuweather-ortb-data-structure
- name: Accuweather Ortb Publisher Structure
  property_count: 3
  slug: accuweather-ortb-publisher-structure
- name: Accuweather Ortb Relationship Type Structure
  property_count: 0
  slug: accuweather-ortb-relationship-type-structure
- name: Accuweather Ortb Segment Structure
  property_count: 2
  slug: accuweather-ortb-segment-structure
- name: Accuweather Ortb Site Structure
  property_count: 12
  slug: accuweather-ortb-site-structure
- name: Accuweather Page Info Structure
  property_count: 3
  slug: accuweather-page-info-structure
- name: Accuweather Partner Structure
  property_count: 3
  slug: accuweather-partner-structure
- name: Accuweather Pollutant Structure
  property_count: 5
  slug: accuweather-pollutant-structure
- name: Accuweather Polygon Structure
  property_count: 2
  slug: accuweather-polygon-structure
- name: Accuweather Prebid Timeout Out Vars Structure
  property_count: 12
  slug: accuweather-prebid-timeout-out-vars-structure
- name: Accuweather Precipitation Summary Structure
  property_count: 7
  slug: accuweather-precipitation-summary-structure
- name: Accuweather Quantity Range Estimate Structure
  property_count: 5
  slug: accuweather-quantity-range-estimate-structure
- name: Accuweather Raine Page View Structure
  property_count: 13
  slug: accuweather-raine-page-view-structure
- name: Accuweather Recent Location Structure
  property_count: 13
  slug: accuweather-recent-location-structure
- name: Accuweather Session Info Structure
  property_count: 3
  slug: accuweather-session-info-structure
- name: Accuweather Storm Icon Structure
  property_count: 0
  slug: accuweather-storm-icon-structure
- name: Accuweather Storm Position Structure
  property_count: 29
  slug: accuweather-storm-position-structure
- name: Accuweather Storm Structure
  property_count: 21
  slug: accuweather-storm-structure
- name: Accuweather Theme Type Structure
  property_count: 0
  slug: accuweather-theme-type-structure
- name: Accuweather User Info Structure
  property_count: 8
  slug: accuweather-user-info-structure
- name: Accuweather User Network Structure
  property_count: 3
  slug: accuweather-user-network-structure
- name: Accuweather Utm Info Structure
  property_count: 4
  slug: accuweather-utm-info-structure
- name: Accuweather Uv Index Structure
  property_count: 2
  slug: accuweather-uv-index-structure
- name: Accuweather Weather Event Type Structure
  property_count: 0
  slug: accuweather-weather-event-type-structure
- name: Accuweather Weather Info Structure
  property_count: 1
  slug: accuweather-weather-info-structure
- name: Accuweather Wind Direction Display Type Structure
  property_count: 0
  slug: accuweather-wind-direction-display-type-structure
jsonld:
- class_count: 47
  name: Accuweather Context
  property_count: 250
  slug: accuweather-context
layout: provider
modified: '2026-05-19'
name: AccuWeather
nav: Providers
network: true
overview: 'AccuWeather publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Active Storms API, Ads API, AirQuality API, and 18 more. Tagged areas include Weather, Forecasts, Meteorology, Location Services, and Air Quality.


  The AccuWeather catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AccuWeather''s developer surface includes developer portal, getting-started guide, FAQ, pricing, and 10 more developer resources.'
plans:
- name: Accuweather Plans Pricing
  plan_count: 3
  slug: accuweather-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Accuweather Rate Limits
  slug: accuweather-rate-limits
rules:
- name: AccuWeather API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: accuweather-jsonschema-spectral-rules
- name: AccuWeather API Rules
  rule_count: 29
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 14
  slug: accuweather-spectral-rules
score:
  band: developing
  composite: 53.7
  delta: -3.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/screenshots/accuweather-2026-06-20T163703.png
security:
- kind: domain-security
  name: Accuweather Domain Security
  slug: accuweather-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accuweather
tags:
- Weather
- Forecasts
- Meteorology
- Location Services
- Air Quality
- Storms
use_cases:
- description: Power mobile and web weather apps with accurate current conditions, forecasts, and location-aware weather data.
  name: Consumer Weather Applications
- description: Trigger IoT device actions based on real-time weather conditions, forecasts, and precipitation alerts.
  name: IoT and Smart Home Automation
- description: Integrate weather data into travel booking, outdoor activity planning, and event management platforms.
  name: Travel and Outdoor Planning
- description: Use storm tracking, severe weather alerts, and precipitation forecasts for emergency response and public safety.
  name: Emergency Management
- description: Access hyper-local weather data and forecasts for precision agriculture, crop management, and environmental monitoring.
  name: Agriculture and Environmental Monitoring
website: https://developer.accuweather.com/
---
