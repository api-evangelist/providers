---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Venice Ai Agentic Access
  operation_count: 55
  slug: venice-ai-agentic-access
  summary_line: 55 operations · 33 acting
api_count: 2
apis:
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The API Keys API from Venice.ai — 5 operation(s) for api keys.
  name: Venice.ai API Keys API
  slug: venice-ai-api-keys-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Generate speech/audio, transcribe audio, and manage asynchronous audio generation jobs.
  name: Venice.ai Audio API
  slug: venice-ai-audio-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Augment API from Venice.ai — 3 operation(s) for augment.
  name: Venice.ai Augment API
  slug: venice-ai-augment-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: 'Billing and usage analytics. **Beta**: This API is currently in beta and may be unstable. Endpoints, request/response schemas, and behavior may change without notice.'
  name: Venice.ai Billing API
  slug: venice-ai-billing-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: List and retrieve character information for use in completions.
  name: Venice.ai Characters API
  slug: venice-ai-characters-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Proxy JSON-RPC requests to blockchain nodes. Billed per credit.
  name: Venice.ai Crypto RPC API
  slug: venice-ai-crypto-rpc-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: 'Evaluate a state against typed questions and get structured answers (yes/no probabilities, option picks with distributions, rubric scores). **Beta**: This API is currently in beta and may be unstable.'
  name: Venice.ai Decisions API
  slug: venice-ai-decisions-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Create vector embeddings from text. `input` must be a string or an array of strings. Token arrays are not supported. LangChain OpenAIEmbeddings must set `check_embedding_ctx_length=False` to send text
  name: Venice.ai Embeddings API
  slug: venice-ai-embeddings-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Generate and manipulate images using AI models.
  name: Venice.ai Image API
  slug: venice-ai-image-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: List and describe the various models available in the API.
  name: Venice.ai Models API
  slug: venice-ai-models-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Preview API from Venice.ai — 3 operation(s) for preview.
  name: Venice.ai Preview API
  slug: venice-ai-preview-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Responses API from Venice.ai — 1 operation(s) for responses.
  name: Venice.ai Responses API
  slug: venice-ai-responses-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Speech API from Venice.ai — 1 operation(s) for speech.
  name: Venice.ai Speech API
  slug: venice-ai-speech-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Transcriptions API from Venice.ai — 1 operation(s) for transcriptions.
  name: Venice.ai Transcriptions API
  slug: venice-ai-transcriptions-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Generate videos using AI models.
  name: Venice.ai Video API
  slug: venice-ai-video-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: The Voices API from Venice.ai — 1 operation(s) for voices.
  name: Venice.ai Voices API
  slug: venice-ai-voices-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Wallet-based API access using the x402 protocol. No API key required — authenticate with an EVM or Solana wallet. **How it works:** 1. **Authenticate** — Send a `SIGN-IN-WITH-X` header (base64-encoded
  name: Venice.ai X402 API
  slug: venice-ai-x402-api
- baseURL: https://api.venice.ai/api/v1
  baseurl_source: declared
  description: Given a list of messages comprising a conversation, the model will return a response. Supports multimodal inputs including text, images, audio (input_audio), and video (video_url) for compatible model
  name: Venice.ai Chat Completions API
  slug: venice-ai-chat-completions-api
artifact_total: 31
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/agentic-access/venice-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/venice-ai-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/rate-limits/venice-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/venice-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/rules/venice-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/venice-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/json-ld/venice-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/venice-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/vocabulary/venice-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/venice-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/data-model/venice-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/venice-ai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/conventions/venice-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/venice-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/conventions/venice-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/venice-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/errors/venice-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/venice-ai-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/errors/venice-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/venice-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/conformance/venice-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/venice-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/llms/venice-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/venice-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/a2a/venice-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/venice-ai-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/mcp/venice-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/venice-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/mcp/venice-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/venice-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/well-known/venice-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/venice-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/hosts/venice-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/venice-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/vendors/venice-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/venice-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/packages/venice-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/venice-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/packages/venice-ai-packages.yml
  title: ''
  type: Packages
  url: packages/venice-ai-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://venice.ai/media
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.venice.ai`
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/authentication/venice-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/venice-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/venice-ai/refs/heads/main/security/venice-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/venice-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://venice.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.venice.ai/api-reference/api-spec
- group: company
  title: ''
  type: Blog
  url: https://venice.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://venice.ai/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.venice.ai/overview/about-venice
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.venice.ai/getting-started/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veniceai
- group: start
  title: ''
  type: Login
  url: https://venice.ai/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://venice.ai/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://venice.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://venice.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://venice.ai/legal/tos
- group: build
  title: ''
  type: Postman
  url: https://docs.venice.ai/guides/getting-started/postman
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.venice.ai/overview/deprecations
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.venice.ai/api-reference/rate-limiting
created: '2026-10-13'
description: Venice.ai is a privacy-first, uncensored AI platform and API offering text generation, image generation, audio synthesis, speech-to-speech voice conversion, video generation, music, embeddings and developer tools (web search, document parsing, blockchain RPC) with zero data retention, through an OpenAI-compatible REST API at api.venice.ai, payable by API key or x402 crypto micropayments.
image: https://venice.ai/social.webp
json_schemas:
- name: ChatCompletionRequest
  property_count: 38
  slug: venice-ai-chat-completion-request
- name: GenerateImageRequest
  property_count: 25
  slug: venice-ai-generate-image-request
- name: ModelResponse
  property_count: 8
  slug: venice-ai-model-response
- name: MultiEditImageRequest
  property_count: 11
  slug: venice-ai-multi-edit-image-request
- name: QueueVideoRequest
  property_count: 37
  slug: venice-ai-queue-video-request
- name: Responses API Request
  property_count: 17
  slug: venice-ai-responses-request
jsonld:
- class_count: 47
  name: Venice Ai Context
  property_count: 173
  slug: venice-ai-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 27 tools listed.
  name: Venice MCP Server
  slug: venice-mcp-server
modified: '2026-10-13'
name: Venice.ai
nav: Providers
network: true
overview: 'Venice.ai publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Audio API, Augment API, and 15 more. Tagged areas include Company, Artificial Intelligence, LLM, Image Generation, and Video Generation.


  The Venice.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Venice.ai''s developer surface includes authentication, API reference, engineering blog, changelog, documentation, getting-started guide, signup flow, and 33 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 12
  name: Venice Ai Rate Limits
  slug: venice-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Venice.ai API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 4
  slug: venice-ai-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 65.0
    developer_ergonomics: 66.1
    discoverability: 73.3
    operational_transparency: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Venice Ai Authentication
  slug: venice-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Venice Ai Domain Security
  slug: venice-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: venice-ai
tags:
- Company
- Artificial Intelligence
- LLM
- Image Generation
- Video Generation
- Text-to-Speech
- Embeddings
- Privacy
- OpenAI-Compatible
- x402
website: https://venice.ai
---
