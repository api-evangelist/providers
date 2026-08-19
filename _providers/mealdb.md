---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
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
    agentic_access: derived
    auth_clarity: false
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
  score: 28.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mealdb Agentic Access
  operation_count: 8
  slug: mealdb-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: The Categories.php API from TheMealDB — 1 operation(s) for categories.php.
  name: TheMealDB Categories.php API
  slug: mealdb-categories-php-api
- description: The Filter.php API from TheMealDB — 1 operation(s) for filter.php.
  name: TheMealDB Filter.php API
  slug: mealdb-filter-php-api
- description: The List.php API from TheMealDB — 1 operation(s) for list.php.
  name: TheMealDB List.php API
  slug: mealdb-list-php-api
- description: The Lookup.php API from TheMealDB — 1 operation(s) for lookup.php.
  name: TheMealDB Lookup.php API
  slug: mealdb-lookup-php-api
- description: Premium-only endpoints requiring a paid lifetime supporter API key
  name: TheMealDB Premium API
  slug: mealdb-premium-api
- description: The Random.php API from TheMealDB — 1 operation(s) for random.php.
  name: TheMealDB Random.php API
  slug: mealdb-random-php-api
- description: The Search.php API from TheMealDB — 1 operation(s) for search.php.
  name: TheMealDB Search.php API
  slug: mealdb-search-php-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TheMealDB Categories.php API
  slug: open-mealdb-categories-php-api
- collection_type: open
  name: TheMealDB Categories.php Filter.php API
  slug: open-mealdb-filter-php-api
- collection_type: open
  name: TheMealDB Categories.php List.php API
  slug: open-mealdb-list-php-api
- collection_type: open
  name: TheMealDB Categories.php Lookup.php API
  slug: open-mealdb-lookup-php-api
- collection_type: open
  name: TheMealDB Categories.php Premium API
  slug: open-mealdb-premium-api
- collection_type: open
  name: TheMealDB Categories.php Random.php API
  slug: open-mealdb-random-php-api
- collection_type: open
  name: TheMealDB Categories.php Search.php API
  slug: open-mealdb-search-php-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mealdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mealdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.themealdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.themealdb.com/api.php
- group: commercial
  title: ''
  type: Pricing
  url: https://www.themealdb.com/api.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.themealdb.com/terms_of_use.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.themealdb.com/privacy_policy.php
- group: commercial
  title: ''
  type: Plans
  url: plans/mealdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mealdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mealdb-finops.yml
- group: other
  title: ''
  type: X
  url: https://twitter.com/TheAudioDB
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TheDataDB/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/pFvgaXV
created: '2026-06-13'
description: TheMealDB is an open, crowd-sourced database of recipes from around the world offering a free REST API with 669 meals, 927 ingredients, 300+ recipes complete with ingredients, step-by-step cooking instructions, categories, area cuisines, and meal images. The API and site will always remain free at point of access; a lifetime supporter upgrade unlocks premium V2 endpoints including multi-ingredient filtering, random sets, latest meals, and the ability to add custom meals and images.
examples:
- key_count: 3
  name: Filter By Category
  slug: filter-by-category
- key_count: 3
  name: List Categories
  slug: list-categories
- key_count: 3
  name: Search Meal By Name
  slug: search-meal-by-name
finops:
- name: Mealdb Finops
  service_category: Open Data
  slug: mealdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mealdb.png
json_schemas:
- name: Category
  property_count: 4
  slug: category
- name: MealSummary
  property_count: 3
  slug: meal-summary
- name: Meal
  property_count: 53
  slug: meal
jsonld:
- class_count: 56
  name: Mealdb Context
  property_count: 2
  slug: mealdb-context
layout: provider
modified: '2026-06-13'
name: TheMealDB
nav: Providers
network: true
overview: 'TheMealDB publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Categories.php API, Filter.php API, List.php API, and 4 more. Tagged areas include Food, Recipes, Meals, Cooking, and Ingredients.


  The TheMealDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TheMealDB''s developer surface includes documentation, pricing, and 11 more developer resources.'
plans:
- name: Mealdb Plans Pricing
  plan_count: 2
  slug: mealdb-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Mealdb Rate Limits
  slug: mealdb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TheMealDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mealdb-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.7
  delta: -2.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 9.8
    contract_quality: 56.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 46.2
  provenance:
    agentic_access: derived
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
    score: 35.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mealdb/refs/heads/main/screenshots/mealdb-2026-06-20T185110.png
security:
- kind: domain-security
  name: Mealdb Domain Security
  slug: mealdb-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mealdb
tags:
- Food
- Recipes
- Meals
- Cooking
- Ingredients
- Cuisine
- Open Data
website: https://www.themealdb.com
---
