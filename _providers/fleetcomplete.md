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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: List and filter vehicles (getVehicles with VehicleFilter), fetch a vehicle by ID or VIN (getVehicleById, getVehiclesByVin), list active vehicles, read vehicle types and custom fields, inspect mapped s
  name: Fleet Complete Unity Vehicles API
  slug: fleetcomplete-unity-vehicles-api
- description: Manage the people and drivers in a fleet - list and filter people (getPeople with PersonFilter), fetch a person by ID, read custom fields, and look up driver-to-vehicle assignments (getDriverAssignmen
  name: Fleet Complete Unity Drivers & People API
  slug: fleetcomplete-unity-drivers-people-api
- description: Fetch a geofence by ID or list/filter geofences (getGeofenceById, getGeofences with GeofenceFilter), then create, update, or delete a geofence and move geofences between groups (changeGeofenceGroups).
  name: Fleet Complete Unity Geofences API
  slug: fleetcomplete-unity-geofences-api
- description: Look up telematics hardware by ID or serial (getDeviceById, getDevicesBySerial; the older getDeviceBySerial is documented as deprecated), and read or set in-cab dash-cam privacy mode (getCameraPrivacy
  name: Fleet Complete Unity Devices & Cameras API
  slug: fleetcomplete-unity-devices-cameras-api
- description: Read the organizational groups and roles used to segment vehicles, people, and geofences (getGroups, getRoles), and create, update, or delete groups (createGroup, updateGroup, deleteGroup).
  name: Fleet Complete Unity Groups & Roles API
  slug: fleetcomplete-unity-groups-roles-api
- description: Pull "wrapped" report data and its input options (getWrappedReport, getWrappedReportInputs), read work schedules by ID or in bulk (getWorkScheduleById, getWorkSchedules), read alert/compliance rules (
  name: Fleet Complete Unity Reports & Scheduling API
  slug: fleetcomplete-unity-reports-scheduling-api
- description: Older, regionally hosted OAuth REST surface predating the Unity GraphQL API, still referenced in Fleet Complete/Powerfleet support materials as the "FleetComplete WebAPI" (versioned v8_5_0/v8_6_1) and
  name: Fleet Complete Legacy Integration WebAPI
  slug: fleetcomplete-legacy-integration-webapi
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fleetcomplete-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetcomplete-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fleet-complete
- group: company
  title: ''
  type: Website
  url: https://www.fleetcomplete.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fleetcomplete.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/fleetcomplete-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fleetcomplete-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fleetcomplete-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.fleetcomplete.com/feed/
created: '2026-07-03'
description: Fleet Complete (operating under parent company Powerfleet since its 2024 rebrand) is a global connected commercial vehicle and mobile workforce management platform - GPS/telematics tracking, driver safety, dispatching, geofencing, and regulatory (HOS/ELD) compliance. Its current developer surface is the Unity API, a Bearer-token-authenticated GraphQL API at api.fleetcomplete.com/graphql covering vehicles, drivers/people, geofences, devices/cameras, groups/roles, and reports/work schedules with roughly 30 queries and 22 mutations. Fleet Complete also still references an older, regionally hosted REST "Integration WebAPI" / EcoFleet-SeeMe surface (versioned v8_5_0/v8_6_1) covering vehicle trip history, tasks/dispatch, work schedules, and logbook reporting. Standard API access is provided free to existing Fleet Complete/Powerfleet clients; custom integrations built by Fleet Complete Professional Services carry additional fees.
finops:
- name: Fleetcomplete Finops
  service_category: IoT / Fleet Management and Telematics
  slug: fleetcomplete-finops
graphqls:
- description: Fleet Complete's current developer surface is the Unity API - a single GraphQL
  name: Fleet Complete Unity GraphQL API
  slug: fleetcomplete-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fleetcomplete.png
layout: provider
modified: '2026-07-03'
name: Fleet Complete
nav: Providers
network: true
overview: 'Fleet Complete publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Telematics, GPS Tracking, IoT, and GraphQL.


  Fleet Complete''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Fleetcomplete Plans Pricing
  plan_count: 3
  slug: fleetcomplete-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Fleetcomplete Rate Limits
  slug: fleetcomplete-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleetcomplete/refs/heads/main/screenshots/fleetcomplete-2026-07-25T214736.png
security:
- kind: domain-security
  name: Fleetcomplete Domain Security
  slug: fleetcomplete-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fleetcomplete Vulnerability Disclosure
  slug: fleetcomplete-vulnerability-disclosure
  summary_line: disclosure policy published
slug: fleetcomplete
tags:
- Fleet Management
- Telematics
- GPS Tracking
- IoT
- GraphQL
- Vehicle Tracking
- Driver Safety
- Geofencing
website: https://www.fleetcomplete.com/
---
