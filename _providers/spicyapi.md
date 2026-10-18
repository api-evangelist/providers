---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Spicyapi Agentic Access
  operation_count: 24
  slug: spicyapi-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 2
apis:
- baseURL: https://api.spicyapi.ai
  baseurl_source: declared
  description: The Account API from SpicyAPI — 2 operation(s) for account.
  name: SpicyAPI Account API
  slug: spicyapi-account-api
- baseURL: https://api.spicyapi.ai
  baseurl_source: declared
  description: The Media API from SpicyAPI — 3 operation(s) for media.
  name: SpicyAPI Media API
  slug: spicyapi-media-api
- baseURL: https://api.spicyapi.ai
  baseurl_source: declared
  description: The Models API from SpicyAPI — 3 operation(s) for models.
  name: SpicyAPI Models API
  slug: spicyapi-models-api
- baseURL: https://api.spicyapi.ai
  baseurl_source: declared
  description: OpenAI / Anthropic protocol shells under `/v1` and the Google Gemini shell under `/v1beta`. They share API keys, limits, validation and billing with `/api/v1` but use the external protocol's own reque
  name: SpicyAPI OpenAI Compatible API
  slug: spicyapi-openai-compatible-api
- baseURL: https://api.spicyapi.ai
  baseurl_source: declared
  description: The Tasks API from SpicyAPI — 7 operation(s) for tasks.
  name: SpicyAPI Tasks API
  slug: spicyapi-tasks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Spicyapi Webhooks
  slug: spicyapi-webhooks
common:
- group: auth
  title: ''
  type: Security
  url: https://spicyapi.ai/legal/reporting
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/agentic-access/spicyapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spicyapi-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/rate-limits/spicyapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spicyapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/plans/spicyapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spicyapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/rules/spicyapi-rules.yml
  title: ''
  type: Spectral
  url: rules/spicyapi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/json-ld/spicyapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spicyapi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/vocabulary/spicyapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spicyapi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/asyncapi/spicyapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/spicyapi-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/data-model/spicyapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spicyapi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/conventions/spicyapi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/spicyapi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/conventions/spicyapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spicyapi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/errors/spicyapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spicyapi-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/conformance/spicyapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spicyapi-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/llms/spicyapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spicyapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/mcp/spicyapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/spicyapi-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/well-known/spicyapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spicyapi-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/well-known/spicyapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spicyapi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/hosts/spicyapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spicyapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/vendors/spicyapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spicyapi-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/packages/spicyapi-packages.yml
  title: ''
  type: Packages
  url: packages/spicyapi-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://spicyapi.ai/trust
- group: start
  title: ''
  type: Sandbox
  url: https://spicyapi.ai/console
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@spicyapi/sdk
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/authentication/spicyapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spicyapi-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/security/spicyapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/spicyapi-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/security/spicyapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spicyapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spicyapi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spicyapi.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spicyapi.ai/docs/api-reference
- group: company
  title: ''
  type: Blog
  url: https://spicyapi.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://spicyapi.ai/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://spicyapi.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spicyapi.ai/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spicyapi-ai
- group: start
  title: ''
  type: Login
  url: https://spicyapi.ai/login
- group: start
  title: ''
  type: SignUp
  url: https://spicyapi.ai/register
- group: commercial
  title: ''
  type: Pricing
  url: https://spicyapi.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spicyapi.ai/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spicyapi.ai/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spicyapi.ai
created: '2026-10-09'
description: SpicyAPI is a pay-as-you-go aggregator for generative media and chat models. One API key reaches image, video, audio and LLM models through an async jobs API (quote, create task, poll, stream, retry) plus OpenAI-, Anthropic- and Gemini-compatible endpoints (chat completions, responses, messages, generateContent, videos), with a model catalog, usage and credit endpoints, signed upload/download URLs, webhooks and first-party SDKs.
image: https://spicyapi.ai/opengraph-image
json_schemas:
- name: ChatCompletionRequest
  property_count: 14
  slug: spicyapi-chat-completion-request
- name: ChatCompletion
  property_count: 6
  slug: spicyapi-chat-completion
- name: CreateTaskRequest
  property_count: 5
  slug: spicyapi-create-task-request
- name: GeminiGenerateContentRequest
  property_count: 5
  slug: spicyapi-gemini-generate-content-request
- name: OpenAIModelList
  property_count: 2
  slug: spicyapi-open-aimodel-list
- name: ResponseObject
  property_count: 9
  slug: spicyapi-response-object
jsonld:
- class_count: 49
  name: Spicyapi Context
  property_count: 196
  slug: spicyapi-context
layout: provider
mcp_servers:
- description: ''
  name: SpicyAPI MCP Server
  slug: spicyapi-mcp-server
modified: '2026-10-09'
name: SpicyAPI
nav: Providers
network: true
overview: 'SpicyAPI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Media API, Models API, and 2 more. Tagged areas include Company, Artificial Intelligence, Generative Media, LLM, and Video Generation.


  The SpicyAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SpicyAPI''s developer surface includes sandbox, authentication, documentation, API reference, engineering blog, changelog, getting-started guide, and 33 more developer resources.'
plans:
- name: Spicyapi Plans Pricing
  plan_count: 1
  slug: spicyapi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Spicyapi Rate Limits
  slug: spicyapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: SpicyAPI API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 7
  slug: spicyapi-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 73.7
    contract_governance: 22.0
    contract_quality: 70.5
    developer_ergonomics: 66.7
    discoverability: 71.7
    operational_transparency: 86.8
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/spicyapi/refs/heads/main/screenshots/spicyapi-2026-10-11T130144.png
security:
- kind: authentication
  name: Spicyapi Authentication
  slug: spicyapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spicyapi Domain Security
  slug: spicyapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spicyapi Vulnerability Disclosure
  slug: spicyapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spicyapi
tags:
- Company
- Artificial Intelligence
- Generative Media
- LLM
- Video Generation
- Image Generation
- Model Aggregator
website: https://spicyapi.ai
---
