---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Doubao Agentic Access
  operation_count: 7
  slug: doubao-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 6
apis:
- description: OpenAI-compatible chat, responses, embedding, batch, image (Seedream), video (Seedance), 3D, and TTS APIs serving the Doubao model family. Base URL https://ark.cn-beijing.volces.com/api/v3. Includes t
  name: Volcano Engine Ark API
  slug: ark
- description: The Batch API from ByteDance Doubao — 1 operation(s) for batch.
  name: ByteDance Doubao Batch API
  slug: doubao-batch-api
- description: The Chat API from ByteDance Doubao — 1 operation(s) for chat.
  name: ByteDance Doubao Chat API
  slug: doubao-chat-api
- description: The Embeddings API from ByteDance Doubao — 1 operation(s) for embeddings.
  name: ByteDance Doubao Embeddings API
  slug: doubao-embeddings-api
- description: The Images API from ByteDance Doubao — 1 operation(s) for images.
  name: ByteDance Doubao Images API
  slug: doubao-images-api
- description: The Videos API from ByteDance Doubao — 2 operation(s) for videos.
  name: ByteDance Doubao Videos API
  slug: doubao-videos-api
artifact_total: 14
collections:
- collection_type: open
  name: Volcano Engine Ark API (Doubao)
  slug: open-doubao
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doubao-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doubao-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doubao-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doubao-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bytedance
- group: company
  title: ''
  type: Website
  url: https://www.volcengine.com/product/doubao
- group: docs
  title: ''
  type: Documentation
  url: https://www.volcengine.com/docs/82379
- group: commercial
  title: ''
  type: Plans
  url: plans/doubao-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doubao-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doubao-finops.yml
created: '2026-05-08'
description: Doubao is ByteDance's foundation model family, served via the Volcano Engine Ark platform. Offers chat completions, deep reasoning, multimodal vision, embeddings, image generation (Seedream), video generation (Seedance), 3D generation, and TTS through OpenAI-compatible and native endpoints.
finops:
- name: Doubao Finops
  service_category: AI and Machine Learning
  slug: doubao-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doubao.png
layout: provider
modified: '2026-05-08'
name: ByteDance Doubao
nav: Providers
network: true
overview: 'ByteDance Doubao publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Chat API, Embeddings API, and 2 more. Tagged areas include AI, LLM, Inference, ByteDance, and Multimodal.


  ByteDance Doubao''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Doubao Plans Pricing
  plan_count: 2
  slug: doubao-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Doubao Rate Limits
  slug: doubao-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.7
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doubao/refs/heads/main/screenshots/doubao-2026-06-20T180218.png
security:
- kind: authentication
  name: Doubao Authentication
  slug: doubao-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doubao Domain Security
  slug: doubao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doubao Vulnerability Disclosure
  slug: doubao-vulnerability-disclosure
  summary_line: disclosure policy published
slug: doubao
tags:
- AI
- LLM
- Inference
- ByteDance
- Multimodal
- Volcano Engine
website: https://www.volcengine.com/product/doubao
---
