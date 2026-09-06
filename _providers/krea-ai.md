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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Krea Ai Agentic Access
  operation_count: 72
  slug: krea-ai-agentic-access
  summary_line: 72 operations · 64 acting
api_count: 1
apis:
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Asset management endpoints for uploading and managing images, videos, audio files, and 3D models
  name: Krea Assets API
  slug: krea-ai-assets-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Core API operations including job management and billing information
  name: Krea General API
  slug: krea-ai-general-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Image generation endpoints
  name: Krea Image API
  slug: krea-ai-image-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Image enhance endpoints
  name: Krea Image Enhance API
  slug: krea-ai-image-enhance-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Executing custom node apps built in our nodes tool
  name: Krea Node Apps API
  slug: krea-ai-node-apps-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Style (LoRA) generation and management endpoints
  name: Krea Styles API
  slug: krea-ai-styles-api
- baseURL: https://api.krea.ai
  baseurl_source: declared
  description: Video generation endpoints
  name: Krea Video API
  slug: krea-ai-video-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Krea Assets API
  slug: open-krea-ai-assets-api
- collection_type: open
  name: Krea Assets General API
  slug: open-krea-ai-general-api
- collection_type: open
  name: Krea Assets Image API
  slug: open-krea-ai-image-api
- collection_type: open
  name: Krea Assets Image Enhance API
  slug: open-krea-ai-image-enhance-api
- collection_type: open
  name: Krea Assets Node Apps API
  slug: open-krea-ai-node-apps-api
- collection_type: open
  name: Krea Assets Styles API
  slug: open-krea-ai-styles-api
- collection_type: open
  name: Krea Assets Video API
  slug: open-krea-ai-video-api
- collection_type: open
  name: Krea API
  slug: open-krea-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/krea-ai-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/krea-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/krea-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/krea-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/krea-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.krea.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.krea.ai/developers/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/CLAUDE.md
- group: commercial
  title: ''
  type: Pricing
  url: https://www.krea.ai/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://www.krea.ai/settings/api-tokens
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.krea.ai/developers/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://docs.krea.ai/developers/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/developers/job-lifecycle
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.krea.ai/developers/deprecations
- group: start
  title: ''
  type: Sandbox
  url: https://docs.krea.ai/developers/interactiveexample
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/realtime
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/image-generation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/video
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/3-d
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/edit
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/enhancer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/training
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/nodes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/teams
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/features/audio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/compute-units
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/saml-sso-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/domain-verification
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/model-access-controls
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/manage-subscriptions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.krea.ai/user-guide/help-and-support/refunds-and-billing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krea-ai
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/krea-ai/realtime-video
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/krea-ai/flux-krea
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/krea-ai/open-prompts
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/krea-ai/prompt-search
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/krea-ai/skills
- group: operate
  title: ''
  type: Forums
  url: https://krea.ai/discord
- group: company
  title: ''
  type: X-Twitter
  url: https://x.com/krea_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/krea-ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@krea_ai
- group: commercial
  title: ''
  type: Plans
  url: https://www.krea.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.krea.ai/blog
created: '2026-05-25T00:00:00.000Z'
description: Krea is a real-time AI creative suite that lets designers, filmmakers, brand teams, and everyday creators generate, edit, enhance, and animate images and videos with professional controls from a single workspace. The Krea API at https://api.krea.ai exposes 50+ third-party and proprietary image and video models — Flux, Imagen, Veo, Nano Banana, gpt-image, Runway, Kling, Seedream, Seedance, Hailuo, Wan, Ray, Grok Imagine, Ideogram, Qwen, Z Image, Topaz, and more — through one Bearer-token-authenticated REST surface with a unified async job lifecycle, compute-unit billing, asset management, LoRA style training, Nodes workflow execution, and webhook delivery. Krea also publishes open-source models including FLUX.1 Krea [dev] (in collaboration with Black Forest Labs) and Krea Realtime 14B, a Self-Forcing distillation of Wan 2.1 that produces 11 fps text-to-video on an NVIDIA B200.
features:
- One Bearer-token Krea API at https://api.krea.ai exposing 67 endpoints across image, video, enhance, assets, styles, jobs, and node-apps
- 22 image generation models across Black Forest Labs Flux (1 dev, 1 Kontext, 1.1 Pro, 1.1 Pro Ultra), Google Imagen 3/4 family and Nano Banana / Nano Banana 2 / Nano Banana Pro, OpenAI gpt-image and gpt-image-2, ByteDance Seedream 4 / Seedream 5 Lite / SeedEdit, Ideogram 2 Turbo and Ideogram 3, Runway Gen-4 Image, Luma UNI-1, Qwen 2512, and Z Image
- 31 video generation models across Google Veo 2 / Veo 3 / Veo 3 Fast / Veo 3.1 / Veo 3.1 Fast / Veo 3.1 Lite, Runway Gen-3, Gen-4 Video, Gen-4.5, and Aleph, Kling 1.0 through 3.0 plus Kling o1, MiniMax Hailuo and Hailuo 02 / 2.3 / 2.3 Fast, Alibaba Wan 2.1 / 2.2 / 2.5, ByteDance Seedance Pro and Seedance Pro Fast, Luma Ray 2, Lightricks LTX-2.3 22B, and xAI Grok Imagine
- Topaz-powered image enhancement at /generate/enhance/topaz with standard, generative, and bloom variants delivering up to 22K upscales
- Krea Realtime experience with sub-50ms image generation and an open-source Realtime 14B autoregressive video model distilled from Wan 2.1 (CC BY-NC-SA 4.0)
- Open-source FLUX.1 Krea [dev] 12B rectified-flow image model from a research collaboration with Black Forest Labs, with weights on Hugging Face
- Custom LoRA style training, search, sharing, and workspace controls via the Styles API
- Krea Nodes visual workflow tool exposed programmatically via /node-apps/{id}/execute
- Asset management API for uploading and reusing images, videos, audio, and 3D models across generation jobs
- Unified asynchronous job lifecycle (queued, processing, completed, failed, cancelled) with GET /jobs/{id} polling at 2-5s intervals and DELETE /jobs/{id} cancellation
- Webhook delivery via X-Webhook-URL header — full job payload POSTed on terminal state with no separate webhook subscription registration
- Compute-unit billing model — only completed jobs consume units; failed and cancelled jobs are free
- Plan-tiered rate limits with job-backlog queueing instead of hard rejection
- Public OpenAPI 3.1.0 spec at https://docs.krea.ai/api-reference/openapi.json plus Postman import and an interactive in-browser playground
- Code samples in cURL, Python, JavaScript, and Go on every endpoint
- Workspace, teams, SAML SSO, domain verification, model access controls, per-member spend limits, audit logs, and a separate Business / Enterprise tier
- Used by Lego, Samsung, Nike, Microsoft, and Shopify
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/krea-ai.png
layout: provider
modified: '2026-05-25'
name: Krea
nav: Providers
network: true
overview: 'Krea publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, General API, Image API, and 4 more. Tagged areas include Artificial Intelligence, Image-Generation, Video Generation, Generative AI, and Real-Time.


  Krea''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, sandbox, YouTube channel, and 39 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/krea-ai/refs/heads/main/screenshots/krea-ai-2026-06-20T184155.png
security:
- kind: authentication
  name: Krea Ai Authentication
  slug: krea-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Krea Ai Domain Security
  slug: krea-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Krea Ai Trust Center
  slug: krea-ai-trust-center
  summary_line: SOC 2
slug: krea-ai
tags:
- Artificial Intelligence
- Image-Generation
- Video Generation
- Generative AI
- Real-Time
- Multi-Modal
- Creative Tools
- 3D
- Upscaling
website: https://www.krea.ai
---
