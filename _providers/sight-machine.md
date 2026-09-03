---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: REST endpoint that returns the fully-resolved values behind a Sight Machine dashboard, panel by panel, so dashboard data can be consumed by external enterprise applications. Authenticated with a tenan
  name: Sight Machine Dashboard API
  slug: sight-machine-dashboard-api
- description: 'The /v1 datatab and selector surface of the Sight Machine Manufacturing Data Platform — cycles, downtime, parts, lines, raw data, machine types, machine schemas and KPI selectors. This is the surface '
  name: Sight Machine Platform Data API
  slug: sight-machine-platform-data-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sight Machine Event Surface
  slug: sight-machine-event-surface
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sight-machine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sightmachine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sightmachine.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sightmachine.com/docs/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sightmachine.com/docs/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sightmachine
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sightmachine.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sightmachine.com/software-and-services-agreement
- group: auth
  title: ''
  type: Security
  url: https://www.sightmachine.com/security
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/sight-machine
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sight-machine-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sight-machine-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sight-machine-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sight-machine-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sight-machine-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sight-machine-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sight-machine-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sight-machine-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sight-machine-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sight-machine-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sight-machine-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sight-machine-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sight-machine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sight-machine-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sight-machine-vulnerability-disclosure.yml
created: '2026-08-27'
description: Sight Machine is an industrial AI company (founded 2011, San Francisco and Ann Arbor) whose Manufacturing Data Platform connects to plant OT and IT systems — historians, MES, ERP, PLCs, OPC UA servers and MQTT brokers — and builds a semantic model of the factory that AI agents reason over. The platform is delivered as a per-customer tenant at {tenant}.sightmachine.io, and exposes its production data through a versioned /v1 REST surface (Dashboard API plus datatab/selector data endpoints), a first-party Python SDK (smsdk), and a PostgreSQL-wire ODBC/JDBC connector. Edge ingestion runs through FactoryTX, which speaks OPC UA, MQTT, SQL and file/cloud-store protocols. Authentication is by API key and secret headers issued per tenant; there is no public sandbox, no published pricing, and the API reference itself is served from inside the authenticated tenant environment.
layout: provider
modified: '2026-08-27'
name: Sight Machine
nav: Providers
network: true
overview: 'Sight Machine publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Industrial IoT, Analytics, Artificial Intelligence, and Agents.


  The Sight Machine catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sight Machine''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 20 more developer resources.'
plans:
- name: Sight Machine Plans Pricing
  plan_count: 0
  slug: sight-machine-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Sight Machine Rate Limits
  slug: sight-machine-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 37.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sight-machine/refs/heads/main/screenshots/sight-machine-2026-09-02T155420.png
security:
- kind: authentication
  name: Sight Machine Authentication
  slug: sight-machine-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sight Machine Domain Security
  slug: sight-machine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sight Machine Vulnerability Disclosure
  slug: sight-machine-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sight-machine
tags:
- Manufacturing
- Industrial IoT
- Analytics
- Artificial Intelligence
- Agents
- Data
- OPC UA
- MQTT
- Digital Twin
website: https://www.sightmachine.com/
---
