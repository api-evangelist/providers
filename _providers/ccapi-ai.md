---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Ccapi Ai Agentic Access
  operation_count: 38
  slug: ccapi-ai-agentic-access
  summary_line: 38 operations · 28 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: CCAPI provides an OpenAI-compatible API gateway for over 100 AI models.
  name: CCAPI
  slug: ccapi
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Upscale an input image by x2 via CCAPI''s OpenAI Images-compatible API. The public model name is `ccapi-upscale-v1`. --- ## Endpoint Use `POST /v1/images/generations` as the unified image endpoint. Thi'
  name: ccapi-ai CCAPI Image Upscale API
  slug: ccapi-ai-ccapi-image-upscale-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Access the Claude native Messages API via CCAPI proxy routing. --- ## Authentication Recommended Claude native-style request headers: - `x-api-key: <CCAPI Token>` - `anthropic-version: 2023-06-01` The'
  name: ccapi-ai Claude / Anthropic LLM Integration API
  slug: ccapi-ai-claude-anthropic-llm-integration-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Call the official DeepSeek V4 API through CCAPI with one token. --- ## Authentication Use `Authorization: Bearer <CCAPI Token>`. --- ## Recommended endpoint - `POST /v1/chat/completions` --- ## Curren'
  name: ccapi-ai DeepSeek LLM Integration API
  slug: ccapi-ai-deepseek-llm-integration-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: Generate and edit images with Seedream 5.0 Pro, 5.0, and 4.5 through the VolcEngine-native endpoint. Replace the official host with your CCAPI host; the request and response shapes remain compatible.
  name: ccapi-ai Doubao Seedream Official Image API
  slug: ccapi-ai-doubao-seedream-official-image-api-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Access Gemini per-call image generation capabilities via CCAPI''s OpenAI Images-compatible API. The public model name is the `nano-banana` series. --- ## What This Document Covers This document corresp'
  name: ccapi-ai Gemini Per-Call Image Generation API
  slug: ccapi-ai-gemini-per-call-image-generation-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Per-call video generation with the Gemini Video model family: `veo-3.1-quality`, `veo-3.1-fast`, `veo-3.1-lite` and `omni-flash`, using the OpenAI-compatible `/v1/videos` async task flow. **Flow**: `P'
  name: ccapi-ai Gemini Video (Veo 3.1 / Omni Flash) API
  slug: ccapi-ai-gemini-video-veo-3-1-omni-flash-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Access the Google Gemini native API via CCAPI Gemini proxy routing. --- ## Authentication The Gemini native path supports two ways to pass the CCAPI token: - Header: `x-goog-api-key: <CCAPI Token>` - '
  name: ccapi-ai Google Gemini LLM Integration API
  slug: ccapi-ai-google-gemini-llm-integration-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Access GPT Image 2 via CCAPI''s OpenAI Images-compatible API. --- ## What This Document Covers This document corresponds to the **per-call billing version**, using `POST /v1/images/generations` as the '
  name: ccapi-ai GPT Image 2 Per-Call Image Generation API
  slug: ccapi-ai-gpt-image-2-per-call-image-generation-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Per-call image-to-video generation with `grok-imagine-video-1-5-preview`, using the OpenAI-compatible `/v1/videos` async task flow. **Flow**: `POST /v1/videos` returns a `task_id` immediately; poll `G'
  name: ccapi-ai Grok Imagine Video API
  slug: ccapi-ai-grok-imagine-video-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: Generate Midjourney images through CCAPI's simplified asynchronous image API. Submit one `mj_imagine` text-to-image task, then poll by `task_id`. A successful task returns four ordered split images in
  name: ccapi-ai Midjourney Imagine API
  slug: ccapi-ai-midjourney-imagine-api-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: Generate 5–15 second videos through the unified CCAPI task flow. H3 provides text-to-video, image-to-video, and reference-to-video. Reference-to-video accepts image, video, and audio inputs and also c
  name: ccapi-ai MiniMax H3 Family Video Generation API
  slug: ccapi-ai-minimax-h3-family-video-generation-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Connect to MiniMax text models via CCAPI''s proxy routing. --- ## Authentication Use `Authorization: Bearer <CCAPI Token>`. --- ## Recommended Endpoint - `POST /v1/chat/completions` --- ## Capabilities'
  name: ccapi-ai MiniMax LLM Integration API
  slug: ccapi-ai-minimax-llm-integration-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Access OpenAI series LLMs via CCAPI proxy routing. --- ## Authentication Use `Authorization: Bearer <CCAPI Token>`. --- ## Recommended Endpoints - `POST /v1/chat/completions`: Standard OpenAI Chat Com'
  name: ccapi-ai OpenAI LLM Integration API
  slug: ccapi-ai-openai-llm-integration-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'CCAPI''s Producer task API. Uses a unified async task architecture: submit returns a public task ID, then poll via fetch to get normalized results without exposing upstream provider details. --- ## Wor'
  name: ccapi-ai Producer Task API
  slug: ccapi-ai-producer-task-api-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: Seedance 2.5, 2.0, Fast, and Mini use the unified video API. Submit with `POST /v1/videos`, then poll `GET /v1/videos/{task_id}` using the public task ID. Provider-native endpoints and channel impleme
  name: ccapi-ai Seedance 2.5 / 2.0 Video Generation API
  slug: ccapi-ai-seedance-2-5-2-0-video-generation-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'List platform-reviewed public Seedance assets and private authorized assets owned by the current account. **Start with the official public virtual-avatar library**: it requires no real-person verifica'
  name: ccapi-ai Seedance Trusted Asset Library API
  slug: ccapi-ai-seedance-trusted-asset-library-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'CCAPI''s Suno task API. Uses a unified async task architecture: submit returns a public task ID, then poll via fetch to get normalized results without exposing upstream provider details. --- ## Workflo'
  name: ccapi-ai Suno Task API
  slug: ccapi-ai-suno-task-api-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'CCAPI is fully compatible with the Vidu official API. **Simply replace the domain name.** **Domain replacement** ``` Official: api.vidu.cn CCAPI: api.ccapi.ai ``` **Auth**: `Authorization: Token sk-xx'
  name: ccapi-ai Vidu Video Generation API
  slug: ccapi-ai-vidu-video-generation-api-api
- baseURL: https://api.ccapi.ai
  baseurl_source: declared
  description: 'Fast text-to-image generation with strong Chinese and English typography. Z-Image Turbo uses a strict four-field request contract, requires an explicit aspect ratio, and returns exactly one image per '
  name: ccapi-ai Z-Image Turbo API
  slug: ccapi-ai-z-image-turbo-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/ccapi-ai/agentic-access/ccapi-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ccapi-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ccapi-ai/rules/ccapi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ccapi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/ccapi-ai/json-ld/ccapi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ccapi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/ccapi-ai/vocabulary/ccapi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ccapi-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ccapi-ai/data-model/ccapi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ccapi-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ccapi-ai/authentication/ccapi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ccapi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/ccapi-ai/errors/ccapi-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ccapi-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ccapi-ai/conformance/ccapi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ccapi-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ccapi-ai/llms/ccapi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ccapi-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/ccapi-ai/mcp/ccapi-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ccapi-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/ccapi-ai/hosts/ccapi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ccapi-ai-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ccapi.ai/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ccapi.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://ccapi.ai/blog
- group: auth
  href: https://artifacts.apis.io/ccapi-ai/security/ccapi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ccapi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ccapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ccapi.ai/docs/en
- group: commercial
  title: ''
  type: Pricing
  url: https://ccapi.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ccapi.ai/register
created: '2026-10-30'
description: CCAPI provides a unified API gateway that gives developers access to over 100 AI models across text, image, video, and music domains, including models from OpenAI, Anthropic, Google, ByteDance, Suno and others. It offers a single API key, transparent pay‑as‑you‑go pricing, and supports OpenAI‑compatible endpoints, enabling easy integration without managing multiple provider accounts.
image: https://ccapi.ai/logo.svg
jsonld:
- class_count: 38
  name: Ccapi Ai Context
  property_count: 87
  slug: ccapi-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at ccapi.ai.
  name: ccapi-ai MCP Server
  slug: ccapi-ai-mcp-yml
modified: '2026-10-30'
name: ccapi-ai
nav: Providers
network: true
overview: 'ccapi-ai publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including CCAPI Image Upscale API, Claude / Anthropic LLM Integration API, DeepSeek LLM Integration API, and 17 more. Tagged areas include Company, Artificial Intelligence, Gateways, Models, and Platform.


  The ccapi-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ccapi-ai''s developer surface includes authentication, sandbox, engineering blog, documentation, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Ccapi Ai Plans Pricing
  plan_count: 0
  slug: ccapi-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Ccapi Ai Rate Limits
  slug: ccapi-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ccapi-ai API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 5
  slug: ccapi-ai-rules
scopes:
- name: Ccapi Ai Scopes
  scope_count: 0
  slug: ccapi-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ccapi-ai/ccapi-ai-2026-11-03T123539.png
security:
- kind: authentication
  name: Ccapi Ai Authentication
  slug: ccapi-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ccapi Ai Domain Security
  slug: ccapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ccapi-ai
tags:
- Company
- Artificial Intelligence
- Gateways
- Models
- Platform
website: https://ccapi.ai/
---
