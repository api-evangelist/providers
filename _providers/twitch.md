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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Twitch Agentic Access
  operation_count: 107
  slug: twitch-agentic-access
  summary_line: 107 operations · 53 acting
api_count: 6
apis:
- baseURL: https://api.twitch.tv/helix/eventsub
  baseurl_source: declared
  description: EventSub is Twitch's webhook-based subscription service for receiving real-time notifications about events on Twitch.
  name: Twitch EventSub
  slug: twitch-eventsub
- baseURL: wss://irc-ws.chat.twitch.tv:443
  baseurl_source: declared
  description: IRC and WebSocket-based APIs for integrating with Twitch chat.
  name: Twitch Chat API
  slug: twitch-chat-api
- description: APIs for embedding Twitch live streams, video on demand, clips, and chat into external websites.
  name: Twitch Embed API
  slug: twitch-embed-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage and start commercial ad breaks
  name: Twitch Ads API
  slug: twitch-ads-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve Drops analytics
  name: Twitch Analytics API
  slug: twitch-analytics-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve Bits leaderboard and Cheermote information
  name: Twitch Bits API
  slug: twitch-bits-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage custom channel point rewards and redemptions
  name: Twitch Channel Points API
  slug: twitch-channel-points-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage channel information and editors
  name: Twitch Channels API
  slug: twitch-channels-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Game character data
  name: Twitch Characters API
  slug: twitch-characters-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve charity campaign information
  name: Twitch Charity API
  slug: twitch-charity-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage chat settings, emotes, badges, and announcements
  name: Twitch Chat API
  slug: twitch-chat-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Create and retrieve clips
  name: Twitch Clips API
  slug: twitch-clips-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Game collections and franchises
  name: Twitch Collections API
  slug: twitch-collections-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Game company data
  name: Twitch Companies API
  slug: twitch-companies-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage EventSub conduits and shards
  name: Twitch Conduits API
  slug: twitch-conduits-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Extension configuration service
  name: Twitch Configuration API
  slug: twitch-configuration-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage Drops entitlements and fulfillment
  name: Twitch Entitlements API
  slug: twitch-entitlements-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage EventSub subscriptions
  name: Twitch EventSub API
  slug: twitch-eventsub-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Analytics data for extensions
  name: Twitch Extension Analytics API
  slug: twitch-extension-analytics-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage and query extension information
  name: Twitch Extensions API
  slug: twitch-extensions-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Analytics data for games
  name: Twitch Game Analytics API
  slug: twitch-game-analytics-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve game/category information
  name: Twitch Games API
  slug: twitch-games-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Game genre data
  name: Twitch Genres API
  slug: twitch-genres-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve creator goals
  name: Twitch Goals API
  slug: twitch-goals-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve Hype Train events
  name: Twitch Hype Train API
  slug: twitch-hype-train-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Ingest server information for broadcasting
  name: Twitch Ingest API
  slug: twitch-ingest-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Screenshots, artwork, and videos
  name: Twitch Media API
  slug: twitch-media-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage channel moderation including bans, blocks, and AutoMod
  name: Twitch Moderation API
  slug: twitch-moderation-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Gaming platform data
  name: Twitch Platforms API
  slug: twitch-platforms-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Create and manage channel polls
  name: Twitch Polls API
  slug: twitch-polls-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Create and manage channel predictions
  name: Twitch Predictions API
  slug: twitch-predictions-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Extension PubSub messaging
  name: Twitch Pubsub API
  slug: twitch-pubsub-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Start and cancel raids
  name: Twitch Raids API
  slug: twitch-raids-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage channel stream schedules
  name: Twitch Schedule API
  slug: twitch-schedule-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Search for channels and categories
  name: Twitch Search API
  slug: twitch-search-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve stream information and markers
  name: Twitch Streams API
  slug: twitch-streams-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve subscription information
  name: Twitch Subscriptions API
  slug: twitch-subscriptions-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Retrieve team information
  name: Twitch Teams API
  slug: twitch-teams-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Game theme data
  name: Twitch Themes API
  slug: twitch-themes-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Extension Bits transactions
  name: Twitch Transactions API
  slug: twitch-transactions-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage user information and blocks
  name: Twitch Users API
  slug: twitch-users-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Manage and retrieve videos
  name: Twitch Videos API
  slug: twitch-videos-api
- baseURL: https://api.twitch.tv/helix
  baseurl_source: declared
  description: Send whisper messages
  name: Twitch Whispers API
  slug: twitch-whispers-api
artifact_total: 117
asyncapis:
- description: EventSub is Twitch's event-driven subscription service for receiving real-time notifications about events on Twitch. Supports webhook, WebSocket, and conduit transport methods. Subscribe to events suc
  name: Twitch EventSub
  slug: twitch-eventsub-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Twitch Drops Ads API
  slug: open-twitch-ads-api
- collection_type: open
  name: Twitch Drops Ads Analytics API
  slug: open-twitch-analytics-api
- collection_type: open
  name: Twitch Drops Ads Bits API
  slug: open-twitch-bits-api
- collection_type: open
  name: Twitch Drops Ads Channel Points API
  slug: open-twitch-channel-points-api
- collection_type: open
  name: Twitch Drops Ads Channels API
  slug: open-twitch-channels-api
- collection_type: open
  name: Twitch Drops Ads Characters API
  slug: open-twitch-characters-api
- collection_type: open
  name: Twitch Drops Ads Charity API
  slug: open-twitch-charity-api
- collection_type: open
  name: Twitch Drops Ads Chat API
  slug: open-twitch-chat-api
- collection_type: open
  name: Twitch Drops Ads Clips API
  slug: open-twitch-clips-api
- collection_type: open
  name: Twitch Drops Ads Collections API
  slug: open-twitch-collections-api
- collection_type: open
  name: Twitch Drops Ads Companies API
  slug: open-twitch-companies-api
- collection_type: open
  name: Twitch Drops Ads Conduits API
  slug: open-twitch-conduits-api
- collection_type: open
  name: Twitch Drops Ads Configuration API
  slug: open-twitch-configuration-api
- collection_type: open
  name: Twitch Drops API
  slug: open-twitch-drops
- collection_type: open
  name: Twitch Drops Ads Entitlements API
  slug: open-twitch-entitlements-api
- collection_type: open
  name: Twitch Drops Ads EventSub API
  slug: open-twitch-eventsub-api
- collection_type: open
  name: Twitch Drops Ads Extension Analytics API
  slug: open-twitch-extension-analytics-api
- collection_type: open
  name: Twitch Drops Ads Extensions API
  slug: open-twitch-extensions-api
- collection_type: open
  name: Twitch Extensions API
  slug: open-twitch-extensions
- collection_type: open
  name: Twitch Drops Ads Game Analytics API
  slug: open-twitch-game-analytics-api
- collection_type: open
  name: Twitch Drops Ads Games API
  slug: open-twitch-games-api
- collection_type: open
  name: Twitch Drops Ads Genres API
  slug: open-twitch-genres-api
- collection_type: open
  name: Twitch Drops Ads Goals API
  slug: open-twitch-goals-api
- collection_type: open
  name: Twitch Helix API
  slug: open-twitch-helix
- collection_type: open
  name: Twitch Drops Ads Hype Train API
  slug: open-twitch-hype-train-api
- collection_type: open
  name: Twitch IGDB API
  slug: open-twitch-igdb
- collection_type: open
  name: Twitch Drops Ads Ingest API
  slug: open-twitch-ingest-api
- collection_type: open
  name: Twitch Insights and Analytics API
  slug: open-twitch-insights-analytics
- collection_type: open
  name: Twitch Drops Ads Media API
  slug: open-twitch-media-api
- collection_type: open
  name: Twitch Drops Ads Moderation API
  slug: open-twitch-moderation-api
- collection_type: open
  name: Twitch Drops Ads Platforms API
  slug: open-twitch-platforms-api
- collection_type: open
  name: Twitch Drops Ads Polls API
  slug: open-twitch-polls-api
- collection_type: open
  name: Twitch Drops Ads Predictions API
  slug: open-twitch-predictions-api
- collection_type: open
  name: Twitch Drops Ads Pubsub API
  slug: open-twitch-pubsub-api
- collection_type: open
  name: Twitch Drops Ads Raids API
  slug: open-twitch-raids-api
- collection_type: open
  name: Twitch Drops Ads Schedule API
  slug: open-twitch-schedule-api
- collection_type: open
  name: Twitch Drops Ads Search API
  slug: open-twitch-search-api
- collection_type: open
  name: Twitch Drops Ads Streams API
  slug: open-twitch-streams-api
- collection_type: open
  name: Twitch Drops Ads Subscriptions API
  slug: open-twitch-subscriptions-api
- collection_type: open
  name: Twitch Drops Ads Teams API
  slug: open-twitch-teams-api
- collection_type: open
  name: Twitch Drops Ads Themes API
  slug: open-twitch-themes-api
- collection_type: open
  name: Twitch Drops Ads Transactions API
  slug: open-twitch-transactions-api
- collection_type: open
  name: Twitch Drops Ads Users API
  slug: open-twitch-users-api
- collection_type: open
  name: Twitch Video Broadcast API
  slug: open-twitch-video-broadcast
- collection_type: open
  name: Twitch Drops Ads Videos API
  slug: open-twitch-videos-api
- collection_type: open
  name: Twitch Drops Ads Whispers API
  slug: open-twitch-whispers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/twitch-capability-edges.yml
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


  Twitch''s developer surface includes authentication, developer console, engineering blog, GitHub presence, support, changelog, and 30 more developer resources.'
plans:
- name: Twitch Plans Pricing
  plan_count: 1
  slug: twitch-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Twitch Rate Limits
  slug: twitch-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Twitch API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: twitch-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Twitch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: twitch-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Twitch API Rules
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
  composite: 51.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 69.1
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
