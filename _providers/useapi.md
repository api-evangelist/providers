---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Cross-cutting account API for the useapi.net subscription itself — retrieve account details and the configured service accounts, set the default replyUrl webhook applied to every API, and query per-bo
  name: useapi.net Account Management API v2
  slug: account-v2
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: The Account API from useapi.net — 4 operation(s) for account.
  name: useapi.net Account API
  slug: useapi-account-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: Dreamina API v1 by useapi.net
  name: useapi.net Dreamina API
  slug: useapi-dreamina-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: FlowMusic API v1 by useapi.net
  name: useapi.net Flowmusic API
  slug: useapi-flowmusic-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: Google Flow API v1 by useapi.net
  name: useapi.net Google Flow API
  slug: useapi-google-flow-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: The Jobs API from useapi.net — 12 operation(s) for jobs.
  name: useapi.net Jobs API
  slug: useapi-jobs-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: Kling API v1 by useapi.net
  name: useapi.net Kling API
  slug: useapi-kling-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: Mureka API v1 by useapi.net
  name: useapi.net Mureka API
  slug: useapi-mureka-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: PixVerse API v2 (web) by useapi.net
  name: useapi.net Pixverse API
  slug: useapi-pixverse-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: Runway API v1 by useapi.net
  name: useapi.net Runwayml API
  slug: useapi-runwayml-api
- baseURL: https://api.useapi.net/v1/google-flow
  baseurl_source: declared
  description: TemPolor API v1 by useapi.net
  name: useapi.net Tempolor API
  slug: useapi-tempolor-api
- baseURL: https://api.useapi.net/v2/account
  baseurl_source: declared
  description: InsightFaceSwap API v1 by useapi.net
  name: useapi.net Face Swap API
  slug: useapi-face-swap-api
- baseURL: https://api.useapi.net/v2/account
  baseurl_source: declared
  description: MiniMax API v1 by useapi.net
  name: useapi.net Mini Max API
  slug: useapi-mini-max-api
- baseURL: https://api.useapi.net/v1/google-vids
  baseurl_source: declared
  description: 'useapi.net''s third-party REST API over a customer''s own Google Vids account: generate avatar videos and Veo clips and manage Vids projects. useapi.net is an independent service, not affiliated with Go'
  name: useapi.net Google Vids API v1
  slug: google-vids-v1
- baseURL: https://api.useapi.net/v1/gemini-notebook
  baseurl_source: declared
  description: 'useapi.net''s third-party REST API over a customer''s own NotebookLM (Gemini Notebook) account: notebooks, sources, Audio and Video Overviews, and chat. useapi.net is an independent service, not affilia'
  name: useapi.net NotebookLM (Gemini Notebook) API v1
  slug: gemini-notebook-v1
- baseURL: https://api.useapi.net/v1/muse
  baseurl_source: declared
  description: 'useapi.net''s third-party REST API over a customer''s own Meta Muse account: Muse images, videos and agent chat. useapi.net is an independent service, not affiliated with Meta; customers connect their o'
  name: useapi.net Meta Muse API v1
  slug: muse-v1
artifact_total: 47
asyncapis:
- description: ''
  name: Useapi Jobs Webhooks
  slug: useapi-jobs-webhooks
collections:
- collection_type: open
  name: Dreamina API v1 by useapi.net
  slug: open-useapi-dreamina-v1
- collection_type: open
  name: InsightFaceSwap API v1 by useapi.net
  slug: open-useapi-faceswap-v1
- collection_type: open
  name: FlowMusic API v1 by useapi.net
  slug: open-useapi-flowmusic-v1
- collection_type: open
  name: Google Flow API v1 by useapi.net
  slug: open-useapi-google-flow-v1
- collection_type: open
  name: Kling API v1 by useapi.net
  slug: open-useapi-kling-v1
- collection_type: open
  name: Midjourney REST API by useapi.net
  slug: open-useapi-midjourney-v1
- collection_type: open
  name: Midjourney REST API v2 by useapi.net
  slug: open-useapi-midjourney-v2
- collection_type: open
  name: MiniMax API v1 by useapi.net
  slug: open-useapi-minimax-v1
- collection_type: open
  name: Mureka API v1 by useapi.net
  slug: open-useapi-mureka-v1
- collection_type: open
  name: PixVerse API v2 (web) by useapi.net
  slug: open-useapi-pixverse-v2
- collection_type: open
  name: Runway API v1 by useapi.net
  slug: open-useapi-runwayml-v1
- collection_type: open
  name: TemPolor API v1 by useapi.net
  slug: open-useapi-tempolor-v1
common:
- group: commercial
  href: https://artifacts.apis.io/useapi/plans/useapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/useapi-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-google-flow-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-google-flow-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-flowmusic-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-flowmusic-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-dreamina-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-dreamina-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-kling-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-kling-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-minimax-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-minimax-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-runwayml-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-runwayml-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-pixverse-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-pixverse-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-mureka-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-mureka-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-tempolor-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-tempolor-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/useapi/overlays/useapi-faceswap-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/useapi-faceswap-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://useapi.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://useapi.net/docs/start-here
- group: docs
  title: ''
  type: Documentation
  url: https://useapi.net/docs/subscription
- group: docs
  title: ''
  type: APIReference
  url: https://useapi.net/docs/api-google-flow-v1
- group: start
  title: ''
  type: GettingStarted
  url: https://useapi.net/docs/start-here/setup-useapi
- group: operate
  title: ''
  type: Support
  url: https://useapi.net/docs/support
- group: company
  title: ''
  type: Blog
  url: https://useapi.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useapi
- group: commercial
  title: ''
  type: Pricing
  url: https://useapi.net/docs/subscription
- group: start
  title: ''
  type: SignUp
  url: https://buy.stripe.com/8x2aEX4Bd8Vh9PMg4qeUU03
- group: start
  title: ''
  type: Login
  url: https://billing.stripe.com/p/login/28obM4fZld0JaHu6oo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useapi.net/docs/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useapi.net/docs/legal
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/useapinet/workspace/useapi-net
- group: build
  href: https://artifacts.apis.io/useapi/postman/_index.yml
  title: ''
  type: PostmanCollection
  url: postman/_index.yml
- group: start
  href: https://artifacts.apis.io/useapi/sandbox/useapi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/useapi-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/useapi/well-known/useapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/useapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/useapi/well-known/useapi-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/useapi-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/useapi/llms/useapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/useapi-llms.txt
- group: build
  href: https://artifacts.apis.io/useapi/packages/useapi-packages.yml
  title: ''
  type: Packages
  url: packages/useapi-packages.yml
- group: build
  href: https://artifacts.apis.io/useapi/packages/useapi-packages.yml
  title: ''
  type: SDKs
  url: packages/useapi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/google-flow/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/google-vids/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/muse/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/gemini-notebook/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/kling/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/mureka/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://api.useapi.net/v1/flowmusic/mcp
- group: agent
  href: https://artifacts.apis.io/useapi/mcp/useapi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/useapi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/useapi/authentication/useapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/useapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/useapi/conventions/useapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/useapi-conventions.yml
- group: operate
  href: https://artifacts.apis.io/useapi/conventions/useapi-conventions.yml
  title: ''
  type: RateLimits
  url: conventions/useapi-conventions.yml
- group: design
  href: https://artifacts.apis.io/useapi/errors/useapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/useapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/useapi/lifecycle/useapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/useapi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/useapi/lifecycle/useapi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/useapi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/useapi/changelog/useapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/useapi-changelog.yml
- group: design
  href: https://artifacts.apis.io/useapi/conformance/useapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/useapi-conformance.yml
- group: design
  href: https://artifacts.apis.io/useapi/data-model/useapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/useapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/useapi/asyncapi/useapi-jobs-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/useapi-jobs-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/useapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/useapi/security/useapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/useapi-domain-security.yml
- group: other
  title: ''
  type: ModelMatrix
  url: https://useapi.net/model-matrix
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/w28uK3cnmF
- group: other
  title: ''
  type: Telegram
  url: https://t.me/use_api
- group: docs
  title: ''
  type: SwaggerHub
  url: https://app.swaggerhub.com/apis/useapi/Midjourney_API_v2/1.0
created: '2026-07-27'
description: useapi.net is a third-party, unified REST API platform, in production since 2023, that fronts a set of consumer AI content-generation services — video, image, music, speech and face-swap models — behind one flat $15/month subscription and a single bearer-token API surface, so developers do not have to hold a separate developer account with each underlying provider. Thirteen services are exposed today (Google Flow, Flow Music, Google Vids, Gemini Notebook (NotebookLM), Meta Muse, Dreamina, Kling, MiniMax/Hailuo, Runway, PixVerse, Mureka, TemPolor and InsightFaceSwap), each as its own versioned REST API under api.useapi.net with its own native request/response shapes, and seven of them (Google Flow, Google Vids, Muse, Gemini Notebook, Kling, Mureka, Flow Music) also as hosted MCP servers (Streamable HTTP, Bearer token) listed in the official MCP Registry under net.useapi/*. useapi.net is an independent third-party service, not affiliated with Google, Meta or the other model vendors.
  The platform is built around bring-your-own-account access — the caller links one or more of their existing accounts on the underlying AI service and useapi.net performs automated multi-account load balancing, quarantine of rate-limited accounts, asynchronous job handling and replyUrl webhook callbacks on job completion or failure. It is positioned as substantially cheaper than the official first-party APIs of the services it wraps.
finops:
- has_sources: true
  method: derived
  name: Useapi Finops
  primary_unit: subscription
  service_category: ''
  slug: useapi-finops
  template: false
image: https://useapi.net/assets/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Hosted MCP server (Streamable HTTP, Bearer token; MCP Registry net.useapi/google-vids)
  slug: hosted-mcp-server-streamable-http-bearer-token-mcp-registry-net-useapi-google-vids
- description: ''
  name: Hosted MCP server (Streamable HTTP, Bearer token; MCP Registry net.useapi/gemini-notebook)
  slug: hosted-mcp-server-streamable-http-bearer-token-mcp-registry-net-useapi-gemini-notebook
- description: ''
  name: Hosted MCP server (Streamable HTTP, Bearer token; MCP Registry net.useapi/muse)
  slug: hosted-mcp-server-streamable-http-bearer-token-mcp-registry-net-useapi-muse
- description: ''
  name: useapi.net google-flow MCP server (MCP Registry net.useapi/google-flow)
  slug: useapi-net-google-flow-mcp-server-mcp-registry-net-useapi-google-flow
- description: ''
  name: useapi.net kling MCP server (MCP Registry net.useapi/kling)
  slug: useapi-net-kling-mcp-server-mcp-registry-net-useapi-kling
- description: ''
  name: useapi.net mureka MCP server (MCP Registry net.useapi/mureka)
  slug: useapi-net-mureka-mcp-server-mcp-registry-net-useapi-mureka
- description: ''
  name: useapi.net flowmusic MCP server (MCP Registry net.useapi/flowmusic)
  slug: useapi-net-flowmusic-mcp-server-mcp-registry-net-useapi-flowmusic
modified: '2026-10-19'
name: useapi.net
nav: Providers
network: true
overview: 'useapi.net publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Dreamina API, Flowmusic API, and 13 more. Tagged areas include Company, Artificial Intelligence, Generative AI, Video Generation, and Image Generation.


  The useapi.net catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  useapi.net''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 49 more developer resources.'
plans:
- name: Useapi Plans Pricing
  plan_count: 2
  slug: useapi-plans-pricing
- name: Useapi Price Estimates
  plan_count: 0
  slug: useapi-price-estimates
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: useapi.net API Rules
  rule_count: 63
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 11
  slug: useapi-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 21.8
    developer_ergonomics: 75.6
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 20
      marker_coverage: 90.9
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/useapi/useapi-2026-08-17T082646.png
security:
- kind: authentication
  name: Useapi Authentication
  slug: useapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Useapi Domain Security
  slug: useapi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 5
skills:
- name: Swap and enhance faces with InsightFaceSwap via useapi.net
  slug: useapi-faceswap-images
- name: Generate and download a song with Mureka via useapi.net
  slug: useapi-generate-music-mureka
- name: Generate a video with Google Flow (Veo) via useapi.net
  slug: useapi-generate-video-google-flow
- name: Operate useapi.net — link accounts, set webhooks, watch usage
  slug: useapi-operate-accounts-and-webhooks
- name: Generate and upscale a Runway video via useapi.net
  slug: useapi-runway-generate-and-upscale
slug: useapi
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video Generation
- Image Generation
- Music Generation
- Text-to-Speech
- Face Swap
- API Aggregator
- Machine Learning
- Media
- Webhook
website: https://useapi.net/
---
