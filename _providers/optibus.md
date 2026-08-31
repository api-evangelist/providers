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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Optibus Agentic Access
  operation_count: 58
  slug: optibus-agentic-access
  summary_line: 58 operations · 18 acting
api_count: 1
apis:
- description: API endpoints for managing absences for drivers - i.e. periods where they are unavailable for work.
  name: Optibus Driver Absences API
  slug: optibus-driver-absences-api
- description: The Driver App Notifications API from Optibus — 1 operation(s) for driver app notifications.
  name: Optibus Driver App Notifications API
  slug: optibus-driver-app-notifications-api
- description: API endpoints for managing custom attributes for drivers - i.e. additional properties that can be set for drivers - including querying and updating their historical values.
  name: Optibus Driver Custom Attributes API
  slug: optibus-driver-custom-attributes-api
- description: API endpoints for managing employment periods for drivers - i.e. periods where they are employed, hired, terminated, etc.
  name: Optibus Driver Employment Periods API
  slug: optibus-driver-employment-periods-api
- description: API endpoints for managing driver groups.
  name: Optibus Driver Groups API
  slug: optibus-driver-groups-api
- description: API endpoints for fetching volunteering periods for drivers - i.e. periods where a driver is willing to volunteer for extra work, such as on a rest day or for overtime.
  name: Optibus Driver Volunteering Periods API
  slug: optibus-driver-volunteering-periods-api
- description: API endpoints for managing drivers.
  name: Optibus Drivers API
  slug: optibus-drivers-api
- description: These API endpoints are deprecated and could be removed in a future version. Please use the corresponding new API endpoints instead, which should offer improved usability and extra functionality.
  name: Optibus Drivers (Deprecated) API
  slug: optibus-drivers-deprecated-api
- description: The Event Webhooks API from Optibus — 1 operation(s) for event webhooks.
  name: Optibus Event Webhooks API
  slug: optibus-event-webhooks-api
- description: The Operational Plan API from Optibus — 3 operation(s) for operational plan.
  name: Optibus Operational Plan API
  slug: optibus-operational-plan-api
- description: These API endpoints are deprecated and could be removed in a future version. Please use GET /v2/operational-plan instead.
  name: Optibus Operational Plan (Deprecated) API
  slug: optibus-operational-plan-deprecated-api
- description: The Payroll API from Optibus — 1 operation(s) for payroll.
  name: Optibus Payroll API
  slug: optibus-payroll-api
- description: The Preferences API from Optibus — 2 operation(s) for preferences.
  name: Optibus Preferences API
  slug: optibus-preferences-api
- description: The Private Hires API from Optibus — 4 operation(s) for private hires.
  name: Optibus Private Hires API
  slug: optibus-private-hires-api
- description: The Regions API from Optibus — 1 operation(s) for regions.
  name: Optibus Regions API
  slug: optibus-regions-api
- description: A roster describes the daily operator runs grouped into packages of (repeating) weekly work assignments.
  name: Optibus Roster API
  slug: optibus-roster-api
- description: API endpoints for fetching sign-on/off times & deviations for drivers - i.e. the actual and expected sign-on and sign-off times for a driver and how much they deviate from each other.
  name: Optibus Signing Times API
  slug: optibus-signing-times-api
- description: API endpoints for fetching computed statistics over a date range - per-task duty statistics (mirroring the duty side panel in the Ops UI) and the calculation limits that bound a single request.
  name: Optibus Statistics API
  slug: optibus-statistics-api
- description: The Stops API from Optibus — 1 operation(s) for stops.
  name: Optibus Stops API
  slug: optibus-stops-api
- description: API endpoint for ingesting normalized Tachograph activity data from the Data Team.
  name: Optibus Tacho Ingestion API
  slug: optibus-tacho-ingestion-api
- description: The Tasks API from Optibus — 1 operation(s) for tasks.
  name: Optibus Tasks API
  slug: optibus-tasks-api
- description: API endpoints for managing custom attributes for vehicles - i.e. additional properties that can be set for vehicles - including querying and updating their historical values.
  name: Optibus Vehicle Custom Attributes API
  slug: optibus-vehicle-custom-attributes-api
- description: API endpoints for managing downtimes for vehicles - i.e. periods where they are unavailable for service.
  name: Optibus Vehicle Downtimes API
  slug: optibus-vehicle-downtimes-api
- description: API endpoints for managing vehicles.
  name: Optibus Vehicles API
  slug: optibus-vehicles-api
- description: These API endpoints are deprecated and could be removed in a future version. Please use the corresponding new API endpoints instead, which should offer improved usability and extra functionality.
  name: Optibus Vehicles (Deprecated) API
  slug: optibus-vehicles-deprecated-api
- description: The Work Entities API from Optibus — 2 operation(s) for work entities.
  name: Optibus Work Entities API
  slug: optibus-work-entities-api
artifact_total: 59
asyncapis:
- description: ''
  name: Optibus Operational Webhooks
  slug: optibus-operational-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Optibus Operations Driver Absences API
  slug: open-optibus-driver-absences-api
- collection_type: open
  name: Optibus Operations Driver Absences Driver App Notifications API
  slug: open-optibus-driver-app-notifications-api
- collection_type: open
  name: Optibus Operations Driver Absences Driver Custom Attributes API
  slug: open-optibus-driver-custom-attributes-api
- collection_type: open
  name: Optibus Operations Driver Absences Driver Employment Periods API
  slug: open-optibus-driver-employment-periods-api
- collection_type: open
  name: Optibus Operations Driver Absences Driver Groups API
  slug: open-optibus-driver-groups-api
- collection_type: open
  name: Optibus Operations Driver Absences Driver Volunteering Periods API
  slug: open-optibus-driver-volunteering-periods-api
- collection_type: open
  name: Optibus Operations Driver Absences Drivers API
  slug: open-optibus-drivers-api
- collection_type: open
  name: Optibus Operations Driver Absences Drivers (Deprecated) API
  slug: open-optibus-drivers-deprecated-api
- collection_type: open
  name: Optibus Operations Driver Absences Event Webhooks API
  slug: open-optibus-event-webhooks-api
- collection_type: open
  name: Optibus Operations Driver Absences Operational Plan API
  slug: open-optibus-operational-plan-api
- collection_type: open
  name: Optibus Operations Driver Absences Operational Plan (Deprecated) API
  slug: open-optibus-operational-plan-deprecated-api
- collection_type: open
  name: Optibus Operations Driver Absences Payroll API
  slug: open-optibus-payroll-api
- collection_type: open
  name: Optibus Operations Driver Absences Preferences API
  slug: open-optibus-preferences-api
- collection_type: open
  name: Optibus Operations Driver Absences Private Hires API
  slug: open-optibus-private-hires-api
- collection_type: open
  name: Optibus Operations Driver Absences Regions API
  slug: open-optibus-regions-api
- collection_type: open
  name: Optibus Operations Driver Absences Roster API
  slug: open-optibus-roster-api
- collection_type: open
  name: Optibus Operations Driver Absences Signing Times API
  slug: open-optibus-signing-times-api
- collection_type: open
  name: Optibus Operations Driver Absences Statistics API
  slug: open-optibus-statistics-api
- collection_type: open
  name: Optibus Operations Driver Absences Stops API
  slug: open-optibus-stops-api
- collection_type: open
  name: Optibus Operations Driver Absences Tacho Ingestion API
  slug: open-optibus-tacho-ingestion-api
- collection_type: open
  name: Optibus Operations Driver Absences Tasks API
  slug: open-optibus-tasks-api
- collection_type: open
  name: Optibus Operations Driver Absences Vehicle Custom Attributes API
  slug: open-optibus-vehicle-custom-attributes-api
- collection_type: open
  name: Optibus Operations Driver Absences Vehicle Downtimes API
  slug: open-optibus-vehicle-downtimes-api
- collection_type: open
  name: Optibus Operations Driver Absences Vehicles API
  slug: open-optibus-vehicles-api
- collection_type: open
  name: Optibus Operations Driver Absences Vehicles (Deprecated) API
  slug: open-optibus-vehicles-deprecated-api
- collection_type: open
  name: Optibus Operations Driver Absences Work Entities API
  slug: open-optibus-work-entities-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/optibus-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/optibus-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optibus-operations-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.ops.optibus.co/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.ops.optibus.co/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.ops.optibus.co/
- group: company
  title: ''
  type: Website
  url: https://www.optibus.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.optibus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Optibus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optibus.com/optibus-privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://optibus.com/contacts/
- group: auth
  title: ''
  type: Security
  url: https://optibus.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://optibus.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/optibus-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optibus-conformance.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optibus.co/
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.ops.optibus.co/#tag/Versioning
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optibus-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optibus-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optibus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optibus-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optibus-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optibus-operational-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optibus-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optibus-llms.txt
created: '2026-07-17'
description: Optibus is a cloud-native, end-to-end operating system for public transportation planning, scheduling, rostering and operations, used by transit agencies and operators in more than 3,000 cities. Its proprietary AI and optimization algorithms modernize network planning, vehicle and crew scheduling, driver rostering, fleet monitoring, payroll and depot management. The Optibus Operations API (OpenAPI 3.0.0, 58 operations) provides programmatic access to drivers, vehicles, absences, employment periods, operational plans, rosters, payroll and statistics, plus outbound HMAC-signed operational event webhooks, for integrating Optibus with external HR, payroll and fleet-management systems. Backed by Bessemer Venture Partners and Insight Partners.
image: https://optibus.com/file/2026/01/Thumbnail-HP.png
layout: provider
mcp_servers:
- description: ''
  name: Optibus MCP Server
  slug: optibus-mcp-server
modified: '2026-07-20'
name: Optibus
nav: Providers
network: true
overview: 'Optibus publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Driver Absences API, Driver App Notifications API, Driver Custom Attributes API, and 23 more. Tagged areas include Company, Vertical Software, Public Transportation, Transit, and Scheduling.


  The Optibus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Optibus'' developer surface includes documentation, API reference, engineering blog, support, changelog, authentication, and 20 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.1
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 56.6
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optibus/refs/heads/main/screenshots/optibus-2026-08-07T190805.png
security:
- kind: authentication
  name: Optibus Authentication
  slug: optibus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Optibus Domain Security
  slug: optibus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Optibus Trust Center
  slug: optibus-trust-center
  summary_line: ISO 27001:2022, SOC 2
slug: optibus
tags:
- Company
- Vertical Software
- Public Transportation
- Transit
- Scheduling
- Fleet Management
- Mobility
- Optimization
- Workforce Management
website: https://www.optibus.com/
---
