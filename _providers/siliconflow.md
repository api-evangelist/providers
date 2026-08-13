---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 11
apis:
- description: OpenAI- and Anthropic-compatible inference covering chat completions, messages, embeddings, reranking, image generation, video (Wan2.2), audio (speech, transcription, voice cloning, voice list), files
  name: SiliconFlow Cloud Platform API
  slug: platform
- description: The Audio API from SiliconFlow — 4 operation(s) for audio.
  name: SiliconFlow Audio API
  slug: siliconflow-audio-api
- description: The Chat API from SiliconFlow — 1 operation(s) for chat.
  name: SiliconFlow Chat API
  slug: siliconflow-chat-api
- description: The Completions API from SiliconFlow — 1 operation(s) for completions.
  name: SiliconFlow Completions API
  slug: siliconflow-completions-api
- description: The Embeddings API from SiliconFlow — 1 operation(s) for embeddings.
  name: SiliconFlow Embeddings API
  slug: siliconflow-embeddings-api
- description: The Images API from SiliconFlow — 1 operation(s) for images.
  name: SiliconFlow Images API
  slug: siliconflow-images-api
- description: The Messages API from SiliconFlow — 1 operation(s) for messages.
  name: SiliconFlow Messages API
  slug: siliconflow-messages-api
- description: The Models API from SiliconFlow — 1 operation(s) for models.
  name: SiliconFlow Models API
  slug: siliconflow-models-api
- description: The Rerank API from SiliconFlow — 1 operation(s) for rerank.
  name: SiliconFlow Rerank API
  slug: siliconflow-rerank-api
- description: The User API from SiliconFlow — 1 operation(s) for user.
  name: SiliconFlow User API
  slug: siliconflow-user-api
- description: The Videos API from SiliconFlow — 2 operation(s) for videos.
  name: SiliconFlow Videos API
  slug: siliconflow-videos-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siliconflow-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/siliconflow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siliconflow
- group: company
  title: ''
  type: Website
  url: https://siliconflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siliconflow.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/siliconflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/siliconflow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/siliconflow-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.siliconflow.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://siliconflow.com/blog
created: '2026-05-08'
description: SiliconFlow is an AI inference cloud serving a broad catalog of open-source models with OpenAI- and Anthropic-compatible APIs. Hosts DeepSeek-R1/V3, Qwen3-Coder, GLM-4.6V, Kimi-K2, MiniMax-M1-80k, gpt-oss-120b, Llama 3.3 70B, FLUX 1.1 Pro, Wan2.2 (video), CosyVoice2 and Fish-Speech (audio). Surfaces include chat, completions, embeddings, reranking, image, video, audio (speech + transcription + voice cloning), files, fine-tuning, and batch.
finops:
- name: Siliconflow Finops
  service_category: AI
  slug: siliconflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siliconflow.png
layout: provider
modified: '2026-05-08'
name: SiliconFlow
nav: Providers
network: true
overview: 'SiliconFlow publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 7 more. Tagged areas include AI, LLM, Inference, Open Source, and OpenAI Compatible.


  SiliconFlow''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Siliconflow Plans Pricing
  plan_count: 1
  slug: siliconflow-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 1
  name: Siliconflow Rate Limits
  slug: siliconflow-rate-limits
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 59.7
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siliconflow/refs/heads/main/screenshots/siliconflow-2026-06-20T193920.png
security:
- kind: domain-security
  name: Siliconflow Domain Security
  slug: siliconflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: siliconflow
tags:
- AI
- LLM
- Inference
- Open Source
- OpenAI Compatible
- Anthropic Compatible
- Image Generation
- Audio
- Video
website: https://siliconflow.com/
---
