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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transportapi Agentic Access
  operation_count: 7
  slug: transportapi-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: Real-time and scheduled bus departure and arrival data
  name: TransportAPI Bus Information API
  slug: transportapi-bus-information-api
- description: Multimodal journey planning across Great Britain
  name: TransportAPI Journey Planner API
  slug: transportapi-journey-planner-api
- description: Transport stops, stations, and points of interest
  name: TransportAPI Places API
  slug: transportapi-places-api
- description: Real-time and scheduled rail departure and arrival data
  name: TransportAPI Rail Information API
  slug: transportapi-rail-information-api
artifact_total: 16
collections:
- collection_type: open
  name: TransportAPI
  slug: open-transportapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transportapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transportapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transportapi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transportapi
- group: company
  title: ''
  type: Website
  url: https://www.transportapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.transportapi.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.transportapi.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/transportapi
- group: company
  title: ''
  type: Blog
  url: https://www.transportapi.com/blog/
created: '2025-05-02'
description: TransportAPI is a managed data service provider for UK public transport, offering real-time and scheduled bus, rail, and multimodal transport data via REST and WebSocket APIs to power apps, websites, analytics, and data-mining workflows.
examples:
- key_count: 2
  name: Transportapi Get Bus Stop Live Departures Example
  slug: transportapi-get-bus-stop-live-departures-example
- key_count: 2
  name: Transportapi Plan Journey Example
  slug: transportapi-plan-journey-example
finops:
- name: Transportapi Finops
  service_category: API
  slug: transportapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transportapi.png
json_structures:
- name: Transportapi Departure Structure
  property_count: 0
  slug: transportapi-departure-structure
jsonld:
- class_count: 29
  name: Transportapi Context
  property_count: 0
  slug: transportapi-context
layout: provider
modified: '2026-05-19'
name: TransportAPI
nav: Providers
network: true
overview: 'TransportAPI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bus Information API, Journey Planner API, Places API, and 1 more. Tagged areas include Public Transit, Transport, UK, Real-Time, and Journey Planning.


  The TransportAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TransportAPI''s developer surface includes authentication, documentation, signup flow, GitHub presence, engineering blog, and 4 more developer resources.'
plans:
- name: Transportapi Plans Pricing
  plan_count: 3
  slug: transportapi-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Transportapi Rate Limits
  slug: transportapi-rate-limits
rules:
- name: TransportAPI API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 3
    info: 1
    warn: 4
  slug: transportapi-rules
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transportapi/refs/heads/main/screenshots/transportapi-2026-06-20T195629.png
security:
- kind: authentication
  name: Transportapi Authentication
  slug: transportapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Transportapi Domain Security
  slug: transportapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: transportapi
tags:
- Public Transit
- Transport
- UK
- Real-Time
- Journey Planning
- Bus
- Rail
website: https://www.transportapi.com/
---
