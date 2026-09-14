---
access_model:
  confidence: medium
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
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Qwen Agentic Access
  operation_count: 3
  slug: qwen-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Native Alibaba Cloud Model Studio API serving the Qwen model family. Provides chat completions, multimodal vision, embeddings, audio (TTS/ASR), image generation, video generation, function calling, an
  name: DashScope (Alibaba Cloud Model Studio) API
  slug: dashscope
- baseURL: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  baseurl_source: declared
  description: The Chat API from Qwen — 1 operation(s) for chat.
  name: Qwen Chat API
  slug: qwen-chat-api
- baseURL: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  baseurl_source: declared
  description: The Embeddings API from Qwen — 1 operation(s) for embeddings.
  name: Qwen Embeddings API
  slug: qwen-embeddings-api
- baseURL: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
  baseurl_source: declared
  description: The Models API from Qwen — 1 operation(s) for models.
  name: Qwen Models API
  slug: qwen-models-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qwen via Alibaba Cloud Model Studio (DashScope) Chat API
  slug: open-qwen-chat-api
- collection_type: open
  name: Qwen via Alibaba Cloud Model Studio (DashScope) Chat Embeddings API
  slug: open-qwen-embeddings-api
- collection_type: open
  name: Qwen via Alibaba Cloud Model Studio (DashScope) Chat Models API
  slug: open-qwen-models-api
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
overview: 'Qwen publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat API, Embeddings API, and Models API. Tagged areas include Artificial Intelligence, LLM, Inference, Open-Source, and Alibaba.


  Qwen''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Qwen Plans Pricing
  plan_count: 3
  slug: qwen-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Qwen Rate Limits
  slug: qwen-rate-limits
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
- Artificial Intelligence
- LLM
- Inference
- Open-Source
- Alibaba
- Multi-Modal
website: https://qwen.ai/
---
