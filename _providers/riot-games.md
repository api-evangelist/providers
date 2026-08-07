---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Riot Games Agentic Access
  operation_count: 17
  slug: riot-games-agentic-access
  summary_line: 17 operations
api_count: 13
apis:
- description: API for accessing VALORANT game data including match history, ranked standings, content catalog, and status information. Covers both PC and console platforms.
  name: VALORANT API
  slug: valorant-api
- description: API for accessing Teamfight Tactics game data including match history, ranked standings, summoner profiles, and live spectator data for the auto battler game mode.
  name: Teamfight Tactics API
  slug: teamfight-tactics-api
- description: API for accessing Legends of Runeterra game data including player decks, inventory, match history, and ranked standings. Requires Riot Sign-On (RSO) authentication for player-specific data.
  name: Legends of Runeterra API
  slug: legends-of-runeterra-api
- description: Cross-game account API for resolving Riot IDs (gameName + tagLine) to PUUIDs used across all Riot Games APIs. Supports account linking through Riot Sign-On (RSO) OAuth 2.0 authentication.
  name: Riot Account API
  slug: account-api
- description: Static data and asset delivery service for Riot Games. Provides localized game data for champions, items, summoner spells, runes, profile icons, and maps in JSON format. Available in 28+ languages. Up
  name: Riot Data Dragon
  slug: data-dragon
- description: Free champion rotation
  name: Riot Games Champion API
  slug: riot-games-champion-api
- description: Champion mastery data
  name: Riot Games Champion Mastery API
  slug: riot-games-champion-mastery-api
- description: Clash tournament operations
  name: Riot Games Clash API
  slug: riot-games-clash-api
- description: Ranked league standings
  name: Riot Games League API
  slug: riot-games-league-api
- description: Match history and details
  name: Riot Games Match API
  slug: riot-games-match-api
- description: Live game spectator data
  name: Riot Games Spectator API
  slug: riot-games-spectator-api
- description: Platform status
  name: Riot Games Status API
  slug: riot-games-status-api
- description: Summoner profile operations
  name: Riot Games Summoner API
  slug: riot-games-summoner-api
artifact_total: 45
collections:
- collection_type: open
  name: Riot Games League of Legends API
  slug: open-riot-games-league-of-legends
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/riot-games-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/riot-games-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riot-games-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/riot-games-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/riot-games
- group: other
  title: ''
  type: Developer
  url: https://developer.riotgames.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.riotgames.com/apis
- group: auth
  title: ''
  type: Authentication
  url: https://developer.riotgames.com/docs/portal
- group: operate
  title: ''
  type: RateLimiting
  url: https://developer.riotgames.com/docs/portal
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/RiotGames
- group: start
  title: ''
  type: Signup
  url: https://developer.riotgames.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.riotgames.com/policies/general
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riotgames.com/en/privacy-notice
- group: company
  title: ''
  type: Website
  url: https://www.riotgames.com
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/rules/riot-games-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-schema/riot-games-summoner-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-schema/riot-games-match-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/json-ld/riot-games-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/vocabulary/riot-games-vocabulary.yml
created: '2025-02-08'
description: Riot Games provides a comprehensive developer platform for accessing game data across League of Legends, VALORANT, Teamfight Tactics, Legends of Runeterra, and other titles. The Riot Developer Portal offers REST APIs for match history, ranked standings, champion mastery, live spectator data, tournament management, and player account data.
examples:
- key_count: 2
  name: Riot Games Get Match Example
  slug: riot-games-get-match-example
- key_count: 2
  name: Riot Games Get Summoner Example
  slug: riot-games-get-summoner-example
finops:
- name: Riot Games Finops
  service_category: Gaming Developer Platform
  slug: riot-games-finops
graphqls:
- description: This GraphQL schema provides a unified query interface over the Riot Games Developer API, covering League of Legends, VALORANT, Teamfight Tactics, Legends of Runeterra, and the cross-game Account API.
  name: Riot Games GraphQL Schema
  slug: riot-games-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riot-games.png
json_schemas:
- name: AccountDTO
  property_count: 3
  slug: riot-games-accountdto
- name: ChampionInfoDTO
  property_count: 3
  slug: riot-games-championinfodto
- name: ChampionMasteryDTO
  property_count: 9
  slug: riot-games-championmasterydto
- name: ClashPlayerDTO
  property_count: 4
  slug: riot-games-clashplayerdto
- name: CurrentGameInfoDTO
  property_count: 9
  slug: riot-games-currentgameinfodto
- name: CurrentGameParticipantDTO
  property_count: 7
  slug: riot-games-currentgameparticipantdto
- name: FeaturedGamesDTO
  property_count: 2
  slug: riot-games-featuredgamesdto
- name: LeagueEntryDTO
  property_count: 13
  slug: riot-games-leagueentrydto
- name: LeagueListDTO
  property_count: 5
  slug: riot-games-leaguelistdto
- name: Riot Games Match
  property_count: 2
  slug: riot-games-match
- name: MatchDTO
  property_count: 2
  slug: riot-games-matchdto
- name: MatchTimelineDTO
  property_count: 2
  slug: riot-games-matchtimelinedto
- name: ParticipantDTO
  property_count: 12
  slug: riot-games-participantdto
- name: PlatformDataDTO
  property_count: 5
  slug: riot-games-platformdatadto
- name: Riot Games Summoner
  property_count: 7
  slug: riot-games-summoner
- name: SummonerDTO
  property_count: 7
  slug: riot-games-summonerdto
json_structures:
- name: Riot Games Match Structure
  property_count: 0
  slug: riot-games-match-structure
- name: Riot Games Structure
  property_count: 0
  slug: riot-games-structure
jsonld:
- class_count: 48
  name: Riot Games Context
  property_count: 0
  slug: riot-games-context
layout: provider
modified: '2026-05-19'
name: Riot Games
nav: Providers
network: true
overview: 'Riot Games publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Champion API, Champion Mastery API, Clash API, and 5 more. Tagged areas include Esports, Gaming, League of Legends, Legends of Runeterra, and Teamfight Tactics.


  The Riot Games catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Riot Games'' developer surface includes authentication, documentation, signup flow, and 16 more developer resources.'
plans:
- name: Riot Games Plans Pricing
  plan_count: 3
  slug: riot-games-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 5
  name: Riot Games Rate Limits
  slug: riot-games-rate-limits
rules:
- name: Riot Games API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: riot-games-jsonschema-spectral-rules
- name: Riot Games API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: riot-games-rules
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riot-games/refs/heads/main/screenshots/riot-games-2026-06-20T193125.png
security:
- kind: authentication
  name: Riot Games Authentication
  slug: riot-games-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Riot Games Domain Security
  slug: riot-games-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Riot Games Vulnerability Disclosure
  slug: riot-games-vulnerability-disclosure
  summary_line: Hackerone
slug: riot-games
tags:
- Esports
- Gaming
- League of Legends
- Legends of Runeterra
- Teamfight Tactics
- VALORANT
website: https://www.riotgames.com
---
