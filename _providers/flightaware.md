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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Flightaware Agentic Access
  operation_count: 58
  slug: flightaware-agentic-access
  summary_line: 58 operations · 6 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'AeroAPI is FlightAware''s query-based REST API for accessing aviation data on demand. It exposes 60+ endpoints across flights, airports, operators, alerts, history, and Foresight predictive analytics, '
  name: FlightAware AeroAPI
  slug: aeroapi
- description: Firehose is FlightAware's real-time streaming feed of global flight data, delivering ADS-B, radar, and ATC-derived position, status, and event messages over a persistent TLS connection for enterprise-
  name: FlightAware Firehose
  slug: firehose
- description: The airports API from FlightAware — 17 operation(s) for airports.
  name: FlightAware airports API
  slug: flightaware-airports-api
- description: AeroAPI alerting can be used to configure and receive real-time alerts on key flight events. With customizable alerting offered by our alert endpoints, AeroAPI empowers users to selectively pick vario
  name: FlightAware alerts API
  slug: flightaware-alerts-api
- description: The flights API from FlightAware — 11 operation(s) for flights.
  name: FlightAware flights API
  slug: flightaware-flights-api
- description: 'Foresight endpoints provide access to FlightAware''s Foresight predictive models and predictions for key events. Our advanced machine learning (ML) models identify key influencing factors for a flight '
  name: FlightAware foresight API
  slug: flightaware-foresight-api
- description: The history API from FlightAware — 5 operation(s) for history.
  name: FlightAware history API
  slug: flightaware-history-api
- description: The miscellaneous API from FlightAware — 6 operation(s) for miscellaneous.
  name: FlightAware miscellaneous API
  slug: flightaware-miscellaneous-api
- description: The operators API from FlightAware — 8 operation(s) for operators.
  name: FlightAware operators API
  slug: flightaware-operators-api
artifact_total: 16
collections:
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Flightaware Rate Limits
  slug: flightaware-rate-limits
score:
  band: developing
  composite: 46.9
  delta: 2.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.6
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.9
  schema_version: 0.5
  scored_at: '2026-07-27'
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
