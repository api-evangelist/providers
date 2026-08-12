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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chicago Transit Authority Agentic Access
  operation_count: 11
  slug: chicago-transit-authority-agentic-access
  summary_line: 11 operations
api_count: 11
apis:
- description: The Customer Alerts API delivers real-time service status, planned outages, and disruption information for CTA bus and rail services. It provides both a route-level status feed and per-route or per-st
  name: CTA Customer Alerts API
  slug: customer-alerts-api
- description: CTA publishes a GTFS (General Transit Feed Specification) schedule feed covering the physical layout, stop locations, and static schedules for the entire CTA bus and L train system. The feed is a down
  name: CTA GTFS Schedule Feed
  slug: gtfs-feed
- description: Train arrival prediction operations
  name: Chicago Transit Authority Arrivals API
  slug: chicago-transit-authority-arrivals-api
- description: The Bulletins API from Chicago Transit Authority — 1 operation(s) for bulletins.
  name: Chicago Transit Authority Bulletins API
  slug: chicago-transit-authority-bulletins-api
- description: Follow an individual train run
  name: Chicago Transit Authority Follow API
  slug: chicago-transit-authority-follow-api
- description: Train geolocation operations
  name: Chicago Transit Authority Locations API
  slug: chicago-transit-authority-locations-api
- description: The Predictions API from Chicago Transit Authority — 1 operation(s) for predictions.
  name: Chicago Transit Authority Predictions API
  slug: chicago-transit-authority-predictions-api
- description: The Routes API from Chicago Transit Authority — 3 operation(s) for routes.
  name: Chicago Transit Authority Routes API
  slug: chicago-transit-authority-routes-api
- description: The Stops API from Chicago Transit Authority — 1 operation(s) for stops.
  name: Chicago Transit Authority Stops API
  slug: chicago-transit-authority-stops-api
- description: The System API from Chicago Transit Authority — 1 operation(s) for system.
  name: Chicago Transit Authority System API
  slug: chicago-transit-authority-system-api
- description: The Vehicles API from Chicago Transit Authority — 1 operation(s) for vehicles.
  name: Chicago Transit Authority Vehicles API
  slug: chicago-transit-authority-vehicles-api
artifact_total: 39
collections:
- collection_type: open
  name: CTA Bus Tracker API
  slug: open-cta-bus-tracker
- collection_type: open
  name: CTA Train Tracker API
  slug: open-cta-train-tracker
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chicago-transit-authority-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chicago-transit-authority-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chicago-transit-authority-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chicago-transit-authority
- group: company
  title: ''
  type: Website
  url: https://www.transitchicago.com/
- group: start
  title: ''
  type: Portal
  url: https://www.transitchicago.com/developers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transitchicago.com/developers/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transitchicago.com/privacy/
- group: auth
  title: ''
  type: APIKeyApplication
  url: https://www.transitchicago.com/developers/traintrackerapply/
- group: start
  title: ''
  type: ChicagoDataPortal
  url: https://data.cityofchicago.org
- group: other
  title: ''
  type: SystemMap
  url: https://www.transitchicago.com/maps/
- group: company
  title: ''
  type: Newsroom
  url: https://www.transitchicago.com/news/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.transitchicago.com/contactus/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chicago-transit-authority-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: spectral/chicago-transit-authority-spectral.yml
- group: other
  title: ''
  type: Standards
  url: ''
created: '2025-05-02'
description: The Chicago Transit Authority (CTA) is the public transit operator for the City of Chicago and 35 surrounding suburbs, operating the second largest public transit system in the United States with bus and rapid-transit (L) train services. The CTA Developer Center publishes open transit data feeds and APIs for developers building rider-facing applications, including the Train Tracker API for real-time L-train arrivals, the Bus Tracker API for real-time bus arrivals and vehicle locations, the Customer Alerts API for service status and disruptions, and GTFS schedule data feeds for the entire CTA bus and rail network.
features:
- name: Real-Time Train Arrivals
- name: Real-Time Bus Arrivals
- name: Train Run Locations
- name: Bus Vehicle Locations
- name: Route and Stop Directories
- name: Customer Alerts and Service Status
- name: Planned Outage Notifications
- name: GTFS Static Schedule Feed
- name: API Key Issuance
- name: Open Chicago Transit Data
finops:
- name: Chicago Transit Authority Finops
  service_category: API
  slug: chicago-transit-authority-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chicago-transit-authority.png
jsonld:
- class_count: 0
  name: Chicago Transit Authority Context
  property_count: 4
  slug: chicago-transit-authority-context
layout: provider
modified: '2026-05-19'
name: Chicago Transit Authority
nav: Providers
network: true
overview: 'Chicago Transit Authority publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Arrivals API, Bulletins API, Follow API, and 6 more. Tagged areas include Bus, Bus Tracker, Chicago, CTA, and Customer Alerts.


  The Chicago Transit Authority catalog on APIs.io includes 1 JSON-LD context.


  Chicago Transit Authority''s developer surface includes authentication, developer portal, and 13 more developer resources.'
plans:
- name: Chicago Transit Authority Plans Pricing
  plan_count: 3
  slug: chicago-transit-authority-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Chicago Transit Authority Rate Limits
  slug: chicago-transit-authority-rate-limits
score:
  band: thin
  composite: 36.7
  delta: -7.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/chicago-transit-authority/refs/heads/main/screenshots/chicago-transit-authority-2026-06-20T174303.png
security:
- kind: authentication
  name: Chicago Transit Authority Authentication
  slug: chicago-transit-authority-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chicago Transit Authority Domain Security
  slug: chicago-transit-authority-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chicago-transit-authority
tags:
- Bus
- Bus Tracker
- Chicago
- CTA
- Customer Alerts
- GTFS
- L Train
- Open Data
- Public Transit
- Real-Time
- Train
- Train Tracker
- Transit
- Transportation
use_cases:
- name: Rider-Facing Mobile Apps
- name: Trip Planners and Routing
- name: Real-Time Arrival Displays
- name: Service Disruption Notifications
- name: Schedule Visualizations
- name: Accessibility Tooling
- name: Smart City Dashboards
- name: Multimodal Transit Apps
- name: Research and Open Data Analysis
website: https://www.transitchicago.com/
---
