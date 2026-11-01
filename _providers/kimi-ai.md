---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kimi Ai Agentic Access
  operation_count: 13
  slug: kimi-ai-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: The Batch API from Moonshot AI — 4 operation(s) for batch.
  name: Moonshot AI Batch API
  slug: kimi-ai-batch-api
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: The Billing API from Moonshot AI — 1 operation(s) for billing.
  name: Moonshot AI Billing API
  slug: kimi-ai-billing-api
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: The Files API from Moonshot AI — 3 operation(s) for files.
  name: Moonshot AI Files API
  slug: kimi-ai-files-api
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: The Models API from Moonshot AI — 1 operation(s) for models.
  name: Moonshot AI Models API
  slug: kimi-ai-models-api
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: The Utilities API from Moonshot AI — 2 operation(s) for utilities.
  name: Moonshot AI Utilities API
  slug: kimi-ai-utilities-api
- description: OpenAI-compatible embeddings endpoint that returns vector representations of input text for semantic search, clustering, and retrieval-augmented generation workflows.
  name: Kimi Embeddings API
  slug: kimi-ai-embeddings-api
- description: Fine-tuning jobs endpoint for customizing Moonshot base models on customer-supplied training data. Mirrors the OpenAI fine-tuning surface.
  name: Kimi Fine-Tuning API
  slug: kimi-ai-fine-tuning-api
- description: Helper endpoint exposed by the Moonshot platform for counting tokens against a given model's tokenizer prior to submission, useful for managing long-context budgets.
  name: Kimi Tokenizer API
  slug: kimi-ai-tokenizer-api
- description: Consumer-facing AI assistant at kimi.com (also kimi.ai) powered by the Kimi models. Supports long-document upload, web search grounding, and tool use through a chat UI.
  name: Kimi Assistant (kimi.com)
  slug: kimi-ai-kimi-assistant
- description: Open-weight Kimi model releases (for example prior Kimi K1 / K2 checkpoints) published under the MoonshotAI GitHub organization for research and self-hosted use.
  name: Moonshot Open-Weights Releases
  slug: kimi-ai-open-weights
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: POST /v1/responses — "Create a model response", an OpenAI Responses-compatible endpoint with function, custom and web-search tools and streaming events, as published in https://platform.kimi.ai/docs/o
  name: Moonshot AI Responses API
  slug: kimi-ai-responses-api
- baseURL: https://api.moonshot.ai
  baseurl_source: declared
  description: 'Official tools for models: POST /v1/tools/search (Web Search Basic), POST /v1/tools/search_pro (Web Search Pro) and POST /v1/tools/fetch (URL Fetch), as published in https://platform.kimi.ai/docs/open'
  name: Moonshot AI Tools API
  slug: kimi-ai-tools-api
- baseURL: https://api.moonshot.cn
  baseurl_source: declared
  description: The Messages API from Kimi (Moonshot AI) — 1 operation(s) for messages.
  name: Kimi (Moonshot AI) Messages API
  slug: kimi-ai-messages-api
- baseURL: https://api.moonshot.cn
  baseurl_source: declared
  description: The Chat Completions API from Kimi (Moonshot AI) — 1 operation(s) for chat completions.
  name: Kimi (Moonshot AI) Chat Completions API
  slug: kimi-ai-chat-completions-api
artifact_total: 51
asyncapis:
- description: 'AsyncAPI 2.6 description of the Moonshot AI streaming chat completions surface. Moonshot''s `/v1/chat/completions` endpoint is OpenAI-compatible and, when invoked with `stream: true`, delivers incremen'
  name: Moonshot AI Chat Completions Streaming API
  slug: kimi-ai-chat-completions-asyncapi
collections:
- collection_type: open
  name: Moonshot AI Batch API
  slug: open-kimi-ai-batch-api
- collection_type: open
  name: Moonshot AI Batch Billing API
  slug: open-kimi-ai-billing-api
- collection_type: open
  name: Moonshot AI Batch Chat API
  slug: open-kimi-ai-chat-api
- collection_type: open
  name: Moonshot AI Batch Files API
  slug: open-kimi-ai-files-api
- collection_type: open
  name: Moonshot AI Batch Models API
  slug: open-kimi-ai-models-api
- collection_type: open
  name: Moonshot AI Batch Utilities API
  slug: open-kimi-ai-utilities-api
- collection_type: open
  name: Moonshot AI API
  slug: open-kimi-ai
common:
- group: other
  href: https://artifacts.apis.io/kimi-ai/capabilities/kimi-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kimi-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kimi-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/kimi-ai/cli/kimi-ai-cli.yml
  title: ''
  type: CLI
  url: cli/kimi-ai-cli.yml
- group: build
  href: https://artifacts.apis.io/kimi-ai/packages/kimi-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/kimi-ai-packages.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/rules/kimi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/kimi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/rules/kimi-ai-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/kimi-ai-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/json-ld/kimi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kimi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/kimi-ai/vocabulary/kimi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kimi-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/data-model/kimi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kimi-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/errors/kimi-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kimi-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kimi-ai/conformance/kimi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kimi-ai-conformance.yml
- group: build
  href: https://artifacts.apis.io/kimi-ai/integrations/kimi-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/kimi-ai-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/kimi-ai/agentic-access/kimi-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kimi-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kimi-ai/security/kimi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kimi-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kimi-ai/authentication/kimi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kimi-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoonshotAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kimi-ai-linkedin
- group: company
  title: ''
  type: Website
  url: https://www.moonshot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.kimi.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.kimi.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://platform.kimi.ai/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.kimi.ai/docs/get-your-api-key
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.kimi.ai/docs/pricing/chat
- group: start
  title: ''
  type: SignUp
  url: https://platform.kimi.ai/console
- group: operate
  title: ''
  type: ContactSales
  url: https://platform.kimi.ai/contact-sales
- group: company
  title: ''
  type: Blog
  url: https://platform.kimi.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.kimi.ai/docs/platform-changelog
- group: operate
  title: ''
  type: Support
  url: https://forum.moonshot.ai/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/TYU2fdJykW
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.kimi.ai/docs/agreement/modeluse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.kimi.ai/docs/agreement/userprivacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://platform.kimi.ai/docs/llms.txt
- group: company
  title: ''
  type: Careers
  url: https://careers.kimi.ai/
- group: commercial
  href: https://artifacts.apis.io/kimi-ai/plans/kimi-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kimi-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kimi-ai/rate-limits/kimi-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kimi-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kimi-ai/finops/kimi-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/kimi-ai-finops.yml
created: '2026-05-08'
description: Moonshot AI (moonshot.ai) is a Chinese foundation model company whose stated mission is "to seek the optimal conversion from energy to intelligence", best known for Kimi, a family of large language models with long-context capabilities (Kimi K3.1 Pro advertises a 1M-token context window) and the consumer Kimi assistant at kimi.com. The Kimi API Platform (platform.kimi.ai, formerly platform.moonshot.ai; platform.kimi.com in China) exposes OpenAI-compatible chat completion, Anthropic Messages-compatible, files, batch, models, balance, and token-estimation APIs, and the company publishes open-weight Kimi models on GitHub.
finops:
- has_sources: true
  method: generated
  name: Kimi Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: kimi-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonshot-ai.png
json_schemas:
- name: BalanceResponse
  property_count: 4
  slug: kimi-ai-balance-response
- name: BatchCreateRequest
  property_count: 4
  slug: kimi-ai-batch-create-request
- name: BatchListResponse
  property_count: 3
  slug: kimi-ai-batch-list-response
- name: BatchObject
  property_count: 18
  slug: kimi-ai-batch-object
- name: ChatCompletionResponse
  property_count: 6
  slug: kimi-ai-chat-completion-response
- name: EstimateTokenRequest
  property_count: 2
  slug: kimi-ai-estimate-token-request
- name: EstimateTokenResponse
  property_count: 1
  slug: kimi-ai-estimate-token-response
- name: FileDeleteResponse
  property_count: 3
  slug: kimi-ai-file-delete-response
- name: FileListResponse
  property_count: 2
  slug: kimi-ai-file-list-response
- name: FileObject
  property_count: 8
  slug: kimi-ai-file-object
- name: kimi-k2
  property_count: 0
  slug: kimi-ai-kimi-k2-chat-request
- name: kimi-k2-thinking
  property_count: 0
  slug: kimi-ai-kimi-k2-thinking-chat-request
- name: kimi-k2.5
  property_count: 0
  slug: kimi-ai-kimi-k25-chat-request
- name: kimi-k2.6
  property_count: 0
  slug: kimi-ai-kimi-k26-chat-request
- name: moonshot-v1
  property_count: 0
  slug: kimi-ai-moonshot-v1-chat-request
jsonld:
- class_count: 15
  name: Kimi Ai Context
  property_count: 51
  slug: kimi-ai-context
layout: provider
modified: '2026-10-26'
name: Kimi (Moonshot AI)
nav: Providers
network: true
overview: 'Kimi (Moonshot AI) publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Moonshot AI Batch API, Moonshot AI Billing API, Moonshot AI Files API, and 11 more. Tagged areas include Artificial Intelligence, LLM, Inference, Long Context, and Kimi.


  The Kimi (Moonshot AI) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Kimi (Moonshot AI)''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Kimi Ai Plans Pricing
  plan_count: 11
  slug: kimi-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 30
  name: Kimi Ai Rate Limits
  slug: kimi-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Kimi (Moonshot AI) — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: kimi-ai-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Kimi (Moonshot AI) API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: kimi-ai-rules
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 72.2
    developer_ergonomics: 80.4
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kimi-ai/kimi-ai-2026-06-20T185801.png
security:
- kind: authentication
  name: Kimi Ai Authentication
  slug: kimi-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kimi Ai Domain Security
  slug: kimi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: kimi-ai-batch-processing
  slug: kimi-ai-batch-processing
- name: kimi-ai-chat-completion
  slug: kimi-ai-chat-completion
- name: kimi-ai-check-balance
  slug: kimi-ai-check-balance
- name: kimi-ai-file-question-answering
  slug: kimi-ai-file-question-answering
- name: kimi-ai-web-research
  slug: kimi-ai-web-research
slug: kimi-ai
tags:
- Artificial Intelligence
- LLM
- Inference
- Long Context
- Kimi
- Foundation Models
website: https://www.moonshot.ai/
---
