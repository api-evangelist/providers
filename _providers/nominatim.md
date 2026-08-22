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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nominatim Agentic Access
  operation_count: 7
  slug: nominatim-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Objects removed from OpenStreetMap but retained in Nominatim.
  name: Nominatim Deletable API
  slug: nominatim-deletable-api
- description: Internal place details, intended for debugging.
  name: Nominatim Details API
  slug: nominatim-details-api
- description: Look up address details for OSM objects by their OSM ID.
  name: Nominatim Lookup API
  slug: nominatim-lookup-api
- description: Problematic polygon data detected by the system.
  name: Nominatim Polygons API
  slug: nominatim-polygons-api
- description: Reverse geocoding — find the closest OSM object to a coordinate.
  name: Nominatim Reverse API
  slug: nominatim-reverse-api
- description: Forward geocoding — search OSM objects by name or address.
  name: Nominatim Search API
  slug: nominatim-search-api
- description: Service and database status reporting.
  name: Nominatim Status API
  slug: nominatim-status-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nominatim Deletable API
  slug: open-nominatim-deletable-api
- collection_type: open
  name: Nominatim Deletable Details API
  slug: open-nominatim-details-api
- collection_type: open
  name: Nominatim Deletable Lookup API
  slug: open-nominatim-lookup-api
- collection_type: open
  name: Nominatim Deletable Polygons API
  slug: open-nominatim-polygons-api
- collection_type: open
  name: Nominatim Deletable Reverse API
  slug: open-nominatim-reverse-api
- collection_type: open
  name: Nominatim Deletable Search API
  slug: open-nominatim-search-api
- collection_type: open
  name: Nominatim Deletable Status API
  slug: open-nominatim-status-api
- collection_type: open
  name: Nominatim API
  slug: open-nominatim
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/osm-search/Nominatim/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/osm-search/Nominatim/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/osm-search/Nominatim/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/osm-search/Nominatim/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/osm-search/Nominatim/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nominatim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nominatim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nominatim.org/
- group: docs
  title: ''
  type: Documentation
  url: https://nominatim.org/release-docs/develop/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/osm-search
- group: build
  title: Nominatim core (Python)
  type: GitHubRepository
  url: https://github.com/osm-search/Nominatim
- group: build
  title: Nominatim debug UI (Svelte)
  type: GitHubRepository
  url: https://github.com/osm-search/nominatim-ui
- group: build
  title: Data Analyser QA tool
  type: GitHubRepository
  url: https://github.com/osm-search/Nominatim-Data-Analyser
- group: build
  title: Wikipedia/Wikidata preprocessing
  type: GitHubRepository
  url: https://github.com/osm-search/wikipedia-wikidata
- group: build
  title: US Census TIGER preprocessing
  type: GitHubRepository
  url: https://github.com/osm-search/TIGER-data
- group: build
  title: GB postcode preprocessing
  type: GitHubRepository
  url: https://github.com/osm-search/gb-postcode-data
- group: build
  title: Country grid preprocessing
  type: GitHubRepository
  url: https://github.com/osm-search/country-grid-data
- group: build
  title: Secondary importance raster builder
  type: GitHubRepository
  url: https://github.com/osm-search/secondary-importance
- group: commercial
  title: Nominatim Usage Policy
  type: TermsOfService
  url: https://operations.osmfoundation.org/policies/nominatim/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nominatim-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nominatim-plans-pricing.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nominatim-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/nominatim-rules.yml
- group: build
  title: osmmcp — OpenStreetMap MCP Server (Nominatim + Overpass + OSRM)
  type: Tools
  url: https://github.com/NERVsystems/osmmcp
- group: build
  title: geocoding-ai/mcp — Nominatim Geocoding MCP Server (Node.js)
  type: Tools
  url: https://github.com/geocoding-ai/mcp
- group: build
  title: geocode-mcp — Nominatim Geocoding MCP Server (Python)
  type: Tools
  url: https://github.com/X-McKay/geocode-mcp
- group: build
  title: open-streetmap-mcp — OpenStreetMap MCP Server
  type: Tools
  url: https://github.com/jagan-shanmugam/open-streetmap-mcp
- group: build
  title: Unofficial Nominatim OpenAPI spec
  type: Tools
  url: https://github.com/sparkfabrik/nominatim-openapi
- group: company
  title: ''
  type: Blog
  url: https://nominatim.org/feed.xml
created: '2026-05-28'
description: Nominatim is an open-source (BSD-2-Clause) search engine for OpenStreetMap data, supporting forward geocoding (address to coordinates), reverse geocoding (coordinates to address), and address lookup by OSM ID. The OpenStreetMap Foundation runs a free public instance at nominatim.openstreetmap.org under a published usage policy, and the project is also widely self-hosted and resold by commercial providers (MapTiler, LocationIQ, Geocode Earth).
examples:
- key_count: 12
  name: Nominatim Address Example
  slug: nominatim-address-example
- key_count: 2
  name: Nominatim Details Example
  slug: nominatim-details-example
- key_count: 2
  name: Nominatim Lookup Example
  slug: nominatim-lookup-example
- key_count: 17
  name: Nominatim Place Example
  slug: nominatim-place-example
- key_count: 2
  name: Nominatim Reverse Example
  slug: nominatim-reverse-example
- key_count: 2
  name: Nominatim Search Example
  slug: nominatim-search-example
- key_count: 2
  name: Nominatim Status Example
  slug: nominatim-status-example
features:
- description: Convert free-form or structured addresses into coordinates and full place metadata.
  name: Forward Geocoding
- description: Identify the closest OSM feature to a coordinate at a chosen administrative zoom level.
  name: Reverse Geocoding
- description: Resolve up to 50 OSM nodes/ways/relations to detailed address breakdowns per call.
  name: OSM Object Lookup
- description: Returns json, jsonv2, geojson, geocodejson, and xml from a single endpoint via `format`.
  name: Multi-Format Output
- description: Optional geometry output as GeoJSON, KML, SVG, or WKT with a simplification tolerance.
  name: Polygon Geometry
- description: Bias or restrict results by ISO country code, viewbox, layer (address/poi/etc.), or feature type.
  name: Country And Layer Filtering
- description: /status endpoint exposes data freshness, software version, and database version for monitoring.
  name: Service Health
- description: Install on your own infrastructure from a planet.osm.pbf import; BSD-2-Clause licensed.
  name: Self-Hostable
image: https://nominatim.org/theme/images/osm-logo.svg
integrations:
- description: Python geocoding library shipping a built-in Nominatim adapter.
  name: geopy
- description: Django GIS framework with Nominatim geocoder support.
  name: GeoDjango
- description: Leaflet plugin offering a Nominatim geocoder out of the box.
  name: Leaflet Control Geocoder
- description: Web mapping library frequently paired with Nominatim for search.
  name: OpenLayers
- description: Desktop GIS plugin that batch-geocodes via Nominatim.
  name: QGIS MMQGIS
- description: Commercial hosted Nominatim-style API from MapTiler.
  name: MapTiler Cloud Geocoding
- description: Commercial Nominatim-compatible geocoding/routing platform.
  name: LocationIQ
- description: Commercial Pelias deployment (Nominatim-compatible workloads).
  name: Geocode Earth
json_schemas:
- name: Address
  property_count: 16
  slug: nominatim-address
- name: PlaceDetails
  property_count: 25
  slug: nominatim-place-details
- name: Place
  property_count: 20
  slug: nominatim-place
- name: Status
  property_count: 5
  slug: nominatim-status
json_structures:
- name: Nominatim Address Structure
  property_count: 0
  slug: nominatim-address-structure
- name: Nominatim Place Structure
  property_count: 0
  slug: nominatim-place-structure
- name: Nominatim Status Structure
  property_count: 0
  slug: nominatim-status-structure
jsonld:
- class_count: 33
  name: Nominatim Context
  property_count: 3
  slug: nominatim-context
layout: provider
modified: '2026-05-29'
name: Nominatim
nav: Providers
network: true
overview: 'Nominatim publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Deletable API, Details API, Lookup API, and 4 more. Tagged areas include Geocoding, OpenStreetMap, Maps, LocationServices, and OpenSource.


  The Nominatim catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nominatim''s developer surface includes documentation, tooling, engineering blog, and 26 more developer resources.'
plans:
- name: Nominatim Plans Pricing
  plan_count: 2
  slug: nominatim-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Nominatim Rate Limits
  slug: nominatim-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nominatim API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nominatim-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Nominatim API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: nominatim-rules
score:
  band: developing
  composite: 39.7
  delta: -6.5
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 25.0
    contract_quality: 64.2
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 28.9
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nominatim/refs/heads/main/screenshots/nominatim-2026-06-20T190357.png
security:
- kind: domain-security
  name: Nominatim Domain Security
  slug: nominatim-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: nominatim
solutions:
- description: Free hosted Nominatim under the OSMF Usage Policy (1 req/sec ceiling).
  name: OSMF Public Instance
- description: BSD-2-Clause stack you import a planet dump into; no upstream rate limits.
  name: Self-Hosted Nominatim
- description: Paid hosted offerings from MapTiler, LocationIQ, Geocode Earth and others.
  name: Commercial Hosted Nominatim
tags:
- Geocoding
- OpenStreetMap
- Maps
- LocationServices
- OpenSource
- Public APIs
use_cases:
- description: Power "find a place" search boxes in OSM-based map applications.
  name: Map Search Box
- description: Attach human-readable addresses to coordinates collected from devices, vehicles, or sensors.
  name: Reverse Geocoding For Telemetry
- description: Provide geocoding for public-interest tools where commercial pricing is a barrier.
  name: Civic Tech And Open Data
- description: When self-hosted, normalize address strings in pipelines without per-call costs.
  name: Background Address Normalisation
- description: Ground LLM agents in real-world places via an MCP server backed by Nominatim.
  name: AI Agents With Map Tools
website: https://nominatim.org/
---
