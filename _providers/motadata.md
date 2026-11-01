---
access_model:
  confidence: high
  label: Quote-based, sales-led; trial requested through a form
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/motadata-plans-pricing.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: ObserveOps (formerly Motadata AIOps) is a unified observability platform correlating metrics, logs, traces, flows and topology with anomaly detection that needs no training period. Its REST API is mou
  name: Motadata ObserveOps
  slug: observeops
- description: ServiceOps is Motadata's AI-powered, ITIL-aligned IT and enterprise service management suite. Its REST API lets third-party systems create, read, update and delete requests, problems, changes, release
  name: Motadata ServiceOps
  slug: serviceops
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.motadata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.motadata.com
- group: company
  title: ''
  type: Blog
  url: https://www.motadata.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.motadata.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.motadata.com/support-portal
- group: start
  title: ''
  type: SignUp
  url: https://www.motadata.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motadata.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motadata.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motadata
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/motadata2025
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/motadata
- group: agent
  href: https://artifacts.apis.io/motadata/llms/motadata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/motadata-llms.txt
- group: build
  href: https://artifacts.apis.io/motadata/packages/motadata-packages.yml
  title: ''
  type: Packages
  url: packages/motadata-packages.yml
- group: build
  href: https://artifacts.apis.io/motadata/packages/motadata-packages.yml
  title: ''
  type: SDKs
  url: packages/motadata-packages.yml
- group: agent
  href: https://artifacts.apis.io/motadata/mcp/motadata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/motadata-mcp.yml
- group: agent
  href: https://artifacts.apis.io/motadata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/motadata/cli/motadata-cli.yml
  title: ''
  type: CLI
  url: cli/motadata-cli.yml
- group: design
  href: https://artifacts.apis.io/motadata/components/motadata-components.yml
  title: ''
  type: Components
  url: components/motadata-components.yml
- group: auth
  href: https://artifacts.apis.io/motadata/authentication/motadata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/motadata-authentication.yml
- group: auth
  href: https://artifacts.apis.io/motadata/scopes/motadata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/motadata-scopes.yml
- group: design
  href: https://artifacts.apis.io/motadata/conventions/motadata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/motadata-conventions.yml
- group: design
  href: https://artifacts.apis.io/motadata/conformance/motadata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/motadata-conformance.yml
- group: design
  href: https://artifacts.apis.io/motadata/errors/motadata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/motadata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/motadata/data-model/motadata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/motadata-data-model.yml
- group: design
  href: https://artifacts.apis.io/motadata/lifecycle/motadata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/motadata-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/motadata/changelog/motadata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/motadata-changelog.yml
- group: operate
  href: https://artifacts.apis.io/motadata/rate-limits/motadata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/motadata-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/motadata/plans/motadata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/motadata-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/motadata/finops/motadata-finops.yml
  title: ''
  type: FinOps
  url: finops/motadata-finops.yml
- group: auth
  href: https://artifacts.apis.io/motadata/security/motadata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/motadata-domain-security.yml
created: '2026-03-27'
description: 'Motadata (Mindarray Systems) is a global IT software company running two AI-native platforms on a shared deep-learning foundation: ObserveOps, a unified observability and AIOps platform that brings metrics, logs, traces, flows and topology into one backend, and ServiceOps, an ITIL-aligned IT and enterprise service management suite covering service desk, CMDB, asset management, patch management and workflow automation. Both products are deployed in the customer''s own environment, so every API host, credential and rate limit belongs to the customer rather than to Motadata. ObserveOps exposes a REST API at /api/v1 across 96 configuration resource types plus a Vert.x EventBus websocket for live streams, and ships an official agent-first CLI that doubles as an MCP server with 22 tools and five packaged Agent Skills. ServiceOps exposes a documented REST API over OAuth 2.0 or an API key across request, problem, change, release, CMDB, asset and service-catalog objects. Motadata publishes
  no OpenAPI for either product.'
finops:
- has_sources: false
  method: generated
  name: Motadata Finops
  primary_unit: request
  service_category: API
  slug: motadata-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motadata.png
layout: provider
mcp_servers:
- description: Motadata ships an MCP server inside its official ObserveOps CLI. `observeops mcp` exposes the ObserveOps (AIOps) platform as typed MCP tools over stdio, holding one authenticated session for the whole
  name: Motadata MCP Server
  slug: observeops
modified: '2026-08-29'
name: Motadata
nav: Providers
network: true
overview: 'Motadata is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Monitoring, Observability, ITSM, and Service Desk.


  Motadata''s developer surface includes documentation, engineering blog, getting-started guide, support, signup flow, CLI, authentication, and 23 more developer resources.'
plans:
- name: Motadata Plans Pricing
  plan_count: 0
  slug: motadata-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Motadata Rate Limits
  slug: motadata-rate-limits
scopes:
- name: Motadata Scopes
  scope_count: 1
  slug: motadata-scopes
  summary_line: 1 scope · password
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 65.0
    operational_transparency: 42.1
  previous_composite: 37.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/motadata/motadata-2026-06-20T185837.png
security:
- kind: authentication
  name: Motadata Authentication
  slug: motadata-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Motadata Domain Security
  slug: motadata-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: observeops-cli
  slug: motadata-observeops-cli
- name: observeops-eventbus
  slug: motadata-observeops-eventbus
- name: observeops-resources
  slug: motadata-observeops-resources
- name: observeops-triage
  slug: motadata-observeops-triage
- name: observeops
  slug: motadata-observeops
slug: motadata
tags:
- AIOps
- Monitoring
- Observability
- ITSM
- Service Desk
- Network Monitoring
- Log Management
- IT Operations
- Application Performance Monitoring
- OpenTelemetry
website: https://www.motadata.com
---
