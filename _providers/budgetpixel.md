---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.0
  scored_at: '2026-11-06'
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
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Image-to-3D models — a picture in, a textured 3D model (GLB, plus FBX/USDZ/STL on Meshy) out
  name: BudgetPixel 3D Models API
  slug: budgetpixel-3d-models-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Turn a video into a depth map video to guide other video models with its structure and motion
  name: BudgetPixel Depth Maps API
  slug: budgetpixel-depth-maps-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Meta API from BudgetPixel — 1 operation(s) for meta.
  name: BudgetPixel Meta API
  slug: budgetpixel-meta-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Search the free stock image library — available on every plan, including Free
  name: BudgetPixel Stock Images API
  slug: budgetpixel-stock-images-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Search the free background music library — available on every plan, including Free
  name: BudgetPixel Stock Music API
  slug: budgetpixel-stock-music-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: Search the free sound effect library — available on every plan, including Free
  name: BudgetPixel Stock Sound Effects API
  slug: budgetpixel-stock-sound-effects-api
- baseURL: https://api.budgetpixel.com/v1
  baseurl_source: declared
  description: The Mini Max API from BudgetPixel — 2 operation(s) for mini max.
  name: BudgetPixel Mini Max API
  slug: budgetpixel-mini-max-api
artifact_total: 45
common:
- group: other
  href: https://artifacts.apis.io/budgetpixel/capabilities/budgetpixel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/budgetpixel-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.budgetpixel.com/
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
  href: https://artifacts.apis.io/budgetpixel/plans/budgetpixel-plans-pricing.yml
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
  href: https://artifacts.apis.io/budgetpixel/mcp/budgetpixel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/budgetpixel-mcp.yml
- group: build
  href: https://artifacts.apis.io/budgetpixel/mcp/budgetpixel-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/budgetpixel-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/budgetpixel/a2a/budgetpixel-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/budgetpixel-a2a.yml
- group: agent
  href: https://artifacts.apis.io/budgetpixel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/budgetpixel/llms/budgetpixel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/budgetpixel-llms.txt
- group: agent
  href: https://artifacts.apis.io/budgetpixel/well-known/budgetpixel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/budgetpixel-well-known.yml
- group: auth
  href: https://artifacts.apis.io/budgetpixel/authentication/budgetpixel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/budgetpixel-authentication.yml
- group: auth
  href: https://artifacts.apis.io/budgetpixel/scopes/budgetpixel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/budgetpixel-scopes.yml
- group: design
  href: https://artifacts.apis.io/budgetpixel/conventions/budgetpixel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/budgetpixel-conventions.yml
- group: design
  href: https://artifacts.apis.io/budgetpixel/errors/budgetpixel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/budgetpixel-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/budgetpixel/rate-limits/budgetpixel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/budgetpixel-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/budgetpixel/lifecycle/budgetpixel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/budgetpixel-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/budgetpixel/conformance/budgetpixel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budgetpixel-conformance.yml
- group: design
  href: https://artifacts.apis.io/budgetpixel/data-model/budgetpixel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budgetpixel-data-model.yml
- group: build
  href: https://artifacts.apis.io/budgetpixel/packages/budgetpixel-packages.yml
  title: ''
  type: Packages
  url: packages/budgetpixel-packages.yml
- group: other
  href: https://artifacts.apis.io/budgetpixel/overlays/budgetpixel-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/budgetpixel-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/budgetpixel/security/budgetpixel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budgetpixel-domain-security.yml
created: '2026-08-28'
description: 'BudgetPixel is an AI creative platform offering credit-based access to 70+ generative media models for image, video, music and sound-effect generation, plus upscaling, lip sync, motion control, format conversion and content moderation. Alongside a free design-studio canvas, LoRA training and a public community feed, it ships a unified developer surface: a 74-operation OpenAPI 3.1 REST API at api.budgetpixel.com/v1 (private beta, bearer bpx_live_* keys, Premium/Pro/Ultra plans) with an asynchronous create-then-poll job model and a POST /v1/cost endpoint that quotes the exact credit charge before you commit; a first-party remote MCP server at mcp.budgetpixel.com/mcp exposing 12 tools over streamable HTTP with OAuth 2.1 + PKCE and Google SSO; an A2A agent card and a published Agent Skill; and llms.txt indexes. One credit balance, one set of conventions, and identical published prices across every surface.'
finops:
- has_sources: true
  method: derived
  name: Budgetpixel Finops
  primary_unit: ''
  service_category: ''
  slug: budgetpixel-finops
  template: true
image: https://budgetpixel.com/logo.png
layout: provider
mcp_servers:
- description: 'PRODUCT MCP, live: 12 tools (generate_image, generate_video, generate_music, generate_sound_effect, upscale_image, upscale_video, check_generation_status, get_credit_balance...). Streamable HTTP with '
  name: BudgetPixel MCP Server
  slug: mcp
- description: Mintlify DOCUMENTATION-SEARCH MCP (search_budget_pixel_api, query_docs_filesystem_budget_pixel_api, submit_feedback) -- not the generation API. Distinct from the product MCP at mcp.budgetpixel.com/mcp
  name: BudgetPixel MCP Server
  slug: mcp-2
modified: '2026-08-28'
name: BudgetPixel
nav: Providers
network: true
overview: 'BudgetPixel publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alibaba API, Audios API, and 30 more. Tagged areas include Generative AI, AI Image Generation, AI Video Generation, AI Music Generation, and Audio Generation.


  The BudgetPixel catalog on APIs.io includes 1 Spectral governance ruleset.


  BudgetPixel''s developer surface includes documentation, API reference, getting-started guide, pricing, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Budgetpixel Plans Pricing
  plan_count: 6
  slug: budgetpixel-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Budgetpixel Rate Limits
  slug: budgetpixel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: BudgetPixel API Rules
  rule_count: 64
  severity_counts:
    error: 52
    hint: 0
    info: 4
    warn: 8
  slug: budgetpixel-rules
scopes:
- name: Budgetpixel Scopes
  scope_count: 2
  slug: budgetpixel-scopes
  summary_line: 2 scopes · authorization_code
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 52.8
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 34.2
  previous_composite: 55.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/budgetpixel/budgetpixel-2026-09-02T144959.png
security:
- kind: authentication
  name: Budgetpixel Authentication
  slug: budgetpixel-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Budgetpixel Domain Security
  slug: budgetpixel-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 3
skills:
- name: budgetpixel-generate-image
  slug: budgetpixel-generate-image
- name: budgetpixel-generate-video
  slug: budgetpixel-generate-video
- name: Budgetpixel
  slug: budgetpixel-provider-published-skill
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
- Agent-Native
- MCP
- MCP Server
- Artificial Intelligence
- Image Models
- Video Models
- Music/Audio Generation
- Generative Media
- Llms.txt
- Media Processing
- Image Generation
- Video Generation
- Upscaling
- Credit
- Model Aggregator
- A2A
website: https://www.budgetpixel.com/
---
