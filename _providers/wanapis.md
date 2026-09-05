---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: OpenAI-compatible REST API gateway aggregating GPT, Claude, Gemini, DeepSeek, plus image, video, and audio model providers behind a single key and routing/failover layer. Model marketplace, usage logs
  name: WanAPIs Unified AI API
  slug: wanapis-unified-ai-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Text-to-speech, transcription, and translation.
  name: WanAPIs Audio API
  slug: wanapis-audio-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Chat completion endpoints (OpenAI Chat Completions compatible).
  name: WanAPIs Chat API
  slug: wanapis-chat-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Legacy text completions (OpenAI compatible).
  name: WanAPIs Completions API
  slug: wanapis-completions-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Vector embeddings (OpenAI compatible).
  name: WanAPIs Embeddings API
  slug: wanapis-embeddings-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Image generation and editing.
  name: WanAPIs Images API
  slug: wanapis-images-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Discover the models available in the marketplace.
  name: WanAPIs Models API
  slug: wanapis-models-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: WanAPIs Responses API for structured, multi-step model workflows.
  name: WanAPIs Responses API
  slug: wanapis-responses-api
- baseURL: https://api.wanapis.com/v1
  baseurl_source: declared
  description: Async task polling for long-running image/video/audio jobs.
  name: WanAPIs Tasks API
  slug: wanapis-tasks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WanAPIs Unified AI Audio API
  slug: open-wanapis-audio-api
- collection_type: open
  name: WanAPIs Unified AI Chat API
  slug: open-wanapis-chat-api
- collection_type: open
  name: WanAPIs Unified AI Completions API
  slug: open-wanapis-completions-api
- collection_type: open
  name: WanAPIs Unified AI Embeddings API
  slug: open-wanapis-embeddings-api
- collection_type: open
  name: WanAPIs Unified AI Images API
  slug: open-wanapis-images-api
- collection_type: open
  name: WanAPIs Unified AI Models API
  slug: open-wanapis-models-api
- collection_type: open
  name: WanAPIs Unified AI Responses API
  slug: open-wanapis-responses-api
- collection_type: open
  name: WanAPIs Unified AI Tasks API
  slug: open-wanapis-tasks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wanapis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wanapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wanapis.com/docs
- group: other
  title: ''
  type: ModelMarketplace
  url: https://wanapis.com/model
- group: commercial
  title: ''
  type: Pricing
  url: https://wanapis.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://wanapis.com/auth
created: '2026-05-27'
description: Developer-focused AI API gateway with an OpenAI-compatible endpoint. One API key gives access to GPT, Claude, Gemini, DeepSeek, image, video, and audio models behind a single unified surface. Platform includes a model marketplace, usage logs, quota management, transparent metering, multi-channel routing, and failover.
examples:
- key_count: 2
  name: Wanapis Chat Completion Example
  slug: wanapis-chat-completion-example
- key_count: 2
  name: Wanapis Embedding Example
  slug: wanapis-embedding-example
- key_count: 2
  name: Wanapis Image Generation Example
  slug: wanapis-image-generation-example
finops:
- name: Wanapis Finops
  service_category: AI Model Aggregation
  slug: wanapis-finops
image: https://wanapis.com/logo.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 15
  slug: wanapis-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 6
  slug: wanapis-chatcompletionresponse
- name: ChatMessage
  property_count: 5
  slug: wanapis-chatmessage
- name: EmbeddingRequest
  property_count: 5
  slug: wanapis-embeddingrequest
- name: ImageGenerationRequest
  property_count: 8
  slug: wanapis-imagerequest
jsonld:
- class_count: 31
  name: Wanapis Context
  property_count: 5
  slug: wanapis-context
layout: provider
modified: '2026-05-27'
name: WanAPIs
nav: Providers
network: true
overview: 'WanAPIs publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 5 more. Tagged areas include LLM Gateway, AI API Gateway, OpenAI-Compatible, Model Marketplace, and LLM.


  The WanAPIs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WanAPIs'' developer surface includes documentation, pricing, signup flow, and 3 more developer resources.'
plans:
- name: Wanapis Plans Pricing
  plan_count: 2
  slug: wanapis-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Wanapis Rate Limits
  slug: wanapis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WanAPIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wanapis-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: WanAPIs API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: wanapis-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 72.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 13.6
    contract_quality: 63.5
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 31.6
  previous_composite: 41.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wanapis/refs/heads/main/screenshots/wanapis-2026-06-20T201218.png
security:
- kind: domain-security
  name: Wanapis Domain Security
  slug: wanapis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wanapis
tags:
- LLM Gateway
- AI API Gateway
- OpenAI-Compatible
- Model Marketplace
- LLM
- GPT
- Claude
- Gemini
- DeepSeek
- Image-Generation
- Video Generation
- Audio
- Multi-Modal
- Routing
- Failover
website: https://wanapis.com/
---
