---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Geofabrik Agentic Access
  operation_count: 5
  slug: geofabrik-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Managed Overpass API service providing a reliable, low-latency alternative to the public OpenStreetMap Overpass servers for running complex OSM data queries. Available in Small (10k req/mo), Medium (1
  name: Geofabrik Overpass API
  slug: overpass-api
- description: Managed geocoding service powered by Nominatim and Photon, converting addresses to coordinates and vice versa using OpenStreetMap data. Photon supports auto-completion and typo tolerance. Available in
  name: Geofabrik Geocoding API
  slug: geocoding-api
- description: Managed routing service powered by OSRM and GraphHopper for route calculation, turn-by-turn instructions, distance matrix computation, isochrones, and map matching. OSRM supports car routing and matri
  name: Geofabrik Routing API
  slug: routing-api
- description: Direct download of OSM data extract files
  name: Geofabrik Downloads API
  slug: geofabrik-downloads-api
- description: Machine-readable index of all available extracts
  name: Geofabrik Index API
  slug: geofabrik-index-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Geofabrik Download Downloads API
  slug: open-geofabrik-downloads-api
- collection_type: open
  name: Geofabrik Download Downloads Index API
  slug: open-geofabrik-index-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geofabrik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geofabrik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.geofabrik.de
- group: docs
  title: ''
  type: Documentation
  url: https://download.geofabrik.de/technical.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/geofabrik
- group: company
  title: ''
  type: Blog
  url: https://blog.geofabrik.de
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geofabrik.de/data/overpass-api.html
- group: other
  title: ''
  type: X
  url: https://twitter.com/geofabrik
- group: company
  title: ''
  type: Mastodon
  url: https://en.osm.town/@geofabrik
- group: commercial
  title: ''
  type: Plans
  url: plans/geofabrik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geofabrik-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geofabrik-finops.yml
created: '2026-06-13'
description: Geofabrik is a geographic data processing company specializing in OpenStreetMap data extraction, processing, and distribution. Their download REST API provides daily-updated OSM extracts in PBF, shapefile, and GeoPackage formats for every region of the world, alongside paid managed services for geocoding (Nominatim/Photon), routing (OSRM/GraphHopper), and the Overpass API for advanced OSM queries. All public downloads are free under the ODbL 1.0 license.
examples:
- key_count: 2
  name: Geofabrik Extract Index Example
  slug: geofabrik-extract-index-example
finops:
- name: Geofabrik Finops
  service_category: ''
  slug: geofabrik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geofabrik.png
json_schemas:
- name: Geofabrik Extract Index
  property_count: 2
  slug: geofabrik-extract-index
jsonld:
- class_count: 30
  name: Geofabrik Context
  property_count: 12
  slug: geofabrik-context
layout: provider
modified: '2026-06-13'
name: Geofabrik
nav: Providers
network: true
overview: 'Geofabrik publishes 2 APIs on the [APIs.io](https://apis.io/) network: Downloads API and Index API. Tagged areas include OpenStreetMap, Geospatial, GIS, Maps, and Downloads.


  The Geofabrik catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Geofabrik''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Geofabrik Plans Pricing
  plan_count: 5
  slug: geofabrik-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Geofabrik Rate Limits
  slug: geofabrik-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Geofabrik API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: geofabrik-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geofabrik/refs/heads/main/screenshots/geofabrik-2026-06-20T181750.png
security:
- kind: domain-security
  name: Geofabrik Domain Security
  slug: geofabrik-domain-security
  summary_line: TLSv1.3
slug: geofabrik
tags:
- OpenStreetMap
- Geospatial
- GIS
- Maps
- Downloads
- OSM
- Routing
- Geocoding
website: https://www.geofabrik.de
---
