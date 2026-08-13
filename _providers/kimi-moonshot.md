---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kimi Moonshot Agentic Access
  operation_count: 13
  slug: kimi-moonshot-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 13
apis:
- description: OpenAI-compatible embeddings endpoint that returns vector representations of input text for semantic search, clustering, and retrieval-augmented generation workflows.
  name: Kimi Embeddings API
  slug: embeddings
- description: File management endpoint for uploading documents that can be referenced from chat completions (for example, long-document Q&A and the file_id-based context attachment pattern).
  name: Kimi Files API
  slug: files
- description: Fine-tuning jobs endpoint for customizing Moonshot base models on customer-supplied training data. Mirrors the OpenAI fine-tuning surface.
  name: Kimi Fine-Tuning API
  slug: fine-tuning
- description: Lists models available to the authenticated account and exposes per-model metadata (context window, modality support, pricing tier).
  name: Kimi Models API
  slug: models
- description: Helper endpoint exposed by the Moonshot platform for counting tokens against a given model's tokenizer prior to submission, useful for managing long-context budgets.
  name: Kimi Tokenizer API
  slug: tokenizer
- description: Consumer-facing AI assistant at kimi.com (also kimi.ai) powered by the Kimi models. Supports long-document upload, web search grounding, and tool use through a chat UI.
  name: Kimi Assistant (kimi.com)
  slug: assistant
- description: Open-weight Kimi model releases (for example prior Kimi K1 / K2 checkpoints) published under the MoonshotAI GitHub organization for research and self-hosted use.
  name: Moonshot Open-Weights Releases
  slug: open-weights
- description: The Batch API from Kimi (Moonshot AI) — 3 operation(s) for batch.
  name: Kimi (Moonshot AI) Batch API
  slug: kimi-moonshot-batch-api
- description: The Billing API from Kimi (Moonshot AI) — 1 operation(s) for billing.
  name: Kimi (Moonshot AI) Billing API
  slug: kimi-moonshot-billing-api
- description: The Chat API from Kimi (Moonshot AI) — 1 operation(s) for chat.
  name: Kimi (Moonshot AI) Chat API
  slug: kimi-moonshot-chat-api
- description: The Files API from Kimi (Moonshot AI) — 3 operation(s) for files.
  name: Kimi (Moonshot AI) Files API
  slug: kimi-moonshot-files-api
- description: The Models API from Kimi (Moonshot AI) — 1 operation(s) for models.
  name: Kimi (Moonshot AI) Models API
  slug: kimi-moonshot-models-api
- description: The Utilities API from Kimi (Moonshot AI) — 1 operation(s) for utilities.
  name: Kimi (Moonshot AI) Utilities API
  slug: kimi-moonshot-utilities-api
artifact_total: 22
asyncapis:
- description: 'AsyncAPI definition for Moonshot AI''s Kimi `POST /v1/chat/completions` streaming response channel. Moonshot''s chat completions surface is OpenAI-compatible. When the request body sets `"stream": true`'
  name: Kimi (Moonshot AI) Streaming Chat Completions API
  slug: kimi-moonshot-asyncapi
collections:
- collection_type: open
  name: Moonshot AI API
  slug: open-kimi-moonshot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kimi-moonshot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kimi-moonshot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kimi-moonshot-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.moonshot.cn/
- group: other
  title: ''
  type: Assistant
  url: https://kimi.com/
- group: other
  title: ''
  type: Platform
  url: https://platform.moonshot.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.moonshot.cn/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MoonshotAI
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/moonshotai
- group: company
  title: ''
  type: Blog
  url: https://www.kimi.com/blog
created: '2026-05-23'
description: Moonshot AI is a Beijing-based AI lab that develops the Kimi family of long-context multilingual large language models. The consumer assistant is available at kimi.com (and kimi.ai); the developer platform at platform.moonshot.cn (also platform.kimi.com / platform.kimi.ai) exposes an OpenAI-compatible REST API for chat completions, embeddings, file management, fine-tuning, and model listing. Kimi models advertise very long context windows (8K, 32K, 128K, with newer K2.x models pushing toward 256K) and the platform offers multimodal text, image, and video inputs on the flagship Kimi K2.x line. Open-source weights for prior Kimi releases live under the MoonshotAI GitHub organization.
finops:
- name: Kimi Moonshot Finops
  service_category: API
  slug: kimi-moonshot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kimi-moonshot.png
layout: provider
modified: '2026-05-29'
name: Kimi (Moonshot AI)
nav: Providers
network: true
overview: 'Kimi (Moonshot AI) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Billing API, Chat API, and 3 more. Tagged areas include LLM, Long Context, AI, OpenAI Compatible, and Multimodal.


  The Kimi (Moonshot AI) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kimi (Moonshot AI)''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Kimi Moonshot Plans Pricing
  plan_count: 1
  slug: kimi-moonshot-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 2
  name: Kimi Moonshot Rate Limits
  slug: kimi-moonshot-rate-limits
rules:
- name: Kimi (Moonshot AI) API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: kimi-moonshot-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kimi-moonshot/refs/heads/main/screenshots/kimi-moonshot-2026-06-20T184035.png
security:
- kind: authentication
  name: Kimi Moonshot Authentication
  slug: kimi-moonshot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kimi Moonshot Domain Security
  slug: kimi-moonshot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kimi-moonshot
tags:
- LLM
- Long Context
- AI
- OpenAI Compatible
- Multimodal
- China
website: https://www.moonshot.cn/
---
