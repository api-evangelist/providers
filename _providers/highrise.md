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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: WebSocket API for building and running programmable bots inside Highrise rooms. Bots receive a stream of room events (chat, emotes, reactions, joins/leaves, movement, tips, voice, DMs, moderation) and
  name: Highrise Bot API
  slug: highrise-bot-api
- description: Highrise Studio is the world-building toolset. Its Engine API and Cloud API let creators script custom worlds, games and experiences in Lua with deep customization of the Highrise runtime.
  name: Highrise Studio (Engine + Cloud API)
  slug: highrise-studio-engine-cloud-api
- description: The grabs API from Highrise — 2 operation(s) for grabs.
  name: Highrise grabs API
  slug: highrise-grabs-api
- description: The items API from Highrise — 2 operation(s) for items.
  name: Highrise items API
  slug: highrise-items-api
- description: The posts API from Highrise — 2 operation(s) for posts.
  name: Highrise posts API
  slug: highrise-posts-api
- description: The rooms API from Highrise — 2 operation(s) for rooms.
  name: Highrise rooms API
  slug: highrise-rooms-api
- description: The users API from Highrise — 2 operation(s) for users.
  name: Highrise users API
  slug: highrise-users-api
artifact_total: 11
asyncapis:
- description: Event surface of the Highrise Bot API, generated faithfully from the official highrise-bot-sdk event model (github.com/pocketzworld/python-bot-sdk, src/highrise/models.py). Bots open a single WebSocke
  name: Highrise Bot API — Event Surface
  slug: highrise-bot-api-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://highrise.game
- group: start
  title: ''
  type: DeveloperPortal
  url: https://create.highrise.game
- group: docs
  title: ''
  type: Documentation
  url: https://create.highrise.game/learn
- group: docs
  title: ''
  type: APIReference
  url: https://create.highrise.game/learn
- group: start
  title: ''
  type: GettingStarted
  url: https://create.highrise.game/learn/guides/bots/creating-a-bot
- group: operate
  title: ''
  type: Support
  url: https://support.highrise.game
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pocketzworld
- group: commercial
  title: ''
  type: TermsOfService
  url: https://highrise.game/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://highrise.game/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://highrise.game/account/settings
- group: company
  title: ''
  type: Partnerships
  url: https://create.highrise.game/partnerships
- group: build
  title: ''
  type: Packages
  url: packages/highrise-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/highrise-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/highrise-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/highrise-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/highrise-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/highrise-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/highrise-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/highrise-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/highrise-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/highrise-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/highrise-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/highrise-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/highrise-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highrise-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/highrise-web-api-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/highrise-bot-api-asyncapi.yml
created: '2026-07-17'
description: 'Highrise is a mobile-first virtual world by Pocket Worlds Inc where users create avatars, hang out in social rooms, design and trade fashion items, and build custom worlds. Alongside the consumer app, Highrise operates a developer platform for creators: a WebSocket Bot API for running programmable bots inside rooms (official Python and .NET SDKs), a read-only REST Web API exposing public users, rooms, posts, items and grabs data, and Highrise Studio with an Engine API and Cloud API for scripting worlds and games in Lua. Bots authenticate with an API token minted from the Highrise account settings and are bound to a room ID.'
image: https://highrise.game/assets/images/highrise-meta.png
layout: provider
mcp_servers:
- description: ''
  name: highrise-mcp.yml
  slug: highrise-mcpyml
modified: '2026-07-19'
name: Highrise
nav: Providers
network: true
overview: 'Highrise publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bot API, grabs API, items API, and 3 more. Tagged areas include Company, Virtual World, Metaverse, Social, and Gaming.


  The Highrise catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Highrise''s developer surface includes documentation, API reference, getting-started guide, support, CLI, authentication, changelog, and 21 more developer resources.'
random_paper: 91
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 24.8
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highrise/refs/heads/main/screenshots/highrise-2026-07-25T221206.png
security:
- kind: authentication
  name: Highrise Authentication
  slug: highrise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Highrise Domain Security
  slug: highrise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: highrise
tags:
- Company
- Virtual World
- Metaverse
- Social
- Gaming
- Avatars
- Bots
- Developer Platform
- Chat
website: https://highrise.game
---
