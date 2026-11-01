---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 32
  human_in_the_loop: 32
  name: Apihubs Ru Agentic Access
  operation_count: 71
  slug: apihubs-ru-agentic-access
  summary_line: 71 operations · 32 acting · 32 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.apihubs.ru
  baseurl_source: declared
  description: The Агент API from apihubs-ru — 57 operation(s) for агент.
  name: apihubs-ru Агент API
  slug: apihubs-ru-default-api
- baseURL: https://api.apihubs.ru
  baseurl_source: declared
  description: The LLM API from apihubs-ru — 3 operation(s) for llm.
  name: apihubs-ru LLM API
  slug: apihubs-ru-llm-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/apihubs-ru/agentic-access/apihubs-ru-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apihubs-ru-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/apihubs-ru/rules/apihubs-ru-rules.yml
  title: ''
  type: Spectral
  url: rules/apihubs-ru-rules.yml
- group: design
  href: https://artifacts.apis.io/apihubs-ru/json-ld/apihubs-ru-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apihubs-ru-context.jsonld
- group: design
  href: https://artifacts.apis.io/apihubs-ru/vocabulary/apihubs-ru-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apihubs-ru-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apihubs-ru/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apihubs-ru/data-model/apihubs-ru-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apihubs-ru-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apihubs-ru/authentication/apihubs-ru-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apihubs-ru-authentication.yml
- group: design
  href: https://artifacts.apis.io/apihubs-ru/errors/apihubs-ru-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apihubs-ru-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apihubs-ru/conformance/apihubs-ru-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apihubs-ru-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apihubs-ru/llms/apihubs-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apihubs-ru-llms.txt
- group: agent
  href: https://artifacts.apis.io/apihubs-ru/well-known/apihubs-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apihubs-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/apihubs-ru/hosts/apihubs-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apihubs-ru-hosts.yml
- group: other
  href: https://artifacts.apis.io/apihubs-ru/vendors/apihubs-ru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apihubs-ru-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://apihubs.ru/auth/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.apihubs.ru</code
- group: auth
  href: https://artifacts.apis.io/apihubs-ru/security/apihubs-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apihubs-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apihubs.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apihubs.ru/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apihubs.ru/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apihubs.ru/en/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://apihubs.ru/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://apihubs.ru/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apihubs.ru/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apihubs.ru/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/apihubs-ru
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.apihubs.ru/openapi.json
  - status: 401
    url: https://api.apihubs.ru/mcp
  - status: 200
    url: https://apihubs.ru/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: API Hubs provides a marketplace of over 70 cutting‑edge AI models, including GPT, Claude, Gemini, DeepSeek, Veo, Kling and Suno, all accessible via a single unified API at low prices. Payments are accepted via Russian fast‑payment system (СБП) and Mir cards, without VPN or subscription requirements. The platform offers quick start guides, pricing details, and comprehensive documentation in Russian and English.
image: https://apihubs.ru/opengraph-image
json_schemas:
- name: AnthropicMessageRequestDto
  property_count: 4
  slug: apihubs-ru-anthropic-message-request-dto
- name: CatalogModelDto
  property_count: 17
  slug: apihubs-ru-catalog-model-dto
- name: ChatCompletionRequestDto
  property_count: 8
  slug: apihubs-ru-chat-completion-request-dto
- name: CreateGenerationRequestDto
  property_count: 3
  slug: apihubs-ru-create-generation-request-dto
- name: GenerationDto
  property_count: 13
  slug: apihubs-ru-generation-dto
- name: StatsResponseDto
  property_count: 6
  slug: apihubs-ru-stats-response-dto
jsonld:
- class_count: 76
  name: Apihubs Ru Context
  property_count: 224
  slug: apihubs-ru-context
layout: provider
modified: '2026-10-30'
name: apihubs-ru
nav: Providers
network: true
overview: 'apihubs-ru publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Агент API and LLM API. Tagged areas include API, AI, Marketplace, Russian, and SaaS.


  The apihubs-ru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apihubs-ru''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Apihubs Ru Plans Pricing
  plan_count: 0
  slug: apihubs-ru-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Apihubs Ru Rate Limits
  slug: apihubs-ru-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: apihubs-ru API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: apihubs-ru-rules
scopes:
- name: Apihubs Ru Scopes
  scope_count: 0
  slug: apihubs-ru-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 55.3
    developer_ergonomics: 63.6
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apihubs Ru Authentication
  slug: apihubs-ru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apihubs Ru Domain Security
  slug: apihubs-ru-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: apihubs-ru-agent
  slug: apihubs-ru-agent
slug: apihubs-ru
tags:
- API
- AI
- Marketplace
- Russian
- SaaS
website: https://apihubs.ru/
---
