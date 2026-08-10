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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Battle Net Agentic Access
  operation_count: 7
  slug: battle-net-agentic-access
  summary_line: 7 operations
api_count: 12
apis:
- description: 'Provides access to World of Warcraft game data including achievements, auction house listings, character classes, races, realms, guild data, items, spells, zones, and PvP leaderboards. Requires OAuth '
  name: World of Warcraft Game Data API
  slug: world-of-warcraft-game-data
- description: Provides access to player profile data for World of Warcraft including character summaries, equipment, achievements, collections, mythic keystone profile, and PvP profile data. Requires OAuth 2.0 auth
  name: World of Warcraft Profile API
  slug: world-of-warcraft-profile
- description: Provides game data for World of Warcraft Classic (Era and Seasonal), including classic realm lists, auction house data, character classes, races, and items specific to the classic game versions.
  name: World of Warcraft Classic Game Data API
  slug: world-of-warcraft-classic
- description: Provides access to Diablo III game data including season index and season data, era index and era leaderboards. Requires OAuth 2.0 client credentials flow.
  name: Diablo III Game Data API
  slug: diablo-3-game-data
- description: Provides access to Diablo III community data including character profiles, hero data, item data, follower data, artisan data, and act information. Requires OAuth 2.0 for profile endpoints.
  name: Diablo III Community API
  slug: diablo-3-community
- description: Provides access to StarCraft II game data including league data for multiple game modes. Requires OAuth 2.0 client credentials flow.
  name: StarCraft II Game Data API
  slug: starcraft-2-game-data
- description: Provides access to StarCraft II community data including player profile, ladder summaries, grandmaster leaderboards, and static game data for profile, legacy, and ladder resources.
  name: StarCraft II Community API
  slug: starcraft-2-community
- description: Provides OAuth 2.0 authorization services for Battle.net including client credentials flow for game data access and authorization code flow for player profile data. Token endpoint, authorization endpo
  name: Battle.net OAuth API
  slug: battle-net-oauth
- description: Hearthstone card back collections
  name: Battle.net Card Backs API
  slug: battle-net-card-backs-api
- description: Hearthstone card search and lookup
  name: Battle.net Cards API
  slug: battle-net-cards-api
- description: Hearthstone deck lookup
  name: Battle.net Decks API
  slug: battle-net-decks-api
- description: Hearthstone metadata including sets, classes, types, and keywords
  name: Battle.net Metadata API
  slug: battle-net-metadata-api
artifact_total: 87
collections:
- collection_type: postman
  name: Battle.net Hearthstone Game Data Card Backs API
  slug: postman-battle-net-card-backs-api
- collection_type: postman
  name: Battle.net Hearthstone Game Data Card Backs Cards API
  slug: postman-battle-net-cards-api
- collection_type: postman
  name: Battle.net Hearthstone Game Data Card Backs Decks API
  slug: postman-battle-net-decks-api
- collection_type: postman
  name: Battle.net Hearthstone Game Data Card Backs Metadata API
  slug: postman-battle-net-metadata-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/battlenet/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/battle-net-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/battle-net-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/battle-net-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/battle-net-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://community.developer.battle.net/
- group: docs
  title: ''
  type: Documentation
  url: https://community.developer.battle.net/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://community.developer.battle.net/documentation/guides/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://community.developer.battle.net/documentation/guides/using-oauth
- group: operate
  title: ''
  type: RateLimits
  url: https://us.forums.blizzard.com/en/blizzard/t/api-access-clients-rate-limits/5602
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blizzard
- group: operate
  title: ''
  type: Support
  url: https://us.forums.blizzard.com/en/blizzard/c/api-discussion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blizzard.com/en-us/legal/a2989b50-54f6-43f3-b55c-fa78e0ca3b38/blizzard-developer-api-terms-of-use
- group: build
  title: Passport.js Battle.net Strategy
  type: SDKs
  url: https://github.com/Blizzard/passport-bnet
- group: build
  title: OmniAuth Battle.net Strategy (Ruby)
  type: SDKs
  url: https://github.com/Blizzard/omniauth-bnet
- group: build
  title: Java OAuth Sample
  type: CodeExamples
  url: https://github.com/Blizzard/java-signature-generator
- group: build
  title: Node.js OAuth Sample
  type: CodeExamples
  url: https://github.com/Blizzard/node-signature-generator
- group: build
  title: Ruby OAuth Sample
  type: CodeExamples
  url: https://github.com/Blizzard/ruby-signature-generator
- group: build
  title: OAuth Client Sample
  type: CodeExamples
  url: https://github.com/Blizzard/oauth-client-sample
- group: design
  title: ''
  type: SpectralRules
  url: rules/battle-net-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/battle-net-vocabulary.yaml
created: '2025-03-01'
description: Battle.net is Blizzard Entertainment's online gaming platform and developer API ecosystem. It provides game data and player profile APIs for World of Warcraft, Diablo III, Hearthstone, and StarCraft II via OAuth 2.0-secured REST endpoints, enabling developers to build applications that access character data, game statistics, leaderboards, card collections, and auction house data.
examples:
- key_count: 6
  name: Battle Net Getcard Example
  slug: battle-net-getcard-example
- key_count: 6
  name: Battle Net Getcardback Example
  slug: battle-net-getcardback-example
- key_count: 6
  name: Battle Net Getdeck Example
  slug: battle-net-getdeck-example
- key_count: 6
  name: Battle Net Getmetadata Example
  slug: battle-net-getmetadata-example
- key_count: 6
  name: Battle Net Getmetadatatype Example
  slug: battle-net-getmetadatatype-example
- key_count: 6
  name: Battle Net Searchcardbacks Example
  slug: battle-net-searchcardbacks-example
- key_count: 6
  name: Battle Net Searchcards Example
  slug: battle-net-searchcards-example
- key_count: 6
  name: Hearthstone Game Data Card Back Example
  slug: hearthstone-game-data-card-back-example
- key_count: 4
  name: Hearthstone Game Data Card Back Search Response Example
  slug: hearthstone-game-data-card-back-search-response-example
- key_count: 18
  name: Hearthstone Game Data Card Example
  slug: hearthstone-game-data-card-example
- key_count: 4
  name: Hearthstone Game Data Card Search Response Example
  slug: hearthstone-game-data-card-search-response-example
- key_count: 4
  name: Hearthstone Game Data Deck Card Example
  slug: hearthstone-game-data-deck-card-example
- key_count: 3
  name: Hearthstone Game Data Deck Class Example
  slug: hearthstone-game-data-deck-class-example
- key_count: 6
  name: Hearthstone Game Data Deck Example
  slug: hearthstone-game-data-deck-example
- key_count: 3
  name: Hearthstone Game Data Error Response Example
  slug: hearthstone-game-data-error-response-example
- key_count: 7
  name: Hearthstone Game Data Metadata Example
  slug: hearthstone-game-data-metadata-example
- key_count: 3
  name: Hearthstone Game Data Metadata Item Example
  slug: hearthstone-game-data-metadata-item-example
features:
- description: Supports both client credentials flow for game data and authorization code flow for player profile data access.
  name: OAuth 2.0 Authentication
- description: APIs are available across US, EU, and APAC regions with regional base URLs (us.api.blizzard.com, eu.api.blizzard.com).
  name: Multi-Region Support
- description: Access static and dynamic game data including items, spells, realms, seasons, leaderboards, and card metadata.
  name: Game Data APIs
- description: Access authenticated player data including character profiles, achievements, equipment, and PvP records.
  name: Player Profile APIs
- description: API responses support multiple locales per region, enabling localized game data in multiple languages.
  name: Localization Support
finops:
- name: Battle Net Finops
  service_category: Gaming / Developer APIs
  slug: battle-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/battle-net.png
integrations:
- description: Battle.net OAuth strategy for Node.js applications using Passport.js authentication middleware.
  name: Passport.js
- description: Battle.net authentication strategy for Ruby on Rails applications using OmniAuth.
  name: OmniAuth
- description: API mocking and testing platform for Battle.net API contract testing.
  name: Microcks
json_schemas:
- name: Card
  property_count: 18
  slug: battle-net-card
- name: Card Back
  property_count: 6
  slug: battle-net-cardback
- name: Card Back Search Response
  property_count: 4
  slug: battle-net-cardbacksearchresponse
- name: Card Search Response
  property_count: 4
  slug: battle-net-cardsearchresponse
- name: Deck
  property_count: 6
  slug: battle-net-deck
- name: Deck Card
  property_count: 4
  slug: battle-net-deckcard
- name: Deck Class
  property_count: 3
  slug: battle-net-deckclass
- name: Error Response
  property_count: 3
  slug: battle-net-errorresponse
- name: Metadata
  property_count: 7
  slug: battle-net-metadata
- name: Metadata Item
  property_count: 3
  slug: battle-net-metadataitem
- name: CardBack
  property_count: 6
  slug: hearthstone-game-data-card-back
- name: CardBackSearchResponse
  property_count: 4
  slug: hearthstone-game-data-card-back-search-response
- name: Card
  property_count: 18
  slug: hearthstone-game-data-card
- name: CardSearchResponse
  property_count: 4
  slug: hearthstone-game-data-card-search-response
- name: DeckCard
  property_count: 4
  slug: hearthstone-game-data-deck-card
- name: DeckClass
  property_count: 3
  slug: hearthstone-game-data-deck-class
- name: Deck
  property_count: 6
  slug: hearthstone-game-data-deck
- name: ErrorResponse
  property_count: 3
  slug: hearthstone-game-data-error-response
- name: MetadataItem
  property_count: 3
  slug: hearthstone-game-data-metadata-item
- name: Metadata
  property_count: 7
  slug: hearthstone-game-data-metadata
json_structures:
- name: Battle Net Structure
  property_count: 0
  slug: battle-net-structure
- name: Hearthstone Game Data Card Back Search Response Structure
  property_count: 4
  slug: hearthstone-game-data-card-back-search-response-structure
- name: Hearthstone Game Data Card Back Structure
  property_count: 6
  slug: hearthstone-game-data-card-back-structure
- name: Hearthstone Game Data Card Search Response Structure
  property_count: 4
  slug: hearthstone-game-data-card-search-response-structure
- name: Hearthstone Game Data Card Structure
  property_count: 18
  slug: hearthstone-game-data-card-structure
- name: Hearthstone Game Data Deck Card Structure
  property_count: 4
  slug: hearthstone-game-data-deck-card-structure
- name: Hearthstone Game Data Deck Class Structure
  property_count: 3
  slug: hearthstone-game-data-deck-class-structure
- name: Hearthstone Game Data Deck Structure
  property_count: 6
  slug: hearthstone-game-data-deck-structure
- name: Hearthstone Game Data Error Response Structure
  property_count: 3
  slug: hearthstone-game-data-error-response-structure
- name: Hearthstone Game Data Metadata Item Structure
  property_count: 3
  slug: hearthstone-game-data-metadata-item-structure
- name: Hearthstone Game Data Metadata Structure
  property_count: 7
  slug: hearthstone-game-data-metadata-structure
jsonld:
- class_count: 12
  name: Battle Net Hearthstone Game Data Context
  property_count: 37
  slug: battle-net-hearthstone-game-data-context
layout: provider
modified: '2026-05-19'
name: Battle.net
nav: Providers
network: true
overview: 'Battle.net publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Card Backs API, Cards API, Decks API, and 1 more. Tagged areas include Games, Gaming, Blizzard, World Of Warcraft, and Diablo.


  The Battle.net catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Battle.net''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, code examples, and 15 more developer resources.'
plans:
- name: Battle Net Plans Pricing
  plan_count: 1
  slug: battle-net-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 2
  name: Battle Net Rate Limits
  slug: battle-net-rate-limits
rules:
- name: Battle.net API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: battle-net-jsonschema-spectral-rules
- name: Battle.net API Rules
  rule_count: 37
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 21
  slug: battle-net-spectral-rules
scopes:
- name: Battle Net Scopes
  scope_count: 4
  slug: battle-net-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.2
    developer_ergonomics: 54.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/battle-net/refs/heads/main/screenshots/battle-net-2026-06-20T173043.png
security:
- kind: authentication
  name: Battle Net Authentication
  slug: battle-net-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Battle Net Domain Security
  slug: battle-net-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: battle-net
tags:
- Games
- Gaming
- Blizzard
- World Of Warcraft
- Diablo
- Hearthstone
- Starcraft
use_cases:
- description: Build companion applications for WoW, Hearthstone, or Diablo that display character stats, gear scores, and progression.
  name: Game Companion Apps
- description: Monitor World of Warcraft auction house data to track item prices and market trends.
  name: Auction House Trackers
- description: Show StarCraft II, Diablo III season, and WoW PvP leaderboards in custom applications.
  name: Leaderboard Displays
- description: Create Hearthstone deck-building tools using the card data, metadata, and deck APIs.
  name: Deck Builders
- description: Build guild management utilities using WoW guild roster, achievements, and activity data.
  name: Guild Management Tools
website: https://community.developer.battle.net/
---
