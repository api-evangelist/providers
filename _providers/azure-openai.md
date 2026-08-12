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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azure Openai Agentic Access
  operation_count: 6
  slug: azure-openai-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 8
apis:
- description: Data-plane REST API for running inference against deployed Azure OpenAI models, including chat completions, completions, embeddings, image generation, and audio transcription/translation. Authenticate
  name: Azure OpenAI Inference REST API
  slug: inference-api
- description: Stateful, agent-friendly API for building multi-turn AI experiences with tool use, file inputs, and conversation state managed on the service side.
  name: Azure OpenAI Responses API
  slug: responses-api
- description: Azure Resource Manager (ARM) REST API for creating and managing Azure OpenAI accounts, model deployments, network rules, and other resource configuration.
  name: Azure OpenAI Control Plane API
  slug: control-plane
- description: Audio transcription and translation (Whisper)
  name: Azure OpenAI Service Audio API
  slug: azure-openai-audio-api
- description: Chat-formatted text generation
  name: Azure OpenAI Service Chat Completions API
  slug: azure-openai-chat-completions-api
- description: Plain text completions
  name: Azure OpenAI Service Completions API
  slug: azure-openai-completions-api
- description: Vector embeddings
  name: Azure OpenAI Service Embeddings API
  slug: azure-openai-embeddings-api
- description: Image generation (DALL-E)
  name: Azure OpenAI Service Images API
  slug: azure-openai-images-api
artifact_total: 17
asyncapis:
- description: 'AsyncAPI 2.6 description of the asynchronous and streaming surfaces of the Azure OpenAI Service (part of Microsoft Foundry Models): * The **Realtime API** over a WebSocket connection used for low-late'
  name: Azure OpenAI Service - Streaming and Realtime APIs
  slug: azure-openai-asyncapi
collections:
- collection_type: open
  name: Azure OpenAI Inference REST API
  slug: open-azure-openai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-openai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-openai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-openai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-openai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-openai-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/ai-services/openai-service
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/ai-services/openai/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: build
  title: ''
  type: GitHub Samples
  url: https://github.com/Azure-Samples/Azure-OpenAI-Docs-Samples
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/cognitiveservices/data-plane/AzureOpenAI
- group: agent
  title: ''
  type: LlmsText
  url: https://azure.microsoft.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=azure-ai-foundry-blog
created: '2026-05-11'
description: Azure OpenAI Service (part of Microsoft Foundry Models) provides REST API access to OpenAI models including GPT, o-series reasoning models, DALL-E, Whisper, and embedding models, hosted within Microsoft Azure with enterprise security, regional availability, private networking, content filtering, and Microsoft Entra ID integration. The data-plane REST API exposes endpoints for chat completions, completions, embeddings, image generation, audio transcription/translation, fine-tuning, and the Responses API, while the control-plane API manages Azure OpenAI resources and deployments.
graphqls:
- description: Azure OpenAI Service provides REST API access to OpenAI models (GPT-4, GPT-3.5, DALL-E, Whisper, Embeddings) with enterprise SLAs, private networking, and Azure identity. The API covers completions, c
  name: Azure OpenAI Service GraphQL API
  slug: azure-openai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-openai.png
layout: provider
modified: '2026-05-29'
name: Azure OpenAI Service
nav: Providers
network: true
overview: 'Azure OpenAI Service publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Azure OpenAI Inference REST API, Audio API, Chat Completions API, and 3 more. Tagged areas include AI, LLM, Generative AI, Azure, and OpenAI.


  The Azure OpenAI Service catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Azure OpenAI Service''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 72
rules:
- name: Azure OpenAI Service API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: azure-openai-asyncapi-spectral-rules
scopes:
- name: Azure Openai Scopes
  scope_count: 1
  slug: azure-openai-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 42.6
  delta: 2.9
  facets:
    commercial_clarity: 23.7
    contract_quality: 67.4
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 0.0
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-openai/refs/heads/main/screenshots/azure-openai-2026-06-20T172911.png
security:
- kind: authentication
  name: Azure Openai Authentication
  slug: azure-openai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Openai Domain Security
  slug: azure-openai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Openai Vulnerability Disclosure
  slug: azure-openai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-openai
tags:
- AI
- LLM
- Generative AI
- Azure
- OpenAI
- Foundation Models
- Chat Completions
- Embeddings
website: https://azure.microsoft.com/en-us/products/ai-services/openai-service
---
