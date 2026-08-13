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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kongregate Agentic Access
  operation_count: 15
  slug: kongregate-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 14
apis:
- description: Browser-side JavaScript API loaded by script tag from cdn1.kongregate.com. Exposes kongregate.services.* for player identity (getUserId, getUsername, getGameAuthToken, isGuest, showRegistrationBox, re
  name: Kongregate Client JavaScript API
  slug: kongregate-client-javascript-api
- description: The Authenticate.json API from Kongregate — 1 operation(s) for authenticate.json.
  name: Kongregate Authenticate.json API
  slug: kongregate-authenticate-json-api
- description: The Characters.json API from Kongregate — 1 operation(s) for characters.json.
  name: Kongregate Characters.json API
  slug: kongregate-characters-json-api
- description: The Guilds API from Kongregate — 1 operation(s) for guilds.
  name: Kongregate Guilds API
  slug: kongregate-guilds-api
- description: The Guilds.json API from Kongregate — 1 operation(s) for guilds.json.
  name: Kongregate Guilds.json API
  slug: kongregate-guilds-json-api
- description: The High Scores API from Kongregate — 2 operation(s) for high scores.
  name: Kongregate High Scores API
  slug: kongregate-high-scores-api
- description: The Items.json API from Kongregate — 1 operation(s) for items.json.
  name: Kongregate Items.json API
  slug: kongregate-items-json-api
- description: The Kongpanions API from Kongregate — 1 operation(s) for kongpanions.
  name: Kongregate Kongpanions API
  slug: kongregate-kongpanions-api
- description: The Kongpanions.json API from Kongregate — 1 operation(s) for kongpanions.json.
  name: Kongregate Kongpanions.json API
  slug: kongregate-kongpanions-json-api
- description: The Shared Links API from Kongregate — 2 operation(s) for shared links.
  name: Kongregate Shared Links API
  slug: kongregate-shared-links-api
- description: The Submit Statistics.json API from Kongregate — 1 operation(s) for submit statistics.json.
  name: Kongregate Submit Statistics.json API
  slug: kongregate-submit-statistics-json-api
- description: The Use Item.json API from Kongregate — 1 operation(s) for use item.json.
  name: Kongregate Use Item.json API
  slug: kongregate-use-item-json-api
- description: The User Info.json API from Kongregate — 1 operation(s) for user info.json.
  name: Kongregate User Info.json API
  slug: kongregate-user-info-json-api
- description: The User Items.json API from Kongregate — 1 operation(s) for user items.json.
  name: Kongregate User Items.json API
  slug: kongregate-user-items-json-api
artifact_total: 19
asyncapis:
- description: ''
  name: Kongregate Callbacks Webhooks
  slug: kongregate-callbacks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kongregate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kongregate.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kongregate.com/docs/integration-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kongregate.com/reference/server-api-authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kongregate.com/docs/kongregate-launch-101
- group: operate
  title: ''
  type: Support
  url: https://kongregatesupport.zendesk.com/hc/en-us/categories/26688218392717-Developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kongregate
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kongregate.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.kongregate.com/privacy_policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kongregate.com/en/kreds
- group: start
  title: ''
  type: SignUp
  url: https://www.kongregate.com/en/accounts/new
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kongregate-server-api-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/kongregate-server-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kongregate-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kongregate-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kongregate-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kongregate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kongregate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kongregate-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kongregate-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kongregate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kongregate-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kongregate-callbacks-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/kongregate-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kongregate-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kongregate-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kongregate-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kongregate-domain-security.yml
created: '2026-07-17'
description: 'Kongregate is a browser-game platform and publisher that hosts thousands of free online games across action, puzzle, RPG, strategy, idle and multiplayer genres. For game developers it operates a two-part developer API: a CDN-delivered client JavaScript API (with Unity WebGL bindings) handling player identity, in-page registration, statistic submission and the Kreds purchase flow; and a server-side REST API at api.kongregate.com that authenticates players, reads and consumes the Kreds virtual-goods inventory, submits statistics, reads lifetime/weekly/daily/friends leaderboards, and registers game-defined guilds and characters. Kongregate monetizes through Kreds, its own virtual currency, and rewards player engagement with badges and collectible Kongpanions. Outbound API callbacks are delivered as HMAC-SHA256 signed requests. Kongregate Inc. is backed by Lightspeed Venture Partners and Uncork Capital.'
image: https://www.kongregate.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: kongregate-mcp.yml
  slug: kongregate-mcpyml
modified: '2026-07-19'
name: Kongregate
nav: Providers
network: true
overview: 'Kongregate publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authenticate.json API, Characters.json API, Guilds API, and 10 more. Tagged areas include Company, Gaming, Games, Game Development, and Browser Games.


  The Kongregate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kongregate''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 103
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.1
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kongregate/refs/heads/main/screenshots/kongregate-2026-07-25T224157.png
security:
- kind: authentication
  name: Kongregate Authentication
  slug: kongregate-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Kongregate Domain Security
  slug: kongregate-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: kongregate
tags:
- Company
- Gaming
- Games
- Game Development
- Browser Games
- Virtual Goods
- Microtransactions
- Leaderboards
- Player Identity
- Unity
- Developer Platform
website: https://www.kongregate.com
---
