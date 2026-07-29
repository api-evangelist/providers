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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: OpenAI-compatible REST API gateway aggregating GPT, Claude, Gemini, DeepSeek, plus image, video, and audio model providers behind a single key and routing/failover layer. Model marketplace, usage logs
  name: WanAPIs Unified AI API
  slug: wanapis-unified-ai-api
artifact_total: 16
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
overview: 'WanAPIs publishes 1 API on the [APIs.io](https://apis.io/) network: Unified AI API. Tagged areas include LLM Gateway, AI API Gateway, OpenAI Compatible, Model Marketplace, and LLM.


  The WanAPIs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WanAPIs'' developer surface includes documentation, pricing, signup flow, and 3 more developer resources.'
plans:
- name: Wanapis Plans Pricing
  plan_count: 2
  slug: wanapis-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 4
  name: Wanapis Rate Limits
  slug: wanapis-rate-limits
rules:
- name: WanAPIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wanapis-jsonschema-spectral-rules
- name: WanAPIs API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: wanapis-rules
score:
  band: thin
  composite: 41.6
  delta: -3.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.2
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 45.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- OpenAI Compatible
- Model Marketplace
- LLM
- GPT
- Claude
- Gemini
- DeepSeek
- Image Generation
- Video Generation
- Audio
- Multimodal
- Routing
- Failover
website: https://wanapis.com/
---
