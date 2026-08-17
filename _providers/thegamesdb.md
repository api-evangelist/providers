---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Thegamesdb Agentic Access
  operation_count: 26
  slug: thegamesdb-agentic-access
  summary_line: 26 operations
api_count: 5
apis:
- description: The Developers API from TheGamesDB — 1 operation(s) for developers.
  name: TheGamesDB Developers API
  slug: thegamesdb-developers-api
- description: The Games API from TheGamesDB — 6 operation(s) for games.
  name: TheGamesDB Games API
  slug: thegamesdb-games-api
- description: The Genres API from TheGamesDB — 1 operation(s) for genres.
  name: TheGamesDB Genres API
  slug: thegamesdb-genres-api
- description: The Platforms API from TheGamesDB — 4 operation(s) for platforms.
  name: TheGamesDB Platforms API
  slug: thegamesdb-platforms-api
- description: The Publishers API from TheGamesDB — 1 operation(s) for publishers.
  name: TheGamesDB Publishers API
  slug: thegamesdb-publishers-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TheGamesDB Developers API
  slug: open-thegamesdb-developers-api
- collection_type: open
  name: TheGamesDB Developers Games API
  slug: open-thegamesdb-games-api
- collection_type: open
  name: TheGamesDB Developers Genres API
  slug: open-thegamesdb-genres-api
- collection_type: open
  name: TheGamesDB Developers Platforms API
  slug: open-thegamesdb-platforms-api
- collection_type: open
  name: TheGamesDB Developers Publishers API
  slug: open-thegamesdb-publishers-api
- collection_type: open
  name: TheGamesDB API
  slug: open-thegamesdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thegamesdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thegamesdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thegamesdb.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.thegamesdb.net/
- group: start
  title: ''
  type: Signup
  url: https://api.thegamesdb.net/key.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheGamesDB
- group: design
  title: TheGamesDB Spectral Rules
  type: SpectralRules
  url: rules/thegamesdb-spectral-rules.yml
- group: design
  title: TheGamesDB Vocabulary
  type: Vocabulary
  url: vocabulary/thegamesdb-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://api.thegamesdb.net/key.php
- group: auth
  title: ''
  type: Authentication
  url: https://api.thegamesdb.net/key.php
created: '2025-02-08'
description: An open, online database for video game fans providing game information, artwork, and metadata via API.
examples:
- key_count: 12
  name: Thegamesdb Game Example
  slug: thegamesdb-game-example
- key_count: 5
  name: Thegamesdb Game Image Example
  slug: thegamesdb-game-image-example
- key_count: 5
  name: Thegamesdb Games By Game Id Response Example
  slug: thegamesdb-games-by-game-id-response-example
- key_count: 3
  name: Thegamesdb Games Images Response Example
  slug: thegamesdb-games-images-response-example
- key_count: 3
  name: Thegamesdb Games Updates Response Example
  slug: thegamesdb-games-updates-response-example
- key_count: 3
  name: Thegamesdb Genres Developers Publishers Response Example
  slug: thegamesdb-genres-developers-publishers-response-example
- key_count: 10
  name: Thegamesdb Platform Example
  slug: thegamesdb-platform-example
- key_count: 3
  name: Thegamesdb Platforms Response Example
  slug: thegamesdb-platforms-response-example
features:
- description: Search games by name with optional platform filtering
  name: Game Search
- description: Retrieve complete game metadata by ID including overview, ratings, and system requirements
  name: Game Details
- description: Full catalog of all gaming platforms with hardware specifications and images
  name: Platform Catalog
- description: Boxart, screenshots, fanart, banners, and clearlogos for games and platforms
  name: Game Artwork
- description: Retrieve games updated since a given timestamp for database synchronization
  name: Game Updates
- description: Complete lists of genres, developers, and publishers
  name: Reference Data
- description: Request multiple game or platform IDs in a single API call
  name: Batch Requests
finops:
- name: Thegamesdb Finops
  service_category: API
  slug: thegamesdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thegamesdb.png
integrations:
- description: Popular retro gaming frontend using TheGamesDB for scraping
  name: EmulationStation
- description: Game scraper tools using the API for artwork and metadata
  name: Skraper
json_schemas:
- name: GameImage
  property_count: 5
  slug: thegamesdb-game-image
- name: Game
  property_count: 12
  slug: thegamesdb-game
- name: GamesByGameIDResponse
  property_count: 5
  slug: thegamesdb-games-by-game-id-response
- name: GamesImagesResponse
  property_count: 3
  slug: thegamesdb-games-images-response
- name: GamesUpdatesResponse
  property_count: 3
  slug: thegamesdb-games-updates-response
- name: GenresDevelopersPublishersResponse
  property_count: 3
  slug: thegamesdb-genres-developers-publishers-response
- name: Platform
  property_count: 10
  slug: thegamesdb-platform
- name: PlatformsResponse
  property_count: 3
  slug: thegamesdb-platforms-response
json_structures:
- name: Thegamesdb Game Image Structure
  property_count: 5
  slug: thegamesdb-game-image-structure
- name: Thegamesdb Game Structure
  property_count: 12
  slug: thegamesdb-game-structure
- name: Thegamesdb Games By Game Id Response Structure
  property_count: 5
  slug: thegamesdb-games-by-game-id-response-structure
- name: Thegamesdb Games Images Response Structure
  property_count: 3
  slug: thegamesdb-games-images-response-structure
- name: Thegamesdb Games Updates Response Structure
  property_count: 3
  slug: thegamesdb-games-updates-response-structure
- name: Thegamesdb Genres Developers Publishers Response Structure
  property_count: 3
  slug: thegamesdb-genres-developers-publishers-response-structure
- name: Thegamesdb Platform Structure
  property_count: 10
  slug: thegamesdb-platform-structure
- name: Thegamesdb Platforms Response Structure
  property_count: 3
  slug: thegamesdb-platforms-response-structure
jsonld:
- class_count: 9
  name: Thegamesdb Context
  property_count: 35
  slug: thegamesdb-context
layout: provider
modified: '2026-05-19'
name: TheGamesDB
nav: Providers
network: true
overview: 'TheGamesDB publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Developers API, Games API, Genres API, and 2 more. Tagged areas include Database, Gaming, Video Games, Metadata, and Artwork.


  The TheGamesDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TheGamesDB''s developer surface includes documentation, signup flow, authentication, and 7 more developer resources.'
plans:
- name: Thegamesdb Plans Pricing
  plan_count: 3
  slug: thegamesdb-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Thegamesdb Rate Limits
  slug: thegamesdb-rate-limits
rules:
- name: TheGamesDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thegamesdb-jsonschema-spectral-rules
- name: TheGamesDB API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 14
  slug: thegamesdb-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.1
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thegamesdb/refs/heads/main/screenshots/thegamesdb-2026-06-20T195247.png
security:
- kind: domain-security
  name: Thegamesdb Domain Security
  slug: thegamesdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thegamesdb
tags:
- Database
- Gaming
- Video Games
- Metadata
- Artwork
use_cases:
- description: Build game databases, libraries, and collection managers
  name: Gaming Applications
- description: Power game scrapers for Emulation Station, Kodi, and similar media centers
  name: Media Centers
- description: Manage personal or commercial video game collection databases
  name: Game Collections
- description: Power AI agents that answer questions about video games
  name: AI Game Assistant
website: https://thegamesdb.net/
---
