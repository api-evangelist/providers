---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Spoonacular Agentic Access
  operation_count: 99
  slug: spoonacular-agentic-access
  summary_line: 99 operations · 24 acting
api_count: 7
apis:
- description: The Ingredients API from Spoonacular — 9 operation(s) for ingredients.
  name: Spoonacular Ingredients API
  slug: spoonacular-ingredients-api
- description: The Meal Planning API from Spoonacular — 12 operation(s) for meal planning.
  name: Spoonacular Meal Planning API
  slug: spoonacular-meal-planning-api
- description: The Menu Items API from Spoonacular — 8 operation(s) for menu items.
  name: Spoonacular Menu Items API
  slug: spoonacular-menu-items-api
- description: The Misc API from Spoonacular — 11 operation(s) for misc.
  name: Spoonacular Misc API
  slug: spoonacular-misc-api
- description: The Products API from Spoonacular — 11 operation(s) for products.
  name: Spoonacular Products API
  slug: spoonacular-products-api
- description: The Recipes API from Spoonacular — 42 operation(s) for recipes.
  name: Spoonacular Recipes API
  slug: spoonacular-recipes-api
- description: The Wine API from Spoonacular — 4 operation(s) for wine.
  name: Spoonacular Wine API
  slug: spoonacular-wine-api
artifact_total: 63
collections:
- collection_type: postman
  name: spoonacular Ingredients API
  slug: postman-spoonacular-ingredients-api
- collection_type: postman
  name: spoonacular Ingredients Meal Planning API
  slug: postman-spoonacular-meal-planning-api
- collection_type: postman
  name: spoonacular Ingredients Menu Items API
  slug: postman-spoonacular-menu-items-api
- collection_type: postman
  name: spoonacular Ingredients Misc API
  slug: postman-spoonacular-misc-api
- collection_type: postman
  name: spoonacular Ingredients Products API
  slug: postman-spoonacular-products-api
- collection_type: postman
  name: spoonacular Ingredients Recipes API
  slug: postman-spoonacular-recipes-api
- collection_type: postman
  name: spoonacular Ingredients Wine API
  slug: postman-spoonacular-wine-api
- collection_type: open
  name: spoonacular API
  slug: open-spoonacular
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spoonacular/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spoonacular-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spoonacular-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spoonacular-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spoonacular.com/food-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://spoonacular.com/food-api
- group: company
  title: ''
  type: Blog
  url: https://spoonacular.com/blog/feed/
- group: start
  title: ''
  type: Console
  url: https://spoonacular.com/food-api/console
- group: start
  title: ''
  type: Signup
  url: https://spoonacular.com/food-api/console#Dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://spoonacular.com/food-api/pricing
- group: build
  title: API Clients (22 languages)
  type: SDKs
  url: https://spoonacular.com/food-api/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ddsky
- group: build
  title: API Clients
  type: GitHubRepository
  url: https://github.com/ddsky/spoonacular-api-clients
- group: learn
  title: ''
  type: Tutorials
  url: https://github.com/ddsky/spoonacular-api-tutorials
- group: build
  title: Widgets
  type: CodeExamples
  url: https://github.com/ddsky/spoonacular-widgets
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/ddsky/spoonacular-mcp
- group: build
  title: MCP Server (npm)
  type: Tools
  url: https://www.npmjs.com/package/spoonacular-mcp
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/spoonacular-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spoonacular-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spoonacular-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/spoonacular-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spoonacular-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spoonacular-finops.yml
created: '2026-05-28'
description: The Spoonacular Recipe and Food API provides programmatic access to thousands of recipes, thousands of ingredients, 800,000+ food products, and 100,000+ menu items, plus nutrition analysis, meal planning, wine pairing, and food classification. Authentication is via an API key sent in the x-api-key header.
examples:
- key_count: 4
  name: Spoonacular Comparable Product Example
  slug: spoonacular-comparable-product-example
- key_count: 3
  name: Spoonacular Ingredient Basics Example
  slug: spoonacular-ingredient-basics-example
- key_count: 17
  name: Spoonacular Ingredient Information Example
  slug: spoonacular-ingredient-information-example
- key_count: 12
  name: Spoonacular Menu Item Example
  slug: spoonacular-menu-item-example
- key_count: 24
  name: Spoonacular Product Information Example
  slug: spoonacular-product-information-example
- key_count: 35
  name: Spoonacular Recipe Information Example
  slug: spoonacular-recipe-information-example
- key_count: 8
  name: Spoonacular Search Result Example
  slug: spoonacular-search-result-example
- key_count: 7
  name: Spoonacular Taste Information Example
  slug: spoonacular-taste-information-example
features:
- description: Complex multi-filter search, search by ingredients or nutrients, full recipe information, similar/random recipes, autocomplete, and analyzed instructions.
  name: Recipe Search and Information
- description: Compute and visualize nutrition for recipes, ingredients, products, and menu items including macro- and micronutrient breakdowns.
  name: Nutrition Analysis
- description: Search ingredients, get information and substitutes, parse ingredient strings, compute conversions, and look up glycemic load.
  name: Ingredient Intelligence
- description: Search 800,000+ packaged food products by name or UPC, retrieve product information, compare products, and classify them.
  name: Grocery Products
- description: Search and retrieve 100,000+ restaurant menu items with nutrition and autocomplete.
  name: Menu Items
- description: Generate daily and weekly meal plans, build shopping lists, and manage meal plan templates.
  name: Meal Planning
- description: Recommend wine pairings for dishes and recipes and return wine descriptions and recommendations.
  name: Wine Pairing
- description: Classify food in images, search recipe videos, extract recipes from web pages, and return food jokes and trivia.
  name: Food Classification and Media
finops:
- name: Spoonacular Finops
  service_category: Food And Drink Data
  slug: spoonacular-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spoonacular.png
integrations:
- description: Official spoonacular-mcp server exposes the API as MCP tools for AI assistants.
  name: Model Context Protocol
- description: Official multi-language client SDKs are generated from the OpenAPI 3 spec with OpenAPI Generator.
  name: OpenAPI Generator
- description: The Spoonacular API is also available through the RapidAPI marketplace.
  name: RapidAPI
json_schemas:
- name: ComparableProduct
  property_count: 4
  slug: spoonacular-comparable-product
- name: IngredientBasics
  property_count: 3
  slug: spoonacular-ingredient-basics
- name: IngredientInformation
  property_count: 17
  slug: spoonacular-ingredient-information
- name: MenuItem
  property_count: 12
  slug: spoonacular-menu-item
- name: ProductInformation
  property_count: 19
  slug: spoonacular-product-information
- name: RecipeInformation
  property_count: 38
  slug: spoonacular-recipe-information
- name: SearchResult
  property_count: 8
  slug: spoonacular-search-result
- name: TasteInformation
  property_count: 7
  slug: spoonacular-taste-information
json_structures:
- name: Spoonacular Comparable Product Structure
  property_count: 4
  slug: spoonacular-comparable-product-structure
- name: Spoonacular Ingredient Basics Structure
  property_count: 3
  slug: spoonacular-ingredient-basics-structure
- name: Spoonacular Ingredient Information Structure
  property_count: 17
  slug: spoonacular-ingredient-information-structure
- name: Spoonacular Menu Item Structure
  property_count: 12
  slug: spoonacular-menu-item-structure
- name: Spoonacular Product Information Structure
  property_count: 19
  slug: spoonacular-product-information-structure
- name: Spoonacular Recipe Information Structure
  property_count: 38
  slug: spoonacular-recipe-information-structure
- name: Spoonacular Search Result Structure
  property_count: 8
  slug: spoonacular-search-result-structure
- name: Spoonacular Taste Information Structure
  property_count: 7
  slug: spoonacular-taste-information-structure
jsonld:
- class_count: 8
  name: Spoonacular Context
  property_count: 102
  slug: spoonacular-context
layout: provider
modified: '2026-06-03'
name: Spoonacular
nav: Providers
network: true
overview: 'Spoonacular publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ingredients API, Meal Planning API, Menu Items API, and 4 more. Tagged areas include Restaurant, Food And Drink, Recipes, Nutrition, and Meal Planning.


  The Spoonacular catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spoonacular''s developer surface includes authentication, engineering blog, developer console, signup flow, pricing, code examples, tooling, and 17 more developer resources.'
plans:
- name: Spoonacular Plans Pricing
  plan_count: 5
  slug: spoonacular-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 6
  name: Spoonacular Rate Limits
  slug: spoonacular-rate-limits
rules:
- name: Spoonacular API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spoonacular-jsonschema-spectral-rules
- name: Spoonacular API Rules
  rule_count: 29
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 19
  slug: spoonacular-spectral-rules
score:
  band: strong
  composite: 59.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 82.9
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spoonacular/refs/heads/main/screenshots/spoonacular-2026-06-20T194333.png
security:
- kind: authentication
  name: Spoonacular Authentication
  slug: spoonacular-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spoonacular Domain Security
  slug: spoonacular-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: spoonacular
tags:
- Restaurant
- Food And Drink
- Recipes
- Nutrition
- Meal Planning
- Public APIs
use_cases:
- description: Power consumer cooking apps with searchable recipes, step-by-step instructions, and ingredient-based discovery.
  name: Recipe and Cooking Apps
- description: Analyze meals and products for calories and nutrients to drive diet, fitness, and health applications.
  name: Diet and Nutrition Tracking
- description: Build shopping lists from meal plans and look up packaged products by name or UPC.
  name: Grocery and Shopping List Tools
- description: Expose recipe, nutrition, and meal-planning operations to LLM agents through the official MCP server.
  name: AI Cooking Assistants
website: https://spoonacular.com/food-api
---
