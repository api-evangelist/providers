---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 30
  human_in_the_loop: 9
  name: Leapfrog Power Agentic Access
  operation_count: 48
  slug: leapfrog-power-agentic-access
  summary_line: 48 operations · 30 acting · 9 human-in-the-loop
api_count: 8
apis:
- description: Create or update meters on the Leap platform individually or in bulk, accepting CSV or JSON input and returning a job ID, plus endpoints to list meter upload jobs, check job status and manage provisio
  name: Leap Create Meters API
  slug: leapfrog-power-create-meters-api
- description: Retrieve and search enrollment information for meters, including current enrollment status, participation preferences, associated programs and required actions, alongside idle period, disenrollment an
  name: Leap Meter Enrollment API
  slug: leapfrog-power-meter-enrollment-api
- description: Get and search meter details such as customer, utility, site and device information across a partner's meter inventory, with optional filtering by request parameters. OpenAPI 3.0.2.
  name: Leap Meter Details API
  slug: leapfrog-power-meter-details-api
- description: Suggest, retrieve and delete nomination suggestions for individual meters or in bulk for each applicable program and time period. Suggestions are reviewed by Leap before becoming actual market nominat
  name: Leap Meter Nomination API
  slug: leapfrog-power-nominations-api
- description: Receive and search grid dispatch instructions at meter and group level through Leap Dispatch API V2, including webhook URL management for meter and group dispatches. OpenAPI 3.0.3, served from the /v2
  name: Leap Dispatch API
  slug: leapfrog-power-dispatch-api
- description: List, create, update, delete and test webhooks that deliver Leap event notifications such as meter, connect and dispatch events to a partner receiver URL. OpenAPI 3.0.1.
  name: Leap Webhook Subscription API
  slug: leapfrog-power-webhooks-api
- description: Retrieve settlement and performance data — monthly revenue reports, annual revenue data, revenue report versions, event performance and unresponsive meter reporting — for a partner's enrolled fleet. O
  name: Leap Revenue and Analytics API
  slug: leapfrog-power-revenue-analytics-api
- description: 'Submit and monitor partner-supplied interval meter data — upload statuses, data validation errors, aggregated intervals and meter-level intervals — for meters where Leap does not receive utility data '
  name: Leap Interval Data Upload API
  slug: leapfrog-power-interval-data-upload-api
artifact_total: 13
asyncapis:
- description: API Evangelist DERIVED AsyncAPI rendering of Leap's published webhook surface. Leap does not publish an AsyncAPI document; this document was derived from the public event catalog and the published exa
  name: Leap Webhook Events
  slug: leapfrog-power-events-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leapfrog-power-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leapfrog-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leapfrog-power-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.leap.energy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.leap.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.leap.energy/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.leap.energy/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.leap.energy/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.leap.energy/docs/api-key-authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.leap.energy/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.leap.energy/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://partner.leap.energy/
- group: operate
  title: ''
  type: Support
  url: https://support.leap.energy/support/solutions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leap.energy/
- group: company
  title: ''
  type: Blog
  url: https://www.leap.energy/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leap.energy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leap.energy/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/leapfrog-power-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leapfrog-power-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leapfrog-power-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leapfrog-power-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/leapfrog-power-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leapfrog-power-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/leapfrog-power-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leapfrog-power-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.leap.energy/changelog/meters-api-v1-deprecation-date-set
- group: design
  title: ''
  type: Conventions
  url: conventions/leapfrog-power-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leapfrog-power-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/leapfrog-power-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/leapfrog-power-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leapfrog-power-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/leapfrog-power-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.leap.energy/reference/metercreated
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-create-meters-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-dispatch-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-interval-data-upload-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-meter-details-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-meter-enrollment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-nominations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-revenue-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/leapfrog-power-webhooks-overlay.yaml
created: '2026-07-27'
description: Leap (Leapfrog Power, Inc.) is a San Francisco based energy software company whose primary domain leap.ac 301-redirects to www.leap.energy. Leap sits in the private, unmandated layer of the United States energy stack — between distributed energy resources and the wholesale markets — letting technology brands build and scale virtual power plants without owning market access. Its software-only platform aggregates residential and commercial battery storage, smart thermostats, heat pumps, HVAC and EV charging, registers those assets into CAISO, NYISO, PJM and utility demand response programs, and settles the revenue back to the partner. Leap publishes a genuinely open developer portal at developer.leap.energy with eight anonymously downloadable OpenAPI definitions covering meter creation, enrollment and idle periods, meter details, market nominations, dispatch, webhooks, interval data upload and revenue and analytics. Its API posture is open documentation over a closed door — every
  specification and guide can be read without an account, but no key can be self-issued — keys are created only inside a Leap-provisioned partner account and prospective partners are told to contact an account manager or partners@leap.ac. No data-sharing mandate applies to Leap. It is not a utility, not a retailer and not a designated data holder anywhere; it is a downstream recipient of consumer data that California's investor-owned utilities are compelled to share, integrating PG&E, SCE and SDG&E through their Share My Data authorization flow. Leap's documentation never names Green Button, ESPI, OpenADR, IEEE 2030.5, OCPP or CIM. Consumer usage and settlement data are reachable through the API but only for a partner's own consented, enrolled meters, and Leap publishes no open grid or market data at all.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: leapfrog-power-mcp.yml
  slug: leapfrog-power-mcpyml
modified: '2026-07-27'
name: Leap
nav: Providers
network: true
overview: 'Leap publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Create Meters API, Meter Enrollment API, Meter Details API, and 5 more. Tagged areas include Energy, United States, Electricity, Grid, and Demand Response.


  The Leap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leap''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, signup flow, support, and 35 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 49.6
  delta: -3.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 69.5
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leapfrog-power/refs/heads/main/screenshots/leapfrog-power-2026-08-07T171518.png
security:
- kind: authentication
  name: Leapfrog Power Authentication
  slug: leapfrog-power-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Leapfrog Power Domain Security
  slug: leapfrog-power-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leapfrog-power
tags:
- Energy
- United States
- Electricity
- Grid
- Demand Response
- DER
- Virtual Power Plant
- Energy Markets
- Storage Flexibility
- EV Charging
- Smart Metering
website: https://www.leap.energy/
---
