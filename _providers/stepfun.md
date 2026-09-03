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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
api_count: 12
apis:
- description: OpenAI-compatible chat completions for the Step model family (e.g. step-3.7-flash, step-3.5-flash, stepaudio-2.5-chat), with multimodal image/video/audio message parts, tool calling, JSON mode, stream
  name: StepFun Chat Completions API
  slug: chat-completions-api
- description: Anthropic Messages API-compatible endpoint (POST /v1/messages) that lets the Anthropic SDK and Claude-style JSON structures run against Step models by pointing base_url at https://api.stepfun.com.
  name: StepFun Messages API
  slug: messages-api
- description: OpenAI Responses API-style endpoint for generating model responses on the StepFun open platform.
  name: StepFun Responses API
  slug: responses-api
- description: List available Step models, retrieve a single model, and inspect the model object.
  name: StepFun Models API
  slug: models-api
- description: Speech synthesis (TTS), voice cloning with preview, official voice catalog, audio transcription, and file-based / streaming speech recognition (ASR) across the StepAudio 2.5 and step-tts model familie
  name: StepFun Audio API
  slug: audio-api
- baseURL: https://api.stepfun.com
  baseurl_source: declared
  description: Bidirectional realtime voice over WebSocket (wss://api.stepfun.com/v1/realtime) with OpenAI Realtime-style session, conversation, and response events, plus a streaming TTS channel at /v1/realtime/audi
  name: StepFun Realtime API
  slug: realtime-api
- description: Image generation, image editing, and image-to-image endpoints for the step-2x-large and step-image-edit-2 models.
  name: StepFun Images API
  slug: images-api
- description: Upload, list, retrieve, delete files and fetch file content for use with Step models and knowledge bases.
  name: StepFun Files API
  slug: files-api
- description: Knowledge-base (vector store) management — create/list/retrieve/delete stores and attach or remove files for retrieval-augmented generation.
  name: StepFun Vector Stores API
  slug: vector-stores-api
- description: Web search and text-to-image search endpoints (POST /v1/search) billed per call as value-added capabilities.
  name: StepFun Web Search API
  slug: web-search-api
- description: Pre-count prompt tokens for a model request (POST /v1/token/count) to estimate usage and cost.
  name: StepFun Token Count API
  slug: token-count-api
- description: Retrieve account information including balances (GET /v1/accounts).
  name: StepFun Accounts API
  slug: accounts-api
artifact_total: 17
asyncapis:
- description: 'StepFun''s realtime event surface: a bidirectional realtime voice channel at wss://api.stepfun.com/v1/realtime (OpenAI Realtime-style session / conversation / response events, models stepaudio-2.5-real'
  name: StepFun Realtime Voice & Streaming TTS WebSocket API
  slug: stepfun-realtime-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stepfun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stepfun.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.stepfun.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.stepfun.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform.stepfun.com/docs/zh/api-reference/chat/chat-completion-create
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.stepfun.com/docs/zh/quickstart/overview
- group: operate
  title: ''
  type: Support
  url: https://platform.stepfun.com/docs/zh/guides/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stepfun-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.stepfun.com/docs/zh/guides/pricing/details
- group: start
  title: ''
  type: SignUp
  url: https://platform.stepfun.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.stepfun.com/docs/zh/agreement/userservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.stepfun.com/docs/zh/agreement/userprivacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stepfun-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stepfun-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stepfun-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stepfun-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stepfun-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stepfun-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stepfun-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stepfun-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stepfun-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://platform.stepfun.com/docs/zh/guides/model-migration
- group: build
  title: ''
  type: Packages
  url: packages/stepfun-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stepfun-packages.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/stepfun-realtime-asyncapi.yml
created: '2026-07-17'
description: StepFun (阶跃星辰) is a Shanghai-based AI foundation-model company whose open platform serves the Step model family — multimodal reasoning (step-3.7-flash), fast language reasoning (step-3.5-flash), vision, image generation and editing (step-2x-large, step-image-edit-2), and a deep audio stack spanning TTS, voice cloning, ASR, and end-to-end realtime voice (StepAudio 2.5) — via an OpenAI-compatible REST API at api.stepfun.com, an Anthropic-compatible Messages API, WebSocket realtime channels, and a hosted StepSearch MCP server for agent clients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stepfun.png
layout: provider
mcp_servers:
- description: StepFun operates an official hosted remote MCP server, StepSearch — a search service built on the Model Context Protocol that gives Claude Code, Cline, OpenCode, Goose, and other MCP-compatible client
  name: StepFun MCP Server
  slug: stepfun-mcp-server
modified: '2026-07-21'
name: StepFun
nav: Providers
network: true
overview: 'StepFun publishes 1 API on the [APIs.io](https://apis.io/) network: Realtime API. Tagged areas include Artificial Intelligence, LLM, Multi-Modal, Chat Completion, and Audio.


  The StepFun catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StepFun''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 18
  name: Stepfun Rate Limits
  slug: stepfun-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.7
    developer_ergonomics: 61.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 47.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stepfun/refs/heads/main/screenshots/stepfun-2026-08-17T082149.png
security:
- kind: authentication
  name: Stepfun Authentication
  slug: stepfun-authentication
  summary_line: http-bearer-api-key · 1 scheme
- kind: domain-security
  name: Stepfun Domain Security
  slug: stepfun-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: stepfun
tags:
- Artificial Intelligence
- LLM
- Multi-Modal
- Chat Completion
- Audio
- Speech
- Text-to-Speech
- Speech Recognition
- Image
- Real-Time
- Vector Stores
- China
website: https://www.stepfun.com
---
