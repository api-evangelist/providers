---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-12'
api_count: 12
apis:
- description: REST API for Google Flow (Veo 3.1 video, Gemini Omni Flash audio-native video, Imagen 4 and Nano Banana image generation) driven through one or more linked Google accounts, with a captcha-solver pipel
  name: Google Flow API v1
  slug: google-flow-v1
- description: 'REST API for Google Flow Music (Lyria 3 Pro) — generate complete vocal or instrumental songs from a prompt, restyle with cover, remix lyrics, extend, replace and apply audio effects, plus lyrics-only '
  name: Flow Music API v1
  slug: flowmusic-v1
- description: REST API for ByteDance Dreamina (CapCut) — Seedance video models and Seedream image models, with asset upload, image and video upscale, frame interpolation and a job scheduler.
  name: Dreamina API v1
  slug: dreamina-v1
- description: REST API for Kling AI by Kuaishou — Kling v3/O3, Turbo, 2.x and 1.x video models plus lip-sync avatars, native audio, motion control, reusable elements and custom voice cloning.
  name: Kling AI API v1
  slug: kling-v1
- description: REST API for MiniMax via Hailuo AI — Hailuo video models plus third-party video, a broad image model catalog, MiniMax Speech 2.5 text-to-speech, Music 2.0, a MiniMax Agent endpoint and a free MiniMax-
  name: MiniMax / Hailuo AI API v1
  slug: minimax-v1
- description: 'REST API for Runway AI — Gen-4.x native video plus third-party video models routed through Runway, a large image model catalog, Act Two character animation, lip sync, Frames, image and video upscale, '
  name: Runway API v1
  slug: runwayml-v1
- description: REST API for PixVerse.ai — native PixVerse video models plus third-party video, a broad image catalog, music generation, text-to-speech across MiniMax and ElevenLabs voices, extend, upscale, lip sync,
  name: PixVerse API v2
  slug: pixverse-v2
- description: REST API for Mureka AI by Kunlun Tech — generate songs from lyrics, descriptions or musical styles across the Mureka V9, O2, V8 and V7.6 models, with vocal references, melody seeding, custom vocal clo
  name: Mureka API v1
  slug: mureka-v1
- description: REST API for TemPolor royalty-free music generation — create soundtracks from text prompts, custom lyrics or MIDI, with voice cloning, chord and BPM customization and export to mp3, wav and stems.
  name: TemPolor API v1
  slug: tempolor-v1
- description: REST API for the InsightFaceSwap Discord bot by Picsi.Ai — swap faces from source images onto target images with HiFidelity mode, ARTIFY effects, age transformation, multi-face morphing, background ch
  name: InsightFaceSwap API v1
  slug: faceswap-v1
- description: Cross-cutting account API for the useapi.net subscription itself — retrieve account details and the configured service accounts, set the default replyUrl webhook applied to every API, and query per-bo
  name: useapi.net Account Management API v2
  slug: account-v2
- description: Reverse-engineered REST API for Midjourney, driven through a linked Discord account. Retired — useapi.net discontinued Midjourney support on June 24, 2026. The v1 surface was previously sunset on Marc
  name: Midjourney REST API v2 (retired)
  slug: midjourney-v2
artifact_total: 16
asyncapis:
- description: ''
  name: Useapi Jobs Webhooks
  slug: useapi-jobs-webhooks
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: useapi-mcp.yml
  slug: useapi-mcpyml
modified: '2026-07-27'
name: useapi.net
nav: Providers
network: true
overview: 'useapi.net publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Google Flow API v1, Flow Music API v1, Dreamina API v1, and 8 more. Tagged areas include Company, AI, Generative AI, Video Generation, and Image Generation.


  The useapi.net catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  useapi.net''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 47
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.1
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 56.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
- AI
- Generative AI
- Video Generation
- Image Generation
- Music Generation
- Text to Speech
- Face Swap
- API Aggregator
- Machine Learning
- Media
- Webhooks
website: https://useapi.net/
---
