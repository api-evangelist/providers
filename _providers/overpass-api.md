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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Read-only API for querying OpenStreetMap data. Supports retrieval of nodes, ways, relations, and areas using the Overpass Query Language (QL) or XML syntax, with output in JSON, XML, CSV, or custom fo
  name: Overpass API
  slug: overpass-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/drolbr/Overpass-API/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/drolbr/Overpass-API/releases
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


  Overpass API''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 60.5
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
