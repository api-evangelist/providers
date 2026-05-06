---
aid: epic
name: Epic Games
description: Epic Games operates the Epic Games Store digital storefront and the Epic Online Services (EOS) platform, providing developers with cross-platform game services. Epic Online Services is a free SDK based on Fortnite's backend infrastructure, supporting matchmaking, friends, leaderboards, achievements, voice chat, anti-cheat, and player data storage across Windows, macOS, PlayStation, Xbox, Nintendo Switch, iOS, and Android. The Epic Account Services and EOS Web APIs deliver authentication, account management, ecommerce, and analytics for games published on the Epic Games Store and other platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Game Services
  - Gaming
  - Cross-Platform
  - Achievements
  - Leaderboards
  - Matchmaking
  - Anti-Cheat
  - OAuth2
url: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.19'
position: Provider
access: Partner
apis:
  - aid: epic:epic-account-services
    name: Epic Account Services API
    description: Epic Account Services (EAS) provides authentication and identity for players using Epic Games accounts. Supports OAuth 2.0 authorization code, device, and exchange code flows, account info retrieval, and single sign-on across Epic Games Store and partner titles.
    humanURL: https://dev.epicgames.com/docs/epic-account-services
    baseURL: https://api.epicgames.dev
    tags:
      - Authentication
      - OAuth2
      - Identity
      - Single Sign-On
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/epic-account-services
      - type: Authentication
        url: https://dev.epicgames.com/docs/epic-account-services/auth/auth-interface
      - type: GettingStarted
        url: https://dev.epicgames.com/docs/epic-account-services/getting-started
  - aid: epic:eos-achievements
    name: Epic Online Services Achievements API
    description: The EOS Achievements API enables developers to define, unlock, and query player achievements across platforms. Supports definitions, player progress, and unlocking via the EOS SDK or Web API.
    humanURL: https://dev.epicgames.com/docs/game-services/achievements
    baseURL: https://api.epicgames.dev
    tags:
      - Achievements
      - Game Services
      - Progression
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/achievements
  - aid: epic:eos-leaderboards
    name: Epic Online Services Leaderboards API
    description: The EOS Leaderboards API provides global and per-friend leaderboards backed by player stats. Developers configure leaderboards in the developer portal and query rankings via the EOS SDK or Web API.
    humanURL: https://dev.epicgames.com/docs/game-services/leaderboards
    baseURL: https://api.epicgames.dev
    tags:
      - Leaderboards
      - Game Services
      - Stats
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/leaderboards
  - aid: epic:eos-stats
    name: Epic Online Services Stats API
    description: The EOS Stats API tracks player statistics over time, providing the data source that powers leaderboards and achievements. Supports ingest, increment, and query operations on stat values.
    humanURL: https://dev.epicgames.com/docs/game-services/eos-stats-interface
    baseURL: https://api.epicgames.dev
    tags:
      - Stats
      - Game Services
      - Telemetry
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/eos-stats-interface
  - aid: epic:eos-friends
    name: Epic Online Services Friends API
    description: The EOS Friends API exposes a player's Epic Games friends list, allowing games to surface social presence, invitations, and party formation across platforms.
    humanURL: https://dev.epicgames.com/docs/epic-account-services/eos-friends-interface
    baseURL: https://api.epicgames.dev
    tags:
      - Friends
      - Social
      - Game Services
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/epic-account-services/eos-friends-interface
  - aid: epic:eos-ecom
    name: Epic Online Services Ecom API
    description: The EOS Ecom (Ecommerce) Interface API exposes the player's Epic Games Store entitlements, ownership, catalog offers, and checkout flows. Used by titles published on the Epic Games Store to verify purchases and unlock downloadable content.
    humanURL: https://dev.epicgames.com/docs/epic-games-store/services/ecom/ecom-overview
    baseURL: https://api.epicgames.dev
    tags:
      - Ecommerce
      - Entitlements
      - Catalog
      - Epic Games Store
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/epic-games-store/services/ecom/ecom-overview
  - aid: epic:eos-lobby-sessions
    name: Epic Online Services Lobby and Sessions API
    description: The EOS Lobby and Sessions APIs provide matchmaking primitives for multiplayer games, including lobby creation, joining, attribute filtering, and dedicated session management.
    humanURL: https://dev.epicgames.com/docs/game-services/lobbies-and-sessions
    baseURL: https://api.epicgames.dev
    tags:
      - Matchmaking
      - Lobbies
      - Sessions
      - Multiplayer
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/lobbies-and-sessions
  - aid: epic:eos-player-data-storage
    name: Epic Online Services Player Data Storage API
    description: The EOS Player Data Storage and Title Storage APIs persist per-player save data and shared title-level configuration in the cloud, with cross-platform availability and versioning.
    humanURL: https://dev.epicgames.com/docs/game-services/player-data-storage
    baseURL: https://api.epicgames.dev
    tags:
      - Storage
      - Cloud Saves
      - Game Services
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/player-data-storage
  - aid: epic:eos-anti-cheat
    name: Epic Online Services Anti-Cheat API
    description: Easy Anti-Cheat (EAC) integrated into Epic Online Services provides kernel and user-mode anti-cheat protections, server-side validation, and reporting tooling for cross-platform multiplayer titles.
    humanURL: https://dev.epicgames.com/docs/game-services/anti-cheat
    baseURL: https://api.epicgames.dev
    tags:
      - Anti-Cheat
      - Security
      - Multiplayer
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/anti-cheat
  - aid: epic:eos-voice
    name: Epic Online Services Voice API
    description: The EOS Voice Interface delivers in-game voice chat using Vivox backend infrastructure, with positional audio, room management, and moderation controls across platforms.
    humanURL: https://dev.epicgames.com/docs/game-services/eos-voice-interface
    baseURL: https://api.epicgames.dev
    tags:
      - Voice
      - Chat
      - Communications
      - Vivox
    properties:
      - type: Documentation
        url: https://dev.epicgames.com/docs/game-services/eos-voice-interface
common:
  - type: Website
    url: https://www.epicgames.com/
  - type: Portal
    url: https://dev.epicgames.com/portal/
  - type: Documentation
    url: https://dev.epicgames.com/docs/
  - type: GettingStarted
    url: https://dev.epicgames.com/docs/epic-online-services/eos-get-started
  - type: Authentication
    url: https://dev.epicgames.com/docs/epic-account-services/auth/auth-interface
  - type: TermsOfService
    url: https://dev.epicgames.com/services-agreement
  - type: PrivacyPolicy
    url: https://www.epicgames.com/site/en-US/privacypolicy
  - type: Support
    url: https://dev.epicgames.com/community/
  - type: Store
    url: https://store.epicgames.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
