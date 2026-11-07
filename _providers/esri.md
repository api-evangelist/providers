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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Esri Agentic Access
  operation_count: 15
  slug: esri-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- description: The Esri ArcGIS Platform API is a set of REST APIs and SDKs from Esri, provider of the ArcGIS GIS suite. It enables developers to integrate Esri's mapping, geocoding, routing, and spatial analysis ser
  name: Esri ArcGIS Platform API
  slug: esri-arcgis-platform-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: The Auth API from Esri — 1 operation(s) for auth.
  name: Esri Auth API
  phrasing_intents:
  - id: getOAuthToken
    intent: Get an ArcGIS access token via OAuth
    question: How do I get an ArcGIS access token for my app using its client ID and secret?
  phrasing_ops: 1
  slug: esri-auth-api
- baseURL: https://geocode-api.arcgis.com/arcgis/rest/services
  baseurl_source: declared
  description: The Geocoding API from Esri — 4 operation(s) for geocoding.
  name: Esri Geocoding API
  phrasing_intents:
  - id: findAddressCandidates
    intent: Match an address on the World GeocodeServer
    question: Can I send street, city, region and postal code separately to the World GeocodeServer and get candidate matches back?
  - id: geocodeAddresses
    intent: Batch geocode a list of addresses
    question: How do I geocode hundreds of addresses in one request instead of one at a time?
  - id: reverseGeocode
    intent: Reverse geocode a point on the World GeocodeServer
    question: Can I limit World GeocodeServer reverse geocoding to certain feature types, like a point of interest or street intersection?
  - id: suggestAddresses
    intent: Autocomplete a partial address
    question: How do I show address autocomplete suggestions while a user is still typing?
  - id: getFindAddressCandidates
    intent: Geocode an address to coordinates
    question: How do I convert an address like 380 New York St, Redlands into coordinates with a match score?
  - id: getReverseGeocode
    intent: Turn coordinates into a readable address
    question: What address is closest to a latitude and longitude I have?
  phrasing_ops: 6
  slug: esri-geocoding-api
- baseURL: https://route-api.arcgis.com/arcgis/rest/services
  baseurl_source: declared
  description: The Routing API from Esri — 1 operation(s) for routing.
  name: Esri Routing API
  phrasing_intents:
  - id: solveRoute
    intent: Calculate a route between stops
    question: How do I get driving directions between several stops?
  phrasing_ops: 1
  slug: esri-routing-api
- description: The ArcGIS Maps SDK for JavaScript enables web developers to build compelling 2D and 3D mapping applications with interactive visualizations, spatial analysis tools, geocoding, routing, and portal con
  name: ArcGIS Maps SDK for JavaScript
  slug: esri-arcgis-maps-sdk-javascript
- description: 'The ArcGIS API for Python provides a Pythonic interface for GIS capabilities including data management, spatial analysis, geocoding, routing, and administration of ArcGIS Online and ArcGIS Enterprise '
  name: ArcGIS API for Python
  slug: esri-arcgis-api-for-python
- description: A GraphQL API for ArcGIS Urban - urban models, plans, projects, branches, parcels, zones, spaces, building types, indicators, metrics, overlays, viewpoints and scenario analyses (elevation profile, li
  name: ArcGIS Urban API
  slug: esri-arcgis-urban-api
- description: Esri-hosted Model Context Protocol server exposing ArcGIS Location Services - geocoding, reverse geocoding, routing, elevation, static maps and GeoEnrichment - as seven MCP tools. Remote HTTP transpor
  name: MCP for ArcGIS Location Services (beta)
  slug: esri-arcgis-mcp-location-services
- description: ArcGIS Server publishes any map or feature service through the OGC interfaces - WMS, WFS, WCS, WMTS and KML. The two capabilities documents registered here were fetched from Esri's public ArcGIS Serve
  name: ArcGIS Server OGC Web Services
  slug: esri-arcgis-ogc-services
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: Points of interest search and retrieval
  name: Esri Places API
  phrasing_intents:
  - id: findPlacesNearPoint
    intent: Find points of interest near a location
    question: How do I find restaurants or other places within walking distance of a coordinate?
  - id: getPlaceDetails
    intent: Get details for a place
    question: How can I get a place's phone number and opening hours from its place ID?
  phrasing_ops: 2
  slug: esri-places-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: Portal items, users, groups, and organizational management
  name: Esri Portal API
  phrasing_intents:
  - id: getPortalSelf
    intent: Get my organization's portal information
    question: How do I see my ArcGIS organization's portal name, description and thumbnail?
  - id: getUser
    intent: Get a portal user's profile
    question: Can I look up the profile of a specific member of our ArcGIS organization?
  - id: getUserItems
    intent: List content items a user owns
    question: How do I list all the maps, layers and apps a particular user owns?
  - id: getItem
    intent: Get a portal item's details
    question: What information can I get about a single map or layer item by its ID?
  - id: searchPortal
    intent: Search portal items, groups and users
    question: Can I search across the whole portal for feature services owned by a certain person?
  phrasing_ops: 5
  slug: esri-portal-api
artifact_total: 42
asyncapis:
- description: ''
  name: Esri Webhooks
  slug: esri-webhooks
collections:
- collection_type: open
  name: Esri ArcGIS Location Services Auth API
  slug: open-esri-auth-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Geocoding API
  slug: open-esri-geocoding-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Routing API
  slug: open-esri-routing-api
- collection_type: open
  name: Esri ArcGIS Location Services API
  slug: open-esri
common:
- group: design
  href: https://artifacts.apis.io/esri/rules/esri-rules.yml
  title: ''
  type: Spectral
  url: rules/esri-rules.yml
- group: design
  href: https://artifacts.apis.io/esri/json-ld/esri-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/esri-context.jsonld
- group: design
  href: https://artifacts.apis.io/esri/vocabulary/esri-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/esri-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/esri/wsdl/esri-route-api-service-catalog.wsdl
  title: ''
  type: WSDL
  url: wsdl/esri-route-api-service-catalog.wsdl
- group: other
  href: https://artifacts.apis.io/esri/wsdl/esri-geocode-api-service-catalog.wsdl
  title: ''
  type: WSDL
  url: wsdl/esri-geocode-api-service-catalog.wsdl
- group: other
  href: https://artifacts.apis.io/esri/hosts/esri-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esri-hosts.yml
- group: build
  href: https://artifacts.apis.io/esri/integrations/esri-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/esri-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/esri/vendors/esri-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esri-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://mediaspace.esri.com/media/t/1_qay3ob9a?co3=true
- group: other
  href: https://artifacts.apis.io/esri/overlays/esri-arcgis-geocoding-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/esri-arcgis-geocoding-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/esri/overlays/esri-arcgis-places-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/esri-arcgis-places-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/esri/overlays/esri-arcgis-portal-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/esri-arcgis-portal-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/esri/agentic-access/esri-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/esri-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/esri/security/esri-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esri-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/esri/authentication/esri-authentication.yml
  title: ''
  type: Authentication
  url: authentication/esri-authentication.yml
- group: auth
  href: https://artifacts.apis.io/esri/scopes/esri-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/esri-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esri
- group: company
  title: ''
  type: Website
  url: https://www.esri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.arcgis.com/
- group: other
  title: ''
  type: Alias
  url: https://github.com/api-evangelist/esri-arcgis
- group: agent
  href: https://artifacts.apis.io/esri/mcp/esri-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/esri-mcp.yml
- group: build
  href: https://artifacts.apis.io/esri/mcp/esri-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/esri-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/esri/llms/esri-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/esri-llms.txt
- group: agent
  href: https://artifacts.apis.io/esri/well-known/esri-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/esri-well-known.yml
- group: build
  href: https://artifacts.apis.io/esri/packages/esri-packages.yml
  title: ''
  type: Packages
  url: packages/esri-packages.yml
- group: build
  href: https://artifacts.apis.io/esri/packages/esri-packages.yml
  title: ''
  type: SDKs
  url: packages/esri-packages.yml
- group: design
  href: https://artifacts.apis.io/esri/components/esri-components.yml
  title: ''
  type: Components
  url: components/esri-components.yml
- group: design
  href: https://artifacts.apis.io/esri/conventions/esri-conventions.yml
  title: ''
  type: Conventions
  url: conventions/esri-conventions.yml
- group: design
  href: https://artifacts.apis.io/esri/errors/esri-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/esri-problem-types.yml
- group: design
  href: https://artifacts.apis.io/esri/lifecycle/esri-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/esri-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.location.arcgis.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://location.arcgis.com/help/release-notes/2026-07/
- group: operate
  href: https://artifacts.apis.io/esri/changelog/esri-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/esri-changelog.yml
- group: design
  href: https://artifacts.apis.io/esri/conformance/esri-conformance.yml
  title: ''
  type: Conformance
  url: conformance/esri-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.arcgis.com/en/compliance/compliance.htm
- group: auth
  href: https://artifacts.apis.io/esri/security/esri-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esri-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/esri/security/esri-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/esri-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.arcgis.com/en/security-concern/
- group: design
  href: https://artifacts.apis.io/esri/asyncapi/esri-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/esri-webhooks.yml
- group: design
  href: https://artifacts.apis.io/esri/data-model/esri-data-model.yml
  title: ''
  type: DataModel
  url: data-model/esri-data-model.yml
- group: agent
  href: https://artifacts.apis.io/esri/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/esri/rate-limits/esri-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/esri-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/esri/plans/esri-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/esri-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/esri/finops/esri-finops.yml
  title: ''
  type: FinOps
  url: finops/esri-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.arcgis.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.arcgis.com/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.arcgis.com/documentation/mapping-and-location-services/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.esri.com/en-us/products/arcgis-location-platform
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.esri.com/t5/developers/ct-p/developers
- group: company
  title: ''
  type: Blog
  url: https://community.esri.com/t5/developers-blog/bg-p/developers-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Esri
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/esridevs/workspace/esri-arcgis-services
- group: commercial
  title: ''
  type: Pricing
  url: https://location.arcgis.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://location.arcgis.com/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.esri.com/en-us/legal/terms/full-master-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esri.com/en-us/privacy/overview
created: '2025-01-14'
description: 'Esri is a global leader in geographic information system (GIS) technology, offering innovative solutions for mapping and spatial analysis. The company provides software, data, and services to help organizations make better decisions based on location intelligence. Esri''s technology is used across a wide range of industries, including government, natural resources, utilities, and public safety. NOTE: This repository is an alias for the canonical Esri ArcGIS profile maintained at api-evangelist/esri-arcgis, which contains the full set of API definitions, OpenAPI artifacts, and developer resources.'
finops:
- has_sources: true
  method: derived
  name: Esri Finops
  primary_unit: 1,000 places
  service_category: ''
  slug: esri-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/esri.png
json_schemas:
- name: Candidate
  property_count: 5
  slug: esri-candidate
- name: GeocodeResponse
  property_count: 2
  slug: esri-geocode-response
- name: ItemCollection
  property_count: 5
  slug: esri-item-collection
- name: Item
  property_count: 16
  slug: esri-item
- name: Place
  property_count: 7
  slug: esri-place
- name: PlacesResponse
  property_count: 2
  slug: esri-places-response
- name: Portal
  property_count: 9
  slug: esri-portal
- name: ReverseGeocodeResponse
  property_count: 2
  slug: esri-reverse-geocode-response
- name: SearchResults
  property_count: 6
  slug: esri-search-results
- name: User
  property_count: 11
  slug: esri-user
jsonld:
- class_count: 17
  name: Esri Context
  property_count: 53
  slug: esri-context
layout: provider
mcp_servers:
- description: An Esri-hosted Model Context Protocol server that exposes ArcGIS Location Services — geocoding, routing, elevation, static maps and GeoEnrichment — to MCP-compliant clients and AI agents without calli
  name: MCP for ArcGIS Location Services (beta)
  slug: arcgis-location-services
modified: '2026-09-07'
name: Esri
nav: Providers
network: true
overview: 'Esri publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Geocoding API, Routing API, and 8 more. Tagged areas include Geographic, Geospatial, GIS, Location, and Mapping.


  The Esri catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Esri''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 49 more developer resources.'
plans:
- name: Esri Plans Pricing
  plan_count: 35
  slug: esri-plans-pricing
- name: Esri Price Estimates
  plan_count: 0
  slug: esri-price-estimates
random_paper: 3
rate_limits:
- limit_count: 6
  name: Esri Rate Limits
  slug: esri-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Esri API Rules
  rule_count: 62
  severity_counts:
    error: 55
    hint: 0
    info: 5
    warn: 2
  slug: esri-rules
scopes:
- name: Esri Scopes
  scope_count: 2
  slug: esri-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 77.8
  coverage:
    artifact_dirs: 39
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.6
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 69.8
    developer_ergonomics: 68.5
    discoverability: 76.7
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/esri/esri-2026-06-20T180822.png
security:
- kind: authentication
  name: Esri Authentication
  slug: esri-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Esri Domain Security
  slug: esri-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Esri Vulnerability Disclosure
  slug: esri-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Esri Trust Center
  slug: esri-trust-center
  summary_line: FedRAMP Moderate, ISO/IEC 27001:2022, SOC 2, GDPR, EU-U.S. Data Privacy Framework, CCPA / CPRA
skill_count: 3
skills:
- name: Call the Esri ArcGIS Location Services MCP server
  slug: esri-call-the-mcp-server
- name: Geocode an address with ArcGIS
  slug: esri-geocode-an-address
- name: Solve a route with ArcGIS
  slug: esri-solve-a-route
slug: esri
tags:
- Geographic
- Geospatial
- GIS
- Location
- Mapping
- Maps
- Spatial Analysis
- Geocoding
- Routing
website: https://www.esri.com/
---
