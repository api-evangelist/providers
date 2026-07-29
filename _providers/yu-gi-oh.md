---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Yu Gi Oh Agentic Access
  operation_count: 7
  slug: yu-gi-oh-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: Recognised Yu-Gi-Oh! archetype catalog.
  name: YGOPRODeck Archetypes API
  slug: yu-gi-oh-archetypes-api
- description: Yu-Gi-Oh! card set catalog and per-print details.
  name: YGOPRODeck Card Sets API
  slug: yu-gi-oh-card-sets-api
- description: Card search, filtering, and metadata retrieval.
  name: YGOPRODeck Cards API
  slug: yu-gi-oh-cards-api
- description: Database version and freshness information.
  name: YGOPRODeck Database API
  slug: yu-gi-oh-database-api
- description: Valid value enumerations used by the search engine.
  name: YGOPRODeck Reference Data API
  slug: yu-gi-oh-reference-data-api
artifact_total: 56
collections:
- collection_type: open
  name: YGOPRODeck Yu-Gi-Oh! Card Database API
  slug: open-yu-gi-oh-ygoprodeck
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yu-gi-oh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yu-gi-oh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ygoprodeck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ygoprodeck.com/api-guide/
- group: docs
  title: Supplemental API Guide
  type: Documentation
  url: https://ygoprodeck.com/api-guide-supplemental/
- group: commercial
  title: YGOPRODeck Premium (supports the free API)
  type: Pricing
  url: https://ygoprodeck.com/premium/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: docs
  title: magicDGS-gaming/ygoprodeck-openapi
  type: ThirdPartyOpenAPI
  url: https://github.com/magicDGS-gaming/ygoprodeck-openapi
- group: operate
  title: 20 Requests per Second per IP (1 hour ban on violation)
  type: RateLimits
  url: https://ygoprodeck.com/api-guide/
- group: build
  title: Draw Yu-Gi-Oh! Card GitHub Action
  type: Tools
  url: https://github.com/Doarakko/draw-action
- group: build
  title: YGO Bubble Tea CLI
  type: Tools
  url: https://github.com/Morphclue/ygo-bubble-tea
- group: build
  title: YGOPRODeckArchive (.NET archiver)
  type: Tools
  url: https://github.com/BillyCool/YGOPRODeckArchive
- group: build
  title: MCP Server (alisyedn/yugioh-mcp-server)
  type: Tools
  url: https://github.com/alisyedn/yugioh-mcp-server
- group: build
  title: MCP Server (ludoplex/yugioh-mcp-server - PSCT + ruling engine)
  type: Tools
  url: https://github.com/ludoplex/yugioh-mcp-server
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/yu-gi-oh-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/yu-gi-oh-ygoprodeck-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/yu-gi-oh-rules.yml
created: '2026-05-28'
description: YGOPRODeck is a community-run Yu-Gi-Oh! TCG database and deck-sharing platform that exposes a free, public REST API (v7) for querying every Yu-Gi-Oh! card, archetype, card set, banlist status, format legality, market price, and card image. The API is the canonical open data source used by community deck builders, mobile apps, Discord bots, simulators, and analytics tools across the Yu-Gi-Oh! ecosystem.
examples:
- key_count: 1
  name: Ygoprodeck Api Archetype Example
  slug: ygoprodeck-api-archetype-example
- key_count: 2
  name: Ygoprodeck Api Card Class Values Example
  slug: ygoprodeck-api-card-class-values-example
- key_count: 21
  name: Ygoprodeck Api Card Example
  slug: ygoprodeck-api-card-example
- key_count: 4
  name: Ygoprodeck Api Card Image Example
  slug: ygoprodeck-api-card-image-example
- key_count: 16
  name: Ygoprodeck Api Card Misc Info Example
  slug: ygoprodeck-api-card-misc-info-example
- key_count: 5
  name: Ygoprodeck Api Card Price Example
  slug: ygoprodeck-api-card-price-example
- key_count: 5
  name: Ygoprodeck Api Card Printing Entry Example
  slug: ygoprodeck-api-card-printing-entry-example
- key_count: 2
  name: Ygoprodeck Api Card Search Response Example
  slug: ygoprodeck-api-card-search-response-example
- key_count: 5
  name: Ygoprodeck Api Card Set Example
  slug: ygoprodeck-api-card-set-example
- key_count: 6
  name: Ygoprodeck Api Card Set Print Example
  slug: ygoprodeck-api-card-set-print-example
- key_count: 4
  name: Ygoprodeck Api Card Type Entry Example
  slug: ygoprodeck-api-card-type-entry-example
- key_count: 5
  name: Ygoprodeck Api Card Values Example
  slug: ygoprodeck-api-card-values-example
- key_count: 2
  name: Ygoprodeck Api Database Version Example
  slug: ygoprodeck-api-database-version-example
- key_count: 5
  name: Ygoprodeck Api Monster Values Example
  slug: ygoprodeck-api-monster-values-example
- key_count: 7
  name: Ygoprodeck Api Search Meta Example
  slug: ygoprodeck-api-search-meta-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yu-gi-oh.png
json_schemas:
- name: Archetype
  property_count: 1
  slug: ygoprodeck-api-archetype
- name: CardClassValues
  property_count: 2
  slug: ygoprodeck-api-card-class-values
- name: CardImage
  property_count: 4
  slug: ygoprodeck-api-card-image
- name: CardMiscInfo
  property_count: 16
  slug: ygoprodeck-api-card-misc-info
- name: CardPrice
  property_count: 5
  slug: ygoprodeck-api-card-price
- name: CardPrintingEntry
  property_count: 5
  slug: ygoprodeck-api-card-printing-entry
- name: Card
  property_count: 21
  slug: ygoprodeck-api-card
- name: CardSearchResponse
  property_count: 2
  slug: ygoprodeck-api-card-search-response
- name: CardSetPrint
  property_count: 6
  slug: ygoprodeck-api-card-set-print
- name: CardSet
  property_count: 5
  slug: ygoprodeck-api-card-set
- name: CardTypeEntry
  property_count: 4
  slug: ygoprodeck-api-card-type-entry
- name: CardValues
  property_count: 5
  slug: ygoprodeck-api-card-values
- name: DatabaseVersion
  property_count: 2
  slug: ygoprodeck-api-database-version
- name: MonsterValues
  property_count: 5
  slug: ygoprodeck-api-monster-values
- name: SearchMeta
  property_count: 7
  slug: ygoprodeck-api-search-meta
json_structures:
- name: Ygoprodeck Api Archetype Structure
  property_count: 1
  slug: ygoprodeck-api-archetype-structure
- name: Ygoprodeck Api Card Class Values Structure
  property_count: 2
  slug: ygoprodeck-api-card-class-values-structure
- name: Ygoprodeck Api Card Image Structure
  property_count: 4
  slug: ygoprodeck-api-card-image-structure
- name: Ygoprodeck Api Card Misc Info Structure
  property_count: 16
  slug: ygoprodeck-api-card-misc-info-structure
- name: Ygoprodeck Api Card Price Structure
  property_count: 5
  slug: ygoprodeck-api-card-price-structure
- name: Ygoprodeck Api Card Printing Entry Structure
  property_count: 5
  slug: ygoprodeck-api-card-printing-entry-structure
- name: Ygoprodeck Api Card Search Response Structure
  property_count: 2
  slug: ygoprodeck-api-card-search-response-structure
- name: Ygoprodeck Api Card Set Print Structure
  property_count: 6
  slug: ygoprodeck-api-card-set-print-structure
- name: Ygoprodeck Api Card Set Structure
  property_count: 5
  slug: ygoprodeck-api-card-set-structure
- name: Ygoprodeck Api Card Structure
  property_count: 21
  slug: ygoprodeck-api-card-structure
- name: Ygoprodeck Api Card Type Entry Structure
  property_count: 4
  slug: ygoprodeck-api-card-type-entry-structure
- name: Ygoprodeck Api Card Values Structure
  property_count: 5
  slug: ygoprodeck-api-card-values-structure
- name: Ygoprodeck Api Database Version Structure
  property_count: 2
  slug: ygoprodeck-api-database-version-structure
- name: Ygoprodeck Api Monster Values Structure
  property_count: 5
  slug: ygoprodeck-api-monster-values-structure
- name: Ygoprodeck Api Search Meta Structure
  property_count: 7
  slug: ygoprodeck-api-search-meta-structure
jsonld:
- class_count: 15
  name: Yu Gi Oh Ygoprodeck Context
  property_count: 73
  slug: yu-gi-oh-ygoprodeck-context
layout: provider
modified: '2026-05-30'
name: YGOPRODeck
nav: Providers
network: true
overview: 'YGOPRODeck publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Archetypes API, Card Sets API, Cards API, and 2 more. Tagged areas include Games, Trading Card Games, Yu Gi Oh, Card Database, and Open Data.


  The YGOPRODeck catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  YGOPRODeck''s developer surface includes documentation, pricing, tooling, and 14 more developer resources.'
random_paper: 58
rules:
- name: YGOPRODeck API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: yu-gi-oh-jsonschema-spectral-rules
- name: YGOPRODeck API Rules
  rule_count: 43
  severity_counts:
    error: 20
    hint: 0
    info: 7
    warn: 16
  slug: yu-gi-oh-rules
score:
  band: thin
  composite: 31.4
  delta: -6.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 52.2
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/yu-gi-oh/refs/heads/main/screenshots/yu-gi-oh-2026-06-20T201751.png
security:
- kind: domain-security
  name: Yu Gi Oh Domain Security
  slug: yu-gi-oh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yu-gi-oh
tags:
- Games
- Trading Card Games
- Yu Gi Oh
- Card Database
- Open Data
- Community API
- Public APIs
website: https://ygoprodeck.com/
---
