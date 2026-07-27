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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ai21 Labs Agentic Access
  operation_count: 5
  slug: ai21-labs-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 11
apis:
- description: Conversational completions endpoint backed by the Jamba family of hybrid Mamba/Transformer models (Jamba 1.5 Mini, Jamba 1.5 Large, Jamba 1.6). Accepts a message array, system prompts, temperature, ma
  name: AI21 Jamba Chat Completions API
  slug: chat-completions
- description: Dynamic planning system that, at inference time, determines the optimal sequence of actions to solve a task. Exposes run creation and retrieval endpoints, supports validated output for strict instruct
  name: AI21 Maestro API
  slug: maestro
- description: Managed file storage for RAG workflows. Upload, list, retrieve, update, and delete documents that Maestro and Jamba endpoints can ground on at inference time.
  name: AI21 File Library API
  slug: library
- description: Asynchronous batch processing for large volumes of Jamba completions. Submit a batch job, poll for status, and download results when the run completes.
  name: AI21 Batch API
  slug: batch
- description: Fine-tuning service for Jamba models supporting full, LoRA, and QLoRA strategies. Create training jobs from uploaded datasets and deploy the resulting model variants behind the standard chat completio
  name: AI21 Fine-Tuning API
  slug: fine-tuning
- description: Official Python SDK (ai21 on PyPI) wrapping the AI21 Studio REST API with sync and async clients, streaming support, LangChain / LlamaIndex integrations, and helpers for chat, Maestro, library, and ba
  name: AI21 Python SDK
  slug: python-sdk
- description: Official TypeScript and JavaScript client for the AI21 Studio API, with typed request and response models and streaming helpers for browser and Node.js runtimes.
  name: AI21 TypeScript / JavaScript SDK
  slug: typescript-sdk
- description: Open-weight releases of the Jamba family on Hugging Face for self-hosted inference via vLLM, Transformers, and other runtimes.
  name: AI21 Jamba on Hugging Face
  slug: huggingface
- description: The Chat API from AI21 Labs — 1 operation(s) for chat.
  name: AI21 Labs Chat API
  slug: ai21-labs-chat-api
- description: The Library API from AI21 Labs — 1 operation(s) for library.
  name: AI21 Labs Library API
  slug: ai21-labs-library-api
- description: The Maestro API from AI21 Labs — 2 operation(s) for maestro.
  name: AI21 Labs Maestro API
  slug: ai21-labs-maestro-api
artifact_total: 21
asyncapis:
- description: AsyncAPI description of AI21 Labs' documented streaming surface. The AI21 Studio Jamba chat completions endpoint streams partial responses over HTTP using Server-Sent Events (SSE) when the `stream` re
  name: AI21 Studio Streaming API
  slug: ai21-labs-asyncapi
collections:
- collection_type: open
  name: AI21 Studio API
  slug: open-ai21-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ai21-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai21-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ai21-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ai21.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ai21.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ai21.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI21Labs
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/ai21labs
- group: company
  title: ''
  type: Blog
  url: https://www.ai21.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ai21.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ai21.com/changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ai21/
- group: other
  title: ''
  type: X
  url: https://x.com/AI21Labs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ai21.com/llms.txt
created: '2026-05-23'
description: AI21 Labs is an enterprise foundation-model company best known for the Jamba family of open-weight hybrid Mamba/Transformer models and AI21 Maestro, a dynamic planning system that orchestrates tools, retrieval, and validated output during inference. The platform exposes a Bearer-token REST API at api.ai21.com covering chat completions, conversational RAG over a managed file library, batch processing, fine-tuning, and function calling. Official Python and TypeScript SDKs wrap the API with sync and async clients and integrate natively into LangChain and LlamaIndex. Jamba weights are also published on Hugging Face for self-hosted vLLM deployment.
finops:
- name: Ai21 Labs Finops
  service_category: API
  slug: ai21-labs-finops
graphqls:
- description: 'This conceptual GraphQL schema maps the AI21 Labs REST API surface — covering the Jamba chat completion, Maestro agentic planning, conversational RAG file library, batch processing, fine-tuning, text '
  name: AI21 Labs GraphQL Schema
  slug: ai21-labs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ai21-labs.png
layout: provider
modified: '2026-05-29'
name: AI21 Labs
nav: Providers
network: true
overview: 'AI21 Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AI21 Jamba Chat Completions API, Chat API, Library API, and 1 more. Tagged areas include AI, Foundation Models, LLM, Jamba, and Mamba.


  The AI21 Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AI21 Labs'' developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, and 8 more developer resources.'
plans:
- name: Ai21 Labs Plans Pricing
  plan_count: 1
  slug: ai21-labs-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Ai21 Labs Rate Limits
  slug: ai21-labs-rate-limits
rules:
- name: AI21 Labs API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: ai21-labs-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.9
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 52.6
    operational_transparency: 42.1
  previous_composite: 46.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ai21-labs/refs/heads/main/screenshots/ai21-labs-2026-06-20T170826.png
security:
- kind: authentication
  name: Ai21 Labs Authentication
  slug: ai21-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ai21 Labs Domain Security
  slug: ai21-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai21-labs
tags:
- AI
- Foundation Models
- LLM
- Jamba
- Mamba
- RAG
- Agents
- Maestro
- Inference
- Enterprise AI
- Fine-Tuning
website: https://www.ai21.com/
---
