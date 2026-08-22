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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.1
  scored_at: '2026-08-19'
api_count: 10
apis:
- description: The create meters API from Leap — 4 operation(s) for create meters.
  name: Leap create meters API
  slug: leap-create-meters-api
- description: Endpoints for group dispatches
  name: Leap group-dispatches API
  slug: leap-group-dispatches-api
- description: The Meter Details API from Leap — 2 operation(s) for meter details.
  name: Leap Meter Details API
  slug: leap-meter-details-api
- description: Endpoints for meter dispatches
  name: Leap meter-dispatches API
  slug: leap-meter-dispatches-api
- description: The meter enrollment API from Leap — 2 operation(s) for meter enrollment.
  name: Leap meter enrollment API
  slug: leap-meter-enrollment-api
- description: The nominations API from Leap — 5 operation(s) for nominations.
  name: Leap nominations API
  slug: leap-nominations-api
- description: The performance API from Leap — 1 operation(s) for performance.
  name: Leap performance API
  slug: leap-performance-api
- description: The provisional assets API from Leap — 2 operation(s) for provisional assets.
  name: Leap provisional assets API
  slug: leap-provisional-assets-api
- description: The revenue API from Leap — 8 operation(s) for revenue.
  name: Leap revenue API
  slug: leap-revenue-api
- description: The webhooks API from Leap — 3 operation(s) for webhooks.
  name: Leap webhooks API
  slug: leap-webhooks-api
artifact_total: 25
asyncapis:
- description: Leap delivers two independent webhook surfaces to partner-hosted HTTPS receivers. 1. The general webhook platform — connect-session and meter/enrollment lifecycle events, with subscriptions managed th
  name: Leap Webhook Events
  slug: leap-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: create meters API
  slug: open-leap-create-meters-api
- collection_type: open
  name: create meters group-dispatches API
  slug: open-leap-group-dispatches-api
- collection_type: open
  name: create meters Meter Details API
  slug: open-leap-meter-details-api
- collection_type: open
  name: create meters meter-dispatches API
  slug: open-leap-meter-dispatches-api
- collection_type: open
  name: create meters meter enrollment API
  slug: open-leap-meter-enrollment-api
- collection_type: open
  name: create meters nominations API
  slug: open-leap-nominations-api
- collection_type: open
  name: create meters performance API
  slug: open-leap-performance-api
- collection_type: open
  name: create meters provisional assets API
  slug: open-leap-provisional-assets-api
- collection_type: open
  name: create meters revenue API
  slug: open-leap-revenue-api
- collection_type: open
  name: create meters webhooks API
  slug: open-leap-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leap-create-meters-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leap-domain-security.yml
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
- group: operate
  title: ''
  type: Support
  url: https://support.leap.energy/support/solutions
- group: company
  title: ''
  type: Blog
  url: https://www.leap.energy/blog
- group: start
  title: ''
  type: SignUp
  url: https://partner.leap.energy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leap.energy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leap.energy/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leap.energy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leap-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/leap-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leap-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leap-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/leap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leap-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/leap-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leap-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/leap-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leap-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leap-events-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/leap-events-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leap-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leap-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/leap-packages.yml
- group: design
  title: ''
  type: Components
  url: components/leap-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leap-onboard-meters.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leap-process-dispatch.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leap-subscribe-webhooks.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leap-revenue-reporting.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/leap-manage-nominations.md
created: '2026-07-17'
description: Leap is a San Francisco-based energy software company that lets technology brands build and scale virtual power plants (VPPs). Its platform aggregates distributed energy resources — residential and commercial battery storage, smart thermostats and heat pumps, and EV charging — and gives them a single point of integration into wholesale electricity markets and utility grid-service programs across CAISO, NYISO and other regions. Leap exposes a universal REST API covering meter onboarding and bulk creation, utility data authorization (Leap Connect), enrollment and participation management, market nominations and bidding, real-time dispatch delivery over webhooks or polling, event performance and interval data, and revenue settlement reporting. Partners authenticate with environment-scoped bearer API keys against separate staging and production hosts, and Leap publishes OpenAPI definitions, a dated changelog, an llms.txt index and a public status page.
image: https://www.leap.energy/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: leap-mcp.yml
  slug: leap-mcpyml
modified: '2026-07-19'
name: Leap
nav: Providers
network: true
overview: 'Leap publishes 10 APIs on the [APIs.io](https://apis.io/) network, including create meters API, group-dispatches API, Meter Details API, and 7 more. Tagged areas include Company, Energy, Electricity, Virtual Power Plant, and Demand Response.


  The Leap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leap''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 29 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 47.3
  delta: -3.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 71.1
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 50.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leap/refs/heads/main/screenshots/leap-2026-07-25T224743.png
security:
- kind: authentication
  name: Leap Authentication
  slug: leap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leap Domain Security
  slug: leap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leap
tags:
- Company
- Energy
- Electricity
- Virtual Power Plant
- Demand Response
- Distributed Energy Resources
- Grid Services
- Energy Markets
- Battery Storage
- EV Charging
- Smart Buildings
- Metering
- Webhooks
- Climate Tech
website: https://www.leap.energy/
---
