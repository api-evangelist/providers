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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Airlabs Agentic Access
  operation_count: 12
  slug: airlabs-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: Track live aircraft positions worldwide with latitude, longitude, altitude, speed, direction, and flight identifiers. Supports filtering by bounding box, airline, airport, aircraft registration, and f
  name: Airlabs Real-Time Flights API
  slug: airlabs-real-time-flights-api
- description: 'Retrieve departure and arrival schedules for any airport including flight status, terminal and gate information, estimated and actual times, and delay information. Free tier limited to 50 results per '
  name: Airlabs Airport Schedules API
  slug: airlabs-airport-schedules-api
- description: Look up detailed information for a specific flight by IATA or ICAO code, combining schedule data, real-time position, and aircraft specifications into a single response for the closest matching flight
  name: Airlabs Flight Information API
  slug: airlabs-flight-information-api
- description: Query flights exceeding a specified delay threshold (minimum 30 minutes) filtered by departure or arrival direction, designed for airport transfer services and flight delay compensation use cases. Sup
  name: Airlabs Flight Delays API
  slug: airlabs-flight-delays-api
- description: Access a comprehensive global airport database with IATA and ICAO codes, coordinates, elevation, runway count, timezone, city and country data, and social media profiles. Filter by IATA, ICAO, city, o
  name: Airlabs Airports Database API
  slug: airlabs-airports-database-api
- description: Look up airline information including IATA and ICAO codes, callsign, country, fleet size, average fleet age, safety data including accidents and crashes over the past 5 years, and IOSA certification s
  name: Airlabs Airlines Database API
  slug: airlabs-airlines-database-api
- description: 'Query airline routes between airports with departure and arrival times in local and UTC, operating days of week, terminal information, flight duration, and the last aircraft type used. Supports up to '
  name: Airlabs Routes Database API
  slug: airlabs-routes-database-api
- description: 'Access global aircraft fleet data with registration numbers, ICAO hex codes, manufacturer serial numbers, aircraft type, engine count and type, build year, age, and current airline operator. Optional '
  name: Airlabs Aircraft Fleet Database API
  slug: airlabs-aircraft-fleet-database-api
- description: 'Retrieve city data including IATA city codes, coordinates, country, timezone, population, and multilingual names. Enables destination mapping and grouping airports into city clusters independently of '
  name: Airlabs Cities Database API
  slug: airlabs-cities-database-api
- description: Find airports and cities closest to given latitude and longitude coordinates within a specified kilometer radius, sorted by distance. Used for nearest-airport lookup and smart assistant applications.
  name: Airlabs NearBy Airports API
  slug: airlabs-nearby-airports-api
- description: Autocomplete airport, city, and country search queries in any language and spelling variant. Returns matched airports, cities, and countries with IATA codes, coordinates, timezone, and popularity metr
  name: Airlabs Name Suggestion API
  slug: airlabs-name-suggestion-api
- description: Airline reference data
  name: Airlabs Airlines API
  slug: airlabs-airlines-api
- description: Airport reference data
  name: Airlabs Airports API
  slug: airlabs-airports-api
- description: Flight monitoring
  name: Airlabs Alert API
  slug: airlabs-alert-api
- description: City reference data
  name: Airlabs Cities API
  slug: airlabs-cities-api
- description: Currently delayed flights
  name: Airlabs Delays API
  slug: airlabs-delays-api
- description: Aircraft fleet records
  name: Airlabs Fleets API
  slug: airlabs-fleets-api
- description: Single flight information
  name: Airlabs Flight API
  slug: airlabs-flight-api
- description: Real-time flight positions
  name: Airlabs Flights API
  slug: airlabs-flights-api
- description: Geographic airport lookup
  name: Airlabs Nearby API
  slug: airlabs-nearby-api
- description: Route reference data
  name: Airlabs Routes API
  slug: airlabs-routes-api
- description: Airport departures and arrivals
  name: Airlabs Schedules API
  slug: airlabs-schedules-api
- description: Autocomplete and search
  name: Airlabs Suggest API
  slug: airlabs-suggest-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AirLabs Aviation Data Airlines API
  slug: open-airlabs-airlines-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Airports API
  slug: open-airlabs-airports-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Alert API
  slug: open-airlabs-alert-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Cities API
  slug: open-airlabs-cities-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Delays API
  slug: open-airlabs-delays-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Fleets API
  slug: open-airlabs-fleets-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Flight API
  slug: open-airlabs-flight-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Flights API
  slug: open-airlabs-flights-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Nearby API
  slug: open-airlabs-nearby-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Routes API
  slug: open-airlabs-routes-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Schedules API
  slug: open-airlabs-schedules-api
- collection_type: open
  name: AirLabs Aviation Data Airlines Suggest API
  slug: open-airlabs-suggest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airlabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airlabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airlabs-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://airlabs.co/docs
- group: commercial
  title: ''
  type: Plans
  url: https://airlabs.co/#Pricing
- group: docs
  title: ''
  type: Documentation
  url: https://airlabs.co/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airlabs.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airlabs.co/terms
- group: operate
  title: ''
  type: Status
  url: https://airlabs.co/status
created: '2026-06-13'
description: Aviation data REST API providing real-time flight status, schedules, routes, airports, airlines, aircraft data, and delays from 250+ airlines and 3,500+ airports worldwide. Built by Data Products LTD, the platform covers approximately 7,300 active flights at any given time.
examples:
- key_count: 2
  name: Airlines Response
  slug: airlines-response
- key_count: 2
  name: Airports Response
  slug: airports-response
- key_count: 2
  name: Flights Response
  slug: flights-response
- key_count: 2
  name: Nearby Response
  slug: nearby-response
- key_count: 2
  name: Schedules Response
  slug: schedules-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airlabs.png
json_schemas:
- name: Airline
  property_count: 14
  slug: airline
- name: Airport
  property_count: 16
  slug: airport
- name: FleetAircraft
  property_count: 21
  slug: fleet-aircraft
- name: Flight
  property_count: 22
  slug: flight
- name: Route
  property_count: 20
  slug: route
- name: Schedule
  property_count: 34
  slug: schedule
jsonld:
- class_count: 0
  name: context Context
  property_count: 36
  slug: context
layout: provider
modified: '2026-06-13'
name: Airlabs
nav: Providers
network: true
overview: 'Airlabs publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Airlines API, Airports API, Alert API, and 9 more. Tagged areas include Aviation, Flights, Airlines, Airports, and Flight Tracking.


  The Airlabs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Airlabs'' developer surface includes authentication, documentation, status page, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 20
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Airlabs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airlabs-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airlabs/refs/heads/main/screenshots/airlabs-2026-06-20T171424.png
security:
- kind: authentication
  name: Airlabs Authentication
  slug: airlabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airlabs Domain Security
  slug: airlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airlabs
tags:
- Aviation
- Flights
- Airlines
- Airports
- Flight Tracking
- Flight Status
- Real-Time Data
---
