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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transit Agentic Access
  operation_count: 7
  slug: transit-agentic-access
  summary_line: 7 operations
api_count: 8
apis:
- description: Deep-link URL scheme for launching the Transit mobile app from partner apps and websites. Supports directions and nearby-routes hand-offs without requiring an API key.
  name: Transit URL Scheme
  slug: url-scheme
- description: Service alerts and disruptions
  name: Transit Alerts API
  slug: transit-alerts-api
- description: Real-time and scheduled transit departure information
  name: Transit Departures API
  slug: transit-departures-api
- description: Shared bikes, scooters, and carshares
  name: Transit Mobility API
  slug: transit-mobility-api
- description: Transit network and agency data
  name: Transit Networks API
  slug: transit-networks-api
- description: Route information and schedules
  name: Transit Routes API
  slug: transit-routes-api
- description: Stop and station information
  name: Transit Stops API
  slug: transit-stops-api
- description: Multimodal trip planning and results
  name: Transit Trips API
  slug: transit-trips-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Transit Alerts API
  slug: open-transit-alerts-api
- collection_type: open
  name: Transit Alerts Departures API
  slug: open-transit-departures-api
- collection_type: open
  name: Transit Alerts Mobility API
  slug: open-transit-mobility-api
- collection_type: open
  name: Transit Alerts Networks API
  slug: open-transit-networks-api
- collection_type: open
  name: Transit Alerts Routes API
  slug: open-transit-routes-api
- collection_type: open
  name: Transit Alerts Stops API
  slug: open-transit-stops-api
- collection_type: open
  name: Transit Alerts Trips API
  slug: open-transit-trips-api
- collection_type: open
  name: Transit API
  slug: open-transit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://transitapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transitapp.com/apis
- group: docs
  title: ''
  type: APIDocumentation
  url: https://api-doc.transitapp.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TransitApp
- group: company
  title: ''
  type: Blog
  url: https://blog.transitapp.com/
- group: company
  title: ''
  type: BlogFeed
  url: https://blog.transitapp.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://help.transitapp.com/
- group: company
  title: ''
  type: Careers
  url: https://transitapp.com/careers
- group: company
  title: ''
  type: Press
  url: https://transitapp.com/press
- group: commercial
  title: ''
  type: Pricing
  url: https://transitapp.com/apis
- group: start
  title: ''
  type: Signup
  url: https://docs.google.com/forms/d/e/1FAIpQLScZbUsb1G1gRzIkEQo4FuuAbfzQbldTvu6-62j_pSRWPtKZiA/viewform
- group: operate
  title: ''
  type: ContactSales
  url: mailto:partners+website@transit.app
- group: operate
  title: ''
  type: ContactGeneral
  url: mailto:info@transit.app
created: '2025-05-02'
description: Transit ("The world's most accurate transit app") provides real-time public transit data, multimodal trip planning, and shared mobility across 1,000+ cities including New York, Paris, London, and Montreal, partnering with 180+ transit agencies. The platform aggregates trains, buses, bikes, scooters, and carshares with crowdsourced GO real-time signals, ships a freemium partner API (5 calls/minute, 1,500 calls/month), and monetizes consumers via the Transit Royale subscription ($2/month billed annually).
examples:
- key_count: 2
  name: Transit Get Stop Departures Example
  slug: transit-get-stop-departures-example
- key_count: 2
  name: Transit Plan Trip Example
  slug: transit-plan-trip-example
finops:
- name: Transit Finops
  service_category: Mobility + Transit Data
  slug: transit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transit.png
json_schemas:
- name: Transit Departure
  property_count: 7
  slug: transit-departure
- name: Transit Stop
  property_count: 6
  slug: transit-stop
json_structures:
- name: Transit Stop Structure
  property_count: 0
  slug: transit-stop-structure
jsonld:
- class_count: 32
  name: Transit Context
  property_count: 0
  slug: transit-context
layout: provider
modified: '2026-05-23'
name: Transit
nav: Providers
network: true
overview: 'Transit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Departures API, Mobility API, and 4 more. Tagged areas include Public Transit, Real-Time, Trip Planning, Multi-Modal, and GTFS.


  The Transit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Transit''s developer surface includes authentication, documentation, GitHub presence, engineering blog, support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Transit Plans Pricing
  plan_count: 3
  slug: transit-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Transit Rate Limits
  slug: transit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Transit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: transit-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Transit API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 5
  slug: transit-rules
score:
  band: developing
  composite: 50.7
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 13.6
    contract_quality: 70.2
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 36.8
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transit/refs/heads/main/screenshots/transit-2026-06-20T195544.png
security:
- kind: authentication
  name: Transit Authentication
  slug: transit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transit Domain Security
  slug: transit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transit
tags:
- Public Transit
- Real-Time
- Trip Planning
- Multi-Modal
- GTFS
- GOFS
- Mobility
- Shared Mobility
website: https://transitapp.com/
---
