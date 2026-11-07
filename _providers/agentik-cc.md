---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    event_surface_described: unknown
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Agentik Cc Agentic Access
  operation_count: 20
  slug: agentik-cc-agentic-access
  summary_line: 20 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agentik.cc
  baseurl_source: declared
  description: The discover API from Agentik — 7 operation(s) for discover.
  name: Agentik Discover API
  slug: agentik-cc-discover-api
- baseURL: https://api.agentik.cc
  baseurl_source: declared
  description: The oauth API from Agentik — 6 operation(s) for oauth.
  name: Agentik OAuth API
  slug: agentik-cc-oauth-api
- baseURL: https://api.agentik.cc
  baseurl_source: declared
  description: The run API from Agentik — 3 operation(s) for run.
  name: Agentik Run API
  slug: agentik-cc-run-api
- baseURL: https://api.agentik.cc
  baseurl_source: declared
  description: The wallet API from Agentik — 4 operation(s) for wallet.
  name: Agentik Wallet API
  slug: agentik-cc-wallet-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/agentik-cc/agentic-access/agentik-cc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentik-cc-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentik-cc/plans/agentik-cc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentik-cc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/rules/agentik-cc-rules.yml
  title: ''
  type: Spectral
  url: rules/agentik-cc-rules.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/json-ld/agentik-cc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentik-cc-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentik-cc/vocabulary/agentik-cc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentik-cc-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentik-cc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/data-model/agentik-cc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentik-cc-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentik-cc/changelog/agentik-cc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentik-cc-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/conventions/agentik-cc-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentik-cc-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/conventions/agentik-cc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentik-cc-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentik-cc/authentication/agentik-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentik-cc-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/errors/agentik-cc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentik-cc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentik-cc/conformance/agentik-cc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentik-cc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentik-cc/llms/agentik-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentik-cc-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentik-cc/well-known/agentik-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentik-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentik-cc/hosts/agentik-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentik-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentik-cc/vendors/agentik-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentik-cc-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.agentik.cc/tools/webhooks
- group: auth
  title: ''
  type: Security
  url: https://www.agentik.cc/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.agentik.cc/tools/news
- group: start
  title: ''
  type: Login
  url: https://www.agentik.cc/account/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agentik.cc/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.agentik.cc/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://www.agentik.cc/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentik-cc/scopes/agentik-cc-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agentik-cc-scopes.yml
- group: auth
  href: https://artifacts.apis.io/agentik-cc/security/agentik-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentik-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentik.cc
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentik.cc/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentik.cc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentik.cc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentik.cc/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.agentik.cc/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentik.cc/playbooks
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://www.agentik.cc/openapi.json
  - status: null
    url: https://ai.agentik.cc/openapi.json
  - status: null
    url: https://api.agentik.cc/openapi.json
  - status: 401
    url: https://ai.agentik.cc/mcp
  - status: 401
    url: https://api.agentik.cc/mcp
  - status: 200
    url: https://www.agentik.cc
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Agentik connects Claude, ChatGPT, Codex and Cursor to over 3,500 tools through a single MCP connection, allowing agents to invoke each tool at the provider's price. The platform offers step‑by‑step playbooks, pricing details, and comprehensive documentation hosted on a modern Next.js site. It is operated by BURIZA, a French single‑member simplified joint‑stock company (SASU) based in Paris, and provides a public API described in OpenAPI format.
image: https://www.agentik.cc/film/agentik-og.jpg
json_schemas:
- name: AgentInfo
  property_count: 9
  slug: agentik-cc-agent-info
- name: DiscoverResponse
  property_count: 2
  slug: agentik-cc-discover-response
- name: RunResult
  property_count: 20
  slug: agentik-cc-run-result
- name: RunView
  property_count: 13
  slug: agentik-cc-run-view
- name: Tool
  property_count: 20
  slug: agentik-cc-tool
- name: WalletBalance
  property_count: 8
  slug: agentik-cc-wallet-balance
jsonld:
- class_count: 13
  name: Agentik Cc Context
  property_count: 71
  slug: agentik-cc-context
layout: provider
modified: '2026-11-05'
name: Agentik
nav: Providers
network: true
overview: 'Agentik publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discover API, OAuth API, Run API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Tools, MCP, and Software-as-a-Service.


  The Agentik catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentik''s developer surface includes changelog, authentication, API reference, documentation, pricing, support, getting-started guide, and 26 more developer resources.'
plans:
- name: Agentik Cc Plans Pricing
  plan_count: 1
  slug: agentik-cc-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Agentik API Rules
  rule_count: 52
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 7
  slug: agentik-cc-rules
scopes:
- name: Agentik Cc Scopes
  scope_count: 1
  slug: agentik-cc-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 56.5
    discoverability: 67.9
    operational_transparency: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentik Cc Authentication
  slug: agentik-cc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentik Cc Domain Security
  slug: agentik-cc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: agentik-cc-discover-tools
  slug: agentik-cc-discover-tools
- name: agentik-cc-oauth-register-and-token
  slug: agentik-cc-oauth-register-and-token
- name: agentik-cc-run-tool-and-check-status
  slug: agentik-cc-run-tool-and-check-status
- name: agentik-cc-wallet-topup
  slug: agentik-cc-wallet-topup
slug: agentik-cc
tags:
- Artificial Intelligence
- Automation
- Tools
- MCP
- Software-as-a-Service
website: https://www.agentik.cc
---
