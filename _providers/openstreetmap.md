---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Openstreetmap Agentic Access
  operation_count: 18
  slug: openstreetmap-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 11
apis:
- description: The Overpass API is a read-only database engine for complex geospatial queries against the OSM dataset. Accepts Overpass QL or XML queries and returns results in XML, JSON, GeoJSON, or CSV. Safe usage
  name: OpenStreetMap Overpass API
  slug: overpass-api
- description: API version and limits
  name: OpenStreetMap Capabilities API
  slug: openstreetmap-capabilities-api
- description: Changeset management for grouped edits
  name: OpenStreetMap Changesets API
  slug: openstreetmap-changesets-api
- description: Bulk map data retrieval by bounding box
  name: OpenStreetMap Map Data API
  slug: openstreetmap-map-data-api
- description: OSM node (point) operations
  name: OpenStreetMap Nodes API
  slug: openstreetmap-nodes-api
- description: Community map notes
  name: OpenStreetMap Notes API
  slug: openstreetmap-notes-api
- description: OSM relation operations
  name: OpenStreetMap Relations API
  slug: openstreetmap-relations-api
- description: User account information
  name: OpenStreetMap Users API
  slug: openstreetmap-users-api
- description: OSM way (line/polygon) operations
  name: OpenStreetMap Ways API
  slug: openstreetmap-ways-api
- description: Forward geocoding, reverse geocoding, and OSM object lookup
  name: OpenStreetMap Geocoding API
  slug: openstreetmap-geocoding-api
- description: Server status and version information
  name: OpenStreetMap Status API
  slug: openstreetmap-status-api
artifact_total: 56
collections:
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities API
  slug: postman-openstreetmap-capabilities-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Changesets API
  slug: postman-openstreetmap-changesets-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Map Data API
  slug: postman-openstreetmap-map-data-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Nodes API
  slug: postman-openstreetmap-nodes-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Notes API
  slug: postman-openstreetmap-notes-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Relations API
  slug: postman-openstreetmap-relations-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Users API
  slug: postman-openstreetmap-users-api
- collection_type: postman
  name: OpenStreetMap API v0.6 Capabilities Ways API
  slug: postman-openstreetmap-ways-api
- collection_type: open
  name: OpenStreetMap API v0.6
  slug: open-openstreetmap-main
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openstreetmap/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openstreetmap-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openstreetmap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openstreetmap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openstreetmap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openstreetmap-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openstreetmap-foundation
- group: company
  title: ''
  type: Website
  url: https://www.openstreetmap.org/
- group: start
  title: ''
  type: Portal
  url: https://www.openstreetmap.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.openstreetmap.org/wiki/API
- group: docs
  title: ''
  type: Reference
  url: https://wiki.openstreetmap.org/wiki/API_v0.6
- group: operate
  title: ''
  type: RateLimits
  url: https://operations.osmfoundation.org/policies/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osmfoundation.org/wiki/Terms_of_Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osmfoundation.org/wiki/Privacy_Policy
- group: company
  title: ''
  type: Blog
  url: https://blog.openstreetmap.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openstreetmap
- group: commercial
  title: ''
  type: License
  url: https://www.openstreetmap.org/copyright
- group: commercial
  title: ''
  type: License
  url: https://opendatacommons.org/licenses/odbl/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.openstreetmap.org/wiki/Main_Page
- group: operate
  title: ''
  type: Forums
  url: https://community.openstreetmap.org/
- group: operate
  title: ''
  type: Support
  url: https://help.openstreetmap.org/
- group: auth
  title: ''
  type: Authentication
  url: https://www.openstreetmap.org/copyright
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openstreetmap/refs/heads/main/openapi/openstreetmap-main-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/openstreetmap/refs/heads/main/openapi/openstreetmap-nominatim-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/openstreetmap/refs/heads/main/json-schema/openstreetmap-node-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/openstreetmap/refs/heads/main/json-ld/openstreetmap-context.jsonld
created: '2026-03-18'
description: 'OpenStreetMap (OSM) is a collaborative project to create a free, editable map of the world. The OSM ecosystem exposes a family of public REST APIs: the main editing API (v0.6) for CRUD operations on map data, the Overpass API for complex read-only geospatial queries, and the Nominatim API for forward and reverse geocoding. Map data is licensed under the Open Database License (ODbL) 1.0 and tile imagery under CC BY-SA 2.0.'
features:
- Free open OSM data under ODbL license
- Public API (osm.org) free for personal/educational use
- AUP requires self-hosting or 3rd-party for production / heavy use
- 'Tile server: 2 req/sec/IP cap'
- 'Nominatim: 1 req/sec/IP cap'
- 'Overpass API: 2 concurrent/IP cap'
- 'Self-hosting: osm2pgsql + Nominatim + tile renderer (Tilemaker, Mapnik)'
- 'Third-party providers: Mapbox, MapTiler, Geoapify, Stadia Maps, TomTom'
- Editing API for contributing data (free for verified users)
- Planet downloads (XML or PBF)
- Diff replication (minutely/hourly/daily)
- Vector tiles via OpenMapTiles, Shortbread, Versatiles
- Funded by OpenStreetMap Foundation (OSMF) donations + corporate sponsors
- Data updated continuously by ~10K daily contributors
- 'Foundation policy: https://operations.osmfoundation.org/policies/'
- 'Wiki: wiki.openstreetmap.org'
finops:
- name: Openstreetmap Finops
  service_category: Open Geospatial Data
  slug: openstreetmap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openstreetmap.png
json_schemas:
- name: Capabilities
  property_count: 6
  slug: openstreetmap-capabilities
- name: Changeset
  property_count: 13
  slug: openstreetmap-changeset
- name: OpenStreetMap Node
  property_count: 11
  slug: openstreetmap-node
- name: Note
  property_count: 3
  slug: openstreetmap-note
- name: NoteCollection
  property_count: 2
  slug: openstreetmap-notecollection
- name: OSMData
  property_count: 9
  slug: openstreetmap-osmdata
- name: Relation
  property_count: 7
  slug: openstreetmap-relation
- name: User
  property_count: 8
  slug: openstreetmap-user
- name: Way
  property_count: 10
  slug: openstreetmap-way
json_structures:
- name: Openstreetmap Structure
  property_count: 0
  slug: openstreetmap-structure
jsonld:
- class_count: 21
  name: Openstreetmap Context
  property_count: 13
  slug: openstreetmap-context
layout: provider
modified: '2026-05-19'
name: OpenStreetMap
nav: Providers
network: true
overview: 'OpenStreetMap publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Capabilities API, Changesets API, Map Data API, and 7 more. Tagged areas include Geospatial, Mapping, Open Data, Geocoding, and Editing.


  The OpenStreetMap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenStreetMap''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 21 more developer resources.'
plans:
- name: Openstreetmap Plans Pricing
  plan_count: 3
  slug: openstreetmap-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 4
  name: Openstreetmap Rate Limits
  slug: openstreetmap-rate-limits
rules:
- name: OpenStreetMap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openstreetmap-jsonschema-spectral-rules
scopes:
- name: Openstreetmap Scopes
  scope_count: 7
  slug: openstreetmap-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 72.8
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openstreetmap/refs/heads/main/screenshots/openstreetmap-2026-06-20T191043.png
security:
- kind: authentication
  name: Openstreetmap Authentication
  slug: openstreetmap-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Openstreetmap Domain Security
  slug: openstreetmap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Openstreetmap Vulnerability Disclosure
  slug: openstreetmap-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: openstreetmap
tags:
- Geospatial
- Mapping
- Open Data
- Geocoding
- Editing
website: https://www.openstreetmap.org/
---
