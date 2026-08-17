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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opensky Agentic Access
  operation_count: 7
  slug: opensky-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: SQL query interface powered by Trino for accessing the full OpenSky historical dataset including state vectors, raw Mode S messages, ADS-C and MLAT data, and flight records. Available to university-af
  name: OpenSky Network Trino Historical Data API
  slug: opensky-network-trino-historical-data-api
- description: Endpoints for retrieving flight records including arrivals, departures, and flights by aircraft.
  name: OpenSky Network Flights API
  slug: opensky-flights-api
- description: Endpoints for retrieving real-time and historical aircraft state vectors (position, velocity, altitude, etc.).
  name: OpenSky Network State Vectors API
  slug: opensky-state-vectors-api
- description: Endpoints for retrieving aircraft trajectory tracks with detailed waypoint data.
  name: OpenSky Network Tracks API
  slug: opensky-tracks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenSky Network REST Flights API
  slug: open-opensky-flights-api
- collection_type: open
  name: OpenSky Network REST Flights State Vectors API
  slug: open-opensky-state-vectors-api
- collection_type: open
  name: OpenSky Network REST Flights Tracks API
  slug: open-opensky-tracks-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/openskynetwork/opensky-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opensky-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opensky-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opensky-authentication.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/openskynetwork
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openskynetwork/opensky-api
- group: docs
  title: ''
  type: Documentation
  url: https://openskynetwork.github.io/opensky-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opensky-network.org/about/terms-of-use
- group: operate
  title: ''
  type: Status
  url: https://opensky-network.org/network/status
- group: start
  title: ''
  type: Login
  url: https://opensky-network.org/login
- group: start
  title: ''
  type: Register
  url: https://opensky-network.org/register
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/opensky/refs/heads/main/finops/opensky.yml
- group: operate
  title: ''
  type: Contact
  url: https://opensky-network.org/about/contact
- group: operate
  title: ''
  type: Forums
  url: https://community.opensky-network.org
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/openskynetwork
created: '2026-06-13'
description: Open-source flight tracking network with a REST API for accessing real-time and historical ADS-B aircraft state vectors, flight tracks, and airport arrivals and departures. The network is powered by a community of volunteer ADS-B receiver operators and is intended for non-commercial research and educational use.
examples:
- key_count: 2
  name: States All Response
  slug: states-all-response
- key_count: 5
  name: Track Response
  slug: track-response
finops:
- name: Opensky
  service_category: ''
  slug: opensky
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensky.png
json_schemas:
- name: FlightObject
  property_count: 12
  slug: flight-object
- name: StateVectorResponse
  property_count: 2
  slug: state-vector-response
- name: TrackResponse
  property_count: 5
  slug: track-response
jsonld:
- class_count: 4
  name: Opensky Context
  property_count: 33
  slug: opensky-context
layout: provider
modified: '2026-06-13'
name: OpenSky Network
nav: Providers
network: true
overview: 'OpenSky Network publishes 3 APIs on the [APIs.io](https://apis.io/) network: Flights API, State Vectors API, and Tracks API. Tagged areas include Aviation, Flight Tracking, ADS-B, Aircraft, and Airport.


  The OpenSky Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenSky Network''s developer surface includes authentication, GitHub presence, documentation, status page, and 11 more developer resources.'
plans:
- name: Opensky Rest Api
  plan_count: 4
  slug: opensky-rest-api
- name: Opensky Trino Api
  plan_count: 2
  slug: opensky-trino-api
random_paper: 32
rate_limits:
- limit_count: 4
  name: Opensky Rest Api
  slug: opensky-rest-api
- limit_count: 3
  name: Opensky Trino Api
  slug: opensky-trino-api
rules:
- name: OpenSky Network API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: opensky-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 69.2
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Opensky Authentication
  slug: opensky-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opensky Domain Security
  slug: opensky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opensky
tags:
- Aviation
- Flight Tracking
- ADS-B
- Aircraft
- Airport
- Real-Time
- Historical Data
---
