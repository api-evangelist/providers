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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Radar Io Agentic Access
  operation_count: 26
  slug: radar-io-agentic-access
  summary_line: 26 operations · 7 acting
api_count: 9
apis:
- description: Validate and verify addresses.
  name: Radar Addresses API
  slug: radar-io-addresses-api
- description: List and manage geofence and place events.
  name: Radar Events API
  slug: radar-io-events-api
- description: Forward, reverse, and IP geocoding.
  name: Radar Geocoding API
  slug: radar-io-geocoding-api
- description: Create, read, update, and delete geofences.
  name: Radar Geofences API
  slug: radar-io-geofences-api
- description: Distance, matrix, directions, and route matching.
  name: Radar Routing API
  slug: radar-io-routing-api
- description: Address and place autocomplete, place search, and geofence search.
  name: Radar Search API
  slug: radar-io-search-api
- description: Raster and vector map tiles.
  name: Radar Tiles API
  slug: radar-io-tiles-api
- description: Track device location and manage users.
  name: Radar Track API
  slug: radar-io-track-api
- description: Create, update, and list trips for trip tracking.
  name: Radar Trips API
  slug: radar-io-trips-api
artifact_total: 16
collections:
- collection_type: open
  name: Radar API
  slug: open-radar-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radar-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radar-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/radar-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radarlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radarlabs
- group: company
  title: ''
  type: Website
  url: https://radar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://radar.com/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/radar-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/radar-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/radar-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://radar.com/blog
created: '2026-07-01'
description: Radar is a geofencing and maps platform that gives developers a unified location infrastructure - forward and reverse geocoding, IP geocoding, address and place autocomplete, place and geofence search, routing (distance, matrix, directions, and route matching), geofence management, device tracking, events, trips, address verification, and map tiles - all under a single api.radar.io/v1 REST interface.
finops:
- name: Radar Io Finops
  service_category: Location and Mapping
  slug: radar-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radar-io.png
layout: provider
modified: '2026-07-01'
name: Radar
nav: Providers
network: true
overview: 'Radar publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Events API, Geocoding API, and 6 more. Tagged areas include Location, Geocoding, Geofencing, Maps, and Routing.


  Radar''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Radar Io Plans Pricing
  plan_count: 2
  slug: radar-io-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 4
  name: Radar Io Rate Limits
  slug: radar-io-rate-limits
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Radar Io Authentication
  slug: radar-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Radar Io Domain Security
  slug: radar-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: radar-io
tags:
- Location
- Geocoding
- Geofencing
- Maps
- Routing
website: https://radar.com/
---
