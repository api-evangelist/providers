---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Skydio Agentic Access
  operation_count: 3
  slug: skydio-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: The Skydio Cloud API is an HTTP-based REST API with JSON request and response bodies that lets developers manage Skydio drone fleets programmatically. It covers vehicles, docks, controllers, batteries
  name: Skydio Cloud API
  slug: skydio-cloud-api
- description: Real-time command and control interface for the Skydio X10D using MAVLink/RAS-A, enabling integration with ground control stations and third-party autonomy stacks. Access is gated through Skydio Suppo
  name: Skydio Control & Telemetry ICD
  slug: skydio-control-telemetry-icd
- description: Android Intent API for the X10D Controller that lets third-party Android applications running on the controller receive information from the Skydio flight stack.
  name: Skydio Android Intent API
  slug: skydio-android-intent-api
- description: Mechanical, electrical, and power interface specification for building custom attachments and payloads for the Skydio X10 and X10D platforms. Access requires a request through Skydio.
  name: Skydio Attachment ICD
  slug: skydio-attachment-icd
- description: Retrieve flights and flight metadata.
  name: Skydio Flights API
  slug: skydio-flights-api
- description: Create or update markers (incidents).
  name: Skydio Markers API
  slug: skydio-markers-api
- description: Manage vehicles in your Skydio Cloud organization.
  name: Skydio Vehicles API
  slug: skydio-vehicles-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Skydio Cloud Flights API
  slug: open-skydio-flights-api
- collection_type: open
  name: Skydio Cloud Flights Markers API
  slug: open-skydio-markers-api
- collection_type: open
  name: Skydio Cloud Flights Vehicles API
  slug: open-skydio-vehicles-api
- collection_type: open
  name: Skydio Cloud API
  slug: open-skydio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skydio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skydio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skydio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.skydio.com/
- group: start
  title: ''
  type: Portal
  url: https://apidocs.skydio.com/
- group: build
  title: ''
  type: DeveloperTools
  url: https://www.skydio.com/developer-tools
- group: build
  title: ''
  type: IntegrationsCatalog
  url: https://www.skydio.com/integrations-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.skydio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.skydio.com/reference/introduction
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.skydio.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.skydio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.skydio.com/platform/reliability-dashboard
- group: learn
  title: ''
  type: Training
  url: https://www.skydio.com/skydio-academy
- group: company
  title: ''
  type: Blog
  url: https://www.skydio.com/blog
- group: start
  title: ''
  type: Login
  url: https://cloud.skydio.com/
- group: company
  title: ''
  type: Careers
  url: https://www.skydio.com/careers
- group: operate
  title: ''
  type: ContactSales
  url: https://www.skydio.com/contact-sales
created: '2026-05-23'
description: Skydio is a U.S. manufacturer of autonomous drones for public safety, defense, and enterprise customers, building self-flying aircraft such as the X10, X10D, X2, and S2+ along with the Skydio Cloud platform for fleet management, mission planning, live telemetry, and media sync. Skydio exposes a public REST API through Skydio Cloud (apidocs.skydio.com) for managing vehicles, docks, flights, missions, media, alerts, webhooks, and users, alongside on-vehicle integration interfaces such as the Control & Telemetry ICD, Android Intent API, and Attachment ICD for partners and developers.
finops:
- name: Skydio Finops
  service_category: API
  slug: skydio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skydio.png
layout: provider
modified: '2026-05-23'
name: Skydio
nav: Providers
network: true
overview: 'Skydio publishes 3 APIs on the [APIs.io](https://apis.io/) network: Flights API, Markers API, and Vehicles API. Tagged areas include Autonomous Systems, Defense, Drones, Enterprise, and Fleet Management.


  Skydio''s developer surface includes authentication, developer portal, documentation, API reference, changelog, support, training material, and 10 more developer resources.'
plans:
- name: Skydio Plans Pricing
  plan_count: 1
  slug: skydio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Skydio Rate Limits
  slug: skydio-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 42.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skydio/refs/heads/main/screenshots/skydio-2026-06-20T194013.png
security:
- kind: authentication
  name: Skydio Authentication
  slug: skydio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skydio Domain Security
  slug: skydio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skydio
tags:
- Autonomous Systems
- Defense
- Drones
- Enterprise
- Fleet Management
- Public Safety
- Robotics
- Unmanned Aerial Vehicles
website: https://www.skydio.com/
---
