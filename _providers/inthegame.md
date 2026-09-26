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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Inthegame Agentic Access
  operation_count: 108
  slug: inthegame-agentic-access
  summary_line: 108 operations · 67 acting
api_count: 1
apis:
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The admin API from Inthegame — 1 operation(s) for admin.
  name: Inthegame Admin API
  slug: inthegame-admin-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The analytics API from Inthegame — 3 operation(s) for analytics.
  name: Inthegame Analytics API
  slug: inthegame-analytics-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The category API from Inthegame — 5 operation(s) for category.
  name: Inthegame Category API
  slug: inthegame-category-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The chat API from Inthegame — 3 operation(s) for chat.
  name: Inthegame Chat API
  slug: inthegame-chat-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The entity API from Inthegame — 7 operation(s) for entity.
  name: Inthegame Entity API
  slug: inthegame-entity-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The general API from Inthegame — 1 operation(s) for general.
  name: Inthegame General API
  slug: inthegame-general-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The item API from Inthegame — 6 operation(s) for item.
  name: Inthegame Item API
  slug: inthegame-item-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The leaderboard API from Inthegame — 1 operation(s) for leaderboard.
  name: Inthegame Leaderboard API
  slug: inthegame-leaderboard-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The moderationData API from Inthegame — 3 operation(s) for moderationdata.
  name: Inthegame Moderation Data API
  slug: inthegame-moderationdata-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The poll API from Inthegame — 7 operation(s) for poll.
  name: Inthegame Poll API
  slug: inthegame-poll-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The promotion API from Inthegame — 5 operation(s) for promotion.
  name: Inthegame Promotion API
  slug: inthegame-promotion-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The rating API from Inthegame — 6 operation(s) for rating.
  name: Inthegame Rating API
  slug: inthegame-rating-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The shop API from Inthegame — 7 operation(s) for shop.
  name: Inthegame Shop API
  slug: inthegame-shop-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The socket API from Inthegame — 1 operation(s) for socket.
  name: Inthegame Socket API
  slug: inthegame-socket-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The sponsor API from Inthegame — 5 operation(s) for sponsor.
  name: Inthegame Sponsor API
  slug: inthegame-sponsor-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The streamer API from Inthegame — 16 operation(s) for streamer.
  name: Inthegame Streamer API
  slug: inthegame-streamer-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The translations API from Inthegame — 6 operation(s) for translations.
  name: Inthegame Translations API
  slug: inthegame-translations-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The trivia API from Inthegame — 6 operation(s) for trivia.
  name: Inthegame Trivia API
  slug: inthegame-trivia-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The uploads API from Inthegame — 3 operation(s) for uploads.
  name: Inthegame Uploads API
  slug: inthegame-uploads-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The user API from Inthegame — 11 operation(s) for user.
  name: Inthegame User API
  slug: inthegame-user-api
- baseURL: https://api-dev.inthegame.io
  baseurl_source: declared
  description: The wiki API from Inthegame — 5 operation(s) for wiki.
  name: Inthegame Wiki API
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
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/openapi/_original/inthegame-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/inthegame-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/asyncapi/inthegame-socket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/inthegame-socket-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/asyncapi/inthegame-socket-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/inthegame-socket-asyncapi.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/authentication/inthegame-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inthegame-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/conventions/inthegame-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inthegame-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/errors/inthegame-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inthegame-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/conformance/inthegame-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inthegame-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/data-model/inthegame-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inthegame-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/examples/inthegame-examples.json
  title: ''
  type: Examples
  url: examples/inthegame-examples.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/overlays/inthegame-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inthegame-openapi-overlay.yaml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/sandbox/inthegame-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/inthegame-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/mcp/inthegame-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inthegame-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/llms/inthegame-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inthegame-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/agentic-access/inthegame-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inthegame-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inthegame/refs/heads/main/security/inthegame-domain-security.yml
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
overview: 'Inthegame publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Analytics API, Category API, and 18 more. Tagged areas include Company, Streaming, CTV, OTT, and Video.


  The Inthegame catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inthegame''s developer surface includes documentation, API reference, authentication, code examples, sandbox, engineering blog, support, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 38.7
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 36.5
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
