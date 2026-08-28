---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Onebusaway Agentic Access
  operation_count: 30
  slug: onebusaway-agentic-access
  summary_line: 30 operations
api_count: 2
apis:
- description: The default API from OneBusAway — 13 operation(s) for default.
  name: OneBusAway default API
  slug: onebusaway-default-api
- description: The Where API from OneBusAway — 17 operation(s) for where.
  name: OneBusAway Where API
  slug: onebusaway-where-api
artifact_total: 102
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OneBusAway default API
  slug: open-onebusaway-default-api
- collection_type: open
  name: OneBusAway default Where API
  slug: open-onebusaway-where-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/OneBusAway/sdk-config/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onebusaway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onebusaway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onebusaway-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opentransitsoftwarefoundation.org/onebusaway/
- group: start
  title: ''
  type: Portal
  url: https://developer.onebusaway.org/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onebusaway.org/api/where
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onebusaway.org/api/where/methods
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onebusaway.org/api/where/elements
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.onebusaway.org/guides/api-webapp-configuration-guide
- group: build
  title: ''
  type: SDKs
  url: https://developer.onebusaway.org/api/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneBusAway
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/onebusaway-application-modules
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/maglev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/sdk-config
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/js-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/python-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/go-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/java-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/kotlin-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/ruby-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/onebusaway-android
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/onebusaway-ios
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OneBusAway/wayfinder
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/app/onebusaway/id329380089
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=com.joulespersecond.seattlebusbot
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opentransitsoftwarefoundation.org/privacy-policy/
created: '2026-06-13'
description: OneBusAway is an open-source real-time transit information platform managed by the Open Transit Software Foundation. It provides transit riders with real-time arrival predictions, service alerts, and schedule data for buses, trains, and other transit modes. The platform exposes a RESTful API that lets developers access agency information, stop data, route details, trip information, real-time arrivals and departures, vehicle positions, and service alerts. Authentication uses an API key passed as a query parameter. The reference deployment runs at api.pugetsound.onebusaway.org; many transit agencies host their own OneBusAway instances using the same API contract. Official SDKs are published for Go, Java, Kotlin, JavaScript/Node.js, Python, and Ruby, all generated from a shared OpenAPI 3.0 specification in the sdk-config repository.
examples:
- key_count: 7
  name: Getarrivalsanddeparturesforlocation
  slug: getArrivalsAndDeparturesForLocation
- key_count: 6
  name: Get_Api_Where_Agencies With Coverage.Json
  slug: get_api_where_agencies-with-coverage.json
- key_count: 7
  name: Get_Api_Where_Agency_Agencyid.Json
  slug: get_api_where_agency_agencyID.json
- key_count: 7
  name: Get_Api_Where_Arrival And Departure For Stop_Stopid.Json
  slug: get_api_where_arrival-and-departure-for-stop_stopID.json
- key_count: 7
  name: Get_Api_Where_Arrivals And Departures For Stop_Stopid.Json
  slug: get_api_where_arrivals-and-departures-for-stop_stopID.json
- key_count: 6
  name: Get_Api_Where_Block_Blockid.Json
  slug: get_api_where_block_blockID.json
- key_count: 6
  name: Get_Api_Where_Config.Json
  slug: get_api_where_config.json
- key_count: 6
  name: Get_Api_Where_Current Time.Json
  slug: get_api_where_current-time.json
- key_count: 6
  name: Get_Api_Where_Route Ids For Agency_Agencyid.Json
  slug: get_api_where_route-ids-for-agency_agencyID.json
- key_count: 7
  name: Get_Api_Where_Route_Routeid.Json
  slug: get_api_where_route_routeID.json
- key_count: 7
  name: Get_Api_Where_Routes For Agency_Agencyid.Json
  slug: get_api_where_routes-for-agency_agencyID.json
- key_count: 7
  name: Get_Api_Where_Routes For Location.Json
  slug: get_api_where_routes-for-location.json
- key_count: 7
  name: Get_Api_Where_Schedule For Route_Routeid.Json
  slug: get_api_where_schedule-for-route_routeID.json
- key_count: 7
  name: Get_Api_Where_Schedule For Stop_Stopid.Json
  slug: get_api_where_schedule-for-stop_stopID.json
- key_count: 7
  name: Get_Api_Where_Shape_Shapeid.Json
  slug: get_api_where_shape_shapeID.json
- key_count: 6
  name: Get_Api_Where_Stop Ids For Agency_Agencyid.Json
  slug: get_api_where_stop-ids-for-agency_agencyID.json
- key_count: 6
  name: Get_Api_Where_Stop_Stopid.Json
  slug: get_api_where_stop_stopID.json
- key_count: 6
  name: Get_Api_Where_Stops For Agency_Agencyid.Json
  slug: get_api_where_stops-for-agency_agencyID.json
- key_count: 7
  name: Get_Api_Where_Stops For Location.Json
  slug: get_api_where_stops-for-location.json
- key_count: 6
  name: Get_Api_Where_Stops For Route_Routeid.Json
  slug: get_api_where_stops-for-route_routeID.json
- key_count: 7
  name: Get_Api_Where_Trip Details_Tripid.Json
  slug: get_api_where_trip-details_tripID.json
- key_count: 7
  name: Get_Api_Where_Trip For Vehicle_Vehicleid.Json
  slug: get_api_where_trip-for-vehicle_vehicleID.json
- key_count: 6
  name: Get_Api_Where_Trip_Tripid.Json
  slug: get_api_where_trip_tripID.json
- key_count: 7
  name: Get_Api_Where_Trips For Location.Json
  slug: get_api_where_trips-for-location.json
- key_count: 7
  name: Get_Api_Where_Trips For Route_Routeid.Json
  slug: get_api_where_trips-for-route_routeID.json
- key_count: 6
  name: Get_Api_Where_Vehicles For Agency_Agencyid.Json
  slug: get_api_where_vehicles-for-agency_agencyID.json
- key_count: 7
  name: Reportproblemwithstop
  slug: reportProblemWithStop
- key_count: 7
  name: Reportproblemwithtrip
  slug: reportProblemWithTrip
- key_count: 7
  name: Searchroute
  slug: searchRoute
- key_count: 7
  name: Searchstop
  slug: searchStop
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onebusaway.png
json_schemas:
- name: Agency
  property_count: 10
  slug: Agency
- name: AgencyResponse
  property_count: 2
  slug: AgencyResponse
- name: ArrivalDepartureForStop
  property_count: 34
  slug: ArrivalDepartureForStop
- name: ArrivalDepartureForStopResponse
  property_count: 2
  slug: ArrivalDepartureForStopResponse
- name: ArrivalsDeparturesForLocationResponse
  property_count: 2
  slug: ArrivalsDeparturesForLocationResponse
- name: ArrivalsDeparturesForStopResponse
  property_count: 2
  slug: ArrivalsDeparturesForStopResponse
- name: BlockConfiguration
  property_count: 3
  slug: BlockConfiguration
- name: BlockEntry
  property_count: 2
  slug: BlockEntry
- name: BlockResponse
  property_count: 2
  slug: BlockResponse
- name: BlockStopTime
  property_count: 4
  slug: BlockStopTime
- name: BlockTrip
  property_count: 4
  slug: BlockTrip
- name: Config
  property_count: 5
  slug: Config
- name: ConfigResponse
  property_count: 2
  slug: ConfigResponse
- name: Coverage
  property_count: 5
  slug: Coverage
- name: CoverageResponse
  property_count: 3
  slug: CoverageResponse
- name: CurrentTime
  property_count: 2
  slug: CurrentTime
- name: CurrentTimeResponse
  property_count: 2
  slug: CurrentTimeResponse
- name: DetailedScheduleStopTime
  property_count: 8
  slug: DetailedScheduleStopTime
- name: Location
  property_count: 2
  slug: Location
- name: Polylines
  property_count: 3
  slug: Polylines
- name: Reference
  property_count: 6
  slug: Reference
- name: ResponseWrapper
  property_count: 4
  slug: ResponseWrapper
- name: Route
  property_count: 10
  slug: Route
- name: RouteIDsForAgencyResponse
  property_count: 3
  slug: RouteIDsForAgencyResponse
- name: RouteResponse
  property_count: 2
  slug: RouteResponse
- name: RoutesForAgencyResponse
  property_count: 3
  slug: RoutesForAgencyResponse
- name: RoutesForLocationResponse
  property_count: 4
  slug: RoutesForLocationResponse
- name: ScheduleEntry
  property_count: 4
  slug: ScheduleEntry
- name: ScheduleForRouteResponse
  property_count: 1
  slug: ScheduleForRouteResponse
- name: ScheduleForStopEntry
  property_count: 3
  slug: ScheduleForStopEntry
- name: ScheduleForStopResponse
  property_count: 2
  slug: ScheduleForStopResponse
- name: ScheduleFrequency
  property_count: 6
  slug: ScheduleFrequency
- name: ScheduleStopTime
  property_count: 7
  slug: ScheduleStopTime
- name: SearchRouteResponse
  property_count: 4
  slug: SearchRouteResponse
- name: SearchStopResponse
  property_count: 4
  slug: SearchStopResponse
- name: ShapeResponse
  property_count: 2
  slug: ShapeResponse
- name: Situation
  property_count: 12
  slug: Situation
- name: Stop
  property_count: 11
  slug: Stop
- name: StopGrouping
  property_count: 4
  slug: StopGrouping
- name: StopIDsForAgencyResponse
  property_count: 3
  slug: StopIDsForAgencyResponse
- name: StopResponse
  property_count: 2
  slug: StopResponse
- name: StopRouteDirectionSchedule
  property_count: 3
  slug: StopRouteDirectionSchedule
- name: StopRouteSchedule
  property_count: 2
  slug: StopRouteSchedule
- name: StopTime
  property_count: 6
  slug: StopTime
- name: StopTripGrouping
  property_count: 5
  slug: StopTripGrouping
- name: StopsForAgencyResponse
  property_count: 4
  slug: StopsForAgencyResponse
- name: StopsForLocationResponse
  property_count: 4
  slug: StopsForLocationResponse
- name: StopsForRouteResponse
  property_count: 2
  slug: StopsForRouteResponse
- name: TimeWindow
  property_count: 2
  slug: TimeWindow
- name: Trip
  property_count: 11
  slug: Trip
- name: TripDetails
  property_count: 6
  slug: TripDetails
- name: TripDetailsResponse
  property_count: 2
  slug: TripDetailsResponse
- name: TripEntry
  property_count: 6
  slug: TripEntry
- name: TripResponse
  property_count: 2
  slug: TripResponse
- name: TripSchedule
  property_count: 5
  slug: TripSchedule
- name: TripStatus
  property_count: 27
  slug: TripStatus
- name: TripVehicleResponse
  property_count: 2
  slug: TripVehicleResponse
- name: TripWithStopTimes
  property_count: 2
  slug: TripWithStopTimes
- name: TripsForLocationResponse
  property_count: 4
  slug: TripsForLocationResponse
- name: VehicleStatus
  property_count: 11
  slug: VehicleStatus
- name: VehiclesForAgencyResponse
  property_count: 3
  slug: VehiclesForAgencyResponse
jsonld:
- class_count: 152
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: OneBusAway
nav: Providers
network: true
overview: 'OneBusAway publishes 2 APIs on the [APIs.io](https://apis.io/) network: default API and Where API. Tagged areas include Transit, Public Transit, Real-Time, Arrivals, and Departures.


  The OneBusAway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OneBusAway''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 23 more developer resources.'
plans:
- name: Onebusaway Plans Pricing
  plan_count: 2
  slug: onebusaway-plans-pricing
random_paper: 15
rules:
- effective_rule_count: 5
  extends: []
  name: OneBusAway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: onebusaway-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 9.8
    contract_quality: 49.6
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 36.5
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
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onebusaway/refs/heads/main/screenshots/onebusaway-2026-06-20T190710.png
security:
- kind: authentication
  name: Onebusaway Authentication
  slug: onebusaway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Onebusaway Domain Security
  slug: onebusaway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: onebusaway
tags:
- Transit
- Public Transit
- Real-Time
- Arrivals
- Departures
- Bus
- GTFS
- Open-Source
- Stop Data
- Trip Planning
- Service Alerts
- Vehicle Positions
- Open Data
website: https://opentransitsoftwarefoundation.org/onebusaway/
---
