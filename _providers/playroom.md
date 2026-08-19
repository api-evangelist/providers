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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://joinplayroom.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.joinplayroom.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinplayroom.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinplayroom.com/api-reference/js
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinplayroom.com
- group: company
  title: ''
  type: Blog
  url: https://docs.joinplayroom.com/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/uDHxeRYhRe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/playroomkit
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.joinplayroom.com/billing
- group: start
  title: ''
  type: SignUp
  url: https://dev.joinplayroom.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinplayroom.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinplayroom.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playroom-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/playroom-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/playroom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/playroom-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/playroom-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/playroom-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/playroom-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/playroom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/playroom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/playroom-error-codes.yml
- group: design
  title: ''
  type: Components
  url: components/playroom-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playroom-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Playroom (Playroom Kit) is a client-side developer platform for building multiplayer apps and games in minutes. Its single JavaScript/TypeScript SDK (npm playroomkit) provides synchronized global and per-player state, an elected host model, remote procedure calls (RPCs), matchmaking and lobbies, on-screen joystick/gamepad controllers, bots, and turn-based helpers, with wrappers for Unity (C#) and Godot and support across React, Next.js, Vue, Angular, Remix, Phaser, and React Three Fiber. Apps authenticate with a read-only gameId issued from the Dev Portal rather than a server API key, and Playroom hosts the realtime infrastructure. It also embeds into Discord Activities and TikTok Live. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/playroom.png
layout: provider
mcp_servers:
- description: ''
  name: playroom-mcp.yml
  slug: playroom-mcpyml
modified: '2026-07-20'
name: Playroom
nav: Providers
network: true
overview: 'Playroom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Multiplayer, Gaming, Game Development, and Real-time.


  Playroom''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 138
score:
  band: emerging
  composite: 22.6
  delta: -9.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.2
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Playroom Authentication
  slug: playroom-authentication
  summary_line: gameId/oauth2 · 3 schemes
- kind: domain-security
  name: Playroom Domain Security
  slug: playroom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: playroom
tags:
- Company
- Multiplayer
- Gaming
- Game Development
- Real-time
- SDK
- State Synchronization
- Developer Tools
website: https://joinplayroom.com
---
