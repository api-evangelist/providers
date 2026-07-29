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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Openrouter Agentic Access
  operation_count: 12
  slug: openrouter-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 7
apis:
- description: Chat completion endpoints (OpenAI-compatible).
  name: OpenRouter Chat API
  slug: openrouter-chat-api
- description: Legacy completions endpoint.
  name: OpenRouter Completions API
  slug: openrouter-completions-api
- description: Account credit balance and usage.
  name: OpenRouter Credits API
  slug: openrouter-credits-api
- description: Query stats and usage for completed generations.
  name: OpenRouter Generation API
  slug: openrouter-generation-api
- description: Provisioning and management of API keys.
  name: OpenRouter Keys API
  slug: openrouter-keys-api
- description: Discover available models and their endpoints.
  name: OpenRouter Models API
  slug: openrouter-models-api
- description: List supported providers.
  name: OpenRouter Providers API
  slug: openrouter-providers-api
artifact_total: 47
collections:
- collection_type: postman
  name: OpenRouter Chat API
  slug: postman-openrouter-chat-api
- collection_type: postman
  name: OpenRouter Chat Completions API
  slug: postman-openrouter-completions-api
- collection_type: postman
  name: OpenRouter Chat Credits API
  slug: postman-openrouter-credits-api
- collection_type: postman
  name: OpenRouter Chat Generation API
  slug: postman-openrouter-generation-api
- collection_type: postman
  name: OpenRouter Chat Keys API
  slug: postman-openrouter-keys-api
- collection_type: postman
  name: OpenRouter Chat Models API
  slug: postman-openrouter-models-api
- collection_type: postman
  name: OpenRouter Chat Providers API
  slug: postman-openrouter-providers-api
- collection_type: open
  name: OpenRouter API
  slug: open-openrouter
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openrouter/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openrouter-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openrouter-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openrouter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openrouter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openrouter
- group: company
  title: ''
  type: Website
  url: https://openrouter.ai/
- group: other
  title: ''
  type: Models
  url: https://openrouter.ai/models
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openrouter.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://openrouter.ai/docs/quickstart
- group: operate
  title: ''
  type: FAQ
  url: https://openrouter.ai/docs/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://openrouter.ai/models?fmt=table
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openrouter.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openrouter.ai/terms
- group: start
  title: ''
  type: Portal
  url: https://openrouter.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/api/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://openrouter.ai/docs/api/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://openrouter.ai/docs/api/reference/limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://openrouter.ai/docs/api/reference/errors-and-debugging
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/api/reference/streaming
- group: docs
  title: ''
  type: OpenAPI
  url: https://openrouter.ai/openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: https://openrouter.ai/openapi.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://openrouter.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://openrouter.ai/support
- group: company
  title: ''
  type: Blog
  url: https://openrouter.ai/announcements
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/openrouter
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenRouterTeam
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OpenRouterTeam/typescript-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OpenRouterTeam/python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://openrouter.ai/docs/sdks/typescript/overview
- group: build
  title: ''
  type: SDKs
  url: https://openrouter.ai/docs/sdks/python/overview
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/community/openai-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/routing/provider-selection
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/tool-calling
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/structured-outputs
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/model-routing
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/guardrails
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/zdr
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/features/plugins/web-search
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/overview/auth/byok
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/guides/for-providers
- group: auth
  title: ''
  type: APIKeys
  url: https://openrouter.ai/settings/keys
- group: docs
  title: ''
  type: Documentation
  url: https://openrouter.ai/docs/guides/overview/principles
- group: agent
  title: ''
  type: LlmsText
  url: https://openrouter.ai/llms.txt
created: '2025-08-19T00:00:00.000Z'
description: OpenRouter is an API platform that provides unified access to multiple AI language models through a single interface. OpenRouter acts as a "router" or gateway that lets developers and applications access dozens of different AI models from various providers through one standardized API, rather than having to integrate with each provider separately.
features:
- 'Free: 25+ models, 50 req/day cap'
- 'Pay-As-You-Go: 300+ models, 0% provider markup'
- 5.5% platform fee on credit purchases
- 'Enterprise: volume discounts, custom platform fee'
- Failed/fallback attempts NOT billed
- OpenAI-compatible Chat Completions API
- 300+ models from OpenAI, Anthropic, Google, Mistral, Meta, etc.
- Automatic fallback routing on errors
- Bring Your Own Key (BYOK) for select providers
- Streaming responses
- Tool use / function calling (model-dependent)
- Vision (model-dependent)
- Per-model upstream rate limit passthrough
- Bearer token auth
- Provider transparency (see live latency/uptime/throughput)
- Credits + Stripe payments + crypto
finops:
- name: Openrouter Finops
  service_category: AI Model Aggregation
  slug: openrouter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openrouter.png
json_schemas:
- name: OpenRouter Chat Message
  property_count: 5
  slug: openrouter-chat-message
- name: ChatCompletionRequest
  property_count: 12
  slug: openrouter-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 6
  slug: openrouter-chatcompletionresponse
- name: ChatMessage
  property_count: 4
  slug: openrouter-chatmessage
- name: CompletionRequest
  property_count: 5
  slug: openrouter-completionrequest
- name: ModelList
  property_count: 1
  slug: openrouter-modellist
json_structures:
- name: Openrouter Structure
  property_count: 0
  slug: openrouter-structure
jsonld:
- class_count: 21
  name: Openrouter Context
  property_count: 1
  slug: openrouter-context
layout: provider
modified: '2026-05-19'
name: OpenRouter
nav: Providers
network: true
overview: 'OpenRouter publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Credits API, and 4 more. Tagged areas include Artificial Intelligence, Gateway, Large Language Models, and Router.


  The OpenRouter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenRouter''s developer surface includes authentication, getting-started guide, FAQ, pricing, developer portal, documentation, support, and 37 more developer resources.'
plans:
- name: Openrouter Plans Pricing
  plan_count: 3
  slug: openrouter-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 3
  name: Openrouter Rate Limits
  slug: openrouter-rate-limits
rules:
- name: OpenRouter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openrouter-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.8
  delta: -2.9
  facets:
    commercial_clarity: 78.9
    contract_quality: 69.6
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openrouter/refs/heads/main/screenshots/openrouter-2026-06-20T191028.png
security:
- kind: authentication
  name: Openrouter Authentication
  slug: openrouter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openrouter Domain Security
  slug: openrouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openrouter Trust Center
  slug: openrouter-trust-center
  summary_line: SOC 2
slug: openrouter
tags:
- Artificial Intelligence
- Gateway
- Large Language Models
- Router
website: https://openrouter.ai/
---
