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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agromonitoring Agentic Access
  operation_count: 10
  slug: agromonitoring-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 6
apis:
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: Historical NDVI vegetation index data
  name: Agromonitoring NDVI History API
  slug: agromonitoring-ndvi-history-api
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: Create and manage field polygon definitions
  name: Agromonitoring Polygons API
  slug: agromonitoring-polygons-api
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: Access satellite imagery and vegetation index data
  name: Agromonitoring Satellite Imagery API
  slug: agromonitoring-satellite-imagery-api
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: Soil temperature and moisture data
  name: Agromonitoring Soil API
  slug: agromonitoring-soil-api
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: UV radiation index data
  name: Agromonitoring UV Index API
  slug: agromonitoring-uv-index-api
- baseURL: https://api.agromonitoring.com/agro/1.0
  baseurl_source: spec
  description: Current, forecast, and historical weather data
  name: Agromonitoring Weather API
  slug: agromonitoring-weather-api
artifact_total: 78
collections:
- collection_type: postman
  name: Agromonitoring Agro NDVI History API
  slug: postman-agromonitoring-ndvi-history-api
- collection_type: postman
  name: Agromonitoring Agro NDVI History Polygons API
  slug: postman-agromonitoring-polygons-api
- collection_type: postman
  name: Agromonitoring Agro NDVI History Satellite Imagery API
  slug: postman-agromonitoring-satellite-imagery-api
- collection_type: postman
  name: Agromonitoring Agro NDVI History Soil API
  slug: postman-agromonitoring-soil-api
- collection_type: postman
  name: Agromonitoring Agro NDVI History UV Index API
  slug: postman-agromonitoring-uv-index-api
- collection_type: postman
  name: Agromonitoring Agro NDVI History Weather API
  slug: postman-agromonitoring-weather-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agromonitoring Agro NDVI History API
  slug: open-agromonitoring-ndvi-history-api
- collection_type: open
  name: Agromonitoring Agro NDVI History Polygons API
  slug: open-agromonitoring-polygons-api
- collection_type: open
  name: Agromonitoring Agro NDVI History Satellite Imagery API
  slug: open-agromonitoring-satellite-imagery-api
- collection_type: open
  name: Agromonitoring Agro NDVI History Soil API
  slug: open-agromonitoring-soil-api
- collection_type: open
  name: Agromonitoring Agro NDVI History UV Index API
  slug: open-agromonitoring-uv-index-api
- collection_type: open
  name: Agromonitoring Agro NDVI History Weather API
  slug: open-agromonitoring-weather-api
- collection_type: open
  name: Agromonitoring Agro API
  slug: open-agromonitoring
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/agromonitoring/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agromonitoring-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agromonitoring-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agromonitoring-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agromonitoring
- group: start
  title: ''
  type: Portal
  url: https://agromonitoring.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agromonitoring.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://agromonitoring.com/api/agro/#auth
- group: commercial
  title: ''
  type: Pricing
  url: https://agromonitoring.com/subscriptions
- group: operate
  title: ''
  type: FAQ
  url: https://agromonitoring.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agromonitoring.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agromonitoring.com/privacy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agromonitoring-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/agromonitoring-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agromonitoring-vocabulary.yaml
created: '2025-02-06'
description: Agromonitoring is a technology company specializing in satellite-based agricultural monitoring. Using Sentinel-2 and Landsat imagery combined with weather and soil data, Agromonitoring provides vegetation index time series (NDVI, EVI, DSWI, LSWI), current weather, multi-day forecasts, and soil conditions for registered field polygons. The platform enables precision agriculture workflows including crop health assessment, irrigation optimization, yield prediction, and climate risk monitoring.
examples:
- key_count: 2
  name: Agromonitoring Errorresponse Example
  slug: agromonitoring-errorresponse-example
- key_count: 2
  name: Agromonitoring Geojson Example
  slug: agromonitoring-geojson-example
- key_count: 4
  name: Agromonitoring Ndvirecord Example
  slug: agromonitoring-ndvirecord-example
- key_count: 5
  name: Agromonitoring Polygon Example
  slug: agromonitoring-polygon-example
- key_count: 2
  name: Agromonitoring Polygoncreaterequest Example
  slug: agromonitoring-polygoncreaterequest-example
- key_count: 5
  name: Agromonitoring Satelliteimage Example
  slug: agromonitoring-satelliteimage-example
- key_count: 4
  name: Agromonitoring Soildata Example
  slug: agromonitoring-soildata-example
- key_count: 3
  name: Agromonitoring Temperaturerange Example
  slug: agromonitoring-temperaturerange-example
- key_count: 5
  name: Agromonitoring Uvindexdata Example
  slug: agromonitoring-uvindexdata-example
- key_count: 5
  name: Agromonitoring Vegetationstats Example
  slug: agromonitoring-vegetationstats-example
- key_count: 8
  name: Agromonitoring Weatherdata Example
  slug: agromonitoring-weatherdata-example
features:
- description: Register, retrieve, and delete georeferenced agricultural field polygons using GeoJSON geometry
  name: Field Polygon Management
- description: Search Sentinel-2 and Landsat satellite archives for cloud-free imagery over registered fields
  name: Satellite Imagery Search
- description: Access NDVI, EVI, EVI2, NRI, DSWI, and LSWI historical time series to track crop health and stress
  name: Vegetation Index Time Series
- description: Real-time weather conditions including temperature, humidity, wind speed, pressure, and cloud cover
  name: Current Weather Data
- description: Multi-day weather forecasts to support irrigation scheduling and field operation planning
  name: Weather Forecasting
- description: Soil temperature at surface and 10cm depth plus volumetric soil moisture content
  name: Soil Monitoring
- description: Solar UV radiation index to assess sun exposure and radiation stress on crops
  name: UV Index Data
finops:
- name: Agromonitoring Finops
  service_category: API
  slug: agromonitoring-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agromonitoring.png
integrations:
- description: Agromonitoring uses OpenWeatherMap weather infrastructure for current and forecast data
  name: OpenWeatherMap
- description: European Space Agency Sentinel-2 satellite data is a primary imagery source
  name: Sentinel-2
- description: NASA/USGS Landsat imagery is available as an additional satellite data source
  name: Landsat
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: agromonitoring-errorresponse
- name: GeoJson
  property_count: 2
  slug: agromonitoring-geojson
- name: NdviRecord
  property_count: 4
  slug: agromonitoring-ndvirecord
- name: Polygon
  property_count: 5
  slug: agromonitoring-polygon
- name: PolygonCreateRequest
  property_count: 2
  slug: agromonitoring-polygoncreaterequest
- name: SatelliteImage
  property_count: 5
  slug: agromonitoring-satelliteimage
- name: SoilData
  property_count: 4
  slug: agromonitoring-soildata
- name: TemperatureRange
  property_count: 3
  slug: agromonitoring-temperaturerange
- name: UvIndexData
  property_count: 5
  slug: agromonitoring-uvindexdata
- name: VegetationStats
  property_count: 5
  slug: agromonitoring-vegetationstats
- name: WeatherData
  property_count: 8
  slug: agromonitoring-weatherdata
json_structures:
- name: Agromonitoring Errorresponse Structure
  property_count: 0
  slug: agromonitoring-errorresponse-structure
- name: Agromonitoring Geojson Structure
  property_count: 0
  slug: agromonitoring-geojson-structure
- name: Agromonitoring Ndvirecord Structure
  property_count: 0
  slug: agromonitoring-ndvirecord-structure
- name: Agromonitoring Polygon Structure
  property_count: 0
  slug: agromonitoring-polygon-structure
- name: Agromonitoring Polygoncreaterequest Structure
  property_count: 0
  slug: agromonitoring-polygoncreaterequest-structure
- name: Agromonitoring Satelliteimage Structure
  property_count: 0
  slug: agromonitoring-satelliteimage-structure
- name: Agromonitoring Soildata Structure
  property_count: 0
  slug: agromonitoring-soildata-structure
- name: Agromonitoring Temperaturerange Structure
  property_count: 0
  slug: agromonitoring-temperaturerange-structure
- name: Agromonitoring Uvindexdata Structure
  property_count: 0
  slug: agromonitoring-uvindexdata-structure
- name: Agromonitoring Vegetationstats Structure
  property_count: 0
  slug: agromonitoring-vegetationstats-structure
- name: Agromonitoring Weatherdata Structure
  property_count: 0
  slug: agromonitoring-weatherdata-structure
jsonld:
- class_count: 33
  name: Agromonitoring Context
  property_count: 6
  slug: agromonitoring-context
layout: provider
modified: '2026-05-19'
name: Agromonitoring
nav: Providers
network: true
overview: 'Agromonitoring publishes 6 APIs on the [APIs.io](https://apis.io/) network, including NDVI History API, Polygons API, Satellite Imagery API, and 3 more. Tagged areas include Agriculture, Satellite Imagery, Vegetation Indices, Weather, and Precision Agriculture.


  The Agromonitoring catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agromonitoring''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, FAQ, and 9 more developer resources.'
plans:
- name: Agromonitoring Plans Pricing
  plan_count: 3
  slug: agromonitoring-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Agromonitoring Rate Limits
  slug: agromonitoring-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agromonitoring API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agromonitoring-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Agromonitoring API Rules
  rule_count: 27
  severity_counts:
    error: 11
    hint: 0
    info: 0
    warn: 16
  slug: agromonitoring-spectral-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.5
    catalog_earned_first_party: 0.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 29.4
    developer_ergonomics: 39.3
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agromonitoring/refs/heads/main/screenshots/agromonitoring-2026-06-20T170453.png
security:
- kind: authentication
  name: Agromonitoring Authentication
  slug: agromonitoring-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agromonitoring Domain Security
  slug: agromonitoring-domain-security
  summary_line: TLSv1.3
slug: agromonitoring
tags:
- Agriculture
- Satellite Imagery
- Vegetation Indices
- Weather
- Precision Agriculture
- Remote Sensing
use_cases:
- description: Track vegetation index trends over the growing season to identify stress, disease, or nutrient deficiencies early
  name: Crop Health Monitoring
- description: Combine soil moisture, weather forecast, and NDVI data to optimize irrigation scheduling and reduce water usage
  name: Irrigation Management
- description: Use satellite-derived vegetation indices across the growing season to build yield prediction models
  name: Yield Prediction
- description: Register precise field polygon boundaries for targeted data retrieval and zonal analysis
  name: Field Boundary Mapping
- description: Apply variable-rate inputs using spatial variability data from satellite imagery and vegetation indices
  name: Precision Agriculture
- description: Monitor weather extremes, drought, and soil conditions to assess climate-related agricultural risks
  name: Climate Risk Assessment
website: https://agromonitoring.com/
---
