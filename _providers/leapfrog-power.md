---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 9
  name: Leapfrog Power Agentic Access
  operation_count: 48
  slug: leapfrog-power-agentic-access
  summary_line: 48 operations · 30 acting · 9 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The create meters API from Leap — 4 operation(s) for create meters.
  name: Leap create meters API
  slug: leapfrog-power-create-meters-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: Endpoints for group dispatches
  name: Leap Group Dispatches API
  slug: leapfrog-power-group-dispatches-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The interval_data_upload API from Leap — 6 operation(s) for interval_data_upload.
  name: Leap Interval Data Upload API
  slug: leapfrog-power-interval-data-upload-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The Meter Details API from Leap — 2 operation(s) for meter details.
  name: Leap Meter Details API
  slug: leapfrog-power-meter-details-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: Endpoints for meter dispatches
  name: Leap Meter Dispatches API
  slug: leapfrog-power-meter-dispatches-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The meter enrollment API from Leap — 2 operation(s) for meter enrollment.
  name: Leap meter enrollment API
  slug: leapfrog-power-meter-enrollment-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The nominations API from Leap — 5 operation(s) for nominations.
  name: Leap Nominations API
  slug: leapfrog-power-nominations-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The performance API from Leap — 1 operation(s) for performance.
  name: Leap Performance API
  slug: leapfrog-power-performance-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The provisional assets API from Leap — 2 operation(s) for provisional assets.
  name: Leap provisional assets API
  slug: leapfrog-power-provisional-assets-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The revenue API from Leap — 8 operation(s) for revenue.
  name: Leap Revenue API
  slug: leapfrog-power-revenue-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The webhooks API from Leap — 3 operation(s) for webhooks.
  name: Leap Webhooks API
  slug: leapfrog-power-webhooks-api
artifact_total: 23
asyncapis:
- description: API Evangelist DERIVED AsyncAPI rendering of Leap's published webhook surface. Leap does not publish an AsyncAPI document; this document was derived from the public event catalog and the published exa
  name: Leap Webhook Events
  slug: leapfrog-power-events-asyncapi
collections:
- collection_type: open
  name: Create Meters
  slug: open-leapfrog-power-create-meters
- collection_type: open
  name: Dispatch
  slug: open-leapfrog-power-dispatch
- collection_type: open
  name: Interval Data Upload
  slug: open-leapfrog-power-interval-data-upload
- collection_type: open
  name: Get meter detail
  slug: open-leapfrog-power-meter-details
- collection_type: open
  name: Meter Information API
  slug: open-leapfrog-power-meter-enrollment
- collection_type: open
  name: Meter Nomination API
  slug: open-leapfrog-power-nominations
- collection_type: open
  name: Revenue & Analytics
  slug: open-leapfrog-power-revenue-analytics
- collection_type: open
  name: Webhook Subscription API
  slug: open-leapfrog-power-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leapfrog-power-capability-edges.yml
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
  type: X-MCPServerCandidate
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
layout: provider
modified: '2026-07-27'
name: Leap
nav: Providers
network: true
overview: 'Leap publishes 11 APIs on the [APIs.io](https://apis.io/) network, including create meters API, Group Dispatches API, Interval Data Upload API, and 8 more. Tagged areas include Energy, United States, Electricity, Grid, and Demand Response.


  The Leap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leap''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, signup flow, support, and 36 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 68.4
    developer_ergonomics: 38.7
    discoverability: 77.8
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
