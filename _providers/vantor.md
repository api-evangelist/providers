---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 2
  name: Maxar Technologies Agentic Access
  operation_count: 43
  slug: maxar-technologies-agentic-access
  summary_line: 43 operations · 18 acting · 2 human-in-the-loop
- acting_count: 24
  human_in_the_loop: 2
  name: Vantor Agentic Access
  operation_count: 59
  slug: vantor-agentic-access
  summary_line: 59 operations · 24 acting · 2 human-in-the-loop
api_count: 31
apis:
- description: Vivid is Maxar's cloud-free, color-balanced basemap product — a global mosaic refreshed from the WorldView archive. The Vivid Basemap API exposes the basemap as OGC tile and feature services through t
  name: Maxar Vivid Basemap API
  slug: basemaps
- description: Legacy Maxar Content Catalog API — the canonical search index against the WorldView / GeoEye / IKONOS / QuickBird archive. Generated from Maxar's published OpenAPI spec (doc.content.maxar.com/maxar-co
  name: Maxar Content Catalog API
  slug: catalog
- description: Free, public STAC (SpatioTemporal Asset Catalog) of pre- and post-event high-resolution Maxar imagery published in support of emergency planning, risk assessment, damage assessment and recovery. Hoste
  name: Maxar Open Data STAC Catalog
  slug: open-data-stac
- description: Transform API exposes image transformation primitives (reproject, tile, mosaic, format-convert) over Maxar imagery. A TypeScript client (@maxar/transform-api) and OpenLayers helpers are published from
  name: Maxar Transform API
  slug: transform-api
- description: OAuth2-style token service that mints bearer access tokens (and 180-day default API keys) for use against all Vantor Hub / MGP APIs.
  name: Maxar Technologies Authentication / Token Service
  slug: authentication
- description: OGC-compliant WFS / WMS / WMTS streaming services for delivering online imagery strips into web mapping clients and GIS workflows.
  name: Maxar Technologies Streaming Imagery API
  slug: streaming-imagery
- description: OGC service delivering Maxar Vivid basemap products and their metadata for cartographic and analytic use.
  name: Maxar Technologies Streaming Basemap API
  slug: streaming-basemap
- description: Streams 3D surface models derived from Maxar's stereo and tri-stereo collections for visualization and 3D analysis.
  name: Maxar Technologies Streaming 3D API
  slug: streaming-3d
- description: Register Areas of Interest and receive alerts when new imagery or analytic outputs match. Drives standing tip-and-cue workflows over the Maxar catalog.
  name: Maxar Technologies Monitoring API
  slug: monitoring
- description: Request new imagery collection from the WorldView Legion and legacy WorldView constellations within a target geometry and time window. Supports Fastview and Flexview tasking tiers.
  name: Maxar Technologies Tasking API
  slug: tasking
- description: Server-side raster processing - band manipulation, classification, and index models (NDVI, NDWI, etc.) - composed as analysis graphs over the Maxar catalog.
  name: Maxar Technologies Raster Analytics API
  slug: raster-analytics
- description: Vector deliveries of change monitoring outputs through OGC WMS / WMTS for downstream analytic and GIS consumption.
  name: Maxar Technologies Vector Analytics API
  slug: vector-analytics
- description: Official Python SDK (maxar-platform on PyPI) wrapping the MGP / Vantor Hub APIs for discovery, ordering, monitoring, streaming, and tasking workflows.
  name: Maxar Technologies Geospatial Platform Python SDK
  slug: python-sdk
- description: Public Postman workspace documenting the Maxar Geospatial Platform API surface for quick exploration and testing.
  name: Maxar Technologies MGP Postman Collection
  slug: postman
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Accounts API from Vantor — 2 operation(s) for accounts.
  name: Vantor Accounts API
  slug: vantor-accounts-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The API Keys API from Vantor — 2 operation(s) for api keys.
  name: Vantor API Keys API
  slug: vantor-api-keys-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Authentication API from Vantor — 2 operation(s) for authentication.
  name: Vantor Authentication API
  slug: vantor-authentication-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: Browse and inspect collections
  name: Vantor Collections API
  slug: vantor-collections-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Credits API from Vantor — 1 operation(s) for credits.
  name: Vantor Credits API
  slug: vantor-credits-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Deliveries API from Vantor — 1 operation(s) for deliveries.
  name: Vantor Deliveries API
  slug: vantor-deliveries-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Discovery API from Vantor — 5 operation(s) for discovery.
  name: Vantor Discovery API
  slug: vantor-discovery-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Estimates API from Vantor — 1 operation(s) for estimates.
  name: Vantor Estimates API
  slug: vantor-estimates-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Events API from Vantor — 1 operation(s) for events.
  name: Vantor Events API
  slug: vantor-events-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Feasibility API from Vantor — 1 operation(s) for feasibility.
  name: Vantor Feasibility API
  slug: vantor-feasibility-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Image API from Vantor — 1 operation(s) for image.
  name: Vantor Image API
  slug: vantor-image-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: Inspect tokens
  name: Vantor Introspection API
  slug: vantor-introspection-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: Retrieve individual STAC items
  name: Vantor Items API
  slug: vantor-items-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Monitors API from Vantor — 2 operation(s) for monitors.
  name: Vantor Monitors API
  slug: vantor-monitors-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Ordering API from Vantor — 6 operation(s) for ordering.
  name: Vantor Ordering API
  slug: vantor-ordering-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Orders API from Vantor — 2 operation(s) for orders.
  name: Vantor Orders API
  slug: vantor-orders-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: Search and filter imagery and derivatives
  name: Vantor Search API
  slug: vantor-search-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Subscriptions API from Vantor — 1 operation(s) for subscriptions.
  name: Vantor Subscriptions API
  slug: vantor-subscriptions-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Tasks API from Vantor — 2 operation(s) for tasks.
  name: Vantor Tasks API
  slug: vantor-tasks-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: Issue and refresh access tokens
  name: Vantor Tokens API
  slug: vantor-tokens-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The Users API from Vantor — 2 operation(s) for users.
  name: Vantor Users API
  slug: vantor-users-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The WFS API from Vantor — 1 operation(s) for wfs.
  name: Vantor WFS API
  slug: vantor-wfs-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The WMS API from Vantor — 1 operation(s) for wms.
  name: Vantor WMS API
  slug: vantor-wms-api
- baseURL: https://securewatch.maxar.com/earthservice
  baseurl_source: declared
  description: The WMTS API from Vantor — 1 operation(s) for wmts.
  name: Vantor WMTS API
  slug: vantor-wmts-api
artifact_total: 112
collections:
- collection_type: postman
  name: Vantor Hub Account Services Accounts API
  slug: postman-maxar-technologies-accounts-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts API Keys API
  slug: postman-maxar-technologies-api-keys-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Collections API
  slug: postman-maxar-technologies-collections-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Credits API
  slug: postman-maxar-technologies-credits-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Deliveries API
  slug: postman-maxar-technologies-deliveries-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Estimates API
  slug: postman-maxar-technologies-estimates-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Events API
  slug: postman-maxar-technologies-events-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Feasibility API
  slug: postman-maxar-technologies-feasibility-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Image API
  slug: postman-maxar-technologies-image-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Introspection API
  slug: postman-maxar-technologies-introspection-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Items API
  slug: postman-maxar-technologies-items-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Monitors API
  slug: postman-maxar-technologies-monitors-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Orders API
  slug: postman-maxar-technologies-orders-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Search API
  slug: postman-maxar-technologies-search-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Subscriptions API
  slug: postman-maxar-technologies-subscriptions-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Tasks API
  slug: postman-maxar-technologies-tasks-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Tokens API
  slug: postman-maxar-technologies-tokens-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts Users API
  slug: postman-maxar-technologies-users-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts WFS API
  slug: postman-maxar-technologies-wfs-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts WMS API
  slug: postman-maxar-technologies-wms-api
- collection_type: postman
  name: Vantor Hub Account Services Accounts WMTS API
  slug: postman-maxar-technologies-wmts-api
- collection_type: open
  name: Vantor Hub Account Services API
  slug: open-admin
- collection_type: open
  name: Vantor Hub Authentication API
  slug: open-authentication
- collection_type: open
  name: Vantor Hub Discovery API
  slug: open-discovery
- collection_type: open
  name: Vantor Hub Account Services Accounts API
  slug: open-maxar-technologies-accounts-api
- collection_type: open
  name: Vantor Hub Account Services Accounts API Keys API
  slug: open-maxar-technologies-api-keys-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Collections API
  slug: open-maxar-technologies-collections-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Credits API
  slug: open-maxar-technologies-credits-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Deliveries API
  slug: open-maxar-technologies-deliveries-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Estimates API
  slug: open-maxar-technologies-estimates-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Events API
  slug: open-maxar-technologies-events-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Feasibility API
  slug: open-maxar-technologies-feasibility-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Image API
  slug: open-maxar-technologies-image-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Introspection API
  slug: open-maxar-technologies-introspection-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Items API
  slug: open-maxar-technologies-items-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Monitors API
  slug: open-maxar-technologies-monitors-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Orders API
  slug: open-maxar-technologies-orders-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Search API
  slug: open-maxar-technologies-search-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Subscriptions API
  slug: open-maxar-technologies-subscriptions-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Tasks API
  slug: open-maxar-technologies-tasks-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Tokens API
  slug: open-maxar-technologies-tokens-api
- collection_type: open
  name: Vantor Hub Account Services Accounts Users API
  slug: open-maxar-technologies-users-api
- collection_type: open
  name: Vantor Hub Account Services Accounts WFS API
  slug: open-maxar-technologies-wfs-api
- collection_type: open
  name: Vantor Hub Account Services Accounts WMS API
  slug: open-maxar-technologies-wms-api
- collection_type: open
  name: Vantor Hub Account Services Accounts WMTS API
  slug: open-maxar-technologies-wmts-api
- collection_type: open
  name: Maxar Geospatial Platform Monitoring API
  slug: open-monitoring
- collection_type: open
  name: Maxar Geospatial Platform Ordering API
  slug: open-ordering
- collection_type: open
  name: Maxar Geospatial Platform Streaming API
  slug: open-streaming
- collection_type: open
  name: Maxar Geospatial Platform Tasking API
  slug: open-tasking
common:
- group: company
  title: ''
  type: Blog
  url: https://vantor.com/blog/
- group: other
  href: https://artifacts.apis.io/vantor/capabilities/vantor-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vantor-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/vantor/capabilities/maxar-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/maxar-technologies-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/maxar-technologies/overview
- group: agent
  href: https://artifacts.apis.io/vantor/agentic-access/maxar-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/maxar-technologies-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vantor/security/maxar-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maxar-technologies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vantor/authentication/maxar-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maxar-technologies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vantor.com/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.maxar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.vantor.com/
- group: start
  title: ''
  type: LegacyDeveloperPortal
  url: https://pro.maxar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.vantor.com/docs/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Maxar-Corp/maxar-geospatial-platform
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Maxar-Corp/maxar-geospatial-platform-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Maxar-Corp/maxar-geospatial-platform-r
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Maxar-Corp/maxarcat
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/MGP-SDK/
- group: build
  title: ''
  type: Package
  url: https://cran.r-project.org/web/packages/MGPSDK/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Maxar-Corp
- group: build
  title: ''
  type: GitHubLegacy
  url: https://github.com/DigitalGlobe
- group: build
  title: ''
  type: GitHubAnalytics
  url: https://github.com/maxar-analytics
- group: operate
  title: ''
  type: StatusPage
  url: https://hub-status.vantor.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://hub.vantor.com/docs/release-notes
- group: build
  title: ''
  type: SampleProjects
  url: https://hub.vantor.com/sample-projects/
- group: build
  title: ''
  type: APICollection
  url: https://hub.vantor.com/docs/developer-tools/api-collection
- group: start
  title: ''
  type: Login
  url: https://hub.vantor.com/
- group: start
  title: ''
  type: Login
  url: https://discover.vantor.com/
- group: operate
  title: ''
  type: Contact
  url: https://vantor.com/get-started/
- group: other
  title: ''
  type: OpenData
  url: https://github.com/opengeos/maxar-open-data
- group: other
  title: ''
  type: SuccessorIntelligence
  url: https://vantor.com/
- group: other
  title: ''
  type: SuccessorSpaceSystems
  url: https://en.wikipedia.org/wiki/Lanteris_Space_Systems
- group: other
  title: ''
  type: Owner
  url: https://www.adventinternational.com/
- group: other
  title: ''
  type: AcquirerSpaceSystems
  url: https://www.intuitivemachines.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Vantor_(company)
- group: other
  title: ''
  type: WikipediaLanteris
  url: https://en.wikipedia.org/wiki/Lanteris_Space_Systems
- group: commercial
  href: https://artifacts.apis.io/vantor/plans/maxar-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/maxar-technologies-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vantor/rate-limits/maxar-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maxar-technologies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vantor/finops/maxar-technologies-finops.yml
  title: ''
  type: FinOps
  url: finops/maxar-technologies-finops.yml
- group: design
  href: https://artifacts.apis.io/vantor/vocabulary/maxar-technologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maxar-technologies-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vantor/json-ld/maxar-technologies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/maxar-technologies-context.jsonld
created: '2026-05-22'
description: 'Maxar Technologies was a publicly traded Earth-imaging and space-systems company formed from the 2017 merger of MacDonald, Dettwiler and Associates (MDA) with DigitalGlobe (founded 1992 in Oakland, California). In December 2022 private-equity firm Advent International agreed to take Maxar private in a USD 6.4 billion cash deal that closed in May 2023, after which Advent split the company into two operating units: Maxar Intelligence (imagery and geospatial software in Westminster, Colorado) and Maxar Space Systems (satellite manufacturing in Palo Alto, California). On 1 October 2025 both units rebranded — Maxar Intelligence became Vantor and Maxar Space Systems became Lanteris Space Systems. On 13 January 2026 Intuitive Machines completed the acquisition of Lanteris from Advent for approximately USD 800 million, leaving Vantor as the sole remaining Advent-owned successor of the Maxar brand. The public developer surface for the original Maxar APIs — imagery search, streaming
  (WMS/WMTS/WFS), tasking, ordering, monitoring, authentication and account services — is now delivered through the Vantor Hub (hub.vantor.com / pro.maxar.com) and the Maxar Geospatial Platform (MGP) SDKs (Python, Java, R). The Maxar Open Data Program continues to publish a public STAC catalog of pre-/post-event high-resolution imagery on AWS Open Data.'
examples:
- key_count: 2
  name: Auth Token Request
  slug: auth-token-request
- key_count: 5
  name: Auth Token Response
  slug: auth-token-response
- key_count: 5
  name: Discovery Search Request
  slug: discovery-search-request
- key_count: 4
  name: Discovery Search Response
  slug: discovery-search-response
- key_count: 4
  name: Monitor Create Request
  slug: monitor-create-request
- key_count: 5
  name: Order Place Request
  slug: order-place-request
- key_count: 7
  name: Order Place Response
  slug: order-place-response
- key_count: 9
  name: Task Submit Request
  slug: task-submit-request
finops:
- has_sources: false
  method: generated
  name: Maxar Technologies Finops
  primary_unit: ''
  service_category: ''
  slug: maxar-technologies-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxar-technologies.png
json_schemas:
- name: Maxar Monitor
  property_count: 6
  slug: maxar-technologies-monitor
- name: Maxar Order
  property_count: 8
  slug: maxar-technologies-order
- name: Maxar STAC Item
  property_count: 9
  slug: maxar-technologies-stac-item
- name: Maxar Tasking Request
  property_count: 6
  slug: maxar-technologies-task
json_structures:
- name: Maxar Technologies Order Structure
  property_count: 0
  slug: maxar-technologies-order-structure
- name: Maxar Technologies Stac Item Structure
  property_count: 0
  slug: maxar-technologies-stac-item-structure
- name: Maxar Technologies Task Structure
  property_count: 0
  slug: maxar-technologies-task-structure
jsonld:
- class_count: 28
  name: Maxar Technologies Context
  property_count: 0
  slug: maxar-technologies-context
layout: provider
modified: '2026-10-06'
name: Vantor
nav: Providers
network: true
overview: 'Vantor publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Authentication API, and 35 more. Tagged areas include Satellite Imagery, Earth Observation, Geospatial, Remote Sensing, and Spatial Intelligence.


  The Vantor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vantor''s developer surface includes engineering blog, authentication, documentation, GitHub presence, changelog, and 35 more developer resources.'
plans:
- name: Maxar Technologies Plans Pricing
  plan_count: 4
  slug: maxar-technologies-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Maxar Technologies Rate Limits
  slug: maxar-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Vantor — maxar technologies jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: maxar-technologies-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Vantor — maxar technologies rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: maxar-technologies-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 14.5
    contract_governance: 27.3
    contract_quality: 51.4
    developer_ergonomics: 44.8
    discoverability: 71.4
    operational_transparency: 28.9
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 24
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vantor/maxar-technologies-2026-06-20T185049.png
security:
- kind: authentication
  name: Maxar Technologies Authentication
  slug: maxar-technologies-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Maxar Technologies Domain Security
  slug: maxar-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vantor
tags:
- Satellite Imagery
- Earth Observation
- Geospatial
- Remote Sensing
- Spatial Intelligence
- Defense
- Intelligence
- WorldView
- STAC
- OGC
- WMS
- WMTS
- WFS
- Tasking
- Basemaps
- Vantor
- Lanteris
- Advent International
- Private Equity
- Satellite
website: https://vantor.com/
---
