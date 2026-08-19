---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pokemon Tcg Agentic Access
  operation_count: 8
  slug: pokemon-tcg-agentic-access
  summary_line: 8 operations
api_count: 3
apis:
- description: Individual Pokémon, Trainer, and Energy cards with full gameplay data, images, legalities, and market prices.
  name: Pokémon TCG API Cards API
  slug: pokemon-tcg-cards-api
- description: The controlled vocabularies used across cards - energy types, card subtypes, supertypes, and rarities.
  name: Pokémon TCG API Metadata API
  slug: pokemon-tcg-metadata-api
- description: Trading card game sets (expansions), from Base Set onward.
  name: Pokémon TCG API Sets API
  slug: pokemon-tcg-sets-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pokémon TCG Cards API
  slug: open-pokemon-tcg-cards-api
- collection_type: open
  name: Pokémon TCG Cards Metadata API
  slug: open-pokemon-tcg-metadata-api
- collection_type: open
  name: Pokémon TCG Cards Sets API
  slug: open-pokemon-tcg-sets-api
- collection_type: open
  name: Pokémon TCG API
  slug: open-pokemon-tcg
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pokemon-tcg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pokemon-tcg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pokemon-tcg-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pokemontcg.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pokemontcg.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PokemonTCG
- group: start
  title: ''
  type: PortalSignup
  url: https://dev.pokemontcg.io
- group: build
  title: ''
  type: SDKs
  url: https://docs.pokemontcg.io/sdks/overview
- group: docs
  title: ''
  type: RateLimitsDocumentation
  url: https://docs.pokemontcg.io/getting-started/rate-limits
- group: auth
  title: ''
  type: Authentication
  url: https://docs.pokemontcg.io/getting-started/authentication
- group: design
  title: ''
  type: Errors
  url: https://docs.pokemontcg.io/getting-started/errors
- group: commercial
  title: ''
  type: Plans
  url: plans/pokemon-tcg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pokemon-tcg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pokemon-tcg-finops.yml
created: '2026-07-11'
description: The Pokémon TCG API is a free, community-run REST API created and maintained by Andrew Backes that serves Pokémon Trading Card Game data - more than 20,000 cards across 170+ sets, from Base Set onward. Every card carries full gameplay data (attacks, abilities, weaknesses, resistances, retreat costs), format legalities, high-resolution card images, and daily-updated market prices from TCGplayer and Cardmarket. A Lucene-like query syntax supports keyword, phrase, wildcard, exact, range, and nested-field searches across every field. The API works without authentication at a reduced rate limit; a free API key from the developer portal, sent in the X-Api-Key header, raises the limits. Official SDKs cover Python, Ruby, JavaScript, TypeScript, C#, Kotlin, PHP, Go, Dart, and Elixir.
finops:
- name: Pokemon Tcg Finops
  service_category: Gaming and Entertainment Data
  slug: pokemon-tcg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pokemon-tcg.png
layout: provider
modified: '2026-07-11'
name: Pokémon TCG API
nav: Providers
network: true
overview: 'Pokémon TCG API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cards API, Metadata API, and Sets API. Tagged areas include Pokemon, Trading Cards, TCG, Gaming, and Card Games.


  Pokémon TCG API''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Pokemon Tcg Plans Pricing
  plan_count: 3
  slug: pokemon-tcg-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Pokemon Tcg Rate Limits
  slug: pokemon-tcg-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Pokemon Tcg Authentication
  slug: pokemon-tcg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pokemon Tcg Domain Security
  slug: pokemon-tcg-domain-security
  summary_line: TLSv1.3
slug: pokemon-tcg
tags:
- Pokemon
- Trading Cards
- TCG
- Gaming
- Card Games
- Collectibles
- Card Prices
website: https://pokemontcg.io
---
