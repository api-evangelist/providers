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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Ollama Agentic Access
  operation_count: 21
  slug: ollama-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 14
apis:
- description: Ollama provides compatibility with parts of the OpenAI API, allowing existing applications built for OpenAI to connect to locally-running models through Ollama. Supported endpoints include chat comple
  name: Ollama OpenAI Compatibility API
  slug: ollama-openai-compatibility-api
- description: Ollama provides compatibility with the Anthropic Messages API, enabling tools like Claude Code to work with locally-running open-source models. Supports messages, streaming, system prompts, tool calli
  name: Ollama Anthropic Compatibility API
  slug: ollama-anthropic-compatibility-api
- description: Ollama Cloud provides cloud-hosted inference for large language models, giving access to larger models and faster responses without requiring a powerful local GPU. Cloud models are accessed through th
  name: Ollama Cloud API
  slug: ollama-cloud-api
- description: Manage binary large objects used by models.
  name: Ollama Blobs API
  slug: ollama-blobs-api
- description: Generate chat completions with multi-turn conversation support.
  name: Ollama Chat API
  slug: ollama-chat-api
- description: Generate chat completions using the OpenAI-compatible chat endpoint with multi-turn conversation support.
  name: Ollama Chat Completions API
  slug: ollama-chat-completions-api
- description: Generate text completions using the OpenAI-compatible completions endpoint.
  name: Ollama Completions API
  slug: ollama-completions-api
- description: Generate vector embeddings from text input.
  name: Ollama Embeddings API
  slug: ollama-embeddings-api
- description: Generate text completions from a prompt using a specified model.
  name: Ollama Generate API
  slug: ollama-generate-api
- description: Generate images from text descriptions using the OpenAI-compatible images endpoint. Experimental feature.
  name: Ollama Images API
  slug: ollama-images-api
- description: List, show, create, copy, pull, push, and delete models.
  name: Ollama Models API
  slug: ollama-models-api
- description: Generate structured responses with optional reasoning using the OpenAI-compatible Responses API.
  name: Ollama Responses API
  slug: ollama-responses-api
- description: View models currently loaded in memory and their resource usage.
  name: Ollama Running Models API
  slug: ollama-running-models-api
- description: Retrieve the Ollama server version.
  name: Ollama Version API
  slug: ollama-version-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ollama API
  slug: open-ollama-api
- collection_type: open
  name: Ollama Blobs API
  slug: open-ollama-blobs-api
- collection_type: open
  name: Ollama Blobs Chat API
  slug: open-ollama-chat-api
- collection_type: open
  name: Ollama Blobs Chat Completions API
  slug: open-ollama-chat-completions-api
- collection_type: open
  name: Ollama Blobs Completions API
  slug: open-ollama-completions-api
- collection_type: open
  name: Ollama Blobs Embeddings API
  slug: open-ollama-embeddings-api
- collection_type: open
  name: Ollama Blobs Generate API
  slug: open-ollama-generate-api
- collection_type: open
  name: Ollama Blobs Images API
  slug: open-ollama-images-api
- collection_type: open
  name: Ollama Blobs Models API
  slug: open-ollama-models-api
- collection_type: open
  name: Ollama OpenAI Compatibility API
  slug: open-ollama-openai-compatibility-api
- collection_type: open
  name: Ollama Blobs Responses API
  slug: open-ollama-responses-api
- collection_type: open
  name: Ollama Blobs Running Models API
  slug: open-ollama-running-models-api
- collection_type: open
  name: Ollama Blobs Version API
  slug: open-ollama-version-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ollama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ollama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ollama-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ollama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/
- group: operate
  title: ''
  type: FAQ
  url: https://docs.ollama.com/faq
- group: start
  title: ''
  type: Login
  url: https://signin.ollama.com/?client_id=client_01JX0QMHD43PFFCCNXH82A6K8B&redirect_uri=https%3A%2F%2Follama.com%2Fauth%2Fcallback&authorization_session_id=01KE5QZJQP6W24EJGN9TYDR5K8
- group: start
  title: ''
  type: Signup
  url: https://signin.ollama.com/sign-up?redirect_uri=https%3A%2F%2Follama.com%2Fauth%2Fcallback&authorization_session_id=01KE5QZJQP6W24EJGN9TYDR5K8
- group: commercial
  title: ''
  type: Pricing
  url: https://ollama.com/cloud
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ollama/ollama
- group: company
  title: ''
  type: Blog
  url: https://ollama.ai/blog
- group: other
  title: ''
  type: Models
  url: https://ollama.ai/library
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.ollama.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ollama.com/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.ollama.com/api/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://ollama.com/pricing
- group: other
  title: ''
  type: Downloads
  url: https://ollama.com/download
- group: other
  title: ''
  type: Models
  url: https://ollama.com/search
- group: company
  title: ''
  type: Blog
  url: https://ollama.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ollama/ollama/releases
- group: auth
  title: ''
  type: Security
  url: https://github.com/ollama/ollama/security
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/ollama/ollama-python
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/ollama/ollama-js
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/ollama
- group: other
  title: ''
  type: Reddit
  url: https://reddit.com/r/ollama
- group: other
  title: ''
  type: X
  url: https://twitter.com/ollama
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ollama
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/tool-calling
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/structured-outputs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/vision
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/embeddings
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/thinking
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/web-search
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/capabilities/streaming
- group: other
  title: ''
  type: Docker
  url: https://docs.ollama.com/docker
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/modelfile
- group: build
  title: ''
  type: CLI
  url: https://docs.ollama.com/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/gpu
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.ollama.com/troubleshooting
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/import
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/context-length
- group: build
  title: ''
  type: Dart SDK
  url: https://github.com/ollama/ollama-dart
- group: build
  title: ''
  type: Swift SDK
  url: https://github.com/ollama/ollama-swift
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ollama
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Ollama-AI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ollama
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/ollama/ollama/issues
- group: other
  title: ''
  type: Events
  url: https://ollama.com/events
- group: build
  title: ''
  type: Go SDK
  url: https://pkg.go.dev/github.com/ollama/ollama/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/linux
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/macos
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ollama.com/windows
created: '2025-11-19'
description: API for running large language models locally.
finops:
- name: Ollama Finops
  service_category: AI Infrastructure
  slug: ollama-finops
image: https://ollama.ai/public/ollama.png
layout: provider
modified: '2026-05-19'
name: Ollama
nav: Providers
network: true
overview: 'Ollama publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Blobs API, Chat API, Chat Completions API, and 8 more. Tagged areas include Artificial Intelligence, Large Language Models, and Models.


  Ollama''s developer surface includes authentication, documentation, FAQ, signup flow, pricing, GitHub presence, engineering blog, and 46 more developer resources.'
plans:
- name: Ollama Plans Pricing
  plan_count: 4
  slug: ollama-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Ollama Rate Limits
  slug: ollama-rate-limits
score:
  band: developing
  composite: 40.8
  delta: 0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 48.6
    developer_ergonomics: 54.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ollama/refs/heads/main/screenshots/ollama-2026-06-20T190657.png
security:
- kind: authentication
  name: Ollama Authentication
  slug: ollama-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ollama Domain Security
  slug: ollama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ollama
tags:
- Artificial Intelligence
- Large Language Models
- Models
website: https://ollama.com/
---
