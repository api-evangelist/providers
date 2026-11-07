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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deepinfra Agentic Access
  operation_count: 9
  slug: deepinfra-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 2
apis:
- description: OpenAI- and Anthropic-compatible inference API for 100+ open-source models. Surfaces include chat completions, anthropic messages, embeddings, reranking, audio (speech/transcriptions/translations), im
  name: DeepInfra Platform API
  slug: platform
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Audio API from DeepInfra — 3 operation(s) for audio.
  name: DeepInfra Audio API
  slug: deepinfra-audio-api
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Completions API from DeepInfra — 1 operation(s) for completions.
  name: DeepInfra Completions API
  slug: deepinfra-completions-api
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Embeddings API from DeepInfra — 1 operation(s) for embeddings.
  name: DeepInfra Embeddings API
  slug: deepinfra-embeddings-api
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Images API from DeepInfra — 1 operation(s) for images.
  name: DeepInfra Images API
  slug: deepinfra-images-api
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Models API from DeepInfra — 2 operation(s) for models.
  name: DeepInfra Models API
  slug: deepinfra-models-api
- baseURL: https://api.deepinfra.com/v1/openai
  baseurl_source: declared
  description: The Chat Completions API from DeepInfra — 1 operation(s) for chat completions.
  name: DeepInfra Chat Completions API
  slug: deepinfra-chat-completions-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: User profile, team management, rate limits, and GPU pool limits.
  name: DeepInfra Account API
  slug: deepinfra-account-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Manage agent-framework instances (OpenClaw and friends).
  name: DeepInfra Agents API
  slug: deepinfra-agents-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: API tokens, SSH keys, scoped JWTs, and login flows.
  name: DeepInfra Authentication API
  slug: deepinfra-authentication-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Payment methods, usage tracking, and billing.
  name: DeepInfra Billing API
  slug: deepinfra-billing-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: The Decisions API from DeepInfra — 2 operation(s) for decisions.
  name: DeepInfra Decisions API
  slug: deepinfra-decisions-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Deploy and manage private model instances with autoscaling.
  name: DeepInfra Dedicated Models API
  slug: deepinfra-dedicated-models-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: File uploads and batch processing.
  name: DeepInfra Files & Batches API
  slug: deepinfra-files-batches-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Rent dedicated GPU containers.
  name: DeepInfra GPU Rentals API
  slug: deepinfra-gpu-rentals-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Generate, edit, and create variations of images.
  name: DeepInfra Image Generation API
  slug: deepinfra-image-generation-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Native DeepInfra inference API for models and deployments.
  name: DeepInfra Inference API
  slug: deepinfra-inference-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Query inference logs, deployment logs, and usage metrics.
  name: DeepInfra Logs & Metrics API
  slug: deepinfra-logs-metrics-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Create, manage, and query LoRA adapter models.
  name: DeepInfra LoRA Adapters API
  slug: deepinfra-lora-adapters-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: The Responses API from DeepInfra — 2 operation(s) for responses.
  name: DeepInfra Responses API
  slug: deepinfra-responses-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Create and manage isolated sandbox environments.
  name: DeepInfra Sandboxes API
  slug: deepinfra-sandboxes-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: OpenAI-compatible text completion endpoints.
  name: DeepInfra Text Completions API
  slug: deepinfra-text-completions-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: ElevenLabs-compatible TTS endpoints and voice management.
  name: DeepInfra Text to Speech API
  slug: deepinfra-text-to-speech-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: The Tokenizer API from DeepInfra — 2 operation(s) for tokenizer.
  name: DeepInfra Tokenizer API
  slug: deepinfra-tokenizer-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: Feedback submission and CLI version.
  name: DeepInfra Utilities API
  slug: deepinfra-utilities-api
- baseURL: https://api.deepinfra.com
  baseurl_source: declared
  description: The Videos API from DeepInfra — 6 operation(s) for videos.
  name: DeepInfra Videos API
  slug: deepinfra-videos-api
artifact_total: 41
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://deepinfra.com/blog
- group: agent
  href: https://artifacts.apis.io/deepinfra/agentic-access/deepinfra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepinfra-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/deepinfra/security/deepinfra-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deepinfra-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deepinfra/security/deepinfra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepinfra-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/deepinfra/authentication/deepinfra-authentication.yml
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
  href: https://artifacts.apis.io/deepinfra/plans/deepinfra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepinfra-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deepinfra/rate-limits/deepinfra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deepinfra-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deepinfra/finops/deepinfra-finops.yml
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
- has_sources: true
  method: generated
  name: Deepinfra Finops
  primary_unit: ''
  service_category: AI
  slug: deepinfra-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepinfra.png
layout: provider
modified: '2026-10-06'
name: DeepInfra
nav: Providers
network: true
overview: 'DeepInfra publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Completions API, Embeddings API, and 23 more. Tagged areas include Artificial Intelligence, LLM, Inference, Serverless, and Open Source.


  The DeepInfra catalog on APIs.io includes 1 Spectral governance ruleset.


  DeepInfra''s developer surface includes engineering blog, authentication, documentation, and 10 more developer resources.'
plans:
- name: Deepinfra Plans Pricing
  plan_count: 1
  slug: deepinfra-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Deepinfra Rate Limits
  slug: deepinfra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: DeepInfra API Rules
  rule_count: 54
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 18
  slug: deepinfra-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/deepinfra/deepinfra-2026-06-20T175818.png
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
- Open Source
- OpenAI-Compatible
- Anthropic Compatible
- Image Generation
- Audio
- Embeddings
website: https://deepinfra.com/
---
