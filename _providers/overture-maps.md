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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 11
apis:
- description: Open dataset of global address points and ranges, released as cloud-native GeoParquet alongside the other Overture themes.
  name: Overture Addresses Theme
  slug: addresses
- description: Open dataset of base map features - land cover, water, land use, infra - released as cloud-native GeoParquet to serve as a foundation for map rendering.
  name: Overture Base Theme
  slug: base
- description: Open dataset of global building footprints with attributes (heights, classes, sources), released as cloud-native GeoParquet.
  name: Overture Buildings Theme
  slug: buildings
- description: Open dataset of administrative and statistical boundaries (countries, regions, counties, localities, neighborhoods) released as cloud-native GeoParquet.
  name: Overture Divisions Theme
  slug: divisions
- description: Open dataset of global points of interest - businesses, landmarks, and services - released as cloud-native GeoParquet with categories, addresses, and confidence scoring.
  name: Overture Places Theme
  slug: places
- description: Open dataset of the global road and transportation network (segments and connectors) released as cloud-native GeoParquet, suitable for routing and analytics.
  name: Overture Transportation Theme
  slug: transportation
- description: Canonical open schema specification for all Overture themes, maintained in the OvertureMaps/schema GitHub repository and versioned with each data release.
  name: Overture Schema
  slug: schema
- description: Repository of release notes, cloud paths (Amazon S3 and Microsoft Azure), and access scripts for every Overture data release. Datasets are distributed as cloud-native GeoParquet and versioned per rele
  name: Overture Data Releases
  slug: data
- description: Open-source Python command-line tool and library for downloading and querying Overture data. Maintained at OvertureMaps/overturemaps-py.
  name: Overture Maps Python CLI
  slug: cli
- description: Interactive web explorer for browsing and inspecting Overture features across themes and releases.
  name: Overture Explorer
  slug: explorer
- description: Open tile-generation tooling that builds vector tilesets from Overture data for rendering and downstream applications.
  name: Overture Tiles
  slug: tiles
artifact_total: 15
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/OvertureMaps/schema/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overture-maps-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/overture-maps-foundation
- group: company
  title: ''
  type: Website
  url: https://overturemaps.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overturemaps.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OvertureMaps
- group: commercial
  title: ''
  type: Plans
  url: plans/overture-maps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/overture-maps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/overture-maps-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.overturemaps.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://overturemaps.org/blog/
created: '2026-05-23'
description: Overture Maps Foundation is a Linux Foundation collaborative project that produces free, open, and interoperable map data. Overture publishes cloud-native GeoParquet datasets, on a regular release cadence, across six themes - Addresses, Base, Buildings, Divisions, Places, and Transportation - governed by a common conflation pipeline and an open schema. Rather than a hosted REST API, Overture distributes data through Amazon S3 and Microsoft Azure (and via partner mirrors on BigQuery, Snowflake, Databricks, Fused, Wherobots), and provides an open Python CLI, a tile generator, and an Explorer site for developers. Founding members include Amazon, Meta, Microsoft, and TomTom.
finops:
- name: Overture Maps Finops
  service_category: API
  slug: overture-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/overture-maps.png
layout: provider
modified: '2026-05-23'
name: Overture Maps Foundation
nav: Providers
network: true
overview: 'Overture Maps Foundation publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Maps, Geospatial, Open Data, GeoParquet, and Open Source.


  Overture Maps Foundation''s developer surface includes documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Overture Maps Plans Pricing
  plan_count: 1
  slug: overture-maps-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Overture Maps Rate Limits
  slug: overture-maps-rate-limits
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overture-maps/refs/heads/main/screenshots/overture-maps-2026-06-20T191239.png
security:
- kind: domain-security
  name: Overture Maps Domain Security
  slug: overture-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overture-maps
tags:
- Maps
- Geospatial
- Open Data
- GeoParquet
- Open Source
- Linux Foundation
website: https://overturemaps.org/
---
