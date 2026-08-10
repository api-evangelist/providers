---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: Chat completion API for conversational AI using Mistral's language models, with function calling, streaming, and JSON / structured output.
  name: Mistral AI Chat API
  slug: mistral-ai-chat-api
- description: Generate vector embeddings for text and code for retrieval, clustering, classification, and semantic search.
  name: Mistral Embeddings API
  slug: mistral-embeddings-api
- description: Content moderation and classification API for detecting harmful content across nine safety categories for text and chat.
  name: Mistral Moderation API
  slug: mistral-moderation-api
- description: Agent completions API for building AI agents that handle complex tasks, maintain context, coordinate actions, and use tools and connectors.
  name: Mistral AI Agents API
  slug: mistral-ai-agents-api
- description: Fill-in-the-Middle code completion API powered by Codestral for generating code between a prompt and suffix across 80+ languages.
  name: Mistral AI FIM API
  slug: mistral-ai-fim-api
- description: Document AI / OCR API that extracts text, images, tables, and structured data from documents and PDFs with complex layouts.
  name: Mistral AI OCR API
  slug: mistral-ai-ocr-api
- description: Fine-tuning API for customizing Mistral models on your own datasets, supporting text, vision, and classifier fine-tuning.
  name: Mistral AI Fine-Tuning API
  slug: mistral-ai-fine-tuning-api
- description: File management API for uploading, retrieving, downloading, and deleting files used across fine-tuning, batch, and OCR.
  name: Mistral AI Files API
  slug: mistral-ai-files-api
- description: Models management API for listing available models, retrieving model details, and managing fine-tuned models.
  name: Mistral AI Models API
  slug: mistral-ai-models-api
- description: Batch inference API for processing up to one million requests asynchronously at reduced cost across most endpoints.
  name: Mistral AI Batch API
  slug: mistral-ai-batch-api
- description: Audio transcription API powered by Voxtral for speech-to-text with diarization, word-level timestamps, and streaming.
  name: Mistral AI Audio Transcription API
  slug: mistral-ai-audio-transcription-api
artifact_total: 13
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mistral-ai/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mistralai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mistral.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mistral.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mistral.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mistral.ai/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mistral.ai/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@mistral.ai
- group: company
  title: ''
  type: Blog
  url: https://mistral.ai/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mistralai
- group: commercial
  title: ''
  type: Pricing
  url: https://mistral.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.mistral.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mistral.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mistral.ai/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mistral.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mistral.ai/getting-started/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mistralai-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mistral.ai/getting-started/models/models_overview/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MistralAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mistralai
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/mistralai
- group: build
  title: ''
  type: SDKs
  url: packages/mistralai-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/mistralai-packages.yml
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/mistralai/client-python
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/mistralai/client-ts
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mistralai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mistralai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mistralai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mistralai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mistralai-conformance.yml
created: '2026-07-17'
description: Mistral AI is a Paris-based artificial intelligence company that develops and operates frontier open-weight and commercial large language models, exposed to developers and enterprises through La Plateforme (api.mistral.ai). The developer platform provides an OpenAI-compatible REST surface spanning chat completions, embeddings, content moderation, agents and tool-use, fill-in-the-middle code completion (Codestral), document OCR, audio transcription (Voxtral), fine-tuning, file management, model management, and asynchronous batch inference. Access is via a bearer API key issued from the console, with first-party Python and TypeScript SDKs, published pricing, a status page, and a dated changelog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mistralai.png
layout: provider
modified: '2026-07-20'
name: Mistral AI
nav: Providers
network: true
overview: 'Mistral AI publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Large Language Models, Generative AI, and Machine Learning.


  Mistral AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 37.0
  provenance:
    conformance: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mistralai/refs/heads/main/screenshots/mistralai-2026-08-07T183801.png
security:
- kind: authentication
  name: Mistralai Authentication
  slug: mistralai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mistralai Domain Security
  slug: mistralai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mistralai
tags:
- Company
- Artificial Intelligence
- Large Language Models
- Generative AI
- Machine Learning
- Chat
- Embeddings
- Agents
- OCR
- Fine-Tuning
- Developer Platform
website: https://mistral.ai
---
