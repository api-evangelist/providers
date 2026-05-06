---
aid: discord
name: Discord
description: Discord is a voice, video and text communication service used by hundreds of millions of people to hang out and talk with their communities and friends.
url: https://raw.githubusercontent.com/api-evangelist/discord/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://discord.com/assets/fc0b01fe10a0b8c602fb0106d8189d9b.png
tags:
  - Chat
  - Communication
  - Gaming
  - Messaging
  - Social
  - Video
  - Voice
created: '2024-04-14'
modified: '2026-05-04'
specificationVersion: '0.18'
apis:
  - aid: discord:discord-rest-api
    name: Discord REST API
    description: The Discord REST API provides programmatic access to Discord resources including users, guilds, channels, messages, emojis, webhooks, and more. It is the primary interface for building bots, integrations, and applications that interact with Discord data through standard HTTP request-response operations.
    humanURL: https://discord.com/developers/docs/reference
    baseURL: https://discord.com/api/v10
    tags:
      - Channels
      - Guilds
      - Messaging
      - REST
      - Users
      - Webhooks
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/reference
      - type: OpenAPI
        url: https://github.com/discord/discord-api-spec
      - type: OpenAPI
        url: openapi/discord-rest-api-openapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-gateway-api
    name: Discord Gateway API
    description: The Discord Gateway API provides persistent, stateful WebSocket connections between your client and Discord servers. These connections are used for sending and receiving real-time events your client can use to track and update local state, including message creation, guild updates, presence changes, and voice state updates.
    humanURL: https://discord.com/developers/docs/events/gateway
    tags:
      - Events
      - Gateway
      - Real-Time
      - WebSocket
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/events/gateway
      - type: Documentation
        url: https://discord.com/developers/docs/events/gateway-events
      - type: AsyncAPI
        url: asyncapi/discord-gateway-api-asyncapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-interactions-api
    name: Discord Interactions API
    description: The Discord Interactions API enables applications to create and respond to application commands (slash commands), message components, and modals. It supports both Gateway-based and webhook-based interaction handling, allowing bots to build rich, interactive user experiences within Discord.
    humanURL: https://discord.com/developers/docs/interactions/overview
    tags:
      - Components
      - Interactions
      - Modals
      - Slash Commands
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/interactions/overview
      - type: Documentation
        url: https://discord.com/developers/docs/interactions/application-commands
      - type: Documentation
        url: https://discord.com/developers/docs/interactions/receiving-and-responding
      - type: OpenAPI
        url: openapi/discord-interactions-api-openapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-oauth2-api
    name: Discord OAuth2 API
    description: The Discord OAuth2 API enables application developers to build applications that utilize authentication and data from the Discord API. Discord supports the authorization code grant, the implicit grant, client credentials, and specialized flows for bots and webhooks, allowing third-party applications to access Discord user data with proper consent.
    humanURL: https://discord.com/developers/docs/topics/oauth2
    tags:
      - Authentication
      - Authorization
      - OAuth2
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/topics/oauth2
      - type: OpenAPI
        url: openapi/discord-oauth2-api-openapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-webhook-events-api
    name: Discord Webhook Events API
    description: The Discord Webhook Events API provides HTTP-based outgoing webhook events that allow applications to receive notifications for specific events without maintaining a persistent connection. Supported events include APPLICATION_AUTHORIZED, ENTITLEMENT_CREATE, and QUEST_USER_ENROLLMENT.
    humanURL: https://discord.com/developers/docs/events/webhook-events
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/events/webhook-events
      - type: OpenAPI
        url: openapi/discord-webhook-events-api-openapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-embedded-app-sdk
    name: Discord Embedded App SDK
    description: The Discord Embedded App SDK lets you build rich, multiplayer experiences as Activities inside Discord. It handles RPC calls between your application and Discord, enabling interactive activities like games that can run in voice channels, text channels, or DMs.
    humanURL: https://discord.com/developers/docs/developer-tools/embedded-app-sdk
    tags:
      - Activities
      - Embedded
      - Games
      - SDK
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/developer-tools/embedded-app-sdk
      - type: GitHubRepo
        url: https://github.com/discord/embedded-app-sdk
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-voice-api
    name: Discord Voice API
    description: The Discord Voice API provides the protocol for establishing and managing voice connections between clients and Discord voice servers. It handles UDP-based voice data transmission, encryption with XSalsa20-Poly1305, and supports features like speaking indicators and voice state updates.
    humanURL: https://discord.com/developers/docs/topics/voice-connections
    tags:
      - Real-Time
      - UDP
      - Voice
      - WebSocket
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/topics/voice-connections
      - type: AsyncAPI
        url: asyncapi/discord-voice-api-asyncapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-linked-roles-api
    name: Discord Linked Roles API
    description: The Discord Linked Roles API enables applications to associate third-party metadata with Discord users through role connection metadata. Server admins can use this metadata to configure requirements for linked roles, such as verified accounts or achievement thresholds from external platforms.
    humanURL: https://discord.com/developers/docs/tutorials/configuring-app-metadata-for-linked-roles
    tags:
      - Metadata
      - OAuth2
      - Roles
      - Verification
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/tutorials/configuring-app-metadata-for-linked-roles
      - type: OpenAPI
        url: openapi/discord-linked-roles-api-openapi.yml
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
  - aid: discord:discord-social-sdk
    name: Discord Social SDK
    description: The Discord Social SDK allows game developers to add rich social features into their games across desktop, mobile, and console platforms. It supports features like account linking, rich presence, lobbies, voice chat, direct messaging, friends lists, and game invites to create connected social experiences powered by Discord.
    humanURL: https://discord.com/developers/docs/discord-social-sdk/overview
    tags:
      - Gaming
      - Rich Presence
      - SDK
      - Social
      - Voice
    properties:
      - type: Documentation
        url: https://discord.com/developers/docs/discord-social-sdk/overview
      - type: GettingStarted
        url: https://discord.com/developers/docs/discord-social-sdk/getting-started
    contact:
      - FN: Discord Support
        url: https://support-dev.discord.com/hc/en-us
        email: support@discord.com
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - name: Discord Inc.
    twitter: discord
    email: support@discord.com
common:
  - url: https://discord.com/developers/applications
    type: Portal
  - url: https://discord.com/terms
    type: Terms of Service
  - url: https://discord.com/privacy
    type: Privacy Policy
  - url: https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service
    type: Developer Terms
  - url: https://discord.com/guidelines
    type: Community Guidelines
  - url: https://discord.com/blog
    type: Blog
  - url: https://twitter.com/discord
    type: Twitter
  - url: https://discord.com/developers/docs/reference
    type: Documentation
  - url: https://discord.com/developers/docs/quick-start/getting-started
    type: GettingStarted
  - url: https://discord.com/developers/docs/change-log
    type: ChangeLog
  - url: https://discordstatus.com/
    type: Status
  - url: https://support-dev.discord.com/hc/en-us
    type: Support
  - url: https://github.com/discord
    type: GitHubOrg
  - url: https://github.com/discord/discord-api-docs
    type: GitHubRepo
  - url: https://github.com/discord/discord-api-spec
    type: OpenAPI
  - url: https://discord.com/developers/docs/topics/rate-limits
    type: RateLimits
  - url: https://discord.com/developers/docs/topics/permissions
    type: Permissions
  - url: https://discord.com/developers/docs/topics/oauth2
    type: Authentication
  - url: https://discord.com/developers/docs/topics/opcodes-and-status-codes
    type: StatusCodes
  - url: https://discord.com/developers/docs/developer-tools/community-resources
    type: CommunityResources
  - url: https://discord.com/developers/docs/topics/threads
    type: Documentation
  - url: https://discord.com/developers/docs/topics/teams
    type: Documentation
  - url: https://discord.com/developers/docs/topics/voice-connections
    type: Documentation
  - url: https://discord.com/developers/docs/monetization/overview
    type: Monetization
  - url: https://discord.com/developers/docs/discovery/overview
    type: Discovery
  - url: https://discord.com/developers/docs/rich-presence/overview
    type: RichPresence
  - url: https://discord.com/branding
    type: Branding
  - url: https://discord.com/invite/discord-developers
    type: Community
  - url: https://discord.com/developers/docs/policies/developer-policy
    type: DeveloperPolicy
  - url: https://discord.com/developers/docs/policies/developer-terms-of-service
    type: DeveloperTermsOfService
  - url: https://www.postman.com/discord-api
    type: PostmanWorkspace
  - url: https://discord.com/developers/docs/game-sdk/sdk-starter-guide
    type: Game SDK
  - url: https://discord.com/developers/docs/tutorials/hosting-on-cloudflare-workers
    type: Tutorials
  - url: https://stackoverflow.com/questions/tagged/discord
    type: Stack Overflow
  - url: https://www.youtube.com/@Discord
    type: YouTube
  - url: https://discord.com/safety
    type: Safety
  - url: https://discord.com/developers/docs/policies-and-agreements/developer-policy
    type: Developer Policy
  - url: json-schema/discord-guild-schema.json
    type: JSONSchema
  - url: json-schema/discord-channel-schema.json
    type: JSONSchema
  - url: json-schema/discord-message-schema.json
    type: JSONSchema
  - url: json-schema/discord-user-schema.json
    type: JSONSchema
  - url: json-schema/discord-role-schema.json
    type: JSONSchema
  - url: json-schema/discord-emoji-schema.json
    type: JSONSchema
  - url: json-schema/discord-webhook-schema.json
    type: JSONSchema
  - url: json-ld/discord-context.jsonld
    type: JSON-LD
  - type: Features
    data:
      - Free Discord with 25 MB upload limit and unlimited servers
      - Nitro Basic at $2.99/mo or $29.99/yr with 50 MB uploads
      - Nitro at $9.99/mo or $99.99/yr with 500 MB uploads and 2 server boosts
      - Discord Bot API free for developers
      - 'Global bot rate limit: 50 req/sec'
      - Per-route bucket-based rate limits with X-RateLimit-Bucket headers
      - 'Webhook execute: 5 req per 2 seconds'
      - 'Identify (gateway): 1 per 5 seconds, 1,000 per day'
      - 'Invalid request limit: 10,000 per 10 minutes per IP'
      - REST API at discord.com/api/v10
      - Gateway WebSocket for realtime events
      - Voice gateway for voice/video
      - Slash commands and interactions API
      - Application commands (chat, user, message)
      - OAuth 2.0 with bot/identify/guilds scopes
      - Custom embeds, components, modals
    sources:
      - https://discord.com/pricing
      - https://discord.com/nitro
    updated: '2026-05-04'
---
