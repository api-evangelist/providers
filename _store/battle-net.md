---
aid: battle-net
url: https://raw.githubusercontent.com/api-evangelist/battle-net/refs/heads/main/apis.yml
name: Battle.net
description: Battle.net is Blizzard Entertainment's online gaming platform and developer API ecosystem. It provides game data and player profile APIs for World of Warcraft, Diablo III, Hearthstone, and StarCraft II via OAuth 2.0-secured REST endpoints, enabling developers to build applications that access character data, game statistics, leaderboards, card collections, and auction house data.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Games
  - Gaming
  - Blizzard
  - World Of Warcraft
  - Diablo
  - Hearthstone
  - Starcraft
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-21'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: battle-net:world-of-warcraft-game-data
    name: World of Warcraft Game Data API
    description: Provides access to World of Warcraft game data including achievements, auction house listings, character classes, races, realms, guild data, items, spells, zones, and PvP leaderboards. Requires OAuth 2.0 client credentials flow.
    humanURL: https://community.developer.battle.net/documentation/world-of-warcraft/game-data-apis
    tags:
      - Games
      - Gaming
      - World Of Warcraft
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/world-of-warcraft/game-data-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:world-of-warcraft-profile
    name: World of Warcraft Profile API
    description: Provides access to player profile data for World of Warcraft including character summaries, equipment, achievements, collections, mythic keystone profile, and PvP profile data. Requires OAuth 2.0 authorization code flow with user consent.
    humanURL: https://community.developer.battle.net/documentation/world-of-warcraft/profile-apis
    tags:
      - Games
      - Gaming
      - World Of Warcraft
      - Player Profile
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/world-of-warcraft/profile-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:world-of-warcraft-classic
    name: World of Warcraft Classic Game Data API
    description: Provides game data for World of Warcraft Classic (Era and Seasonal), including classic realm lists, auction house data, character classes, races, and items specific to the classic game versions.
    humanURL: https://community.developer.battle.net/documentation/world-of-warcraft-classic/game-data-apis
    tags:
      - Games
      - Gaming
      - World Of Warcraft Classic
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/world-of-warcraft-classic/game-data-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:diablo-3-game-data
    name: Diablo III Game Data API
    description: Provides access to Diablo III game data including season index and season data, era index and era leaderboards. Requires OAuth 2.0 client credentials flow.
    humanURL: https://community.developer.battle.net/documentation/diablo-3/game-data-apis
    tags:
      - Games
      - Gaming
      - Diablo
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/diablo-3/game-data-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:diablo-3-community
    name: Diablo III Community API
    description: Provides access to Diablo III community data including character profiles, hero data, item data, follower data, artisan data, and act information. Requires OAuth 2.0 for profile endpoints.
    humanURL: https://community.developer.battle.net/documentation/diablo-3/community-apis
    tags:
      - Games
      - Gaming
      - Diablo
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/diablo-3/community-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:hearthstone-game-data
    name: Hearthstone Game Data API
    description: Provides access to Hearthstone card data including card search, card back collections, deck building, and metadata such as card sets, classes, card types, rarities, and keywords. Requires OAuth 2.0 client credentials flow.
    humanURL: https://community.developer.battle.net/documentation/hearthstone/game-data-apis
    tags:
      - Games
      - Gaming
      - Hearthstone
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/hearthstone/game-data-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
      - type: OpenAPI
        url: openapi/battle-net-hearthstone-game-data.yaml
      - type: JSONSchema
        url: json-schema/hearthstone-game-data-card-schema.json
        title: Card Schema
      - type: JSONSchema
        url: json-schema/hearthstone-game-data-card-back-schema.json
        title: Card Back Schema
      - type: JSONSchema
        url: json-schema/hearthstone-game-data-deck-schema.json
        title: Deck Schema
      - type: JSONSchema
        url: json-schema/hearthstone-game-data-metadata-schema.json
        title: Metadata Schema
  - aid: battle-net:starcraft-2-game-data
    name: StarCraft II Game Data API
    description: Provides access to StarCraft II game data including league data for multiple game modes. Requires OAuth 2.0 client credentials flow.
    humanURL: https://community.developer.battle.net/documentation/starcraft-2/game-data-apis
    tags:
      - Games
      - Gaming
      - Starcraft
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/starcraft-2/game-data-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:starcraft-2-community
    name: StarCraft II Community API
    description: Provides access to StarCraft II community data including player profile, ladder summaries, grandmaster leaderboards, and static game data for profile, legacy, and ladder resources.
    humanURL: https://community.developer.battle.net/documentation/starcraft-2/community-apis
    tags:
      - Games
      - Gaming
      - Starcraft
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/starcraft-2/community-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
  - aid: battle-net:battle-net-oauth
    name: Battle.net OAuth API
    description: Provides OAuth 2.0 authorization services for Battle.net including client credentials flow for game data access and authorization code flow for player profile data. Token endpoint, authorization endpoint, and token validation endpoint are available per region (US, EU, APAC).
    humanURL: https://community.developer.battle.net/documentation/battle-net/oauth-apis
    tags:
      - Authentication
      - Gaming
      - OAuth
    properties:
      - type: Documentation
        url: https://community.developer.battle.net/documentation/battle-net/oauth-apis
      - type: Authentication
        url: https://community.developer.battle.net/documentation/guides/using-oauth
common:
  - type: Portal
    url: https://community.developer.battle.net/
  - type: Documentation
    url: https://community.developer.battle.net/documentation
  - type: GettingStarted
    url: https://community.developer.battle.net/documentation/guides/getting-started
  - type: Authentication
    url: https://community.developer.battle.net/documentation/guides/using-oauth
  - type: RateLimits
    url: https://us.forums.blizzard.com/en/blizzard/t/api-access-clients-rate-limits/5602
  - type: GitHubOrganization
    url: https://github.com/Blizzard
  - type: Support
    url: https://us.forums.blizzard.com/en/blizzard/c/api-discussion
  - type: TermsOfService
    url: https://www.blizzard.com/en-us/legal/a2989b50-54f6-43f3-b55c-fa78e0ca3b38/blizzard-developer-api-terms-of-use
  - type: SDK
    url: https://github.com/Blizzard/passport-bnet
    title: Passport.js Battle.net Strategy
  - type: SDK
    url: https://github.com/Blizzard/omniauth-bnet
    title: OmniAuth Battle.net Strategy (Ruby)
  - type: CodeExamples
    url: https://github.com/Blizzard/java-signature-generator
    title: Java OAuth Sample
  - type: CodeExamples
    url: https://github.com/Blizzard/node-signature-generator
    title: Node.js OAuth Sample
  - type: CodeExamples
    url: https://github.com/Blizzard/ruby-signature-generator
    title: Ruby OAuth Sample
  - type: CodeExamples
    url: https://github.com/Blizzard/oauth-client-sample
    title: OAuth Client Sample
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Supports both client credentials flow for game data and authorization code flow for player profile data access.
      - name: Multi-Region Support
        description: APIs are available across US, EU, and APAC regions with regional base URLs (us.api.blizzard.com, eu.api.blizzard.com).
      - name: Game Data APIs
        description: Access static and dynamic game data including items, spells, realms, seasons, leaderboards, and card metadata.
      - name: Player Profile APIs
        description: Access authenticated player data including character profiles, achievements, equipment, and PvP records.
      - name: Localization Support
        description: API responses support multiple locales per region, enabling localized game data in multiple languages.
  - type: UseCases
    data:
      - name: Game Companion Apps
        description: Build companion applications for WoW, Hearthstone, or Diablo that display character stats, gear scores, and progression.
      - name: Auction House Trackers
        description: Monitor World of Warcraft auction house data to track item prices and market trends.
      - name: Leaderboard Displays
        description: Show StarCraft II, Diablo III season, and WoW PvP leaderboards in custom applications.
      - name: Deck Builders
        description: Create Hearthstone deck-building tools using the card data, metadata, and deck APIs.
      - name: Guild Management Tools
        description: Build guild management utilities using WoW guild roster, achievements, and activity data.
  - type: SpectralRules
    url: rules/battle-net-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/battle-net-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/gaming-data.yaml
  - type: Integrations
    data:
      - name: Passport.js
        description: Battle.net OAuth strategy for Node.js applications using Passport.js authentication middleware.
      - name: OmniAuth
        description: Battle.net authentication strategy for Ruby on Rails applications using OmniAuth.
      - name: Microcks
        description: API mocking and testing platform for Battle.net API contract testing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
