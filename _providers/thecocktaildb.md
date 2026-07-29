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
  name: Thecocktaildb Agentic Access
  operation_count: 5
  slug: thecocktaildb-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Free cocktail and drinks recipe database with a REST API providing drink recipes, ingredients, glass types, categories, and cocktail images. Search cocktails by name, ingredient, category, glass type,
  name: TheCocktailDB API
  slug: thecocktaildb
- description: Filter cocktails by attributes
  name: TheCocktailDB Filter API
  slug: thecocktaildb-filter-api
- description: List available categories, glasses, and ingredients
  name: TheCocktailDB List API
  slug: thecocktaildb-list-api
- description: Retrieve details by ID
  name: TheCocktailDB Lookup API
  slug: thecocktaildb-lookup-api
- description: Search for cocktails and ingredients
  name: TheCocktailDB Search API
  slug: thecocktaildb-search-api
artifact_total: 26
collections:
- collection_type: open
  name: TheCocktailDB API
  slug: open-thecocktaildb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thecocktaildb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thecocktaildb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thecocktaildb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thecocktaildb.com/api.php
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/thecocktaildb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thecocktaildb
- group: company
  title: ''
  type: Blog
  url: https://www.thecocktaildb.com/about.php
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patreon.com/thedatadb
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/thecocktaildb-status
- group: other
  title: ''
  type: X
  url: https://twitter.com/TheAudioDB
- group: commercial
  title: ''
  type: Plans
  url: plans/thecocktaildb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thecocktaildb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thecocktaildb-finops.yml
created: '2026-06-13'
description: An open, crowd-sourced database of cocktails and drinks from around the world with a free API providing drink recipes, ingredients, glass types, categories, and cocktail images.
examples:
- key_count: 1
  name: Thecocktaildb Cocktails Response Example
  slug: thecocktaildb-cocktails-response-example
- key_count: 29
  name: Thecocktaildb Drink Example
  slug: thecocktaildb-drink-example
- key_count: 1
  name: Thecocktaildb Filter Response Example
  slug: thecocktaildb-filter-response-example
- key_count: 1
  name: Thecocktaildb List Response Example
  slug: thecocktaildb-list-response-example
finops:
- name: Thecocktaildb Finops
  service_category: Recipes / Open Data
  slug: thecocktaildb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thecocktaildb.png
json_schemas:
- name: CocktailsResponse
  property_count: 1
  slug: thecocktaildb-cocktails-response
- name: Drink
  property_count: 25
  slug: thecocktaildb-drink
- name: FilterResponse
  property_count: 1
  slug: thecocktaildb-filter-response
- name: ListResponse
  property_count: 1
  slug: thecocktaildb-list-response
json_structures:
- name: Thecocktaildb Cocktails Response Structure
  property_count: 1
  slug: thecocktaildb-cocktails-response-structure
- name: Thecocktaildb Drink Structure
  property_count: 25
  slug: thecocktaildb-drink-structure
- name: Thecocktaildb Filter Response Structure
  property_count: 1
  slug: thecocktaildb-filter-response-structure
- name: Thecocktaildb List Response Structure
  property_count: 1
  slug: thecocktaildb-list-response-structure
jsonld:
- class_count: 4
  name: Thecocktaildb Context
  property_count: 26
  slug: thecocktaildb-context
layout: provider
modified: '2026-06-13'
name: TheCocktailDB
nav: Providers
network: true
overview: 'TheCocktailDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Filter API, List API, Lookup API, and 1 more. Tagged areas include Cocktails, Drinks, Recipes, Food And Beverage, and Open Data.


  The TheCocktailDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TheCocktailDB''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Thecocktaildb Plans Pricing
  plan_count: 2
  slug: thecocktaildb-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 2
  name: Thecocktaildb Rate Limits
  slug: thecocktaildb-rate-limits
rules:
- name: TheCocktailDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thecocktaildb-jsonschema-spectral-rules
- name: TheCocktailDB API Rules
  rule_count: 24
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 13
  slug: thecocktaildb-spectral-rules
score:
  band: thin
  composite: 38.0
  delta: -6.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/thecocktaildb/refs/heads/main/screenshots/thecocktaildb-2026-06-20T195244.png
security:
- kind: domain-security
  name: Thecocktaildb Domain Security
  slug: thecocktaildb-domain-security
  summary_line: TLSv1.3
slug: thecocktaildb
tags:
- Cocktails
- Drinks
- Recipes
- Food And Beverage
- Open Data
website: https://www.thecocktaildb.com/
---
