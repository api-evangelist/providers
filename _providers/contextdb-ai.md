---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Contextdb Ai Agentic Access
  operation_count: 24
  slug: contextdb-ai-agentic-access
  summary_line: 24 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.contextdb.ai
  baseurl_source: declared
  description: Check trusted memories and resolve explicit confirmations
  name: ContextDB Decisions API
  slug: contextdb-ai-decisions-api
- baseURL: https://api.contextdb.ai
  baseurl_source: declared
  description: Model Context Protocol discovery and tool calls
  name: ContextDB MCP API
  slug: contextdb-ai-mcp-api
- baseURL: https://api.contextdb.ai
  baseurl_source: declared
  description: Store, extract, and recall customer memories
  name: ContextDB Memory API
  slug: contextdb-ai-memory-api
- baseURL: https://api.contextdb.ai
  baseurl_source: declared
  description: Public process health and dependency readiness
  name: ContextDB Meta API
  slug: contextdb-ai-meta-api
- baseURL: https://api.contextdb.ai
  baseurl_source: declared
  description: OAuth discovery, dynamic registration, tokens, and revocation for MCP
  name: ContextDB OAuth API
  slug: contextdb-ai-oauth-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/contextdb-ai/agentic-access/contextdb-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contextdb-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/contextdb-ai/plans/contextdb-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextdb-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/rules/contextdb-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/contextdb-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/json-ld/contextdb-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contextdb-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/contextdb-ai/vocabulary/contextdb-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextdb-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/contextdb-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/data-model/contextdb-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextdb-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/contextdb-ai/changelog/contextdb-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contextdb-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/conventions/contextdb-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/contextdb-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/conventions/contextdb-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contextdb-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://contextdb.ai/security
- group: design
  href: https://artifacts.apis.io/contextdb-ai/errors/contextdb-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contextdb-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/contextdb-ai/conformance/contextdb-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextdb-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextdb-ai/llms/contextdb-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextdb-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextdb-ai/well-known/contextdb-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextdb-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextdb-ai/hosts/contextdb-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextdb-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/contextdb-ai/packages/contextdb-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/contextdb-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/contextdb-ai/packages/contextdb-ai-packages.yml
  title: ''
  type: Packages
  url: packages/contextdb-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://contextdb.ai/status
- group: auth
  title: ''
  type: Security
  url: https://contextdb.ai/security
- group: start
  title: ''
  type: Sandbox
  url: https://app.contextdb.ai/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://contextdb.ai/changelog
- group: auth
  href: https://artifacts.apis.io/contextdb-ai/scopes/contextdb-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/contextdb-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/contextdb-ai/authentication/contextdb-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contextdb-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/contextdb-ai/security/contextdb-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contextdb-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/contextdb-ai/security/contextdb-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextdb-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextdb.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://contextdb.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://contextdb.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://contextdb.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://contextdb.ai/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://contextdb.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://contextdb.ai/trust
- group: start
  title: ''
  type: SignUp
  url: https://app.contextdb.ai/register
- group: start
  title: ''
  type: Login
  url: https://app.contextdb.ai/login
created: '2026-11-04'
description: ContextDB provides a customer memory platform for AI agents, enabling them to retain context across calls, chats, and days. The service records interactions, stores evidence, and allows agents to act, ask for clarification, or abstain based on verified data, improving reliability and compliance for automated decision-making.
image: https://cdn.contextdb.ai/v1/og/20260921-1/index-1200x630.png
json_schemas:
- name: EvolveRequest
  property_count: 11
  slug: contextdb-ai-evolve-request
- name: EvolveResponse
  property_count: 10
  slug: contextdb-ai-evolve-response
- name: ExecutionReceiptRequest
  property_count: 6
  slug: contextdb-ai-execution-receipt-request
- name: FormationJob
  property_count: 22
  slug: contextdb-ai-formation-job
- name: FormationResponse
  property_count: 13
  slug: contextdb-ai-formation-response
- name: RecallRequest
  property_count: 10
  slug: contextdb-ai-recall-request
jsonld:
- class_count: 44
  name: db Ai Context
  property_count: 112
  slug: contextdb-ai-context
layout: provider
modified: '2026-11-04'
name: ContextDB
nav: Providers
network: true
overview: 'ContextDB publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Decisions API, MCP API, Memory API, and 2 more. Tagged areas include Artificial Intelligence, Memory, Customer Data, Agent Platform, and Context.


  The ContextDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ContextDB''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Contextdb Ai Plans Pricing
  plan_count: 6
  slug: contextdb-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: ContextDB API Rules
  rule_count: 69
  severity_counts:
    error: 60
    hint: 0
    info: 4
    warn: 5
  slug: contextdb-ai-rules
scopes:
- name: Contextdb Ai Scopes
  scope_count: 3
  slug: contextdb-ai-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 70.8
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contextdb Ai Authentication
  slug: contextdb-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Contextdb Ai Domain Security
  slug: contextdb-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Contextdb Ai Trust Center
  slug: contextdb-ai-trust-center
  summary_line: SOC 2
skill_count: 2
skills:
- name: contextdb-ai-decisions-workflow
  slug: contextdb-ai-decisions-workflow
- name: contextdb-ai-oauth-token-management
  slug: contextdb-ai-oauth-token-management
slug: contextdb-ai
tags:
- Artificial Intelligence
- Memory
- Customer Data
- Agent Platform
- Context
website: https://contextdb.ai/
---
