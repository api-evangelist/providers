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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Read-only API for querying OpenStreetMap data. Supports retrieval of nodes, ways, relations, and areas using the Overpass Query Language (QL) or XML syntax, with output in JSON, XML, CSV, or custom fo
  name: Overpass API
  slug: overpass-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overpass-api-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.overpass-api.de/overpass-doc/en/
- group: docs
  title: ''
  type: LanguageReference
  url: https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/drolbr/Overpass-API
- group: commercial
  title: ''
  type: License
  url: https://github.com/drolbr/Overpass-API/blob/master/LICENSE
- group: build
  title: ''
  type: InteractiveTool
  url: https://overpass-turbo.eu/
- group: operate
  title: ''
  type: StatusPage
  url: https://overpass-api.de/api/status
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/finops/finops.yml
description: Overpass API is a read-only OpenStreetMap data API that enables querying geographic features including nodes, ways, relations, and tags using the Overpass Query Language (QL). It supports complex spatial queries with filters for bounding boxes, tags, proximity, area containment, and element relationships, making it the primary tool for extracting custom subsets of OSM data programmatically.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://overpass-api.de/img/osm_logo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Overpass API
nav: Providers
network: true
overview: 'Overpass API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OpenStreetMap, Geographic, Spatial, GIS, and Maps.


  The Overpass API catalog on APIs.io includes 1 JSON-LD context.


  Overpass API''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 57
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 18.7
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 21.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/screenshots/overpass-api-2026-06-20T191236.png
security:
- kind: domain-security
  name: Overpass Api Domain Security
  slug: overpass-api-domain-security
  summary_line: TLSv1.3
slug: overpass-api
tags:
- OpenStreetMap
- Geographic
- Spatial
- GIS
- Maps
- Open Data
- Query Language
---
