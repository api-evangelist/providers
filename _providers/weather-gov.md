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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Weather Gov Agentic Access
  operation_count: 65
  slug: weather-gov-agentic-access
  summary_line: 65 operations
api_count: 13
apis:
- description: The Alerts API from Weather.gov — 8 operation(s) for alerts.
  name: Weather.gov Alerts API
  slug: weather-gov-alerts-api
- description: The Aviation API from Weather.gov — 7 operation(s) for aviation.
  name: Weather.gov Aviation API
  slug: weather-gov-aviation-api
- description: The Glossary API from Weather.gov — 1 operation(s) for glossary.
  name: Weather.gov Glossary API
  slug: weather-gov-glossary-api
- description: The Gridpoints API from Weather.gov — 4 operation(s) for gridpoints.
  name: Weather.gov Gridpoints API
  slug: weather-gov-gridpoints-api
- description: The Icons API from Weather.gov — 3 operation(s) for icons.
  name: Weather.gov Icons API
  slug: weather-gov-icons-api
- description: The Offices API from Weather.gov — 8 operation(s) for offices.
  name: Weather.gov Offices API
  slug: weather-gov-offices-api
- description: The Points API from Weather.gov — 3 operation(s) for points.
  name: Weather.gov Points API
  slug: weather-gov-points-api
- description: The Products API from Weather.gov — 9 operation(s) for products.
  name: Weather.gov Products API
  slug: weather-gov-products-api
- description: The Radar API from Weather.gov — 7 operation(s) for radar.
  name: Weather.gov Radar API
  slug: weather-gov-radar-api
- description: The Radio API from Weather.gov — 1 operation(s) for radio.
  name: Weather.gov Radio API
  slug: weather-gov-radio-api
- description: The Stations API from Weather.gov — 7 operation(s) for stations.
  name: Weather.gov Stations API
  slug: weather-gov-stations-api
- description: The Thumbnails API from Weather.gov — 1 operation(s) for thumbnails.
  name: Weather.gov Thumbnails API
  slug: weather-gov-thumbnails-api
- description: The Zones API from Weather.gov — 6 operation(s) for zones.
  name: Weather.gov Zones API
  slug: weather-gov-zones-api
artifact_total: 371
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: weather.gov API
  slug: open-openapi
- collection_type: open
  name: weather.gov Alerts API
  slug: open-weather-gov-alerts-api
- collection_type: open
  name: weather.gov Alerts Aviation API
  slug: open-weather-gov-aviation-api
- collection_type: open
  name: weather.gov Alerts Glossary API
  slug: open-weather-gov-glossary-api
- collection_type: open
  name: weather.gov Alerts Gridpoints API
  slug: open-weather-gov-gridpoints-api
- collection_type: open
  name: weather.gov Alerts Icons API
  slug: open-weather-gov-icons-api
- collection_type: open
  name: weather.gov Alerts Offices API
  slug: open-weather-gov-offices-api
- collection_type: open
  name: weather.gov Alerts Points API
  slug: open-weather-gov-points-api
- collection_type: open
  name: weather.gov Alerts Products API
  slug: open-weather-gov-products-api
- collection_type: open
  name: weather.gov Alerts Radar API
  slug: open-weather-gov-radar-api
- collection_type: open
  name: weather.gov Alerts Radio API
  slug: open-weather-gov-radio-api
- collection_type: open
  name: weather.gov Alerts Stations API
  slug: open-weather-gov-stations-api
- collection_type: open
  name: weather.gov Alerts Thumbnails API
  slug: open-weather-gov-thumbnails-api
- collection_type: open
  name: weather.gov Alerts Zones API
  slug: open-weather-gov-zones-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weather-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weather-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weather-gov-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/noaa-nws
- group: docs
  title: ''
  type: Documentation
  url: https://www.weather.gov/documentation/services-web-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/weather-gov/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.weather.gov/openapi.json
- group: start
  title: ''
  type: Portal
  url: https://www.weather.gov
- group: operate
  title: ''
  type: Contact
  url: https://www.weather.gov/contact
- group: other
  title: ''
  type: Glossary
  url: https://api.weather.gov/glossary
- group: design
  title: ''
  type: SpectralRules
  url: rules/weather-gov-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weather-gov-vocabulary.yml
created: '2024-07-02T00:00:00.000Z'
description: Weather.gov is the official website of the National Weather Service (NWS), operated by NOAA within the US Department of Commerce. The NWS provides weather, hydrologic, and climate forecasts and warnings for the United States, its territories, adjacent waters, and ocean areas. The Weather.gov API provides free, open access to forecasts, alerts, observations, radar data, aviation weather, and geographic zone information across all 50 states and territories.
examples:
- key_count: 19
  name: Weather Gov Alert Atom Entry Example
  slug: weather-gov-alert-atom-entry-example
- key_count: 6
  name: Weather Gov Alert Atom Feed Example
  slug: weather-gov-alert-atom-feed-example
- key_count: 0
  name: Weather Gov Alert Cap Example
  slug: weather-gov-alert-cap-example
- key_count: 0
  name: Weather Gov Alert Certainty Example
  slug: weather-gov-alert-certainty-example
- key_count: 2
  name: Weather Gov Alert Collection Example
  slug: weather-gov-alert-collection-example
- key_count: 0
  name: Weather Gov Alert Collection Geo Json Example
  slug: weather-gov-alert-collection-geo-json-example
- key_count: 0
  name: Weather Gov Alert Collection Json Ld Example
  slug: weather-gov-alert-collection-json-ld-example
- key_count: 19
  name: Weather Gov Alert Example
  slug: weather-gov-alert-example
- key_count: 0
  name: Weather Gov Alert Geo Json Example
  slug: weather-gov-alert-geo-json-example
- key_count: 0
  name: Weather Gov Alert Id Example
  slug: weather-gov-alert-id-example
- key_count: 1
  name: Weather Gov Alert Json Ld Example
  slug: weather-gov-alert-json-ld-example
- key_count: 0
  name: Weather Gov Alert Message Type Example
  slug: weather-gov-alert-message-type-example
- key_count: 0
  name: Weather Gov Alert Severity Example
  slug: weather-gov-alert-severity-example
- key_count: 0
  name: Weather Gov Alert Status Example
  slug: weather-gov-alert-status-example
- key_count: 0
  name: Weather Gov Alert Urgency Example
  slug: weather-gov-alert-urgency-example
- key_count: 2
  name: Weather Gov Alert Xml Parameter Example
  slug: weather-gov-alert-xml-parameter-example
- key_count: 0
  name: Weather Gov Area Code Example
  slug: weather-gov-area-code-example
- key_count: 9
  name: Weather Gov Astronomical Data Example
  slug: weather-gov-astronomical-data-example
- key_count: 0
  name: Weather Gov Atsu Identifier Example
  slug: weather-gov-atsu-identifier-example
- key_count: 0
  name: Weather Gov Binary File Example
  slug: weather-gov-binary-file-example
- key_count: 0
  name: Weather Gov Center Weather Advisory Collection Geo Json Example
  slug: weather-gov-center-weather-advisory-collection-geo-json-example
- key_count: 7
  name: Weather Gov Center Weather Advisory Example
  slug: weather-gov-center-weather-advisory-example
- key_count: 0
  name: Weather Gov Center Weather Advisory Geo Json Example
  slug: weather-gov-center-weather-advisory-geo-json-example
- key_count: 0
  name: Weather Gov Center Weather Service Unit Json Ld Example
  slug: weather-gov-center-weather-service-unit-json-ld-example
- key_count: 0
  name: Weather Gov Date Example
  slug: weather-gov-date-example
- key_count: 0
  name: Weather Gov Geo Json Bounding Box Example
  slug: weather-gov-geo-json-bounding-box-example
- key_count: 0
  name: Weather Gov Geo Json Coordinate Example
  slug: weather-gov-geo-json-coordinate-example
- key_count: 2
  name: Weather Gov Geo Json Feature Collection Example
  slug: weather-gov-geo-json-feature-collection-example
- key_count: 3
  name: Weather Gov Geo Json Feature Example
  slug: weather-gov-geo-json-feature-example
- key_count: 0
  name: Weather Gov Geo Json Geometry Example
  slug: weather-gov-geo-json-geometry-example
- key_count: 0
  name: Weather Gov Geo Json Line String Example
  slug: weather-gov-geo-json-line-string-example
- key_count: 0
  name: Weather Gov Geo Json Polygon Example
  slug: weather-gov-geo-json-polygon-example
- key_count: 0
  name: Weather Gov Geometry String Example
  slug: weather-gov-geometry-string-example
- key_count: 9
  name: Weather Gov Gridpoint Example
  slug: weather-gov-gridpoint-example
- key_count: 0
  name: Weather Gov Gridpoint Forecast Units Example
  slug: weather-gov-gridpoint-forecast-units-example
- key_count: 0
  name: Weather Gov Gridpoint Geo Json Example
  slug: weather-gov-gridpoint-geo-json-example
- key_count: 4
  name: Weather Gov Gridpoint Hourly Forecast Example
  slug: weather-gov-gridpoint-hourly-forecast-example
- key_count: 0
  name: Weather Gov Gridpoint Hourly Forecast Geo Json Example
  slug: weather-gov-gridpoint-hourly-forecast-geo-json-example
- key_count: 0
  name: Weather Gov Gridpoint Hourly Forecast Json Ld Example
  slug: weather-gov-gridpoint-hourly-forecast-json-ld-example
- key_count: 11
  name: Weather Gov Gridpoint Hourly Forecast Period Example
  slug: weather-gov-gridpoint-hourly-forecast-period-example
- key_count: 0
  name: Weather Gov Gridpoint Json Ld Example
  slug: weather-gov-gridpoint-json-ld-example
- key_count: 1
  name: Weather Gov Gridpoint Quantitative Value Layer Example
  slug: weather-gov-gridpoint-quantitative-value-layer-example
- key_count: 4
  name: Weather Gov Gridpoint12H Forecast Example
  slug: weather-gov-gridpoint12h-forecast-example
- key_count: 0
  name: Weather Gov Gridpoint12H Forecast Geo Json Example
  slug: weather-gov-gridpoint12h-forecast-geo-json-example
- key_count: 0
  name: Weather Gov Gridpoint12H Forecast Json Ld Example
  slug: weather-gov-gridpoint12h-forecast-json-ld-example
- key_count: 11
  name: Weather Gov Gridpoint12H Forecast Period Example
  slug: weather-gov-gridpoint12h-forecast-period-example
- key_count: 0
  name: Weather Gov Iso8601 Duration Example
  slug: weather-gov-iso8601-duration-example
- key_count: 0
  name: Weather Gov Iso8601 Interval Example
  slug: weather-gov-iso8601-interval-example
- key_count: 0
  name: Weather Gov Json Ld Context Example
  slug: weather-gov-json-ld-context-example
- key_count: 0
  name: Weather Gov Land Region Code Example
  slug: weather-gov-land-region-code-example
- key_count: 0
  name: Weather Gov Marine Area Code Example
  slug: weather-gov-marine-area-code-example
- key_count: 0
  name: Weather Gov Marine Region Code Example
  slug: weather-gov-marine-region-code-example
- key_count: 5
  name: Weather Gov Metar Phenomenon Example
  slug: weather-gov-metar-phenomenon-example
- key_count: 0
  name: Weather Gov Metar Sky Coverage Example
  slug: weather-gov-metar-sky-coverage-example
- key_count: 0
  name: Weather Gov Nws Center Weather Service Unit Id Example
  slug: weather-gov-nws-center-weather-service-unit-id-example
- key_count: 8
  name: Weather Gov Nws Connect Document Metadata Example
  slug: weather-gov-nws-connect-document-metadata-example
- key_count: 0
  name: Weather Gov Nws Forecast Office Id Example
  slug: weather-gov-nws-forecast-office-id-example
- key_count: 0
  name: Weather Gov Nws National Hq Id Example
  slug: weather-gov-nws-national-hq-id-example
- key_count: 0
  name: Weather Gov Nws Office Id Example
  slug: weather-gov-nws-office-id-example
- key_count: 0
  name: Weather Gov Nws Regional Hq Id Example
  slug: weather-gov-nws-regional-hq-id-example
- key_count: 0
  name: Weather Gov Nws Zone Id Example
  slug: weather-gov-nws-zone-id-example
- key_count: 0
  name: Weather Gov Nws Zone Type Example
  slug: weather-gov-nws-zone-type-example
- key_count: 0
  name: Weather Gov Observation Collection Geo Json Example
  slug: weather-gov-observation-collection-geo-json-example
- key_count: 1
  name: Weather Gov Observation Collection Json Ld Example
  slug: weather-gov-observation-collection-json-ld-example
- key_count: 9
  name: Weather Gov Observation Example
  slug: weather-gov-observation-example
- key_count: 0
  name: Weather Gov Observation Geo Json Example
  slug: weather-gov-observation-geo-json-example
- key_count: 0
  name: Weather Gov Observation Json Ld Example
  slug: weather-gov-observation-json-ld-example
- key_count: 0
  name: Weather Gov Observation Station Collection Geo Json Example
  slug: weather-gov-observation-station-collection-geo-json-example
- key_count: 2
  name: Weather Gov Observation Station Collection Json Ld Example
  slug: weather-gov-observation-station-collection-json-ld-example
- key_count: 10
  name: Weather Gov Observation Station Example
  slug: weather-gov-observation-station-example
- key_count: 0
  name: Weather Gov Observation Station Geo Json Example
  slug: weather-gov-observation-station-geo-json-example
- key_count: 0
  name: Weather Gov Observation Station Json Ld Example
  slug: weather-gov-observation-station-json-ld-example
- key_count: 0
  name: Weather Gov Office Briefing Example
  slug: weather-gov-office-briefing-example
- key_count: 15
  name: Weather Gov Office Example
  slug: weather-gov-office-example
- key_count: 1
  name: Weather Gov Office Headline Collection Example
  slug: weather-gov-office-headline-collection-example
- key_count: 9
  name: Weather Gov Office Headline Example
  slug: weather-gov-office-headline-example
- key_count: 0
  name: Weather Gov Office Weather Story Collection Example
  slug: weather-gov-office-weather-story-collection-example
- key_count: 0
  name: Weather Gov Office Weather Story Example
  slug: weather-gov-office-weather-story-example
- key_count: 1
  name: Weather Gov Pagination Info Example
  slug: weather-gov-pagination-info-example
- key_count: 16
  name: Weather Gov Point Example
  slug: weather-gov-point-example
- key_count: 0
  name: Weather Gov Point Geo Json Example
  slug: weather-gov-point-geo-json-example
- key_count: 0
  name: Weather Gov Point Json Ld Example
  slug: weather-gov-point-json-ld-example
- key_count: 0
  name: Weather Gov Point String Example
  slug: weather-gov-point-string-example
- key_count: 3
  name: Weather Gov Quantitative Value Example
  slug: weather-gov-quantitative-value-example
- key_count: 0
  name: Weather Gov Region Code Example
  slug: weather-gov-region-code-example
- key_count: 2
  name: Weather Gov Relative Location Example
  slug: weather-gov-relative-location-example
- key_count: 0
  name: Weather Gov Relative Location Geo Json Example
  slug: weather-gov-relative-location-geo-json-example
- key_count: 0
  name: Weather Gov Relative Location Json Ld Example
  slug: weather-gov-relative-location-json-ld-example
- key_count: 0
  name: Weather Gov Sigmet Collection Geo Json Example
  slug: weather-gov-sigmet-collection-geo-json-example
- key_count: 4
  name: Weather Gov Sigmet Example
  slug: weather-gov-sigmet-example
- key_count: 0
  name: Weather Gov Sigmet Geo Json Example
  slug: weather-gov-sigmet-geo-json-example
- key_count: 0
  name: Weather Gov Sigmet Sequence Number Example
  slug: weather-gov-sigmet-sequence-number-example
- key_count: 0
  name: Weather Gov State Territory Code Example
  slug: weather-gov-state-territory-code-example
- key_count: 1
  name: Weather Gov Text Product Collection Example
  slug: weather-gov-text-product-collection-example
- key_count: 8
  name: Weather Gov Text Product Example
  slug: weather-gov-text-product-example
- key_count: 1
  name: Weather Gov Text Product Location Collection Example
  slug: weather-gov-text-product-location-collection-example
- key_count: 1
  name: Weather Gov Text Product Type Collection Example
  slug: weather-gov-text-product-type-collection-example
- key_count: 0
  name: Weather Gov Time Example
  slug: weather-gov-time-example
- key_count: 0
  name: Weather Gov Unit Of Measure Example
  slug: weather-gov-unit-of-measure-example
- key_count: 0
  name: Weather Gov Zone Collection Geo Json Example
  slug: weather-gov-zone-collection-geo-json-example
- key_count: 1
  name: Weather Gov Zone Collection Json Ld Example
  slug: weather-gov-zone-collection-json-ld-example
- key_count: 12
  name: Weather Gov Zone Example
  slug: weather-gov-zone-example
- key_count: 3
  name: Weather Gov Zone Forecast Example
  slug: weather-gov-zone-forecast-example
- key_count: 0
  name: Weather Gov Zone Forecast Geo Json Example
  slug: weather-gov-zone-forecast-geo-json-example
- key_count: 0
  name: Weather Gov Zone Forecast Json Ld Example
  slug: weather-gov-zone-forecast-json-ld-example
- key_count: 0
  name: Weather Gov Zone Geo Json Example
  slug: weather-gov-zone-geo-json-example
- key_count: 0
  name: Weather Gov Zone Json Ld Example
  slug: weather-gov-zone-json-ld-example
features:
- description: No API key required (only a User-Agent header); completely free for any use.
  name: Free and Open
- description: 12-hour and hourly forecasts for 2.5km grid cells across the US.
  name: Forecast Gridpoints
- description: Live weather alerts and warnings including active counts by area, zone, and region.
  name: Real-Time Alerts
- description: Latest and historical observations from thousands of weather stations across the US.
  name: Observation Data
- description: Radar station metadata, alarms, queues, and wind profiler data.
  name: Radar Data
- description: SIGMETs, AIRMETs, Center Weather Advisories, and Terminal Aerodrome Forecasts for pilots.
  name: Aviation Weather
- description: All responses return GeoJSON or JSON-LD by default, suitable for mapping and linked data.
  name: GeoJSON Responses
- description: Supports GeoJSON, JSON-LD, DWML, OXML, CAP, and ATOM formats.
  name: Multiple Output Formats
finops:
- name: Weather Gov Finops
  service_category: API
  slug: weather-gov-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/api-web-service.png
json_schemas:
- name: AlertAtomEntry
  property_count: 19
  slug: weather-gov-alert-atom-entry
- name: AlertAtomFeed
  property_count: 6
  slug: weather-gov-alert-atom-feed
- name: AlertCap
  property_count: 0
  slug: weather-gov-alert-cap
- name: AlertCertainty
  property_count: 0
  slug: weather-gov-alert-certainty
- name: AlertCollectionGeoJson
  property_count: 0
  slug: weather-gov-alert-collection-geo-json
- name: AlertCollectionJsonLd
  property_count: 0
  slug: weather-gov-alert-collection-json-ld
- name: AlertCollection
  property_count: 3
  slug: weather-gov-alert-collection
- name: AlertGeoJson
  property_count: 0
  slug: weather-gov-alert-geo-json
- name: AlertId
  property_count: 0
  slug: weather-gov-alert-id
- name: AlertJsonLd
  property_count: 1
  slug: weather-gov-alert-json-ld
- name: AlertMessageType
  property_count: 0
  slug: weather-gov-alert-message-type
- name: Alert
  property_count: 30
  slug: weather-gov-alert
- name: AlertSeverity
  property_count: 0
  slug: weather-gov-alert-severity
- name: AlertStatus
  property_count: 0
  slug: weather-gov-alert-status
- name: AlertUrgency
  property_count: 0
  slug: weather-gov-alert-urgency
- name: AlertXMLParameter
  property_count: 2
  slug: weather-gov-alert-xml-parameter
- name: AreaCode
  property_count: 0
  slug: weather-gov-area-code
- name: AstronomicalData
  property_count: 9
  slug: weather-gov-astronomical-data
- name: ATSUIdentifier
  property_count: 0
  slug: weather-gov-atsu-identifier
- name: BinaryFile
  property_count: 0
  slug: weather-gov-binary-file
- name: CenterWeatherAdvisoryCollectionGeoJson
  property_count: 0
  slug: weather-gov-center-weather-advisory-collection-geo-json
- name: CenterWeatherAdvisoryGeoJson
  property_count: 0
  slug: weather-gov-center-weather-advisory-geo-json
- name: CenterWeatherAdvisory
  property_count: 8
  slug: weather-gov-center-weather-advisory
- name: CenterWeatherServiceUnitJsonLd
  property_count: 0
  slug: weather-gov-center-weather-service-unit-json-ld
- name: Date
  property_count: 0
  slug: weather-gov-date
- name: GeoJsonBoundingBox
  property_count: 0
  slug: weather-gov-geo-json-bounding-box
- name: GeoJsonCoordinate
  property_count: 0
  slug: weather-gov-geo-json-coordinate
- name: GeoJsonFeatureCollection
  property_count: 3
  slug: weather-gov-geo-json-feature-collection
- name: GeoJsonFeature
  property_count: 5
  slug: weather-gov-geo-json-feature
- name: GeoJsonGeometry
  property_count: 0
  slug: weather-gov-geo-json-geometry
- name: GeoJsonLineString
  property_count: 0
  slug: weather-gov-geo-json-line-string
- name: GeoJsonPolygon
  property_count: 0
  slug: weather-gov-geo-json-polygon
- name: GeometryString
  property_count: 0
  slug: weather-gov-geometry-string
- name: GridpointForecastUnits
  property_count: 0
  slug: weather-gov-gridpoint-forecast-units
- name: GridpointGeoJson
  property_count: 0
  slug: weather-gov-gridpoint-geo-json
- name: GridpointHourlyForecastGeoJson
  property_count: 0
  slug: weather-gov-gridpoint-hourly-forecast-geo-json
- name: GridpointHourlyForecastJsonLd
  property_count: 0
  slug: weather-gov-gridpoint-hourly-forecast-json-ld
- name: GridpointHourlyForecastPeriod
  property_count: 17
  slug: weather-gov-gridpoint-hourly-forecast-period
- name: GridpointHourlyForecast
  property_count: 9
  slug: weather-gov-gridpoint-hourly-forecast
- name: GridpointJsonLd
  property_count: 0
  slug: weather-gov-gridpoint-json-ld
- name: GridpointQuantitativeValueLayer
  property_count: 2
  slug: weather-gov-gridpoint-quantitative-value-layer
- name: Gridpoint
  property_count: 13
  slug: weather-gov-gridpoint
- name: Gridpoint12hForecastGeoJson
  property_count: 0
  slug: weather-gov-gridpoint12h-forecast-geo-json
- name: Gridpoint12hForecastJsonLd
  property_count: 0
  slug: weather-gov-gridpoint12h-forecast-json-ld
- name: Gridpoint12hForecastPeriod
  property_count: 15
  slug: weather-gov-gridpoint12h-forecast-period
- name: Gridpoint12hForecast
  property_count: 9
  slug: weather-gov-gridpoint12h-forecast
- name: ISO8601Duration
  property_count: 0
  slug: weather-gov-iso8601-duration
- name: ISO8601Interval
  property_count: 0
  slug: weather-gov-iso8601-interval
- name: JsonLdContext
  property_count: 0
  slug: weather-gov-json-ld-context
- name: LandRegionCode
  property_count: 0
  slug: weather-gov-land-region-code
- name: MarineAreaCode
  property_count: 0
  slug: weather-gov-marine-area-code
- name: MarineRegionCode
  property_count: 0
  slug: weather-gov-marine-region-code
- name: MetarPhenomenon
  property_count: 5
  slug: weather-gov-metar-phenomenon
- name: MetarSkyCoverage
  property_count: 0
  slug: weather-gov-metar-sky-coverage
- name: NWSCenterWeatherServiceUnitId
  property_count: 0
  slug: weather-gov-nws-center-weather-service-unit-id
- name: NWSConnectDocumentMetadata
  property_count: 8
  slug: weather-gov-nws-connect-document-metadata
- name: NWSForecastOfficeId
  property_count: 0
  slug: weather-gov-nws-forecast-office-id
- name: NWSNationalHQId
  property_count: 0
  slug: weather-gov-nws-national-hq-id
- name: NWSOfficeId
  property_count: 0
  slug: weather-gov-nws-office-id
- name: NWSRegionalHQId
  property_count: 0
  slug: weather-gov-nws-regional-hq-id
- name: NWSZoneID
  property_count: 0
  slug: weather-gov-nws-zone-id
- name: NWSZoneType
  property_count: 0
  slug: weather-gov-nws-zone-type
- name: ObservationCollectionGeoJson
  property_count: 0
  slug: weather-gov-observation-collection-geo-json
- name: ObservationCollectionJsonLd
  property_count: 3
  slug: weather-gov-observation-collection-json-ld
- name: ObservationGeoJson
  property_count: 0
  slug: weather-gov-observation-geo-json
- name: ObservationJsonLd
  property_count: 0
  slug: weather-gov-observation-json-ld
- name: Observation
  property_count: 30
  slug: weather-gov-observation
- name: ObservationStationCollectionGeoJson
  property_count: 0
  slug: weather-gov-observation-station-collection-geo-json
- name: ObservationStationCollectionJsonLd
  property_count: 4
  slug: weather-gov-observation-station-collection-json-ld
- name: ObservationStationGeoJson
  property_count: 0
  slug: weather-gov-observation-station-geo-json
- name: ObservationStationJsonLd
  property_count: 0
  slug: weather-gov-observation-station-json-ld
- name: ObservationStation
  property_count: 15
  slug: weather-gov-observation-station
- name: OfficeBriefing
  property_count: 0
  slug: weather-gov-office-briefing
- name: OfficeHeadlineCollection
  property_count: 2
  slug: weather-gov-office-headline-collection
- name: OfficeHeadline
  property_count: 11
  slug: weather-gov-office-headline
- name: Office
  property_count: 16
  slug: weather-gov-office
- name: OfficeWeatherStoryCollection
  property_count: 0
  slug: weather-gov-office-weather-story-collection
- name: OfficeWeatherStory
  property_count: 0
  slug: weather-gov-office-weather-story
- name: PaginationInfo
  property_count: 1
  slug: weather-gov-pagination-info
- name: PointGeoJson
  property_count: 0
  slug: weather-gov-point-geo-json
- name: PointJsonLd
  property_count: 0
  slug: weather-gov-point-json-ld
- name: Point
  property_count: 22
  slug: weather-gov-point
- name: PointString
  property_count: 0
  slug: weather-gov-point-string
- name: QuantitativeValue
  property_count: 5
  slug: weather-gov-quantitative-value
- name: RegionCode
  property_count: 0
  slug: weather-gov-region-code
- name: RelativeLocationGeoJson
  property_count: 0
  slug: weather-gov-relative-location-geo-json
- name: RelativeLocationJsonLd
  property_count: 0
  slug: weather-gov-relative-location-json-ld
- name: RelativeLocation
  property_count: 4
  slug: weather-gov-relative-location
- name: SigmetCollectionGeoJson
  property_count: 0
  slug: weather-gov-sigmet-collection-geo-json
- name: SigmetGeoJson
  property_count: 0
  slug: weather-gov-sigmet-geo-json
- name: Sigmet
  property_count: 8
  slug: weather-gov-sigmet
- name: SigmetSequenceNumber
  property_count: 0
  slug: weather-gov-sigmet-sequence-number
- name: StateTerritoryCode
  property_count: 0
  slug: weather-gov-state-territory-code
- name: TextProductCollection
  property_count: 2
  slug: weather-gov-text-product-collection
- name: TextProductLocationCollection
  property_count: 2
  slug: weather-gov-text-product-location-collection
- name: TextProduct
  property_count: 9
  slug: weather-gov-text-product
- name: TextProductTypeCollection
  property_count: 2
  slug: weather-gov-text-product-type-collection
- name: Time
  property_count: 0
  slug: weather-gov-time
- name: UnitOfMeasure
  property_count: 0
  slug: weather-gov-unit-of-measure
- name: ZoneCollectionGeoJson
  property_count: 0
  slug: weather-gov-zone-collection-geo-json
- name: ZoneCollectionJsonLd
  property_count: 2
  slug: weather-gov-zone-collection-json-ld
- name: ZoneForecastGeoJson
  property_count: 0
  slug: weather-gov-zone-forecast-geo-json
- name: ZoneForecastJsonLd
  property_count: 0
  slug: weather-gov-zone-forecast-json-ld
- name: ZoneForecast
  property_count: 5
  slug: weather-gov-zone-forecast
- name: ZoneGeoJson
  property_count: 0
  slug: weather-gov-zone-geo-json
- name: ZoneJsonLd
  property_count: 0
  slug: weather-gov-zone-json-ld
- name: Zone
  property_count: 18
  slug: weather-gov-zone
json_structures:
- name: Weather Gov Alert Atom Entry Structure
  property_count: 19
  slug: weather-gov-alert-atom-entry-structure
- name: Weather Gov Alert Atom Feed Structure
  property_count: 6
  slug: weather-gov-alert-atom-feed-structure
- name: Weather Gov Alert Cap Structure
  property_count: 0
  slug: weather-gov-alert-cap-structure
- name: Weather Gov Alert Certainty Structure
  property_count: 0
  slug: weather-gov-alert-certainty-structure
- name: Weather Gov Alert Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-alert-collection-geo-json-structure
- name: Weather Gov Alert Collection Json Ld Structure
  property_count: 0
  slug: weather-gov-alert-collection-json-ld-structure
- name: Weather Gov Alert Collection Structure
  property_count: 3
  slug: weather-gov-alert-collection-structure
- name: Weather Gov Alert Geo Json Structure
  property_count: 0
  slug: weather-gov-alert-geo-json-structure
- name: Weather Gov Alert Id Structure
  property_count: 0
  slug: weather-gov-alert-id-structure
- name: Weather Gov Alert Json Ld Structure
  property_count: 1
  slug: weather-gov-alert-json-ld-structure
- name: Weather Gov Alert Message Type Structure
  property_count: 0
  slug: weather-gov-alert-message-type-structure
- name: Weather Gov Alert Severity Structure
  property_count: 0
  slug: weather-gov-alert-severity-structure
- name: Weather Gov Alert Status Structure
  property_count: 0
  slug: weather-gov-alert-status-structure
- name: Weather Gov Alert Structure
  property_count: 30
  slug: weather-gov-alert-structure
- name: Weather Gov Alert Urgency Structure
  property_count: 0
  slug: weather-gov-alert-urgency-structure
- name: Weather Gov Alert Xml Parameter Structure
  property_count: 2
  slug: weather-gov-alert-xml-parameter-structure
- name: Weather Gov Area Code Structure
  property_count: 0
  slug: weather-gov-area-code-structure
- name: Weather Gov Astronomical Data Structure
  property_count: 9
  slug: weather-gov-astronomical-data-structure
- name: Weather Gov Atsu Identifier Structure
  property_count: 0
  slug: weather-gov-atsu-identifier-structure
- name: Weather Gov Binary File Structure
  property_count: 0
  slug: weather-gov-binary-file-structure
- name: Weather Gov Center Weather Advisory Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-center-weather-advisory-collection-geo-json-structure
- name: Weather Gov Center Weather Advisory Geo Json Structure
  property_count: 0
  slug: weather-gov-center-weather-advisory-geo-json-structure
- name: Weather Gov Center Weather Advisory Structure
  property_count: 8
  slug: weather-gov-center-weather-advisory-structure
- name: Weather Gov Center Weather Service Unit Json Ld Structure
  property_count: 0
  slug: weather-gov-center-weather-service-unit-json-ld-structure
- name: Weather Gov Date Structure
  property_count: 0
  slug: weather-gov-date-structure
- name: Weather Gov Geo Json Bounding Box Structure
  property_count: 0
  slug: weather-gov-geo-json-bounding-box-structure
- name: Weather Gov Geo Json Coordinate Structure
  property_count: 0
  slug: weather-gov-geo-json-coordinate-structure
- name: Weather Gov Geo Json Feature Collection Structure
  property_count: 3
  slug: weather-gov-geo-json-feature-collection-structure
- name: Weather Gov Geo Json Feature Structure
  property_count: 5
  slug: weather-gov-geo-json-feature-structure
- name: Weather Gov Geo Json Geometry Structure
  property_count: 0
  slug: weather-gov-geo-json-geometry-structure
- name: Weather Gov Geo Json Line String Structure
  property_count: 0
  slug: weather-gov-geo-json-line-string-structure
- name: Weather Gov Geo Json Polygon Structure
  property_count: 0
  slug: weather-gov-geo-json-polygon-structure
- name: Weather Gov Geometry String Structure
  property_count: 0
  slug: weather-gov-geometry-string-structure
- name: Weather Gov Gridpoint Forecast Units Structure
  property_count: 0
  slug: weather-gov-gridpoint-forecast-units-structure
- name: Weather Gov Gridpoint Geo Json Structure
  property_count: 0
  slug: weather-gov-gridpoint-geo-json-structure
- name: Weather Gov Gridpoint Hourly Forecast Geo Json Structure
  property_count: 0
  slug: weather-gov-gridpoint-hourly-forecast-geo-json-structure
- name: Weather Gov Gridpoint Hourly Forecast Json Ld Structure
  property_count: 0
  slug: weather-gov-gridpoint-hourly-forecast-json-ld-structure
- name: Weather Gov Gridpoint Hourly Forecast Period Structure
  property_count: 17
  slug: weather-gov-gridpoint-hourly-forecast-period-structure
- name: Weather Gov Gridpoint Hourly Forecast Structure
  property_count: 9
  slug: weather-gov-gridpoint-hourly-forecast-structure
- name: Weather Gov Gridpoint Json Ld Structure
  property_count: 0
  slug: weather-gov-gridpoint-json-ld-structure
- name: Weather Gov Gridpoint Quantitative Value Layer Structure
  property_count: 2
  slug: weather-gov-gridpoint-quantitative-value-layer-structure
- name: Weather Gov Gridpoint Structure
  property_count: 13
  slug: weather-gov-gridpoint-structure
- name: Weather Gov Gridpoint12H Forecast Geo Json Structure
  property_count: 0
  slug: weather-gov-gridpoint12h-forecast-geo-json-structure
- name: Weather Gov Gridpoint12H Forecast Json Ld Structure
  property_count: 0
  slug: weather-gov-gridpoint12h-forecast-json-ld-structure
- name: Weather Gov Gridpoint12H Forecast Period Structure
  property_count: 15
  slug: weather-gov-gridpoint12h-forecast-period-structure
- name: Weather Gov Gridpoint12H Forecast Structure
  property_count: 9
  slug: weather-gov-gridpoint12h-forecast-structure
- name: Weather Gov Iso8601 Duration Structure
  property_count: 0
  slug: weather-gov-iso8601-duration-structure
- name: Weather Gov Iso8601 Interval Structure
  property_count: 0
  slug: weather-gov-iso8601-interval-structure
- name: Weather Gov Json Ld Context Structure
  property_count: 0
  slug: weather-gov-json-ld-context-structure
- name: Weather Gov Land Region Code Structure
  property_count: 0
  slug: weather-gov-land-region-code-structure
- name: Weather Gov Marine Area Code Structure
  property_count: 0
  slug: weather-gov-marine-area-code-structure
- name: Weather Gov Marine Region Code Structure
  property_count: 0
  slug: weather-gov-marine-region-code-structure
- name: Weather Gov Metar Phenomenon Structure
  property_count: 5
  slug: weather-gov-metar-phenomenon-structure
- name: Weather Gov Metar Sky Coverage Structure
  property_count: 0
  slug: weather-gov-metar-sky-coverage-structure
- name: Weather Gov Nws Center Weather Service Unit Id Structure
  property_count: 0
  slug: weather-gov-nws-center-weather-service-unit-id-structure
- name: Weather Gov Nws Connect Document Metadata Structure
  property_count: 8
  slug: weather-gov-nws-connect-document-metadata-structure
- name: Weather Gov Nws Forecast Office Id Structure
  property_count: 0
  slug: weather-gov-nws-forecast-office-id-structure
- name: Weather Gov Nws National Hq Id Structure
  property_count: 0
  slug: weather-gov-nws-national-hq-id-structure
- name: Weather Gov Nws Office Id Structure
  property_count: 0
  slug: weather-gov-nws-office-id-structure
- name: Weather Gov Nws Regional Hq Id Structure
  property_count: 0
  slug: weather-gov-nws-regional-hq-id-structure
- name: Weather Gov Nws Zone Id Structure
  property_count: 0
  slug: weather-gov-nws-zone-id-structure
- name: Weather Gov Nws Zone Type Structure
  property_count: 0
  slug: weather-gov-nws-zone-type-structure
- name: Weather Gov Observation Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-observation-collection-geo-json-structure
- name: Weather Gov Observation Collection Json Ld Structure
  property_count: 3
  slug: weather-gov-observation-collection-json-ld-structure
- name: Weather Gov Observation Geo Json Structure
  property_count: 0
  slug: weather-gov-observation-geo-json-structure
- name: Weather Gov Observation Json Ld Structure
  property_count: 0
  slug: weather-gov-observation-json-ld-structure
- name: Weather Gov Observation Station Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-observation-station-collection-geo-json-structure
- name: Weather Gov Observation Station Collection Json Ld Structure
  property_count: 4
  slug: weather-gov-observation-station-collection-json-ld-structure
- name: Weather Gov Observation Station Geo Json Structure
  property_count: 0
  slug: weather-gov-observation-station-geo-json-structure
- name: Weather Gov Observation Station Json Ld Structure
  property_count: 0
  slug: weather-gov-observation-station-json-ld-structure
- name: Weather Gov Observation Station Structure
  property_count: 15
  slug: weather-gov-observation-station-structure
- name: Weather Gov Observation Structure
  property_count: 30
  slug: weather-gov-observation-structure
- name: Weather Gov Office Briefing Structure
  property_count: 0
  slug: weather-gov-office-briefing-structure
- name: Weather Gov Office Headline Collection Structure
  property_count: 2
  slug: weather-gov-office-headline-collection-structure
- name: Weather Gov Office Headline Structure
  property_count: 11
  slug: weather-gov-office-headline-structure
- name: Weather Gov Office Structure
  property_count: 16
  slug: weather-gov-office-structure
- name: Weather Gov Office Weather Story Collection Structure
  property_count: 0
  slug: weather-gov-office-weather-story-collection-structure
- name: Weather Gov Office Weather Story Structure
  property_count: 0
  slug: weather-gov-office-weather-story-structure
- name: Weather Gov Pagination Info Structure
  property_count: 1
  slug: weather-gov-pagination-info-structure
- name: Weather Gov Point Geo Json Structure
  property_count: 0
  slug: weather-gov-point-geo-json-structure
- name: Weather Gov Point Json Ld Structure
  property_count: 0
  slug: weather-gov-point-json-ld-structure
- name: Weather Gov Point String Structure
  property_count: 0
  slug: weather-gov-point-string-structure
- name: Weather Gov Point Structure
  property_count: 22
  slug: weather-gov-point-structure
- name: Weather Gov Quantitative Value Structure
  property_count: 5
  slug: weather-gov-quantitative-value-structure
- name: Weather Gov Region Code Structure
  property_count: 0
  slug: weather-gov-region-code-structure
- name: Weather Gov Relative Location Geo Json Structure
  property_count: 0
  slug: weather-gov-relative-location-geo-json-structure
- name: Weather Gov Relative Location Json Ld Structure
  property_count: 0
  slug: weather-gov-relative-location-json-ld-structure
- name: Weather Gov Relative Location Structure
  property_count: 4
  slug: weather-gov-relative-location-structure
- name: Weather Gov Sigmet Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-sigmet-collection-geo-json-structure
- name: Weather Gov Sigmet Geo Json Structure
  property_count: 0
  slug: weather-gov-sigmet-geo-json-structure
- name: Weather Gov Sigmet Sequence Number Structure
  property_count: 0
  slug: weather-gov-sigmet-sequence-number-structure
- name: Weather Gov Sigmet Structure
  property_count: 8
  slug: weather-gov-sigmet-structure
- name: Weather Gov State Territory Code Structure
  property_count: 0
  slug: weather-gov-state-territory-code-structure
- name: Weather Gov Text Product Collection Structure
  property_count: 2
  slug: weather-gov-text-product-collection-structure
- name: Weather Gov Text Product Location Collection Structure
  property_count: 2
  slug: weather-gov-text-product-location-collection-structure
- name: Weather Gov Text Product Structure
  property_count: 9
  slug: weather-gov-text-product-structure
- name: Weather Gov Text Product Type Collection Structure
  property_count: 2
  slug: weather-gov-text-product-type-collection-structure
- name: Weather Gov Time Structure
  property_count: 0
  slug: weather-gov-time-structure
- name: Weather Gov Unit Of Measure Structure
  property_count: 0
  slug: weather-gov-unit-of-measure-structure
- name: Weather Gov Zone Collection Geo Json Structure
  property_count: 0
  slug: weather-gov-zone-collection-geo-json-structure
- name: Weather Gov Zone Collection Json Ld Structure
  property_count: 2
  slug: weather-gov-zone-collection-json-ld-structure
- name: Weather Gov Zone Forecast Geo Json Structure
  property_count: 0
  slug: weather-gov-zone-forecast-geo-json-structure
- name: Weather Gov Zone Forecast Json Ld Structure
  property_count: 0
  slug: weather-gov-zone-forecast-json-ld-structure
- name: Weather Gov Zone Forecast Structure
  property_count: 5
  slug: weather-gov-zone-forecast-structure
- name: Weather Gov Zone Geo Json Structure
  property_count: 0
  slug: weather-gov-zone-geo-json-structure
- name: Weather Gov Zone Json Ld Structure
  property_count: 0
  slug: weather-gov-zone-json-ld-structure
- name: Weather Gov Zone Structure
  property_count: 18
  slug: weather-gov-zone-structure
jsonld:
- class_count: 42
  name: Weather Gov Context
  property_count: 181
  slug: weather-gov-context
layout: provider
modified: '2026-05-19'
name: Weather.gov
nav: Providers
network: true
overview: 'Weather.gov publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Aviation API, Glossary API, and 10 more. Tagged areas include Weather, Government, United States, Forecasting, and Alerts.


  The Weather.gov catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Weather.gov''s developer surface includes authentication, documentation, API reference, developer portal, and 8 more developer resources.'
plans:
- name: Weather Gov Plans Pricing
  plan_count: 3
  slug: weather-gov-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Weather Gov Rate Limits
  slug: weather-gov-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Weather.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: weather-gov-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Weather.gov API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 16
  slug: weather-gov-spectral-rules
score:
  band: developing
  composite: 39.3
  delta: -2.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 62.5
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 41.4
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
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weather-gov/refs/heads/main/screenshots/weather-gov-2026-06-20T201308.png
security:
- kind: authentication
  name: Weather Gov Authentication
  slug: weather-gov-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Weather Gov Domain Security
  slug: weather-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: weather-gov
tags:
- Weather
- Government
- United States
- Forecasting
- Alerts
- Open Data
use_cases:
- description: Monitor active weather alerts and warnings for emergency response and public safety decisions.
  name: Emergency Management
- description: Integrate NWS weather data into mobile apps, websites, and IoT devices.
  name: Application Development
- description: Access SIGMETs, AIRMETs, and TAFs for flight planning and aviation safety.
  name: Aviation Planning
- description: Use zone forecasts and observation data for crop management and agricultural planning.
  name: Agricultural Monitoring
- description: Access historical observation data and forecast products for climate research and educational purposes.
  name: Research and Education
website: https://www.weather.gov
---
