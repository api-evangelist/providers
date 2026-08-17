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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The Skybox Exports API from Blockade Games — 2 operation(s) for skybox exports.
  name: Blockade Games Skybox Exports API
  slug: blockade-games-skybox-exports-api
- description: The Skyboxes API from Blockade Games — 8 operation(s) for skyboxes.
  name: Blockade Games Skyboxes API
  slug: blockade-games-skyboxes-api
artifact_total: 9
asyncapis:
- description: ''
  name: Blockade Games Webhooks
  slug: blockade-games-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blockade Labs API Documentation Skybox Exports API
  slug: open-blockade-games-skybox-exports-api
- collection_type: open
  name: Blockade Labs API Documentation Skybox Exports Skyboxes API
  slug: open-blockade-games-skyboxes-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/blockade-games-skybox-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.blockadelabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-documentation.blockadelabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-documentation.blockadelabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-documentation.blockadelabs.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-documentation.blockadelabs.com/api/
- group: company
  title: ''
  type: Blog
  url: https://www.blockadelabs.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.blockadelabs.com/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blockade-Games
- group: commercial
  title: ''
  type: Pricing
  url: https://skybox.blockadelabs.com/membership
- group: start
  title: ''
  type: SignUp
  url: https://skybox.blockadelabs.com/signup
- group: start
  title: ''
  type: Login
  url: https://skybox.blockadelabs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockadelabs.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockadelabs.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://ed7hj152vhk.typeform.com/to/PHuboGPh
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/blockadelabs/workspace/public-workspace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blockadelabs.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/blockade-games-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockade-games-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blockade-games-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blockade-games-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blockade-games-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blockade-games-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blockade-games-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blockade-games-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/blockade-games-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blockade-games-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blockade-games-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockade-games-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blockade-games-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/blockade-games-generate-skybox.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/blockade-games-export-skybox.md
created: '2026-07-17'
description: Blockade Games (operating as Blockade Labs) is the maker of Skybox AI, an AI-powered platform that generates production-ready 360 equirectangular panoramas and skyboxes from text prompts, along with depth maps for 3D scenes. It offers a public REST API for asynchronous skybox generation, style selection, remixing, history, and multi-format exports, with delivery via webhooks and Pusher realtime events. First-party SDKs ship for JavaScript/TypeScript (npm), PHP/Laravel (Packagist), and Unity (C#), plus engine and tool integrations for Blender, Unreal, Godot, Roblox, SketchUp, and Figma. The product serves game, VR/AR, film, e-commerce, and education teams.
image: https://static.wixstatic.com/media/8d6639_b2ee76a88e224659804c1ef09c7bc5da~mv2.jpg/v1/fit/w_2500,h_1330,al_c/8d6639_b2ee76a88e224659804c1ef09c7bc5da~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: blockade-games-mcp.yml
  slug: blockade-games-mcpyml
modified: '2026-07-18'
name: Blockade Games
nav: Providers
network: true
overview: 'Blockade Games publishes 2 APIs on the [APIs.io](https://apis.io/) network: Skybox Exports API and Skyboxes API. Tagged areas include Company, Artificial Intelligence, Image Generation, 3D, and Gaming.


  The Blockade Games catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blockade Games'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
random_paper: 50
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 62.7
    developer_ergonomics: 73.4
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 34.2
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockade-games/refs/heads/main/screenshots/blockade-games-2026-07-25T203333.png
security:
- kind: authentication
  name: Blockade Games Authentication
  slug: blockade-games-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blockade Games Domain Security
  slug: blockade-games-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockade-games
tags:
- Company
- Artificial Intelligence
- Image Generation
- 3D
- Gaming
- Virtual Reality
- Content Generation
- Skybox
website: https://www.blockadelabs.com/
---
