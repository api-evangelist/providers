---
name: Twitch
description: Twitch is a live streaming platform for gamers, content creators, and communities.
image: https://www.twitch.tv/favicon.ico
url: https://www.twitch.tv
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.18'
tags:
  - Entertainment
  - Gaming
  - Live Video
  - Streaming
  - Video
apis:
  - name: Twitch API
    description: The Twitch API enables developers to build experiences that integrate with Twitch, including retrieving stream data, managing users, and interacting with chat.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/
    baseURL: https://api.twitch.tv/helix
    tags:
      - Chat
      - Gaming
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/api/
      - type: OpenAPI
        url: https://dev.twitch.tv/docs/api/reference
      - type: Authentication
        url: https://dev.twitch.tv/docs/authentication
      - type: Getting Started
        url: https://dev.twitch.tv/docs/api/get-started
      - type: Rate Limits
        url: https://dev.twitch.tv/docs/api/guide#rate-limits
      - type: Webhooks
        url: https://dev.twitch.tv/docs/eventsub
      - type: API Status
        url: https://devstatus.twitch.tv/
      - type: Terms of Service
        url: https://www.twitch.tv/p/legal/terms-of-service/
      - type: Privacy Policy
        url: https://www.twitch.tv/p/legal/privacy-notice/
      - type: Scopes
        url: https://dev.twitch.tv/docs/authentication/scopes/
      - type: Change Log
        url: https://dev.twitch.tv/docs/change-log/
      - type: Migration Guide
        url: https://dev.twitch.tv/docs/api/migration
      - type: Concepts
        url: https://dev.twitch.tv/docs/api/guide
      - type: Clips
        url: https://dev.twitch.tv/docs/api/clips
      - type: Videos
        url: https://dev.twitch.tv/docs/api/videos/
      - type: OpenAPI
        url: openapi/twitch-helix-openapi.yml
    contact:
      - type: Support
        url: https://help.twitch.tv/
      - type: Twitter
        url: https://twitter.com/TwitchDev
      - type: Discord
        url: https://discord.gg/twitchdev
  - name: Twitch EventSub
    description: EventSub is Twitch's webhook-based subscription service for receiving real-time notifications about events on Twitch.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/eventsub
    baseURL: https://api.twitch.tv/helix/eventsub
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/eventsub
      - type: Subscription Types
        url: https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types
      - type: WebSocket Reference
        url: https://dev.twitch.tv/docs/eventsub/websocket-reference/
      - type: Handling WebSocket Events
        url: https://dev.twitch.tv/docs/eventsub/handling-websocket-events/
      - type: Handling Conduit Events
        url: https://dev.twitch.tv/docs/eventsub/handling-conduit-events/
      - type: AsyncAPI
        url: asyncapi/twitch-eventsub-asyncapi.yml
  - name: Twitch Chat API
    description: IRC and WebSocket-based APIs for integrating with Twitch chat.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/chat
    baseURL: wss://irc-ws.chat.twitch.tv:443
    tags:
      - Chat
      - Irc
      - Messaging
      - Websocket
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/chat
      - type: Chat Commands
        url: https://dev.twitch.tv/docs/irc/commands
      - type: Chat Badges
        url: https://dev.twitch.tv/docs/irc/tags#privmsg-tags
      - type: Authentication
        url: https://dev.twitch.tv/docs/chat/authenticating/
  - name: Twitch Embed API
    description: APIs for embedding Twitch live streams, video on demand, clips, and chat into external websites.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/embed/
    baseURL: https://embed.twitch.tv
    tags:
      - Chat
      - Clips
      - Embed
      - Player
      - Video
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/embed/
      - type: Video and Clips
        url: https://dev.twitch.tv/docs/embed/video-and-clips/
      - type: Chat
        url: https://dev.twitch.tv/docs/embed/chat/
      - type: Everything
        url: https://dev.twitch.tv/docs/embed/everything/
  - name: Twitch Extensions API
    description: APIs for building interactive extensions that run as overlays or panels on Twitch channels, communicating via a sandboxed iframe.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/extensions/
    baseURL: https://api.twitch.tv/helix/extensions
    tags:
      - Extensions
      - Interactive
      - Overlays
      - Panels
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/extensions/
      - type: Building Extensions
        url: https://dev.twitch.tv/docs/extensions/building/
      - type: Extensions Reference
        url: https://dev.twitch.tv/docs/extensions/reference/
      - type: Frontend API Usage
        url: https://dev.twitch.tv/docs/extensions/frontend-api-usage/
      - type: OpenAPI
        url: openapi/twitch-extensions-openapi.yml
  - name: Twitch Drops API
    description: APIs for game developers to create and manage Drops campaigns that grant in-game rewards to Twitch viewers watching streamers play their game.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/drops/
    baseURL: https://api.twitch.tv/helix
    tags:
      - Campaigns
      - Drops
      - Gaming
      - Rewards
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/drops/
      - type: Campaign Guide
        url: https://dev.twitch.tv/docs/drops/campaign-guide
      - type: Technical Guide
        url: https://dev.twitch.tv/docs/drops/technical-guide/
      - type: OpenAPI
        url: openapi/twitch-drops-openapi.yml
  - name: Twitch Video Broadcast API
    description: API for retrieving ingest server information used by broadcasters to send live video streams to Twitch via RTMP.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/video-broadcast/
    baseURL: https://ingest.twitch.tv
    tags:
      - Broadcast
      - Ingest
      - Rtmp
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/video-broadcast/
      - type: API Reference
        url: https://dev.twitch.tv/docs/video-broadcast/reference/
      - type: OpenAPI
        url: openapi/twitch-video-broadcast-openapi.yml
  - name: Twitch Insights and Analytics API
    description: APIs for accessing extension and game analytics data including views, clicks, hours watched, and concurrent streamers as downloadable CSV reports.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://dev.twitch.tv/docs/insights/
    baseURL: https://api.twitch.tv/helix/analytics
    tags:
      - Analytics
      - Insights
      - Metrics
      - Reporting
    properties:
      - type: Documentation
        url: https://dev.twitch.tv/docs/insights/
      - type: Dashboard
        url: https://dev.twitch.tv/insights/
      - type: OpenAPI
        url: openapi/twitch-insights-analytics-openapi.yml
  - name: IGDB API
    description: The Internet Game Database API provides comprehensive video game information including metadata, ratings, and media, and is owned and operated by Twitch.
    image: https://www.twitch.tv/favicon.ico
    humanURL: https://api-docs.igdb.com/
    baseURL: https://api.igdb.com/v4
    tags:
      - Database
      - Games
      - Metadata
      - Ratings
    properties:
      - type: Documentation
        url: https://api-docs.igdb.com/
      - type: Authentication
        url: https://dev.twitch.tv/docs/authentication
      - type: OpenAPI
        url: openapi/twitch-igdb-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Developer Portal
    url: https://dev.twitch.tv/
  - type: Console
    url: https://dev.twitch.tv/console
  - type: Blog
    url: https://blog.twitch.tv/en/tags/developers/
  - type: GitHub
    url: https://github.com/twitchdev
  - type: Extensions
    url: https://dev.twitch.tv/docs/extensions
  - type: CLI Tools
    url: https://dev.twitch.tv/docs/cli
  - type: Support
    url: https://dev.twitch.tv/support/
  - type: Forum
    url: https://discuss.dev.twitch.com/
  - type: Feedback
    url: https://twitch.uservoice.com/forums/310213-developers
  - type: Community Resources
    url: https://dev.twitch.tv/code/
  - type: Products
    url: https://dev.twitch.tv/products/
  - type: Change Log
    url: https://dev.twitch.tv/docs/change-log/
  - type: Product Lifecycle
    url: https://dev.twitch.tv/docs/product-lifecycle/
  - type: Authentication
    url: https://dev.twitch.tv/docs/authentication
  - type: Mobile Deep Links
    url: https://dev.twitch.tv/docs/mobile-deeplinks/
  - type: Game Engine Plugins
    url: https://dev.twitch.tv/docs/game-engine-plugins/
  - type: Terms of Service
    url: https://www.twitch.tv/p/legal/terms-of-service/
  - type: Privacy Policy
    url: https://www.twitch.tv/p/legal/privacy-notice/
  - type: JSON-LD
    url: json-ld/twitch-context.jsonld
  - type: JSONSchema
    url: json-schema/twitch-stream-schema.json
  - type: JSONSchema
    url: json-schema/twitch-user-schema.json
  - type: JSONSchema
    url: json-schema/twitch-channel-schema.json
  - type: JSONSchema
    url: json-schema/twitch-clip-schema.json
  - type: JSONSchema
    url: json-schema/twitch-subscription-schema.json
  - type: JSONSchema
    url: json-schema/twitch-video-schema.json
  - type: JSONStructure
    url: json-structure/twitch-stream-structure.json
  - type: JSONStructure
    url: json-structure/twitch-channel-structure.json
  - type: JSONStructure
    url: json-structure/twitch-user-structure.json
  - type: Vocabulary
    url: vocabulary/twitch-vocabulary.yml
  - type: SpectralRules
    url: rules/twitch-rules.yml
  - type: NaftikoCapability
    url: capabilities/content-discovery.yaml
  - type: NaftikoCapability
    url: capabilities/channel-management.yaml
---
