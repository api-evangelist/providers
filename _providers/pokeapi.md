---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pokeapi Agentic Access
  operation_count: 86
  slug: pokeapi-agentic-access
  summary_line: 86 operations
api_count: 12
apis:
- description: The PokéAPI GraphQL beta exposes the same Pokémon dataset as the REST API through a single endpoint with field-level selection, joins, and filtering. It is well suited to clients that want to cherry-p
  name: PokéAPI GraphQL API (Beta)
  slug: pokeapi-graphql
- description: Berries, their flavors, and firmness ratings.
  name: PokéAPI Berries API
  slug: pokeapi-berries-api
- description: Contest types, contest effects, and super-contest effects.
  name: PokéAPI Contests API
  slug: pokeapi-contests-api
- description: Encounter methods, conditions, and condition values used in the wild.
  name: PokéAPI Encounters API
  slug: pokeapi-encounters-api
- description: Evolution chains and the triggers that drive them.
  name: PokéAPI Evolution API
  slug: pokeapi-evolution-api
- description: Generations, Pokédexes, individual versions, and version groups.
  name: PokéAPI Games API
  slug: pokeapi-games-api
- description: Items, item attributes, categories, fling effects, and bag pockets.
  name: PokéAPI Items API
  slug: pokeapi-items-api
- description: Locations, location areas, Pal Park areas, and regions.
  name: PokéAPI Locations API
  slug: pokeapi-locations-api
- description: Items that teach moves to Pokémon (TMs and HMs).
  name: PokéAPI Machines API
  slug: pokeapi-machines-api
- description: Moves, ailments, battle styles, categories, damage classes, learn methods, and targets.
  name: PokéAPI Moves API
  slug: pokeapi-moves-api
- description: Pokémon, species, abilities, types, stats, natures, egg groups, growth rates, genders, characteristics, and Pokéathlon stats.
  name: PokéAPI Pokémon API
  slug: pokeapi-pok-mon-api
- description: Cross-cutting utility resources such as supported languages.
  name: PokéAPI Utility API
  slug: pokeapi-utility-api
artifact_total: 205
collections:
- collection_type: open
  name: PokéAPI
  slug: open-pokeapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pokeapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pokeapi-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://pokeapi.co
- group: start
  title: ''
  type: GettingStarted
  url: https://pokeapi.co/docs/v2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PokeAPI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PokeAPI/pokeapi
- group: commercial
  title: BSD-3-Clause
  type: License
  url: https://github.com/PokeAPI/pokeapi/blob/master/LICENSE.md
- group: commercial
  title: Open Collective (Donations)
  type: Pricing
  url: https://opencollective.com/pokeapi
- group: commercial
  title: GitHub Sponsors
  type: Pricing
  url: https://github.com/sponsors/PokeAPI
- group: company
  title: ''
  type: About
  url: https://pokeapi.co/about
- group: commercial
  title: Fair Use Policy
  type: TermsOfService
  url: https://pokeapi.co/docs/v2#fairuse
- group: operate
  title: Slack Community
  type: Support
  url: https://pokeapi.slack.com
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/pokeapi
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PokeAPI/pokeapi/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/PokeAPI/pokeapi/releases
- group: build
  title: Docker Image
  type: SDKs
  url: https://hub.docker.com/r/pokeapi/pokeapi
- group: build
  title: Pokémon Sprites (Static Assets)
  type: SDKs
  url: https://github.com/PokeAPI/sprites
- group: build
  title: Static API Data Dump + JSON Schema
  type: SDKs
  url: https://github.com/PokeAPI/api-data
- group: build
  title: ''
  type: Tools
  url: ''
- group: design
  title: PokéAPI Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/pokeapi/refs/heads/main/rules/pokeapi-rules.yml
- group: design
  title: PokéAPI Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/pokeapi/refs/heads/main/vocabulary/pokeapi-vocabulary.yaml
created: '2026-05-30'
description: PokéAPI (pokeapi.co) is a free, open-source RESTful and GraphQL API serving comprehensive Pokémon data — including Pokémon species, abilities, moves, items, types, locations, evolution chains, encounters, berries, contests, games, and machines. Built as an educational tool licensed under BSD-3-Clause, it is community-funded via Open Collective and GitHub Sponsors, requires no authentication, and is hosted with a fair-use policy encouraging clients to cache responses locally. The API powers tutorials, fan apps, machine-learning experiments, and game tooling worldwide and consistently serves one billion-plus requests per month.
examples:
- key_count: 8
  name: Pokeapi Ability Example
  slug: pokeapi-ability-example
- key_count: 1
  name: Pokeapi Api Resource Example
  slug: pokeapi-api-resource-example
- key_count: 4
  name: Pokeapi Api Resource List Example
  slug: pokeapi-api-resource-list-example
- key_count: 12
  name: Pokeapi Berry Example
  slug: pokeapi-berry-example
- key_count: 4
  name: Pokeapi Berry Firmness Example
  slug: pokeapi-berry-firmness-example
- key_count: 5
  name: Pokeapi Berry Flavor Example
  slug: pokeapi-berry-flavor-example
- key_count: 4
  name: Pokeapi Chain Link Example
  slug: pokeapi-chain-link-example
- key_count: 5
  name: Pokeapi Characteristic Example
  slug: pokeapi-characteristic-example
- key_count: 5
  name: Pokeapi Contest Effect Example
  slug: pokeapi-contest-effect-example
- key_count: 4
  name: Pokeapi Contest Type Example
  slug: pokeapi-contest-type-example
- key_count: 2
  name: Pokeapi Description Example
  slug: pokeapi-description-example
- key_count: 2
  name: Pokeapi Effect Example
  slug: pokeapi-effect-example
- key_count: 4
  name: Pokeapi Egg Group Example
  slug: pokeapi-egg-group-example
- key_count: 4
  name: Pokeapi Encounter Condition Example
  slug: pokeapi-encounter-condition-example
- key_count: 4
  name: Pokeapi Encounter Condition Value Example
  slug: pokeapi-encounter-condition-value-example
- key_count: 4
  name: Pokeapi Encounter Method Example
  slug: pokeapi-encounter-method-example
- key_count: 3
  name: Pokeapi Evolution Chain Example
  slug: pokeapi-evolution-chain-example
- key_count: 4
  name: Pokeapi Evolution Trigger Example
  slug: pokeapi-evolution-trigger-example
- key_count: 3
  name: Pokeapi Flavor Text Example
  slug: pokeapi-flavor-text-example
- key_count: 4
  name: Pokeapi Gender Example
  slug: pokeapi-gender-example
- key_count: 9
  name: Pokeapi Generation Example
  slug: pokeapi-generation-example
- key_count: 6
  name: Pokeapi Growth Rate Example
  slug: pokeapi-growth-rate-example
- key_count: 5
  name: Pokeapi Item Attribute Example
  slug: pokeapi-item-attribute-example
- key_count: 5
  name: Pokeapi Item Category Example
  slug: pokeapi-item-category-example
- key_count: 13
  name: Pokeapi Item Example
  slug: pokeapi-item-example
- key_count: 4
  name: Pokeapi Item Fling Effect Example
  slug: pokeapi-item-fling-effect-example
- key_count: 4
  name: Pokeapi Item Pocket Example
  slug: pokeapi-item-pocket-example
- key_count: 6
  name: Pokeapi Language Example
  slug: pokeapi-language-example
- key_count: 2
  name: Pokeapi Location Area Encounter Example
  slug: pokeapi-location-area-encounter-example
- key_count: 7
  name: Pokeapi Location Area Example
  slug: pokeapi-location-area-example
- key_count: 6
  name: Pokeapi Location Example
  slug: pokeapi-location-example
- key_count: 4
  name: Pokeapi Machine Example
  slug: pokeapi-machine-example
- key_count: 4
  name: Pokeapi Move Ailment Example
  slug: pokeapi-move-ailment-example
- key_count: 3
  name: Pokeapi Move Battle Style Example
  slug: pokeapi-move-battle-style-example
- key_count: 4
  name: Pokeapi Move Category Example
  slug: pokeapi-move-category-example
- key_count: 5
  name: Pokeapi Move Damage Class Example
  slug: pokeapi-move-damage-class-example
- key_count: 18
  name: Pokeapi Move Example
  slug: pokeapi-move-example
- key_count: 5
  name: Pokeapi Move Learn Method Example
  slug: pokeapi-move-learn-method-example
- key_count: 5
  name: Pokeapi Move Target Example
  slug: pokeapi-move-target-example
- key_count: 2
  name: Pokeapi Name Example
  slug: pokeapi-name-example
- key_count: 2
  name: Pokeapi Named Api Resource Example
  slug: pokeapi-named-api-resource-example
- key_count: 4
  name: Pokeapi Named Api Resource List Example
  slug: pokeapi-named-api-resource-list-example
- key_count: 7
  name: Pokeapi Nature Example
  slug: pokeapi-nature-example
- key_count: 4
  name: Pokeapi Pal Park Area Example
  slug: pokeapi-pal-park-area-example
- key_count: 4
  name: Pokeapi Pokeathlon Stat Example
  slug: pokeapi-pokeathlon-stat-example
- key_count: 8
  name: Pokeapi Pokedex Example
  slug: pokeapi-pokedex-example
- key_count: 17
  name: Pokeapi Pokemon Example
  slug: pokeapi-pokemon-example
- key_count: 23
  name: Pokeapi Pokemon Species Example
  slug: pokeapi-pokemon-species-example
- key_count: 7
  name: Pokeapi Region Example
  slug: pokeapi-region-example
- key_count: 9
  name: Pokeapi Stat Example
  slug: pokeapi-stat-example
- key_count: 4
  name: Pokeapi Super Contest Effect Example
  slug: pokeapi-super-contest-effect-example
- key_count: 10
  name: Pokeapi Type Example
  slug: pokeapi-type-example
- key_count: 4
  name: Pokeapi Version Example
  slug: pokeapi-version-example
- key_count: 8
  name: Pokeapi Version Group Example
  slug: pokeapi-version-group-example
features:
- description: All endpoints are publicly accessible without API keys, tokens, or signup.
  name: No Authentication
- description: Choose REST under /api/v2 or GraphQL at beta.pokeapi.co/graphql/v1beta — same dataset, two access patterns.
  name: REST and GraphQL Interfaces
- description: Roughly 60 endpoints covering Pokémon, species, moves, abilities, items, berries, types, locations, encounters, evolution chains, contests, games, and machines.
  name: Comprehensive Pokémon Dataset
- description: Data spans every released generation of Pokémon games with version-specific and version-group-specific resource variants.
  name: Multi-Generation Coverage
- description: Names, flavor text, and descriptions are returned in multiple languages selectable via the Language utility resource.
  name: Multi-Language Localization
- description: Resources are immutable game data — responses are highly cacheable, and the fair-use policy actively encourages clients to cache locally.
  name: Cacheable Resources
- description: Companion sprites repo (PokeAPI/sprites) provides every official artwork, sprite, and shiny variant referenced by the REST responses.
  name: Pokémon Sprites Library
- description: PokeAPI/api-data publishes a static JSON snapshot of every resource for offline / build-time use cases.
  name: Static Data Dump
- description: Docker image, Kubernetes Kustomize manifests, and Firebase deployment scripts let teams run a private mirror.
  name: Self-Hostable
- description: Source code, sprites, GraphQL schema, and client wrappers are open source.
  name: Open Source (BSD-3-Clause)
graphqls:
- description: The PokéAPI GraphQL beta exposes the same Pokémon dataset as the REST API through a single endpoint with field-level selection, joins, and filtering. It is well suited to clients that want to cherry-p
  name: PokéAPI GraphQL API
  slug: pokeapi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pokeapi.png
integrations:
- description: Browser-friendly async JavaScript wrapper with built-in cache.
  name: pokeapi-js-wrapper
- description: Node.js / TypeScript promise-based client.
  name: pokedex-promise-v2
- description: Python 3 wrapper covering all v2 endpoints.
  name: pokebase
- description: Alternative Python wrapper for PokéAPI.
  name: pokepy
- description: Kotlin Multiplatform client for PokéAPI.
  name: pokekotlin
- description: Companion repo of sprite images served alongside REST responses.
  name: PokeAPI Sprites
- description: GitHub-hosted JSON snapshot for offline / build-time consumption.
  name: Static API Data Dump
- description: Numerous community MCP servers wrap PokéAPI as agent tools (poke-mcp, pokeapi-mcp-server, MCP_Pokemon, pokedex-mcp, etc.).
  name: Model Context Protocol Servers
json_schemas:
- name: Ability
  property_count: 8
  slug: pokeapi-ability
- name: APIResourceList
  property_count: 4
  slug: pokeapi-api-resource-list
- name: APIResource
  property_count: 1
  slug: pokeapi-api-resource
- name: BerryFirmness
  property_count: 4
  slug: pokeapi-berry-firmness
- name: BerryFlavor
  property_count: 5
  slug: pokeapi-berry-flavor
- name: Berry
  property_count: 12
  slug: pokeapi-berry
- name: ChainLink
  property_count: 4
  slug: pokeapi-chain-link
- name: Characteristic
  property_count: 5
  slug: pokeapi-characteristic
- name: ContestEffect
  property_count: 5
  slug: pokeapi-contest-effect
- name: ContestType
  property_count: 4
  slug: pokeapi-contest-type
- name: Description
  property_count: 2
  slug: pokeapi-description
- name: Effect
  property_count: 2
  slug: pokeapi-effect
- name: EggGroup
  property_count: 4
  slug: pokeapi-egg-group
- name: EncounterCondition
  property_count: 4
  slug: pokeapi-encounter-condition
- name: EncounterConditionValue
  property_count: 4
  slug: pokeapi-encounter-condition-value
- name: EncounterMethod
  property_count: 4
  slug: pokeapi-encounter-method
- name: EvolutionChain
  property_count: 3
  slug: pokeapi-evolution-chain
- name: EvolutionTrigger
  property_count: 4
  slug: pokeapi-evolution-trigger
- name: FlavorText
  property_count: 3
  slug: pokeapi-flavor-text
- name: Gender
  property_count: 4
  slug: pokeapi-gender
- name: Generation
  property_count: 9
  slug: pokeapi-generation
- name: GrowthRate
  property_count: 6
  slug: pokeapi-growth-rate
- name: ItemAttribute
  property_count: 5
  slug: pokeapi-item-attribute
- name: ItemCategory
  property_count: 5
  slug: pokeapi-item-category
- name: ItemFlingEffect
  property_count: 4
  slug: pokeapi-item-fling-effect
- name: ItemPocket
  property_count: 4
  slug: pokeapi-item-pocket
- name: Item
  property_count: 13
  slug: pokeapi-item
- name: Language
  property_count: 6
  slug: pokeapi-language
- name: LocationAreaEncounter
  property_count: 2
  slug: pokeapi-location-area-encounter
- name: LocationArea
  property_count: 7
  slug: pokeapi-location-area
- name: Location
  property_count: 6
  slug: pokeapi-location
- name: Machine
  property_count: 4
  slug: pokeapi-machine
- name: MoveAilment
  property_count: 4
  slug: pokeapi-move-ailment
- name: MoveBattleStyle
  property_count: 3
  slug: pokeapi-move-battle-style
- name: MoveCategory
  property_count: 4
  slug: pokeapi-move-category
- name: MoveDamageClass
  property_count: 5
  slug: pokeapi-move-damage-class
- name: MoveLearnMethod
  property_count: 5
  slug: pokeapi-move-learn-method
- name: Move
  property_count: 18
  slug: pokeapi-move
- name: MoveTarget
  property_count: 5
  slug: pokeapi-move-target
- name: Name
  property_count: 2
  slug: pokeapi-name
- name: NamedAPIResourceList
  property_count: 4
  slug: pokeapi-named-api-resource-list
- name: NamedAPIResource
  property_count: 2
  slug: pokeapi-named-api-resource
- name: Nature
  property_count: 7
  slug: pokeapi-nature
- name: PalParkArea
  property_count: 4
  slug: pokeapi-pal-park-area
- name: PokeathlonStat
  property_count: 4
  slug: pokeapi-pokeathlon-stat
- name: Pokedex
  property_count: 8
  slug: pokeapi-pokedex
- name: Pokemon
  property_count: 17
  slug: pokeapi-pokemon
- name: PokemonSpecies
  property_count: 23
  slug: pokeapi-pokemon-species
- name: Region
  property_count: 7
  slug: pokeapi-region
- name: Stat
  property_count: 9
  slug: pokeapi-stat
- name: SuperContestEffect
  property_count: 4
  slug: pokeapi-super-contest-effect
- name: Type
  property_count: 10
  slug: pokeapi-type
- name: VersionGroup
  property_count: 8
  slug: pokeapi-version-group
- name: Version
  property_count: 4
  slug: pokeapi-version
json_structures:
- name: Pokeapi Ability Structure
  property_count: 8
  slug: pokeapi-ability-structure
- name: Pokeapi Api Resource List Structure
  property_count: 4
  slug: pokeapi-api-resource-list-structure
- name: Pokeapi Api Resource Structure
  property_count: 1
  slug: pokeapi-api-resource-structure
- name: Pokeapi Berry Firmness Structure
  property_count: 4
  slug: pokeapi-berry-firmness-structure
- name: Pokeapi Berry Flavor Structure
  property_count: 5
  slug: pokeapi-berry-flavor-structure
- name: Pokeapi Berry Structure
  property_count: 12
  slug: pokeapi-berry-structure
- name: Pokeapi Chain Link Structure
  property_count: 4
  slug: pokeapi-chain-link-structure
- name: Pokeapi Characteristic Structure
  property_count: 5
  slug: pokeapi-characteristic-structure
- name: Pokeapi Contest Effect Structure
  property_count: 5
  slug: pokeapi-contest-effect-structure
- name: Pokeapi Contest Type Structure
  property_count: 4
  slug: pokeapi-contest-type-structure
- name: Pokeapi Description Structure
  property_count: 2
  slug: pokeapi-description-structure
- name: Pokeapi Effect Structure
  property_count: 2
  slug: pokeapi-effect-structure
- name: Pokeapi Egg Group Structure
  property_count: 4
  slug: pokeapi-egg-group-structure
- name: Pokeapi Encounter Condition Structure
  property_count: 4
  slug: pokeapi-encounter-condition-structure
- name: Pokeapi Encounter Condition Value Structure
  property_count: 4
  slug: pokeapi-encounter-condition-value-structure
- name: Pokeapi Encounter Method Structure
  property_count: 4
  slug: pokeapi-encounter-method-structure
- name: Pokeapi Evolution Chain Structure
  property_count: 3
  slug: pokeapi-evolution-chain-structure
- name: Pokeapi Evolution Trigger Structure
  property_count: 4
  slug: pokeapi-evolution-trigger-structure
- name: Pokeapi Flavor Text Structure
  property_count: 3
  slug: pokeapi-flavor-text-structure
- name: Pokeapi Gender Structure
  property_count: 4
  slug: pokeapi-gender-structure
- name: Pokeapi Generation Structure
  property_count: 9
  slug: pokeapi-generation-structure
- name: Pokeapi Growth Rate Structure
  property_count: 6
  slug: pokeapi-growth-rate-structure
- name: Pokeapi Item Attribute Structure
  property_count: 5
  slug: pokeapi-item-attribute-structure
- name: Pokeapi Item Category Structure
  property_count: 5
  slug: pokeapi-item-category-structure
- name: Pokeapi Item Fling Effect Structure
  property_count: 4
  slug: pokeapi-item-fling-effect-structure
- name: Pokeapi Item Pocket Structure
  property_count: 4
  slug: pokeapi-item-pocket-structure
- name: Pokeapi Item Structure
  property_count: 13
  slug: pokeapi-item-structure
- name: Pokeapi Language Structure
  property_count: 6
  slug: pokeapi-language-structure
- name: Pokeapi Location Area Encounter Structure
  property_count: 2
  slug: pokeapi-location-area-encounter-structure
- name: Pokeapi Location Area Structure
  property_count: 7
  slug: pokeapi-location-area-structure
- name: Pokeapi Location Structure
  property_count: 6
  slug: pokeapi-location-structure
- name: Pokeapi Machine Structure
  property_count: 4
  slug: pokeapi-machine-structure
- name: Pokeapi Move Ailment Structure
  property_count: 4
  slug: pokeapi-move-ailment-structure
- name: Pokeapi Move Battle Style Structure
  property_count: 3
  slug: pokeapi-move-battle-style-structure
- name: Pokeapi Move Category Structure
  property_count: 4
  slug: pokeapi-move-category-structure
- name: Pokeapi Move Damage Class Structure
  property_count: 5
  slug: pokeapi-move-damage-class-structure
- name: Pokeapi Move Learn Method Structure
  property_count: 5
  slug: pokeapi-move-learn-method-structure
- name: Pokeapi Move Structure
  property_count: 18
  slug: pokeapi-move-structure
- name: Pokeapi Move Target Structure
  property_count: 5
  slug: pokeapi-move-target-structure
- name: Pokeapi Name Structure
  property_count: 2
  slug: pokeapi-name-structure
- name: Pokeapi Named Api Resource List Structure
  property_count: 4
  slug: pokeapi-named-api-resource-list-structure
- name: Pokeapi Named Api Resource Structure
  property_count: 2
  slug: pokeapi-named-api-resource-structure
- name: Pokeapi Nature Structure
  property_count: 7
  slug: pokeapi-nature-structure
- name: Pokeapi Pal Park Area Structure
  property_count: 4
  slug: pokeapi-pal-park-area-structure
- name: Pokeapi Pokeathlon Stat Structure
  property_count: 4
  slug: pokeapi-pokeathlon-stat-structure
- name: Pokeapi Pokedex Structure
  property_count: 8
  slug: pokeapi-pokedex-structure
- name: Pokeapi Pokemon Species Structure
  property_count: 23
  slug: pokeapi-pokemon-species-structure
- name: Pokeapi Pokemon Structure
  property_count: 17
  slug: pokeapi-pokemon-structure
- name: Pokeapi Region Structure
  property_count: 7
  slug: pokeapi-region-structure
- name: Pokeapi Stat Structure
  property_count: 9
  slug: pokeapi-stat-structure
- name: Pokeapi Super Contest Effect Structure
  property_count: 4
  slug: pokeapi-super-contest-effect-structure
- name: Pokeapi Type Structure
  property_count: 10
  slug: pokeapi-type-structure
- name: Pokeapi Version Group Structure
  property_count: 8
  slug: pokeapi-version-group-structure
- name: Pokeapi Version Structure
  property_count: 4
  slug: pokeapi-version-structure
jsonld:
- class_count: 54
  name: Pokeapi Context
  property_count: 133
  slug: pokeapi-context
layout: provider
modified: '2026-05-30'
name: PokéAPI
nav: Providers
network: true
overview: 'PokéAPI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Berries API, Contests API, Encounters API, and 8 more. Tagged areas include Pokémon, Open Source, Open Data, REST, and GraphQL.


  The PokéAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  PokéAPI''s developer surface includes developer portal, getting-started guide, pricing, support, Stack Overflow tag, changelog, tooling, and 13 more developer resources.'
random_paper: 49
rules:
- name: PokéAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pokeapi-jsonschema-spectral-rules
- name: PokéAPI API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 8
    warn: 11
  slug: pokeapi-rules
score:
  band: developing
  composite: 43.4
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 62.7
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pokeapi/refs/heads/main/screenshots/pokeapi-2026-06-20T191844.png
security:
- kind: domain-security
  name: Pokeapi Domain Security
  slug: pokeapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pokeapi
tags:
- Pokémon
- Open Source
- Open Data
- REST
- GraphQL
- Gaming
- Educational
- Community
use_cases:
- description: Build mobile, web, or desktop Pokédex applications that render species, abilities, moves, and sprites.
  name: Pokédex Apps
- description: Power competitive team-builder, damage-calculator, and battle-simulator tools with type matchups, base stats, and movesets.
  name: Team Builders and Battle Simulators
- description: PokéAPI is widely used in tutorials teaching REST, GraphQL, caching, pagination, and client-side data binding.
  name: Educational Coding Tutorials
- description: Researchers use the static dataset to train and benchmark recommendation, embedding, and image-classification models on Pokémon entities.
  name: Machine Learning Datasets
- description: A favorite first example for MCP servers, agent demos, and tool-use tutorials — the data is rich, recognizable, and unauthenticated.
  name: AI Assistant Demos
- description: Provide reference data for fan-built wikis, trading marketplaces, and card-collection trackers.
  name: Fan Wikis and Trading Apps
website: https://pokeapi.co
---
