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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: First-party hosted remote Model Context Protocol server (streamable HTTP, protocol 2025-06-18) giving agents 12 tools to generate images, video, music and sound effects on the signed-in account, upsca
  name: BudgetPixel MCP Server
  slug: budgetpixel-mcp-server
- description: Read-only MCP server hosted on the BudgetPixel documentation site (Mintlify) giving agents two tools -- full-text documentation search and a sandboxed read-only filesystem query over the docs pages an
  name: BudgetPixel Docs Search MCP Server
  slug: budgetpixel-docs-search-mcp-server
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Account and credit balance
  name: BudgetPixel Account API
  slug: budgetpixel-account-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Alibaba API from BudgetPixel — 12 operation(s) for alibaba.
  name: BudgetPixel Alibaba API
  slug: budgetpixel-alibaba-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Music and sound-effect job status
  name: BudgetPixel Audios API
  slug: budgetpixel-audios-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: FLUX image models
  name: BudgetPixel Black Forest Labs API
  slug: budgetpixel-black-forest-labs-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: SeeDream image models
  name: BudgetPixel Bytedance API
  slug: budgetpixel-bytedance-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: SeeDance video models
  name: BudgetPixel ByteDance (SeeDance) API
  slug: budgetpixel-bytedance-seedance-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Content classification — music genre detection
  name: BudgetPixel Classification API
  slug: budgetpixel-classification-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Format conversion for images, video, and audio
  name: BudgetPixel Conversions API
  slug: budgetpixel-conversions-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Google API from BudgetPixel — 3 operation(s) for google.
  name: BudgetPixel Google API
  slug: budgetpixel-google-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Image job status
  name: BudgetPixel Images API
  slug: budgetpixel-images-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Kuaishou Kling video models
  name: BudgetPixel Kling API
  slug: budgetpixel-kling-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Lip Sync API from BudgetPixel — 3 operation(s) for lip sync.
  name: BudgetPixel Lip Sync API
  slug: budgetpixel-lip-sync-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The MiniMax API from BudgetPixel — 1 operation(s) for minimax.
  name: BudgetPixel Mini Max API
  slug: budgetpixel-minimax-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Discover available models and pricing
  name: BudgetPixel Models API
  slug: budgetpixel-models-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Content moderation — NSFW rating and CSAM detection
  name: BudgetPixel Moderation API
  slug: budgetpixel-moderation-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Motion Control API from BudgetPixel — 3 operation(s) for motion control.
  name: BudgetPixel Motion Control API
  slug: budgetpixel-motion-control-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Music generation models
  name: BudgetPixel Music API
  slug: budgetpixel-music-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The OpenAI API from BudgetPixel — 1 operation(s) for openai.
  name: BudgetPixel Open AI API
  slug: budgetpixel-openai-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Pruna AI API from BudgetPixel — 3 operation(s) for pruna ai.
  name: BudgetPixel Pruna AI API
  slug: budgetpixel-pruna-ai-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Publish posts to your BudgetPixel feed
  name: BudgetPixel Social API
  slug: budgetpixel-social-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Text-to-sound-effect models (priced per second)
  name: BudgetPixel Sound Effects API
  slug: budgetpixel-sound-effects-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Upload input media for image/video generation
  name: BudgetPixel Uploads API
  slug: budgetpixel-uploads-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Upscaling API from BudgetPixel — 5 operation(s) for upscaling.
  name: BudgetPixel Upscaling API
  slug: budgetpixel-upscaling-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Video job status
  name: BudgetPixel Videos API
  slug: budgetpixel-videos-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The xAI API from BudgetPixel — 2 operation(s) for xai.
  name: BudgetPixel X AI API
  slug: budgetpixel-xai-api
artifact_total: 35
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/budgetpixel-ai/budgetpixel-mcp/blob/main/LICENSE
- group: start
  title: ''
  type: DeveloperPortal
  url: https://budgetpixel.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.budgetpixel.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.budgetpixel.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.budgetpixel.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://budgetpixel.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/budgetpixel-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://budgetpixel.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://budgetpixel.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://budgetpixel.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://budgetpixel.com/faq
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/tDbT2RDmkw
- group: company
  title: ''
  type: Blog
  url: https://budgetpixel.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/budgetpixel-ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/budgetpixel-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/budgetpixel-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/budgetpixel-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/budgetpixel-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/budgetpixel-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/budgetpixel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/budgetpixel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/budgetpixel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/budgetpixel-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/budgetpixel-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/budgetpixel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/budgetpixel-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/budgetpixel-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/budgetpixel-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/budgetpixel-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/budgetpixel-domain-security.yml
created: '2026-08-28'
description: 'BudgetPixel is an AI creative platform offering credit-based access to 70+ generative media models for image, video, music and sound-effect generation, plus upscaling, lip sync, motion control, format conversion and content moderation. Alongside a free design-studio canvas, LoRA training and a public community feed, it ships a unified developer surface: a 74-operation OpenAPI 3.1 REST API at api.budgetpixel.com/v1 (private beta, bearer bpx_live_* keys, Premium/Pro/Ultra plans) with an asynchronous create-then-poll job model and a POST /v1/cost endpoint that quotes the exact credit charge before you commit; a first-party remote MCP server at mcp.budgetpixel.com/mcp exposing 12 tools over streamable HTTP with OAuth 2.1 + PKCE and Google SSO; an A2A agent card and a published Agent Skill; and llms.txt indexes. One credit balance, one set of conventions, and identical published prices across every surface.'
image: https://budgetpixel.com/logo.png
layout: provider
mcp_servers:
- description: 'PRODUCT MCP, live: 12 tools (generate_image, generate_video, generate_music, generate_sound_effect, upscale_image, upscale_video, check_generation_status, get_credit_balance...). Streamable HTTP with '
  name: BudgetPixel MCP Server
  slug: budgetpixel-mcp-server
- description: ''
  name: BudgetPixel MCP Server
  slug: budgetpixel-mcp-server-2
- description: Mintlify DOCUMENTATION-SEARCH MCP (search_budget_pixel_api, query_docs_filesystem_budget_pixel_api, submit_feedback) -- not the generation API. Distinct from the product MCP at mcp.budgetpixel.com/mcp
  name: BudgetPixel MCP Server
  slug: budgetpixel-mcp-server-3
modified: '2026-08-28'
name: BudgetPixel
nav: Providers
network: true
overview: 'BudgetPixel publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Account API, Alibaba API, Audios API, and 22 more. Tagged areas include Generative AI, AI Image Generation, AI Video Generation, AI Music Generation, and Audio Generation.


  BudgetPixel''s developer surface includes documentation, API reference, getting-started guide, pricing, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Budgetpixel Plans Pricing
  plan_count: 6
  slug: budgetpixel-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Budgetpixel Rate Limits
  slug: budgetpixel-rate-limits
scopes:
- name: Budgetpixel Scopes
  scope_count: 0
  slug: budgetpixel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 57.5
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 57.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/budgetpixel/refs/heads/main/screenshots/budgetpixel-2026-09-02T144959.png
security:
- kind: authentication
  name: Budgetpixel Authentication
  slug: budgetpixel-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Budgetpixel Domain Security
  slug: budgetpixel-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: budgetpixel
tags:
- Generative AI
- AI Image Generation
- AI Video Generation
- AI Music Generation
- Audio Generation
- Content Moderation
- Creative Tools
- Design
- agent-native
- MCP
- MCP Server
- Artificial Intelligence
- Image Models
- Video Models
- Music/Audio Generation
- Generative Media
- llms-txt
- Media Processing
- Text-to-Image
- Text-to-Video
- Upscaling
- Credits
- Model Aggregator
- Agent Card
website: https://budgetpixel.com/api
---
