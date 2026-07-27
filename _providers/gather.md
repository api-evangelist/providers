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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: Manage the email guestlist (members/guests) of a space
  name: Gather Guestlist API
  slug: gather-guestlist-api
- description: Read and write the map/room data of a space
  name: Gather Maps API
  slug: gather-maps-api
- description: Create and manage Gather spaces
  name: Gather Spaces API
  slug: gather-spaces-api
artifact_total: 6
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gather-http-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gather-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gather-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/gather-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gather-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gather-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gather-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gather-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gather-http-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/gather-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gather-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gather-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gather.town/
- group: design
  title: ''
  type: Conventions
  url: conventions/gather-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gather-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.gather.town/hc/en-us/categories/api-integration
- group: docs
  title: ''
  type: Documentation
  url: https://gathertown.notion.site/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444
- group: docs
  title: ''
  type: APIReference
  url: https://gathertown.notion.site/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/gathertown/api-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gathertown
- group: operate
  title: ''
  type: Support
  url: https://support.gather.town/
- group: company
  title: ''
  type: Blog
  url: https://gather.town/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gather.town/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gather.town/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gather.town/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gather.town/privacy
- group: company
  title: ''
  type: Website
  url: https://gather.town/
created: '2026-07-17'
description: Gather (gather.town) is a video-calling platform that places people in a navigable 2D virtual space, letting multiple groups hold separate conversations in parallel and walk in and out of them as easily as they would in real life. It is used for remote and hybrid offices, conferences, and events. Gather exposes a public HTTP API for programmatically creating spaces and reading/writing the map (room) data of a space, plus managing a space's email guestlist, and a realtime WebSocket "game" API (via the official @gathertown/gather-game-client SDK) for subscribing to player/movement/chat events and driving avatars or bots. API keys are generated at gather.town/apiKeys and require Admin or Builder permission on the target space. Gather was surfaced as a portfolio company of Index Ventures and True Ventures and enriched into the API Evangelist network.
image: https://app.gather.town/images/site/site_preview.png
layout: provider
mcp_servers:
- description: ''
  name: gather-mcp.yml
  slug: gather-mcpyml
modified: '2026-07-19'
name: Gather
nav: Providers
network: true
overview: 'Gather publishes 3 APIs on the [APIs.io](https://apis.io/) network: Guestlist API, Maps API, and Spaces API. Tagged areas include Company, Future Of Work, Virtual Office, Video Conferencing, and Collaboration.


  Gather''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 51.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gather/refs/heads/main/screenshots/gather-2026-07-25T215458.png
security:
- kind: authentication
  name: Gather Authentication
  slug: gather-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gather Domain Security
  slug: gather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gather
tags:
- Company
- Future Of Work
- Virtual Office
- Video Conferencing
- Collaboration
- Metaverse
- Remote Work
- Events
website: https://gather.town/
---
