---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Themealdb Agentic Access
  operation_count: 6
  slug: themealdb-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Filter meals by attributes
  name: TheMealDB Filter API
  slug: themealdb-filter-api
- description: List available categories, areas, and ingredients
  name: TheMealDB List API
  slug: themealdb-list-api
- description: Retrieve details by ID or random meal
  name: TheMealDB Lookup API
  slug: themealdb-lookup-api
- description: Search for meals and ingredients
  name: TheMealDB Search API
  slug: themealdb-search-api
artifact_total: 39
collections:
- collection_type: open
  name: TheMealDB API
  slug: open-themealdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/themealdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/themealdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.themealdb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.themealdb.com/api.php
- group: start
  title: ''
  type: Signup
  url: https://www.themealdb.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.themealdb.com/
- group: design
  title: TheMealDB Spectral Rules
  type: SpectralRules
  url: rules/themealdb-spectral-rules.yml
- group: design
  title: TheMealDB Vocabulary
  type: Vocabulary
  url: vocabulary/themealdb-vocabulary.yml
created: '2024-11-14'
description: TheMealDB is a comprehensive online platform offering a vast collection of recipes from around the world with a free API. The API and site will always remain free at point of access.
examples:
- key_count: 1
  name: Themealdb Categories Response Example
  slug: themealdb-categories-response-example
- key_count: 4
  name: Themealdb Category Example
  slug: themealdb-category-example
- key_count: 1
  name: Themealdb Filter Response Example
  slug: themealdb-filter-response-example
- key_count: 1
  name: Themealdb List Response Example
  slug: themealdb-list-response-example
- key_count: 16
  name: Themealdb Meal Example
  slug: themealdb-meal-example
- key_count: 1
  name: Themealdb Meals Response Example
  slug: themealdb-meals-response-example
features:
- 'TheMealDB: free public API'
- Free public meal recipe API. Patreon supporters get premium API key with no rate limits.
- 'Public URL: https://www.themealdb.com/'
finops:
- name: Themealdb Finops
  service_category: Recipes / Open Data
  slug: themealdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/themealdb.png
integrations:
- description: Sister site providing cocktail recipes from the same provider
  name: TheCocktailDB
json_schemas:
- name: CategoriesResponse
  property_count: 1
  slug: themealdb-categories-response
- name: Category
  property_count: 4
  slug: themealdb-category
- name: FilterResponse
  property_count: 1
  slug: themealdb-filter-response
- name: ListResponse
  property_count: 1
  slug: themealdb-list-response
- name: Meal
  property_count: 16
  slug: themealdb-meal
- name: MealsResponse
  property_count: 1
  slug: themealdb-meals-response
json_structures:
- name: Themealdb Categories Response Structure
  property_count: 1
  slug: themealdb-categories-response-structure
- name: Themealdb Category Structure
  property_count: 4
  slug: themealdb-category-structure
- name: Themealdb Filter Response Structure
  property_count: 1
  slug: themealdb-filter-response-structure
- name: Themealdb List Response Structure
  property_count: 1
  slug: themealdb-list-response-structure
- name: Themealdb Meal Structure
  property_count: 16
  slug: themealdb-meal-structure
- name: Themealdb Meals Response Structure
  property_count: 1
  slug: themealdb-meals-response-structure
jsonld:
- class_count: 6
  name: Themealdb Context
  property_count: 21
  slug: themealdb-context
layout: provider
modified: '2026-05-19'
name: TheMealDB
nav: Providers
network: true
overview: 'TheMealDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Filter API, List API, Lookup API, and 1 more. Tagged areas include Recipes, Meals, Food, and Cooking.


  The TheMealDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TheMealDB''s developer surface includes documentation, signup flow, pricing, and 5 more developer resources.'
plans:
- name: Themealdb Plans Pricing
  plan_count: 1
  slug: themealdb-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Themealdb Rate Limits
  slug: themealdb-rate-limits
rules:
- name: TheMealDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: themealdb-jsonschema-spectral-rules
- name: TheMealDB API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 12
  slug: themealdb-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: 4.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.3
    developer_ergonomics: 8.7
    discoverability: 75.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 42.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/themealdb/refs/heads/main/screenshots/themealdb-2026-06-20T195246.png
security:
- kind: domain-security
  name: Themealdb Domain Security
  slug: themealdb-domain-security
  summary_line: TLSv1.3 · HSTS
slug: themealdb
tags:
- Recipes
- Meals
- Food
- Cooking
use_cases:
- description: Build meal recipe apps and cooking websites
  name: Recipe App Development
- description: Plan weekly meals by category, region, or available ingredients
  name: Meal Planning
- description: Power AI agents that suggest meals and cooking ideas
  name: AI Cooking Assistant
- description: Find meals filtered by ingredients, cuisine, or category
  name: Dietary Filtering
website: https://www.themealdb.com/
---
