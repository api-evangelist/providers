---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: CDN-backed hosted basemap tile API serving OpenStreetMap-derived vector tiles in MVT format. Provides Style JSON, TileJSON, and ZXY tile endpoints. Free for non-commercial use; commercial use requires
  name: Protomaps Hosted Tile API
  slug: protomaps-hosted-tile-api
- description: Single-binary command-line tool for working with PMTiles archives. Supports show, tile, verify, extract, merge, serve, convert, cluster, upload, and edit operations. Can serve PMTiles as a ZXY tile en
  name: PMTiles CLI
  slug: pmtiles-cli
- description: Daily OpenStreetMap planet builds in PMTiles format available for download and self-hosting. Provides the full planet tileset as well as tools for extracting regional subsets by bounding box or GeoJSO
  name: Protomaps Basemap Downloads
  slug: protomaps-basemap-downloads
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/protomaps/go-pmtiles/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/protomaps/go-pmtiles/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/protomaps/go-pmtiles/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/protomaps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://protomaps.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.protomaps.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/protomaps
- group: company
  title: ''
  type: Blog
  url: https://protomaps.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/sponsors/protomaps
- group: other
  title: ''
  type: X
  url: https://twitter.com/protomaps
- group: commercial
  title: ''
  type: Plans
  url: plans/protomaps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/protomaps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/protomaps-finops.yml
created: 2026-06-13
description: Protomaps is an open-source map system that delivers an interactive map of the world as a single PMTiles file hosted on cloud storage. It provides a hosted vector tile API powered by Cloudflare CDN, plus tools for converting, serving, and delivering map tiles without servers using HTTP range requests. The PMTiles format enables self-hosting on S3, Cloudflare R2, Azure Blob, and Google Cloud Storage at a fraction of the cost of commercial map APIs.
finops:
- name: Protomaps Finops
  service_category: ''
  slug: protomaps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/protomaps.png
jsonld:
- class_count: 10
  name: Protomaps Context
  property_count: 0
  slug: protomaps-context
layout: provider
modified: 2026-06-13
name: Protomaps
nav: Providers
network: true
overview: 'Protomaps publishes 1 API on the [APIs.io](https://apis.io/) network: Hosted Tile API. Tagged areas include Maps, Tiles, Geospatial, PMTiles, and Vector Tiles.


  The Protomaps catalog on APIs.io includes 1 JSON-LD context.


  Protomaps'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Protomaps Plans Pricing
  plan_count: 4
  slug: protomaps-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Protomaps Rate Limits
  slug: protomaps-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 25.0
  previous_composite: 34.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/protomaps/refs/heads/main/screenshots/protomaps-2026-06-20T192223.png
security:
- kind: domain-security
  name: Protomaps Domain Security
  slug: protomaps-domain-security
  summary_line: TLSv1.3 · DMARC
slug: protomaps
tags:
- Maps
- Tiles
- Geospatial
- PMTiles
- Vector Tiles
- Open-Source
- Self-Hosted
- OpenStreetMap
website: https://protomaps.com
---
