---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Large daily exports of the entire Scryfall card database.
  name: Scryfall Bulk Data API
  slug: scryfall-bulk-data-api
- description: Look up, search, and fetch Magic card objects in many ways.
  name: Scryfall Cards API
  slug: scryfall-cards-api
- description: Convenience lists of Magic data points (card names, types, supertypes, etc.).
  name: Scryfall Catalogs API
  slug: scryfall-catalogs-api
- description: Records of card-object migrations and merges.
  name: Scryfall Migrations API
  slug: scryfall-migrations-api
- description: Oracle rulings, WotC release notes, and Scryfall notes for a card.
  name: Scryfall Rulings API
  slug: scryfall-rulings-api
- description: 'List and retrieve Magic: The Gathering set metadata.'
  name: Scryfall Sets API
  slug: scryfall-sets-api
- description: All card symbols and their semantics.
  name: Scryfall Symbology API
  slug: scryfall-symbology-api
artifact_total: 82
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scryfall Bulk Data API
  slug: open-scryfall-bulk-data-api
- collection_type: open
  name: Scryfall Cards API
  slug: open-scryfall-cards-api
- collection_type: open
  name: Scryfall Catalogs API
  slug: open-scryfall-catalogs-api
- collection_type: open
  name: Scryfall Migrations API
  slug: open-scryfall-migrations-api
- collection_type: open
  name: Scryfall Rulings API
  slug: open-scryfall-rulings-api
- collection_type: open
  name: Scryfall Sets API
  slug: open-scryfall-sets-api
- collection_type: open
  name: Scryfall Symbology API
  slug: open-scryfall-symbology-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/scryfall/api-types/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/scryfall/api-types/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/scryfall/api-types/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/scryfall/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scryfall-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scryfall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scryfall.com
- group: docs
  title: ''
  type: Documentation
  url: https://scryfall.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://scryfall.com/docs/api/cards
- group: start
  title: ''
  type: GettingStarted
  url: https://scryfall.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://scryfall.com/blog/category/api
- group: operate
  title: ''
  type: ChangeLog
  url: https://scryfall.com/blog/category/api
- group: operate
  title: ''
  type: Support
  url: https://scryfall.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://scryfall.com/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/scryfall-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scryfall-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/scryfall-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/scryfall-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/scryfall-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scryfall
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/api-types
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/google-sheets
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/manamoji-slack
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/manamoji-discord
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/thopter
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/servo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/scion
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/gatherer-bugs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/scryfall/art-game
- group: build
  title: ''
  type: SDKs
  url: https://github.com/crookedneighbor/scryfall-client
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/scryfall-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NandaScott/Scrython
- group: build
  title: ''
  type: SDKs
  url: https://docs.rs/scryfall
- group: build
  title: ''
  type: Tools
  url: https://github.com/cryppadotta/scryfall-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/bmurdock/scryfall-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/andershaig/mcp-scryfall
- group: build
  title: ''
  type: Tools
  url: https://github.com/joemocode/scryfall-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/artillect/mtg-mcp-servers
- group: commercial
  title: ''
  type: Pricing
  url: https://scryfall.com/donate
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scryfall.com/docs/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scryfall.com/privacy
created: '2026-05-28'
description: Scryfall is the most comprehensive free Magic - The Gathering card database. The Scryfall API exposes Cards (search, autocomplete, named, random, collection, by various IDs), Sets, Rulings, Symbology, Catalogs, Bulk Data downloads, and card-object Migrations. The service is community-funded (Patreon / Ko-fi) and offered free of charge under the Wizards of the Coast Fan Content Policy for community software, research, and content. The API is HTTPS-only, requires a descriptive User-Agent and Accept header on every request, and asks that clients keep sustained traffic under 10 requests per second.
examples:
- key_count: 12
  name: Scryfall Bulk Data Example
  slug: scryfall-bulk-data-example
- key_count: 42
  name: Scryfall Card Example
  slug: scryfall-card-example
- key_count: 4
  name: Scryfall Card List Example
  slug: scryfall-card-list-example
- key_count: 15
  name: Scryfall Card Symbol Example
  slug: scryfall-card-symbol-example
- key_count: 4
  name: Scryfall Catalog Example
  slug: scryfall-catalog-example
- key_count: 4
  name: Scryfall Error Example
  slug: scryfall-error-example
- key_count: 8
  name: Scryfall Migration Example
  slug: scryfall-migration-example
- key_count: 3
  name: Scryfall Ruling Example
  slug: scryfall-ruling-example
- key_count: 21
  name: Scryfall Set Example
  slug: scryfall-set-example
features:
- description: Every Magic - The Gathering printing across paper, MTGO, and Arena with localized translations.
  name: Comprehensive card database
- description: Powerful Scryfall search syntax supporting color, type, format legality, set, price, oracle text, and more.
  name: Fulltext search query language
- description: Five daily JSON exports - oracle_cards, unique_artwork, default_cards, all_cards, and rulings - for offline ingestion.
  name: Daily bulk-data exports
- description: Six image renderings per card - small, normal, large, png, art_crop, border_crop.
  name: Multi-resolution card imagery
- description: USD / EUR / MTGO Tix pricing across normal, foil, and etched finishes.
  name: Up-to-date market prices
- description: Wizards of the Coast Oracle rulings plus Scryfall editorial notes per card.
  name: Oracle rulings
- description: All Magic mana and text symbols with parser endpoint and downloadable SVG art.
  name: Symbology with SVG renderings
- description: Canonical lists of card names, creature types, supertypes, keyword abilities, and more for autocomplete and validation.
  name: Catalogs of in-game data points
- description: No API key, no paid tier - usage is governed by attribution and a documented rate-limit policy.
  name: Free with attribution
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scryfall.png
integrations:
- description: Cross-referenced card identifiers and purchase links via tcgplayer_id.
  name: TCGplayer
- description: Cross-referenced card identifiers and purchase links via cardmarket_id.
  name: Cardmarket
- description: MTGO price feed integration and purchase links.
  name: Cardhoarder
- description: Cross-referenced via multiverse_ids for canonical Oracle text.
  name: Wizards of the Coast Gatherer
- description: Identifier mapping via mtgo_id and mtgo_foil_id.
  name: Magic Online (MTGO)
- description: Identifier mapping via arena_id.
  name: Magic Arena
- description: Commander-format recommendation data linked from card.related_uris.
  name: EDHREC
- description: Multiple community MCP servers expose Scryfall to Claude Desktop and other MCP clients.
  name: Anthropic Claude (MCP)
- description: Official Scryfall =SCRYFALL() custom function for spreadsheet card lookups.
  name: Google Sheets
- description: Official Scryfall Scion workflow for fast card search from Alfred.
  name: Alfred (macOS)
json_schemas:
- name: Scryfall Bulk Data
  property_count: 12
  slug: scryfall-bulk-data
- name: Scryfall Card Face
  property_count: 20
  slug: scryfall-card-face
- name: Scryfall Card
  property_count: 67
  slug: scryfall-card
- name: Scryfall Card Symbol
  property_count: 15
  slug: scryfall-card-symbol
- name: Scryfall Catalog
  property_count: 4
  slug: scryfall-catalog
- name: Scryfall Error
  property_count: 6
  slug: scryfall-error
- name: Scryfall Image URIs
  property_count: 6
  slug: scryfall-image-uris
- name: Scryfall Legalities
  property_count: 20
  slug: scryfall-legalities
- name: Scryfall List
  property_count: 7
  slug: scryfall-list
- name: Scryfall Migration
  property_count: 8
  slug: scryfall-migration
- name: Scryfall Prices
  property_count: 6
  slug: scryfall-prices
- name: Scryfall Related Card
  property_count: 6
  slug: scryfall-related-card
- name: Scryfall Ruling
  property_count: 5
  slug: scryfall-ruling
- name: Scryfall Set
  property_count: 21
  slug: scryfall-set
json_structures:
- name: Scryfall Bulk Data Structure
  property_count: 12
  slug: scryfall-bulk-data-structure
- name: Scryfall Card Structure
  property_count: 45
  slug: scryfall-card-structure
- name: Scryfall Card Symbol Structure
  property_count: 15
  slug: scryfall-card-symbol-structure
- name: Scryfall Catalog Structure
  property_count: 4
  slug: scryfall-catalog-structure
- name: Scryfall Migration Structure
  property_count: 8
  slug: scryfall-migration-structure
- name: Scryfall Ruling Structure
  property_count: 5
  slug: scryfall-ruling-structure
- name: Scryfall Set Structure
  property_count: 21
  slug: scryfall-set-structure
jsonld:
- class_count: 2
  name: Scryfall Context
  property_count: 5
  slug: scryfall-context
layout: provider
modified: '2026-05-29'
name: Scryfall
nav: Providers
network: true
overview: 'Scryfall publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk Data API, Cards API, Catalogs API, and 4 more. Tagged areas include Games And Comics, Magic The Gathering, Card Data, Open Data, and Free.


  The Scryfall catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scryfall''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, tooling, and 34 more developer resources.'
plans:
- name: Scryfall Plans Pricing
  plan_count: 2
  slug: scryfall-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Scryfall Rate Limits
  slug: scryfall-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scryfall API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scryfall-jsonschema-spectral-rules
- effective_rule_count: 14
  extends: []
  name: Scryfall API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 7
  slug: scryfall-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 25.0
    contract_quality: 62.2
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 59.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scryfall/refs/heads/main/screenshots/scryfall-2026-06-20T193609.png
security:
- kind: domain-security
  name: Scryfall Domain Security
  slug: scryfall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scryfall Vulnerability Disclosure
  slug: scryfall-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: scryfall
solutions:
- description: Powering thousands of fan-built deck builders, collection trackers, and tools.
  name: Community software
- description: Source of authoritative card data and imagery for podcasts, articles, and video content.
  name: Magic content creators
- description: Bulk-data exports enabling longitudinal analysis of Magic's design and economy.
  name: Researchers
tags:
- Games And Comics
- Magic The Gathering
- Card Data
- Open Data
- Free
- Community Funded
- Public APIs
use_cases:
- description: Powering search, autocomplete, and legality checks in deck-builder web and mobile apps.
  name: Deck building applications
- description: Aggregating USD / EUR / Tix prices across reprints for collection valuation.
  name: Price tracking and portfolio tools
- description: Inline card images, prices, and rulings inside team chat channels.
  name: Discord and Slack card-lookup bots
- description: MCP servers exposing card data, rulings, and search to Claude and other agents.
  name: LLM and AI agent integrations
- description: Bulk-data exports feed academic and journalistic research on Magic's design history and card economy.
  name: Research and dataset publishing
- description: Tracking newly-spoiled cards into and through release day via the Sets and Cards endpoints.
  name: Spoiler and set-release coverage
- description: High-resolution PNG and SVG art for personal-use proxies and educational content.
  name: Custom card-rendering and proxy printing
- description: Format-legality checks for Standard, Pioneer, Modern, Legacy, Vintage, Pauper, Commander, Brawl, Alchemy, and historic formats.
  name: Tournament-legality verification
website: https://scryfall.com
---
