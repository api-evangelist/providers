---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Regrid Agentic Access
  operation_count: 22
  slug: regrid-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 9
apis:
- description: Tile Map Service (TMS) providing interactive vector and raster map layers of the full Regrid parcel dataset for embedding in web and mobile mapping applications. Supports both Standard and Premium sch
  name: Regrid Tile API
  slug: regrid-tile-api
- description: API delivering building footprint geometries matched to parcel records, including building square footage and building count per parcel.
  name: Regrid Matched Building Footprints API
  slug: regrid-matched-building-footprints-api
- description: API providing standardized zoning data and classifications covering major US metropolitan areas, matched to parcel records.
  name: Regrid Standardized Zoning API
  slug: regrid-standardized-zoning-api
- description: API providing current owner information and deeded property details with daily refresh cycles for up-to-date ownership tracking.
  name: Regrid Daily Ownership Updates API
  slug: regrid-daily-ownership-updates-api
- description: Coverage, usage, and data quality endpoints
  name: Regrid Metadata API
  slug: regrid-metadata-api
- description: Filter parcel dataset by indexed schema attributes
  name: Regrid Parcel Query API
  slug: regrid-parcel-query-api
- description: Search parcel records by various criteria
  name: Regrid Parcel Search API
  slug: regrid-parcel-search-api
- description: Field schema definitions for parcel data products
  name: Regrid Schemas API
  slug: regrid-schemas-api
- description: Address autocomplete suggestions
  name: Regrid Typeahead API
  slug: regrid-typeahead-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Regrid Parcel Metadata API
  slug: open-regrid-metadata-api
- collection_type: open
  name: Regrid Parcel Metadata Parcel Query API
  slug: open-regrid-parcel-query-api
- collection_type: open
  name: Regrid Parcel Metadata Parcel Search API
  slug: open-regrid-parcel-search-api
- collection_type: open
  name: Regrid Parcel Metadata Schemas API
  slug: open-regrid-schemas-api
- collection_type: open
  name: Regrid Parcel Metadata Typeahead API
  slug: open-regrid-typeahead-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/regrid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regrid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regrid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://regrid.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.regrid.com/api/section/parcel-api
- group: commercial
  title: ''
  type: Pricing
  url: https://app.regrid.com/api/plans
- group: company
  title: ''
  type: Blog
  url: https://regrid.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.regrid.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regridapp
- group: other
  title: ''
  type: X
  url: https://x.com/regridapp
- group: commercial
  title: ''
  type: Plans
  url: plans/regrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/regrid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/regrid-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/regrid-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/regrid-parcel-properties.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/regrid-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/parcel-point-lookup-response.json
- group: build
  title: ''
  type: Examples
  url: examples/parcel-area-search-request.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: 2026-06-12
description: Regrid is a national land parcel data platform providing REST APIs for querying parcel boundaries, ownership, zoning, assessed values, and deed records across all US counties and Canadian provinces. The platform offers a Parcel API for retrieving structured GeoJSON parcel records by location, address, APN, owner, or polygon area, alongside a Tile API delivering raster and vector map layers. Additional APIs cover matched secondary addresses, building footprints, standardized zoning, and daily ownership updates. Authentication uses API token parameters, billing is metered by parcel records returned, and self-serve monthly subscriptions are available in Standard and Premium schema tiers with enterprise custom packages also offered.
examples:
- key_count: 3
  name: Parcel Area Search Request
  slug: parcel-area-search-request
- key_count: 4
  name: Parcel Point Lookup Response
  slug: parcel-point-lookup-response
finops:
- name: Regrid Finops
  service_category: ''
  slug: regrid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regrid.png
json_schemas:
- name: Regrid Parcel Properties
  property_count: 53
  slug: regrid-parcel-properties
jsonld:
- class_count: 2
  name: Regrid Context
  property_count: 56
  slug: regrid-context
layout: provider
modified: 2026-06-12
name: Regrid
nav: Providers
network: true
overview: 'Regrid publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Parcel Query API, Parcel Search API, and 2 more. Tagged areas include Parcels, Land Data, Property Data, GeoJSON, and Real Estate.


  The Regrid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Regrid''s developer surface includes authentication, documentation, pricing, engineering blog, code examples, and 14 more developer resources.'
plans:
- name: Regrid Plans Pricing
  plan_count: 4
  slug: regrid-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Regrid Rate Limits
  slug: regrid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Regrid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: regrid-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: -6.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 61.5
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 47.4
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/regrid/refs/heads/main/screenshots/regrid-2026-06-20T192759.png
security:
- kind: authentication
  name: Regrid Authentication
  slug: regrid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Regrid Domain Security
  slug: regrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: regrid
tags:
- Parcels
- Land Data
- Property Data
- GeoJSON
- Real Estate
- Zoning
- Ownership
- Geospatial
- Mapping
- Tiles
website: https://regrid.com
---
