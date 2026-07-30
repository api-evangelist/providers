---
access_model:
  confidence: high
  label: Paid · Partner-only onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Virtual Peaker Agentic Access
  operation_count: 23
  slug: virtual-peaker-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 2
apis:
- description: The Device Partner half of Virtual Peaker's Gravity Connect specification — the endpoints a device OEM must implement so a VPP or DERMS platform can discover, enroll, read, group, and command its behi
  name: Gravity Connect API (Device Partner)
  slug: gravity-connect-device-partner-api
- description: The VPP half of the Gravity Connect specification — the publishing endpoints Virtual Peaker hosts so an integrated device partner can stream device signals, settings, command status, and enrollment ev
  name: Gravity Connect API (Virtual Peaker)
  slug: gravity-connect-vpp-api
artifact_total: 8
asyncapis:
- description: ''
  name: Virtual Peaker Gravity Connect Webhooks
  slug: virtual-peaker-gravity-connect-webhooks
collections:
- collection_type: postman
  name: Gravity Connect API
  slug: postman-virtual-peaker-gravity-connect-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virtual-peaker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtual-peaker-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virtual-peaker-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtual-peaker-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://virtual-peaker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://virtual-peaker.com/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://assets.virtualpeaker.io/gravity-connect/device-partner-api.html
- group: company
  title: ''
  type: Blog
  url: https://virtual-peaker.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://virtual-peaker.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.virtual-peaker.com/knowledge
- group: operate
  title: ''
  type: SupportCenter
  url: https://support.virtual-peaker.com/knowledge
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtual-peaker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virtual-peaker/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtual-peaker.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtual-peaker.com/terms-of-use/
- group: operate
  title: ''
  type: ContactForm
  url: https://virtual-peaker.com/company/contact/
- group: start
  title: ''
  type: PartnerPortal
  url: https://virtual-peaker.com/partners/device-partners/
- group: start
  title: ''
  type: GettingStarted
  url: https://assets.virtualpeaker.io/gravity-connect/device-partner-api.html#section/Getting-Started
- group: start
  title: ''
  type: Login
  url: https://utility.virtualpeaker.io/
- group: build
  title: ''
  type: Postman
  url: https://assets.virtualpeaker.io/gravity-connect/Gravity%20Connect%20API.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://virtual-peaker.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtual-peaker-llms.txt
- group: agent
  title: ''
  type: llmsTxt
  url: https://virtual-peaker.com/llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/virtual-peaker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtual-peaker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtual-peaker-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtual-peaker-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtual-peaker-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtual-peaker-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/virtual-peaker-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virtual-peaker-gravity-connect-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/virtual-peaker-packages.yml
created: '2026-07-27'
description: 'Virtual Peaker is a Louisville, Kentucky software company selling grid-edge DERMS and virtual power plant software to United States and Canadian electric utilities — investor-owned utilities, municipal utilities, and rural electric cooperatives. Its platform is sold as three suites: Shift (grid-edge DERMS device control and demand response event dispatch), Relay (customer engagement, enrollment, and incentive processing), and Envision (demand forecasting). Virtual Peaker sits in the private DER-orchestration layer of the energy value chain, between device OEMs behind the meter and the utility back office — it is a vendor, not a utility, not a retailer, and not a data holder, so no consumer energy data right attaches to it. There is no Green Button / ESPI implementation here, no Consumer Data Right obligation, and no open market or grid data of any kind. What it does publish is its own API specification: Gravity Connect, an OpenAPI 3.0.0 contract (v2.0.6) that Virtual Peaker
  authored and openly published as a vendor-agnostic alternative to OpenADR and IEEE 2030.5 for onboarding and controlling DER devices. Gravity Connect is two-sided — the device OEM implements one half, the VPP platform implements the other — and both halves are readable anonymously as full Redoc API references. The honest posture: a real, downloadable, standards-ambitious API contract that is effectively undiscoverable (it is linked from nowhere on the marketing site) and whose credentials are partner-only, issued per utility program by emailing the Gravity Connect team. The commercial Shift API is named and sold on the marketing site but has no public documentation at all.'
image: https://assets.virtualpeaker.io/gravity-connect/assets/vp_logo.png
layout: provider
modified: '2026-07-27'
name: Virtual Peaker
nav: Providers
network: true
overview: 'Virtual Peaker publishes 2 APIs on the [APIs.io](https://apis.io/) network: Gravity Connect API (Device Partner) and Gravity Connect API (Virtual Peaker). Tagged areas include Energy, United States, Utilities, Electricity, and Grid.


  The Virtual Peaker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virtual Peaker''s developer surface includes authentication, documentation, API reference, engineering blog, support, getting-started guide, changelog, and 26 more developer resources.'
random_paper: 58
scopes:
- name: Virtual Peaker Scopes
  scope_count: 3
  slug: virtual-peaker-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 50.1
  delta: 4.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.6
    developer_ergonomics: 56.0
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 74.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Virtual Peaker Authentication
  slug: virtual-peaker-authentication
  summary_line: oauth2/hmac · 3 schemes
- kind: domain-security
  name: Virtual Peaker Domain Security
  slug: virtual-peaker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtual-peaker
tags:
- Energy
- United States
- Utilities
- Electricity
- Grid
- Demand Response
- DER
- DERMS
- Virtual Power Plant
- EV Charging
- Smart Thermostats
- Energy Storage
website: https://virtual-peaker.com/
---
