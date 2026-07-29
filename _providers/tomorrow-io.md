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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Tomorrow Io Agentic Access
  operation_count: 32
  slug: tomorrow-io-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 10
apis:
- description: Retrieve historical weather observations and monthly climate normals for any point or polygon on Earth using the same field catalog as the realtime and forecast APIs.
  name: Tomorrow.io Historical Weather API
  slug: tomorrow-io-historical-api
- description: Retrieve severe weather events, fires, floods, lightning swarms, and custom vector events affecting a point or geometry.
  name: Tomorrow.io Events API
  slug: tomorrow-io-events-api
- description: Retrieve weather along an arbitrary polyline of waypoints at the times each segment is expected to be traversed — powers route optimization, logistics planning, and ETA-aware hazard detection.
  name: Tomorrow.io Weather on Routes API
  slug: tomorrow-io-route-api
- description: Manage saved locations (points, polygons, lines) referenced by ``locationId`` across the Tomorrow.io APIs, with tag-based cohorts for fleet, customer, or asset organization.
  name: Tomorrow.io Locations API
  slug: tomorrow-io-locations-api
- description: Create and manage threshold-based weather alerts that evaluate Tomorrow.io data layers against custom rules for linked locations and deliver notifications via webhook, email, and the Tomorrow.io app.
  name: Tomorrow.io Alerts API
  slug: tomorrow-io-alerts-api
- description: Define and manage reusable Insights — named rules combining Tomorrow.io data layers, operators, and thresholds — that power the Events and Alerts APIs.
  name: Tomorrow.io Insights API
  slug: tomorrow-io-insights-api
- description: 1h / 1d step weather forecast for the next 14 days.
  name: Tomorrow.io Forecast API
  slug: tomorrow-io-forecast-api
- description: Web Mercator tile service for weather layers.
  name: Tomorrow.io Maps API
  slug: tomorrow-io-maps-api
- description: Current weather conditions for a point or location.
  name: Tomorrow.io Realtime API
  slug: tomorrow-io-realtime-api
- description: Flexible timeline retrieval across any combination of fields and timesteps.
  name: Tomorrow.io Timelines API
  slug: tomorrow-io-timelines-api
arazzos:
- description: Inspect an existing alert, retune its threshold, and confirm the updated definition.
  name: Tomorrow.io Alert Threshold Tuning
  slug: tomorrow-io-alert-threshold-tuning-workflow
- description: Confirm a location exists, unlink it from an alert, then delete the saved location.
  name: Tomorrow.io Decommission a Monitored Location
  slug: tomorrow-io-decommission-location-workflow
- description: Save a location, pull its historical weather timeline, and compare against climate normals.
  name: Tomorrow.io Historical and Climate Normals Analysis
  slug: tomorrow-io-historical-and-normals-analysis-workflow
- description: Define a reusable insight, build an alert from it, bind locations, and activate monitoring.
  name: Tomorrow.io Insight-Driven Alert Setup
  slug: tomorrow-io-insight-driven-alert-setup-workflow
- description: Define an insight, then run an advanced event query filtered to that insight over an area.
  name: Tomorrow.io Insight-Scoped Event Query
  slug: tomorrow-io-insight-scoped-event-query-workflow
- description: Save a location, scan it for severe weather events, and branch on whether any are active.
  name: Tomorrow.io Location Severe Weather Events
  slug: tomorrow-io-location-severe-weather-events-workflow
- description: Read realtime precipitation for a point, then fetch the matching weather map tile.
  name: Tomorrow.io Map Tile Precipitation Overlay
  slug: tomorrow-io-map-tile-precipitation-overlay-workflow
- description: Take a realtime reading, then pull a multi-field timeline window over the same location.
  name: Tomorrow.io Realtime Snapshot then Timelines Deep Dive
  slug: tomorrow-io-realtime-then-timelines-deep-dive-workflow
- description: Compare current conditions for a location against its long-term monthly climate normals.
  name: Tomorrow.io Realtime vs Climate Normals Benchmark
  slug: tomorrow-io-realtime-vs-climate-normals-workflow
- description: Retrieve weather along a planned route, then scan the destination for severe events.
  name: Tomorrow.io Route Weather Hazard Scan
  slug: tomorrow-io-route-weather-hazard-scan-workflow
- description: Create a reusable saved location, then pull realtime conditions and a multi-day forecast for it.
  name: Tomorrow.io Saved Location Realtime and Forecast
  slug: tomorrow-io-saved-location-realtime-forecast-workflow
- description: Create a location, tag it into a cohort, confirm the tag, and read its current conditions.
  name: Tomorrow.io Tag and Monitor a Location Cohort
  slug: tomorrow-io-tag-location-cohort-workflow
artifact_total: 95
collections:
- collection_type: postman
  name: Tomorrow.io Alerts API
  slug: postman-tomorrow-io-alerts-api
- collection_type: postman
  name: Tomorrow.io Events API
  slug: postman-tomorrow-io-events-api
- collection_type: postman
  name: Tomorrow.io Historical Weather API
  slug: postman-tomorrow-io-historical-api
- collection_type: postman
  name: Tomorrow.io Insights API
  slug: postman-tomorrow-io-insights-api
- collection_type: postman
  name: Tomorrow.io Locations API
  slug: postman-tomorrow-io-locations-api
- collection_type: postman
  name: Tomorrow.io Weather Maps API
  slug: postman-tomorrow-io-map-tiles-api
- collection_type: postman
  name: Tomorrow.io Weather on Routes API
  slug: postman-tomorrow-io-route-api
- collection_type: postman
  name: Tomorrow.io Weather API
  slug: postman-tomorrow-io-weather-api
- collection_type: open
  name: Tomorrow.io Alerts API
  slug: open-tomorrow-io-alerts-api
- collection_type: open
  name: Tomorrow.io Events API
  slug: open-tomorrow-io-events-api
- collection_type: open
  name: Tomorrow.io Historical Weather API
  slug: open-tomorrow-io-historical-api
- collection_type: open
  name: Tomorrow.io Insights API
  slug: open-tomorrow-io-insights-api
- collection_type: open
  name: Tomorrow.io Locations API
  slug: open-tomorrow-io-locations-api
- collection_type: open
  name: Tomorrow.io Weather Maps API
  slug: open-tomorrow-io-map-tiles-api
- collection_type: open
  name: Tomorrow.io Weather on Routes API
  slug: open-tomorrow-io-route-api
- collection_type: open
  name: Tomorrow.io Weather API
  slug: open-tomorrow-io-weather-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tomorrow-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tomorrow-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tomorrow-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tomorrowio/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-alert-threshold-tuning-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-decommission-location-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-historical-and-normals-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-insight-driven-alert-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-insight-scoped-event-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-location-severe-weather-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-map-tile-precipitation-overlay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-realtime-then-timelines-deep-dive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-realtime-vs-climate-normals-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-route-weather-hazard-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-saved-location-realtime-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tomorrow-io-tag-location-cohort-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.tomorrow.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tomorrow.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tomorrow.io/reference/welcome
- group: auth
  title: ''
  type: Authentication
  url: https://app.tomorrow.io/development/keys
- group: start
  title: ''
  type: Signup
  url: https://app.tomorrow.io/signup
- group: start
  title: ''
  type: Console
  url: https://app.tomorrow.io/signin
- group: start
  title: ''
  type: Sandbox
  url: https://docs.tomorrow.io/recipes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tomorrow.io/reference/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.tomorrow.io/reference/rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.tomorrow.io/reference/error-handling
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tomorrow.io/reference/release-notes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tomorrow.io/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tomorrow.io/reference/tomorrow-io-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tomorrow.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tomorrow.io/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tomorrow.io/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.tomorrow.io
- group: company
  title: ''
  type: Blog
  url: https://www.tomorrow.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tomorrow-IO-API
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-postman
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-samples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-route-mapbox
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-timelines-widget
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-events-charts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-api-proxy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-netlify
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-map-spectrums
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/tomorrow-weather-codes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tomorrow-IO-API/climate-normals
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tomorrow-io
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tomorrow_io
- group: design
  title: ''
  type: SpectralRules
  url: rules/tomorrow-io-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tomorrow-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tomorrow-io-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/tomorrow-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tomorrow-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tomorrow-io-finops.yml
created: '2026-05-24'
description: Tomorrow.io is a Boston-based weather intelligence platform combining a global proprietary numerical weather model, a constellation of microsatellite weather radars, and a developer-facing v4 REST API. The platform exposes 60+ hyperlocal data layers — core weather, air quality, pollen, solar, soil, fire, flood, lightning, maritime, aviation, road — together with map tiles, severe-weather event detection, routable forecast queries, climate normals, historical archive access, customer-defined locations, named insights, and threshold-based webhook alerts. Used by airlines, on-demand logistics platforms, agriculture, energy, and the US Air Force, Tomorrow.io's API is designed for ETA-aware route planning, geofenced alerting, agentic workflows, and large-scale operational decisioning under weather risk.
examples:
- key_count: 2
  name: Tomorrow Io Alert Example
  slug: tomorrow-io-alert-example
- key_count: 2
  name: Tomorrow Io Events Example
  slug: tomorrow-io-events-example
- key_count: 2
  name: Tomorrow Io Realtime Example
  slug: tomorrow-io-realtime-example
- key_count: 2
  name: Tomorrow Io Route Example
  slug: tomorrow-io-route-example
- key_count: 2
  name: Tomorrow Io Timelines Example
  slug: tomorrow-io-timelines-example
features:
- description: Core weather, air quality, pollen, solar, soil, fire, flood, lightning, maritime, aviation, and road layers retrievable at point, polygon, or polyline geometry.
  name: 60+ Hyperlocal Data Layers
- description: Tomorrow.io operates its own constellation of space-based weather radars to fill gaps in terrestrial radar coverage, especially over oceans and the developing world.
  name: Proprietary Microsatellite Weather Radar Constellation
- description: 60-minute minute-by-minute precipitation forecast in addition to hourly and daily timelines (Enterprise tier).
  name: Minutely Forecast Resolution
- description: Daily forecast out to 14 days on Enterprise plans, 5 days on Free.
  name: 14-Day Forecast Horizon
- description: Monthly long-term averages for benchmarking current conditions against typical patterns.
  name: Climate Normals
- description: First-class API for severe weather phenomena plus customer-defined vector events for proprietary hazard models.
  name: Severe Weather and Custom Events
- description: Define rule-based alerts that fire webhooks and emails when conditions cross thresholds for linked locations.
  name: Threshold Alerts with Webhooks
- description: Web Mercator PNG tiles for visualizing every data layer in Mapbox, MapLibre, Leaflet, OpenLayers, Google Maps.
  name: Weather Map Tiles
- description: ETA-aware weather retrieval along a polyline of waypoints for logistics, aviation, and maritime planning.
  name: Weather on Routes
- description: Official Tomorrow.io Model Context Protocol server for agentic AI access to the Weather API.
  name: MCP Server
- description: Enterprise SLA with rate-limit response headers exposed for programmatic monitoring.
  name: 99.9% Uptime SLA
- description: Tomorrow.io publishes an LLMs.txt index of every documentation page and endpoint for AI agents.
  name: LLMs.txt Indexed Documentation
finops:
- name: Tomorrow Io Finops
  service_category: Weather Intelligence
  slug: tomorrow-io-finops
image: https://www.tomorrow.io/favicon-32x32.png
integrations:
- description: Drop Tomorrow.io map tiles directly into Mapbox GL JS basemaps; official tomorrow-route-mapbox sample.
  name: Mapbox
- description: Open-source slippy-map client compatible with the Tomorrow.io Maps API.
  name: MapLibre
- description: Compatible with the Tomorrow.io Maps XYZ tile service.
  name: Leaflet
- description: Official tomorrow-api-proxy sample demonstrates key-safe proxy deployment on GCP.
  name: Google Cloud Functions
- description: Official tomorrow-netlify sample for serverless edge proxying.
  name: Netlify Edge
- description: Official Tomorrow.io Postman collection covering every v4 endpoint.
  name: Postman
- description: Official Tomorrow.io MCP server for plugging Weather, Forecast, Timelines, and Events into AI agents.
  name: Model Context Protocol (MCP)
- description: First-class webhook delivery for alert notifications.
  name: Webhooks
- description: tomorrow-events-charts open-source dashboard demonstrating the Events API.
  name: Insights Dashboard
json_schemas:
- name: Tomorrow.io Alert
  property_count: 7
  slug: tomorrow-io-alert
- name: Tomorrow.io Event
  property_count: 9
  slug: tomorrow-io-event
- name: Tomorrow.io Insight
  property_count: 5
  slug: tomorrow-io-insight
- name: Tomorrow.io Location
  property_count: 6
  slug: tomorrow-io-location
- name: Tomorrow.io Weather Values
  property_count: 20
  slug: tomorrow-io-weather-values
json_structures:
- name: Tomorrow Io Weather Values Structure
  property_count: 0
  slug: tomorrow-io-weather-values-structure
jsonld:
- class_count: 4
  name: Tomorrow Io Context
  property_count: 16
  slug: tomorrow-io-context
layout: provider
modified: '2026-05-24'
name: Tomorrow.io
nav: Providers
network: true
overview: 'Tomorrow.io publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Historical Weather API, Events API, Weather on Routes API, and 7 more. Tagged areas include Weather, Forecast, Climate, Risk, and Air Quality.


  The Tomorrow.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tomorrow.io''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, developer console, sandbox, and 46 more developer resources.'
plans:
- name: Tomorrow Io Plans Pricing
  plan_count: 4
  slug: tomorrow-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Tomorrow Io Rate Limits
  slug: tomorrow-io-rate-limits
rules:
- name: Tomorrow.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tomorrow-io-jsonschema-spectral-rules
- name: Tomorrow.io API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: tomorrow-io-rules
score:
  band: exemplar
  composite: 70.2
  delta: -4.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 71.2
    developer_ergonomics: 78.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 74.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tomorrow-io/refs/heads/main/screenshots/tomorrow-io-2026-06-20T195444.png
security:
- kind: authentication
  name: Tomorrow Io Authentication
  slug: tomorrow-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tomorrow Io Domain Security
  slug: tomorrow-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tomorrow-io
solutions:
- description: Self-serve developer API with 60+ data layers, Postman collection, and MCP server.
  name: Weather API for Developers
- description: Operational dashboards, alerts, and decision automation built on top of the Tomorrow.io Weather API.
  name: Tomorrow.io Resilience Platform
- description: Vertical solution for airline operations centers, dispatch, and aerodrome operations.
  name: Aviation Resilience
- description: Vertical solution for utility load forecasting, generation forecasting, and outage management.
  name: Energy Resilience
- description: Vertical solution for fleet, freight, and last-mile delivery routing under weather risk.
  name: Logistics Resilience
- description: Tomorrow.io serves the US Air Force and other defense and government customers with operational weather intelligence and proprietary space-based weather radar.
  name: Government and Defense
tags:
- Weather
- Forecast
- Climate
- Risk
- Air Quality
- Pollen
- Lightning
- Severe Weather
- Maps
- Routing
- Satellite
- Microsatellites
- Radar
- Geospatial
- Alerts
use_cases:
- description: ETA-aware weather along truck, drone, and last-mile routes to avoid storms, ice, and visibility hazards.
  name: Route Optimization and Logistics
- description: Airline operations centers and dispatch use Tomorrow.io for icing, turbulence, low-level wind shear, and aerodrome forecasts.
  name: Aviation Planning
- description: Wind and solar generation forecasting, load forecasting under heat events, and outage management.
  name: Energy Forecasting
- description: Soil moisture, evapotranspiration, frost, and growing-degree-day analytics for farm operations.
  name: Agriculture
- description: Geofenced alerting for tropical storms, severe thunderstorms, hail, lightning, and flash floods.
  name: Severe Weather Alerting
- description: Game-day, race-day, and venue operations under lightning, heat, and precipitation risk.
  name: Sports and Outdoor Events
- description: Historical and climate-normals data for parametric insurance pricing and physical climate risk modeling.
  name: Insurance and Climate Risk
- description: Bulk historical timelines for training operational decision models and backtesting weather-sensitive workflows.
  name: Data Science
- description: Wave height, swell direction, and sea-state forecasting for shipping, offshore energy, and fisheries.
  name: Maritime Operations
- description: Surge demand modeling and worker-safety alerting for rideshare, delivery, and on-demand services.
  name: On-Demand Platforms
website: https://www.tomorrow.io
---
