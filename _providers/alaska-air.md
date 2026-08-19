---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Alaska Air Agentic Access
  operation_count: 11
  slug: alaska-air-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 8
apis:
- description: Airport information for Alaska Airlines served destinations
  name: Alaska Airlines Airports API
  slug: alaska-air-airports-api
- description: Real-time flight status and tracking for Alaska Airlines and Horizon Air flights
  name: Alaska Airlines Flight Status API
  slug: alaska-air-flight-status-api
- description: Mileage Plan member data and tier information
  name: Alaska Airlines Members API
  slug: alaska-air-members-api
- description: Partner mile reporting for hotel, car rental, and retail activities
  name: Alaska Airlines Partner Miles API
  slug: alaska-air-partner-miles-api
- description: Cargo rate estimation
  name: Alaska Airlines Rates API
  slug: alaska-air-rates-api
- description: Flight schedule data for Alaska Airlines and Horizon Air routes
  name: Alaska Airlines Schedules API
  slug: alaska-air-schedules-api
- description: Cargo shipment booking and tracking operations
  name: Alaska Airlines Shipments API
  slug: alaska-air-shipments-api
- description: Mile earn and redemption transaction history
  name: Alaska Airlines Transactions API
  slug: alaska-air-transactions-api
artifact_total: 112
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alaska Air Cargo Airports API
  slug: open-alaska-air-airports-api
- collection_type: open
  name: Alaska Air Cargo Airports Flight Status API
  slug: open-alaska-air-flight-status-api
- collection_type: open
  name: Alaska Air Cargo Airports Members API
  slug: open-alaska-air-members-api
- collection_type: open
  name: Alaska Air Cargo Airports Partner Miles API
  slug: open-alaska-air-partner-miles-api
- collection_type: open
  name: Alaska Air Cargo Airports Rates API
  slug: open-alaska-air-rates-api
- collection_type: open
  name: Alaska Air Cargo Airports Schedules API
  slug: open-alaska-air-schedules-api
- collection_type: open
  name: Alaska Air Cargo Airports Shipments API
  slug: open-alaska-air-shipments-api
- collection_type: open
  name: Alaska Air Cargo Airports Transactions API
  slug: open-alaska-air-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alaska-air-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alaska-air-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alaska-air-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alaska-air-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlaskaAirlines
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alaska-airlines
- group: company
  title: ''
  type: Website
  url: https://www.alaskaair.com
- group: start
  title: ''
  type: Portal
  url: https://developers.alaskaair.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alaskaair.com/content/about-us/news-and-events
- group: operate
  title: ''
  type: Support
  url: https://www.alaskaair.com/content/about-us/investor-relations
- group: docs
  title: Alaska Air Cargo Portal
  type: Documentation
  url: https://www.alaskacargo.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/alaska-air-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/alaska-air-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/alaska-air-context.jsonld
created: '2024-01-01'
description: Alaska Air Group is the parent company of Alaska Airlines and Horizon Air, providing passenger and cargo air transportation throughout the United States, Mexico, Canada, Costa Rica, and Belize. Alaska Airlines offers a developer portal at developers.alaskaair.com for accessing flight status, schedules, and other APIs, and operates Alaska Air Cargo serving 115+ destinations worldwide with dedicated cargo aircraft.
examples:
- key_count: 4
  name: Alaska Air Cargo Dimensions Example
  slug: alaska-air-cargo-dimensions-example
- key_count: 6
  name: Alaska Air Cargo Rate Request Example
  slug: alaska-air-cargo-rate-request-example
- key_count: 8
  name: Alaska Air Cargo Rate Response Example
  slug: alaska-air-cargo-rate-response-example
- key_count: 8
  name: Alaska Air Cargo Shipment Example
  slug: alaska-air-cargo-shipment-example
- key_count: 2
  name: Alaska Air Cargo Shipment List Example
  slug: alaska-air-cargo-shipment-list-example
- key_count: 9
  name: Alaska Air Cargo Shipment Request Example
  slug: alaska-air-cargo-shipment-request-example
- key_count: 7
  name: Alaska Air Cargo Shipment Tracking Example
  slug: alaska-air-cargo-shipment-tracking-example
- key_count: 4
  name: Alaska Air Cargo Tracking Event Example
  slug: alaska-air-cargo-tracking-event-example
- key_count: 8
  name: Alaska Air Flight Schedules Airport Info Example
  slug: alaska-air-flight-schedules-airport-info-example
- key_count: 2
  name: Alaska Air Flight Schedules Airport List Example
  slug: alaska-air-flight-schedules-airport-list-example
- key_count: 9
  name: Alaska Air Flight Schedules Schedule Example
  slug: alaska-air-flight-schedules-schedule-example
- key_count: 4
  name: Alaska Air Flight Schedules Schedule Response Example
  slug: alaska-air-flight-schedules-schedule-response-example
- key_count: 2
  name: Alaska Air Flight Status Aircraft Example
  slug: alaska-air-flight-status-aircraft-example
- key_count: 8
  name: Alaska Air Flight Status Airport Example
  slug: alaska-air-flight-status-airport-example
- key_count: 4
  name: Alaska Air Flight Status Flight List Example
  slug: alaska-air-flight-status-flight-list-example
- key_count: 9
  name: Alaska Air Flight Status Flight Status Example
  slug: alaska-air-flight-status-flight-status-example
- key_count: 6
  name: Alaska Air Flight Status Flight Summary Example
  slug: alaska-air-flight-status-flight-summary-example
- key_count: 8
  name: Alaska Air Mileage Plan Member Example
  slug: alaska-air-mileage-plan-member-example
- key_count: 8
  name: Alaska Air Mileage Plan Partner Miles Request Example
  slug: alaska-air-mileage-plan-partner-miles-request-example
- key_count: 5
  name: Alaska Air Mileage Plan Partner Miles Response Example
  slug: alaska-air-mileage-plan-partner-miles-response-example
- key_count: 6
  name: Alaska Air Mileage Plan Transaction Example
  slug: alaska-air-mileage-plan-transaction-example
- key_count: 3
  name: Alaska Air Mileage Plan Transaction List Example
  slug: alaska-air-mileage-plan-transaction-list-example
features:
- description: Track live flight status, departure and arrival times, gate assignments, and delay information for Alaska Airlines and Horizon Air flights.
  name: Real-Time Flight Status
- description: Access flight schedule data including routes, operating days, departure/arrival times, and equipment across the Alaska network.
  name: Flight Schedules
- description: Book shipments and track cargo across 115+ destinations worldwide via Alaska Air Cargo's network, including dedicated widebody aircraft.
  name: Cargo Booking and Tracking
- description: Get real-time rate estimates for cargo shipments based on origin, destination, weight, dimensions, and special handling requirements.
  name: Cargo Rate Estimates
- description: Enable partner mile accrual and redemption for Alaska's Mileage Plan loyalty program across airline, hotel, car rental, and retail partners.
  name: Mileage Plan Partner Integration
- description: Alaska Air Cargo operates the only U.S. passenger airline with dedicated cargo aircraft (Airbus A330s and Boeing 787s) for increased capacity on key routes.
  name: Dedicated Cargo Aircraft
- description: Support for dangerous goods transport, live animal shipments via Pet Connect, and international cargo across Asia, Pacific, Canada, and Mexico.
  name: Specialized Cargo Services
- description: Developer portal powered by Microsoft Azure API Management with subscription-based key management, interactive API console, and automatic API documentation generation.
  name: API Management via Azure
finops:
- name: Alaska Air Finops
  service_category: Travel & Transportation
  slug: alaska-air-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alaska-air.png
integrations:
- description: Developer portal and API gateway powered by Azure API Management with subscription key management and interactive testing console.
  name: Microsoft Azure API Management
- description: Alaska Air Cargo partnerships including connections with Hawaiian Airlines cargo network for Pacific and inter-island routes.
  name: Hawaiian Airlines
- description: Member of the oneworld airline alliance enabling Mileage Plan accrual and redemption across 13 member airlines.
  name: One World Alliance
- description: Third-party travel API provider enabling search, booking, and ticket issuance for Alaska Airlines flights.
  name: Duffel
- description: Customer service platform integration for Alaska Air Cargo live chat and support operations.
  name: Five9
json_schemas:
- name: Dimensions
  property_count: 4
  slug: alaska-air-cargo-dimensions
- name: RateRequest
  property_count: 6
  slug: alaska-air-cargo-rate-request
- name: RateResponse
  property_count: 8
  slug: alaska-air-cargo-rate-response
- name: ShipmentList
  property_count: 2
  slug: alaska-air-cargo-shipment-list
- name: ShipmentRequest
  property_count: 9
  slug: alaska-air-cargo-shipment-request
- name: Shipment
  property_count: 8
  slug: alaska-air-cargo-shipment
- name: ShipmentTracking
  property_count: 7
  slug: alaska-air-cargo-shipment-tracking
- name: TrackingEvent
  property_count: 4
  slug: alaska-air-cargo-tracking-event
- name: AirportInfo
  property_count: 8
  slug: alaska-air-flight-schedules-airport-info
- name: AirportList
  property_count: 2
  slug: alaska-air-flight-schedules-airport-list
- name: ScheduleResponse
  property_count: 4
  slug: alaska-air-flight-schedules-schedule-response
- name: Schedule
  property_count: 9
  slug: alaska-air-flight-schedules-schedule
- name: Aircraft
  property_count: 2
  slug: alaska-air-flight-status-aircraft
- name: Airport
  property_count: 8
  slug: alaska-air-flight-status-airport
- name: FlightList
  property_count: 4
  slug: alaska-air-flight-status-flight-list
- name: FlightStatus
  property_count: 9
  slug: alaska-air-flight-status-flight-status
- name: FlightSummary
  property_count: 6
  slug: alaska-air-flight-status-flight-summary
- name: Member
  property_count: 8
  slug: alaska-air-mileage-plan-member
- name: PartnerMilesRequest
  property_count: 8
  slug: alaska-air-mileage-plan-partner-miles-request
- name: PartnerMilesResponse
  property_count: 5
  slug: alaska-air-mileage-plan-partner-miles-response
- name: TransactionList
  property_count: 3
  slug: alaska-air-mileage-plan-transaction-list
- name: Transaction
  property_count: 6
  slug: alaska-air-mileage-plan-transaction
json_structures:
- name: Alaska Air Cargo Dimensions Structure
  property_count: 4
  slug: alaska-air-cargo-dimensions-structure
- name: Alaska Air Cargo Rate Request Structure
  property_count: 6
  slug: alaska-air-cargo-rate-request-structure
- name: Alaska Air Cargo Rate Response Structure
  property_count: 8
  slug: alaska-air-cargo-rate-response-structure
- name: Alaska Air Cargo Shipment List Structure
  property_count: 2
  slug: alaska-air-cargo-shipment-list-structure
- name: Alaska Air Cargo Shipment Request Structure
  property_count: 9
  slug: alaska-air-cargo-shipment-request-structure
- name: Alaska Air Cargo Shipment Structure
  property_count: 8
  slug: alaska-air-cargo-shipment-structure
- name: Alaska Air Cargo Shipment Tracking Structure
  property_count: 7
  slug: alaska-air-cargo-shipment-tracking-structure
- name: Alaska Air Cargo Tracking Event Structure
  property_count: 4
  slug: alaska-air-cargo-tracking-event-structure
- name: Alaska Air Flight Schedules Airport Info Structure
  property_count: 8
  slug: alaska-air-flight-schedules-airport-info-structure
- name: Alaska Air Flight Schedules Airport List Structure
  property_count: 2
  slug: alaska-air-flight-schedules-airport-list-structure
- name: Alaska Air Flight Schedules Schedule Response Structure
  property_count: 4
  slug: alaska-air-flight-schedules-schedule-response-structure
- name: Alaska Air Flight Schedules Schedule Structure
  property_count: 9
  slug: alaska-air-flight-schedules-schedule-structure
- name: Alaska Air Flight Status Aircraft Structure
  property_count: 2
  slug: alaska-air-flight-status-aircraft-structure
- name: Alaska Air Flight Status Airport Structure
  property_count: 8
  slug: alaska-air-flight-status-airport-structure
- name: Alaska Air Flight Status Flight List Structure
  property_count: 4
  slug: alaska-air-flight-status-flight-list-structure
- name: Alaska Air Flight Status Flight Status Structure
  property_count: 9
  slug: alaska-air-flight-status-flight-status-structure
- name: Alaska Air Flight Status Flight Summary Structure
  property_count: 6
  slug: alaska-air-flight-status-flight-summary-structure
- name: Alaska Air Mileage Plan Member Structure
  property_count: 8
  slug: alaska-air-mileage-plan-member-structure
- name: Alaska Air Mileage Plan Partner Miles Request Structure
  property_count: 8
  slug: alaska-air-mileage-plan-partner-miles-request-structure
- name: Alaska Air Mileage Plan Partner Miles Response Structure
  property_count: 5
  slug: alaska-air-mileage-plan-partner-miles-response-structure
- name: Alaska Air Mileage Plan Transaction List Structure
  property_count: 3
  slug: alaska-air-mileage-plan-transaction-list-structure
- name: Alaska Air Mileage Plan Transaction Structure
  property_count: 6
  slug: alaska-air-mileage-plan-transaction-structure
jsonld:
- class_count: 22
  name: Alaska Air Context
  property_count: 84
  slug: alaska-air-context
layout: provider
modified: '2026-05-19'
name: Alaska Airlines
nav: Providers
network: true
overview: 'Alaska Airlines publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Airports API, Flight Status API, Members API, and 5 more. Tagged areas include Airlines, Aviation, Travel, Cargo, and Loyalty.


  The Alaska Airlines catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Alaska Airlines'' developer surface includes authentication, developer portal, engineering blog, support, documentation, and 9 more developer resources.'
plans:
- name: Alaska Air Plans Pricing
  plan_count: 1
  slug: alaska-air-plans-pricing
press:
- date: '2026-05-25'
  title: Alaska Airlines and UP.Labs launch Odysee, an AI- ...
  url: https://news.alaskaair.com/company/alaska-airlines-up-labs-launch-odysee-ai-enabled-startup-taking-a-new-approach-to-schedule-optimization/
- date: '2026-05-25'
  title: Alaska Airlines Group Sets Innovation Path at APEX TECH ...
  url: https://apex.aero/articles/alaska-airlines-group-sets-innovation-path-at-apex-tech-2025-keynote/
- date: '2026-05-25'
  title: Alaska Airlines and Airspace Intelligence announce first-of- ...
  url: https://news.alaskaair.com/newsroom/alaska-airlines-and-airspace-intelligence-announce-first-of-its-kind-partnership-to-optimize-air-traffic-flow-with-artificial-intelligence-and-machine-learning/
- date: '2026-05-25'
  title: Alaska Air Group details 2025 operations and risks - ALK
  url: https://www.stocktitan.net/sec-filings/ALK/10-k-alaska-air-group-inc-files-annual-report-e351e80cfb66.html
- date: '2026-05-25'
  title: Alaska Airlines and Tailsight launch AI-powered ...
  url: https://www.prnewswire.com/news-releases/alaska-airlines-and-tailsight-launch-ai-powered-maintenance-planning-solution-302744315.html
random_paper: 88
rate_limits:
- limit_count: 1
  name: Alaska Air Rate Limits
  slug: alaska-air-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Alaska Airlines API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: alaska-air-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Alaska Airlines API Rules
  rule_count: 36
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 18
  slug: alaska-air-spectral-rules
scopes:
- name: Alaska Air Scopes
  scope_count: 2
  slug: alaska-air-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 27.4
  delta: -5.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 22.9
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/screenshots/alaska-air-2026-06-20T171459.png
security:
- kind: authentication
  name: Alaska Air Authentication
  slug: alaska-air-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Alaska Air Domain Security
  slug: alaska-air-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: alaska-air
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
- Fortune 500
use_cases:
- description: Integrate Alaska Airlines flight schedules and status into online travel agencies and booking platforms for real-time availability and status updates.
  name: Travel Agent and OTA Integration
- description: Enable freight forwarders and cargo brokers to book shipments, get rate quotes, and track Alaska Air Cargo shipments programmatically.
  name: Cargo Partner Booking
- description: Integrate Mileage Plan mile accrual into partner platforms (hotels, car rentals, credit cards) to automatically report earned miles.
  name: Loyalty Partner Mile Reporting
- description: Power airport operations systems and display boards with real-time Alaska Airlines flight status and gate assignment data.
  name: Airport Operations Display
- description: Integrate Alaska Airlines flight data into corporate travel management systems for booking, tracking, and expense reporting.
  name: Corporate Travel Management
- description: Embed Alaska Airlines flight status and schedule data into third-party mobile applications for travelers.
  name: Mobile App Integration
website: https://www.alaskaair.com
---
