---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flightradar24 Agentic Access
  operation_count: 16
  slug: flightradar24-agentic-access
  summary_line: 16 operations
api_count: 16
apis:
- description: 'Returns a lightweight snapshot of real-time aircraft positions worldwide, including latitude, longitude, altitude, speed, heading, callsign, and aircraft registration. Optimised for mapping use cases '
  name: Live Flights Light
  slug: live-flights-light
- description: Returns complete real-time aircraft flight movement records including latitude, longitude, speed, altitude, and heading alongside enriched flight information such as origin and destination airports, c
  name: Live Flights Full
  slug: live-flights-full
- description: Provides historical aircraft positional data using Unix timestamp ranges. Returns lightweight position records (latitude, longitude, altitude, speed, heading, callsign, registration) for past flights.
  name: Historical Flights Light
  slug: historical-flights-light
- description: Returns full historical aircraft flight movement records for a given time window, combining positional data with enriched flight metadata including origin, destination, callsign, registration, aircraf
  name: Historical Flights Full
  slug: historical-flights-full
- description: Returns synopses of individual flights including key event timings and locations such as actual takeoff and landing times, departure and arrival airports, and primary flight, aircraft, and operator id
  name: Flight Summaries
  slug: flight-summaries
- description: Returns the full positional track of a specific flight identified by its FR24 flight ID. Provides a time-ordered sequence of latitude, longitude, altitude, speed, and heading records spanning the enti
  name: Flight Tracks
  slug: flight-tracks
- description: Returns detailed reference data for airports worldwide, including full airport name, IATA and ICAO codes, geographic coordinates, elevation, country, city, state, and timezone. Supports lookup by IATA
  name: Airports
  slug: airports
- description: Returns reference data for airlines including airline name, IATA code, and ICAO code. Supports lookup by identifier. Useful for resolving callsign prefixes and operator codes present in flight data in
  name: Airlines
  slug: airlines
- description: Reference data for airlines
  name: Flightradar24 Airlines API
  slug: flightradar24-airlines-api
- description: Reference data for airports worldwide
  name: Flightradar24 Airports API
  slug: flightradar24-airports-api
- description: Synopses of individual flights including event timings and key identifiers
  name: Flightradar24 Flight Summary API
  slug: flightradar24-flight-summary-api
- description: Full positional track of a specific flight by FR24 flight ID
  name: Flightradar24 Flight Tracks API
  slug: flightradar24-flight-tracks-api
- description: Historical flight event data (takeoff, landing, gate movements, airspace transitions)
  name: Flightradar24 Historic Events API
  slug: flightradar24-historic-events-api
- description: Historical aircraft position data (back to May 11, 2016)
  name: Flightradar24 Historic Positions API
  slug: flightradar24-historic-positions-api
- description: Real-time aircraft position data
  name: Flightradar24 Live Positions API
  slug: flightradar24-live-positions-api
- description: API account usage and credit consumption
  name: Flightradar24 Usage API
  slug: flightradar24-usage-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flightradar24-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightradar24-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flightradar24-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://fr24api.flightradar24.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fr24api.flightradar24.com/docs/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://fr24api.flightradar24.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://fr24api.flightradar24.com/docs/authentication
- group: start
  title: ''
  type: Sandbox
  url: https://fr24api.flightradar24.com/docs/sandbox-environment
- group: commercial
  title: ''
  type: Pricing
  url: https://fr24api.flightradar24.com/subscriptions-and-credits
- group: operate
  title: ''
  type: FAQ
  url: https://fr24api.flightradar24.com/docs/faq
- group: company
  title: ''
  type: Blog
  url: https://www.flightradar24.com/blog/b2b/
- group: operate
  title: ''
  type: Support
  url: https://support.fr24.com/support/solutions/folders/3000022922
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flightradar24
- group: build
  title: ''
  type: SDKPython
  url: https://fr24api.flightradar24.com/docs/sdk/python
- group: build
  title: ''
  type: SDKJavaScript
  url: https://github.com/Flightradar24/fr24api-sdk-js
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Flightradar24/fr24api-mcp
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/flightradar24/main/openapi/openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/flightradar24/main/json-schema/flight-position-light.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/flightradar24/main/json-schema/flight-summary-full.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/flightradar24/main/json-schema/airport-full.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/flightradar24/main/json-ld/context.jsonld
created: '2026-06-13'
description: Flightradar24 is the world's most popular real-time flight tracking platform, monitoring over 250,000 daily flights using data from a global network of ADS-B, MLAT, and radar receivers. The FR24 API provides developers with programmatic access to live aircraft positions, historical flight data, flight summaries, and reference data for airports and airlines. The credit-based subscription API uses Bearer token authentication and is available at https://fr24api.flightradar24.com/api with three tiers — Explorer, Essential, and Advanced — covering hobby projects through high-volume commercial applications.
examples:
- key_count: 11
  name: Airport Full
  slug: airport-full
- key_count: 1
  name: Flight Summary Full
  slug: flight-summary-full
- key_count: 1
  name: Flight Tracks
  slug: flight-tracks
- key_count: 1
  name: Live Positions Light
  slug: live-positions-light
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightradar24.png
json_schemas:
- name: AirportFull
  property_count: 11
  slug: airport-full
- name: FlightPositionLight
  property_count: 12
  slug: flight-position-light
- name: FlightSummaryFull
  property_count: 25
  slug: flight-summary-full
jsonld:
- class_count: 62
  name: context Context
  property_count: 6
  slug: context
layout: provider
mcp_servers:
- description: ''
  name: fr24api-mcp
  slug: fr24api-mcp
modified: '2026-06-13'
name: Flightradar24
nav: Providers
network: true
overview: 'Flightradar24 publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Airlines API, Airports API, Flight Summary API, and 5 more. Tagged areas include Aviation, Flight Tracking, Real-Time, Aircraft, and Airports.


  The Flightradar24 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Flightradar24''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, pricing, FAQ, and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 47
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Flightradar24 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: flightradar24-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.3
    developer_ergonomics: 60.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flightradar24/refs/heads/main/screenshots/flightradar24-2026-06-20T181313.png
security:
- kind: authentication
  name: Flightradar24 Authentication
  slug: flightradar24-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flightradar24 Domain Security
  slug: flightradar24-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flightradar24
tags:
- Aviation
- Flight Tracking
- Real-Time
- Aircraft
- Airports
- Airlines
- ADS-B
- Historical Data
website: https://fr24api.flightradar24.com/
---
