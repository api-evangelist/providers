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
- acting_count: 6
  human_in_the_loop: 1
  name: Here Technologies Agentic Access
  operation_count: 14
  slug: here-technologies-agentic-access
  summary_line: 14 operations · 6 acting · 1 human-in-the-loop
api_count: 27
apis:
- description: Forward and reverse geocoding, address lookup, place discovery, browse, and details. Returns rich location data including addresses, places, categories, and geometry.
  name: HERE Geocoding and Search API
  slug: geocoding-search
- description: Type-ahead search returning place and address suggestions for partial queries, sharing the geocoding and search dataset.
  name: HERE Autosuggest API
  slug: autosuggest
- description: Calculates routes for car, truck, bicycle, pedestrian, scooter, taxi, and EV vehicles with traffic, restrictions, tolls, alternatives, and turn-by-turn instructions.
  name: HERE Routing API v8
  slug: routing
- description: Batch many-to-many travel time and distance matrices for fleet routing, logistics, and territory planning.
  name: HERE Matrix Routing API v8
  slug: matrix-routing
- description: Computes reachable areas (isolines) by time, distance, or consumption from one or more origins for site selection and service-area analysis.
  name: HERE Isoline Routing API v8
  slug: isoline-routing
- description: Vehicle routing problem (VRP) solver for fleets, with time windows, capacities, breaks, skills, multi-trip, and pickup-and-delivery constraints.
  name: HERE Tour Planning API
  slug: tour-planning
- description: Optimizes the order of intermediate stops for a single vehicle route to minimize travel time or distance.
  name: HERE Waypoint Sequence API
  slug: waypoint-sequence
- description: 'Real-time traffic flow and incident data: speeds, jam factors, and incident events for monitoring, routing, and analytics.'
  name: HERE Traffic API v7
  slug: traffic
- description: Multi-modal public transit routing, station and stop lookup, departure boards, and next-departure data for transit-enabled apps.
  name: HERE Public Transit API
  slug: public-transit
- description: Current conditions, forecasts, and severe weather alerts at a coordinate or destination, intended to enrich routing, ETAs, and travel planning.
  name: HERE Destination Weather API
  slug: destination-weather
- description: Raster, vector, satellite, and hybrid map tiles served via tile and style endpoints, including the HERE Vector Tile API for client-side rendering.
  name: HERE Map Tile API
  slug: map-tile
- description: Renders static map images for a given location, route, or geometry as PNG/JPEG, with markers and overlays.
  name: HERE Map Image API
  slug: map-image
- description: 'Asset tracking platform: ingests positions and telemetry from devices, manages devices and projects, and exposes geofencing, history, and events through REST.'
  name: HERE Tracking API
  slug: tracking
- description: High-precision indoor and outdoor positioning using Wi-Fi, cellular, and Bluetooth signals.
  name: HERE Positioning API
  slug: positioning
- description: On-street and off-street parking availability, pricing, restrictions, and locations.
  name: HERE Parking API
  slug: parking
- description: Catalog, layer, and partition APIs for hosting and accessing location-centric data products on the HERE Platform / Workspace.
  name: HERE Platform Data API
  slug: platform-data
- description: High-definition map product for automated driving with road geometry, lanes, signs, hazards, and dynamic updates, distributed via the HERE Platform.
  name: HERE HD Live Map
  slug: hd-live-map
- description: Browser SDK for embedding interactive maps, routing, search, and traffic visualizations in web applications.
  name: HERE Maps API for JavaScript
  slug: maps-api-javascript
- description: Native iOS SDK with maps, routing, search, navigation, and offline capabilities for mobile applications.
  name: HERE SDK for iOS
  slug: sdk-ios
- description: Native Android SDK with maps, routing, search, navigation, and offline capabilities for mobile applications.
  name: HERE SDK for Android
  slug: sdk-android
- description: Flutter SDK wrapping HERE Mobile SDK capabilities for cross-platform mobile applications.
  name: HERE SDK for Flutter
  slug: sdk-flutter
- description: Web-based mapping studio for designing custom map styles, uploading and visualizing geospatial data, and publishing interactive map experiences on top of the HERE Platform.
  name: HERE Studio
  slug: studio
- description: The Batch Jobs API from HERE Technologies — 6 operation(s) for batch jobs.
  name: HERE Technologies Batch Jobs API
  slug: here-technologies-batch-jobs-api
- description: The Geocode API from HERE Technologies — 1 operation(s) for geocode.
  name: HERE Technologies Geocode API
  slug: here-technologies-geocode-api
- description: The Health API from HERE Technologies — 1 operation(s) for health.
  name: HERE Technologies Health API
  slug: here-technologies-health-api
- description: The Notifications API from HERE Technologies — 1 operation(s) for notifications.
  name: HERE Technologies Notifications API
  slug: here-technologies-notifications-api
- description: The Reverse Geocode API from HERE Technologies — 1 operation(s) for reverse geocode.
  name: HERE Technologies Reverse Geocode API
  slug: here-technologies-reverse-geocode-api
artifact_total: 34
collections:
- collection_type: open
  name: HERE Geocoding & Search API v7
  slug: open-here-technologies
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/here-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/here-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/here-technologies-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/here
- group: company
  title: ''
  type: Website
  url: https://www.here.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.here.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/heremaps
- group: commercial
  title: ''
  type: Plans
  url: plans/here-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/here-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/here-technologies-finops.yml
created: '2026-05-23'
description: HERE Technologies is a location data and technology company offering a broad REST API surface for mapping, geocoding, search, routing, fleet planning, traffic, weather, transit, geofencing, tracking, and HD live mapping for automated driving, plus client SDKs (Maps API for JavaScript, native SDKs for iOS and Android, Flutter), HERE Studio and Workspace for data hosting, and HERE Platform for enterprise data ingestion and processing. Most Location Services APIs are served under the *.hereapi.com domain and authenticated by API key, OAuth token, or app id / app code.
finops:
- name: Here Technologies Finops
  service_category: API
  slug: here-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/here-technologies.png
layout: provider
modified: '2026-05-23'
name: HERE Technologies
nav: Providers
network: true
overview: 'HERE Technologies publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch Jobs API, Geocode API, Health API, and 2 more. Tagged areas include Maps, Geocoding, Routing, Location Services, and Traffic.


  HERE Technologies'' developer surface includes authentication, documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Here Technologies Plans Pricing
  plan_count: 1
  slug: here-technologies-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 2
  name: Here Technologies Rate Limits
  slug: here-technologies-rate-limits
score:
  band: thin
  composite: 33.0
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/here-technologies/refs/heads/main/screenshots/here-technologies-2026-06-20T182642.png
security:
- kind: authentication
  name: Here Technologies Authentication
  slug: here-technologies-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Here Technologies Domain Security
  slug: here-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: here-technologies
tags:
- Maps
- Geocoding
- Routing
- Location Services
- Traffic
- HD Live Map
- Automotive
- Fleet
website: https://www.here.com/
---
