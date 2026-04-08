---
aid: unity
url: https://raw.githubusercontent.com/api-evangelist/unity/refs/heads/main/apis.yml
apis:
- aid: unity:unity
  name: Unity
  description: The EnvironmentsApi allows you to refresh the environments list, get all environments, set the active environment, and validate that the active environment ...
  humanURL: https://docs.unity.com/ugs/manual/overview/manual/environments-api
  tags: []
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/manual/overview/manual/environments-api
- aid: unity:player-authentication
  name: Unity Player Authentication API
  description: The Player Authentication REST API verifies player identity and manages authentication workflows, providing endpoints for sign-in, sign-up, token management, and linking external identity providers.
  humanURL: https://docs.unity.com/ugs/en-us/manual/authentication/manual/rest-api
  tags:
  - Authentication
  - Identity
  - Players
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/authentication/manual/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/player-auth-admin/v1/
- aid: unity:cloud-code
  name: Unity Cloud Code API
  description: The Cloud Code API enables running serverless game logic in the cloud, allowing you to create, manage, and execute scripts and modules without maintaining dedicated servers.
  humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual
  tags:
  - Cloud
  - Code Execution
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual
  - type: API Reference
    url: https://services.docs.unity.com/cloud-code/index.html
- aid: unity:cloud-save
  name: Unity Cloud Save API
  description: The Cloud Save REST API provides endpoints for persisting player data and game state in the cloud, with both a Player API for client-side actions and an Admin API for server-side management.
  humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-save/manual/reference/rest-api
  tags:
  - Cloud Storage
  - Game State
  - Player Data
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/cloud-save/manual/reference/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/cloud-save-admin/v1/
- aid: unity:economy
  name: Unity Economy API
  description: The Economy REST API allows you to manage in-game economies including virtual currencies, inventory items, purchases, and player balances through both admin and client endpoints.
  humanURL: https://docs.unity.com/ugs/en-us/manual/economy/manual/write-configuration/rest-api
  tags:
  - Economy
  - In-App Purchases
  - Virtual Currency
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/economy/manual/write-configuration/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/economy-admin/v2/index.html
- aid: unity:leaderboards
  name: Unity Leaderboards API
  description: The Leaderboards REST API provides a Player API for submitting and fetching scores and an Admin API for creating, updating, and managing leaderboard configurations.
  humanURL: https://docs.unity.com/ugs/en-us/manual/leaderboards/manual/write-configuration/rest-api
  tags:
  - Leaderboards
  - Rankings
  - Scores
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/leaderboards/manual/write-configuration/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/leaderboards-admin/v1/
- aid: unity:remote-config
  name: Unity Remote Config API
  description: The Remote Config REST API enables launching new features, testing functionality, and modifying game configurations without requiring app updates, with both a Runtime API and an Admin API.
  humanURL: https://docs.unity.com/ugs/en-us/manual/remote-config/manual/write-configuration/rest-api
  tags:
  - Configuration
  - Feature Flags
  - Remote Config
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/remote-config/manual/write-configuration/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/remote-config-admin/v1/
- aid: unity:analytics
  name: Unity Analytics API
  description: The Analytics REST API provides endpoints for tracking player behavior, recording custom events, and querying analytics data for your Unity projects.
  humanURL: https://docs.unity.com/ugs/en-us/manual/analytics/manual/rest-api
  tags:
  - Analytics
  - Events
  - Telemetry
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/analytics/manual/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/analytics/v1/
- aid: unity:lobby
  name: Unity Lobby API
  description: The Lobby REST API provides endpoints for creating, managing, and querying multiplayer game lobbies, allowing players to group together before joining a game session.
  humanURL: https://docs.unity.com/ugs/en-us/manual/lobby/manual/lobby-apis
  tags:
  - Lobby
  - Matchmaking
  - Multiplayer
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/lobby/manual/lobby-apis
- aid: unity:matchmaker
  name: Unity Matchmaker API
  description: The Matchmaker REST API provides endpoints for creating and managing matchmaking tickets, defining matchmaking rules, and configuring match pools and queues.
  humanURL: https://docs.unity.com/ugs/en-us/manual/matchmaker/manual/matchmaker-api
  tags:
  - Matchmaking
  - Multiplayer
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/matchmaker/manual/matchmaker-api
  - type: API Reference
    url: https://services.docs.unity.com/matchmaker-admin/v3/
- aid: unity:relay
  name: Unity Relay API
  description: The Relay REST API provides the Relay Allocations API and QoS Discovery API, enabling peer-to-peer multiplayer connectivity without dedicated game servers.
  humanURL: https://docs.unity.com/ugs/en-us/manual/relay/manual/rest-api
  tags:
  - Multiplayer
  - Networking
  - Relay
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/relay/manual/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/relay-allocations/v1/
- aid: unity:multiplay-game-server-hosting
  name: Unity Multiplay Game Server Hosting API
  description: The Multiplay Game Server Hosting REST API provides Admin API endpoints for resource configuration and a Game Server Lifecycle API for managing the lifecycle of dedicated game servers.
  humanURL: https://docs.unity.com/ugs/en-us/manual/game-server-hosting/manual/api/rest-api
  tags:
  - Game Servers
  - Hosting
  - Multiplayer
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/game-server-hosting/manual/api/rest-api
  - type: API Reference
    url: https://services.docs.unity.com/multiplay-config/v1/
- aid: unity:cloud-content-delivery
  name: Unity Cloud Content Delivery API
  description: The Cloud Content Delivery (CCD) REST API enables building and releasing game updates with powerful asset management and content delivery through the cloud.
  humanURL: https://docs.unity.com/ugs/manual/ccd/manual/ccd-rest-api
  tags:
  - Assets
  - CDN
  - Content Delivery
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/manual/ccd/manual/ccd-rest-api
  - type: API Reference
    url: https://services.docs.unity.com/content-delivery-management/v1/
- aid: unity:triggers
  name: Unity Triggers API
  description: The Triggers API monitors a stream of internal events emitted by Unity Gaming Services and the Scheduler service, enabling Cloud Code scripts and modules to run automatically based on event conditions.
  humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
  tags:
  - Automation
  - Events
  - Triggers
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
  - type: API Reference
    url: https://services.docs.unity.com/triggers-admin/v1/
- aid: unity:scheduler
  name: Unity Scheduler API
  description: The Scheduler API enables scheduling events to occur at a set or recurring moment in time, which can be used to trigger Cloud Code execution on a defined schedule.
  humanURL: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
  tags:
  - Automation
  - Cron
  - Scheduler
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/triggers
  - type: API Reference
    url: https://services.docs.unity.com/scheduler-admin/v1/
- aid: unity:friends
  name: Unity Friends API
  description: The Friends API helps players connect with others to add a social experience to games, providing endpoints for managing friend lists, friend requests, and social relationships.
  humanURL: https://docs.unity.com/ugs/en-us/manual/friends/manual/overview
  tags:
  - Friends
  - Multiplayer
  - Social
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/friends/manual/overview
  - type: API Reference
    url: https://services.docs.unity.com/friends/v1/
- aid: unity:vivox
  name: Unity Vivox Voice and Text Chat API
  description: Vivox provides voice and text-based communication services for games, with APIs for managing channels, participants, and communication sessions across platforms.
  humanURL: https://docs.unity.com/ugs/en-us/manual/vivox-unity/manual/Unity/Unity
  tags:
  - Communication
  - Text Chat
  - Voice Chat
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/vivox-unity/manual/Unity/Unity
  - type: API Reference
    url: https://docs.unity.com/ugs/en-us/manual/vivox-core/manual/reference-manual/core/api-reference
- aid: unity:moderation
  name: Unity Moderation API
  description: The Moderation API provides endpoints for actioning incidents, reviewing evidence, and monitoring community health scores to manage player behavior and content moderation.
  humanURL: https://docs.unity.com/ugs/en-us/manual/moderation/manual/overview
  tags:
  - Moderation
  - Safety
  - Trust
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/moderation/manual/overview
  - type: API Reference
    url: https://services.docs.unity.com/moderation/v1/
- aid: unity:user-generated-content
  name: Unity User Generated Content API
  description: The User Generated Content (UGC) API is a format and content-agnostic service for incorporating user-generated content features into games, handling content storage, discovery, ingestion, moderation, and ratings.
  humanURL: https://docs.unity.com/ugs/manual/user-generated-content/manual/overview
  tags:
  - Community
  - Content
  - UGC
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
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/push-notifications/manual/overview
- aid: unity:build-automation
  name: Unity Build Automation API
  description: The Build Automation REST API enables automating and integrating continuous integration builds into custom workflows, providing insight into build history and webhook callbacks for build events.
  humanURL: https://docs.unity.com/ugs/manual/devops/manual/build-automation/build-automation-api
  tags:
  - Build
  - CI/CD
  - DevOps
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/manual/devops/manual/build-automation/build-automation-api
  - type: API Reference
    url: https://build-api.cloud.unity3d.com/docs/
- aid: unity:version-control
  name: Unity Version Control API
  description: Unity Version Control (previously Plastic SCM) provides REST API access for managing version-controlled repositories, branches, and changesets in both cloud and on-premise deployments.
  humanURL: https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-version-control
  tags:
  - DevOps
  - Source Control
  - Version Control
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-version-control
  - type: API Reference
    url: https://services.docs.unity.com/guides/unity-version-control-cm/overview/
- aid: unity:access
  name: Unity Access API
  description: The Access API provides endpoints for managing access control, resource policies, and permissions that control who can access, modify, or delete game data and resources across Unity Gaming Services.
  humanURL: https://docs.unity.com/ugs/manual/overview/manual/access-control
  tags:
  - Access Control
  - Permissions
  - Security
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/manual/overview/manual/access-control
  - type: API Reference
    url: https://services.docs.unity.com/access/v1/
- aid: unity:scim
  name: Unity SCIM API
  description: The SCIM v2 API provides a standardized protocol for automating user and group provisioning between your Identity Provider and Unity Cloud, streamlining cross-domain identity management.
  humanURL: https://support.unity.com/hc/en-us/articles/38766626849684-How-do-I-configure-SCIM-provisioning
  tags:
  - Identity
  - Provisioning
  - SCIM
  properties:
  - type: Documentation
    url: https://support.unity.com/hc/en-us/articles/38766626849684-How-do-I-configure-SCIM-provisioning
  - type: API Reference
    url: https://services.docs.unity.com/scim/v2/
- aid: unity:distributed-authority
  name: Unity Distributed Authority API
  description: The Distributed Authority API enables decentralized multiplayer networking where game clients share responsibility for owning and tracking the state of networked objects.
  humanURL: https://unity.com/products/distributed-authority
  tags:
  - Distributed
  - Multiplayer
  - Networking
  properties:
  - type: Documentation
    url: https://unity.com/products/distributed-authority
  - type: API Reference
    url: https://services.docs.unity.com/distributed-authority/v1/
- aid: unity:safe-text
  name: Unity Safe Text API
  description: The Safe Text API provides AI-powered text chat moderation, filtering inappropriate content and generating evidence reports for review through the Moderation Platform.
  humanURL: https://docs.unity.com/ugs/en-us/manual/safe-text/manual/overview
  tags:
  - Moderation
  - Safety
  - Text Filtering
  properties:
  - type: Documentation
    url: https://docs.unity.com/ugs/en-us/manual/safe-text/manual/overview
name: Unity
tags:
- API
type: Index
image: https://unity.com/logo.png
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Unity is a cross-platform game engine and development platform with comprehensive APIs for game development, real-time 3D content creation, and interactive experiences.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

