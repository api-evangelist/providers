---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Litellm Agentic Access
  operation_count: 20
  slug: litellm-agentic-access
  summary_line: 20 operations · 20 acting
api_count: 33
apis:
- description: Provides an OpenAI-compatible /completions endpoint for text completion requests routed through the LiteLLM proxy to supported LLM providers.
  name: LiteLLM Completions API
  slug: completions-api
- description: Provides an OpenAI-compatible /responses endpoint supporting the Responses API specification, including conversation history compression via /responses/compact.
  name: LiteLLM Responses API
  slug: responses-api
- description: Provides an OpenAI-compatible /embeddings endpoint for generating text embeddings across multiple providers including OpenAI, Cohere, HuggingFace, and Bedrock with unified formatting.
  name: LiteLLM Embeddings API
  slug: embeddings-api
- description: Provides OpenAI-compatible /images/generations, /images/edits, and /images/variations endpoints for image generation and manipulation routed through the LiteLLM proxy.
  name: LiteLLM Image Generation API
  slug: image-generation-api
- description: Provides OpenAI-compatible /audio/transcriptions and /audio/speech endpoints for audio transcription and text-to-speech conversion across supported providers.
  name: LiteLLM Audio API
  slug: audio-api
- description: Provides an OpenAI-compatible /moderations endpoint for content moderation across supported providers through the LiteLLM proxy.
  name: LiteLLM Moderations API
  slug: moderations-api
- description: Provides an OpenAI-compatible /batches endpoint for batch processing operations, enabling bulk request handling across LLM providers.
  name: LiteLLM Batches API
  slug: batches-api
- description: Provides an OpenAI-compatible /files endpoint for file management operations used in conjunction with fine-tuning and batch processing.
  name: LiteLLM Files API
  slug: files-api
- description: Provides an OpenAI-compatible /fine_tuning endpoint for model fine-tuning operations across supported providers through the LiteLLM proxy.
  name: LiteLLM Fine-Tuning API
  slug: fine-tuning-api
- description: Provides a /rerank endpoint for document reranking operations, supporting providers like Cohere through the LiteLLM proxy with a unified interface.
  name: LiteLLM Rerank API
  slug: rerank-api
- description: Provides /vector_stores endpoints for creating and managing vector stores, file operations within vector stores, and search functionality for retrieval-augmented generation (RAG) use cases.
  name: LiteLLM Vector Stores API
  slug: vector-stores-api
- description: Provides Anthropic-compatible /v1/messages and /v1/messages/count_tokens endpoints for native Anthropic API format support through the LiteLLM proxy.
  name: LiteLLM Anthropic Messages API
  slug: messages-api
- description: Provides /realtime WebSocket endpoints for real-time model interactions with load balancing and guardrails support across providers.
  name: LiteLLM Realtime API
  slug: realtime-api
- description: Provides /mcp endpoints for Model Context Protocol (MCP) integration, enabling LLMs to interact with external tools and APIs through OpenAPI specifications.
  name: LiteLLM MCP API
  slug: mcp-api
- description: Provides an /ocr endpoint for optical character recognition, enabling text extraction from images through supported providers via the LiteLLM proxy.
  name: LiteLLM OCR API
  slug: ocr-api
- description: Provides /guardrails/apply_guardrail endpoint for applying configured content filtering and safety guardrails to LLM requests and responses.
  name: LiteLLM Guardrails API
  slug: guardrails-api
- description: Provides /evals endpoints for the Evaluations API, enabling measurement and benchmarking of model performance through the LiteLLM proxy.
  name: LiteLLM Evals API
  slug: evals-api
- description: Provides /a2a endpoints for the Agent-to-Agent (A2A) gateway, enabling agent registration, publishing, and inter-agent communication.
  name: LiteLLM A2A Agent Gateway API
  slug: a2a-api
- description: Provides /videos endpoints for video generation and handling through supported providers like RunwayML via the LiteLLM proxy.
  name: LiteLLM Videos API
  slug: videos-api
- description: The Assistants API from LiteLLM — 1 operation(s) for assistants.
  name: LiteLLM Assistants API
  slug: litellm-assistants-api
- description: The Audio API from LiteLLM — 2 operation(s) for audio.
  name: LiteLLM Audio API
  slug: litellm-audio-api
- description: The Batches API from LiteLLM — 1 operation(s) for batches.
  name: LiteLLM Batches API
  slug: litellm-batches-api
- description: The Chat API from LiteLLM — 1 operation(s) for chat.
  name: LiteLLM Chat API
  slug: litellm-chat-api
- description: The Completions API from LiteLLM — 1 operation(s) for completions.
  name: LiteLLM Completions API
  slug: litellm-completions-api
- description: The Embeddings API from LiteLLM — 1 operation(s) for embeddings.
  name: LiteLLM Embeddings API
  slug: litellm-embeddings-api
- description: The Fine Tuning API from LiteLLM — 1 operation(s) for fine tuning.
  name: LiteLLM Fine Tuning API
  slug: litellm-fine-tuning-api
- description: The Images API from LiteLLM — 3 operation(s) for images.
  name: LiteLLM Images API
  slug: litellm-images-api
- description: The Messages API from LiteLLM — 2 operation(s) for messages.
  name: LiteLLM Messages API
  slug: litellm-messages-api
- description: The Moderations API from LiteLLM — 1 operation(s) for moderations.
  name: LiteLLM Moderations API
  slug: litellm-moderations-api
- description: The Ocr API from LiteLLM — 1 operation(s) for ocr.
  name: LiteLLM Ocr API
  slug: litellm-ocr-api
- description: The Rag API from LiteLLM — 2 operation(s) for rag.
  name: LiteLLM Rag API
  slug: litellm-rag-api
- description: The Rerank API from LiteLLM — 1 operation(s) for rerank.
  name: LiteLLM Rerank API
  slug: litellm-rerank-api
- description: The Vector Stores API from LiteLLM — 2 operation(s) for vector stores.
  name: LiteLLM Vector Stores API
  slug: litellm-vector-stores-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LiteLLM Proxy Assistants API
  slug: open-litellm-assistants-api
- collection_type: open
  name: LiteLLM Proxy Assistants Audio API
  slug: open-litellm-audio-api
- collection_type: open
  name: LiteLLM Proxy Assistants Batches API
  slug: open-litellm-batches-api
- collection_type: open
  name: LiteLLM Proxy Assistants Chat API
  slug: open-litellm-chat-api
- collection_type: open
  name: LiteLLM Proxy Assistants Completions API
  slug: open-litellm-completions-api
- collection_type: open
  name: LiteLLM Proxy Assistants Embeddings API
  slug: open-litellm-embeddings-api
- collection_type: open
  name: LiteLLM Proxy Assistants Fine Tuning API
  slug: open-litellm-fine-tuning-api
- collection_type: open
  name: LiteLLM Proxy Assistants Images API
  slug: open-litellm-images-api
- collection_type: open
  name: LiteLLM Proxy Assistants Messages API
  slug: open-litellm-messages-api
- collection_type: open
  name: LiteLLM Proxy Assistants Moderations API
  slug: open-litellm-moderations-api
- collection_type: open
  name: LiteLLM Proxy Assistants Ocr API
  slug: open-litellm-ocr-api
- collection_type: open
  name: LiteLLM Proxy Assistants Rag API
  slug: open-litellm-rag-api
- collection_type: open
  name: LiteLLM Proxy Assistants Rerank API
  slug: open-litellm-rerank-api
- collection_type: open
  name: LiteLLM Proxy Assistants Vector Stores API
  slug: open-litellm-vector-stores-api
- collection_type: open
  name: LiteLLM Proxy API
  slug: open-litellm
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/litellm-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/litellm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litellm-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/litellm
- group: start
  title: ''
  type: Portal
  url: https://www.litellm.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.litellm.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.litellm.ai/docs/proxy/quick_start
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/BerriAI/litellm
- group: company
  title: ''
  type: Blog
  url: https://docs.litellm.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.litellm.ai/changelog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.litellm.ai/release_notes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.litellm.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.litellm.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.litellm.ai/docs/enterprise
- group: other
  title: ''
  type: Dashboard
  url: https://admin.litellm.ai/
- group: other
  title: ''
  type: Providers
  url: https://docs.litellm.ai/docs/providers
- group: other
  title: ''
  type: Models
  url: https://models.litellm.ai/
- group: other
  title: ''
  type: Configuration
  url: https://docs.litellm.ai/docs/proxy/configs
- group: auth
  title: ''
  type: Authentication
  url: https://docs.litellm.ai/docs/set_keys
- group: other
  title: ''
  type: Guardrails
  url: https://docs.litellm.ai/docs/apply_guardrail
- group: other
  title: ''
  type: Enterprise
  url: https://docs.litellm.ai/docs/proxy/enterprise
- group: operate
  title: ''
  type: ReleaseCycle
  url: https://docs.litellm.ai/docs/proxy/release_cycle
- group: other
  title: ''
  type: SSO
  url: https://docs.litellm.ai/docs/proxy/admin_ui_sso
- group: other
  title: ''
  type: Docker
  url: https://docs.litellm.ai/docs/proxy/docker_quick_start
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/litellm/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.litellm.ai/llms.txt
created: '2026-03-03'
description: LiteLLM is an open-source Python SDK and proxy server providing a unified OpenAI-compatible interface to 100+ LLM providers.
finops:
- name: Litellm Finops
  service_category: API
  slug: litellm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litellm.png
layout: provider
modified: '2026-05-19'
name: LiteLLM
nav: Providers
network: true
overview: 'LiteLLM publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Assistants API, Audio API, Batches API, and 11 more. Tagged areas include Gateways.


  LiteLLM''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, changelog, release notes, support, and 19 more developer resources.'
plans:
- name: Litellm Plans Pricing
  plan_count: 3
  slug: litellm-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Litellm Rate Limits
  slug: litellm-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 37.4
    developer_ergonomics: 50.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litellm/refs/heads/main/screenshots/litellm-2026-06-20T184603.png
security:
- kind: domain-security
  name: Litellm Domain Security
  slug: litellm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: litellm
tags:
- Gateways
website: https://www.litellm.ai/
---
