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
  name: Microsoft Azure Maps Agentic Access
  operation_count: 4
  slug: microsoft-azure-maps-agentic-access
  summary_line: 4 operations
api_count: 11
apis:
- description: Calculates routes between origin and destination, provides turn-by-turn directions, supports multiple travel modes, traffic-aware routing, route matrices, and route range (isochrone) calculations.
  name: Azure Maps Route API
  slug: azure-maps-route-api
- description: Returns map tiles, static images, and vector tiles in multiple styles including satellite, road, and hybrid. Supports raster and vector tile formats, custom imagery, and traffic overlays for embedding
  name: Azure Maps Render API
  slug: azure-maps-render-api
- description: Provides real-time and historical traffic data including traffic flow, incident reports, and traffic tile imagery. Useful for routing, fleet management, and applications requiring up-to-date road cond
  name: Azure Maps Traffic API
  slug: azure-maps-traffic-api
- description: Provides current weather conditions, hourly and daily forecasts, severe weather alerts, weather along a route, and historical weather. Powered by AccuWeather data and global coverage.
  name: Azure Maps Weather API
  slug: azure-maps-weather-api
- description: Returns time zone information for a given coordinate, IANA time zone ID, or Windows time zone ID. Includes current time, daylight saving offsets, and time zone metadata.
  name: Azure Maps Timezone API
  slug: azure-maps-timezone-api
- description: Returns the ISO country code for a supplied IP address, useful for content localization, regulatory compliance, and access control based on user geographic location.
  name: Azure Maps Geolocation API
  slug: azure-maps-geolocation-api
- description: Performs spatial computations such as distance, closest point, point in polygon, geofence evaluation, and great circle distance. Enables location analytics and spatial reasoning workloads.
  name: Azure Maps Spatial API
  slug: azure-maps-spatial-api
- description: Returns elevation data in meters above sea level for points, polylines, and bounding boxes. Useful for terrain analysis, topographic visualization, and elevation profile calculations along a route.
  name: Azure Maps Elevation API
  slug: azure-maps-elevation-api
- description: Indoor maps service for creating, managing, and rendering custom indoor maps. Supports drawing package conversion, dataset and tileset management, feature state, and wayfinding for indoor environments
  name: Azure Maps Creator API
  slug: azure-maps-creator-api
- description: The Geocoding API from Azure Maps — 2 operation(s) for geocoding.
  name: Azure Maps Geocoding API
  slug: microsoft-azure-maps-geocoding-api
- description: The Search API from Azure Maps — 2 operation(s) for search.
  name: Azure Maps Search API
  slug: microsoft-azure-maps-search-api
artifact_total: 19
collections:
- collection_type: open
  name: Azure Maps Search REST API
  slug: open-microsoft-azure-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-maps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-maps-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-maps/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-maps/quick-demo-map-app
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/azure-maps/azure-maps-authentication
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/azure-maps/about-azure-maps
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/azure-maps/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/tag/azure-maps/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/azure-maps/release-notes-map-control
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/azure-maps
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Maps provides geospatial APIs for maps, routing, geocoding, traffic, weather, and spatial analysis. The service offers a comprehensive suite of REST APIs to embed location intelligence into applications spanning mobile, web, and IoT scenarios across multiple transport modes.
finops:
- name: Microsoft Azure Maps Finops
  service_category: API
  slug: microsoft-azure-maps-finops
image: https://azure.microsoft.com/svghandler/azure-maps/
layout: provider
modified: '2026-05-19'
name: Azure Maps
nav: Providers
network: true
overview: 'Azure Maps publishes 2 APIs on the [APIs.io](https://apis.io/) network: Geocoding API and Search API. Tagged areas include Geocoding, Geospatial, Location, Maps, and Mobility.


  Azure Maps'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, support, engineering blog, and 14 more developer resources.'
plans:
- name: Microsoft Azure Maps Plans Pricing
  plan_count: 3
  slug: microsoft-azure-maps-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Microsoft Azure Maps Rate Limits
  slug: microsoft-azure-maps-rate-limits
scopes:
- name: Microsoft Azure Maps Scopes
  scope_count: 1
  slug: microsoft-azure-maps-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 58.1
  delta: -1.3
  facets:
    commercial_clarity: 84.2
    contract_quality: 55.1
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-maps/refs/heads/main/screenshots/microsoft-azure-maps-2026-06-20T185424.png
security:
- kind: authentication
  name: Microsoft Azure Maps Authentication
  slug: microsoft-azure-maps-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Azure Maps Domain Security
  slug: microsoft-azure-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-maps
tags:
- Geocoding
- Geospatial
- Location
- Maps
- Mobility
- Routing
- Traffic
- Weather
website: https://azure.microsoft.com/en-us/products/azure-maps
---
