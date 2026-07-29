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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hasura-powered GraphQL interface to the complete PokéAPI dataset, providing flexible queries over Pokémon species, moves, abilities, items, evolutions, encounters, and game version data via a single e
  name: PokéAPI GraphQL API
  slug: pokemon-graphql-graphql
artifact_total: 3
common:
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


  PokéAPI GraphQL''s developer surface includes documentation and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.0
  delta: 7.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.2
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
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
