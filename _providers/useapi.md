---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-03'
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
  description: InsightFaceSwap API v1 by useapi.net
  name: useapi.net Faceswap API
  slug: useapi-faceswap-api
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
  description: MiniMax API v1 by useapi.net
  name: useapi.net Minimax API
  slug: useapi-minimax-api
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
artifact_total: 28
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
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-google-flow-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-flowmusic-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-dreamina-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-kling-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-minimax-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-runwayml-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-pixverse-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-mureka-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/useapi-tempolor-v1-overlay.yaml
- group: other
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
  title: ''
  type: PostmanCollection
  url: postman/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/useapi-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/useapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/useapi-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/useapi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/useapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/useapi-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/useapi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/useapi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/useapi-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/useapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/useapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/useapi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/useapi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/useapi-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/useapi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/useapi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/useapi-jobs-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
description: useapi.net is an experimental, unified REST API platform that fronts a set of consumer AI content-generation services — video, image, music, speech and face-swap models — behind one flat $15/month subscription and a single bearer-token API surface, so developers do not have to hold a separate developer account with each underlying provider. Ten services are exposed today (Google Flow, Flow Music, Dreamina, Kling, MiniMax/Hailuo, Runway, PixVerse, Mureka, TemPolor and InsightFaceSwap), each as its own versioned REST API under api.useapi.net with its own native request/response shapes. The platform is built around bring-your-own-account access — the caller links one or more of their existing accounts on the underlying AI service and useapi.net performs automated multi-account load balancing, quarantine of rate-limited accounts, asynchronous job handling and replyUrl webhook callbacks on job completion or failure. It is a reverse-engineered, explicitly experimental service, positioned
  as substantially cheaper than the official first-party APIs of the services it wraps.
image: https://useapi.net/assets/images/logo.png
layout: provider
modified: '2026-07-27'
name: useapi.net
nav: Providers
network: true
overview: 'useapi.net publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Dreamina API, Faceswap API, and 9 more. Tagged areas include Company, Artificial Intelligence, Generative AI, Video Generation, and Image-Generation.


  The useapi.net catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  useapi.net''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 41 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 21.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 41.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 20
      marker_coverage: 90.9
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/useapi/refs/heads/main/screenshots/useapi-2026-08-17T082646.png
security:
- kind: authentication
  name: Useapi Authentication
  slug: useapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Useapi Domain Security
  slug: useapi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: useapi
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video Generation
- Image-Generation
- Music Generation
- Text-to-Speech
- Face Swap
- API Aggregator
- Machine-Learning
- Media
- Webhook
website: https://useapi.net/
---
