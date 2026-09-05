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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Hasura-powered GraphQL interface to the complete PokéAPI dataset, providing flexible queries over Pokémon species, moves, abilities, items, evolutions, encounters, and game version data via a single e
  name: PokéAPI GraphQL API
  slug: pokemon-graphql-graphql
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PokeAPI/pokeapi/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/PokeAPI/pokeapi/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/PokeAPI/pokeapi/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/PokeAPI/pokeapi/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/PokeAPI/pokeapi/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/PokeAPI/pokeapi/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pokemon-graphql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pokeapi.co
- group: docs
  title: ''
  type: Documentation
  url: https://pokeapi.co/docs/graphql
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PokeAPI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PokeAPI/pokeapi
- group: company
  title: ''
  type: About
  url: https://pokeapi.co/about
- group: commercial
  title: ''
  type: Plans
  url: plans/pokemon-graphql-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pokemon-graphql-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/pokemon-graphql-finops.md
created: '2026-06-14'
description: GraphQL beta endpoint for PokéAPI providing Hasura-powered queries over the complete Pokémon database including species, moves, abilities, items, evolutions, and game version data.
graphqls:
- description: The PokéAPI GraphQL endpoint is a Hasura-powered GraphQL interface over the complete PokéAPI Pokémon database. It exposes every table in the `pokemon_v2` schema as a top-level query, supporting filter
  name: PokéAPI GraphQL API
  slug: pokemon-graphql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pokemon-graphql.png
layout: provider
modified: '2026-06-14'
name: PokéAPI GraphQL
nav: Providers
network: true
overview: 'PokéAPI GraphQL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Pokemon, Gaming, Open Data, and Hasura.


  PokéAPI GraphQL''s developer surface includes documentation and 14 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 27.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pokemon-graphql/refs/heads/main/screenshots/pokemon-graphql-2026-06-20T191846.png
security:
- kind: domain-security
  name: Pokemon Graphql Domain Security
  slug: pokemon-graphql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pokemon-graphql
tags:
- GraphQL
- Pokemon
- Gaming
- Open Data
- Hasura
- Developer Tools
website: https://pokeapi.co
---
