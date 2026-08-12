---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nasa Cmr Agentic Access
  operation_count: 10
  slug: nasa-cmr-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 9
apis:
- description: REST API for creating, updating, and deleting metadata records in the Common Metadata Repository. Supports collections, granules, variables, services, tools, and subscriptions. Requires EDL Bearer Tok
  name: CMR Ingest API
  slug: cmr-ingest
- description: REST API for managing Access Control Lists (ACLs) and checking user permissions across CMR concepts. Supports system, provider, single-instance, and catalog-item identity types. Enables fine-grained a
  name: CMR Access Control API
  slug: cmr-access-control
- description: Unified GraphQL interface for querying the Common Metadata Repository. Provides a single endpoint to search collections, granules, variables, tools, services, citations, visualizations, grids, groups,
  name: CMR GraphQL API
  slug: cmr-graphql
- description: SpatioTemporal Asset Catalog (STAC) compliant API wrapping the CMR Search API. Organizes the full NASA CMR catalog by provider and enables discovery of STAC collections and items. CMR-CLOUDSTAC varian
  name: CMR STAC API
  slug: cmr-stac
- description: 'OpenSearch-compliant API wrapper for CMR Search enabling standard OpenSearch client integration. Supports collection discovery with spatial and temporal parameters. Complements the native REST search '
  name: CMR OpenSearch API
  slug: cmr-opensearch
- description: essential characteristics of this API
  name: NASA CMR Capabilities API
  slug: nasa-cmr-capabilities-api
- description: Collection Search
  name: NASA CMR Collections API
  slug: nasa-cmr-collections-api
- description: access to data (features)
  name: NASA CMR Data API
  slug: nasa-cmr-data-api
- description: Extension to WFS3 Core to support STAC metadata model and search API
  name: NASA CMR STAC API
  slug: nasa-cmr-stac-api
artifact_total: 28
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nasa/cmr-stac/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nasa/cmr-stac/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-cmr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-cmr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.earthdata.nasa.gov/about/esdis/eosdis/cmr
- group: docs
  title: ''
  type: Documentation
  url: https://www.earthdata.nasa.gov/engage/open-data-services-software/earthdata-developer-portal/cmr-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nasa
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nasa/Common-Metadata-Repository
- group: operate
  title: ''
  type: Forums
  url: https://forum.earthdata.nasa.gov/
- group: start
  title: ''
  type: Login
  url: https://urs.earthdata.nasa.gov/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.earthdata.nasa.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.earthdata.nasa.gov/news
- group: commercial
  title: ''
  type: Plans
  url: plans/nasa-cmr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasa-cmr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nasa-cmr-finops.yml
created: '2026-06-13'
description: NASA Common Metadata Repository (CMR) is a high-performance metadata system that catalogs Earth science data collections, granules, variables, services, and tools across NASA data centers. It provides REST, GraphQL, STAC, OpenSearch, and CSW interfaces for discovering, searching, and ingesting metadata for satellite and Earth observation datasets spanning decades of NASA missions.
examples:
- key_count: 10
  name: Nasa Cmr Ingest Collection Request
  slug: nasa-cmr-ingest-collection-request
- key_count: 3
  name: Nasa Cmr Search Collections Response
  slug: nasa-cmr-search-collections-response
- key_count: 3
  name: Nasa Cmr Search Granules Response
  slug: nasa-cmr-search-granules-response
- key_count: 7
  name: Nasa Cmr Stac Landing Page
  slug: nasa-cmr-stac-landing-page
finops:
- name: Nasa Cmr Finops
  service_category: ''
  slug: nasa-cmr-finops
graphqls:
- description: The NASA Common Metadata Repository (CMR) GraphQL API provides a unified interface for querying and managing Earth science metadata across NASA data centers. It exposes collections, granules, variable
  name: NASA CMR GraphQL API
  slug: nasa-cmr-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-cmr.png
json_schemas:
- name: NASA CMR STAC Collection
  property_count: 7
  slug: nasa-cmr-stac-collection
- name: NASA CMR STAC Featurecollectiongeojson
  property_count: 6
  slug: nasa-cmr-stac-featureCollectionGeoJSON
- name: NASA CMR STAC Featuregeojson
  property_count: 5
  slug: nasa-cmr-stac-featureGeoJSON
- name: NASA CMR STAC Landingpage
  property_count: 3
  slug: nasa-cmr-stac-landingPage
- name: Link
  property_count: 6
  slug: nasa-cmr-stac-link
- name: NASA CMR STAC Searchbody
  property_count: 0
  slug: nasa-cmr-stac-searchBody
jsonld:
- class_count: 0
  name: Nasa Cmr Context
  property_count: 22
  slug: nasa-cmr-context
- class_count: 0
  name: Nasa Cmr Dataset Context
  property_count: 0
  slug: nasa-cmr-dataset
layout: provider
modified: '2026-06-13'
name: NASA CMR
nav: Providers
network: true
overview: 'NASA CMR publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Capabilities API, Collections API, Data API, and 1 more. Tagged areas include NASA, Earth Science, Satellite Data, Remote Sensing, and Geospatial.


  The NASA CMR catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  NASA CMR''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Nasa Cmr Plans Pricing
  plan_count: 3
  slug: nasa-cmr-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 6
  name: Nasa Cmr Rate Limits
  slug: nasa-cmr-rate-limits
rules:
- name: NASA CMR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nasa-cmr-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.8
  delta: 2.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.5
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-cmr/refs/heads/main/screenshots/nasa-cmr-2026-06-20T185946.png
security:
- kind: domain-security
  name: Nasa Cmr Domain Security
  slug: nasa-cmr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nasa-cmr
tags:
- NASA
- Earth Science
- Satellite Data
- Remote Sensing
- Geospatial
- Open Data
- Metadata
- Collections
- Granules
website: https://www.earthdata.nasa.gov/about/esdis/eosdis/cmr
---
