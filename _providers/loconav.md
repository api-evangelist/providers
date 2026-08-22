---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-19'
api_count: 12
apis:
- description: <p>With our Alert subscription APIs, you can manage the alerts effectively on a platform</p>
  name: LocoNav Alert Subscriptions API
  slug: loconav-alert-subscriptions-api
- description: The Alerts API from LocoNav — 2 operation(s) for alerts.
  name: LocoNav Alerts API
  slug: loconav-alerts-api
- description: The Alerts Subscriptions API from LocoNav — 1 operation(s) for alerts subscriptions.
  name: LocoNav Alerts Subscriptions API
  slug: loconav-alerts-subscriptions-api
- description: <p>Efficient driver management is essential for the optimal operation of a fleet.</p> <p>Leveraging the capabilities of LocoNav REST APIs, fleet managers can seamlessly create, update, and retrieve de
  name: LocoNav Drivers API
  slug: loconav-drivers-api
- description: The Mobilization API from LocoNav — 2 operation(s) for mobilization.
  name: LocoNav Mobilization API
  slug: loconav-mobilization-api
- description: <p>A geofence is a virtual boundary, often a <strong>rectangular bounding box</strong>, created using mapping software with specified latitude and longitude coordinates. Integrated with fleet manageme
  name: LocoNav Polygon (Geofence) API
  slug: loconav-polygon-geofence-api
- description: The Trips API from LocoNav — 3 operation(s) for trips.
  name: LocoNav Trips API
  slug: loconav-trips-api
- description: The Users API from LocoNav — 1 operation(s) for users.
  name: LocoNav Users API
  slug: loconav-users-api
- description: <p>Loconav's Vehicle APIs offer developers a powerful toolkit for real-time fleet management. The Fetch Vehicle Details API provides comprehensive vehicle insights, while the Last Known Stats API deli
  name: LocoNav Vehicles API
  slug: loconav-vehicles-api
- description: <p>Thes APIs allows you to access telematics data for vehicles, enabling you to retrieve real-time information and history about their status, location, and various sensor readings.</p>
  name: LocoNav Vehicles / Telematics API
  slug: loconav-vehicles-telematics-api
- description: The Video Telematics VT / Live Stream API from LocoNav — 3 operation(s) for video telematics vt / live stream.
  name: LocoNav Video Telematics VT / Live Stream API
  slug: loconav-video-telematics-vt-live-stream-api
- description: The Video Telematics VT / Videos API from LocoNav — 2 operation(s) for video telematics vt / videos.
  name: LocoNav Video Telematics VT / Videos API
  slug: loconav-video-telematics-vt-videos-api
artifact_total: 31
asyncapis:
- description: AsyncAPI description of LocoNav alert and live-location webhooks derived from the published Postman webhook examples. LocoNav POSTs these events to a partner-registered receiver URL.
  name: LocoNav Webhooks
  slug: loconav-webhooks-asyncapi
- description: ''
  name: Loconav Webhooks
  slug: loconav-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LocoNav Integration Alert Subscriptions API
  slug: open-loconav-alert-subscriptions-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Alerts API
  slug: open-loconav-alerts-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Alerts Subscriptions API
  slug: open-loconav-alerts-subscriptions-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Drivers API
  slug: open-loconav-drivers-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Mobilization API
  slug: open-loconav-mobilization-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Polygon (Geofence) API
  slug: open-loconav-polygon-geofence-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Trips API
  slug: open-loconav-trips-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Users API
  slug: open-loconav-users-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Vehicles API
  slug: open-loconav-vehicles-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Vehicles / Telematics API
  slug: open-loconav-vehicles-telematics-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Video Telematics VT / Live Stream API
  slug: open-loconav-video-telematics-vt-live-stream-api
- collection_type: open
  name: LocoNav Integration Alert Subscriptions Video Telematics VT / Videos API
  slug: open-loconav-video-telematics-vt-videos-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/loconav-integration-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.loconav.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.loconav.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.loconav.com/
- group: company
  title: ''
  type: Website
  url: https://loconav.com/
- group: start
  title: ''
  type: SignUp
  url: https://loconav.com/contact-us
- group: operate
  title: ''
  type: Support
  url: https://loconav.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://loconav.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loconav.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loconav.com/privacypolicy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loconav-tech
- group: auth
  title: ''
  type: Compliance
  url: https://loconav.com/blog/loconav-gets-iso-27001-2013-certified/
- group: auth
  title: ''
  type: Authentication
  url: authentication/loconav-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loconav-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loconav-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loconav-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loconav-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loconav-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loconav-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: postman/loconav-postman-collection.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loconav-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/loconav-webhooks-asyncapi.yml
created: '2026-07-17'
description: 'LocoNav is an AI- and IoT-powered GPS vehicle tracking and smart fleet management platform used across 50+ countries, integrating 2,200+ device and sensor types to track vehicles and assets in real time. Its LocoNav Integration API exposes REST endpoints and webhooks for fleet telematics: telematics data (sensor readings, GPS location, distance, timelines, video and live streams), CRUD management of drivers, vehicles, trips, geofence polygons and users, driver-vehicle assignment, vehicle scorecards, immobilization, live share links, and alert subscriptions. Real-time alert and live-location webhooks push events such as overspeed, harsh braking/acceleration, geofence, fatigue, crash, fuel-theft, anti-theft and device-offline. Authentication is a user-level token in the User-Authentication header; all listing endpoints are paginated and time parameters use epoch seconds.'
image: https://loconav.com/marketing_pages/assets/images/loconav-logo.png
layout: provider
mcp_servers:
- description: ''
  name: loconav-mcp.yml
  slug: loconav-mcpyml
modified: '2026-07-20'
name: LocoNav
nav: Providers
network: true
overview: 'LocoNav publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Alert Subscriptions API, Alerts API, Alerts Subscriptions API, and 9 more. Tagged areas include Company, Fleet Management, Telematics, GPS Tracking, and Vehicle Tracking.


  The LocoNav catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  LocoNav''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Loconav Rate Limits
  slug: loconav-rate-limits
score:
  band: developing
  composite: 51.3
  delta: 1.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 66.7
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 31.6
  previous_composite: 50.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loconav/refs/heads/main/screenshots/loconav-2026-07-25T225438.png
security:
- kind: authentication
  name: Loconav Authentication
  slug: loconav-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loconav Domain Security
  slug: loconav-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: loconav
tags:
- Company
- Fleet Management
- Telematics
- GPS Tracking
- Vehicle Tracking
- Transportation
- Logistics
- IoT
- Video Telematics
- Webhooks
website: https://loconav.com/
---
