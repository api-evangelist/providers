---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deepinfra Agentic Access
  operation_count: 9
  slug: deepinfra-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 7
apis:
- description: OpenAI- and Anthropic-compatible inference API for 100+ open-source models. Surfaces include chat completions, anthropic messages, embeddings, reranking, audio (speech/transcriptions/translations), im
  name: DeepInfra Platform API
  slug: platform
- description: The Audio API from DeepInfra — 3 operation(s) for audio.
  name: DeepInfra Audio API
  slug: deepinfra-audio-api
- description: The Chat API from DeepInfra — 1 operation(s) for chat.
  name: DeepInfra Chat API
  slug: deepinfra-chat-api
- description: The Completions API from DeepInfra — 1 operation(s) for completions.
  name: DeepInfra Completions API
  slug: deepinfra-completions-api
- description: The Embeddings API from DeepInfra — 1 operation(s) for embeddings.
  name: DeepInfra Embeddings API
  slug: deepinfra-embeddings-api
- description: The Images API from DeepInfra — 1 operation(s) for images.
  name: DeepInfra Images API
  slug: deepinfra-images-api
- description: The Models API from DeepInfra — 2 operation(s) for models.
  name: DeepInfra Models API
  slug: deepinfra-models-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DeepInfra Inference Audio API
  slug: open-deepinfra-audio-api
- collection_type: open
  name: DeepInfra Inference Audio Chat API
  slug: open-deepinfra-chat-api
- collection_type: open
  name: DeepInfra Inference Audio Completions API
  slug: open-deepinfra-completions-api
- collection_type: open
  name: DeepInfra Inference Audio Embeddings API
  slug: open-deepinfra-embeddings-api
- collection_type: open
  name: DeepInfra Inference Audio Images API
  slug: open-deepinfra-images-api
- collection_type: open
  name: DeepInfra Inference Audio Models API
  slug: open-deepinfra-models-api
- collection_type: open
  name: DeepInfra Inference API
  slug: open-deepinfra
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepinfra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/deepinfra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepinfra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepinfra-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepinfra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deep-infra
- group: company
  title: ''
  type: Website
  url: https://deepinfra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deepinfra.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/deepinfra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepinfra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deepinfra-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.deepinfra.com/llms.txt
created: '2026-05-08'
description: DeepInfra is a serverless inference platform for open-source models. Hosts 100+ LLMs (Llama, Qwen, DeepSeek, Mixtral) plus image (Flux, Stable Diffusion), video, audio (Whisper, TTS, Voxtral), embeddings/reranking, and vision/OCR models. Includes fine-tuning, dedicated GPU rentals, and private deployments. OpenAI- and Anthropic- compatible endpoints.
finops:
- name: Deepinfra Finops
  service_category: AI
  slug: deepinfra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepinfra.png
layout: provider
modified: '2026-05-08'
name: DeepInfra
nav: Providers
network: true
overview: 'DeepInfra publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Completions API, and 3 more. Tagged areas include Artificial Intelligence, LLM, Inference, Serverless, and Open-Source.


  DeepInfra''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Deepinfra Plans Pricing
  plan_count: 1
  slug: deepinfra-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Deepinfra Rate Limits
  slug: deepinfra-rate-limits
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 46.2
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepinfra/refs/heads/main/screenshots/deepinfra-2026-06-20T175818.png
security:
- kind: authentication
  name: Deepinfra Authentication
  slug: deepinfra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepinfra Domain Security
  slug: deepinfra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Deepinfra Trust Center
  slug: deepinfra-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: deepinfra
tags:
- Artificial Intelligence
- LLM
- Inference
- Serverless
- Open-Source
- OpenAI-Compatible
- Anthropic Compatible
- Image-Generation
- Audio
- Embeddings
website: https://deepinfra.com/
---
