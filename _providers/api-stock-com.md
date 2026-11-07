---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 32
  name: Api Stock Com Agentic Access
  operation_count: 71
  slug: api-stock-com-agentic-access
  summary_line: 71 operations · 32 acting · 32 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Account Management API from api-stock-com — 2 operation(s) for account management.
  name: api-stock-com Account Management API
  slug: api-stock-com-account-management-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Agent API from api-stock-com — 45 operation(s) for agent.
  name: api-stock-com Agent API
  slug: api-stock-com-agent-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Catalog API from api-stock-com — 3 operation(s) for catalog.
  name: api-stock-com Catalog API
  slug: api-stock-com-catalog-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Costs API from api-stock-com — 2 operation(s) for costs.
  name: api-stock-com Costs API
  slug: api-stock-com-costs-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Generations API from api-stock-com — 4 operation(s) for generations.
  name: api-stock-com Generations API
  slug: api-stock-com-generations-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The LLM API from api-stock-com — 3 operation(s) for llm.
  name: api-stock-com LLM API
  slug: api-stock-com-llm-api
- baseURL: https://api.api-stock.com
  baseurl_source: declared
  description: The Task Management API from api-stock-com — 1 operation(s) for task management.
  name: api-stock-com Task Management API
  slug: api-stock-com-task-management-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/api-stock-com/agentic-access/api-stock-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/api-stock-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/api-stock-com/rate-limits/api-stock-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/api-stock-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/api-stock-com/rules/api-stock-com-rules.yml
  title: ''
  type: Spectral
  url: rules/api-stock-com-rules.yml
- group: design
  href: https://artifacts.apis.io/api-stock-com/json-ld/api-stock-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/api-stock-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/api-stock-com/vocabulary/api-stock-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/api-stock-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/api-stock-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/api-stock-com/data-model/api-stock-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/api-stock-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/api-stock-com/authentication/api-stock-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/api-stock-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/api-stock-com/errors/api-stock-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-stock-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/api-stock-com/conformance/api-stock-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-stock-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/api-stock-com/llms/api-stock-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-stock-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/api-stock-com/well-known/api-stock-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api-stock-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/api-stock-com/hosts/api-stock-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-stock-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/api-stock-com/vendors/api-stock-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-stock-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api-stock.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://api-stock.com/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api-stock.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://api-stock.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.api-stock.com</code
- group: auth
  href: https://artifacts.apis.io/api-stock-com/security/api-stock-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-stock-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api-stock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api-stock.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api-stock.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api-stock.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://api-stock.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.api-stock.com/openapi.json
  - status: 401
    url: https://api.api-stock.com/mcp
  - status: 200
    url: https://api-stock.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: API Stock provides a unified API platform offering video, image, music, and large language model (LLM) capabilities. Users can access a catalog of AI models with a single API key and prepaid balance, benefiting from automatic failover to reserve providers. The service includes a dashboard for account management, pricing details, and quickstart guides, and supports OpenAI‑compatible chat endpoints and asynchronous media APIs.
image: https://api-stock.com/opengraph-image
json_schemas:
- name: AnthropicMessageResponseDto
  property_count: 7
  slug: api-stock-com-anthropic-message-response-dto
- name: CatalogModelDto
  property_count: 17
  slug: api-stock-com-catalog-model-dto
- name: ChatCompletionRequestDto
  property_count: 8
  slug: api-stock-com-chat-completion-request-dto
- name: CreateGenerationRequestDto
  property_count: 3
  slug: api-stock-com-create-generation-request-dto
- name: GenerationDto
  property_count: 13
  slug: api-stock-com-generation-dto
- name: StatsResponseDto
  property_count: 6
  slug: api-stock-com-stats-response-dto
jsonld:
- class_count: 76
  name: Api Stock Com Context
  property_count: 224
  slug: api-stock-com-context
layout: provider
modified: '2026-10-30'
name: api-stock-com
nav: Providers
network: true
overview: 'api-stock-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Management API, Agent API, Catalog API, and 4 more. Tagged areas include Artificial Intelligence, Machine Learning, LLM, and Platform.


  The api-stock-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  api-stock-com''s developer surface includes authentication, signup flow, engineering blog, documentation, API reference, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Api Stock Com Plans Pricing
  plan_count: 0
  slug: api-stock-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Api Stock Com Rate Limits
  slug: api-stock-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: api-stock-com API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: api-stock-com-rules
scopes:
- name: Api Stock Com Scopes
  scope_count: 0
  slug: api-stock-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 38.6
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
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
screenshot: https://apis.io/screenshots/api-stock-com/api-stock-com-2026-11-03T120934.png
security:
- kind: authentication
  name: Api Stock Com Authentication
  slug: api-stock-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Api Stock Com Domain Security
  slug: api-stock-com-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 1
skills:
- name: api-stock-com-agent
  slug: api-stock-com-agent
slug: api-stock-com
tags:
- Artificial Intelligence
- Machine Learning
- LLM
- Platform
website: https://api-stock.com/
---
