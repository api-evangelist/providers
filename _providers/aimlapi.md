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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Aimlapi Agentic Access
  operation_count: 21
  slug: aimlapi-agentic-access
  summary_line: 21 operations · 14 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: '## **Creating an API Key** To create a new API key Sign-ip to [app.aimlapi.com](https://app.aimlapi.com), navigate to Key Management page and create an API Key Note that your Keys only work with an Ac'
  name: AIMLAPI API Key Management API
  slug: aimlapi-api-key-management-api
- description: The Assistants API from AIMLAPI — 2 operation(s) for assistants.
  name: AIMLAPI Assistants API
  slug: aimlapi-assistants-api
- description: The Chat API from AIMLAPI — 1 operation(s) for chat.
  name: AIMLAPI Chat API
  slug: aimlapi-chat-api
- description: Given a prompt and/or an input image, the model will generate a new image.
  name: AIMLAPI Images API
  slug: aimlapi-images-api
- description: List and describe the various models available in the API. You can refer to the [Models](https://aimlapi.com/models) documentation to understand what models are available and the differences between t
  name: AIMLAPI Models API
  slug: aimlapi-models-api
- description: The Threads API from AIMLAPI — 1 operation(s) for threads.
  name: AIMLAPI Threads API
  slug: aimlapi-threads-api
- description: The Threads > Messages API from AIMLAPI — 2 operation(s) for threads > messages.
  name: AIMLAPI Threads > Messages API
  slug: aimlapi-threads-messages-api
- description: The Threads > Runs API from AIMLAPI — 2 operation(s) for threads > runs.
  name: AIMLAPI Threads > Runs API
  slug: aimlapi-threads-runs-api
- description: The Voice API from AIMLAPI — 2 operation(s) for voice.
  name: AIMLAPI Voice API
  slug: aimlapi-voice-api
- description: The [WIP] Completions API from AIMLAPI — 1 operation(s) for [wip] completions.
  name: AIMLAPI [WIP] Completions API
  slug: aimlapi-wip-completions-api
artifact_total: 64
collections:
- collection_type: open
  name: AIMLAPI AI/ML API Documentation
  slug: open-aimlapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aimlapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aimlapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aimlapi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aimlapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aimlapi
- group: company
  title: ''
  type: Blog
  url: https://aimlapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aimlapi.com/ai-ml-api-pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aimlapi.com/
- group: operate
  title: ''
  type: FAQ
  url: https://docs.aimlapi.com/faq/can-i-use-api-in-python
- group: operate
  title: ''
  type: ChangeLog
  url: https://aimlapi.com/changelog
- group: start
  title: ''
  type: Signup
  url: https://aimlapi.com/app/sign-up/
- group: other
  title: ''
  type: Affiliate
  url: https://aimlapi.com/affiliate
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimlapi.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimlapi.com/terms-and-conditions
- group: design
  title: ''
  type: SpectralRules
  url: rules/aimlapi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aimlapi-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://aimlapi.com/llms.txt
created: '2025-01-07'
description: AIMLAPI is a unified AI model API gateway providing access to 400+ state-of-the-art AI models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ other providers through a single OpenAI-compatible API. Supported modalities include text/chat LLMs, image generation, video generation, music generation, speech-to-text, text-to-speech, vision/OCR, embeddings, and 3D generation.
examples:
- key_count: 5
  name: Aimlapi Api Key Example
  slug: aimlapi-api-key-example
- key_count: 8
  name: Aimlapi Chat Completion Request Example
  slug: aimlapi-chat-completion-request-example
- key_count: 6
  name: Aimlapi Chat Completion Response Example
  slug: aimlapi-chat-completion-response-example
- key_count: 4
  name: Aimlapi Embedding Request Example
  slug: aimlapi-embedding-request-example
- key_count: 6
  name: Aimlapi Image Generation Request Example
  slug: aimlapi-image-generation-request-example
- key_count: 3
  name: Aimlapi Message Example
  slug: aimlapi-message-example
- key_count: 4
  name: Aimlapi Model Info Example
  slug: aimlapi-model-info-example
features:
- description: Access to 400+ models from OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, Stability AI, and 40+ providers.
  name: 400+ AI Models
- description: Drop-in replacement for OpenAI API — use existing OpenAI client libraries with AIMLAPI endpoint.
  name: OpenAI-Compatible API
- description: Chat completions, completion, function calling, streaming, reasoning, and code generation.
  name: Text and Chat Completions
- description: Generate images via DALL-E, Flux, Stable Diffusion, and other image generation models.
  name: Image Generation
- description: Generate video via Sora 2, Runway, and other video generation models.
  name: Video Generation
- description: Text-to-speech and speech-to-text transcription via Whisper and other speech models.
  name: Speech Models
- description: AI music generation via dedicated music models.
  name: Music Generation
- description: Image understanding, visual question answering, and OCR via vision-capable LLMs.
  name: Vision and OCR
- description: Generate vector embeddings for semantic search and RAG applications.
  name: Embeddings
- description: Online playground for experimenting with all available models without writing code.
  name: Playground
finops:
- name: Aimlapi Finops
  service_category: API
  slug: aimlapi-finops
graphqls:
- description: AIMLAPI is an AI model aggregation API providing access to 200+ AI models including GPT-4, Claude, Llama, Stable Diffusion, Midjourney, and more through a single OpenAI-compatible endpoint.
  name: AIMLAPI GraphQL API
  slug: aimlapi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aimlapi.png
integrations:
- description: Use the official OpenAI Python and Node.js SDKs with AIMLAPI base URL.
  name: OpenAI SDK
- description: Integrate AIMLAPI models with LangChain for agentic AI workflows.
  name: LangChain
- description: Use AIMLAPI with LlamaIndex for RAG and document intelligence pipelines.
  name: LlamaIndex
- description: Build AI-powered web apps using Vercel AI SDK with AIMLAPI as backend.
  name: Vercel AI SDK
- description: Native Python integration via requests library or OpenAI client.
  name: Python
- description: Node.js integration via OpenAI npm package pointed at AIMLAPI endpoint.
  name: Node.js
json_schemas:
- name: ApiKey
  property_count: 5
  slug: aimlapi-api-key
- name: ChatCompletionRequest
  property_count: 8
  slug: aimlapi-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: aimlapi-chat-completion-response
- name: EmbeddingRequest
  property_count: 4
  slug: aimlapi-embedding-request
- name: ImageGenerationRequest
  property_count: 6
  slug: aimlapi-image-generation-request
- name: Message
  property_count: 3
  slug: aimlapi-message
- name: ModelInfo
  property_count: 4
  slug: aimlapi-model-info
json_structures:
- name: Aimlapi Api Key Structure
  property_count: 5
  slug: aimlapi-api-key-structure
- name: Aimlapi Chat Completion Request Structure
  property_count: 8
  slug: aimlapi-chat-completion-request-structure
- name: Aimlapi Chat Completion Response Structure
  property_count: 6
  slug: aimlapi-chat-completion-response-structure
- name: Aimlapi Embedding Request Structure
  property_count: 4
  slug: aimlapi-embedding-request-structure
- name: Aimlapi Image Generation Request Structure
  property_count: 6
  slug: aimlapi-image-generation-request-structure
- name: Aimlapi Message Structure
  property_count: 3
  slug: aimlapi-message-structure
- name: Aimlapi Model Info Structure
  property_count: 4
  slug: aimlapi-model-info-structure
jsonld:
- class_count: 5
  name: Aimlapi Context
  property_count: 10
  slug: aimlapi-context
layout: provider
modified: '2026-04-19'
name: AIMLAPI
nav: Providers
network: true
overview: 'AIMLAPI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including API Key Management API, Assistants API, Chat API, and 7 more. Tagged areas include Artificial Intelligence, Machine Learning, AI Models, LLM, and Image Generation.


  The AIMLAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AIMLAPI''s developer surface includes authentication, engineering blog, pricing, documentation, FAQ, changelog, signup flow, and 10 more developer resources.'
plans:
- name: Aimlapi Plans Pricing
  plan_count: 3
  slug: aimlapi-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Aimlapi Rate Limits
  slug: aimlapi-rate-limits
rules:
- name: AIMLAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aimlapi-jsonschema-spectral-rules
- name: AIMLAPI API Rules
  rule_count: 17
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 10
  slug: aimlapi-spectral-rules
score:
  band: developing
  composite: 55.5
  delta: -3.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aimlapi/refs/heads/main/screenshots/aimlapi-2026-06-20T171417.png
security:
- kind: authentication
  name: Aimlapi Authentication
  slug: aimlapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aimlapi Domain Security
  slug: aimlapi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aimlapi
tags:
- Artificial Intelligence
- Machine Learning
- AI Models
- LLM
- Image Generation
- Video Generation
- Speech
- Embeddings
- API Gateway
- Developer Tools
use_cases:
- description: Build conversational AI chatbots and virtual assistants using leading LLMs.
  name: AI Chatbot Development
- description: Automate text, image, video, and music content generation for media and marketing.
  name: Content Generation
- description: Build retrieval-augmented generation applications using embeddings and LLMs.
  name: RAG Applications
- description: Integrate AI code generation and review capabilities into developer tools.
  name: Code Generation
- description: Extract information and summarize documents using vision and LLM models.
  name: Document Processing
- description: Add speech-to-text transcription and text-to-speech synthesis to applications.
  name: Voice Applications
---
