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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Flightaware Agentic Access
  operation_count: 58
  slug: flightaware-agentic-access
  summary_line: 58 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'AeroAPI is FlightAware''s query-based REST API for accessing aviation data on demand. It exposes 60+ endpoints across flights, airports, operators, alerts, history, and Foresight predictive analytics, '
  name: FlightAware AeroAPI
  slug: aeroapi
- description: Firehose is FlightAware's real-time streaming feed of global flight data, delivering ADS-B, radar, and ATC-derived position, status, and event messages over a persistent TLS connection for enterprise-
  name: FlightAware Firehose
  slug: firehose
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The airports API from FlightAware — 17 operation(s) for airports.
  name: FlightAware airports API
  slug: flightaware-airports-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: AeroAPI alerting can be used to configure and receive real-time alerts on key flight events. With customizable alerting offered by our alert endpoints, AeroAPI empowers users to selectively pick vario
  name: FlightAware alerts API
  slug: flightaware-alerts-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The flights API from FlightAware — 11 operation(s) for flights.
  name: FlightAware flights API
  slug: flightaware-flights-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: 'Foresight endpoints provide access to FlightAware''s Foresight predictive models and predictions for key events. Our advanced machine learning (ML) models identify key influencing factors for a flight '
  name: FlightAware foresight API
  slug: flightaware-foresight-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The history API from FlightAware — 5 operation(s) for history.
  name: FlightAware history API
  slug: flightaware-history-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The miscellaneous API from FlightAware — 6 operation(s) for miscellaneous.
  name: FlightAware miscellaneous API
  slug: flightaware-miscellaneous-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The operators API from FlightAware — 8 operation(s) for operators.
  name: FlightAware operators API
  slug: flightaware-operators-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aero airports API
  slug: open-flightaware-airports-api
- collection_type: open
  name: Aero airports alerts API
  slug: open-flightaware-alerts-api
- collection_type: open
  name: Aero airports flights API
  slug: open-flightaware-flights-api
- collection_type: open
  name: Aero airports foresight API
  slug: open-flightaware-foresight-api
- collection_type: open
  name: Aero airports history API
  slug: open-flightaware-history-api
- collection_type: open
  name: Aero airports miscellaneous API
  slug: open-flightaware-miscellaneous-api
- collection_type: open
  name: Aero airports operators API
  slug: open-flightaware-operators-api
- collection_type: open
  name: AeroAPI
  slug: open-flightaware
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flightaware-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightaware-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flightaware-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flightaware
- group: company
  title: ''
  type: Website
  url: https://www.flightaware.com/
- group: other
  title: ''
  type: CommercialData
  url: https://www.flightaware.com/commercial/data/
- group: start
  title: ''
  type: AeroAPIPortal
  url: https://www.flightaware.com/aeroapi/portal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flightaware.com/aeroapi/portal/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flightaware.com/commercial/aeroapi/
- group: company
  title: ''
  type: Blog
  url: https://blog.flightaware.com/
- group: operate
  title: ''
  type: Support
  url: https://www.flightaware.com/about/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flightaware.com/about/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flightaware.com/about/termsofuse
- group: build
  title: ''
  type: GitHub
  url: https://github.com/flightaware
created: '2025-02-24'
description: FlightAware is a global flight tracking and data platform that provides real-time flight tracking, mapping, and predictive technology to both individual users and commercial aviation companies. The platform collects data from a variety of sources including air traffic control systems, radar, ADS-B, and satellite data, and exposes that data to developers and commercial customers through its AeroAPI query-based REST API and its Firehose streaming feed.
finops:
- name: Flightaware Finops
  service_category: API
  slug: flightaware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightaware.png
layout: provider
modified: '2026-04-28'
name: FlightAware
nav: Providers
network: true
overview: 'FlightAware publishes 7 APIs on the [APIs.io](https://apis.io/) network, including airports API, alerts API, flights API, and 4 more. Tagged areas include Aviation, Flights, Flight Tracking, Mapping, and Radar.


  FlightAware''s developer surface includes authentication, documentation, pricing, engineering blog, support, GitHub presence, and 8 more developer resources.'
plans:
- name: Flightaware Plans Pricing
  plan_count: 3
  slug: flightaware-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Flightaware Rate Limits
  slug: flightaware-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 59.8
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Flightaware Authentication
  slug: flightaware-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flightaware Domain Security
  slug: flightaware-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: flightaware
tags:
- Aviation
- Flights
- Flight Tracking
- Mapping
- Radar
- Satellites
- Traffic Control
website: https://www.flightaware.com/
---
