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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Maptiler Agentic Access
  operation_count: 32
  slug: maptiler-agentic-access
  summary_line: 32 operations
api_count: 18
apis:
- description: Provides access to MapTiler Cloud map styles including embeddable viewers, style configuration, raster tiles, and OGC-compatible endpoints for rendering and serving customizable map styles.
  name: MapTiler Maps API
  slug: maptiler-maps-api
- description: Delivers map tile datasets including satellite imagery, terrain, and other raster or vector tile collections via XYZ, OGC API - Tiles, and WMTS-compatible endpoints.
  name: MapTiler Tiles API
  slug: maptiler-tiles-api
- description: Enables forward and reverse geocoding to search for places and addresses anywhere on Earth and convert coordinates to location data. Supports batch geocoding of up to 50 queries per request with filte
  name: MapTiler Geocoding API
  slug: maptiler-geocoding-api
- description: 'Generates static non-interactive map images in PNG, JPG, or WebP formats. Supports center-based, bounding-box-based, and auto-fitted viewports with optional markers and path overlays. Requires a paid '
  name: MapTiler Static Maps API
  slug: maptiler-static-maps-api
- description: Provides accurate altitude above mean sea level for any location on Earth. Accepts up to 50 coordinate pairs per request and returns elevation in meters or feet.
  name: MapTiler Elevation API
  slug: maptiler-elevation-api
- description: Returns approximate geographic location based on the incoming request's IP address, including country, city, coordinates, timezone, and optional elevation data. Useful for localizing maps and applicat
  name: MapTiler Geolocation API
  slug: maptiler-geolocation-api
- description: Enables searching the EPSG coordinate system database and transforming coordinates between different projections and coordinate reference systems. Supports up to 50 coordinate pairs per transformation
  name: MapTiler Coordinates API
  slug: maptiler-coordinates-api
- description: The Coordinates API from MapTiler — 2 operation(s) for coordinates.
  name: MapTiler Coordinates API
  slug: maptiler-coordinates-api
- description: The Data API from MapTiler — 1 operation(s) for data.
  name: MapTiler Data API
  slug: maptiler-data-api
- description: The Elevation API from MapTiler — 1 operation(s) for elevation.
  name: MapTiler Elevation API
  slug: maptiler-elevation-api
- description: The Geocoding API from MapTiler — 4 operation(s) for geocoding.
  name: MapTiler Geocoding API
  slug: maptiler-geocoding-api
- description: The Geolocation API from MapTiler — 1 operation(s) for geolocation.
  name: MapTiler Geolocation API
  slug: maptiler-geolocation-api
- description: The Images API from MapTiler — 2 operation(s) for images.
  name: MapTiler Images API
  slug: maptiler-images-api
- description: The Maps API from MapTiler — 8 operation(s) for maps.
  name: MapTiler Maps API
  slug: maptiler-maps-api
- description: The Other API from MapTiler — 3 operation(s) for other.
  name: MapTiler Other API
  slug: maptiler-other-api
- description: The Static maps API from MapTiler — 3 operation(s) for static maps.
  name: MapTiler Static maps API
  slug: maptiler-static-maps-api
- description: The Tiles API from MapTiler — 6 operation(s) for tiles.
  name: MapTiler Tiles API
  slug: maptiler-tiles-api
- description: The Weather API from MapTiler — 1 operation(s) for weather.
  name: MapTiler Weather API
  slug: maptiler-weather-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MapTiler Coordinates API
  slug: open-maptiler-coordinates-api
- collection_type: open
  name: MapTiler Coordinates Data API
  slug: open-maptiler-data-api
- collection_type: open
  name: MapTiler Coordinates Elevation API
  slug: open-maptiler-elevation-api
- collection_type: open
  name: MapTiler Coordinates Geocoding API
  slug: open-maptiler-geocoding-api
- collection_type: open
  name: MapTiler Coordinates Geolocation API
  slug: open-maptiler-geolocation-api
- collection_type: open
  name: MapTiler Coordinates Images API
  slug: open-maptiler-images-api
- collection_type: open
  name: MapTiler Coordinates Maps API
  slug: open-maptiler-maps-api
- collection_type: open
  name: MapTiler Coordinates Other API
  slug: open-maptiler-other-api
- collection_type: open
  name: MapTiler Coordinates Static maps API
  slug: open-maptiler-static-maps-api
- collection_type: open
  name: MapTiler Coordinates Tiles API
  slug: open-maptiler-tiles-api
- collection_type: open
  name: MapTiler Coordinates Weather API
  slug: open-maptiler-weather-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maptiler-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/maptiler-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maptiler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maptiler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maptiler-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.maptiler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maptiler.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/maptiler
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maptiler/
- group: company
  title: ''
  type: Blog
  url: https://www.maptiler.com/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maptiler.com/cloud/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.maptiler.com
- group: other
  title: ''
  type: X
  url: https://x.com/MapTiler
- group: commercial
  title: ''
  type: Plans
  url: plans/maptiler-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maptiler-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maptiler-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/maptiler-maptiler-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/maptiler-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/maptiler-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/maptiler-geocoding-result.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/maptiler-geolocation-result.json
- group: build
  title: ''
  type: Examples
  url: examples/maptiler-geocoding-forward.json
- group: build
  title: ''
  type: Examples
  url: examples/maptiler-geolocation-ip.json
- group: build
  title: ''
  type: Examples
  url: examples/maptiler-elevation.json
- group: build
  title: ''
  type: Examples
  url: examples/maptiler-static-map.json
created: '2026-06-12'
description: MapTiler is a map hosting and geospatial API platform providing vector tiles, satellite imagery, geocoding, reverse geocoding, static maps, elevation data, geolocation, and coordinate transformation via REST APIs and SDKs for web, mobile, and server-side developers.
examples:
- key_count: 5
  name: Maptiler Elevation
  slug: maptiler-elevation
- key_count: 4
  name: Maptiler Geocoding Forward
  slug: maptiler-geocoding-forward
- key_count: 4
  name: Maptiler Geolocation Ip
  slug: maptiler-geolocation-ip
- key_count: 3
  name: Maptiler Static Map
  slug: maptiler-static-map
finops:
- name: Maptiler Finops
  service_category: ''
  slug: maptiler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maptiler.png
json_schemas:
- name: SearchResults
  property_count: 4
  slug: maptiler-geocoding-result
- name: GeolocationResult
  property_count: 15
  slug: maptiler-geolocation-result
jsonld:
- class_count: 0
  name: Maptiler Context
  property_count: 36
  slug: maptiler-context
layout: provider
modified: '2026-06-12'
name: MapTiler
nav: Providers
network: true
overview: 'MapTiler publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Maps API, Tiles API, Geocoding API, and 15 more. Tagged areas include Maps, Geospatial, Tiles, Vector Tiles, and Satellite Imagery.


  The MapTiler catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MapTiler''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, code examples, and 19 more developer resources.'
plans:
- name: Maptiler Plans Pricing
  plan_count: 4
  slug: maptiler-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 4
  name: Maptiler Rate Limits
  slug: maptiler-rate-limits
rules:
- name: MapTiler API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: maptiler-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 62.2
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maptiler/refs/heads/main/screenshots/maptiler-2026-06-20T184936.png
security:
- kind: authentication
  name: Maptiler Authentication
  slug: maptiler-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Maptiler Domain Security
  slug: maptiler-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Maptiler Vulnerability Disclosure
  slug: maptiler-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Maptiler Trust Center
  slug: maptiler-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: maptiler
tags:
- Maps
- Geospatial
- Tiles
- Vector Tiles
- Satellite Imagery
- Geocoding
- Reverse Geocoding
- Static Maps
- Elevation
- Geolocation
- Coordinate Transformation
- GIS
- Mapping Platform
website: https://www.maptiler.com/
---
