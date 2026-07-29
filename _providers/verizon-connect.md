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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 18
apis:
- description: Exchanges Base64-encoded Reveal REST credentials for a short-lived bearer authorization token (valid ~20 minutes) via GET /token. Subsequent API calls send an Atmosphere authorization header combining
  name: Verizon Connect Token Authorization API
  slug: verizon-connect-token-authorization-api
- description: Retrieves the vehicles tracked within a Reveal account and their configuration and metadata. Related documented surfaces include the Vehicle Update API and the Attribute API for custom vehicle attribu
  name: Verizon Connect Vehicle API
  slug: verizon-connect-vehicle-api
- description: The Vehicle Update API in the Reveal Real-time Aggregated Data suite lets integrated customers and partners poll the latest GPS position and status captured by vehicles tracked in a Reveal account. De
  name: Verizon Connect Vehicle Location API
  slug: verizon-connect-vehicle-location-api
- description: Retrieves the GPS history for a specified period within a Reveal account, using vehicle number as the unique identifier with a standard GET verb. Endpoints modeled from the published API documentation
  name: Verizon Connect Vehicle GPS History API
  slug: verizon-connect-vehicle-gps-history-api
- description: Provides vehicle trip / segment data - the stops, drives, idles, and journey detail derived from GPS activity for vehicles in a Reveal account. Endpoints modeled from the published API list.
  name: Verizon Connect Vehicle Segment Data API
  slug: verizon-connect-vehicle-segment-data-api
- description: Retrieves and manages the drivers in a Reveal account and their profile data. Endpoints modeled from the published API list.
  name: Verizon Connect Driver API
  slug: verizon-connect-driver-api
- description: Retrieves a specified driver's current activity status (for example GET driver status by driver number), with a companion Driver Status Options API for the configurable status values. Endpoints modele
  name: Verizon Connect Driver Status API
  slug: verizon-connect-driver-status-api
- description: Manages the assignment of drivers to vehicles within a Reveal account. Endpoints modeled from the published API list.
  name: Verizon Connect Driver Assignment API
  slug: verizon-connect-driver-assignment-api
- description: Exposes driver safety and behavior data such as harsh driving, speeding, and related risk events captured across the fleet. Endpoints modeled from the published API list.
  name: Verizon Connect Driver Safety API
  slug: verizon-connect-driver-safety-api
- description: Provides logbook and hours-of-service compliance information (for example current logbook status by driver) to third-party time card reporting, maintenance, routing, and dispatching systems. Endpoints
  name: Verizon Connect Logbook API
  slug: verizon-connect-logbook-api
- description: Manages geofences (Places) - the named locations and boundaries used to trigger entry/exit alerts and location reporting in Reveal. Endpoints modeled from the published API list.
  name: Verizon Connect Geofence API
  slug: verizon-connect-geofence-api
- description: Manages the groups used to organize vehicles, drivers, and assets in a Reveal account, with a companion Group Relocation API for moving entities between groups. Endpoints modeled from the published AP
  name: Verizon Connect Group API
  slug: verizon-connect-group-api
- description: Creates and manages field-service work orders, with companion Work Order Status API and Work Order Type API surfaces for the supporting reference data. Endpoints modeled from the published API list.
  name: Verizon Connect Work Order API
  slug: verizon-connect-work-order-api
- description: Tracks non-powered assets such as trailers and equipment, with companion Non-Powered Assets Update API (latest position/status polling) and Non-Powered Assets GPS History API surfaces. Endpoints model
  name: Verizon Connect Non-Powered Assets API
  slug: verizon-connect-non-powered-assets-api
- description: Exposes fleet inspection (DVIR-style) records completed by drivers, for integration with maintenance and compliance systems. Endpoints modeled from the published API list.
  name: Verizon Connect Fleet Inspections API
  slug: verizon-connect-fleet-inspections-api
- description: 'Provides dash-cam / video safety events captured by Verizon Connect Integrated Video, for pulling triggered clips and event metadata into external safety systems. Endpoints modeled from the published '
  name: Verizon Connect Video Event API
  slug: verizon-connect-video-event-api
- description: Manages the Reveal account users and their details. Endpoints modeled from the published API list.
  name: Verizon Connect User API
  slug: verizon-connect-user-api
- description: Reveal supports two webhook categories - Alert webhooks (event notifications such as Idling, Geofence/Place, Harsh Driving, Ignition, Speeding, Late Start, Long Stop, Sensor activation, Low Battery) a
  name: Verizon Connect Webhooks
  slug: verizon-connect-webhooks
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verizon-connect-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verizonconnect
- group: company
  title: ''
  type: Website
  url: https://www.verizonconnect.com
- group: docs
  title: ''
  type: Documentation
  url: https://reveal-help.verizonconnect.com/hc/en-us/sections/5491620930451-API-integrations
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fim.us.fleetmatics.com
- group: start
  title: ''
  type: SignUp
  url: https://www.verizonconnect.com/services/api-integration/
- group: commercial
  title: ''
  type: Plans
  url: plans/verizon-connect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/verizon-connect-rate-limits.yml
created: '2026-07-04'
description: Verizon Connect is the fleet management, telematics, and GPS vehicle tracking business of Verizon (it grew out of Verizon's acquisitions of Fleetmatics and Telogis). Its Reveal platform exposes a documented suite of REST APIs and webhooks - the Reveal Integration Services / Fleetmatics Integration Manager (FIM) APIs - covering vehicles, drivers, GPS positions and history, trips (segments), driver status and safety, hours-of-service logbooks, geofences (places), groups, work orders, non-powered asset tracking, fleet inspections, and dash-cam video events. The API is not openly self-service - access is gated to Reveal customers and their approved integration partners, who request Integration Manager and Reveal REST credentials through the Reveal marketplace before they can call the documented endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verizon-connect.png
layout: provider
modified: '2026-07-04'
name: Verizon Connect
nav: Providers
network: true
overview: 'Verizon Connect publishes 18 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Telematics, GPS Tracking, Vehicle Tracking, and Fleet Tracking.


  Verizon Connect''s developer surface includes documentation, signup flow, and 6 more developer resources.'
plans:
- name: Verizon Connect Plans Pricing
  plan_count: 3
  slug: verizon-connect-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 0
  name: Verizon Connect Rate Limits
  slug: verizon-connect-rate-limits
score:
  band: emerging
  composite: 19.8
  delta: -2.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Verizon Connect Domain Security
  slug: verizon-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verizon-connect
tags:
- Fleet Management
- Telematics
- GPS Tracking
- Vehicle Tracking
- Fleet Tracking
- Verizon
- Fleetmatics
website: https://www.verizonconnect.com
---
