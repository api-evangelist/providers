---
aid: riot-games
name: Riot Games
description: Riot Games provides a comprehensive developer platform for accessing game data across League of Legends, VALORANT, Teamfight Tactics, Legends of Runeterra, and other titles. The Riot Developer Portal offers REST APIs for match history, ranked standings, champion mastery, live spectator data, tournament management, and player account data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Esports
  - Gaming
  - League of Legends
  - Legends of Runeterra
  - Teamfight Tactics
  - VALORANT
url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: riot-games:league-of-legends-api
    name: League of Legends API
    description: API for accessing League of Legends game data including champion mastery, clash tournaments, ranked league standings, match history, live spectator data, summoner profiles, and tournament management. All APIs are currently version 4 or 5.
    humanURL: https://developer.riotgames.com/apis
    baseURL: https://na1.api.riotgames.com
    tags:
      - Champion Mastery
      - Clash
      - League of Legends
      - Match History
      - Ranked
      - Summoner
      - Tournaments
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/openapi/riot-games-league-of-legends-openapi.yml
  - aid: riot-games:valorant-api
    name: VALORANT API
    description: API for accessing VALORANT game data including match history, ranked standings, content catalog, and status information. Covers both PC and console platforms.
    humanURL: https://developer.riotgames.com/apis
    baseURL: https://na.api.riotgames.com
    tags:
      - Console
      - Match History
      - Ranked
      - VALORANT
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/docs/valorant
  - aid: riot-games:teamfight-tactics-api
    name: Teamfight Tactics API
    description: API for accessing Teamfight Tactics game data including match history, ranked standings, summoner profiles, and live spectator data for the auto battler game mode.
    humanURL: https://developer.riotgames.com/apis
    baseURL: https://na1.api.riotgames.com
    tags:
      - Match History
      - Ranked
      - Summoner
      - Teamfight Tactics
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/apis
  - aid: riot-games:legends-of-runeterra-api
    name: Legends of Runeterra API
    description: API for accessing Legends of Runeterra game data including player decks, inventory, match history, and ranked standings. Requires Riot Sign-On (RSO) authentication for player-specific data.
    humanURL: https://developer.riotgames.com/apis
    baseURL: https://americas.api.riotgames.com
    tags:
      - Decks
      - Legends of Runeterra
      - Match History
      - Ranked
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/docs/lor
  - aid: riot-games:account-api
    name: Riot Account API
    description: Cross-game account API for resolving Riot IDs (gameName + tagLine) to PUUIDs used across all Riot Games APIs. Supports account linking through Riot Sign-On (RSO) OAuth 2.0 authentication.
    humanURL: https://developer.riotgames.com/apis
    baseURL: https://americas.api.riotgames.com
    tags:
      - Account
      - Authentication
      - Identity
      - PUUID
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/apis
  - aid: riot-games:data-dragon
    name: Riot Data Dragon
    description: Static data and asset delivery service for Riot Games. Provides localized game data for champions, items, summoner spells, runes, profile icons, and maps in JSON format. Available in 28+ languages. Updated with each game patch.
    humanURL: https://developer.riotgames.com/docs/lol
    baseURL: https://ddragon.leagueoflegends.com/cdn
    tags:
      - Champions
      - Data Dragon
      - Items
      - Static Data
    properties:
      - type: Documentation
        url: https://developer.riotgames.com/docs/lol
common:
  - type: Developer
    url: https://developer.riotgames.com/
  - type: Documentation
    url: https://developer.riotgames.com/apis
  - type: Authentication
    url: https://developer.riotgames.com/docs/portal
  - type: RateLimiting
    url: https://developer.riotgames.com/docs/portal
  - type: GithubOrg
    url: https://github.com/RiotGames
  - type: SignUp
    url: https://developer.riotgames.com/
  - type: TermsOfService
    url: https://developer.riotgames.com/policies/general
  - type: PrivacyPolicy
    url: https://www.riotgames.com/en/privacy-notice
  - type: Website
    url: https://www.riotgames.com
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/rules/riot-games-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/capabilities/game-data-analytics.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-schema/riot-games-summoner-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-schema/riot-games-match-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-ld/riot-games-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/vocabulary/riot-games-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
