---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flightlabs Agentic Access
  operation_count: 19
  slug: flightlabs-agentic-access
  summary_line: 19 operations
api_count: 7
apis:
- description: Aircraft and aircraft type reference data endpoints
  name: FlightLabs Aircraft API
  slug: flightlabs-aircraft-api
- description: Airline reference data endpoints
  name: FlightLabs Airlines API
  slug: flightlabs-airlines-api
- description: Airport reference data endpoints
  name: FlightLabs Airports API
  slug: flightlabs-airports-api
- description: Real-time and historical flight data endpoints
  name: FlightLabs Flights API
  slug: flightlabs-flights-api
- description: Countries and cities reference data endpoints
  name: FlightLabs Geography API
  slug: flightlabs-geography-api
- description: Flight pricing and fare data endpoints
  name: FlightLabs Pricing API
  slug: flightlabs-pricing-api
- description: Airline route data endpoints
  name: FlightLabs Routes API
  slug: flightlabs-routes-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FlightLabs Aircraft API
  slug: open-flightlabs-aircraft-api
- collection_type: open
  name: FlightLabs Aircraft Airlines API
  slug: open-flightlabs-airlines-api
- collection_type: open
  name: FlightLabs Aircraft Airports API
  slug: open-flightlabs-airports-api
- collection_type: open
  name: FlightLabs Aircraft Flights API
  slug: open-flightlabs-flights-api
- collection_type: open
  name: FlightLabs Aircraft Geography API
  slug: open-flightlabs-geography-api
- collection_type: open
  name: FlightLabs Aircraft Pricing API
  slug: open-flightlabs-pricing-api
- collection_type: open
  name: FlightLabs Aircraft Routes API
  slug: open-flightlabs-routes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flightlabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightlabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flightlabs-authentication.yml
created: '2026-06-13'
description: Aviation data REST API providing real-time and historical flight information, airline schedules, aircraft data, airport details, and global flight tracking with worldwide airline coverage. Operated by Zyla Labs, FlightLabs offers 16+ endpoints covering live flights, flight delays, future predictions, airline routes, and flight pricing.
examples:
- key_count: 2
  name: Airlines
  slug: airlines
- key_count: 2
  name: Airports
  slug: airports
- key_count: 2
  name: Real Time Flights
  slug: real-time-flights
- key_count: 2
  name: Routes
  slug: routes
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightlabs.png
json_schemas:
- name: AirlineData
  property_count: 15
  slug: airline
- name: AirportData
  property_count: 17
  slug: airport
- name: FlightData
  property_count: 22
  slug: flight
jsonld:
- class_count: 39
  name: Flightlabs Context
  property_count: 5
  slug: flightlabs
layout: provider
modified: '2026-06-13'
name: FlightLabs
nav: Providers
network: true
overview: 'FlightLabs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Aircraft API, Airlines API, Airports API, and 4 more. Tagged areas include Aviation, Flights, Airlines, Airports, and Flight Tracking.


  The FlightLabs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FlightLabs'' developer surface includes authentication and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 13
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: FlightLabs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: flightlabs-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flightlabs/refs/heads/main/screenshots/flightlabs-2026-06-20T181312.png
security:
- kind: authentication
  name: Flightlabs Authentication
  slug: flightlabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flightlabs Domain Security
  slug: flightlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flightlabs
tags:
- Aviation
- Flights
- Airlines
- Airports
- Flight Tracking
- Travel
- Real-Time Data
---
