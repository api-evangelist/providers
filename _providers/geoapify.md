---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Geoapify Agentic Access
  operation_count: 1
  slug: geoapify-agentic-access
  summary_line: 1 operation
api_count: 39
apis:
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Forward Geocoding converts text addresses into lat-long coordinates. Search addresses, cities, postcodes (or zipcodes), call the API with Javascript, Java, Python, and other languages.
  name: Geoapify Geocode API
  slug: geoapify-geocode-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Autocomplete partial addresses.
  name: Geoapify Address Autocomplete API
  slug: geoapify-address-autocomplete-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Submit asynchronous geocoding jobs and retrieve normalized geocoding batch results.
  name: Geoapify Batch Geocoding API
  slug: geoapify-batch-geocoding-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Find containing and contained administrative, postal, political, and related boundaries.
  name: Geoapify Boundaries API
  slug: geoapify-boundaries-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Retrieve terrain height and optional point-to-point distances for geographic locations.
  name: Geoapify Elevation API
  slug: geoapify-elevation-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Store GeoJSON and combine stored or generated geometries by union or intersection.
  name: Geoapify Geometry API
  slug: geoapify-geometry-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Analyze, measure, combine, transform, cluster, and generate GeoJSON geometries.
  name: Geoapify Geometry Operations API
  slug: geoapify-geometry-operations-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Get location by IP address to learn more about visitors
  name: Geoapify IP Geolocation API
  slug: geoapify-ip-geolocation-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: The Isolines API calculates isochrones and isodistances for a location. An isoline shows how far you can get from the place and area reachable within a specific time or distance.
  name: Geoapify Isoline API
  slug: geoapify-isoline-api
- baseURL: https://api.geoapify.com/v2
  baseurl_source: declared
  description: Render customizable map marker images.
  name: Geoapify Map Marker API
  slug: geoapify-map-marker-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Map Matching API snaps given geographical coordinates (GPX) to the existing road network. The API also allows you to choose a desired travel mode for cars, trucks, pedestrians, etc.
  name: Geoapify Map Matching API
  slug: geoapify-map-matching-api
- baseURL: https://maps.geoapify.com/v1
  baseurl_source: declared
  description: Here is a list of Map Tiles URLs for OpenStreetMap maps. Check our code samples of using ZYX-tile server and style.json links to create a tile layer.
  name: Geoapify Map Tiles API
  slug: geoapify-map-tiles-api
- baseURL: https://api.geoapify.com/v2
  baseurl_source: declared
  description: Retrieve details, geometry, surroundings, and reachability features for a place.
  name: Geoapify Place Details API
  slug: geoapify-place-details-api
- baseURL: https://api.geoapify.com/v2
  baseurl_source: declared
  description: Retrieve categorized place information for coordinates or an OpenStreetMap object.
  name: Geoapify Place Info API
  slug: geoapify-place-info-api
- baseURL: https://api.geoapify.com/v2
  baseurl_source: declared
  description: The Places API helps to query places, amenities, and points of interest using more than 400 categories. We use the OpenStreetMap as the data source. Cache/store results with no limits.
  name: Geoapify Places API
  slug: geoapify-places-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Resolve coordinates to addresses.
  name: Geoapify Reverse Geocoding API
  slug: geoapify-reverse-geocoding-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Route Matrix API to calculate the time-distance matrix between multiple points
  name: Geoapify Route Matrix API
  slug: geoapify-route-matrix-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Route Planner API to calculate delivery route and manage agents
  name: Geoapify Route Planner API
  slug: geoapify-route-planner-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: A Routing API to calculate route and directions for vehicles of many types, including cars, trucks, buses, bicycles, pedestrians, and hikers.
  name: Geoapify Routing API
  slug: geoapify-routing-api
- baseURL: https://maps.geoapify.com/v1
  baseurl_source: declared
  description: Render static map images with markers, geometries, and GeoJSON overlays.
  name: Geoapify Static Maps API
  slug: geoapify-static-maps-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: The Timezone API returns the time zone, exact UTC offset, and local time at coordinates, and lists daylight saving time changes.
  name: Geoapify Timezone API
  slug: geoapify-timezone-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: The Batch requests let to pack multiple API requests into one API call. As a result, pay up to 50% less for geospatial operations. Cache/store results with no limits.
  name: Geoapify Batch API
  slug: geoapify-batch-api
- baseURL: https://api.geoapify.com/v1
  baseurl_source: declared
  description: Search and list postcode results.
  name: Geoapify Post Code API
  slug: geoapify-post-code-api
artifact_total: 97
collections:
- collection_type: open
  name: Geoapify Forward Geocoding API
  slug: open-geoapify-forward-geocoding-api
- collection_type: open
  name: Geoapify Forward Geocoding Geocode API
  slug: open-geoapify-geocode-api
common:
- group: design
  href: https://artifacts.apis.io/geoapify/rules/geoapify-rules.yml
  title: ''
  type: Spectral
  url: rules/geoapify-rules.yml
- group: design
  href: https://artifacts.apis.io/geoapify/rules/geoapify-geoapify-openapi-specs-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/geoapify-geoapify-openapi-specs-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/geoapify/json-ld/geoapify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/geoapify-context.jsonld
- group: design
  href: https://artifacts.apis.io/geoapify/vocabulary/geoapify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/geoapify-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/geoapify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/geoapify/data-model/geoapify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geoapify-data-model.yml
- group: design
  href: https://artifacts.apis.io/geoapify/components/geoapify-components.yml
  title: ''
  type: Components
  url: components/geoapify-components.yml
- group: operate
  href: https://artifacts.apis.io/geoapify/changelog/geoapify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/geoapify-changelog.yml
- group: design
  href: https://artifacts.apis.io/geoapify/conventions/geoapify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/geoapify-conventions.yml
- group: operate
  href: https://artifacts.apis.io/geoapify/lifecycle/geoapify-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/geoapify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/geoapify/lifecycle/geoapify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geoapify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/geoapify/errors/geoapify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geoapify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/geoapify/conformance/geoapify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geoapify-conformance.yml
- group: build
  href: https://artifacts.apis.io/geoapify/mcp/geoapify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/geoapify-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/geoapify/hosts/geoapify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geoapify-hosts.yml
- group: build
  href: https://artifacts.apis.io/geoapify/integrations/geoapify-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/geoapify-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/geoapify/vendors/geoapify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geoapify-vendors.yml
- group: build
  href: https://artifacts.apis.io/geoapify/packages/geoapify-packages.yml
  title: ''
  type: SDKs
  url: packages/geoapify-packages.yml
- group: build
  href: https://artifacts.apis.io/geoapify/packages/geoapify-packages.yml
  title: ''
  type: Packages
  url: packages/geoapify-packages.yml
- group: auth
  href: https://artifacts.apis.io/geoapify/authentication/geoapify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geoapify-authentication.yml
- group: other
  href: https://artifacts.apis.io/geoapify/capabilities/geoapify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geoapify-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/geoapify/plans/geoapify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geoapify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/geoapify/rate-limits/geoapify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geoapify-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geoapify/finops/geoapify-finops.yml
  title: ''
  type: FinOps
  url: finops/geoapify-finops.yml
- group: agent
  href: https://artifacts.apis.io/geoapify/agentic-access/geoapify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geoapify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/geoapify/security/geoapify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoapify-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geoapify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geoapify
- group: company
  title: ''
  type: Website
  url: https://www.geoapify.com/
- group: start
  title: ''
  type: Signup
  url: https://myprojects.geoapify.com/register
- group: agent
  title: ''
  type: MCPServer
  url: https://api.geoapify.com/v1/mcp
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://www.geoapify.com/mcp/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/geoapify/geoapify-openapi-specs/blob/e8255e614648084d86bae2155c20347d5203ec1d/ruleset.spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.geoapify.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.geoapify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.geoapify.com/tutorials/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.geoapify.com/get-started-with-maps-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geoapify.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://myprojects.geoapify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.geoapify.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.geoapify.com/rss.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.geoapify.com/news-and-updates/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geoapify.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geoapify.com/privacy-policy/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/geoapify
created: '2024-01-01'
description: 'Geoapify Location Platform, operated by KEPTAGO LTD (Paphos, Cyprus), offers EU-hosted location APIs built on OpenStreetMap and other open data: forward, reverse and batch geocoding, address autocomplete, places and place details, boundaries, postcode and IP geolocation, timezone, routing, route matrix, route planner, map matching, isolines, elevation, GeoJSON geometry operations, map tiles, static maps and marker icons. All 23 APIs are described by provider-published OpenAPI 3.1 documents in a machine-readable catalog, authenticate with an API key (query parameter or x-api-key header), and are mirrored on an EU-only processing endpoint (api-eu.geoapify.com). A remote MCP server at api.geoapify.com/v1/mcp exposes 12 tools for AI assistants. Pricing is credit-based with a free tier of 3,000 credits per day.'
features:
- 'Free: 3K credits/day, 5 RPS, limited commercial use'
- 'API 10: $59/mo, 10K credits/day, 12 RPS'
- 'API 25: $109/mo, 25K credits/day, 15 RPS'
- 'API 50: $179/mo, 50K credits/day, 20 RPS'
- 'API 100: $299/mo, 100K credits/day, 25 RPS'
- 'API 250: $609/mo, 250K credits/day, 30 RPS'
- 'Custom from $860/mo: unmetered, dedicated endpoint'
- Geocoding API (forward + reverse)
- Routing API (driving, walking, cycling, truck)
- Isochrones up to 15-120 min by tier
- Place Details API
- Map Tiles API
- Address Autocomplete
- Static Maps API
- Boundaries API
- OpenStreetMap-based data with global coverage
finops:
- has_sources: true
  method: generated
  name: Geoapify Finops
  primary_unit: ''
  service_category: Maps
  slug: geoapify-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geoapify.png
json_schemas:
- name: AddressAutocompleteXmlResponse
  property_count: 2
  slug: geoapify-address-autocomplete-xml-response
- name: BatchCompletedResponse
  property_count: 5
  slug: geoapify-batch-completed-response
- name: BatchGeocodeSearchResults
  property_count: 0
  slug: geoapify-batch-geocode-search-results
- name: BatchGeocodeSearchSubmitRequest
  property_count: 0
  slug: geoapify-batch-geocode-search-submit-request
- name: BatchPendingResponse
  property_count: 3
  slug: geoapify-batch-pending-response
- name: BatchReverseGeocodeResults
  property_count: 0
  slug: geoapify-batch-reverse-geocode-results
- name: BatchReverseGeocodeSubmitRequest
  property_count: 0
  slug: geoapify-batch-reverse-geocode-submit-request
- name: BatchSubmitRequest
  property_count: 5
  slug: geoapify-batch-submit-request
- name: BoundaryFeatureCollection
  property_count: 2
  slug: geoapify-boundary-feature-collection
- name: CalculateRouteMatrixToolCallRequest
  property_count: 4
  slug: geoapify-calculate-route-matrix-tool-call-request
- name: CalculateRouteMatrixToolCallResponse
  property_count: 0
  slug: geoapify-calculate-route-matrix-tool-call-response
- name: ElevationFeatureCollection
  property_count: 2
  slug: geoapify-elevation-feature-collection
- name: ElevationJsonResponse
  property_count: 1
  slug: geoapify-elevation-json-response
- name: ElevationRequest
  property_count: 4
  slug: geoapify-elevation-request
- name: FeatureCollection
  property_count: 2
  slug: geoapify-feature-collection
- name: GeoJsonInput
  property_count: 0
  slug: geoapify-geo-json-input
- name: GeocodingJsonResponse
  property_count: 2
  slug: geoapify-geocoding-json-response
- name: GeometryOperationRequest
  property_count: 24
  slug: geoapify-geometry-operation-request
- name: GeometryOperationResponse
  property_count: 2
  slug: geoapify-geometry-operation-response
- name: IpGeolocationResponse
  property_count: 8
  slug: geoapify-ip-geolocation-response
- name: IsolineFeatureCollection
  property_count: 4
  slug: geoapify-isoline-feature-collection
- name: MapLibreStyle
  property_count: 7
  slug: geoapify-map-libre-style
- name: MapMatchingFeatureCollection
  property_count: 4
  slug: geoapify-map-matching-feature-collection
- name: MapMatchingRequest
  property_count: 6
  slug: geoapify-map-matching-request
- name: PlaceDetailsFeatureCollection
  property_count: 2
  slug: geoapify-place-details-feature-collection
- name: PlacesPostRequest
  property_count: 8
  slug: geoapify-places-post-request
- name: PostcodeFeatureCollection
  property_count: 3
  slug: geoapify-postcode-feature-collection
- name: PostcodeJsonResponse
  property_count: 1
  slug: geoapify-postcode-json-response
- name: ReverseGeocodingFeatureCollection
  property_count: 3
  slug: geoapify-reverse-geocoding-feature-collection
- name: ReverseGeocodingXmlResponse
  property_count: 2
  slug: geoapify-reverse-geocoding-xml-response
- name: RouteMatrixRequest
  property_count: 8
  slug: geoapify-route-matrix-request
- name: RouteMatrixResponse
  property_count: 10
  slug: geoapify-route-matrix-response
- name: RoutePlannerRequest
  property_count: 10
  slug: geoapify-route-planner-request
- name: RoutePlannerResponse
  property_count: 0
  slug: geoapify-route-planner-response
- name: RoutingFeatureCollection
  property_count: 4
  slug: geoapify-routing-feature-collection
- name: RoutingJsonResponse
  property_count: 3
  slug: geoapify-routing-json-response
- name: StaticMapRequest
  property_count: 16
  slug: geoapify-static-map-request
- name: StoredGeometryResponse
  property_count: 1
  slug: geoapify-stored-geometry-response
- name: TextGeocodingFeatureCollection
  property_count: 3
  slug: geoapify-text-geocoding-feature-collection
- name: TimezoneResult
  property_count: 5
  slug: geoapify-timezone-result
- name: TimezoneTransitionsResult
  property_count: 6
  slug: geoapify-timezone-transitions-result
json_structures:
- name: Geoapify Structure
  property_count: 0
  slug: geoapify-structure
jsonld:
- class_count: 120
  name: Geoapify Context
  property_count: 322
  slug: geoapify-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-11-05'
name: Geoapify
nav: Providers
network: true
overview: 'Geoapify publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Geocode API, Address Autocomplete API, Batch Geocoding API, and 20 more. Tagged areas include Geocoding, Geospatial, Location, Maps, and Routing.


  The Geoapify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Geoapify''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, pricing, and 38 more developer resources.'
plans:
- name: Geoapify Plans Pricing
  plan_count: 7
  slug: geoapify-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 15
  name: Geoapify Rate Limits
  slug: geoapify-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Geoapify — geoapify openapi specs rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: geoapify-geoapify-openapi-specs-spectral-rules
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Geoapify API Rules
  rule_count: 67
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 21
  slug: geoapify-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 37
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 35.0
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 74.4
    developer_ergonomics: 56.5
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 95.7
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/geoapify/geoapify-2026-06-20T181748.png
security:
- kind: authentication
  name: Geoapify Authentication
  slug: geoapify-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Geoapify Domain Security
  slug: geoapify-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: geoapify-batch-geocode-addresses
  slug: geoapify-batch-geocode-addresses
- name: geoapify-find-places-nearby
  slug: geoapify-find-places-nearby
- name: geoapify-geocode-and-route
  slug: geoapify-geocode-and-route
- name: geoapify-render-static-map
  slug: geoapify-render-static-map
slug: geoapify
tags:
- Geocoding
- Geospatial
- Location
- Maps
- Routing
- Places
- Timezone
- MCP
- GeoJSON
- OpenStreetMap
- Static Maps
- Isolines
website: https://www.geoapify.com/
---
