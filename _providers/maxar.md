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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Maxar Agentic Access
  operation_count: 16
  slug: maxar-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 15
apis:
- description: OAuth2-style token service that mints bearer access tokens (and 180-day default API keys) for use against all Vantor Hub / MGP APIs.
  name: Maxar Authentication / Token Service
  slug: authentication
- description: Unified catalog search across Archive Imagery, Vivid Basemaps, and Change Monitoring. Supports filtering and sorting and returns STAC and GeoJSON metadata representations of matching items.
  name: Maxar Discovery API
  slug: discovery
- description: Order placement and management for archive and online imagery with multiple delivery options and processing pipelines. Supports tracking order status to completion and delivery.
  name: Maxar Ordering API
  slug: ordering
- description: OGC-compliant WFS / WMS / WMTS streaming services for delivering online imagery strips into web mapping clients and GIS workflows.
  name: Maxar Streaming Imagery API
  slug: streaming-imagery
- description: OGC service delivering Maxar Vivid basemap products and their metadata for cartographic and analytic use.
  name: Maxar Streaming Basemap API
  slug: streaming-basemap
- description: Streams 3D surface models derived from Maxar's stereo and tri-stereo collections for visualization and 3D analysis.
  name: Maxar Streaming 3D API
  slug: streaming-3d
- description: Register Areas of Interest and receive alerts when new imagery or analytic outputs match. Drives standing tip-and-cue workflows over the Maxar catalog.
  name: Maxar Monitoring API
  slug: monitoring
- description: Request new imagery collection from the WorldView Legion and legacy WorldView constellations within a target geometry and time window. Supports Fastview and Flexview tasking tiers.
  name: Maxar Tasking API
  slug: tasking
- description: Server-side raster processing - band manipulation, classification, and index models (NDVI, NDWI, etc.) - composed as analysis graphs over the Maxar catalog.
  name: Maxar Raster Analytics API
  slug: raster-analytics
- description: Vector deliveries of change monitoring outputs through OGC WMS / WMTS for downstream analytic and GIS consumption.
  name: Maxar Vector Analytics API
  slug: vector-analytics
- description: Official Python SDK (maxar-platform on PyPI) wrapping the MGP / Vantor Hub APIs for discovery, ordering, monitoring, streaming, and tasking workflows.
  name: Maxar Geospatial Platform Python SDK
  slug: python-sdk
- description: Public Postman workspace documenting the Maxar Geospatial Platform API surface for quick exploration and testing.
  name: Maxar MGP Postman Collection
  slug: postman
- description: The Authentication API from Maxar — 2 operation(s) for authentication.
  name: Maxar Authentication API
  slug: maxar-authentication-api
- description: The Discovery API from Maxar — 5 operation(s) for discovery.
  name: Maxar Discovery API
  slug: maxar-discovery-api
- description: The Ordering API from Maxar — 6 operation(s) for ordering.
  name: Maxar Ordering API
  slug: maxar-ordering-api
artifact_total: 22
collections:
- collection_type: open
  name: Maxar Geospatial Platform (Vantor Hub) API
  slug: open-maxar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maxar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maxar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.maxar.com/
- group: other
  title: ''
  type: GeospatialPlatform
  url: https://maxar.com/maxar-geospatial-platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.maxar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.maxar.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.maxar.com/docs/authentication/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.maxar.com/docs/release-notes
- group: build
  title: ''
  type: PythonSDK
  url: https://pypi.org/project/maxar-platform/
- group: docs
  title: ''
  type: SDKDocumentation
  url: https://maxar-geospatial-platform.readthedocs.io/
- group: build
  title: ''
  type: Postman
  url: https://api-postman.maxar.com/
- group: docs
  title: ''
  type: ProDocs
  url: https://pro-docs.maxar.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maxar-technologies/
- group: other
  title: ''
  type: X
  url: https://x.com/Maxar
created: '2026-05-23'
description: 'Maxar (operating in 2026 as Vantor / Maxar Intelligence) is a high-resolution Earth observation and 3D geospatial provider operating the WorldView Legion, WorldView-3, WorldView-2, and GeoEye-1 constellations. The Maxar Geospatial Platform (MGP), branded as Vantor Hub, is API-first: developers authenticate through the Authentication / Token Service, search the 125+PB Vivid, archive, and change-monitoring catalog through the Discovery API (STAC / GeoJSON), place orders through the Ordering API, stream imagery and basemaps through OGC-compliant WFS / WMS / WMTS services, retrieve 3D surface models, register Areas of Interest with the Monitoring API, and task new collections through the Tasking API (Fastview / Flexview). Raster and Vector Analytics expose NDVI, NDWI, change-monitoring vectors, and custom analysis graphs. An official Python SDK (maxar-platform) wraps the full surface.'
finops:
- name: Maxar Finops
  service_category: API
  slug: maxar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxar.png
layout: provider
modified: '2026-05-23'
name: Maxar
nav: Providers
network: true
overview: 'Maxar publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Discovery API, and Ordering API. Tagged areas include Earth Observation, Satellite Imagery, High Resolution, Geospatial, and 3D.


  Maxar''s developer surface includes authentication, documentation, release notes, and 12 more developer resources.'
plans:
- name: Maxar Plans Pricing
  plan_count: 1
  slug: maxar-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Maxar Rate Limits
  slug: maxar-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.8
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxar/refs/heads/main/screenshots/maxar-2026-06-20T185048.png
security:
- kind: authentication
  name: Maxar Authentication
  slug: maxar-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Maxar Domain Security
  slug: maxar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maxar
tags:
- Earth Observation
- Satellite Imagery
- High Resolution
- Geospatial
- 3D
- STAC
- OGC
- WorldView
- Tasking
- Vantor
- Basemaps
- Change Monitoring
website: https://www.maxar.com/
---
