---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Twitch Agentic Access
  operation_count: 107
  slug: twitch-agentic-access
  summary_line: 107 operations · 53 acting
api_count: 43
apis:
- description: EventSub is Twitch's webhook-based subscription service for receiving real-time notifications about events on Twitch.
  name: Twitch EventSub
  slug: twitch-eventsub
- description: IRC and WebSocket-based APIs for integrating with Twitch chat.
  name: Twitch Chat API
  slug: twitch-chat-api
- description: APIs for embedding Twitch live streams, video on demand, clips, and chat into external websites.
  name: Twitch Embed API
  slug: twitch-embed-api
- description: Manage and start commercial ad breaks
  name: Twitch Ads API
  slug: twitch-ads-api
- description: Retrieve Drops analytics
  name: Twitch Analytics API
  slug: twitch-analytics-api
- description: Retrieve Bits leaderboard and Cheermote information
  name: Twitch Bits API
  slug: twitch-bits-api
- description: Manage custom channel point rewards and redemptions
  name: Twitch Channel Points API
  slug: twitch-channel-points-api
- description: Manage channel information and editors
  name: Twitch Channels API
  slug: twitch-channels-api
- description: Game character data
  name: Twitch Characters API
  slug: twitch-characters-api
- description: Retrieve charity campaign information
  name: Twitch Charity API
  slug: twitch-charity-api
- description: Manage chat settings, emotes, badges, and announcements
  name: Twitch Chat API
  slug: twitch-chat-api
- description: Create and retrieve clips
  name: Twitch Clips API
  slug: twitch-clips-api
- description: Game collections and franchises
  name: Twitch Collections API
  slug: twitch-collections-api
- description: Game company data
  name: Twitch Companies API
  slug: twitch-companies-api
- description: Manage EventSub conduits and shards
  name: Twitch Conduits API
  slug: twitch-conduits-api
- description: Extension configuration service
  name: Twitch Configuration API
  slug: twitch-configuration-api
- description: Manage Drops entitlements and fulfillment
  name: Twitch Entitlements API
  slug: twitch-entitlements-api
- description: Manage EventSub subscriptions
  name: Twitch EventSub API
  slug: twitch-eventsub-api
- description: Analytics data for extensions
  name: Twitch Extension Analytics API
  slug: twitch-extension-analytics-api
- description: Manage and query extension information
  name: Twitch Extensions API
  slug: twitch-extensions-api
- description: Analytics data for games
  name: Twitch Game Analytics API
  slug: twitch-game-analytics-api
- description: Retrieve game/category information
  name: Twitch Games API
  slug: twitch-games-api
- description: Game genre data
  name: Twitch Genres API
  slug: twitch-genres-api
- description: Retrieve creator goals
  name: Twitch Goals API
  slug: twitch-goals-api
- description: Retrieve Hype Train events
  name: Twitch Hype Train API
  slug: twitch-hype-train-api
- description: Ingest server information for broadcasting
  name: Twitch Ingest API
  slug: twitch-ingest-api
- description: Screenshots, artwork, and videos
  name: Twitch Media API
  slug: twitch-media-api
- description: Manage channel moderation including bans, blocks, and AutoMod
  name: Twitch Moderation API
  slug: twitch-moderation-api
- description: Gaming platform data
  name: Twitch Platforms API
  slug: twitch-platforms-api
- description: Create and manage channel polls
  name: Twitch Polls API
  slug: twitch-polls-api
- description: Create and manage channel predictions
  name: Twitch Predictions API
  slug: twitch-predictions-api
- description: Extension PubSub messaging
  name: Twitch Pubsub API
  slug: twitch-pubsub-api
- description: Start and cancel raids
  name: Twitch Raids API
  slug: twitch-raids-api
- description: Manage channel stream schedules
  name: Twitch Schedule API
  slug: twitch-schedule-api
- description: Search for channels and categories
  name: Twitch Search API
  slug: twitch-search-api
- description: Retrieve stream information and markers
  name: Twitch Streams API
  slug: twitch-streams-api
- description: Retrieve subscription information
  name: Twitch Subscriptions API
  slug: twitch-subscriptions-api
- description: Retrieve team information
  name: Twitch Teams API
  slug: twitch-teams-api
- description: Game theme data
  name: Twitch Themes API
  slug: twitch-themes-api
- description: Extension Bits transactions
  name: Twitch Transactions API
  slug: twitch-transactions-api
- description: Manage user information and blocks
  name: Twitch Users API
  slug: twitch-users-api
- description: Manage and retrieve videos
  name: Twitch Videos API
  slug: twitch-videos-api
- description: Send whisper messages
  name: Twitch Whispers API
  slug: twitch-whispers-api
artifact_total: 76
asyncapis:
- description: EventSub is Twitch's event-driven subscription service for receiving real-time notifications about events on Twitch. Supports webhook, WebSocket, and conduit transport methods. Subscribe to events suc
  name: Twitch EventSub
  slug: twitch-eventsub-asyncapi
collections:
- collection_type: open
  name: Twitch Drops API
  slug: open-twitch-drops
- collection_type: open
  name: Twitch Extensions API
  slug: open-twitch-extensions
- collection_type: open
  name: Twitch Helix API
  slug: open-twitch-helix
- collection_type: open
  name: Twitch IGDB API
  slug: open-twitch-igdb
- collection_type: open
  name: Twitch Insights and Analytics API
  slug: open-twitch-insights-analytics
- collection_type: open
  name: Twitch Video Broadcast API
  slug: open-twitch-video-broadcast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twitch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twitch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twitch-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/twitch-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twitch-tv
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.twitch.tv/
- group: start
  title: ''
  type: Console
  url: https://dev.twitch.tv/console
- group: company
  title: ''
  type: Blog
  url: https://blog.twitch.tv/en/tags/developers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/twitchdev
- group: build
  title: ''
  type: Extensions
  url: https://dev.twitch.tv/docs/extensions
- group: build
  title: ''
  type: CLI Tools
  url: https://dev.twitch.tv/docs/cli
- group: operate
  title: ''
  type: Support
  url: https://dev.twitch.tv/support/
- group: operate
  title: ''
  type: Forums
  url: https://discuss.dev.twitch.com/
- group: other
  title: ''
  type: Feedback
  url: https://twitch.uservoice.com/forums/310213-developers
- group: operate
  title: ''
  type: Community Resources
  url: https://dev.twitch.tv/code/
- group: other
  title: ''
  type: Products
  url: https://dev.twitch.tv/products/
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.twitch.tv/docs/change-log/
- group: design
  title: ''
  type: Product Lifecycle
  url: https://dev.twitch.tv/docs/product-lifecycle/
- group: auth
  title: ''
  type: Authentication
  url: https://dev.twitch.tv/docs/authentication
- group: other
  title: ''
  type: Mobile Deep Links
  url: https://dev.twitch.tv/docs/mobile-deeplinks/
- group: build
  title: ''
  type: Game Engine Plugins
  url: https://dev.twitch.tv/docs/game-engine-plugins/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.twitch.tv/p/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twitch.tv/p/legal/privacy-notice/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/twitch-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-channel-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-clip-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-subscription-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/twitch-video-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/twitch-stream-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/twitch-channel-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/twitch-user-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/twitch-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/twitch-rules.yml
created: '2024'
description: Twitch is a live streaming platform for gamers, content creators, and communities.
examples:
- key_count: 2
  name: Twitch Create Clip Example
  slug: twitch-create-clip-example
- key_count: 2
  name: Twitch Get Clips Example
  slug: twitch-get-clips-example
- key_count: 2
  name: Twitch Get Streams Example
  slug: twitch-get-streams-example
- key_count: 2
  name: Twitch Get Users Example
  slug: twitch-get-users-example
- key_count: 2
  name: Twitch Search Channels Example
  slug: twitch-search-channels-example
finops:
- name: Twitch Finops
  service_category: Streaming Developer API
  slug: twitch-finops
graphqls:
- description: Twitch uses GraphQL internally for its web and mobile clients. While Twitch does not offer an officially supported public GraphQL API, the internal GQL endpoint at `https://gql.twitch.tv/gql` is widel
  name: Twitch GraphQL
  slug: twitch-graphql
image: https://www.twitch.tv/favicon.ico
json_schemas:
- name: Twitch Channel
  property_count: 11
  slug: twitch-channel
- name: Twitch Clip
  property_count: 16
  slug: twitch-clip
- name: Twitch Stream
  property_count: 14
  slug: twitch-stream
- name: Twitch Subscription
  property_count: 12
  slug: twitch-subscription
- name: Twitch User
  property_count: 10
  slug: twitch-user
- name: Twitch Video
  property_count: 17
  slug: twitch-video
json_structures:
- name: Twitch Channel Structure
  property_count: 11
  slug: twitch-channel-structure
- name: Twitch Stream Structure
  property_count: 14
  slug: twitch-stream-structure
- name: Twitch User Structure
  property_count: 11
  slug: twitch-user-structure
jsonld:
- class_count: 0
  name: Twitch Context
  property_count: 11
  slug: twitch-context
layout: provider
modified: '2026-05-19'
name: Twitch
nav: Providers
network: true
overview: 'Twitch publishes 42 APIs on the [APIs.io](https://apis.io/) network, including EventSub, Chat API, Ads API, and 39 more. Tagged areas include Entertainment, Gaming, Live Video, Streaming, and Video.


  The Twitch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Twitch''s developer surface includes authentication, developer console, engineering blog, GitHub presence, support, changelog, and 29 more developer resources.'
plans:
- name: Twitch Plans Pricing
  plan_count: 1
  slug: twitch-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 4
  name: Twitch Rate Limits
  slug: twitch-rate-limits
rules:
- name: Twitch API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: twitch-asyncapi-spectral-rules
- name: Twitch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: twitch-jsonschema-spectral-rules
- name: Twitch API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 4
    info: 0
    warn: 4
  slug: twitch-rules
scopes:
- name: Twitch Scopes
  scope_count: 42
  slug: twitch-scopes
  summary_line: 42 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 55.3
  delta: -1.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 76.0
    developer_ergonomics: 32.6
    discoverability: 66.7
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twitch/refs/heads/main/screenshots/twitch-2026-06-20T195857.png
security:
- kind: authentication
  name: Twitch Authentication
  slug: twitch-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Twitch Domain Security
  slug: twitch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: twitch
tags:
- Entertainment
- Gaming
- Live Video
- Streaming
- Video
website: https://dev.twitch.tv/
---
