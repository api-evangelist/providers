---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Marine Traffic Agentic Access
  operation_count: 78
  slug: marine-traffic-agentic-access
  summary_line: 78 operations · 2 acting
api_count: 14
apis:
- description: The AIS API API from MarineTraffic — 3 operation(s) for ais api.
  name: MarineTraffic AIS API API
  slug: marine-traffic-ais-api-api
- description: The Balances API from MarineTraffic — 1 operation(s) for balances.
  name: MarineTraffic Balances API
  slug: marine-traffic-balances-api
- description: The Fleets API from MarineTraffic — 4 operation(s) for fleets.
  name: MarineTraffic Fleets API
  slug: marine-traffic-fleets-api
- description: The Passage Plans API from MarineTraffic — 1 operation(s) for passage plans.
  name: MarineTraffic Passage Plans API
  slug: marine-traffic-passage-plans-api
- description: The Port Events API from MarineTraffic — 2 operation(s) for port events.
  name: MarineTraffic Port Events API
  slug: marine-traffic-port-events-api
- description: The Ports Information API from MarineTraffic — 4 operation(s) for ports information.
  name: MarineTraffic Ports Information API
  slug: marine-traffic-ports-information-api
- description: The Reverse Geocoding API from MarineTraffic — 1 operation(s) for reverse geocoding.
  name: MarineTraffic Reverse Geocoding API
  slug: marine-traffic-reverse-geocoding-api
- description: The Routing Information API from MarineTraffic — 2 operation(s) for routing information.
  name: MarineTraffic Routing Information API
  slug: marine-traffic-routing-information-api
- description: The Search Vessel API from MarineTraffic — 2 operation(s) for search vessel.
  name: MarineTraffic Search Vessel API
  slug: marine-traffic-search-vessel-api
- description: The Single Vessel Events API from MarineTraffic — 3 operation(s) for single vessel events.
  name: MarineTraffic Single Vessel Events API
  slug: marine-traffic-single-vessel-events-api
- description: The Vessel Historical Track API from MarineTraffic — 2 operation(s) for vessel historical track.
  name: MarineTraffic Vessel Historical Track API
  slug: marine-traffic-vessel-historical-track-api
- description: The Vessel Information API from MarineTraffic — 2 operation(s) for vessel information.
  name: MarineTraffic Vessel Information API
  slug: marine-traffic-vessel-information-api
- description: The Vessel Positions (Legacy API) API from MarineTraffic — 7 operation(s) for vessel positions (legacy api).
  name: MarineTraffic Vessel Positions (Legacy API) API
  slug: marine-traffic-vessel-positions-legacy-api-api
- description: The Voyage Information API from MarineTraffic — 5 operation(s) for voyage information.
  name: MarineTraffic Voyage Information API
  slug: marine-traffic-voyage-information-api
artifact_total: 75
collections:
- collection_type: open
  name: MarineTraffic Events API
  slug: open-marine-traffic-events
- collection_type: open
  name: MarineTraffic Ports Information API
  slug: open-marine-traffic-ports-info
- collection_type: open
  name: MarineTraffic Power User API
  slug: open-marine-traffic-power-user
- collection_type: open
  name: MarineTraffic Reverse Geocoding API
  slug: open-marine-traffic-reverse-geocoding
- collection_type: open
  name: MarineTraffic Routing Information API
  slug: open-marine-traffic-routing
- collection_type: open
  name: MarineTraffic Vessel Positions API
  slug: open-marine-traffic-vessel-positions
- collection_type: open
  name: MarineTraffic Vessels Data API
  slug: open-marine-traffic-vessels-data
- collection_type: open
  name: MarineTraffic Voyage Information API
  slug: open-marine-traffic-voyage-info
- collection_type: open
  name: MarineTraffic AIS Data API
  slug: open-marine-traffic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marine-traffic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marine-traffic-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.marinetraffic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://servicedocs.marinetraffic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://servicedocs.marinetraffic.com/
- group: start
  title: ''
  type: Portal
  url: https://www.kpler.com/product/maritime/data-services
- group: operate
  title: ''
  type: Support
  url: https://support.marinetraffic.com/en/articles/9552659-api-services
- group: design
  title: ''
  type: ErrorCodes
  url: https://support.marinetraffic.com/en/articles/9552800-api-most-common-response-error-codes
- group: docs
  title: ''
  type: Documentation
  url: https://support.marinetraffic.com/en/articles/9552860-what-kind-of-information-is-ais-transmitted
- group: operate
  title: ''
  type: Support
  url: https://support.marinetraffic.com/
- group: start
  title: ''
  type: Sandbox
  url: https://www.marinetraffic.com/en/ais/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marinetraffic
- group: build
  title: ''
  type: Tools
  url: https://github.com/marinetraffic/mt-ais-toolbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marinetraffic
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MarineTraffic
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/marine-traffic-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/marine-traffic-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/marine-traffic-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/marine-traffic-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/marine-traffic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marine-traffic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marine-traffic-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: MarineTraffic is the leading maritime intelligence and AIS ship-tracking platform — now part of Kpler. The MarineTraffic AIS Data API exposes the same live + historical vessel positions, port calls, berth calls, vessel master data, voyage forecasts, predictive arrivals, port-congestion analytics, sea-lane routing, reverse geocoding, and fleet management endpoints that power the public marinetraffic.com map and the Kpler maritime data services. Data is sourced from 13,000+ terrestrial AIS receivers plus satellite AIS, served as REST/JSON (with CSV / XML / JSONO alternatives), authenticated via a per-key prepaid credit balance, and metered in credits per response row with per-service refresh-interval caching.
examples:
- key_count: 20
  name: Marine Traffic Port Call Example
  slug: marine-traffic-port-call-example
- key_count: 28
  name: Marine Traffic Vessel Position Example
  slug: marine-traffic-vessel-position-example
- key_count: 13
  name: Marine Traffic Voyage Forecast Example
  slug: marine-traffic-voyage-forecast-example
features:
- description: Vessel positions sourced from 13,000+ terrestrial AIS receivers and satellite AIS, accessible by single vessel, fleet, area of interest, port, or bounding box. Default delay 1 hour; real-time access via enterprise contract.
  name: AIS vessel positions (live + delayed)
- description: Replay a vessel's AIS track over a defined date / day window.
  name: Vessel historical track
- description: Provider-detected arrival, departure, and berth-touch events per vessel and per port, with voyage duration and time-in-port.
  name: Port calls and berth calls
- description: Static AIS plus MarineTraffic-enriched fields — owner, manager, builder, class, build year, dimensions, deadweight, gross tonnage.
  name: Vessel master data
- description: Ship-photo retrieval via VD01.
  name: Vessel photographs
- description: Search the ship database by identifier (IMO / MMSI / SHIP_ID / call sign) or by name.
  name: Vessel search
- description: Predictive destination, ETA, and route distance for a single vessel or a whole fleet (VI01).
  name: Voyage forecasts
- description: Probability-ranked candidate destination ports for a vessel or fleet (VI04).
  name: Predictive destination areas
- description: Predictive ETA to a specific destination port (VI07).
  name: ETA to port
- description: Per-port arrival forecasts (VI02 / VI05) filtered by market, ship class, draught, and time window.
  name: Expected and predictive port arrivals
- description: Anchorage time, in-port time, vessel and call counts per port / market / ship-class / ISO week (VI06).
  name: Port congestion analytics
- description: Sea-lane-aware route + distance computation between origin and destination (VI03).
  name: Maritime routing
- description: Coordinate-to-maritime-location resolution (port, anchorage, berth, terminal, custom area) (GI01).
  name: Reverse geocoding
- description: CRUD on power-user fleets — set, get, list, clear (PU01–PU05).
  name: Fleet management
- description: Live balance inspection via /exportcredits (free).
  name: Account credit balance
- description: POST /import-passage-plan to ingest voyage plans for power-user fleets.
  name: Passage plan import
- description: Per-call response format — json (default), jsono, xml, csv — via the protocol query parameter.
  name: Multiple response protocols
- description: Hybrid global coverage operated by Kpler / MarineTraffic.
  name: 13,000+ terrestrial AIS receivers + satellite AIS
- description: Direct NMEA AIS streams available as an enterprise data product alongside the REST API.
  name: Live NMEA streams (enterprise)
- description: Hosted cloud-database access and bulk CSV deliveries for high-volume customers.
  name: Cloud database / bulk delivery (enterprise)
finops:
- name: Marine Traffic Finops
  service_category: Maritime Data and Analytics
  slug: marine-traffic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marine-traffic.png
integrations:
- description: MarineTraffic is part of the Kpler maritime intelligence platform; AIS APIs sit alongside Kpler trade flow data.
  name: Kpler
- description: Standard REST + JSON; works directly in Postman, Insomnia, or any HTTP client.
  name: Postman / API clients
- description: Output is lat/lon-tagged — integrates with QGIS, Mapbox, Leaflet, and Esri.
  name: GIS / mapping
- description: Enterprise NMEA streams integrate with ECDIS, fleet-management software, and bridge electronics.
  name: NMEA-compatible bridge systems
- description: MarineTraffic publishes mt-ais-toolbox on GitHub for density-map generation from AIS data.
  name: AIS density-map toolbox
json_schemas:
- name: MarineTraffic Port Call
  property_count: 24
  slug: marine-traffic-port-call
- name: MarineTraffic Port
  property_count: 12
  slug: marine-traffic-port
- name: MarineTraffic Vessel Master Data
  property_count: 23
  slug: marine-traffic-vessel-master
- name: MarineTraffic Vessel Position
  property_count: 28
  slug: marine-traffic-vessel-position
- name: MarineTraffic Voyage Forecast
  property_count: 13
  slug: marine-traffic-voyage-forecast
jsonld:
- class_count: 0
  name: Marine Traffic Context
  property_count: 7
  slug: marine-traffic-context
layout: provider
modified: '2026-05-25'
name: MarineTraffic
nav: Providers
network: true
overview: 'MarineTraffic publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AIS API API, Balances API, Fleets API, and 11 more. Tagged areas include AIS, Maritime, Vessel Tracking, Shipping, and Ports.


  The MarineTraffic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MarineTraffic''s developer surface includes developer portal, documentation, API reference, support, sandbox, tooling, and 16 more developer resources.'
plans:
- name: Marine Traffic Plans Pricing
  plan_count: 2
  slug: marine-traffic-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 0
  name: Marine Traffic Rate Limits
  slug: marine-traffic-rate-limits
rules:
- name: MarineTraffic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: marine-traffic-jsonschema-spectral-rules
- name: MarineTraffic API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: marine-traffic-rules
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.6
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marine-traffic/refs/heads/main/screenshots/marine-traffic-2026-06-20T184946.png
security:
- kind: domain-security
  name: Marine Traffic Domain Security
  slug: marine-traffic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marine-traffic
solutions:
- description: Public REST APIs metered against a prepaid credit balance — what this catalog covers.
  name: Self-serve REST API
- description: Raw NMEA AIS for bridge-side and processing-pipeline customers (enterprise).
  name: NMEA live AIS streams
- description: Hosted MarineTraffic database for SQL / analytics workloads (enterprise).
  name: Cloud database access
- description: Bespoke CSV / JSON delivery against custom queries (enterprise).
  name: Custom data extracts
tags:
- AIS
- Maritime
- Vessel Tracking
- Shipping
- Ports
- Voyage Forecasting
- Geospatial
- Kpler
use_cases:
- description: Power voyage analytics, tonnage tracking, and supply forecasting for commodity desks.
  name: Commodity trading and freight intelligence
- description: Anticipate berth demand, optimize pilotage and tug allocation, and reduce dwell.
  name: Port operations and logistics
- description: Build fleet dashboards and customer-facing tracking pages using PS04 + VI07.
  name: Vessel tracking dashboards
- description: Detect dark fleet behavior, AIS gaps, port-call patterns, and sanctioned vessel touches.
  name: Compliance and sanctions monitoring
- description: Underwrite hull / P&I and route insurance with verified call histories and port-congestion data.
  name: Marine insurance underwriting
- description: Feed maritime domain awareness systems with AIS, port-call, and routing context.
  name: Government and coast guard situational awareness
- description: Compute voyage-level CO2 estimates by combining VI03 routing + VD02 master data + AIS speed.
  name: Carbon and ESG reporting
website: https://www.marinetraffic.com/
---
