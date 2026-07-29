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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: Inthegame Agentic Access
  operation_count: 108
  slug: inthegame-agentic-access
  summary_line: 108 operations · 71 acting
api_count: 21
apis:
- description: The admin API from Inthegame — 1 operation(s) for admin.
  name: Inthegame admin API
  slug: inthegame-admin-api
- description: The analytics API from Inthegame — 3 operation(s) for analytics.
  name: Inthegame analytics API
  slug: inthegame-analytics-api
- description: The category API from Inthegame — 5 operation(s) for category.
  name: Inthegame category API
  slug: inthegame-category-api
- description: The chat API from Inthegame — 3 operation(s) for chat.
  name: Inthegame chat API
  slug: inthegame-chat-api
- description: The entity API from Inthegame — 7 operation(s) for entity.
  name: Inthegame entity API
  slug: inthegame-entity-api
- description: The general API from Inthegame — 1 operation(s) for general.
  name: Inthegame general API
  slug: inthegame-general-api
- description: The item API from Inthegame — 6 operation(s) for item.
  name: Inthegame item API
  slug: inthegame-item-api
- description: The leaderboard API from Inthegame — 1 operation(s) for leaderboard.
  name: Inthegame leaderboard API
  slug: inthegame-leaderboard-api
- description: The moderationData API from Inthegame — 3 operation(s) for moderationdata.
  name: Inthegame moderationData API
  slug: inthegame-moderationdata-api
- description: The poll API from Inthegame — 7 operation(s) for poll.
  name: Inthegame poll API
  slug: inthegame-poll-api
- description: The promotion API from Inthegame — 5 operation(s) for promotion.
  name: Inthegame promotion API
  slug: inthegame-promotion-api
- description: The rating API from Inthegame — 6 operation(s) for rating.
  name: Inthegame rating API
  slug: inthegame-rating-api
- description: The shop API from Inthegame — 7 operation(s) for shop.
  name: Inthegame shop API
  slug: inthegame-shop-api
- description: The socket API from Inthegame — 1 operation(s) for socket.
  name: Inthegame socket API
  slug: inthegame-socket-api
- description: The sponsor API from Inthegame — 5 operation(s) for sponsor.
  name: Inthegame sponsor API
  slug: inthegame-sponsor-api
- description: The streamer API from Inthegame — 16 operation(s) for streamer.
  name: Inthegame streamer API
  slug: inthegame-streamer-api
- description: The translations API from Inthegame — 6 operation(s) for translations.
  name: Inthegame translations API
  slug: inthegame-translations-api
- description: The trivia API from Inthegame — 6 operation(s) for trivia.
  name: Inthegame trivia API
  slug: inthegame-trivia-api
- description: The uploads API from Inthegame — 3 operation(s) for uploads.
  name: Inthegame uploads API
  slug: inthegame-uploads-api
- description: The user API from Inthegame — 11 operation(s) for user.
  name: Inthegame user API
  slug: inthegame-user-api
- description: The wiki API from Inthegame — 5 operation(s) for wiki.
  name: Inthegame wiki API
  slug: inthegame-wiki-api
artifact_total: 27
asyncapis:
- description: Real-time viewer-engagement events pushed over Socket.IO. The socket traces server messages to the app, keeping viewer state in sync when admins inject polls, ratings, trivia, offers and wikis, and st
  name: Inthegame Realtime (Socket.IO)
  slug: inthegame-socket-asyncapi
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/crimson-space-371128/workspace/inthegame-s-public-workspace/documentation/13196255-458fc2a9-5588-4940-abeb-1d6ef234d83a
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/crimson-space-371128/workspace/inthegame-s-public-workspace/documentation/13196255-458fc2a9-5588-4940-abeb-1d6ef234d83a
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/crimson-space-371128/workspace/inthegame-s-public-workspace
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/inthegame-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/inthegame-socket-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/inthegame-socket-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inthegame-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inthegame-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inthegame-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inthegame-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inthegame-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/inthegame-examples.json
- group: other
  title: ''
  type: Overlay
  url: overlays/inthegame-openapi-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/inthegame-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inthegame-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inthegame-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inthegame-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inthegame-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inthegame.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@inthegame.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inthegame.io/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inthegame.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.inthegame.io/
created: '2026-07-17'
description: 'Inthegame (Synced Apps Technologies Ltd.) is a viewer-interaction and CTV/OTT engagement platform. Its patented no-code layer injects interactive in-stream overlays — polls, trivia, ratings, wikis, offers and a points shop — into live and recorded video across smart TVs and mobile devices, driving engagement and monetization for streaming platforms and broadcasters. The API exposes two surfaces: an adminApi for broadcasters to manage streamers/channels and inject engagements, and a userApi for end-viewers to register, play, answer, chat, buy and climb real-time leaderboards, with a Socket.IO channel pushing live engagement events.'
examples:
- key_count: 91
  name: Inthegame Examples
  slug: inthegame-examples
image: https://www.inthegame.io/assets/images/6756948bfd57e173d3fa6e19_favicon_itg.png
layout: provider
mcp_servers:
- description: ''
  name: inthegame-mcp.yml
  slug: inthegame-mcpyml
modified: '2026-07-19'
name: Inthegame
nav: Providers
network: true
overview: 'Inthegame publishes 21 APIs on the [APIs.io](https://apis.io/) network, including admin API, analytics API, category API, and 18 more. Tagged areas include Company, Streaming, CTV, OTT, and Video.


  The Inthegame catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inthegame''s developer surface includes documentation, API reference, authentication, code examples, sandbox, engineering blog, support, and 17 more developer resources.'
random_paper: 77
score:
  band: developing
  composite: 42.4
  delta: -2.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 72.6
    developer_ergonomics: 47.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/screenshots/inthegame-2026-07-25T222719.png
security:
- kind: authentication
  name: Inthegame Authentication
  slug: inthegame-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inthegame Domain Security
  slug: inthegame-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inthegame
tags:
- Company
- Streaming
- CTV
- OTT
- Video
- Engagement
- Interactive
- Gamification
- Sports
- Real-time
website: https://www.inthegame.io/
---
