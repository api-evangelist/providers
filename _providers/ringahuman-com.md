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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Reference for create_call_task / POST /api/tasks: every field, validation and response.'
  name: Ring a Human REST API
  slug: ring-a-human-rest-api
- baseURL: https://api.ringahuman.com
  baseurl_source: declared
  description: 'ringahuman-com API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: ringahuman-com API
  slug: ringahuman-com-api
artifact_total: 18
common:
- group: operate
  href: https://artifacts.apis.io/ringahuman-com/rate-limits/ringahuman-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ringahuman-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ringahuman-com/plans/ringahuman-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ringahuman-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ringahuman-com/rules/ringahuman-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ringahuman-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ringahuman-com/json-ld/ringahuman-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ringahuman-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ringahuman-com/vocabulary/ringahuman-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ringahuman-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ringahuman-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ringahuman-com/data-model/ringahuman-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ringahuman-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/ringahuman-com/sandbox/ringahuman-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ringahuman-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/ringahuman-com/authentication/ringahuman-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ringahuman-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ringahuman-com/scopes/ringahuman-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ringahuman-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/ringahuman-com/errors/ringahuman-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ringahuman-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ringahuman-com/conformance/ringahuman-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ringahuman-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ringahuman-com/llms/ringahuman-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ringahuman-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ringahuman-com/mcp/ringahuman-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ringahuman-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ringahuman-com/well-known/ringahuman-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ringahuman-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ringahuman-com/hosts/ringahuman-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ringahuman-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ringahuman-com/vendors/ringahuman-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ringahuman-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ringahuman-com/security/ringahuman-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ringahuman-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ringahuman.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ringahuman.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ringahuman.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ringahuman.com/docs/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://ringahuman.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://ringahuman.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ringahuman.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ringahuman.com/privacy/
coverage:
  checked: '2026-10-31'
  detail: Documentation provides API reference but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://ringahuman.com/docs/create-call-task/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Ring a Human provides an API that enables AI agents to place vetted phone calls to leads within minutes, respecting calling hours, do‑not‑call regulations, and consent rules. The service returns call outcomes back to the agent, supporting integration via an MCP server, REST API, and a ChatGPT app. This platform helps businesses automate lead outreach while ensuring compliance and delivering real‑time results.
image: https://ringahuman.com/assets/brand/logo.svg
json_schemas:
- name: GetApiBillingResponse
  property_count: 4
  slug: ringahuman-com-get-api-billing-response
- name: GetApiSandboxTasksIdResponse
  property_count: 4
  slug: ringahuman-com-get-api-sandbox-tasks-id-response
- name: PostApiHooksRequest
  property_count: 2
  slug: ringahuman-com-post-api-hooks-request
- name: PostApiIntakeRahInRequest
  property_count: 5
  slug: ringahuman-com-post-api-intake-rah-in-request
- name: PostApiSandboxTasksRequest
  property_count: 6
  slug: ringahuman-com-post-api-sandbox-tasks-request
- name: PostApiTasksRequest
  property_count: 8
  slug: ringahuman-com-post-api-tasks-request
jsonld:
- class_count: 19
  name: Ringahuman Com Context
  property_count: 31
  slug: ringahuman-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ringahuman.com requiring OAuth.
  name: ringahuman-com MCP Server
  slug: ringahuman-com-mcp-yml
modified: '2026-10-31'
name: ringahuman-com
nav: Providers
network: true
overview: 'ringahuman-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Telephony, Lead Generation, and Compliance.


  The ringahuman-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ringahuman-com''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Ringahuman Com Plans Pricing
  plan_count: 1
  slug: ringahuman-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Ringahuman Com Rate Limits
  slug: ringahuman-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ringahuman-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ringahuman-com-rules
scopes:
- name: Ringahuman Com Scopes
  scope_count: 1
  slug: ringahuman-com-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 46.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ringahuman-com/ringahuman-com-2026-11-03T142308.png
security:
- kind: authentication
  name: Ringahuman Com Authentication
  slug: ringahuman-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ringahuman Com Domain Security
  slug: ringahuman-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: ringahuman
  slug: ringahuman-com-ringahuman
- name: ringahuman
  slug: ringahuman-com-skill
slug: ringahuman-com
tags:
- Company
- Artificial Intelligence
- Telephony
- Lead Generation
- Compliance
website: https://ringahuman.com/
---
