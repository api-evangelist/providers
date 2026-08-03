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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Jawg Maps Agentic Access
  operation_count: 13
  slug: jawg-maps-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 7
apis:
- description: The Isochrone API from Jawg Maps — 1 operation(s) for isochrone.
  name: Jawg Maps Isochrone API
  slug: jawg-maps-isochrone-api
- description: The Matrix API from Jawg Maps — 1 operation(s) for matrix.
  name: Jawg Maps Matrix API
  slug: jawg-maps-matrix-api
- description: The Places API from Jawg Maps — 4 operation(s) for places.
  name: Jawg Maps Places API
  slug: jawg-maps-places-api
- description: The Routing API from Jawg Maps — 2 operation(s) for routing.
  name: Jawg Maps Routing API
  slug: jawg-maps-routing-api
- description: The Static Maps API from Jawg Maps — 1 operation(s) for static maps.
  name: Jawg Maps Static Maps API
  slug: jawg-maps-static-maps-api
- description: The Styles API from Jawg Maps — 2 operation(s) for styles.
  name: Jawg Maps Styles API
  slug: jawg-maps-styles-api
- description: The Tiles API from Jawg Maps — 2 operation(s) for tiles.
  name: Jawg Maps Tiles API
  slug: jawg-maps-tiles-api
artifact_total: 14
collections:
- collection_type: open
  name: Jawg Maps API
  slug: open-jawg-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jawg-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jawg-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jawg-maps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jawg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jawg-maps
- group: company
  title: ''
  type: Website
  url: https://www.jawg.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jawg.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/jawg-maps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jawg-maps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jawg-maps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.jawg.io/feed/
created: '2026-07-01'
description: Jawg is a French location platform delivering customizable vector and raster map tiles, hosted map styles, geocoding and places search, routing, isochrones, distance matrices, and static maps. All surfaces are authenticated with a Jawg access token passed as an access-token query parameter (or header) and are served from tile.jawg.io and api.jawg.io.
finops:
- name: Jawg Maps Finops
  service_category: Maps and Location
  slug: jawg-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jawg-maps.png
layout: provider
modified: '2026-07-01'
name: Jawg Maps
nav: Providers
network: true
overview: 'Jawg Maps publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Isochrone API, Matrix API, Places API, and 4 more. Tagged areas include Maps, Geospatial, Tiles, Geocoding, and Routing.


  Jawg Maps'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Jawg Maps Plans Pricing
  plan_count: 4
  slug: jawg-maps-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 4
  name: Jawg Maps Rate Limits
  slug: jawg-maps-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jawg-maps/refs/heads/main/screenshots/jawg-maps-2026-07-25T223104.png
security:
- kind: authentication
  name: Jawg Maps Authentication
  slug: jawg-maps-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Jawg Maps Domain Security
  slug: jawg-maps-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jawg-maps
tags:
- Maps
- Geospatial
- Tiles
- Geocoding
- Routing
- Location
website: https://www.jawg.io/
---
