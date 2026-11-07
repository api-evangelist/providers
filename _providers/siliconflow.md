---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: OpenAI- and Anthropic-compatible inference covering chat completions, messages, embeddings, reranking, image generation, video (Wan2.2), audio (speech, transcription, voice cloning, voice list), files
  name: SiliconFlow Cloud Platform API
  slug: platform
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Audio API from SiliconFlow — 4 operation(s) for audio.
  name: SiliconFlow Audio API
  slug: siliconflow-audio-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Completions API from SiliconFlow — 1 operation(s) for completions.
  name: SiliconFlow Completions API
  slug: siliconflow-completions-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Embeddings API from SiliconFlow — 1 operation(s) for embeddings.
  name: SiliconFlow Embeddings API
  slug: siliconflow-embeddings-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Images API from SiliconFlow — 1 operation(s) for images.
  name: SiliconFlow Images API
  slug: siliconflow-images-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Messages API from SiliconFlow — 1 operation(s) for messages.
  name: SiliconFlow Messages API
  slug: siliconflow-messages-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Models API from SiliconFlow — 1 operation(s) for models.
  name: SiliconFlow Models API
  slug: siliconflow-models-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Rerank API from SiliconFlow — 1 operation(s) for rerank.
  name: SiliconFlow Rerank API
  slug: siliconflow-rerank-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The User API from SiliconFlow — 1 operation(s) for user.
  name: SiliconFlow User API
  slug: siliconflow-user-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Videos API from SiliconFlow — 2 operation(s) for videos.
  name: SiliconFlow Videos API
  slug: siliconflow-videos-api
- baseURL: https://api.siliconflow.com/v1
  baseurl_source: declared
  description: The Chat Completions API from SiliconFlow — 1 operation(s) for chat completions.
  name: SiliconFlow Chat Completions API
  slug: siliconflow-chat-completions-api
artifact_total: 26
collections:
- collection_type: open
  name: SiliconFlow Cloud Platform Audio API
  slug: open-siliconflow-audio-api
- collection_type: open
  name: SiliconFlow Cloud Platform Chat API
  slug: open-siliconflow-chat-api
- collection_type: open
  name: SiliconFlow Cloud Platform Completions API
  slug: open-siliconflow-completions-api
- collection_type: open
  name: SiliconFlow Cloud Platform Embeddings API
  slug: open-siliconflow-embeddings-api
- collection_type: open
  name: SiliconFlow Cloud Platform Images API
  slug: open-siliconflow-images-api
- collection_type: open
  name: SiliconFlow Cloud Platform Messages API
  slug: open-siliconflow-messages-api
- collection_type: open
  name: SiliconFlow Cloud Platform Models API
  slug: open-siliconflow-models-api
- collection_type: open
  name: SiliconFlow Cloud Platform Rerank API
  slug: open-siliconflow-rerank-api
- collection_type: open
  name: SiliconFlow Cloud Platform User API
  slug: open-siliconflow-user-api
- collection_type: open
  name: SiliconFlow Cloud Platform Videos API
  slug: open-siliconflow-videos-api
common:
- group: auth
  href: https://artifacts.apis.io/siliconflow/security/siliconflow-domain-security.yml
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
  href: https://artifacts.apis.io/siliconflow/plans/siliconflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/siliconflow-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/siliconflow/rate-limits/siliconflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/siliconflow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/siliconflow/finops/siliconflow-finops.yml
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
- has_sources: true
  method: generated
  name: Siliconflow Finops
  primary_unit: ''
  service_category: AI
  slug: siliconflow-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siliconflow.png
layout: provider
modified: '2026-05-08'
name: SiliconFlow
nav: Providers
network: true
overview: 'SiliconFlow publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Completions API, Embeddings API, and 8 more. Tagged areas include Artificial Intelligence, LLM, Inference, Open Source, and OpenAI-Compatible.


  The SiliconFlow catalog on APIs.io includes 1 Spectral governance ruleset.


  SiliconFlow''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Siliconflow Plans Pricing
  plan_count: 1
  slug: siliconflow-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Siliconflow Rate Limits
  slug: siliconflow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: SiliconFlow API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: siliconflow-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 49.0
    developer_ergonomics: 19.0
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/siliconflow/siliconflow-2026-06-20T193920.png
security:
- kind: domain-security
  name: Siliconflow Domain Security
  slug: siliconflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: siliconflow
tags:
- Artificial Intelligence
- LLM
- Inference
- Open Source
- OpenAI-Compatible
- Anthropic Compatible
- Image Generation
- Audio
- Video
website: https://siliconflow.com/
---
