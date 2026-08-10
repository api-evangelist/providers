---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Dtn Agentic Access
  operation_count: 250
  slug: dtn-agentic-access
  summary_line: 250 operations · 17 acting
api_count: 38
apis:
- description: DTN Weather Conditions API delivers worldwide forecast, current condition, and historical weather data. The API leverages cloud technology and global forecast models to provide validated, continuously
  name: DTN Weather Conditions API
  slug: dtn-weather-conditions-api
- description: DTN Point Observation API delivers high-quality weather observation data from weather stations and locations worldwide. Supports near real-time and up to 30 years of historical weather observations. A
  name: DTN Point Observation API
  slug: dtn-point-observation-api
- description: DTN Point Forecast API delivers high-quality weather forecasts for specified locations. Provides hourly and daily forecast data for agriculture, aviation, shipping, and utilities use cases. Uses the s
  name: DTN Point Forecast API
  slug: dtn-point-forecast-api
- description: DTN Radar Precipitation Forecast API provides short-term precipitation forecasts derived from radar data. Supports agricultural, utility, and renewable energy operational planning. Uses OAuth2 authent
  name: DTN Radar Precipitation Forecast API
  slug: dtn-radar-precipitation-forecast-api
- description: DTN provides real-time and historical commodity price data, grain and livestock prices, planting condition indices, and market analysis APIs for precision agriculture and commodity trading workflows.
  name: DTN Commodity & Market Data API
  slug: dtn-commodity-data-api
- description: The DTN Agency Bulletin WebSocket API (ABA WebSocket) delivers real-time weather bulletins over a persistent connection for instant updates.
  name: DTN ABA WebSocket
  slug: agency-bulletin-websocket-api
- description: The DTN Agency Bulletin API (ABA) provides access to the latest weather bulletins published by the national meteorological agencies of different countries in a unified format.
  name: DTN Agency Bulletin API
  slug: dtn-agency-bulletin-api
- description: Access the latest global weather bulletins. CAP delivery of the DTN alerts and national agencies bulletins.
  name: DTN Alerting API
  slug: dtn-alerting-api
- description: DTN Astronomical API is an all-in-one solution to get astronomical data. Currently it returns sun and moon data.
  name: DTN Astronomical API
  slug: dtn-astronomical-api
- description: This service empowers consumers with accurate, global, location-specific climatological data to help inform decisions, optimize operations, and develop strategies based on historical environmental con
  name: DTN Climatology API
  slug: dtn-climatology-api
- description: Internal dev-portal API
  name: DTN Developer Portal API
  slug: dtn-developer-portal-api
- description: API for utility companies to access EEI forecasts that translate weather data into actionable risk levels. Features multi-parameter monitoring, seasonal threshold switching, and customer-specific conf
  name: DTN Energy Event Index API
  slug: dtn-energy-event-index-api
- description: Provides data for EDR turbulence (including Nowcast), icing & HIWC, thunderstorms, ozone, jet stream axis, space weather, and QVA.
  name: DTN Enhanced Flight Hazards API
  slug: dtn-enhanced-flight-hazards-api
- description: The DTN Lightning API provides you access to worldwide near real-time and historical lightning data.
  name: DTN Lightning API
  slug: dtn-lightning-api
- description: The Lightning WebSocket delivers real-time lightning data over a persistent connection for instant updates.
  name: DTN Lightning WebSocket
  slug: dtn-lightning-websocket
- description: METARs are a key piece of information required for flight planning and flight operations. DTN METAR API allows customers to get the data critical to them without extra data not needed.
  name: DTN METARs API
  slug: dtn-metars-api
- description: DTN API for various mapping services.. A wide range of vector and raster map layers.
  name: DTN Map Tile API
  slug: dtn-map-tile-api
- description: The DTN Marine Weather API (MWA) is an all-in-one solution to integrate the DTN high-resolution marine weather data into your systems and decision making processes. Utilizing the latest cloud technolo
  name: DTN Marine Weather API
  slug: dtn-marine-weather-api
- description: The DTN NOTAM API is an all-encompassing solution to retrieve the most current NOTAM from multiple available feeds to avoid duplicate NOTAMS. Many sources publish NOTAMs and push them to others such a
  name: DTN NOTAMs API
  slug: dtn-notams-api
- description: PIREPS are a key piece of information required for flight planning and flight operations. DTN PIREP API allows customers to get the data critical to them without extra data not needed.
  name: DTN PIREPs API
  slug: dtn-pireps-api
- description: DTN is developing the platform to supply road data on OSM segments across North America and Europe, allowing users to request data for a geographic area or specific roadway within the database.
  name: DTN Pavement Conditions API
  slug: pavement-conditions-api
- description: 'This API caters to a wide range of users, including: Risk managers assessing weather-related operational risks Agricultural planners making decisions under weather uncertainty Energy companies optimiz'
  name: DTN Probabilistic API
  slug: dtn-probabilistic-api
- description: Summarized product volumes by U.S., PADD, Rack City & Terminal
  name: DTN Refined Fuels Demand
  slug: dtn-refined-fuels-demand
- description: DTN’s Renewables API empowers consumers with accurate, global, location-specific environmental data tailored for the renewable energy industry.
  name: DTN Renewables API
  slug: dtn-renewables-api
- description: The DTN Aviation SIGMET/AIRMET API retrieves available SIGMET, Convective SIGMET, SIERRA (visibility) AIRMETs, TANGO (turbulence) AIRMETs, and ZULU (icing) AIRMETs. Each data type has its own endpoint
  name: DTN SIGMETs/AIRMETs API
  slug: dtn-sigmets-airmets
- description: RouteGuard customers can get all the route advices that are sent to their vessels by DTN's route analysts in PDF, RTZ, CSV and JSON format by calling this api endpoint.
  name: DTN Shipping API
  slug: dtn-shipping-api
- description: This API is an all-in-one solution to integrate obtain hourly and daily soil temperature and moisture data valid for a user-defined time range and location. These values not only give estimates of act
  name: DTN Soil Conditions API
  slug: dtn-soil-api
- description: The models are trained using customer provided data to ensure the predictions are tailored to a specific service territory with predictions produced every six (6) hours.
  name: DTN Storm Impact Analytics
  slug: dtn-storm-impact-analytics
- description: The DTN Storm Risk Analytics API delivers AI/ML electricity customers out and weather risk predictions to enable storm event declarations, escalation of emergency preparedness plans, mobilization of r
  name: DTN Storm Risk Analytics API
  slug: dtn-storm-risk-analytics-api
- description: TAFs are a key piece of information required for flight planning and flight operations. DTN TAF API allows customers to get the data critical to them without extra data not needed.
  name: DTN TAFs API
  slug: dtn-tafs-api
- description: DTN's Tropical Cyclone API provides geospatial data for active tropical cyclones, including past tracks, current positions, forecast tracks and error cones, forecast wind radii and swaths, and aircraf
  name: DTN Tropical Cyclone API
  slug: dtn-tropical-api
- description: Websocket API overview. Websocket API summary.
  name: DTN Websocket API
  slug: dtn-websocket-api
- description: Winds Aloft are a key piece of information for flight planning and flight operations. DTN Winds Aloft allows customers to get the data critical to them without extra data.
  name: DTN Winds Aloft API
  slug: dtn-windsaloft-api
- description: APIs to access & manage your orders from within Digital Commerce
  name: DTN Digital Commerce Orders
  slug: digital-commerce-orders
- description: Energy Sales & Marketing Orders, Pricing and Users Management API
  name: DTN Energy Sales & Marketing Integrations API
  slug: energy-digital-commerce-integrations-api
- description: 'The Farm Intelligence API provides access to DTN''s agricultural datasets through three surfaces: the Producer API for producer discovery and details, the Land API for land search, crop history, and ge'
  name: DTN Farm Intel API
  slug: farm-intel-api
- description: How to request radar and text products from RadarScope servers
  name: DTN RadarScope API
  slug: radarscope-radar-products
- description: DTN Weather Conditions API from DTN — 6 path(s) described in OpenAPI.
  name: DTN Weather Conditions API
  slug: dtn-weather-conditions-openapi
artifact_total: 51
asyncapis:
- description: Faithful AsyncAPI rendering of DTN's Agency Bulletin WebSocket API, which streams global weather agency bulletins in real time over a WebSocket upgrade (HTTP 101). Derived from the provider's publishe
  name: DTN Agency Bulletin WebSocket API (event surface)
  slug: dtn-agency-bulletin-websocket-asyncapi
- description: Faithful AsyncAPI rendering of DTN's Lightning Stream API, which delivers lightning strikes as a continuous HTTP stream (chunked delivery). Derived from the provider's published OpenAPI (openapi/dtn-l
  name: DTN Lightning Stream API (event surface)
  slug: dtn-lightning-stream-asyncapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dtn/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dtn-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dtn-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dtn-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dtn-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dtnllc
- group: company
  title: ''
  type: Website
  url: https://www.dtn.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/openapi/dtn-weather-conditions-api-openapi.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/json-schema/dtn-weather-observation-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/json-ld/dtn-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://devportal.dtn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dtn.com/resources/api-data-integrations/
- group: docs
  title: ''
  type: Reference
  url: https://api.weather.mg/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dtn.com/subscription-agreement-standard-terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dtn.com/wp-content/uploads/2020/04/DTN-External-Privacy-Statement.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dtn.com/weather/
- group: company
  title: ''
  type: Blog
  url: https://www.dtn.com/feed/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dtn.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dtn-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dtn-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dtn-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dtn-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dtn-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dtn-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dtn-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dtn-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dtn-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/dtn-lightning-stream-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/dtn-agency-bulletin-websocket-asyncapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dtn-weather-conditions-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dtn-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://dev-portal-api.prd.coreservices.zones.dtn.com/v1/apis/dtn-weather-conditions-api/postman-collection/2.2.0
- group: operate
  title: ''
  type: Support
  url: https://www.dtn.com/contact-us/
- group: docs
  title: ''
  type: APIReference
  url: https://devportal.dtn.com/catalog
created: '2026-05-01'
description: DTN is an operational intelligence company delivering weather, agriculture, energy, and commodity market data through a catalog of 36 published APIs on its developer portal. Coverage spans current conditions, point and probabilistic forecasts, 30-year station observation history, lightning, radar and map tiles, tropical cyclones, marine weather, aviation weather (METARs, TAFs, NOTAMs, PIREPs, SIGMETs, flight hazards), soil conditions, renewables production forecasting, refined fuels, and Prophet X commodity market data. All APIs authenticate with OAuth2 client credentials via the DTN Auth and Identity Service, publish OpenAPI specs and Postman collections, and stream real-time data over WebSocket and HTTP streaming surfaces.
finops:
- name: Dtn Finops
  service_category: Weather & Industry Data
  slug: dtn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dtn.png
json_schemas:
- name: DTN Weather Observation
  property_count: 15
  slug: dtn-weather-observation
jsonld:
- class_count: 2
  name: Dtn Context
  property_count: 20
  slug: dtn-context
layout: provider
mcp_servers:
- description: ''
  name: dtn-mcp.yml
  slug: dtn-mcpyml
modified: '2026-07-22'
name: DTN
nav: Providers
network: true
overview: 'DTN publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Weather Conditions API, Point Observation API, Radar Precipitation Forecast API, and 34 more. Tagged areas include Weather, Agriculture, Energy, Market Data, and Aviation.


  The DTN catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DTN''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, sandbox, and 28 more developer resources.'
plans:
- name: Dtn Plans Pricing
  plan_count: 2
  slug: dtn-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 1
  name: Dtn Rate Limits
  slug: dtn-rate-limits
rules:
- name: DTN API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dtn-jsonschema-spectral-rules
scopes:
- name: Dtn Scopes
  scope_count: 0
  slug: dtn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.4
    developer_ergonomics: 66.8
    discoverability: 68.5
    governance: 69.8
    operational_transparency: 52.6
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dtn/refs/heads/main/screenshots/dtn-2026-06-20T180300.png
security:
- kind: authentication
  name: Dtn Authentication
  slug: dtn-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dtn Domain Security
  slug: dtn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dtn
tags:
- Weather
- Agriculture
- Energy
- Market Data
- Aviation
- Marine
- Forecasting
- Observations
- Commodities
website: https://www.dtn.com/
---
