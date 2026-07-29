---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Qwen Agentic Access
  operation_count: 3
  slug: qwen-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: Native Alibaba Cloud Model Studio API serving the Qwen model family. Provides chat completions, multimodal vision, embeddings, audio (TTS/ASR), image generation, video generation, function calling, an
  name: DashScope (Alibaba Cloud Model Studio) API
  slug: dashscope
- description: The Chat API from Qwen — 1 operation(s) for chat.
  name: Qwen Chat API
  slug: qwen-chat-api
- description: The Embeddings API from Qwen — 1 operation(s) for embeddings.
  name: Qwen Embeddings API
  slug: qwen-embeddings-api
- description: The Models API from Qwen — 1 operation(s) for models.
  name: Qwen Models API
  slug: qwen-models-api
artifact_total: 11
collections:
- collection_type: open
  name: Qwen via Alibaba Cloud Model Studio (DashScope)
  slug: open-qwen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qwen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwen-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qwen
- group: company
  title: ''
  type: Website
  url: https://qwen.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alibabacloud.com/help/en/model-studio
- group: build
  title: ''
  type: GitHub
  url: https://github.com/QwenLM
- group: commercial
  title: ''
  type: Plans
  url: plans/qwen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qwen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qwen-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://qwenlm.github.io/blog/index.xml
created: '2026-05-08'
description: Qwen is Alibaba's large language model family, including Qwen3-Max, Qwen3.5-Plus, Qwen3.5-Flash, Qwen3-VL (vision), Qwen-Coder, Qwen-Audio, and Qwen open-source weights. APIs are exposed via Alibaba Cloud Model Studio (DashScope) with per-token pricing across multiple regions. The qwen.ai consumer site fronts the chat product.
finops:
- name: Qwen Finops
  service_category: AI and Machine Learning
  slug: qwen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qwen.png
layout: provider
modified: '2026-05-08'
name: Qwen
nav: Providers
network: true
overview: 'Qwen publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat API, Embeddings API, and Models API. Tagged areas include AI, LLM, Inference, Open Source, and Alibaba.


  Qwen''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Qwen Plans Pricing
  plan_count: 3
  slug: qwen-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 3
  name: Qwen Rate Limits
  slug: qwen-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qwen/refs/heads/main/screenshots/qwen-2026-06-20T192458.png
security:
- kind: authentication
  name: Qwen Authentication
  slug: qwen-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qwen Domain Security
  slug: qwen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qwen
tags:
- AI
- LLM
- Inference
- Open Source
- Alibaba
- Multimodal
website: https://qwen.ai/
---
