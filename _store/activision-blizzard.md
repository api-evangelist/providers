---
aid: activision-blizzard
url: https://raw.githubusercontent.com/api-evangelist/activision-blizzard/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - aid: activision-blizzard:battle-net
    name: Battle.net API
    tags:
      - Gaming
      - World Of Warcraft
      - Hearthstone
      - Diablo
      - Starcraft
      - Battle.net
    properties:
      - type: HumanURL
        url: https://develop.battle.net/
      - type: BaseURL
        url: https://us.api.blizzard.com
      - type: OpenAPI
        url: openapi/activision-blizzard-battle-net.json
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: Examples
        url: examples/
    description: Game data and profile APIs for World of Warcraft, Diablo III, Hearthstone, StarCraft II, and Battle.net account information. Requires OAuth2 authentication via develop.battle.net.
common:
  - type: Website
    url: https://www.activision-blizzard.com
  - type: Portal
    url: https://develop.battle.net/
  - type: Documentation
    url: https://develop.battle.net/documentation
  - type: GettingStarted
    url: https://develop.battle.net/documentation/guides/getting-started
  - type: Authentication
    url: https://develop.battle.net/documentation/guides/using-oauth
  - type: Pricing
    url: https://develop.battle.net/documentation/guides/getting-started
  - type: GitHubOrganization
    url: https://github.com/Blizzard
  - type: SpectralRules
    url: rules/activision-blizzard-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/activision-blizzard-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/game-data.yaml
  - type: JSONLD
    url: json-ld/activision-blizzard-context.jsonld
description: Activision Blizzard is a global video game developer and publisher producing franchises including Call of Duty, World of Warcraft, Diablo, Overwatch, and Candy Crush across console, PC, and mobile platforms.
features:
  - name: World Of Warcraft Game Data
    description: Access WoW character profiles, realm listings, guild data, and item information via the Battle.net API.
    tags:
      - World Of Warcraft
      - Game Data
  - name: Diablo III Profiles
    description: Retrieve Diablo III career profiles and hero data for Battle.net accounts.
    tags:
      - Diablo
      - Game Data
  - name: Hearthstone Cards
    description: Search and retrieve Hearthstone collectible card data including class, set, and mana cost filters.
    tags:
      - Hearthstone
      - Game Data
  - name: StarCraft II Profiles
    description: Access StarCraft II player profiles and ladder data.
    tags:
      - Starcraft
      - Game Data
  - name: Battle.net OAuth2
    description: OAuth2 client credentials and authorization code flows for game data and profile access.
    tags:
      - Authentication
      - OAuth2
  - name: Regional API Endpoints
    description: Battle.net APIs are available across US, EU, KR, TW, and CN regions.
    tags:
      - Regions
      - Infrastructure
useCases:
  - name: Community App Development
    description: Build community tools, addons, leaderboards, and companion apps powered by live game data.
    tags:
      - Community
      - Developer
  - name: Game Analytics
    description: Analyze game statistics, player performance, and progression data across Blizzard franchises.
    tags:
      - Analytics
      - Gaming
  - name: Fan Websites
    description: Power fan websites and wikis with live character profiles, item databases, and realm status.
    tags:
      - Fan Sites
      - Gaming
  - name: Discord Bots
    description: Build Discord bots that surface WoW character lookups, Hearthstone card searches, and Diablo profiles.
    tags:
      - Discord
      - Bots
integrations:
  - name: WoW Community Tools
    description: Integrate with World of Warcraft addon ecosystems and community platforms like Wowhead and Curseforge.
    tags:
      - World Of Warcraft
      - Community
  - name: Twitch
    description: Surface game data in Twitch stream overlays and channel bot integrations.
    tags:
      - Twitch
      - Streaming
  - name: Discord
    description: Enable Discord server bots to query Blizzard game data for guild and community members.
    tags:
      - Discord
      - Community
solutions:
  - name: Game Data API Access
    description: Free API access via developer.battle.net for community and non-commercial game data use.
    tags:
      - Developer
      - Free Tier
  - name: OAuth2 Profile Access
    description: Authorized user profile access using OAuth2 authorization code flow for personalized data.
    tags:
      - OAuth2
      - Profile
---
