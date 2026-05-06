---
aid: unity
name: Unity
description: Unity is a cross-platform real-time development platform that provides a comprehensive suite of APIs and services for game development, interactive 3D content creation, and live game operations including multiplayer, analytics, economy, authentication, and DevOps tooling.
type: Index
position: Consumer
access: 3rd-Party
image: https://unity.com/logo.png
tags:
  - Game Development
  - Real-Time 3D
  - Multiplayer
  - Game Services
  - Cloud Gaming
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: unity:player-authentication
    name: Unity Player Authentication API
    description: The Player Authentication REST API verifies player identity and manages authentication workflows, providing endpoints for sign-in, sign-up, token management, and linking external identity providers including Google, Apple, Steam, Facebook, and custom identity providers.
    humanURL: https://docs.unity.com/ugs/en-us/manual/authentication/manual/rest-api
    tags:
      - Authentication
      - Identity
      - Players
      - OAuth
      - Sign-In
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/authentication/manual/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/player-auth-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-player-authentication-openapi.yml
  - aid: unity:cloud-code
    name: Unity Cloud Code API
    description: The Cloud Code API enables running serverless game logic in the cloud, allowing you to create, manage, and execute scripts and modules without maintaining dedicated servers. Supports JavaScript and C# modules.
    humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual
    tags:
      - Cloud
      - Code Execution
      - Serverless
      - Functions
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual
      - type: API Reference
        url: https://services.docs.unity.com/cloud-code-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-cloud-code-openapi.yml
  - aid: unity:cloud-save
    name: Unity Cloud Save API
    description: The Cloud Save REST API provides endpoints for persisting player data and game state in the cloud, with both a Player API for client-side actions and an Admin API for server-side management. Supports custom items with access class controls.
    humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-save/manual/reference/rest-api
    tags:
      - Cloud Storage
      - Game State
      - Player Data
      - Persistence
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/cloud-save/manual/reference/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/cloud-save-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-cloud-save-openapi.yml
  - aid: unity:economy
    name: Unity Economy API
    description: The Economy REST API allows you to manage in-game economies including virtual currencies, inventory items, purchases, and player balances through both admin and player endpoints. Supports currencies, inventory items, virtual purchases, and real-money purchases.
    humanURL: https://docs.unity.com/ugs/en-us/manual/economy/manual/write-configuration/rest-api
    tags:
      - Economy
      - In-App Purchases
      - Virtual Currency
      - Inventory
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/economy/manual/write-configuration/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/economy-admin/v2/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-economy-openapi.yml
  - aid: unity:leaderboards
    name: Unity Leaderboards API
    description: The Leaderboards REST API provides a Player API for submitting and fetching scores and an Admin API for creating, updating, and managing leaderboard configurations. Supports bucket leaderboards, score modifiers, and tiebreaker rules.
    humanURL: https://docs.unity.com/ugs/en-us/manual/leaderboards/manual/write-configuration/rest-api
    tags:
      - Leaderboards
      - Rankings
      - Scores
      - Competitive Gaming
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/leaderboards/manual/write-configuration/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/leaderboards-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-leaderboards-openapi.yml
  - aid: unity:remote-config
    name: Unity Remote Config API
    description: The Remote Config REST API enables launching new features, testing functionality, and modifying game configurations without requiring app updates, with both a Runtime API and an Admin API for managing settings and override rules.
    humanURL: https://docs.unity.com/ugs/en-us/manual/remote-config/manual/write-configuration/rest-api
    tags:
      - Configuration
      - Feature Flags
      - Remote Config
      - A/B Testing
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/remote-config/manual/write-configuration/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/remote-config-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-remote-config-openapi.yml
  - aid: unity:analytics
    name: Unity Analytics API
    description: The Analytics REST API provides endpoints for tracking player behavior, recording custom events, and querying analytics data for Unity projects. Supports custom event ingestion, funnel analysis, and behavioral segmentation.
    humanURL: https://docs.unity.com/ugs/en-us/manual/analytics/manual/rest-api
    tags:
      - Analytics
      - Events
      - Telemetry
      - Player Behavior
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/analytics/manual/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/analytics/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-analytics-openapi.yml
  - aid: unity:lobby
    name: Unity Lobby API
    description: The Lobby REST API provides endpoints for creating, managing, and querying multiplayer game lobbies, allowing players to group together before joining a game session. Supports public and private lobbies with custom data and filters.
    humanURL: https://docs.unity.com/ugs/en-us/manual/lobby/manual/lobby-apis
    tags:
      - Lobby
      - Matchmaking
      - Multiplayer
      - Game Sessions
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/lobby/manual/lobby-apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-lobby-openapi.yml
  - aid: unity:matchmaker
    name: Unity Matchmaker API
    description: The Matchmaker REST API provides endpoints for creating and managing matchmaking tickets, defining matchmaking rules, and configuring match pools and queues for skill-based and attribute-based player matching.
    humanURL: https://docs.unity.com/ugs/en-us/manual/matchmaker/manual/matchmaker-api
    tags:
      - Matchmaking
      - Multiplayer
      - Skill-Based Matching
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/matchmaker/manual/matchmaker-api
      - type: API Reference
        url: https://services.docs.unity.com/matchmaker-admin/v3/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-matchmaker-openapi.yml
  - aid: unity:relay
    name: Unity Relay API
    description: The Relay REST API provides the Relay Allocations API and QoS Discovery API, enabling peer-to-peer multiplayer connectivity without dedicated game servers through secure relay servers.
    humanURL: https://docs.unity.com/ugs/en-us/manual/relay/manual/rest-api
    tags:
      - Multiplayer
      - Networking
      - Relay
      - Peer-to-Peer
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/relay/manual/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/relay-allocations/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-relay-openapi.yml
  - aid: unity:multiplay-game-server-hosting
    name: Unity Multiplay Game Server Hosting API
    description: The Multiplay Game Server Hosting REST API provides Admin API endpoints for resource configuration and a Game Server Lifecycle API for managing the lifecycle of dedicated game servers in cloud, bare metal, or hybrid environments.
    humanURL: https://docs.unity.com/ugs/en-us/manual/game-server-hosting/manual/api/rest-api
    tags:
      - Game Servers
      - Hosting
      - Multiplayer
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/game-server-hosting/manual/api/rest-api
      - type: API Reference
        url: https://services.docs.unity.com/multiplay-config/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-multiplay-openapi.yml
  - aid: unity:cloud-content-delivery
    name: Unity Cloud Content Delivery API
    description: The Cloud Content Delivery (CCD) REST API enables building and releasing game updates with powerful asset management and content delivery through the cloud. Supports buckets, entries, releases, and badges.
    humanURL: https://docs.unity.com/ugs/manual/ccd/manual/ccd-rest-api
    tags:
      - Assets
      - CDN
      - Content Delivery
      - Game Updates
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/manual/ccd/manual/ccd-rest-api
      - type: API Reference
        url: https://services.docs.unity.com/content-delivery-management/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-cloud-content-delivery-openapi.yml
  - aid: unity:triggers
    name: Unity Triggers API
    description: The Triggers API monitors a stream of internal events emitted by Unity Gaming Services and the Scheduler service, enabling Cloud Code scripts and modules to run automatically based on event conditions.
    humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
    tags:
      - Automation
      - Events
      - Triggers
      - Cloud Code
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
      - type: API Reference
        url: https://services.docs.unity.com/triggers-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-triggers-openapi.yml
  - aid: unity:scheduler
    name: Unity Scheduler API
    description: The Scheduler API enables scheduling events to occur at a set or recurring moment in time, which can be used to trigger Cloud Code execution on a defined schedule using cron expressions.
    humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
    tags:
      - Automation
      - Cron
      - Scheduler
      - Cloud Code
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
      - type: API Reference
        url: https://services.docs.unity.com/scheduler-admin/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-scheduler-openapi.yml
  - aid: unity:friends
    name: Unity Friends API
    description: The Friends API helps players connect with others to add a social experience to games, providing endpoints for managing friend lists, friend requests, incoming requests, and blocking players.
    humanURL: https://docs.unity.com/ugs/en-us/manual/friends/manual/overview
    tags:
      - Friends
      - Multiplayer
      - Social
      - Player Relationships
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/friends/manual/overview
      - type: API Reference
        url: https://services.docs.unity.com/friends/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-friends-openapi.yml
  - aid: unity:vivox
    name: Unity Vivox Voice and Text Chat API
    description: Vivox provides voice and text-based communication services for games, with APIs for managing channels, participants, and communication sessions across platforms. Supports 2D and 3D positional audio.
    humanURL: https://docs.unity.com/ugs/en-us/manual/vivox-unity/manual/Unity/Unity
    tags:
      - Communication
      - Text Chat
      - Voice Chat
      - Real-Time Audio
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/vivox-unity/manual/Unity/Unity
      - type: API Reference
        url: https://docs.unity.com/ugs/en-us/manual/vivox-core/manual/reference-manual/core/api-reference
  - aid: unity:moderation
    name: Unity Moderation API
    description: The Moderation API provides endpoints for actioning incidents, reviewing evidence, and monitoring community health scores to manage player behavior and content moderation across Unity Gaming Services.
    humanURL: https://docs.unity.com/ugs/en-us/manual/moderation/manual/overview
    tags:
      - Moderation
      - Safety
      - Trust
      - Community Health
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/moderation/manual/overview
      - type: API Reference
        url: https://services.docs.unity.com/moderation/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-moderation-openapi.yml
  - aid: unity:user-generated-content
    name: Unity User Generated Content API
    description: The User Generated Content (UGC) API is a format and content-agnostic service for incorporating user-generated content features into games, handling content storage, discovery, ingestion, moderation, and ratings.
    humanURL: https://docs.unity.com/ugs/manual/user-generated-content/manual/overview
    tags:
      - Community
      - Content
      - UGC
      - Player Content
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/manual/user-generated-content/manual/overview
  - aid: unity:push-notifications
    name: Unity Push Notifications API
    description: The Push Notifications API allows scheduling messages to players on iOS and Android mobile devices when they are not actively playing, with support for immediate, scheduled, and recurring notifications.
    humanURL: https://docs.unity.com/ugs/en-us/manual/push-notifications/manual/overview
    tags:
      - Messaging
      - Mobile
      - Push Notifications
      - iOS
      - Android
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/push-notifications/manual/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-push-notifications-openapi.yml
  - aid: unity:build-automation
    name: Unity Build Automation API
    description: The Build Automation REST API enables automating and integrating continuous integration builds into custom workflows, providing insight into build history and webhook callbacks for build events across multiple platforms.
    humanURL: https://docs.unity.com/ugs/manual/devops/manual/build-automation/build-automation-api
    tags:
      - Build
      - CI/CD
      - DevOps
      - Automation
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/manual/devops/manual/build-automation/build-automation-api
      - type: API Reference
        url: https://build-api.cloud.unity3d.com/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-build-automation-openapi.yml
  - aid: unity:version-control
    name: Unity Version Control API
    description: Unity Version Control (previously Plastic SCM) provides REST API access for managing version-controlled repositories, branches, changesets, and merge requests in both cloud and on-premise deployments.
    humanURL: https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-version-control
    tags:
      - DevOps
      - Source Control
      - Version Control
      - Branching
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-version-control
      - type: API Reference
        url: https://services.docs.unity.com/guides/unity-version-control-cm/overview/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-version-control-openapi.yml
  - aid: unity:access
    name: Unity Access API
    description: The Access API provides endpoints for managing access control, resource policies, and permissions that control who can access, modify, or delete game data and resources across Unity Gaming Services.
    humanURL: https://docs.unity.com/ugs/manual/overview/manual/access-control
    tags:
      - Access Control
      - Permissions
      - Security
      - IAM
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/manual/overview/manual/access-control
      - type: API Reference
        url: https://services.docs.unity.com/access/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-access-openapi.yml
  - aid: unity:scim
    name: Unity SCIM API
    description: The SCIM v2 API provides a standardized protocol for automating user and group provisioning between your Identity Provider and Unity Cloud, streamlining cross-domain identity management and user lifecycle operations.
    humanURL: https://support.unity.com/hc/en-us/articles/38766626849684-How-do-I-configure-SCIM-provisioning
    tags:
      - Identity
      - Provisioning
      - SCIM
      - SSO
    properties:
      - type: Documentation
        url: https://support.unity.com/hc/en-us/articles/38766626849684-How-do-I-configure-SCIM-provisioning
      - type: API Reference
        url: https://services.docs.unity.com/scim/v2/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-scim-openapi.yml
  - aid: unity:distributed-authority
    name: Unity Distributed Authority API
    description: The Distributed Authority API enables decentralized multiplayer networking where game clients share responsibility for owning and tracking the state of networked objects, reducing server load and latency.
    humanURL: https://unity.com/products/distributed-authority
    tags:
      - Distributed
      - Multiplayer
      - Networking
      - State Management
    properties:
      - type: Documentation
        url: https://unity.com/products/distributed-authority
      - type: API Reference
        url: https://services.docs.unity.com/distributed-authority/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-distributed-authority-openapi.yml
  - aid: unity:safe-text
    name: Unity Safe Text API
    description: The Safe Text API provides AI-powered text chat moderation, filtering inappropriate content and generating evidence reports for review through the Unity Moderation Platform.
    humanURL: https://docs.unity.com/ugs/en-us/manual/safe-text/manual/overview
    tags:
      - Moderation
      - Safety
      - Text Filtering
      - AI Moderation
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/safe-text/manual/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-safe-text-openapi.yml
  - aid: unity:asset-manager
    name: Unity Asset Manager API
    description: The Asset Manager REST API provides endpoints for uploading, managing, transforming, sharing, and accessing complex real-time 3D assets for use across Unity projects and workflows.
    humanURL: https://docs.unity.com/ugs/en-us/manual/asset-manager/manual
    tags:
      - Assets
      - Asset Management
      - 3D Content
      - Collaboration
    properties:
      - type: Documentation
        url: https://docs.unity.com/ugs/en-us/manual/asset-manager/manual
      - type: API Reference
        url: https://services.docs.unity.com/assets-manager/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-asset-manager-openapi.yml
  - aid: unity:monetize
    name: Unity Monetize API
    description: The Unity Monetize API (formerly Unity Ads) provides REST endpoints for managing ad placements, revenue reporting, and monetization configuration for mobile and desktop games.
    humanURL: https://docs.unity.com/ads/en-us/manual/MonetizationResourceCenter
    tags:
      - Monetization
      - Advertising
      - Revenue
      - Mobile Ads
    properties:
      - type: Documentation
        url: https://docs.unity.com/ads/en-us/manual/MonetizationResourceCenter
      - type: API Reference
        url: https://services.docs.unity.com/monetize/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/openapi/unity-monetize-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Unity Technologies
    email: support@unity.com
    url: https://unity.com
common:
  - url: https://cloud.unity.com
    type: Portal
  - url: https://dashboard.unity3d.com
    type: Dashboard
  - url: https://id.unity.com
    type: Sign Up
  - url: https://status.unity.com
    type: Status
  - url: https://support.unity.com
    type: Support
  - url: https://unity.com/legal/terms-of-service
    type: Terms of Service
  - url: https://unity.com/legal/privacy-policy
    type: Privacy Policy
  - url: https://blog.unity.com
    type: Blog
  - url: https://github.com/Unity-Technologies
    type: GitHub Organization
  - url: https://services.docs.unity.com/
    type: API Reference
  - url: https://docs.unity.com/ugs
    type: Documentation
  - url: https://docs.unity.com/ugs/en-us/manual/overview/manual/getting-started
    type: Getting Started
  - url: https://services.docs.unity.com/docs/service-account-auth/
    type: Authentication
  - url: https://services.docs.unity.com/docs/client-auth/
    type: Authentication
  - url: https://unity.com/products/gaming-services/pricing
    type: Pricing
  - url: https://discussions.unity.com/
    type: Forum
  - url: https://unity.com/community
    type: Community
  - url: https://unity.com/developer-tools
    type: Developer Tools
  - url: https://unity.com/faq
    type: FAQ
  - url: https://services.docs.unity.com/docs/errors/
    type: Errors
  - url: https://services.docs.unity.com/docs/api-lifecycle/
    type: API Lifecycle
  - url: https://unity.com/releases/unity-6/support
    type: Change Log
  - url: https://assetstore.unity.com
    type: Marketplace
  - url: https://learn.unity.com
    type: Learning
  - url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/rules/unity-spectral-rules.yml
    type: Spectral Rules
  - url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/vocabulary/unity-vocabulary.yml
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/json-ld/unity-context.jsonld
    type: JSON-LD Context
---
