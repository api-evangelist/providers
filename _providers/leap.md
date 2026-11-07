---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
api_count: 10
apis:
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The create meters API from Leap — 4 operation(s) for create meters.
  name: Leap create meters API
  slug: leap-create-meters-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: Endpoints for group dispatches
  name: Leap Group Dispatches API
  slug: leap-group-dispatches-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The Meter Details API from Leap — 2 operation(s) for meter details.
  name: Leap Meter Details API
  slug: leap-meter-details-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: Endpoints for meter dispatches
  name: Leap Meter Dispatches API
  slug: leap-meter-dispatches-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The meter enrollment API from Leap — 2 operation(s) for meter enrollment.
  name: Leap meter enrollment API
  slug: leap-meter-enrollment-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The nominations API from Leap — 5 operation(s) for nominations.
  name: Leap Nominations API
  slug: leap-nominations-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The performance API from Leap — 1 operation(s) for performance.
  name: Leap Performance API
  slug: leap-performance-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The provisional assets API from Leap — 2 operation(s) for provisional assets.
  name: Leap provisional assets API
  slug: leap-provisional-assets-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The revenue API from Leap — 8 operation(s) for revenue.
  name: Leap Revenue API
  slug: leap-revenue-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The webhooks API from Leap — 3 operation(s) for webhooks.
  name: Leap Webhooks API
  slug: leap-webhooks-api
- baseURL: https://api.leap.energy
  baseurl_source: declared
  description: The interval_data_upload API from Leap — 6 operation(s) for interval_data_upload.
  name: Leap Interval Data Upload API
  slug: leap-interval-data-upload-api
artifact_total: 30
asyncapis:
- description: Leap delivers two independent webhook surfaces to partner-hosted HTTPS receivers. 1. The general webhook platform — connect-session and meter/enrollment lifecycle events, with subscriptions managed th
  name: Leap Webhook Events
  slug: leap-events-asyncapi
collections:
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
  href: https://artifacts.apis.io/leap/capabilities/leap-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leap-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/leap/overlays/leap-create-meters-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leap-create-meters-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/leap/security/leap-domain-security.yml
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
  href: https://artifacts.apis.io/leap/changelog/leap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leap-changelog.yml
- group: operate
  href: https://artifacts.apis.io/leap/lifecycle/leap-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/leap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/leap/lifecycle/leap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leap-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/leap/llms/leap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leap-llms.txt
- group: auth
  href: https://artifacts.apis.io/leap/authentication/leap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leap-authentication.yml
- group: design
  href: https://artifacts.apis.io/leap/conventions/leap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leap-conventions.yml
- group: design
  href: https://artifacts.apis.io/leap/errors/leap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leap-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leap/errors/leap-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/leap-error-codes.yml
- group: design
  href: https://artifacts.apis.io/leap/conformance/leap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leap-conformance.yml
- group: start
  href: https://artifacts.apis.io/leap/sandbox/leap-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/leap-sandbox.yml
- group: design
  href: https://artifacts.apis.io/leap/data-model/leap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leap-data-model.yml
- group: design
  href: https://artifacts.apis.io/leap/asyncapi/leap-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/leap-events-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/leap/asyncapi/leap-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/leap-events-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/leap/mcp/leap-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/leap-mcp.yml
- group: agent
  href: https://artifacts.apis.io/leap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/leap/well-known/leap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leap-well-known.yml
- group: build
  href: https://artifacts.apis.io/leap/packages/leap-packages.yml
  title: ''
  type: Packages
  url: packages/leap-packages.yml
- group: design
  href: https://artifacts.apis.io/leap/components/leap-components.yml
  title: ''
  type: Components
  url: components/leap-components.yml
- group: agent
  href: https://artifacts.apis.io/leap/skills/leap-onboard-meters.md
  title: ''
  type: AgentSkill
  url: skills/leap-onboard-meters.md
- group: agent
  href: https://artifacts.apis.io/leap/skills/leap-process-dispatch.md
  title: ''
  type: AgentSkill
  url: skills/leap-process-dispatch.md
- group: agent
  href: https://artifacts.apis.io/leap/skills/leap-subscribe-webhooks.md
  title: ''
  type: AgentSkill
  url: skills/leap-subscribe-webhooks.md
- group: agent
  href: https://artifacts.apis.io/leap/skills/leap-revenue-reporting.md
  title: ''
  type: AgentSkill
  url: skills/leap-revenue-reporting.md
- group: agent
  href: https://artifacts.apis.io/leap/skills/leap-manage-nominations.md
  title: ''
  type: AgentSkill
  url: skills/leap-manage-nominations.md
created: '2026-07-17'
description: Leap is a San Francisco-based energy software company that lets technology brands build and scale virtual power plants (VPPs). Its platform aggregates distributed energy resources — residential and commercial battery storage, smart thermostats and heat pumps, and EV charging — and gives them a single point of integration into wholesale electricity markets and utility grid-service programs across CAISO, NYISO and other regions. Leap exposes a universal REST API covering meter onboarding and bulk creation, utility data authorization (Leap Connect), enrollment and participation management, market nominations and bidding, real-time dispatch delivery over webhooks or polling, event performance and interval data, and revenue settlement reporting. Partners authenticate with environment-scoped bearer API keys against separate staging and production hosts, and Leap publishes OpenAPI definitions, a dated changelog, an llms.txt index and a public status page.
image: https://www.leap.energy/favicon.ico
layout: provider
modified: '2026-07-19'
name: Leap
nav: Providers
network: true
overview: 'Leap publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including create meters API, Group Dispatches API, Meter Details API, and 8 more. Tagged areas include Company, Energy, Electricity, Virtual Power Plant, and Demand Response.


  The Leap catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Leap''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 30 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Leap API Rules
  rule_count: 65
  severity_counts:
    error: 53
    hint: 0
    info: 3
    warn: 9
  slug: leap-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 65.5
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.3
  provenance:
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
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/leap/leap-2026-07-25T224743.png
security:
- kind: authentication
  name: Leap Authentication
  slug: leap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leap Domain Security
  slug: leap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: leap-manage-nominations
  slug: leap-manage-nominations
- name: leap-onboard-meters
  slug: leap-onboard-meters
- name: leap-process-dispatch
  slug: leap-process-dispatch
- name: leap-revenue-reporting
  slug: leap-revenue-reporting
- name: leap-subscribe-webhooks
  slug: leap-subscribe-webhooks
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
- Webhook
- Climate Tech
website: https://www.leap.energy/
---
