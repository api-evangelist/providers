---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Valhalla Agentic Access
  operation_count: 12
  slug: valhalla-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 11
apis:
- description: The Expansion API from Valhalla — 1 operation(s) for expansion.
  name: Valhalla Expansion API
  slug: valhalla-expansion-api
- description: The Height API from Valhalla — 1 operation(s) for height.
  name: Valhalla Height API
  slug: valhalla-height-api
- description: The Isochrone API from Valhalla — 1 operation(s) for isochrone.
  name: Valhalla Isochrone API
  slug: valhalla-isochrone-api
- description: The Locate API from Valhalla — 1 operation(s) for locate.
  name: Valhalla Locate API
  slug: valhalla-locate-api
- description: The Optimized Route API from Valhalla — 1 operation(s) for optimized route.
  name: Valhalla Optimized Route API
  slug: valhalla-optimized-route-api
- description: The Route API from Valhalla — 1 operation(s) for route.
  name: Valhalla Route API
  slug: valhalla-route-api
- description: The Sources To Targets API from Valhalla — 1 operation(s) for sources to targets.
  name: Valhalla Sources To Targets API
  slug: valhalla-sources-to-targets-api
- description: The Status API from Valhalla — 1 operation(s) for status.
  name: Valhalla Status API
  slug: valhalla-status-api
- description: The Tile API from Valhalla — 1 operation(s) for tile.
  name: Valhalla Tile API
  slug: valhalla-tile-api
- description: The Trace Attributes API from Valhalla — 1 operation(s) for trace attributes.
  name: Valhalla Trace Attributes API
  slug: valhalla-trace-attributes-api
- description: The Trace Route API from Valhalla — 1 operation(s) for trace route.
  name: Valhalla Trace Route API
  slug: valhalla-trace-route-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valhalla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valhalla-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/valhalla/valhalla
- group: docs
  title: ''
  type: Documentation
  url: https://valhalla.github.io/valhalla/
- group: docs
  title: ''
  type: OpenAPI
  url: https://valhalla.github.io/valhalla/api/openapi/
- group: start
  title: ''
  type: DemoServer
  url: https://valhalla.openstreetmap.de/
- group: commercial
  title: ''
  type: License
  url: https://github.com/valhalla/valhalla/blob/master/LICENSE.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/valhalla/refs/heads/main/rate-limits/openstreetmap-de.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/valhalla/refs/heads/main/plans/open-source.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/valhalla/refs/heads/main/finops/self-hosted.yml
created: '2026-06-13'
description: Valhalla is an open-source routing engine and library suite for OpenStreetMap data. It provides turn-by-turn navigation, isochrone computation, time-distance matrix analysis, map matching, elevation sampling, optimized routing (TSP), and graph expansion via a REST API. Valhalla supports multiple travel modes including auto, bicycle, pedestrian, transit, truck, motorcycle, and motor scooter. It uses a tiled hierarchical data structure for efficient offline routing and regional extracts, with dynamic costing via a plugin architecture.
examples:
- key_count: 3
  name: Height
  slug: height
- key_count: 3
  name: Isochrone
  slug: isochrone
- key_count: 3
  name: Route
  slug: route
- key_count: 3
  name: Sources To Targets
  slug: sources-to-targets
finops:
- name: Self Hosted
  service_category: ''
  slug: self-hosted
image: https://valhalla.github.io/valhalla/images/valhalla.png
json_schemas:
- name: IsochroneRequest
  property_count: 11
  slug: isochrone-request
- name: Location
  property_count: 13
  slug: location
- name: MatrixRequest
  property_count: 10
  slug: matrix-request
- name: RouteRequest
  property_count: 15
  slug: route-request
jsonld:
- class_count: 0
  name: Valhalla Context
  property_count: 56
  slug: valhalla-context
layout: provider
modified: '2026-06-13'
name: Valhalla
nav: Providers
network: true
overview: 'Valhalla publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Expansion API, Height API, Isochrone API, and 8 more. Tagged areas include Routing, Navigation, OpenStreetMap, Mapping, and Geospatial.


  The Valhalla catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Valhalla''s developer surface includes GitHub presence, documentation, and 8 more developer resources.'
plans:
- name: Open Source
  plan_count: 2
  slug: open-source
random_paper: 27
rate_limits:
- limit_count: 5
  name: Openstreetmap De
  slug: openstreetmap-de
rules:
- name: Valhalla API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valhalla-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.3
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.3
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Valhalla Domain Security
  slug: valhalla-domain-security
  summary_line: TLSv1.3
slug: valhalla
tags:
- Routing
- Navigation
- OpenStreetMap
- Mapping
- Geospatial
- Directions
- Isochrones
- Travel
- Transportation
- Open Source
---
