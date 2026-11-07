---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
  score: 28.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agentic Memory provides a REST API for persistent AI agent memory.
  name: Agentic Memory API
  slug: agentic-memory-api
- description: 'agenticmemory-ai API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: agenticmemory-ai API
  slug: agenticmemory-ai-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/agenticmemory-ai/rate-limits/agenticmemory-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenticmemory-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agenticmemory-ai/plans/agenticmemory-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenticmemory-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/rules/agenticmemory-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticmemory-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/json-ld/agenticmemory-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenticmemory-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/vocabulary/agenticmemory-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenticmemory-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/data-model/agenticmemory-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenticmemory-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/agenticmemory-ai/cli/agenticmemory-ai-cli.yml
  title: ''
  type: CLI
  url: cli/agenticmemory-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/conventions/agenticmemory-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agenticmemory-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/conventions/agenticmemory-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agenticmemory-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agenticmemory-ai/authentication/agenticmemory-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenticmemory-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenticmemory-ai/conformance/agenticmemory-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticmemory-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticmemory-ai/llms/agenticmemory-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticmemory-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agenticmemory-ai/hosts/agenticmemory-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticmemory-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/agenticmemory-ai/packages/agenticmemory-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/agenticmemory-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/agenticmemory-ai/packages/agenticmemory-ai-packages.yml
  title: ''
  type: Packages
  url: packages/agenticmemory-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agenticmemory.ai/
- group: start
  title: ''
  type: Login
  url: https://agenticmemory.ai/auth/login
- group: other
  title: ''
  type: Leadership
  url: https://agenticmemory.ai/onboard/team
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticmemory.ai/quickstart
- group: auth
  href: https://artifacts.apis.io/agenticmemory-ai/security/agenticmemory-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticmemory-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticmemory.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticmemory.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agenticmemory.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agenticmemory.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://agenticmemory.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticmemory.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticmemory.ai/privacy
coverage:
  checked: '2026-10-30'
  detail: API documentation is served as a JavaScript-rendered HTML page with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://agenticmemory.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Agentic Memory provides a persistent memory API for AI agents and LLMs. It enables developers to store and retrieve conversation history, key‑value context, and scratchpad data with sub‑millisecond latency. A free tier is available, and detailed documentation and SDKs for multiple languages facilitate seamless integration of memory capabilities into autonomous AI workflows.
image: https://prodmedia.tyga.host/public/tyga.cloud/landing/agenticmemory.ai/agenticmemory-black-words.svg
json_schemas:
- name: GetV1MemorySpaceidContextUserPrefsResponse
  property_count: 1
  slug: agenticmemory-ai-get-v1-memory-spaceid-context-user-prefs-response
- name: GetV1MemorySpaceidMessagesResponse
  property_count: 1
  slug: agenticmemory-ai-get-v1-memory-spaceid-messages-response
- name: PostV1MemoryResponse
  property_count: 3
  slug: agenticmemory-ai-post-v1-memory-response
- name: PostV1MemorySpaceidBootstrapResponse
  property_count: 1
  slug: agenticmemory-ai-post-v1-memory-spaceid-bootstrap-response
- name: PostV1MemorySpaceidMessagesResponse
  property_count: 1
  slug: agenticmemory-ai-post-v1-memory-spaceid-messages-response
- name: PostV1MemorySpaceidSearchResponse
  property_count: 1
  slug: agenticmemory-ai-post-v1-memory-spaceid-search-response
jsonld:
- class_count: 20
  name: Agenticmemory Ai Context
  property_count: 18
  slug: agenticmemory-ai-context
layout: provider
modified: '2026-10-30'
name: agenticmemory-ai
nav: Providers
network: true
overview: 'agenticmemory-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, Agents, and LLM.


  The agenticmemory-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agenticmemory-ai''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Agenticmemory Ai Plans Pricing
  plan_count: 3
  slug: agenticmemory-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Agenticmemory Ai Rate Limits
  slug: agenticmemory-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: agenticmemory-ai API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: agenticmemory-ai-rules
scopes:
- name: Agenticmemory Ai Scopes
  scope_count: 0
  slug: agenticmemory-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.0
    catalog_earned_first_party: 20.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 25.0
    developer_ergonomics: 41.7
    discoverability: 58.0
    operational_transparency: 28.9
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
screenshot: https://apis.io/screenshots/agenticmemory-ai/agenticmemory-ai-2026-11-03T120359.png
security:
- kind: authentication
  name: Agenticmemory Ai Authentication
  slug: agenticmemory-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenticmemory Ai Domain Security
  slug: agenticmemory-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenticmemory-ai
tags:
- Company
- Artificial Intelligence
- Memory
- Agents
- LLM
website: https://agenticmemory.ai/
---
