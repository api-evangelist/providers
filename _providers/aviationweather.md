---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aviationweather Agentic Access
  operation_count: 20
  slug: aviationweather-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- description: Decoded navigational information
  name: Aviation Weather Center Navigational Data API
  slug: aviationweather-navigational-data-api
- description: Decoded weather information
  name: Aviation Weather Center Weather Data API
  slug: aviationweather-weather-data-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AviationWeather.gov Navigational Data API
  slug: open-aviationweather-navigational-data-api
- collection_type: open
  name: AviationWeather.gov Navigational Data Weather Data API
  slug: open-aviationweather-weather-data-api
- collection_type: open
  name: AviationWeather.gov API
  slug: open-aviationweather
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aviationweather-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviationweather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aviationweather.gov/
- group: other
  title: NOAA / National Weather Service / Aviation Weather Center
  type: Agency
  url: https://www.weather.gov/aviation/awc
- group: other
  title: NOAA NWS NCEP
  type: ParentOrganization
  url: https://www.ncep.noaa.gov/
- group: other
  title: api.weather.gov (National Weather Service general API)
  type: SisterService
  url: https://www.weather.gov/documentation/services-web-api
- group: docs
  title: ''
  type: Documentation
  url: https://aviationweather.gov/data/api/
- group: build
  title: ''
  type: Examples
  url: https://aviationweather.gov/data/example/
- group: operate
  title: ''
  type: Help
  url: https://aviationweather.gov/help/
- group: other
  title: ''
  type: RecentChanges
  url: https://aviationweather.gov/data/api/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/aviationweather-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aviationweather-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aviationweather-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/aviationweather-rules.yml
- group: other
  title: WIFS API (Weather Information For System)
  type: RelatedService
  url: https://aviationweather.gov/wifs/api?f=html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weather.gov/privacy
- group: commercial
  title: U.S. Government Work (public domain)
  type: License
  url: https://www.weather.gov/disclaimer
created: '2026-05-28'
description: The NOAA/NWS Aviation Weather Center (AWC) public data API provides machine-to-machine access to operational aviation weather products including METARs, TAFs, pilot reports (PIREPs/AIREPs), SIGMETs (domestic and international), G-AIRMETs and AIRMETs, Center Weather Advisories (CWAs), TFM convective forecasts (TCFs), area forecasts, area forecast discussions, meteorological information statements (MIS), and reference data for stations, airports, NAVAIDs, fixes, features, and obstacles. Responses are available in raw text, JSON, GeoJSON, XML, and (for METAR/TAF) IWXXM formats.
examples:
- key_count: 4
  name: Aviationweather Airmet Example
  slug: aviationweather-airmet-example
- key_count: 4
  name: Aviationweather Airport Example
  slug: aviationweather-airport-example
- key_count: 4
  name: Aviationweather Airsigmet Example
  slug: aviationweather-airsigmet-example
- key_count: 4
  name: Aviationweather Areafcst Example
  slug: aviationweather-areafcst-example
- key_count: 4
  name: Aviationweather Cwa Example
  slug: aviationweather-cwa-example
- key_count: 4
  name: Aviationweather Dataserver Example
  slug: aviationweather-dataserver-example
- key_count: 4
  name: Aviationweather Fcstdisc Example
  slug: aviationweather-fcstdisc-example
- key_count: 4
  name: Aviationweather Feature Example
  slug: aviationweather-feature-example
- key_count: 4
  name: Aviationweather Fix Example
  slug: aviationweather-fix-example
- key_count: 4
  name: Aviationweather Gairmet Example
  slug: aviationweather-gairmet-example
- key_count: 4
  name: Aviationweather Isigmet Example
  slug: aviationweather-isigmet-example
- key_count: 4
  name: Aviationweather Metar Example
  slug: aviationweather-metar-example
- key_count: 4
  name: Aviationweather Mis Example
  slug: aviationweather-mis-example
- key_count: 4
  name: Aviationweather Navaid Example
  slug: aviationweather-navaid-example
- key_count: 4
  name: Aviationweather Obstacle Example
  slug: aviationweather-obstacle-example
- key_count: 4
  name: Aviationweather Pirep Example
  slug: aviationweather-pirep-example
- key_count: 4
  name: Aviationweather Stationinfo Example
  slug: aviationweather-stationinfo-example
- key_count: 4
  name: Aviationweather Taf Example
  slug: aviationweather-taf-example
- key_count: 4
  name: Aviationweather Tcf Example
  slug: aviationweather-tcf-example
- key_count: 4
  name: Aviationweather Windtemp Example
  slug: aviationweather-windtemp-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aviationweather.png
json_schemas:
- name: AviationWeather AIRMET
  property_count: 8
  slug: aviationweather-airmet
- name: AviationWeather Airport Info
  property_count: 15
  slug: aviationweather-airport
- name: AviationWeather Domestic SIGMET
  property_count: 14
  slug: aviationweather-airsigmet
- name: AviationWeather Center Weather Advisory (CWA)
  property_count: 8
  slug: aviationweather-cwa
- name: AviationWeather Graphical AIRMET (G-AIRMET)
  property_count: 11
  slug: aviationweather-gairmet
- name: AviationWeather International SIGMET
  property_count: 16
  slug: aviationweather-isigmet
- name: AviationWeather METAR Observation
  property_count: 32
  slug: aviationweather-metar
- name: AviationWeather Pilot Report (PIREP/AIREP)
  property_count: 20
  slug: aviationweather-pirep
- name: AviationWeather Station Info
  property_count: 11
  slug: aviationweather-station
- name: AviationWeather Terminal Aerodrome Forecast (TAF)
  property_count: 15
  slug: aviationweather-taf
json_structures:
- name: Aviationweather Airmet Structure
  property_count: 8
  slug: aviationweather-airmet-structure
- name: Aviationweather Airport Structure
  property_count: 15
  slug: aviationweather-airport-structure
- name: Aviationweather Airsigmet Structure
  property_count: 14
  slug: aviationweather-airsigmet-structure
- name: Aviationweather Cwa Structure
  property_count: 8
  slug: aviationweather-cwa-structure
- name: Aviationweather Gairmet Structure
  property_count: 11
  slug: aviationweather-gairmet-structure
- name: Aviationweather Isigmet Structure
  property_count: 16
  slug: aviationweather-isigmet-structure
- name: Aviationweather Metar Structure
  property_count: 32
  slug: aviationweather-metar-structure
- name: Aviationweather Pirep Structure
  property_count: 20
  slug: aviationweather-pirep-structure
- name: Aviationweather Station Structure
  property_count: 11
  slug: aviationweather-station-structure
- name: Aviationweather Taf Structure
  property_count: 15
  slug: aviationweather-taf-structure
jsonld:
- class_count: 39
  name: Aviationweather Context
  property_count: 40
  slug: aviationweather-context
layout: provider
modified: '2026-05-29'
name: Aviation Weather Center
nav: Providers
network: true
overview: 'Aviation Weather Center publishes 2 APIs on the [APIs.io](https://apis.io/) network: Navigational Data API and Weather Data API. Tagged areas include Aviation, Weather, Government, NOAA, and NWS.


  The Aviation Weather Center catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Aviation Weather Center''s developer surface includes documentation, code examples, and 16 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 4
  name: Aviationweather Rate Limits
  slug: aviationweather-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Aviation Weather Center API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aviationweather-jsonschema-spectral-rules
- effective_rule_count: 89
  extends:
  - spectral:oas
  name: Aviation Weather Center API Rules
  rule_count: 48
  severity_counts:
    error: 14
    hint: 0
    info: 10
    warn: 24
  slug: aviationweather-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 68.7
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 31.6
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviationweather/refs/heads/main/screenshots/aviationweather-2026-06-20T172725.png
security:
- kind: domain-security
  name: Aviationweather Domain Security
  slug: aviationweather-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aviationweather
tags:
- Aviation
- Weather
- Government
- NOAA
- NWS
- METAR
- TAF
- PIREP
- SIGMET
- AIRMET
- Open Data
- Public APIs
website: https://aviationweather.gov/
---
