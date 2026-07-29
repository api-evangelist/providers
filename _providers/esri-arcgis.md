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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Esri Arcgis Agentic Access
  operation_count: 9
  slug: esri-arcgis-agentic-access
  summary_line: 9 operations
api_count: 8
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
- description: Address search, reverse geocoding, and batch geocoding
  name: ESRI ArcGIS Geocoding API
  slug: esri-arcgis-geocoding-api
- description: Points of interest search and retrieval
  name: ESRI ArcGIS Places API
  slug: esri-arcgis-places-api
- description: Portal items, users, groups, and organizational management
  name: ESRI ArcGIS Portal API
  slug: esri-arcgis-portal-api
artifact_total: 36
collections:
- collection_type: open
  name: ESRI ArcGIS Platform API
  slug: open-esri-arcgis-platform
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
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esri-arcgis
description: ESRI ArcGIS is the world's leading geospatial platform providing mapping, spatial analysis, and location intelligence APIs and SDKs. The developer platform includes REST APIs, multiple language SDKs, and cloud services for GIS professionals and developers building location-enabled applications.
finops:
- name: Esri Arcgis Finops
  service_category: GIS / Location Services
  slug: esri-arcgis-finops
image: https://raw.githubusercontent.com/api-evangelist/esri-arcgis/refs/heads/main/image.png
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
modified: '2026-04-28'
name: ESRI ArcGIS
nav: Providers
network: true
overview: 'ESRI ArcGIS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Geocoding API, Places API, and Portal API. Tagged areas include GIS, Geospatial, Mapping, Location, and Spatial Analysis.


  The ESRI ArcGIS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ESRI ArcGIS''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Esri Arcgis Plans Pricing
  plan_count: 9
  slug: esri-arcgis-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 7
  name: Esri Arcgis Rate Limits
  slug: esri-arcgis-rate-limits
rules:
- name: ESRI ArcGIS API Rules
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
  band: developing
  composite: 45.6
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
slug: esri-arcgis
tags:
- GIS
- Geospatial
- Mapping
- Location
- Spatial Analysis
---
