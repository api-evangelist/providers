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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Openrouteservice Agentic Access
  operation_count: 17
  slug: openrouteservice-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 16
apis:
- description: Calculates areas of reachability from given locations within specified time or distance ranges, supporting up to 5 locations and 10 intervals, for travel modes including driving, cycling, and walking.
  name: OpenRouteService Isochrones API
  slug: isochrones
- description: Computes one-to-many, many-to-one, and many-to-many time and distance matrices for logistics optimization, supporting up to 3,500 locations per standard request for route planning and fleet management
  name: OpenRouteService Matrix API
  slug: matrix
- description: 'Resolves addresses to geographic coordinates and vice versa using the Pelias geocoding engine, supporting forward geocoding, reverse geocoding, and autocomplete for address normalization and location '
  name: OpenRouteService Geocoding API
  slug: geocoding
- description: Returns elevation data for point or line geometries using SRTM data, supporting up to 2,000 vertices for enriching routes and locations with altitude information.
  name: OpenRouteService Elevation API
  slug: elevation
- description: Solves vehicle routing problems using the VROOM engine, optimizing routes for fleets of up to 3 vehicles and 50 routes, supporting time windows, capacity constraints, and multi-depot scenarios for log
  name: OpenRouteService Optimization API
  slug: optimization
- description: Returns points of interest in the area surrounding a given geometry, supporting search within a 2 km radius for areas up to 50 km2, filtered by category and keyword using OpenStreetMap POI data.
  name: OpenRouteService POI API
  slug: pois
- description: Snaps arbitrary coordinates to the nearest road network nodes, supporting up to 5,000 locations per request, useful for map matching and correcting GPS coordinates to the road network.
  name: OpenRouteService Snapping API
  slug: snapping
- description: Get routing directions for different modes of transport
  name: OpenRouteService Directions API
  slug: openrouteservice-directions-api
- description: Return elevation data for point or line geometries
  name: OpenRouteService Elevation API
  slug: openrouteservice-elevation-api
- description: Resolve addresses to coordinates and vice versa using Pelias engine
  name: OpenRouteService Geocoding API
  slug: openrouteservice-geocoding-api
- description: Service health and status endpoints
  name: OpenRouteService Health API
  slug: openrouteservice-health-api
- description: Obtain areas of reachability from given locations
  name: OpenRouteService Isochrones API
  slug: openrouteservice-isochrones-api
- description: Obtain one-to-many, many-to-one and many-to-many matrices for time and distance
  name: OpenRouteService Matrix API
  slug: openrouteservice-matrix-api
- description: Solve vehicle routing problems using the VROOM engine
  name: OpenRouteService Optimization API
  slug: openrouteservice-optimization-api
- description: Return points of interest using OpenStreetMap data
  name: OpenRouteService POI API
  slug: openrouteservice-poi-api
- description: Snap coordinates to the nearest road network nodes
  name: OpenRouteService Snapping API
  slug: openrouteservice-snapping-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openrouteservice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openrouteservice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openrouteservice-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openrouteservice.org
- group: docs
  title: ''
  type: Documentation
  url: https://giscience.github.io/openrouteservice/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/GIScience
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GIScience/openrouteservice
- group: company
  title: ''
  type: Blog
  url: https://heigit.org/category/openrouteservice/
- group: commercial
  title: ''
  type: Pricing
  url: https://openrouteservice.org/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://ask.openrouteservice.org/c/announcements/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ors_news
- group: operate
  title: ''
  type: Forums
  url: https://ask.openrouteservice.org
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/GIScience/openrouteservice/blob/main/CHANGELOG.md
- group: docs
  title: ''
  type: OpenAPI
  url: https://openrouteservice.org/wp-json/ors
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GIScience/openrouteservice-py
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GIScience/openrouteservice-js
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GIScience/openrouteservice-r
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GIScience/orstools-qgis-plugin
- group: commercial
  title: ''
  type: Plans
  url: plans/openrouteservice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openrouteservice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openrouteservice-finops.yml
created: '2026-06-13'
description: OpenRouteService is a free, open-source geospatial API platform built on OpenStreetMap data, providing routing directions for multiple transport modes, isochrones for reachability analysis, time-distance matrices, geocoding, elevation data, points of interest, and vehicle route optimization for logistics and humanitarian use cases.
examples:
- key_count: 10
  name: Directions Driving Car Request
  slug: directions-driving-car-request
- key_count: 6
  name: Isochrones Request
  slug: isochrones-request
- key_count: 4
  name: Matrix Request
  slug: matrix-request
- key_count: 3
  name: Optimization Request
  slug: optimization-request
- key_count: 5
  name: Pois Request
  slug: pois-request
- key_count: 3
  name: Snapping Request
  slug: snapping-request
finops:
- name: Openrouteservice Finops
  service_category: ''
  slug: openrouteservice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openrouteservice.png
json_schemas:
- name: OpenRouteService Directions Request
  property_count: 23
  slug: openrouteservice-directions-request
- name: OpenRouteService Isochrones Request
  property_count: 13
  slug: openrouteservice-isochrones-request
- name: OpenRouteService Matrix Request
  property_count: 7
  slug: openrouteservice-matrix-request
jsonld:
- class_count: 13
  name: Openrouteservice Context
  property_count: 73
  slug: openrouteservice-context
layout: provider
modified: '2026-06-13'
name: OpenRouteService
nav: Providers
network: true
overview: 'OpenRouteService publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Directions API, Elevation API, Geocoding API, and 6 more. Tagged areas include Routing, Geospatial, Directions, Isochrones, and Matrix.


  The OpenRouteService catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenRouteService''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 16 more developer resources.'
plans:
- name: Openrouteservice Plans Pricing
  plan_count: 4
  slug: openrouteservice-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Openrouteservice Rate Limits
  slug: openrouteservice-rate-limits
rules:
- name: OpenRouteService API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openrouteservice-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openrouteservice/refs/heads/main/screenshots/openrouteservice-2026-06-20T191029.png
security:
- kind: authentication
  name: Openrouteservice Authentication
  slug: openrouteservice-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openrouteservice Domain Security
  slug: openrouteservice-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openrouteservice
tags:
- Routing
- Geospatial
- Directions
- Isochrones
- Matrix
- Geocoding
- Elevation
- Optimization
- OpenStreetMap
- Navigation
- Logistics
- Humanitarian
website: https://openrouteservice.org
---
