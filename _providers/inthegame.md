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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: Inthegame Agentic Access
  operation_count: 108
  slug: inthegame-agentic-access
  summary_line: 108 operations · 71 acting
api_count: 1
apis:
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The admin API from Inthegame — 1 operation(s) for admin.
  name: Inthegame admin API
  slug: inthegame-admin-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The analytics API from Inthegame — 3 operation(s) for analytics.
  name: Inthegame analytics API
  slug: inthegame-analytics-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The category API from Inthegame — 5 operation(s) for category.
  name: Inthegame category API
  slug: inthegame-category-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The chat API from Inthegame — 3 operation(s) for chat.
  name: Inthegame chat API
  slug: inthegame-chat-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The entity API from Inthegame — 7 operation(s) for entity.
  name: Inthegame entity API
  slug: inthegame-entity-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The general API from Inthegame — 1 operation(s) for general.
  name: Inthegame general API
  slug: inthegame-general-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The item API from Inthegame — 6 operation(s) for item.
  name: Inthegame item API
  slug: inthegame-item-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The leaderboard API from Inthegame — 1 operation(s) for leaderboard.
  name: Inthegame leaderboard API
  slug: inthegame-leaderboard-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The moderationData API from Inthegame — 3 operation(s) for moderationdata.
  name: Inthegame moderationData API
  slug: inthegame-moderationdata-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The poll API from Inthegame — 7 operation(s) for poll.
  name: Inthegame poll API
  slug: inthegame-poll-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The promotion API from Inthegame — 5 operation(s) for promotion.
  name: Inthegame promotion API
  slug: inthegame-promotion-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The rating API from Inthegame — 6 operation(s) for rating.
  name: Inthegame rating API
  slug: inthegame-rating-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The shop API from Inthegame — 7 operation(s) for shop.
  name: Inthegame shop API
  slug: inthegame-shop-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The socket API from Inthegame — 1 operation(s) for socket.
  name: Inthegame socket API
  slug: inthegame-socket-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The sponsor API from Inthegame — 5 operation(s) for sponsor.
  name: Inthegame sponsor API
  slug: inthegame-sponsor-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The streamer API from Inthegame — 16 operation(s) for streamer.
  name: Inthegame streamer API
  slug: inthegame-streamer-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The translations API from Inthegame — 6 operation(s) for translations.
  name: Inthegame translations API
  slug: inthegame-translations-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The trivia API from Inthegame — 6 operation(s) for trivia.
  name: Inthegame trivia API
  slug: inthegame-trivia-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The uploads API from Inthegame — 3 operation(s) for uploads.
  name: Inthegame uploads API
  slug: inthegame-uploads-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The user API from Inthegame — 11 operation(s) for user.
  name: Inthegame user API
  slug: inthegame-user-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The wiki API from Inthegame — 5 operation(s) for wiki.
  name: Inthegame wiki API
  slug: inthegame-wiki-api
artifact_total: 48
asyncapis:
- description: Real-time viewer-engagement events pushed over Socket.IO. The socket traces server messages to the app, keeping viewer state in sync when admins inject polls, ratings, trivia, offers and wikis, and st
  name: Inthegame Realtime (Socket.IO)
  slug: inthegame-socket-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inthegame admin API
  slug: open-inthegame-admin-api
- collection_type: open
  name: Inthegame admin analytics API
  slug: open-inthegame-analytics-api
- collection_type: open
  name: Inthegame admin category API
  slug: open-inthegame-category-api
- collection_type: open
  name: Inthegame admin chat API
  slug: open-inthegame-chat-api
- collection_type: open
  name: Inthegame admin entity API
  slug: open-inthegame-entity-api
- collection_type: open
  name: Inthegame admin general API
  slug: open-inthegame-general-api
- collection_type: open
  name: Inthegame admin item API
  slug: open-inthegame-item-api
- collection_type: open
  name: Inthegame admin leaderboard API
  slug: open-inthegame-leaderboard-api
- collection_type: open
  name: Inthegame admin moderationData API
  slug: open-inthegame-moderationdata-api
- collection_type: open
  name: Inthegame admin poll API
  slug: open-inthegame-poll-api
- collection_type: open
  name: Inthegame admin promotion API
  slug: open-inthegame-promotion-api
- collection_type: open
  name: Inthegame admin rating API
  slug: open-inthegame-rating-api
- collection_type: open
  name: Inthegame admin shop API
  slug: open-inthegame-shop-api
- collection_type: open
  name: Inthegame admin socket API
  slug: open-inthegame-socket-api
- collection_type: open
  name: Inthegame admin sponsor API
  slug: open-inthegame-sponsor-api
- collection_type: open
  name: Inthegame admin streamer API
  slug: open-inthegame-streamer-api
- collection_type: open
  name: Inthegame admin translations API
  slug: open-inthegame-translations-api
- collection_type: open
  name: Inthegame admin trivia API
  slug: open-inthegame-trivia-api
- collection_type: open
  name: Inthegame admin uploads API
  slug: open-inthegame-uploads-api
- collection_type: open
  name: Inthegame admin user API
  slug: open-inthegame-user-api
- collection_type: open
  name: Inthegame admin wiki API
  slug: open-inthegame-wiki-api
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
  url: openapi/_original/inthegame-openapi.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Inthegame
nav: Providers
network: true
overview: 'Inthegame publishes 21 APIs on the [APIs.io](https://apis.io/) network, including admin API, analytics API, category API, and 18 more. Tagged areas include Company, Streaming, CTV, OTT, and Video.


  The Inthegame catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inthegame''s developer surface includes documentation, API reference, authentication, code examples, sandbox, engineering blog, support, and 17 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 64.5
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Real-Time
website: https://www.inthegame.io/
---
