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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pokemon Tcg Agentic Access
  operation_count: 8
  slug: pokemon-tcg-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.pokemontcg.io/v2
  baseurl_source: declared
  description: Individual Pokémon, Trainer, and Energy cards with full gameplay data, images, legalities, and market prices.
  name: Pokémon TCG API Cards API
  slug: pokemon-tcg-cards-api
- baseURL: https://api.pokemontcg.io/v2
  baseurl_source: declared
  description: The controlled vocabularies used across cards - energy types, card subtypes, supertypes, and rarities.
  name: Pokémon TCG API Metadata API
  slug: pokemon-tcg-metadata-api
- baseURL: https://api.pokemontcg.io/v2
  baseurl_source: declared
  description: Trading card game sets (expansions), from Base Set onward.
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
random_paper: 11
rate_limits:
- limit_count: 5
  name: Pokemon Tcg Rate Limits
  slug: pokemon-tcg-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.6
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pokemon-tcg/refs/heads/main/screenshots/pokemon-tcg-2026-09-02T151635.png
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
