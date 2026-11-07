---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ActionDock API provides endpoints for policy evaluation, human approvals, and secure execution of AI agent calls.
  name: ActionDock API
  slug: actiondock-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/actiondock-app/plans/actiondock-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actiondock-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/rules/actiondock-app-rules.yml
  title: ''
  type: Spectral
  url: rules/actiondock-app-rules.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/json-ld/actiondock-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/actiondock-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/actiondock-app/vocabulary/actiondock-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actiondock-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/actiondock-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/data-model/actiondock-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actiondock-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/conventions/actiondock-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/actiondock-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/conventions/actiondock-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/actiondock-app-conventions.yml
- group: start
  href: https://artifacts.apis.io/actiondock-app/sandbox/actiondock-app-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/actiondock-app-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://actiondock.app/security
- group: auth
  href: https://artifacts.apis.io/actiondock-app/authentication/actiondock-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actiondock-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/lifecycle/actiondock-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/actiondock-app-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/errors/actiondock-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/actiondock-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/actiondock-app/conformance/actiondock-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actiondock-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/actiondock-app/llms/actiondock-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actiondock-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/actiondock-app/mcp/actiondock-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/actiondock-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/actiondock-app/hosts/actiondock-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actiondock-app-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://actiondock.app/security
- group: start
  title: ''
  type: Sandbox
  url: https://actiondock.app/sandbox
- group: auth
  href: https://artifacts.apis.io/actiondock-app/security/actiondock-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/actiondock-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/actiondock-app/security/actiondock-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actiondock-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actiondock.app/
- group: docs
  title: ''
  type: Documentation
  url: https://actiondock.app/agents
- group: docs
  title: ''
  type: APIReference
  url: https://actiondock.app/agents
- group: start
  title: ''
  type: GettingStarted
  url: https://actiondock.app/agents
- group: operate
  title: ''
  type: Support
  url: https://actiondock.app/contact
- group: company
  title: ''
  type: Blog
  url: https://actiondock.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://actiondock.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actiondock.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actiondock.app/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://actiondock.app/incidents
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec is listed at https://actiondock.app/openapi.json but cannot be fetched without repeating a preflight probe.
  evidence:
  - status: 200
    url: https://actiondock.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: ActionDock provides a supervised API-write gateway that enables AI agents to make API calls only after deterministic policy evaluation, human owner approval, and secure server‑held credentials. It supports policy‑driven request previews, execution receipts, and integrates with existing REST APIs, offering fine‑grained controls over destination, method, path, network and payload. Designed for low‑to‑moderate volume changes, ActionDock ensures safe, auditable API writes for AI‑driven workflows.
image: https://actiondock.app/logo.png
jsonld:
- class_count: 22
  name: Actiondock App Context
  property_count: 88
  slug: actiondock-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at actiondock.app requiring an API key.
  name: actiondock-app MCP Server
  slug: actiondock-app-mcp-yml
modified: '2026-10-30'
name: actiondock-app
nav: Providers
network: true
overview: 'actiondock-app publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Gateways, and Human-in-the-Loop.


  The actiondock-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  actiondock-app''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Actiondock App Plans Pricing
  plan_count: 3
  slug: actiondock-app-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Actiondock App Rate Limits
  slug: actiondock-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: actiondock-app API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: actiondock-app-rules
scopes:
- name: Actiondock App Scopes
  scope_count: 0
  slug: actiondock-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 14.7
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/actiondock-app/actiondock-app-2026-11-03T120217.png
security:
- kind: authentication
  name: Actiondock App Authentication
  slug: actiondock-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Actiondock App Domain Security
  slug: actiondock-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Actiondock App Trust Center
  slug: actiondock-app-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: use-actiondock
  slug: actiondock-app-use-actiondock
slug: actiondock-app
tags:
- Company
- Artificial Intelligence
- MCP
- Gateways
- Human-in-the-Loop
website: https://actiondock.app/
---
