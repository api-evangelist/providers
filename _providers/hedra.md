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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hedra Agentic Access
  operation_count: 9
  slug: hedra-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: Public endpoints are available to API users.
  name: Hedra Public API
  slug: hedra-public-api
arazzos:
- description: Pick a voice, submit a text-to-speech generation, and poll for the audio.
  name: Hedra — Generate text-to-speech audio
  slug: hedra-generate-audio
- description: Upload an image and an audio track, submit an avatar video generation, and poll for the result.
  name: Hedra — Generate an avatar (talking-head) video
  slug: hedra-generate-avatar-video
- description: Submit an image generation and poll until the image is ready.
  name: Hedra — Generate an image from a text prompt
  slug: hedra-generate-image
- description: Upload a start keyframe image, submit a video generation, and poll for the result.
  name: Hedra — Generate a video from a start image
  slug: hedra-generate-video
artifact_total: 10
asyncapis:
- description: ''
  name: Hedra Webhooks
  slug: hedra-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hedra-web-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hedra.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.hedra.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.hedra.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hedra.com/docs/pages/developer/getting_started/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hedra.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.hedra.com/auth/start?flow=signup
- group: start
  title: ''
  type: Login
  url: https://www.hedra.com/auth/start?flow=login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hedra.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hedra.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.hedra.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.hedra.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hedra-labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hedra.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hedra-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hedra-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/hedra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hedra-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hedra-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hedra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hedra-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hedra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hedra-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hedra-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hedra-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hedra-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hedra-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hedra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hedra-generate-image.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hedra-generate-video.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hedra-generate-avatar-video.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hedra-generate-audio.yml
created: '2026-07-17'
description: Hedra is a generative-media AI lab and creative platform that lets you produce image, video, and audio content through a web studio and a developer API. Its proprietary Character-3 model powers expressive talking-head and character video, and the platform brokers access to leading partner models (Veo, Kling, Grok, Nano Banana Pro, Flux, Sana) behind one credit-based account. The Hedra Web API exposes a small, uniform surface — list models and voices, upload assets, submit generations (image, video, avatar, text-to-speech, voice clone, upscale, video-to-video), poll generation status, and check billing credits — authenticated with an X-API-Key header. Hedra ships first-party Python, Node/TypeScript, and Rust CLI clients. Backed by a16z.
image: https://www.hedra.com/assets/logo/light.svg
layout: provider
mcp_servers:
- description: ''
  name: hedra-mcp.yml
  slug: hedra-mcpyml
modified: '2026-07-19'
name: Hedra
nav: Providers
network: true
overview: 'Hedra publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Artificial Intelligence, Generative AI, Video Generation, and Image Generation.


  The Hedra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hedra''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 26 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.4
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hedra/refs/heads/main/screenshots/hedra-2026-07-25T220905.png
security:
- kind: authentication
  name: Hedra Authentication
  slug: hedra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hedra Domain Security
  slug: hedra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hedra
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video Generation
- Image Generation
- Audio Generation
- Text to Speech
- Avatars
- Media
- Machine Learning
website: https://www.hedra.com/docs
---
