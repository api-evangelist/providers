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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
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
  name: EmbodyMe MCP Server
  slug: embodyme-mcp-server
modified: '2026-07-19'
name: EmbodyMe
nav: Providers
network: true
overview: 'EmbodyMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Avatars, Digital Humans, and Neural Rendering.


  EmbodyMe''s developer surface includes developer portal, documentation, getting-started guide, signup flow, pricing, authentication, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.0
  provenance:
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
