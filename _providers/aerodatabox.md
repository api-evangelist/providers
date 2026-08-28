---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: false
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
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Aerodatabox Agentic Access
  operation_count: 42
  slug: aerodatabox-agentic-access
  summary_line: 42 operations · 4 acting
api_count: 8
apis:
- description: The Aircraft API API from AeroDataBox — 6 operation(s) for aircraft api.
  name: AeroDataBox Aircraft API API
  slug: aerodatabox-aircraft-api-api
- description: The Airport API API from AeroDataBox — 5 operation(s) for airport api.
  name: AeroDataBox Airport API API
  slug: aerodatabox-airport-api-api
- description: The Flight Alert API API from AeroDataBox — 6 operation(s) for flight alert api.
  name: AeroDataBox Flight Alert API API
  slug: aerodatabox-flight-alert-api-api
- description: The Flight API API from AeroDataBox — 8 operation(s) for flight api.
  name: AeroDataBox Flight API API
  slug: aerodatabox-flight-api-api
- description: The Healthcheck API API from AeroDataBox — 3 operation(s) for healthcheck api.
  name: AeroDataBox Healthcheck API API
  slug: aerodatabox-healthcheck-api-api
- description: The Industry API API from AeroDataBox — 1 operation(s) for industry api.
  name: AeroDataBox Industry API API
  slug: aerodatabox-industry-api-api
- description: The Miscellaneous API API from AeroDataBox — 4 operation(s) for miscellaneous api.
  name: AeroDataBox Miscellaneous API API
  slug: aerodatabox-miscellaneous-api-api
- description: The Statistical API API from AeroDataBox — 8 operation(s) for statistical api.
  name: AeroDataBox Statistical API API
  slug: aerodatabox-statistical-api-api
artifact_total: 371
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API API
  slug: open-aerodatabox-aircraft-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Airport API API
  slug: open-aerodatabox-airport-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Flight Alert API API
  slug: open-aerodatabox-flight-alert-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Flight API API
  slug: open-aerodatabox-flight-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Healthcheck API API
  slug: open-aerodatabox-healthcheck-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Industry API API
  slug: open-aerodatabox-industry-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Miscellaneous API API
  slug: open-aerodatabox-miscellaneous-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight Aircraft API Statistical API API
  slug: open-aerodatabox-statistical-api-api
- collection_type: open
  name: AeroDataBox API - Aviation and Flight API
  slug: open-aerodatabox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aerodatabox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerodatabox-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://doc.aerodatabox.com/
- group: start
  title: ''
  type: Portal
  url: https://www.aerodatabox.com/
- group: other
  title: RapidAPI
  type: Marketplace
  url: https://rapidapi.com/aerodatabox/api/aerodatabox
- group: other
  title: API.Market
  type: Marketplace
  url: https://api.market/store/aedbx/aerodatabox
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aerodatabox.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerodatabox.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerodatabox.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.aerodatabox.com/contact
- group: design
  title: ''
  type: SpectralRules
  url: rules/aerodatabox-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aerodatabox-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aerodatabox-context.jsonld
created: '2025-02-24'
description: AeroDataBox is an affordable aviation and flight data API platform tailored for small and medium businesses, individual developers, researchers, and students. Founded in 2019, the platform provides real-time and historical flight status, aircraft information, airport data, delay statistics, and flight alert webhooks through a RESTful API available on RapidAPI and API.Market. AeroDataBox covers global aviation data across airlines, aircraft, airports, and flight operations.
examples:
- key_count: 26
  name: Aerodatabox Aircraft Contract Example
  slug: aerodatabox-aircraft-contract-example
- key_count: 6
  name: Aerodatabox Aircraft Contract Paged Collection Contract Example
  slug: aerodatabox-aircraft-contract-paged-collection-contract-example
- key_count: 5
  name: Aerodatabox Aircraft Registration Contract Example
  slug: aerodatabox-aircraft-registration-contract-example
- key_count: 14
  name: Aerodatabox Airport Contract Example
  slug: aerodatabox-airport-contract-example
- key_count: 5
  name: Aerodatabox Airport Delay Contract Example
  slug: aerodatabox-airport-delay-contract-example
- key_count: 4
  name: Aerodatabox Airport Distance Time Contract Example
  slug: aerodatabox-airport-distance-time-contract-example
- key_count: 4
  name: Aerodatabox Airport Feed Service Status Contract Example
  slug: aerodatabox-airport-feed-service-status-contract-example
- key_count: 2
  name: Aerodatabox Airport Fids Contract Example
  slug: aerodatabox-airport-fids-contract-example
- key_count: 11
  name: Aerodatabox Airport Flight Contract Example
  slug: aerodatabox-airport-flight-contract-example
- key_count: 2
  name: Aerodatabox Airport Local Time Contract Example
  slug: aerodatabox-airport-local-time-contract-example
- key_count: 6
  name: Aerodatabox Airport Urls Contract Example
  slug: aerodatabox-airport-urls-contract-example
- key_count: 2
  name: Aerodatabox Angle Example
  slug: aerodatabox-angle-example
- key_count: 2
  name: Aerodatabox Azimuth Example
  slug: aerodatabox-azimuth-example
- key_count: 2
  name: Aerodatabox Continent Contract Example
  slug: aerodatabox-continent-contract-example
- key_count: 2
  name: Aerodatabox Country Contract Example
  slug: aerodatabox-country-contract-example
- key_count: 2
  name: Aerodatabox Create Web Hook Subscription Example
  slug: aerodatabox-create-web-hook-subscription-example
- key_count: 1
  name: Aerodatabox Daily Route Stat Contract Example
  slug: aerodatabox-daily-route-stat-contract-example
- key_count: 3
  name: Aerodatabox Daily Route Stat Record Contract Example
  slug: aerodatabox-daily-route-stat-record-contract-example
- key_count: 2
  name: Aerodatabox Date Time Contract Example
  slug: aerodatabox-date-time-contract-example
- key_count: 4
  name: Aerodatabox Delay Bracket Contract Example
  slug: aerodatabox-delay-bracket-contract-example
- key_count: 5
  name: Aerodatabox Distance Example
  slug: aerodatabox-distance-example
- key_count: 2
  name: Aerodatabox Distance Flight Plan Unit Contract Example
  slug: aerodatabox-distance-flight-plan-unit-contract-example
- key_count: 1
  name: Aerodatabox Error Contract Example
  slug: aerodatabox-error-contract-example
- key_count: 4
  name: Aerodatabox Faa Ladd Aircraft Status Contract Example
  slug: aerodatabox-faa-ladd-aircraft-status-contract-example
- key_count: 4
  name: Aerodatabox Feed Service Status Contract Example
  slug: aerodatabox-feed-service-status-contract-example
- key_count: 4
  name: Aerodatabox Flight Aircraft Contract Example
  slug: aerodatabox-flight-aircraft-contract-example
- key_count: 3
  name: Aerodatabox Flight Airline Contract Example
  slug: aerodatabox-flight-airline-contract-example
- key_count: 11
  name: Aerodatabox Flight Airport Movement Contract Example
  slug: aerodatabox-flight-airport-movement-contract-example
- key_count: 5
  name: Aerodatabox Flight Batch Delay Contract Example
  slug: aerodatabox-flight-batch-delay-contract-example
- key_count: 13
  name: Aerodatabox Flight Contract Example
  slug: aerodatabox-flight-contract-example
- key_count: 2
  name: Aerodatabox Flight Data General Availability Contract Example
  slug: aerodatabox-flight-data-general-availability-contract-example
- key_count: 9
  name: Aerodatabox Flight Delay Contract Example
  slug: aerodatabox-flight-delay-contract-example
- key_count: 3
  name: Aerodatabox Flight Leg Delay Contract Example
  slug: aerodatabox-flight-leg-delay-contract-example
- key_count: 9
  name: Aerodatabox Flight Location Contract Example
  slug: aerodatabox-flight-location-contract-example
- key_count: 3
  name: Aerodatabox Flight Notification Contract Example
  slug: aerodatabox-flight-notification-contract-example
- key_count: 15
  name: Aerodatabox Flight Notification Item Contract Example
  slug: aerodatabox-flight-notification-item-contract-example
- key_count: 8
  name: Aerodatabox Flight Plan Contract Example
  slug: aerodatabox-flight-plan-contract-example
- key_count: 1
  name: Aerodatabox Flight Search Item Contract Example
  slug: aerodatabox-flight-search-item-contract-example
- key_count: 2
  name: Aerodatabox Geo Coordinates Contract Example
  slug: aerodatabox-geo-coordinates-contract-example
- key_count: 3
  name: Aerodatabox Geo Coordinates Contract Listing Airport Contract Search Result Collection Contract Example
  slug: aerodatabox-geo-coordinates-contract-listing-airport-contract-search-result-collection-contract-example
- key_count: 6
  name: Aerodatabox Getaircraft Example
  slug: aerodatabox-getaircraft-example
- key_count: 6
  name: Aerodatabox Getaircraftimagebyregistration Example
  slug: aerodatabox-getaircraftimagebyregistration-example
- key_count: 6
  name: Aerodatabox Getaircraftregistrations Example
  slug: aerodatabox-getaircraftregistrations-example
- key_count: 6
  name: Aerodatabox Getairlinefleet Example
  slug: aerodatabox-getairlinefleet-example
- key_count: 6
  name: Aerodatabox Getairport Example
  slug: aerodatabox-getairport-example
- key_count: 6
  name: Aerodatabox Getairportdelay Delayscurrent Example
  slug: aerodatabox-getairportdelay-delayscurrent-example
- key_count: 6
  name: Aerodatabox Getairportdelay Delayshistorical Example
  slug: aerodatabox-getairportdelay-delayshistorical-example
- key_count: 6
  name: Aerodatabox Getairportdelays Example
  slug: aerodatabox-getairportdelays-example
- key_count: 6
  name: Aerodatabox Getairportdistancetime Example
  slug: aerodatabox-getairportdistancetime-example
- key_count: 6
  name: Aerodatabox Getairportfeedstatus Example
  slug: aerodatabox-getairportfeedstatus-example
- key_count: 6
  name: Aerodatabox Getairportflights Example
  slug: aerodatabox-getairportflights-example
- key_count: 6
  name: Aerodatabox Getairportflightsrelative Example
  slug: aerodatabox-getairportflightsrelative-example
- key_count: 6
  name: Aerodatabox Getairportlocaltime Example
  slug: aerodatabox-getairportlocaltime-example
- key_count: 6
  name: Aerodatabox Getairportrunways Example
  slug: aerodatabox-getairportrunways-example
- key_count: 6
  name: Aerodatabox Getairportsolartime Solartimecurrent Example
  slug: aerodatabox-getairportsolartime-solartimecurrent-example
- key_count: 6
  name: Aerodatabox Getairportsolartime Solartimespecificdate Example
  slug: aerodatabox-getairportsolartime-solartimespecificdate-example
- key_count: 6
  name: Aerodatabox Getallaircraft Example
  slug: aerodatabox-getallaircraft-example
- key_count: 6
  name: Aerodatabox Getbalance Example
  slug: aerodatabox-getbalance-example
- key_count: 6
  name: Aerodatabox Getfaaladdaircraftstatus Example
  slug: aerodatabox-getfaaladdaircraftstatus-example
- key_count: 6
  name: Aerodatabox Getfeedairports Example
  slug: aerodatabox-getfeedairports-example
- key_count: 6
  name: Aerodatabox Getfeedservicestatus Example
  slug: aerodatabox-getfeedservicestatus-example
- key_count: 6
  name: Aerodatabox Getflight Flightnearest Example
  slug: aerodatabox-getflight-flightnearest-example
- key_count: 6
  name: Aerodatabox Getflight Flightonspecificdate Example
  slug: aerodatabox-getflight-flightonspecificdate-example
- key_count: 6
  name: Aerodatabox Getflightdates Flightdatesall Example
  slug: aerodatabox-getflightdates-flightdatesall-example
- key_count: 6
  name: Aerodatabox Getflightdates Flightdatesinrange Example
  slug: aerodatabox-getflightdates-flightdatesinrange-example
- key_count: 6
  name: Aerodatabox Getflightdelays Example
  slug: aerodatabox-getflightdelays-example
- key_count: 6
  name: Aerodatabox Getflighthistory Flighthistory Example
  slug: aerodatabox-getflighthistory-flighthistory-example
- key_count: 6
  name: Aerodatabox Getglobaldelays Globaldelaysatspecificdate Example
  slug: aerodatabox-getglobaldelays-globaldelaysatspecificdate-example
- key_count: 6
  name: Aerodatabox Getglobaldelays Globaldelayscurent Example
  slug: aerodatabox-getglobaldelays-globaldelayscurent-example
- key_count: 6
  name: Aerodatabox Getroutedailystatistics Routesdailatspecificdate Example
  slug: aerodatabox-getroutedailystatistics-routesdailatspecificdate-example
- key_count: 6
  name: Aerodatabox Getroutedailystatistics Routesdailycurrent Example
  slug: aerodatabox-getroutedailystatistics-routesdailycurrent-example
- key_count: 6
  name: Aerodatabox Getwebhook Example
  slug: aerodatabox-getwebhook-example
- key_count: 6
  name: Aerodatabox Getwebhooklist Example
  slug: aerodatabox-getwebhooklist-example
- key_count: 9
  name: Aerodatabox Listing Airport Contract Example
  slug: aerodatabox-listing-airport-contract-example
- key_count: 2
  name: Aerodatabox Percentile Bracket Contract Example
  slug: aerodatabox-percentile-bracket-contract-example
- key_count: 3
  name: Aerodatabox Pressure Example
  slug: aerodatabox-pressure-example
- key_count: 6
  name: Aerodatabox Refillbalance Example
  slug: aerodatabox-refillbalance-example
- key_count: 6
  name: Aerodatabox Refreshwebhook Example
  slug: aerodatabox-refreshwebhook-example
- key_count: 7
  name: Aerodatabox Resource Contract Example
  slug: aerodatabox-resource-contract-example
- key_count: 9
  name: Aerodatabox Runway Contract Example
  slug: aerodatabox-runway-contract-example
- key_count: 6
  name: Aerodatabox Searchaircraftbyterm Example
  slug: aerodatabox-searchaircraftbyterm-example
- key_count: 6
  name: Aerodatabox Searchairportbyterm Example
  slug: aerodatabox-searchairportbyterm-example
- key_count: 6
  name: Aerodatabox Searchairportsbyipgeolocation Example
  slug: aerodatabox-searchairportsbyipgeolocation-example
- key_count: 6
  name: Aerodatabox Searchairportsbylocation Example
  slug: aerodatabox-searchairportsbylocation-example
- key_count: 6
  name: Aerodatabox Searchflightsbyterm Example
  slug: aerodatabox-searchflightsbyterm-example
- key_count: 13
  name: Aerodatabox Solar State Contract Example
  slug: aerodatabox-solar-state-contract-example
- key_count: 4
  name: Aerodatabox Speed Example
  slug: aerodatabox-speed-example
- key_count: 2
  name: Aerodatabox Speed Flight Plan Unit Contract Example
  slug: aerodatabox-speed-flight-plan-unit-contract-example
- key_count: 3
  name: Aerodatabox String Aircraft Contract Search Result Collection Contract Example
  slug: aerodatabox-string-aircraft-contract-search-result-collection-contract-example
- key_count: 2
  name: Aerodatabox String Collection Contract Example
  slug: aerodatabox-string-collection-contract-example
- key_count: 3
  name: Aerodatabox String Flight Search Item Contract Search Result Collection Contract Example
  slug: aerodatabox-string-flight-search-item-contract-search-result-collection-contract-example
- key_count: 3
  name: Aerodatabox String Listing Airport Contract Search Result Collection Contract Example
  slug: aerodatabox-string-listing-airport-contract-search-result-collection-contract-example
- key_count: 2
  name: Aerodatabox Subscriber Contract Example
  slug: aerodatabox-subscriber-contract-example
- key_count: 6
  name: Aerodatabox Subscribewebhook Example
  slug: aerodatabox-subscribewebhook-example
- key_count: 3
  name: Aerodatabox Subscription Balance Contract Example
  slug: aerodatabox-subscription-balance-contract-example
- key_count: 9
  name: Aerodatabox Subscription Contract Example
  slug: aerodatabox-subscription-contract-example
- key_count: 2
  name: Aerodatabox Subscription Subject Contract Example
  slug: aerodatabox-subscription-subject-contract-example
- key_count: 1
  name: Aerodatabox Subscriptions Balance Refill Request Contract Example
  slug: aerodatabox-subscriptions-balance-refill-request-contract-example
- key_count: 6
  name: Aerodatabox Unsubscribewebhook Example
  slug: aerodatabox-unsubscribewebhook-example
features:
- description: Live flight tracking with departure and arrival times, current status, and delay information for flights worldwide.
  name: Real-Time Flight Status
- description: Flight Information Display System data showing all departures and arrivals at any airport for a given time window.
  name: FIDS Airport Departures and Arrivals
- description: Lookup aircraft by tail number, registration, or ICAO24 hex code with fleet data, registration history, and images.
  name: Aircraft Search and Profiles
- description: Find airports by geographic coordinates, IP address geolocation, or free-text search with runway data included.
  name: Airport Search by Location
- description: Current and historical delay data for airports and specific flight numbers enabling trend analysis and SLA monitoring.
  name: Flight Delay Statistics
- description: Push notification subscriptions for real-time flight status changes, supporting event-driven application architectures.
  name: Webhook Flight Alerts
- description: FAA Limiting Aircraft Data Displayed (LADD) status lookup to determine if an aircraft is opted out of public tracking.
  name: FAA LADD Status
- description: Sunrise, sunset, and solar position data for any airport and date, useful for scheduling and operations planning.
  name: Solar Time Calculations
- description: Daily route statistics for airports showing which routes operate and their frequency.
  name: Route Statistics
finops:
- name: Aerodatabox Finops
  service_category: Aviation Data
  slug: aerodatabox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aerodatabox.png
integrations:
- description: Available on RapidAPI Hub with interactive API playground and usage metering for easy developer onboarding.
  name: RapidAPI
- description: Available on API.Market marketplace with official OpenAPI v3 specifications for download and code generation.
  name: API.Market
- description: Integrates with any webhook-capable endpoint for real-time flight status push notifications.
  name: Webhook Endpoints
json_schemas:
- name: AircraftContractPagedCollectionContract
  property_count: 6
  slug: aerodatabox-aircraft-contract-paged-collection-contract
- name: AircraftContract
  property_count: 26
  slug: aerodatabox-aircraft-contract
- name: AircraftRegistrationContract
  property_count: 5
  slug: aerodatabox-aircraft-registration-contract
- name: AircraftSearchByEnum
  property_count: 0
  slug: aerodatabox-aircraft-search-by-enum
- name: AircraftContract
  property_count: 26
  slug: aerodatabox-aircraftcontract
- name: AircraftContractPagedCollectionContract
  property_count: 6
  slug: aerodatabox-aircraftcontractpagedcollectioncontract
- name: AircraftRegistrationContract
  property_count: 5
  slug: aerodatabox-aircraftregistrationcontract
- name: AircraftSearchByEnum
  property_count: 0
  slug: aerodatabox-aircraftsearchbyenum
- name: AirportCodesByEnum
  property_count: 0
  slug: aerodatabox-airport-codes-by-enum
- name: AirportContract
  property_count: 14
  slug: aerodatabox-airport-contract
- name: AirportDelayContract
  property_count: 5
  slug: aerodatabox-airport-delay-contract
- name: AirportDistanceTimeContract
  property_count: 4
  slug: aerodatabox-airport-distance-time-contract
- name: AirportFeedServiceStatusContract
  property_count: 4
  slug: aerodatabox-airport-feed-service-status-contract
- name: AirportFidsContract
  property_count: 2
  slug: aerodatabox-airport-fids-contract
- name: AirportFlightContract
  property_count: 11
  slug: aerodatabox-airport-flight-contract
- name: AirportLocalTimeContract
  property_count: 2
  slug: aerodatabox-airport-local-time-contract
- name: AirportUrlsContract
  property_count: 6
  slug: aerodatabox-airport-urls-contract
- name: AirportCodesByEnum
  property_count: 0
  slug: aerodatabox-airportcodesbyenum
- name: AirportContract
  property_count: 14
  slug: aerodatabox-airportcontract
- name: AirportDelayContract
  property_count: 5
  slug: aerodatabox-airportdelaycontract
- name: AirportDistanceTimeContract
  property_count: 4
  slug: aerodatabox-airportdistancetimecontract
- name: AirportFeedServiceStatusContract
  property_count: 4
  slug: aerodatabox-airportfeedservicestatuscontract
- name: AirportFidsContract
  property_count: 2
  slug: aerodatabox-airportfidscontract
- name: AirportFlightContract
  property_count: 11
  slug: aerodatabox-airportflightcontract
- name: AirportLocalTimeContract
  property_count: 2
  slug: aerodatabox-airportlocaltimecontract
- name: AirportUrlsContract
  property_count: 6
  slug: aerodatabox-airporturlscontract
- name: Angle
  property_count: 2
  slug: aerodatabox-angle
- name: Azimuth
  property_count: 2
  slug: aerodatabox-azimuth
- name: CodeshareStatus
  property_count: 0
  slug: aerodatabox-codeshare-status
- name: CodeshareStatus
  property_count: 0
  slug: aerodatabox-codesharestatus
- name: ContinentContract
  property_count: 2
  slug: aerodatabox-continent-contract
- name: ContinentContract
  property_count: 2
  slug: aerodatabox-continentcontract
- name: CountryContract
  property_count: 2
  slug: aerodatabox-country-contract
- name: CountryContract
  property_count: 2
  slug: aerodatabox-countrycontract
- name: CreateWebHookSubscription
  property_count: 2
  slug: aerodatabox-create-web-hook-subscription
- name: CreateWebHookSubscription
  property_count: 2
  slug: aerodatabox-createwebhooksubscription
- name: DailyRouteStatContract
  property_count: 1
  slug: aerodatabox-daily-route-stat-contract
- name: DailyRouteStatRecordContract
  property_count: 3
  slug: aerodatabox-daily-route-stat-record-contract
- name: DailyRouteStatContract
  property_count: 1
  slug: aerodatabox-dailyroutestatcontract
- name: DailyRouteStatRecordContract
  property_count: 3
  slug: aerodatabox-dailyroutestatrecordcontract
- name: DateTimeContract
  property_count: 2
  slug: aerodatabox-date-time-contract
- name: DateTimeContract
  property_count: 2
  slug: aerodatabox-datetimecontract
- name: DayTime
  property_count: 0
  slug: aerodatabox-day-time
- name: DayTime
  property_count: 0
  slug: aerodatabox-daytime
- name: DelayBracketContract
  property_count: 4
  slug: aerodatabox-delay-bracket-contract
- name: DelayBracketContract
  property_count: 4
  slug: aerodatabox-delaybracketcontract
- name: DistanceFlightPlanUnitContract
  property_count: 2
  slug: aerodatabox-distance-flight-plan-unit-contract
- name: Distance
  property_count: 5
  slug: aerodatabox-distance
- name: DistanceFlightPlanUnitContract
  property_count: 2
  slug: aerodatabox-distanceflightplanunitcontract
- name: EngineType
  property_count: 0
  slug: aerodatabox-engine-type
- name: EngineType
  property_count: 0
  slug: aerodatabox-enginetype
- name: ErrorContract
  property_count: 1
  slug: aerodatabox-error-contract
- name: ErrorContract
  property_count: 1
  slug: aerodatabox-errorcontract
- name: FaaLaddAircraftStatusContract
  property_count: 4
  slug: aerodatabox-faa-ladd-aircraft-status-contract
- name: FaaLaddAircraftStatusContract
  property_count: 4
  slug: aerodatabox-faaladdaircraftstatuscontract
- name: FeedServiceEnum
  property_count: 0
  slug: aerodatabox-feed-service-enum
- name: FeedServiceStatusContract
  property_count: 4
  slug: aerodatabox-feed-service-status-contract
- name: FeedServiceStatus
  property_count: 0
  slug: aerodatabox-feed-service-status
- name: FeedServiceEnum
  property_count: 0
  slug: aerodatabox-feedserviceenum
- name: FeedServiceStatus
  property_count: 0
  slug: aerodatabox-feedservicestatus
- name: FeedServiceStatusContract
  property_count: 4
  slug: aerodatabox-feedservicestatuscontract
- name: FlightAircraftContract
  property_count: 4
  slug: aerodatabox-flight-aircraft-contract
- name: FlightAirlineContract
  property_count: 3
  slug: aerodatabox-flight-airline-contract
- name: FlightAirportMovementContract
  property_count: 11
  slug: aerodatabox-flight-airport-movement-contract
- name: FlightAirportMovementQualityEnum
  property_count: 0
  slug: aerodatabox-flight-airport-movement-quality-enum
- name: FlightBatchDelayContract
  property_count: 5
  slug: aerodatabox-flight-batch-delay-contract
- name: FlightContract
  property_count: 13
  slug: aerodatabox-flight-contract
- name: FlightDataGeneralAvailabilityContract
  property_count: 2
  slug: aerodatabox-flight-data-general-availability-contract
- name: FlightDelayContract
  property_count: 9
  slug: aerodatabox-flight-delay-contract
- name: FlightDirection
  property_count: 0
  slug: aerodatabox-flight-direction
- name: FlightLegDelayContract
  property_count: 3
  slug: aerodatabox-flight-leg-delay-contract
- name: FlightLocationContract
  property_count: 9
  slug: aerodatabox-flight-location-contract
- name: FlightNotificationContract
  property_count: 3
  slug: aerodatabox-flight-notification-contract
- name: FlightNotificationItemContract
  property_count: 15
  slug: aerodatabox-flight-notification-item-contract
- name: FlightPlanContract
  property_count: 8
  slug: aerodatabox-flight-plan-contract
- name: FlightPlanStatus
  property_count: 0
  slug: aerodatabox-flight-plan-status
- name: FlightRules
  property_count: 0
  slug: aerodatabox-flight-rules
- name: FlightSearchByEnum
  property_count: 0
  slug: aerodatabox-flight-search-by-enum
- name: FlightSearchItemContract
  property_count: 1
  slug: aerodatabox-flight-search-item-contract
- name: FlightStatus
  property_count: 0
  slug: aerodatabox-flight-status
- name: FlightType
  property_count: 0
  slug: aerodatabox-flight-type
- name: FlightAircraftContract
  property_count: 4
  slug: aerodatabox-flightaircraftcontract
- name: FlightAirlineContract
  property_count: 3
  slug: aerodatabox-flightairlinecontract
- name: FlightAirportMovementContract
  property_count: 11
  slug: aerodatabox-flightairportmovementcontract
- name: FlightAirportMovementQualityEnum
  property_count: 0
  slug: aerodatabox-flightairportmovementqualityenum
- name: FlightBatchDelayContract
  property_count: 5
  slug: aerodatabox-flightbatchdelaycontract
- name: FlightContract
  property_count: 13
  slug: aerodatabox-flightcontract
- name: FlightDataGeneralAvailabilityContract
  property_count: 2
  slug: aerodatabox-flightdatageneralavailabilitycontract
- name: FlightDelayContract
  property_count: 9
  slug: aerodatabox-flightdelaycontract
- name: FlightDirection
  property_count: 0
  slug: aerodatabox-flightdirection
- name: FlightLegDelayContract
  property_count: 3
  slug: aerodatabox-flightlegdelaycontract
- name: FlightLocationContract
  property_count: 9
  slug: aerodatabox-flightlocationcontract
- name: FlightNotificationContract
  property_count: 3
  slug: aerodatabox-flightnotificationcontract
- name: FlightNotificationItemContract
  property_count: 15
  slug: aerodatabox-flightnotificationitemcontract
- name: FlightPlanContract
  property_count: 8
  slug: aerodatabox-flightplancontract
- name: FlightPlanStatus
  property_count: 0
  slug: aerodatabox-flightplanstatus
- name: FlightRules
  property_count: 0
  slug: aerodatabox-flightrules
- name: FlightSearchByEnum
  property_count: 0
  slug: aerodatabox-flightsearchbyenum
- name: FlightSearchItemContract
  property_count: 1
  slug: aerodatabox-flightsearchitemcontract
- name: FlightStatus
  property_count: 0
  slug: aerodatabox-flightstatus
- name: FlightType
  property_count: 0
  slug: aerodatabox-flighttype
- name: GeoCoordinatesContractListingAirportContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-geo-coordinates-contract-listing-airport-contract-search-result-collection-contract
- name: GeoCoordinatesContract
  property_count: 2
  slug: aerodatabox-geo-coordinates-contract
- name: GeoCoordinatesContract
  property_count: 2
  slug: aerodatabox-geocoordinatescontract
- name: GeoCoordinatesContractListingAirportContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-geocoordinatescontractlistingairportcontractsearchresultcoll
- name: LicenseType
  property_count: 0
  slug: aerodatabox-license-type
- name: LicenseType
  property_count: 0
  slug: aerodatabox-licensetype
- name: ListingAirportContract
  property_count: 9
  slug: aerodatabox-listing-airport-contract
- name: ListingAirportContract
  property_count: 9
  slug: aerodatabox-listingairportcontract
- name: ModelFlightTimeEnum
  property_count: 0
  slug: aerodatabox-model-flight-time-enum
- name: ModelFlightTimeEnum
  property_count: 0
  slug: aerodatabox-modelflighttimeenum
- name: PercentileBracketContract
  property_count: 2
  slug: aerodatabox-percentile-bracket-contract
- name: PercentileBracketContract
  property_count: 2
  slug: aerodatabox-percentilebracketcontract
- name: Pressure
  property_count: 3
  slug: aerodatabox-pressure
- name: ResourceContract
  property_count: 7
  slug: aerodatabox-resource-contract
- name: ResourceContract
  property_count: 7
  slug: aerodatabox-resourcecontract
- name: RunwayContract
  property_count: 9
  slug: aerodatabox-runway-contract
- name: RunwayContract
  property_count: 9
  slug: aerodatabox-runwaycontract
- name: SolarStateContract
  property_count: 13
  slug: aerodatabox-solar-state-contract
- name: SolarStateContract
  property_count: 13
  slug: aerodatabox-solarstatecontract
- name: SpeedFlightPlanUnitContract
  property_count: 2
  slug: aerodatabox-speed-flight-plan-unit-contract
- name: Speed
  property_count: 4
  slug: aerodatabox-speed
- name: SpeedFlightPlanUnitContract
  property_count: 2
  slug: aerodatabox-speedflightplanunitcontract
- name: StatisticClass
  property_count: 0
  slug: aerodatabox-statistic-class
- name: StatisticClass
  property_count: 0
  slug: aerodatabox-statisticclass
- name: StringAircraftContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-string-aircraft-contract-search-result-collection-contract
- name: StringCollectionContract
  property_count: 2
  slug: aerodatabox-string-collection-contract
- name: StringFlightSearchItemContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-string-flight-search-item-contract-search-result-collection-contract
- name: StringListingAirportContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-string-listing-airport-contract-search-result-collection-contract
- name: StringAircraftContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-stringaircraftcontractsearchresultcollectioncontract
- name: StringCollectionContract
  property_count: 2
  slug: aerodatabox-stringcollectioncontract
- name: StringFlightSearchItemContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-stringflightsearchitemcontractsearchresultcollectioncontract
- name: StringListingAirportContractSearchResultCollectionContract
  property_count: 3
  slug: aerodatabox-stringlistingairportcontractsearchresultcollectioncontract
- name: SubscriberContract
  property_count: 2
  slug: aerodatabox-subscriber-contract
- name: SubscriberContract
  property_count: 2
  slug: aerodatabox-subscribercontract
- name: SubscriptionBalanceContract
  property_count: 3
  slug: aerodatabox-subscription-balance-contract
- name: SubscriptionBillingType
  property_count: 0
  slug: aerodatabox-subscription-billing-type
- name: SubscriptionContract
  property_count: 9
  slug: aerodatabox-subscription-contract
- name: SubscriptionSubjectContract
  property_count: 2
  slug: aerodatabox-subscription-subject-contract
- name: SubscriptionSubjectType
  property_count: 0
  slug: aerodatabox-subscription-subject-type
- name: SubscriptionBalanceContract
  property_count: 3
  slug: aerodatabox-subscriptionbalancecontract
- name: SubscriptionBillingType
  property_count: 0
  slug: aerodatabox-subscriptionbillingtype
- name: SubscriptionContract
  property_count: 9
  slug: aerodatabox-subscriptioncontract
- name: SubscriptionsBalanceRefillRequestContract
  property_count: 1
  slug: aerodatabox-subscriptions-balance-refill-request-contract
- name: SubscriptionsBalanceRefillRequestContract
  property_count: 1
  slug: aerodatabox-subscriptionsbalancerefillrequestcontract
- name: SubscriptionSubjectContract
  property_count: 2
  slug: aerodatabox-subscriptionsubjectcontract
- name: SubscriptionSubjectType
  property_count: 0
  slug: aerodatabox-subscriptionsubjecttype
- name: SurfaceType
  property_count: 0
  slug: aerodatabox-surface-type
- name: SurfaceType
  property_count: 0
  slug: aerodatabox-surfacetype
json_structures:
- name: Aerodatabox Aircraft Contract Paged Collection Contract Structure
  property_count: 6
  slug: aerodatabox-aircraft-contract-paged-collection-contract-structure
- name: Aerodatabox Aircraft Contract Structure
  property_count: 26
  slug: aerodatabox-aircraft-contract-structure
- name: Aerodatabox Aircraft Registration Contract Structure
  property_count: 5
  slug: aerodatabox-aircraft-registration-contract-structure
- name: Aerodatabox Aircraft Search By Enum Structure
  property_count: 0
  slug: aerodatabox-aircraft-search-by-enum-structure
- name: Aerodatabox Airport Codes By Enum Structure
  property_count: 0
  slug: aerodatabox-airport-codes-by-enum-structure
- name: Aerodatabox Airport Contract Structure
  property_count: 14
  slug: aerodatabox-airport-contract-structure
- name: Aerodatabox Airport Delay Contract Structure
  property_count: 5
  slug: aerodatabox-airport-delay-contract-structure
- name: Aerodatabox Airport Distance Time Contract Structure
  property_count: 4
  slug: aerodatabox-airport-distance-time-contract-structure
- name: Aerodatabox Airport Feed Service Status Contract Structure
  property_count: 4
  slug: aerodatabox-airport-feed-service-status-contract-structure
- name: Aerodatabox Airport Fids Contract Structure
  property_count: 2
  slug: aerodatabox-airport-fids-contract-structure
- name: Aerodatabox Airport Flight Contract Structure
  property_count: 11
  slug: aerodatabox-airport-flight-contract-structure
- name: Aerodatabox Airport Local Time Contract Structure
  property_count: 2
  slug: aerodatabox-airport-local-time-contract-structure
- name: Aerodatabox Airport Urls Contract Structure
  property_count: 6
  slug: aerodatabox-airport-urls-contract-structure
- name: Aerodatabox Angle Structure
  property_count: 2
  slug: aerodatabox-angle-structure
- name: Aerodatabox Azimuth Structure
  property_count: 2
  slug: aerodatabox-azimuth-structure
- name: Aerodatabox Codeshare Status Structure
  property_count: 0
  slug: aerodatabox-codeshare-status-structure
- name: Aerodatabox Continent Contract Structure
  property_count: 2
  slug: aerodatabox-continent-contract-structure
- name: Aerodatabox Country Contract Structure
  property_count: 2
  slug: aerodatabox-country-contract-structure
- name: Aerodatabox Create Web Hook Subscription Structure
  property_count: 2
  slug: aerodatabox-create-web-hook-subscription-structure
- name: Aerodatabox Daily Route Stat Contract Structure
  property_count: 1
  slug: aerodatabox-daily-route-stat-contract-structure
- name: Aerodatabox Daily Route Stat Record Contract Structure
  property_count: 3
  slug: aerodatabox-daily-route-stat-record-contract-structure
- name: Aerodatabox Date Time Contract Structure
  property_count: 2
  slug: aerodatabox-date-time-contract-structure
- name: Aerodatabox Day Time Structure
  property_count: 0
  slug: aerodatabox-day-time-structure
- name: Aerodatabox Delay Bracket Contract Structure
  property_count: 4
  slug: aerodatabox-delay-bracket-contract-structure
- name: Aerodatabox Distance Flight Plan Unit Contract Structure
  property_count: 2
  slug: aerodatabox-distance-flight-plan-unit-contract-structure
- name: Aerodatabox Distance Structure
  property_count: 5
  slug: aerodatabox-distance-structure
- name: Aerodatabox Engine Type Structure
  property_count: 0
  slug: aerodatabox-engine-type-structure
- name: Aerodatabox Error Contract Structure
  property_count: 1
  slug: aerodatabox-error-contract-structure
- name: Aerodatabox Faa Ladd Aircraft Status Contract Structure
  property_count: 4
  slug: aerodatabox-faa-ladd-aircraft-status-contract-structure
- name: Aerodatabox Feed Service Enum Structure
  property_count: 0
  slug: aerodatabox-feed-service-enum-structure
- name: Aerodatabox Feed Service Status Contract Structure
  property_count: 4
  slug: aerodatabox-feed-service-status-contract-structure
- name: Aerodatabox Feed Service Status Structure
  property_count: 0
  slug: aerodatabox-feed-service-status-structure
- name: Aerodatabox Flight Aircraft Contract Structure
  property_count: 4
  slug: aerodatabox-flight-aircraft-contract-structure
- name: Aerodatabox Flight Airline Contract Structure
  property_count: 3
  slug: aerodatabox-flight-airline-contract-structure
- name: Aerodatabox Flight Airport Movement Contract Structure
  property_count: 11
  slug: aerodatabox-flight-airport-movement-contract-structure
- name: Aerodatabox Flight Airport Movement Quality Enum Structure
  property_count: 0
  slug: aerodatabox-flight-airport-movement-quality-enum-structure
- name: Aerodatabox Flight Batch Delay Contract Structure
  property_count: 5
  slug: aerodatabox-flight-batch-delay-contract-structure
- name: Aerodatabox Flight Contract Structure
  property_count: 13
  slug: aerodatabox-flight-contract-structure
- name: Aerodatabox Flight Data General Availability Contract Structure
  property_count: 2
  slug: aerodatabox-flight-data-general-availability-contract-structure
- name: Aerodatabox Flight Delay Contract Structure
  property_count: 9
  slug: aerodatabox-flight-delay-contract-structure
- name: Aerodatabox Flight Direction Structure
  property_count: 0
  slug: aerodatabox-flight-direction-structure
- name: Aerodatabox Flight Leg Delay Contract Structure
  property_count: 3
  slug: aerodatabox-flight-leg-delay-contract-structure
- name: Aerodatabox Flight Location Contract Structure
  property_count: 9
  slug: aerodatabox-flight-location-contract-structure
- name: Aerodatabox Flight Notification Contract Structure
  property_count: 3
  slug: aerodatabox-flight-notification-contract-structure
- name: Aerodatabox Flight Notification Item Contract Structure
  property_count: 15
  slug: aerodatabox-flight-notification-item-contract-structure
- name: Aerodatabox Flight Plan Contract Structure
  property_count: 8
  slug: aerodatabox-flight-plan-contract-structure
- name: Aerodatabox Flight Plan Status Structure
  property_count: 0
  slug: aerodatabox-flight-plan-status-structure
- name: Aerodatabox Flight Rules Structure
  property_count: 0
  slug: aerodatabox-flight-rules-structure
- name: Aerodatabox Flight Search By Enum Structure
  property_count: 0
  slug: aerodatabox-flight-search-by-enum-structure
- name: Aerodatabox Flight Search Item Contract Structure
  property_count: 1
  slug: aerodatabox-flight-search-item-contract-structure
- name: Aerodatabox Flight Status Structure
  property_count: 0
  slug: aerodatabox-flight-status-structure
- name: Aerodatabox Flight Type Structure
  property_count: 0
  slug: aerodatabox-flight-type-structure
- name: Aerodatabox Geo Coordinates Contract Listing Airport Contract Search Result Collection Contract Structure
  property_count: 3
  slug: aerodatabox-geo-coordinates-contract-listing-airport-contract-search-result-collection-contract-structure
- name: Aerodatabox Geo Coordinates Contract Structure
  property_count: 2
  slug: aerodatabox-geo-coordinates-contract-structure
- name: Aerodatabox License Type Structure
  property_count: 0
  slug: aerodatabox-license-type-structure
- name: Aerodatabox Listing Airport Contract Structure
  property_count: 9
  slug: aerodatabox-listing-airport-contract-structure
- name: Aerodatabox Model Flight Time Enum Structure
  property_count: 0
  slug: aerodatabox-model-flight-time-enum-structure
- name: Aerodatabox Percentile Bracket Contract Structure
  property_count: 2
  slug: aerodatabox-percentile-bracket-contract-structure
- name: Aerodatabox Pressure Structure
  property_count: 3
  slug: aerodatabox-pressure-structure
- name: Aerodatabox Resource Contract Structure
  property_count: 7
  slug: aerodatabox-resource-contract-structure
- name: Aerodatabox Runway Contract Structure
  property_count: 9
  slug: aerodatabox-runway-contract-structure
- name: Aerodatabox Solar State Contract Structure
  property_count: 13
  slug: aerodatabox-solar-state-contract-structure
- name: Aerodatabox Speed Flight Plan Unit Contract Structure
  property_count: 2
  slug: aerodatabox-speed-flight-plan-unit-contract-structure
- name: Aerodatabox Speed Structure
  property_count: 4
  slug: aerodatabox-speed-structure
- name: Aerodatabox Statistic Class Structure
  property_count: 0
  slug: aerodatabox-statistic-class-structure
- name: Aerodatabox String Aircraft Contract Search Result Collection Contract Structure
  property_count: 3
  slug: aerodatabox-string-aircraft-contract-search-result-collection-contract-structure
- name: Aerodatabox String Collection Contract Structure
  property_count: 2
  slug: aerodatabox-string-collection-contract-structure
- name: Aerodatabox String Flight Search Item Contract Search Result Collection Contract Structure
  property_count: 3
  slug: aerodatabox-string-flight-search-item-contract-search-result-collection-contract-structure
- name: Aerodatabox String Listing Airport Contract Search Result Collection Contract Structure
  property_count: 3
  slug: aerodatabox-string-listing-airport-contract-search-result-collection-contract-structure
- name: Aerodatabox Structure
  property_count: 0
  slug: aerodatabox-structure
- name: Aerodatabox Subscriber Contract Structure
  property_count: 2
  slug: aerodatabox-subscriber-contract-structure
- name: Aerodatabox Subscription Balance Contract Structure
  property_count: 3
  slug: aerodatabox-subscription-balance-contract-structure
- name: Aerodatabox Subscription Billing Type Structure
  property_count: 0
  slug: aerodatabox-subscription-billing-type-structure
- name: Aerodatabox Subscription Contract Structure
  property_count: 9
  slug: aerodatabox-subscription-contract-structure
- name: Aerodatabox Subscription Subject Contract Structure
  property_count: 2
  slug: aerodatabox-subscription-subject-contract-structure
- name: Aerodatabox Subscription Subject Type Structure
  property_count: 0
  slug: aerodatabox-subscription-subject-type-structure
- name: Aerodatabox Subscriptions Balance Refill Request Contract Structure
  property_count: 1
  slug: aerodatabox-subscriptions-balance-refill-request-contract-structure
- name: Aerodatabox Surface Type Structure
  property_count: 0
  slug: aerodatabox-surface-type-structure
jsonld:
- class_count: 80
  name: Aerodatabox Context
  property_count: 200
  slug: aerodatabox-context
layout: provider
modified: '2026-05-19'
name: AeroDataBox
nav: Providers
network: true
overview: 'AeroDataBox publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Aircraft API API, Airport API API, Flight Alert API API, and 5 more. Tagged areas include Aviation, Flights, Aerospace, Flight Data, and Airport Data.


  The AeroDataBox catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AeroDataBox''s developer surface includes documentation, developer portal, pricing, and 10 more developer resources.'
plans:
- name: Aerodatabox Plans Pricing
  plan_count: 1
  slug: aerodatabox-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Aerodatabox Rate Limits
  slug: aerodatabox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AeroDataBox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aerodatabox-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: AeroDataBox API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 18
  slug: aerodatabox-spectral-rules
score:
  band: developing
  composite: 40.0
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 63.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/screenshots/aerodatabox-2026-06-20T165508.png
security:
- kind: domain-security
  name: Aerodatabox Domain Security
  slug: aerodatabox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aerodatabox
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
use_cases:
- description: Build consumer or enterprise flight tracking apps using real-time status data for specific flights or all flights at an airport.
  name: Flight Tracking Applications
- description: Send flight status alerts to travelers by integrating webhook subscriptions for departure and arrival updates.
  name: Travel Booking Notifications
- description: Monitor airport performance, delay patterns, and route activity for operations research and capacity planning.
  name: Airport Operations Intelligence
- description: Analyze fleet composition, route networks, and on-time performance for competitive intelligence and market research.
  name: Airline Research and Analysis
- description: Access historical delay and route statistics for data-driven journalism and research on aviation trends.
  name: Aviation Data Journalism
- description: Track aircraft registrations and history for aviation finance, insurance, and asset management applications.
  name: Aircraft Valuation and Tracking
- description: Integrate airport search, local time, and solar data into travel planning applications to enhance itinerary building.
  name: Trip Planning Tools
website: https://www.aerodatabox.com/
---
