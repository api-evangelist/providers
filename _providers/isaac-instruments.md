---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 8
apis:
- description: 'Modeled interface for retrieving fleet vehicles and tractor/trailer assets configured on the ISAAC platform, including identifiers, VIN, and unit metadata used to correlate telematics data. Endpoints '
  name: ISAAC Vehicles API
  slug: isaac-instruments-vehicles-api
- description: Modeled interface for retrieving drivers and their profile, licensing, and assignment details as managed on the ISAAC platform. Endpoints are documented in ISAAC's partner API Guide and provisioned to
  name: ISAAC Drivers API
  slug: isaac-instruments-drivers-api
- description: Exports drivers' hours-of-service information captured by ISAAC's ELD - time spent in each duty status and distance traveled - for compliance, payroll, and TMS workflows. This capability is explicitly
  name: ISAAC Hours of Service (ELD) API
  slug: isaac-instruments-hours-of-service-api
- description: Modeled interface for GPS positions and location breadcrumbs used by visibility and tracking partners integrating with ISAAC telematics. Endpoints are documented in ISAAC's partner API Guide and provi
  name: ISAAC Positions API
  slug: isaac-instruments-positions-api
- description: Modeled interface for trips, stops, and route/dispatch data flowing between ISAAC and TMS/dispatch partners. Endpoints are documented in ISAAC's partner API Guide and provisioned to approved partners;
  name: ISAAC Trips API
  slug: isaac-instruments-trips-api
- description: Modeled interface for driver-to-dispatch messaging and in-cab workflow forms exchanged through the ISAAC platform. Endpoints are documented in ISAAC's partner API Guide and provisioned to approved par
  name: ISAAC Messaging API
  slug: isaac-instruments-messaging-api
- description: 'Modeled interface for fuel consumption, idling, and driving-performance metrics used by fuel-tax (IFTA) and coaching partners. Endpoints are documented in ISAAC''s partner API Guide and provisioned to '
  name: ISAAC Fuel and Performance API
  slug: isaac-instruments-fuel-api
- description: Modeled interface for vehicle and safety events (fault/diagnostic codes, safety-critical events) surfaced to safety/compliance and maintenance partners. Endpoints are documented in ISAAC's partner API
  name: ISAAC Events API
  slug: isaac-instruments-events-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/isaac-instruments-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/isaac-instruments
- group: company
  title: ''
  type: Website
  url: https://www.isaacinstruments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.isaacinstruments.com/platform/seamless-integration/open-platform/
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.isaacinstruments.com/platform/seamless-integration/open-platform/join-isaac-become-a-partner/
- group: commercial
  title: ''
  type: Plans
  url: https://www2.isaacinstruments.com/request-a-price
created: '2026-07-04'
description: ISAAC Instruments is a Canadian provider of in-cab technology and fleet management for the trucking industry - electronic logging devices (ELD), telematics, hours-of-service (HOS) compliance, driver workflow, messaging, and fuel/performance analytics, delivered as a fully managed hardware-plus-software platform. ISAAC runs an "Open Platform" with a documented API that lets fleets and 80+ integration partners (TMS/dispatch, maintenance, fuel tax, visibility, safety/compliance) share ISAAC data with their chosen vendors. API access is partner-gated - vendors apply through the ISAAC partner program and the full API Guide and reference live behind the ISAAC InRealTime portal and Client Center rather than on a public developer site. The API surface documented here is modeled from ISAAC's public platform and partner materials; exact endpoints, base URLs, and authentication are provisioned to approved partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/isaac-instruments.png
layout: provider
modified: '2026-07-04'
name: ISAAC Instruments
nav: Providers
network: true
overview: 'ISAAC Instruments publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Trucking, Telematics, ELD, Fleet Management, and Hours of Service.


  ISAAC Instruments'' developer surface includes documentation and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/isaac-instruments/refs/heads/main/screenshots/isaac-instruments-2026-07-25T222933.png
security:
- kind: domain-security
  name: Isaac Instruments Domain Security
  slug: isaac-instruments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: isaac-instruments
tags:
- Trucking
- Telematics
- ELD
- Fleet Management
- Hours of Service
- Compliance
- Transportation
- Partner API
website: https://www.isaacinstruments.com/
---
