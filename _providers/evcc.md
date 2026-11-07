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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 72
  human_in_the_loop: 10
  name: Evcc Agentic Access
  operation_count: 88
  slug: evcc-agentic-access
  summary_line: 88 operations · 72 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The auth API from evcc (self-hosted) — 5 operation(s) for auth.
  name: evcc (self-hosted) Auth API
  slug: evcc-auth-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The battery API from evcc (self-hosted) — 12 operation(s) for battery.
  name: evcc (self-hosted) Battery API
  slug: evcc-battery-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The db API from evcc (self-hosted) — 5 operation(s) for db.
  name: evcc (self-hosted) Db API
  slug: evcc-db-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The experimental API from evcc (self-hosted) — 6 operation(s) for experimental.
  name: evcc (self-hosted) Experimental API
  slug: evcc-experimental-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The general API from evcc (self-hosted) — 9 operation(s) for general.
  name: evcc (self-hosted) General API
  slug: evcc-general-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The loadpoints API from evcc (self-hosted) — 29 operation(s) for loadpoints.
  name: evcc (self-hosted) Loadpoints API
  slug: evcc-loadpoints-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The sessions API from evcc (self-hosted) — 3 operation(s) for sessions.
  name: evcc (self-hosted) Sessions API
  slug: evcc-sessions-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The state API from evcc (self-hosted) — 1 operation(s) for state.
  name: evcc (self-hosted) State API
  slug: evcc-state-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The system API from evcc (self-hosted) — 5 operation(s) for system.
  name: evcc (self-hosted) System API
  slug: evcc-system-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The tariffs API from evcc (self-hosted) — 1 operation(s) for tariffs.
  name: evcc (self-hosted) Tariffs API
  slug: evcc-tariffs-api
- baseURL: https://demo.evcc.io/api
  baseurl_source: declared
  description: The vehicles API from evcc (self-hosted) — 10 operation(s) for vehicles.
  name: evcc (self-hosted) Vehicles API
  slug: evcc-vehicles-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/evcc/capabilities/evcc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/evcc-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/evcc/agentic-access/evcc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evcc-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/evcc/rules/evcc-rules.yml
  title: ''
  type: Spectral
  url: rules/evcc-rules.yml
- group: design
  href: https://artifacts.apis.io/evcc/json-ld/evcc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/evcc-context.jsonld
- group: design
  href: https://artifacts.apis.io/evcc/vocabulary/evcc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/evcc-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/evcc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/evcc/data-model/evcc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evcc-data-model.yml
- group: design
  href: https://artifacts.apis.io/evcc/components/evcc-components.yml
  title: ''
  type: Components
  url: components/evcc-components.yml
- group: auth
  href: https://artifacts.apis.io/evcc/authentication/evcc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evcc-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evcc.io/
- group: design
  href: https://artifacts.apis.io/evcc/lifecycle/evcc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evcc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/evcc/errors/evcc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evcc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/evcc/conformance/evcc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evcc-conformance.yml
- group: other
  href: https://artifacts.apis.io/evcc/overlays/evcc-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/evcc-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/evcc/llms/evcc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evcc-llms.txt
- group: other
  href: https://artifacts.apis.io/evcc/hosts/evcc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evcc-hosts.yml
- group: other
  href: https://artifacts.apis.io/evcc/vendors/evcc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evcc-vendors.yml
- group: build
  href: https://artifacts.apis.io/evcc/packages/evcc-packages.yml
  title: ''
  type: SDKs
  url: packages/evcc-packages.yml
- group: build
  href: https://artifacts.apis.io/evcc/packages/evcc-packages.yml
  title: ''
  type: Packages
  url: packages/evcc-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.evcc.io/de/features/plans
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.qrserver.com/v1/create-qr-code/?color=000000\&bgcolor=FFFFFF\&data=evcc%3A%2F%2Fserver%3Furl%3Dhttps%3A%2F%2Fdemo.evcc.io%26title%3DDemo%2520Server%26username%3Dadmin%26password%3Dsecret\&qzone=1\&margin=0\&size=150x150\&ecc=L
- group: auth
  href: https://artifacts.apis.io/evcc/security/evcc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evcc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evcc.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evcc.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evcc.io/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evcc.io/de/installation
- group: company
  title: ''
  type: Blog
  url: https://docs.evcc.io/de/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evcc-io
- group: operate
  title: ''
  type: Support
  url: https://github.com/evcc-io/evcc/issues
created: '2026-10-28'
description: evcc is an open-source, self-hosted smart charging solution for electric vehicles. It intelligently manages charging by coordinating wallboxes, heat pumps, home batteries, and solar surplus, supporting a wide range of manufacturers. Users retain full control and ownership of their data, with community-driven development and extensive integrations. A public demo API is available at https://demo.evcc.io/api, and comprehensive documentation is hosted at docs.evcc.io.
image: https://evcc.io/favicon.ico
json_schemas:
- name: ChargingSessions
  property_count: 0
  slug: evcc-charging-sessions
- name: Flow
  property_count: 5
  slug: evcc-flow
- name: GridSessions
  property_count: 0
  slug: evcc-grid-sessions
- name: OnboardingState
  property_count: 2
  slug: evcc-onboarding-state
- name: RepeatingPlan
  property_count: 5
  slug: evcc-repeating-plan
- name: State
  property_count: 88
  slug: evcc-state
jsonld:
- class_count: 75
  name: Evcc Context
  property_count: 313
  slug: evcc-context
layout: provider
modified: '2026-10-28'
name: evcc (self-hosted)
nav: Providers
network: true
overview: 'evcc (self-hosted) publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Battery API, Db API, and 8 more. Tagged areas include Company, Electric Vehicles, Smart Charging, Open Source, and Energy Management.


  The evcc (self-hosted) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  evcc (self-hosted)''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, engineering blog, support, and 22 more developer resources.'
plans:
- name: Evcc Plans Pricing
  plan_count: 0
  slug: evcc-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Evcc Rate Limits
  slug: evcc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: evcc (self-hosted) API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: evcc-rules
scopes:
- name: Evcc Scopes
  scope_count: 0
  slug: evcc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 48.1
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/evcc/evcc-2026-11-03T131649.png
security:
- kind: authentication
  name: Evcc Authentication
  slug: evcc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Evcc Domain Security
  slug: evcc-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: evcc-auth-flow
  slug: evcc-auth-flow
- name: get-state
  slug: evcc-get-state
slug: evcc
tags:
- Company
- Electric Vehicles
- Smart Charging
- Open Source
- Energy Management
- Home Automation
website: https://evcc.io/
---
