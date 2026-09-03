---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: bearer
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Planet Labs Agentic Access
  operation_count: 33
  slug: planet-labs-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 1
apis:
- description: Programmatic search over Planet's imagery catalog by AOI, time window, cloud cover, item type, and asset type. Returns item and asset metadata for downstream activation and download.
  name: Planet Data API
  slug: data
- description: STAC-based search and access layer over Planet imagery metadata, providing a standards-aligned interface to the archive.
  name: Planet Catalog API
  slug: catalog
- description: Request preparation and delivery of imagery bundles with optional processing operations (clip, composite, harmonize, reproject, band math, file format), and deliver to cloud destinations (S3, GCS, Azu
  name: Planet Orders API
  slug: orders
- description: Standing subscriptions that deliver new imagery and analytic feeds to a cloud destination automatically as new acquisitions clear the AOI and cloud-cover filter.
  name: Planet Subscriptions API
  slug: subscriptions
- description: Discover, view, and download Planet's PlanetScope monitoring and visual basemap mosaics covering the global landmass at regular cadence.
  name: Planet Basemaps API
  slug: basemaps
- description: Tasking interface for SkySat and Pelican constellations. Submit collection requests against a target geometry and time window and track capture and delivery status.
  name: Planet Tasking API
  slug: tasking
- description: Access to Planet Analytics Feeds, including building, road, ship, and change detection outputs derived from the imagery archive.
  name: Planet Analytics API
  slug: analytics
- description: Run custom processing scripts on raw bands and derive indices (NDVI, EVI, etc.) over Planet imagery without downloading source data.
  name: Planet Processing API
  slug: processing
- description: Compute per-AOI statistics (mean, median, percentiles, histograms) over imagery and analytic layers without requiring full raster downloads.
  name: Planet Statistical API
  slug: statistical
- description: XYZ and WMTS tile services for visualizing PlanetScope and SkySat scenes and basemaps in web mapping clients.
  name: Planet Tiles API
  slug: tiles
- description: Save and manage Areas of Interest (features and feature collections) for reuse across Subscriptions, Orders, and Tasking.
  name: Planet Features API
  slug: features
- description: Official Python SDK (planet on PyPI) and CLI for working with all Planet APIs, including async clients for search, orders, subscriptions, and data activation.
  name: Planet Python SDK
  slug: python-sdk
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Item type and asset type metadata.
  name: Planet Labs Data - Item Types API
  slug: planet-labs-data-item-types-api
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Item and asset retrieval.
  name: Planet Labs Data - Items API
  slug: planet-labs-data-items-api
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Catalog search and saved searches.
  name: Planet Labs Data - Search API
  slug: planet-labs-data-search-api
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Search-driven statistics.
  name: Planet Labs Data - Stats API
  slug: planet-labs-data-stats-api
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Bundle preparation and delivery jobs.
  name: Planet Labs Orders API
  slug: planet-labs-orders-api
- baseURL: https://api.planet.com/data/v1
  baseurl_source: declared
  description: Standing area-of-interest delivery feeds.
  name: Planet Labs Subscriptions API
  slug: planet-labs-subscriptions-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Planet Insights Platform Data - Item Types API
  slug: open-planet-labs-data-item-types-api
- collection_type: open
  name: Planet Insights Platform Data - Item Types Data - Items API
  slug: open-planet-labs-data-items-api
- collection_type: open
  name: Planet Insights Platform Data - Item Types Data - Search API
  slug: open-planet-labs-data-search-api
- collection_type: open
  name: Planet Insights Platform Data - Item Types Data - Stats API
  slug: open-planet-labs-data-stats-api
- collection_type: open
  name: Planet Insights Platform Data - Item Types Orders API
  slug: open-planet-labs-orders-api
- collection_type: open
  name: Planet Insights Platform Data - Item Types Subscriptions API
  slug: open-planet-labs-subscriptions-api
- collection_type: open
  name: Planet Insights Platform API
  slug: open-planet-labs
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/planetlabs/planet-client-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/planetlabs/planet-client-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/planetlabs/planet-client-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/planetlabs/planet-client-python/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planet-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planet-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planet-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.planet.com/
- group: other
  title: ''
  type: Developers
  url: https://www.planet.com/markets/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.planet.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.planet.com/develop/apis/
- group: other
  title: ''
  type: InsightsPlatform
  url: https://www.planet.com/products/planet-insights-platform/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planetlabs
- group: company
  title: ''
  type: Blog
  url: https://www.planet.com/pulse/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.planet.com/pricing/
- group: operate
  title: ''
  type: Status
  url: https://status.planet.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planet-labs/
- group: other
  title: ''
  type: X
  url: https://x.com/planet
created: '2026-05-23'
description: 'Planet Labs operates the world''s largest commercial Earth observation constellation, imaging the entire landmass of the planet daily with its PlanetScope satellites and capturing high-resolution targeted imagery with SkySat and Pelican. The Planet Insights Platform is API-first: developers search the archive through the Data and Catalog APIs, order processed bundles through the Orders API, set up standing area-of-interest deliveries through the Subscriptions API, request tip-and-cue collections through the Tasking API, and consume mosaics through the Basemaps and Tiles APIs. Analytics, Processing, Statistical, and Batch APIs run server-side workflows over the catalog and over Planetary Variables. All APIs sit under api.planet.com, authenticate with an API key over HTTP Basic, and are wrapped by the official Planet Python SDK.'
finops:
- name: Planet Labs Finops
  service_category: API
  slug: planet-labs-finops
graphqls:
- description: 'Planet Labs provides daily earth observation imagery from its satellite constellation. The API covers scene discovery, basemap access, analytics feeds, subscription management, orders, data delivery, '
  name: Planet Labs GraphQL API
  slug: planet-labs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/planet-labs.png
layout: provider
modified: '2026-05-23'
name: Planet Labs
nav: Providers
network: true
overview: 'Planet Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Data - Item Types API, Data - Items API, Data - Search API, and 3 more. Tagged areas include Earth Observation, Satellite Imagery, Geospatial, PlanetScope, and SkySat.


  Planet Labs'' developer surface includes authentication, documentation, API reference, engineering blog, pricing, status page, and 12 more developer resources.'
plans:
- name: Planet Labs Plans Pricing
  plan_count: 1
  slug: planet-labs-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Planet Labs Rate Limits
  slug: planet-labs-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 50.0
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planet-labs/refs/heads/main/screenshots/planet-labs-2026-06-20T191756.png
security:
- kind: authentication
  name: Planet Labs Authentication
  slug: planet-labs-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Planet Labs Domain Security
  slug: planet-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: planet-labs
tags:
- Earth Observation
- Satellite Imagery
- Geospatial
- PlanetScope
- SkySat
- Pelican
- Tasking
- Basemaps
- Analytics
- Subscription
- STAC
- GIS
website: https://www.planet.com/
---
