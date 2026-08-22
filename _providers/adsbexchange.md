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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Adsbexchange Agentic Access
  operation_count: 30
  slug: adsbexchange-agentic-access
  summary_line: 30 operations · 9 acting
api_count: 5
apis:
- description: Allows filtering live data based on geopolitical boundaries, such as states/provinces, countries, regions, or even continents. All endpoints support ISO 3166-1 alpha-2 country codes and ISO 3166-2 sub
  name: ADS-B Exchange Geopolitical Filtering API
  slug: adsbexchange-geopolitical-filtering-api
- description: 'Endpoints allow filtering live data based on geospatial boundaries, such as latitude, longitude, altitudes, or even custom GeoJSON shapes. Use these endpoints to get information about aircraft within '
  name: ADS-B Exchange Geospatial Filtering API
  slug: adsbexchange-geospatial-filtering-api
- description: Endpoints provide access to airborne or recently landed aircraft, as well as last known positions. Use these endpoints to get information about aircraft, such as location, flight, altitude, speed, and
  name: ADS-B Exchange Live Positional Data API
  slug: adsbexchange-live-positional-data-api
- description: Endpoints provide access to Takeoffs/Landings operational events.
  name: ADS-B Exchange Operations API
  slug: adsbexchange-operations-api
- description: Endpoints provide access to historical trace files for an aircraft.
  name: ADS-B Exchange Traces API
  slug: adsbexchange-traces-api
artifact_total: 79
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ADSB Exchange Geopolitical Filtering API
  slug: open-adsbexchange-geopolitical-filtering-api
- collection_type: open
  name: ADSB Exchange Geopolitical Filtering Geospatial Filtering API
  slug: open-adsbexchange-geospatial-filtering-api
- collection_type: open
  name: ADSB Exchange Geopolitical Filtering Live Positional Data API
  slug: open-adsbexchange-live-positional-data-api
- collection_type: open
  name: ADSB Exchange Geopolitical Filtering Operations API
  slug: open-adsbexchange-operations-api
- collection_type: open
  name: ADSB Exchange Geopolitical Filtering Traces API
  slug: open-adsbexchange-traces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adsbexchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adsbexchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adsbexchange-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.adsbexchange.com
- group: other
  title: ''
  type: Developer
  url: https://www.adsbexchange.com/community/developer-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://www.adsbexchange.com/version-2-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adsbexchange.com/data-products/
- group: other
  title: ''
  type: DataProducts
  url: https://www.adsbexchange.com/data-products/
- group: operate
  title: ''
  type: Contact
  url: https://www.adsbexchange.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adsbexchange.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adsbexchange.com/legal/privacy-policy/
- group: other
  title: ''
  type: RapidAPI
  url: https://rapidapi.com/adsbx/api/adsbexchange-com1
created: '2026-06-13'
description: Unfiltered flight tracking network with REST APIs for accessing real-time aircraft positions, military flights, and global ADS-B flight data without filtering. Operated by a crowdsourced global network of ADS-B and MLAT receivers providing ultra-low-latency aircraft tracking data for aviation research and applications.
examples:
- key_count: 7
  name: Getapiaircraftv2Airport
  slug: getapiaircraftv2airport
- key_count: 7
  name: Getapiaircraftv2All
  slug: getapiaircraftv2all
- key_count: 7
  name: Getapiaircraftv2Callsign
  slug: getapiaircraftv2callsign
- key_count: 7
  name: Getapiaircraftv2Geospatialcontinent
  slug: getapiaircraftv2geospatialcontinent
- key_count: 7
  name: Getapiaircraftv2Geospatialcountry
  slug: getapiaircraftv2geospatialcountry
- key_count: 7
  name: Getapiaircraftv2Geospatialcountrysubdivision
  slug: getapiaircraftv2geospatialcountrysubdivision
- key_count: 7
  name: Getapiaircraftv2Geospatialcountrysubdivisions
  slug: getapiaircraftv2geospatialcountrysubdivisions
- key_count: 7
  name: Getapiaircraftv2Geospatialregion
  slug: getapiaircraftv2geospatialregion
- key_count: 7
  name: Getapiaircraftv2Hex
  slug: getapiaircraftv2hex
- key_count: 7
  name: Getapiaircraftv2Icao
  slug: getapiaircraftv2icao
- key_count: 7
  name: Getapiaircraftv2Latlondist
  slug: getapiaircraftv2latlondist
- key_count: 7
  name: Getapiaircraftv2Mil
  slug: getapiaircraftv2mil
- key_count: 7
  name: Getapiaircraftv2Minimallatlondist
  slug: getapiaircraftv2minimallatlondist
- key_count: 7
  name: Getapiaircraftv2Nohexdistabovelatlon
  slug: getapiaircraftv2nohexdistabovelatlon
- key_count: 7
  name: Getapiaircraftv2Operationsairport
  slug: getapiaircraftv2operationsairport
- key_count: 7
  name: Getapiaircraftv2Operationsicao
  slug: getapiaircraftv2operationsicao
- key_count: 7
  name: Getapiaircraftv2Registration
  slug: getapiaircraftv2registration
- key_count: 7
  name: Getapiaircraftv2Sqk
  slug: getapiaircraftv2sqk
- key_count: 7
  name: Getapiaircraftv2Totalaircraft
  slug: getapiaircraftv2totalaircraft
- key_count: 7
  name: Getapiaircraftv2Traces
  slug: getapiaircraftv2traces
- key_count: 7
  name: Getapiaircraftv2Traceshisttraces
  slug: getapiaircraftv2traceshisttraces
- key_count: 8
  name: Postapiaircraftv2Airport
  slug: postapiaircraftv2airport
- key_count: 8
  name: Postapiaircraftv2Filter
  slug: postapiaircraftv2filter
- key_count: 8
  name: Postapiaircraftv2Geospatialboundary
  slug: postapiaircraftv2geospatialboundary
- key_count: 8
  name: Postapiaircraftv2Hex
  slug: postapiaircraftv2hex
- key_count: 8
  name: Postapiaircraftv2Icao
  slug: postapiaircraftv2icao
- key_count: 8
  name: Postapiaircraftv2Operationsairports
  slug: postapiaircraftv2operationsairports
- key_count: 8
  name: Postapiaircraftv2Operationsicaos
  slug: postapiaircraftv2operationsicaos
- key_count: 8
  name: Postapiaircraftv2Proximityradius
  slug: postapiaircraftv2proximityradius
- key_count: 8
  name: Postapiaircraftv2Registration
  slug: postapiaircraftv2registration
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adsbexchange.png
json_schemas:
- name: AcasResolutionAdvisoryResponse
  property_count: 11
  slug: acasresolutionadvisoryresponse
- name: AircraftCollectionMinimalResponse
  property_count: 6
  slug: aircraftcollectionminimalresponse
- name: AircraftCollectionResponse
  property_count: 6
  slug: aircraftcollectionresponse
- name: AircraftRequest
  property_count: 1
  slug: aircraftrequest
- name: AircraftSingleMinimalResponse
  property_count: 33
  slug: aircraftsingleminimalresponse
- name: AircraftSingleResponse
  property_count: 60
  slug: aircraftsingleresponse
- name: AirportRequest
  property_count: 1
  slug: airportrequest
- name: ApiForbiddenResponse
  property_count: 2
  slug: apiforbiddenresponse
- name: ApiTooManyRequestsResponse
  property_count: 1
  slug: apitoomanyrequestsresponse
- name: ApiUnauthorizedResponse
  property_count: 2
  slug: apiunauthorizedresponse
- name: BadRequest
  property_count: 1
  slug: badrequest
- name: FeatureCollectionRequest
  property_count: 2
  slug: featurecollectionrequest
- name: FeatureGeometryRequest
  property_count: 2
  slug: featuregeometryrequest
- name: FeatureRequest
  property_count: 3
  slug: featurerequest
- name: FilterDefinition
  property_count: 3
  slug: filterdefinition
- name: FilterRequest
  property_count: 2
  slug: filterrequest
- name: GeoboundaryCountrySubdivision
  property_count: 6
  slug: geoboundarycountrysubdivision
- name: GeoboundaryCountrySubdivisionsResponse
  property_count: 2
  slug: geoboundarycountrysubdivisionsresponse
- name: LastPositionDataResponse
  property_count: 5
  slug: lastpositiondataresponse
- name: OperationsAirportRequest
  property_count: 1
  slug: operationsairportrequest
- name: OperationsIcaosRequest
  property_count: 1
  slug: operationsicaosrequest
- name: OperationsResponse
  property_count: 8
  slug: operationsresponse
- name: OperationsResponseItem
  property_count: 39
  slug: operationsresponseitem
- name: ProblemDetails
  property_count: 5
  slug: problemdetails
- name: ProximityPointFilter
  property_count: 5
  slug: proximitypointfilter
- name: ProximityRequest
  property_count: 1
  slug: proximityrequest
- name: RegistrationRequest
  property_count: 1
  slug: registrationrequest
- name: RequestedUrlTooLongResponse
  property_count: 1
  slug: requestedurltoolongresponse
- name: TraceNotFoundResponse
  property_count: 6
  slug: tracenotfoundresponse
- name: TraceResponse
  property_count: 3
  slug: traceresponse
jsonld:
- class_count: 8
  name: context Context
  property_count: 25
  slug: context
layout: provider
modified: '2026-06-13'
name: ADS-B Exchange
nav: Providers
network: true
overview: 'ADS-B Exchange publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Geopolitical Filtering API, Geospatial Filtering API, Live Positional Data API, and 2 more. Tagged areas include Aviation, Flight Tracking, ADS-B, Aircraft, and Real-Time.


  The ADS-B Exchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ADS-B Exchange''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ADS-B Exchange API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: adsbexchange-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.3
  delta: -10.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 69.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/adsbexchange/refs/heads/main/screenshots/adsbexchange-2026-06-20T165151.png
security:
- kind: authentication
  name: Adsbexchange Authentication
  slug: adsbexchange-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Adsbexchange Domain Security
  slug: adsbexchange-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adsbexchange
tags:
- Aviation
- Flight Tracking
- ADS-B
- Aircraft
- Real-Time
- Military
- MLAT
website: https://www.adsbexchange.com
---
