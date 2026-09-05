---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: Retrieve detailed information about ChargePoint charging stations, including location, address, GPS coordinates, power specifications, port counts, pricing, and station model details. Supports filteri
  name: ChargePoint Stations API
  slug: chargepoint-stations-api
- description: Query real-time status of ChargePoint charging station ports. Returns port availability states including AVAILABLE, INUSE, UNREACHABLE, and UNKNOWN with timestamps, enabling applications to display li
  name: ChargePoint Station Status API
  slug: chargepoint-station-status-api
- description: Monitor and control power load at ChargePoint charging stations. Retrieve current load in kilowatts, issue load shedding commands to limit station power by percentage or maximum load for a specified t
  name: ChargePoint Load Management API
  slug: chargepoint-load-management-api
- description: 'Access charging session data for ChargePoint stations, including energy consumed (kWh), session start and end timestamps, session identifiers, and driver information. Supports fleet and home charging '
  name: ChargePoint Charging Sessions API
  slug: chargepoint-charging-sessions-api
- description: Retrieve and manage alarms from ChargePoint charging stations. Returns alarm type, alarm timestamp, and station identifier for the most recent alarm condition. Supports clearing all active alarms on a
  name: ChargePoint Alarms API
  slug: chargepoint-alarms-api
- description: 'Manage and query ChargePoint station groups that organize charging infrastructure by location, fleet, or organizational unit. Retrieve group hierarchies, station rights profiles, and CPN (ChargePoint '
  name: ChargePoint Station Groups API
  slug: chargepoint-station-groups-api
- description: Manage electric vehicle fleet charging through ChargePoint's platform. Access vehicle registration, driver assignment, charging schedules, and fleet-level usage reporting. Integrates with fleet telema
  name: ChargePoint Fleet Management API
  slug: chargepoint-fleet-management-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/chargepoint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargepoint-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargepoint
- group: company
  title: ''
  type: Website
  url: https://www.chargepoint.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://na.chargepoint.com/terms_web
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chargepoint.com/download-file/chargepoint-api-services-terms-and-conditions-na
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chargepoint.com
- group: other
  title: ''
  type: WSDL
  url: https://webservices.chargepoint.com/cp_api_5.1.wsdl
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chargepoint.com/ref-docs-sec/content/pdfs/4-software/api/cp_api5.1.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://na.chargepoint.com/UI/s3docs/docs/help/SetupWebServicesAPI.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://chargepoint-fleet-telematics.statuspage.io/
- group: company
  title: ''
  type: Blog
  url: https://www.chargepoint.com/blog
- group: company
  title: ''
  type: Blog
  url: https://www.chargepoint.com/engineering/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chargepoint.com/businesses/software
- group: start
  title: ''
  type: Portal
  url: https://partner.chargepoint.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChargePoint
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/mbillow/python-chargepoint
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/chargepoint
- group: auth
  title: ''
  type: Authentication
  url: https://docs.chargepoint.com
- group: operate
  title: ''
  type: Support
  url: mailto:devsupport@chargepoint.com
created: '2026-06-13'
description: ChargePoint operates one of the world's largest EV charging networks, providing a Web Services API for finding stations, checking real-time availability, managing load, initiating and monitoring charging sessions, and accessing usage data for fleet and home charging deployments. The platform supports enterprise fleet electrification through open APIs and 40+ integrations.
features:
- SOAP/WSDL Web Services API v5.1 with WS-Security authentication
- Real-time station availability and status monitoring
- Load management and demand response (shed/clear load commands)
- Charging session data with energy usage and timestamps
- Station alarm monitoring and management
- Fleet management with vehicle and driver assignment
- Station group hierarchy for enterprise deployments
- Open Charge Point Protocol (OCPP) hardware compatibility
- 40+ turnkey integrations including building and energy management systems
- Fleet telematics integration and fuel card system connectivity
- Dynamic pricing controls by driver type, session length, and time-of-use
- 385,000+ activated ports across the ChargePoint network
finops:
- name: Chargepoint Finops
  service_category: Transportation / Energy Infrastructure
  slug: chargepoint-finops
image: https://www.chargepoint.com/themes/chargepoint/images/chargepoint-logo.svg
layout: provider
modified: '2026-06-13'
name: ChargePoint
nav: Providers
network: true
overview: 'ChargePoint publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include EV Charging, Electric Vehicles, Fleet Management, Energy Management, and Transportation.


  ChargePoint''s developer surface includes documentation, API reference, getting-started guide, engineering blog, developer portal, authentication, support, and 13 more developer resources.'
plans:
- name: Chargepoint Plans
  plan_count: 3
  slug: chargepoint-plans
random_paper: 17
rate_limits:
- limit_count: 1
  name: Chargepoint Rate Limits
  slug: chargepoint-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chargepoint/refs/heads/main/screenshots/chargepoint-2026-06-20T174221.png
security:
- kind: domain-security
  name: Chargepoint Domain Security
  slug: chargepoint-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Chargepoint Trust Center
  slug: chargepoint-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP
slug: chargepoint
tags:
- EV Charging
- Electric Vehicles
- Fleet Management
- Energy Management
- Transportation
website: https://www.chargepoint.com
---
