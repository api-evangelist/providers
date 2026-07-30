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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST + WebSocket API for driving real-time photorealistic AI avatars. Create meeting bots that join Google Meet or LiveKit rooms and stream a talking avatar rendered from an avatar_id, wiring audio in
  name: DigiSelf Realtime API
  slug: digiself-realtime-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://company.embodyme.com/
- group: start
  title: ''
  type: Portal
  url: https://digiself.tech/en/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/embodyme/digiself-realtime-api-sample
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/embodyme/digiself-realtime-api-sample/tree/main/quick-start-livekit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/embodyme
- group: start
  title: ''
  type: SignUp
  url: https://app.digiself.tech/subscribe-now
- group: start
  title: ''
  type: Login
  url: https://app.digiself.tech/login
- group: commercial
  title: ''
  type: Pricing
  url: https://digiself.tech/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://embodyme.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/embodyme-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/embodyme-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/embodyme-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/embodyme-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/embodyme-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/embodyme-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/embodyme-domain-security.yml
created: '2026-07-17'
description: EmbodyMe, Inc. is a Tokyo-based AI company building real-time neural rendering and 3D dense face-tracking technology for photorealistic digital humans. Its flagship developer product, DigiSelf, turns a single photo into a lifelike AI avatar that speaks from text or audio in dozens of languages, in both pre-recorded video and sub-second real-time interactive modes. The DigiSelf Realtime API (api.digiself.tech) and Stream API (WebSocket) let developers drive avatars into LiveKit rooms, Google Meet meeting bots, chatbots, live streaming, gaming, and advertising via an x-api-key protected REST + WebSocket surface. EmbodyMe also ships the xpression camera, xpression chat, and xpression avatar consumer apps and a cross-platform Real-time AI Video Generation SDK for iOS, Android, Windows, and Mac. Backed by Techstars, with recognition from NVIDIA, Microsoft, Product Hunt, and SIGGRAPH ASIA.
image: https://digiself.tech/assets/images/logo/logo_text.png
layout: provider
mcp_servers:
- description: ''
  name: embodyme-mcp.yml
  slug: embodyme-mcpyml
modified: '2026-07-19'
name: EmbodyMe
nav: Providers
network: true
overview: 'EmbodyMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Avatars, Digital Humans, and Neural Rendering.


  EmbodyMe''s developer surface includes developer portal, documentation, getting-started guide, signup flow, pricing, authentication, and 10 more developer resources.'
random_paper: 30
score:
  band: emerging
  composite: 24.5
  delta: -1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/embodyme/refs/heads/main/screenshots/embodyme-2026-07-25T213233.png
security:
- kind: authentication
  name: Embodyme Authentication
  slug: embodyme-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Embodyme Domain Security
  slug: embodyme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: embodyme
tags:
- Company
- Artificial Intelligence
- Avatars
- Digital Humans
- Neural Rendering
- Face Tracking
- Generative AI
- Video Generation
- Real-Time
- Streaming
- SDK
website: https://company.embodyme.com/
---
