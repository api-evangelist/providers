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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Esri Arcgis Agentic Access
  operation_count: 9
  slug: esri-arcgis-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The ArcGIS Maps SDK for JavaScript enables web developers to build compelling 2D and 3D mapping applications with interactive visualizations, spatial analysis tools, geocoding, routing, and portal con
  name: ArcGIS Maps SDK for JavaScript
  slug: esri-arcgis-maps-sdk-javascript
- description: 'The ArcGIS API for Python provides a Pythonic interface for GIS capabilities including data management, spatial analysis, geocoding, routing, and administration of ArcGIS Online and ArcGIS Enterprise '
  name: ArcGIS API for Python
  slug: esri-arcgis-api-for-python
- description: The ArcGIS Geocoding Service provides address search, reverse geocoding, address suggestions, and batch geocoding capabilities using the World Geocoding Service.
  name: ArcGIS Geocoding Service
  slug: esri-arcgis-geocoding-service
- description: The ArcGIS Routing Service provides route optimization, turn-by-turn directions, nearest facility finding, service area definition, and fleet management capabilities.
  name: ArcGIS Routing Service
  slug: esri-arcgis-routing-service
- description: The ArcGIS Places Service provides search and retrieval of global points of interest spanning over 1,000 feature categories for location-aware applications.
  name: ArcGIS Places Service
  slug: esri-arcgis-places-service
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: Address search, reverse geocoding, and batch geocoding
  name: ESRI ArcGIS Geocoding API
  slug: esri-arcgis-geocoding-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: Points of interest search and retrieval
  name: ESRI ArcGIS Places API
  slug: esri-arcgis-places-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: Portal items, users, groups, and organizational management
  name: ESRI ArcGIS Portal API
  slug: esri-arcgis-portal-api
- description: A GraphQL API for ArcGIS Urban - urban models, plans, projects, branches, parcels, zones, spaces, building types, indicators, metrics, overlays, viewpoints and scenario analyses (elevation profile, li
  name: ArcGIS Urban API
  slug: esri-arcgis-urban-api
- description: Esri-hosted Model Context Protocol server exposing ArcGIS Location Services - geocoding, reverse geocoding, routing, elevation, static maps and GeoEnrichment - as seven MCP tools. Remote HTTP transpor
  name: MCP for ArcGIS Location Services (beta)
  slug: esri-arcgis-mcp-location-services
- description: ArcGIS Server publishes any map or feature service through the OGC interfaces - WMS, WFS, WCS, WMTS and KML. The two capabilities documents registered here were fetched from Esri's public ArcGIS Serve
  name: ArcGIS Server OGC Web Services
  slug: esri-arcgis-ogc-services
artifact_total: 47
asyncapis:
- description: ''
  name: Esri Arcgis Webhooks
  slug: esri-arcgis-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ESRI ArcGIS Platform Geocoding API
  slug: open-esri-arcgis-geocoding-api
- collection_type: open
  name: ESRI ArcGIS Platform Geocoding Places API
  slug: open-esri-arcgis-places-api
- collection_type: open
  name: ESRI ArcGIS Platform API
  slug: open-esri-arcgis-platform
- collection_type: open
  name: ESRI ArcGIS Platform Geocoding Portal API
  slug: open-esri-arcgis-portal-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/esri-arcgis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esri-arcgis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/esri-arcgis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/esri-arcgis-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/esri-arcgis-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/esri-arcgis-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/esri-arcgis-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/esri-arcgis-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/esri-arcgis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/esri-arcgis-packages.yml
- group: design
  title: ''
  type: Components
  url: components/esri-arcgis-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/esri-arcgis-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/esri-arcgis-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/esri-arcgis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/esri-arcgis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/esri-arcgis-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/esri-arcgis-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/esri-arcgis-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/esri-arcgis-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/esri-arcgis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/esri-arcgis-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/esri-arcgis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/esri-arcgis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/esri-arcgis-trust-center.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/esri-arcgis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/esri-arcgis-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/esri-arcgis-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/esri-arcgis-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/esri-arcgis-jsonschema-spectral-rules.yml
- group: company
  title: ''
  type: Website
  url: https://www.esri.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esri-arcgis
created: '2026-04-28'
description: ESRI ArcGIS is the world's leading geospatial platform providing mapping, spatial analysis, and location intelligence APIs and SDKs. The developer platform includes REST APIs, multiple language SDKs, and cloud services for GIS professionals and developers building location-enabled applications.
finops:
- name: Esri Arcgis Finops
  service_category: GIS / Location Services
  slug: esri-arcgis-finops
image: https://www.esri.com/content/dam/esrisites/en-us/media/social-media/social-sharing-image-default.jpg
json_schemas:
- name: Category
  property_count: 2
  slug: esri-arcgis-category
- name: Error
  property_count: 1
  slug: esri-arcgis-error
- name: ArcGIS Feature
  property_count: 2
  slug: esri-arcgis-feature
- name: GeocodeCandidate
  property_count: 4
  slug: esri-arcgis-geocodecandidate
- name: GeocodeResponse
  property_count: 2
  slug: esri-arcgis-geocoderesponse
- name: GroupRef
  property_count: 3
  slug: esri-arcgis-groupref
- name: Item
  property_count: 16
  slug: esri-arcgis-item
- name: ItemCollection
  property_count: 5
  slug: esri-arcgis-itemcollection
- name: Place
  property_count: 7
  slug: esri-arcgis-place
- name: PlacesResponse
  property_count: 2
  slug: esri-arcgis-placesresponse
- name: PlaceSummary
  property_count: 5
  slug: esri-arcgis-placesummary
- name: Point
  property_count: 3
  slug: esri-arcgis-point
- name: Portal
  property_count: 9
  slug: esri-arcgis-portal
- name: ReverseGeocodeResponse
  property_count: 2
  slug: esri-arcgis-reversegeocoderesponse
- name: SearchResults
  property_count: 6
  slug: esri-arcgis-searchresults
- name: SpatialReference
  property_count: 2
  slug: esri-arcgis-spatialreference
- name: User
  property_count: 11
  slug: esri-arcgis-user
json_structures:
- name: Esri Arcgis Structure
  property_count: 0
  slug: esri-arcgis-structure
jsonld:
- class_count: 33
  name: Esri Arcgis Context
  property_count: 10
  slug: esri-arcgis-context
layout: provider
mcp_servers:
- description: An Esri-hosted, remote Model Context Protocol server that exposes ArcGIS Location Services (geocoding, reverse geocoding, routing, elevation, static maps and GeoEnrichment) to MCP-compliant clients as
  name: MCP for ArcGIS Location Services (beta)
  slug: mcp-for-arcgis-location-services-beta
modified: '2026-09-07'
name: ESRI ArcGIS
nav: Providers
network: true
overview: 'ESRI ArcGIS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Geocoding API, Places API, and Portal API. Tagged areas include GIS, Geospatial, Mapping, Location, and Spatial Analysis.


  The ESRI ArcGIS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ESRI ArcGIS''s developer surface includes authentication, changelog, and 30 more developer resources.'
plans:
- name: Esri Arcgis Plans Pricing
  plan_count: 9
  slug: esri-arcgis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 10
  name: Esri Arcgis Rate Limits
  slug: esri-arcgis-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ESRI ArcGIS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: esri-arcgis-jsonschema-spectral-rules
scopes:
- name: Esri Arcgis Scopes
  scope_count: 2
  slug: esri-arcgis-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 83.3
    catalog_earned_first_party: 24.0
    catalog_gap: 31.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 43.2
    contract_quality: 74.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 89.5
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/esri-arcgis/refs/heads/main/screenshots/esri-arcgis-2026-06-20T180823.png
security:
- kind: authentication
  name: Esri Arcgis Authentication
  slug: esri-arcgis-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Esri Arcgis Domain Security
  slug: esri-arcgis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Esri Arcgis Vulnerability Disclosure
  slug: esri-arcgis-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Esri Arcgis Trust Center
  slug: esri-arcgis-trust-center
  summary_line: FedRAMP Moderate, ISO/IEC 27001:2022, SOC 2
slug: esri-arcgis
tags:
- GIS
- Geospatial
- Mapping
- Location
- Spatial Analysis
- Geocoding
- Routing
- Places
- OGC
- GraphQL
- MCP
website: https://www.esri.com/
---
