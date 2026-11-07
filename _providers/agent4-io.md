---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 通用跨行业租户 RAG 聊天智能平台
  name: Agent4.io API
  slug: agent4-io-api
- description: '多租户 RAG 聊天智能体平台。鉴权分层：`X-Admin-Token`（平台）、`X-API-Key`（租户）、`X-End-User`（代理终端用户）、`Authorization: Bearer `（平台登录终端用户）、`X-Act-Tenant`（admin 以租户身份）、可选 `X-Space-Id`。详见管理端「API 文档」页。'
  name: chatagent-platform Api API
  slug: chatagent-platform-api-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/agent4-io/plans/agent4-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agent4-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agent4-io/rules/agent4-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agent4-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agent4-io/json-ld/agent4-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agent4-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/agent4-io/vocabulary/agent4-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent4-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agent4-io/data-model/agent4-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent4-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agent4-io/changelog/agent4-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agent4-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/agent4-io/authentication/agent4-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent4-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agent4-io/errors/agent4-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent4-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent4-io/conformance/agent4-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent4-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent4-io/llms/agent4-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent4-io-llms.txt
- group: other
  href: https://artifacts.apis.io/agent4-io/hosts/agent4-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent4-io-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://agent4.io/register
- group: operate
  title: ''
  type: ChangeLog
  url: https://agent4.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://agent4.io/solutions/saas-onboarding
- group: docs
  title: ''
  type: APIReference
  url: https://agent4.io/api
- group: auth
  href: https://artifacts.apis.io/agent4-io/security/agent4-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent4-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent4.io/
- group: docs
  title: ''
  type: Documentation
  url: https://agent4.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agent4.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent4.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent4.io/privacy
- group: operate
  title: ''
  type: Contact
  url: https://agent4.io/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.agent4.io/openapi.json
  - status: null
    url: https://api.agent4.io/mcp
  - status: null
    url: https://chat.agent4.io/openapi.json
  - status: null
    url: https://console.agent4.io/openapi.json
  - status: 200
    url: https://agent4.io/api/mcp
  - status: 200
    url: https://agent4.io/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Agent4.io provides AI-powered autonomous agents that consult, convert, and follow up with customers. Their platform automates routine work such as answering queries, qualifying leads, and handling follow‑ups across web, chat, and voice channels. It targets businesses looking to reduce operational costs and free staff for higher‑value tasks. The solution includes customizable workflows, memory per customer, and integration via APIs and MCP, supporting industries like legal, immigration, insurance, lending, and hospitality.
image: https://agent4.io/opengraph-image?8122e713717ccac9
json_schemas:
- name: AgentIn
  property_count: 27
  slug: agent4-io-agent-in
- name: AgentOut
  property_count: 31
  slug: agent4-io-agent-out
- name: AgentPatch
  property_count: 33
  slug: agent4-io-agent-patch
- name: MyDocDetailOut
  property_count: 17
  slug: agent4-io-my-doc-detail-out
- name: ShareChatIn
  property_count: 22
  slug: agent4-io-share-chat-in
- name: ShareInfo
  property_count: 32
  slug: agent4-io-share-info
jsonld:
- class_count: 120
  name: Agent4 Io Context
  property_count: 301
  slug: agent4-io-context
layout: provider
modified: '2026-11-01'
name: Agent4.io
nav: Providers
network: true
overview: 'Agent4.io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including chatagent-platform Api API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Customer Engagement, Software-as-a-Service, and Agent Platform.


  The Agent4.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent4.io''s developer surface includes changelog, authentication, signup flow, getting-started guide, API reference, documentation, pricing, and 15 more developer resources.'
plans:
- name: Agent4 Io Plans Pricing
  plan_count: 4
  slug: agent4-io-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Agent4.io API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: agent4-io-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 47.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agent4 Io Authentication
  slug: agent4-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agent4 Io Domain Security
  slug: agent4-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: agent4-io
tags:
- Artificial Intelligence
- Automation
- Customer Engagement
- Software-as-a-Service
- Agent Platform
website: https://agent4.io/
---
