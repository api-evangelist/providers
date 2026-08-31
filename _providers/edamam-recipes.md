---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Edamam Recipes Agentic Access
  operation_count: 14
  slug: edamam-recipes-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 4
apis:
- description: The Food Nutrition Request - AI Vision (Beta) API from Edamam — 1 operation(s) for food nutrition request - ai vision (beta).
  name: Edamam Food Nutrition Request - AI Vision (Beta) API
  slug: edamam-recipes-food-nutrition-request-ai-vision-beta-api
- description: The Food Request Step 1 - Parser API from Edamam — 1 operation(s) for food request step 1 - parser.
  name: Edamam Food Request Step 1 - Parser API
  slug: edamam-recipes-food-request-step-1-parser-api
- description: The Food Request Step 2 - Nutrients API from Edamam — 1 operation(s) for food request step 2 - nutrients.
  name: Edamam Food Request Step 2 - Nutrients API
  slug: edamam-recipes-food-request-step-2-nutrients-api
- description: The Food Search Autocomplete API from Edamam — 1 operation(s) for food search autocomplete.
  name: Edamam Food Search Autocomplete API
  slug: edamam-recipes-food-search-autocomplete-api
- description: The Nutrition Data API from Edamam — 1 operation(s) for nutrition data.
  name: Edamam Nutrition Data API
  slug: edamam-recipes-nutrition-data-api
- description: The Nutrition Details API from Edamam — 1 operation(s) for nutrition details.
  name: Edamam Nutrition Details API
  slug: edamam-recipes-nutrition-details-api
- description: Meal planning
  name: Edamam planner API
  slug: edamam-recipes-planner-api
- description: Search or access individual recipes.
  name: Edamam Recipe Search API
  slug: edamam-recipes-recipe-search-api
- description: The *Shopping List API* provides aggregation of shopping item quantities over one or more ingredient lists, and optional referral to external shopping services. A `shopping-list` call may be issued on
  name: Edamam Shopping List API
  slug: edamam-recipes-shopping-list-api
- description: Daily values
  name: Edamam values API
  slug: edamam-recipes-values-api
artifact_total: 78
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Food Database API
  slug: open-edamam-food-database-v2
- collection_type: open
  name: Meal Planning API
  slug: open-edamam-meal-planner-v1
- collection_type: open
  name: Nutrition Analysis API
  slug: open-edamam-nutrition-analysis-v1
- collection_type: open
  name: Recipe Search and Shopping List API
  slug: open-edamam-recipe-search-v2
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) API
  slug: open-edamam-recipes-food-nutrition-request-ai-vision-beta-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Food Request Step 1 - Parser API
  slug: open-edamam-recipes-food-request-step-1-parser-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Food Request Step 2 - Nutrients API
  slug: open-edamam-recipes-food-request-step-2-nutrients-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Food Search Autocomplete API
  slug: open-edamam-recipes-food-search-autocomplete-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Nutrition Data API
  slug: open-edamam-recipes-nutrition-data-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Nutrition Details API
  slug: open-edamam-recipes-nutrition-details-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) planner API
  slug: open-edamam-recipes-planner-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Recipe Search API
  slug: open-edamam-recipes-recipe-search-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) Shopping List API
  slug: open-edamam-recipes-shopping-list-api
- collection_type: open
  name: Food Database Food Nutrition Request - AI Vision (Beta) Food Nutrition Request - AI Vision (Beta) values API
  slug: open-edamam-recipes-values-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edamam-recipes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edamam-recipes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edamam-recipes-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.edamam.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.edamam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.edamam.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.edamam.com/admin/applications/new
- group: start
  title: ''
  type: Login
  url: https://developer.edamam.com/admin
- group: operate
  title: ''
  type: FAQ
  url: https://developer.edamam.com/api/faq
- group: operate
  title: ''
  type: Support
  url: https://developer.edamam.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edamam.com/page/api-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edamam.com/page/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/edamam-recipes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edamam-recipes-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/edamam-recipes-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/edamam-recipes-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/edamam-recipes-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edamam-llc
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: Tools
  url: ''
created: '2026-05-28'
description: Edamam is a food and nutrition data platform powering recipe search, NLP-based nutrition analysis, food database lookup (keyword / brand / UPC / AI Vision), and personalized meal planning. The flagship Recipe Search API v2 covers a 2M+ recipe index with 30+ filters across diet, health, cuisine, meal, dish, nutrients, time, glycemic index, and CO2 emissions class.
examples:
- key_count: 2
  name: Food Database Food Search Example
  slug: food-database-food-search-example
- key_count: 2
  name: Meal Planner Create Plan Example
  slug: meal-planner-create-plan-example
- key_count: 2
  name: Nutrition Analysis Full Recipe Analysis Example
  slug: nutrition-analysis-full-recipe-analysis-example
- key_count: 2
  name: Recipe Search Lookup Recipe By Id Example
  slug: recipe-search-lookup-recipe-by-id-example
- key_count: 2
  name: Recipe Search Lookup Recipes By Uri Example
  slug: recipe-search-lookup-recipes-by-uri-example
- key_count: 2
  name: Recipe Search Search Recipe Example
  slug: recipe-search-search-recipe-example
- key_count: 2
  name: Recipe Search Shopping List Example
  slug: recipe-search-shopping-list-example
features:
- description: Search across 2 million recipes from third-party sources plus 20,000+ Edamam-owned recipes with cooking instructions.
  name: 2M+ Recipe Index
- description: Filter by diet, health/allergen labels, cuisine, meal type, dish type, calorie range, total time, nutrients, glycemic index, and excluded ingredients.
  name: 30+ Filters
- description: Per-recipe and per-food breakdowns including macros, vitamins (A, B-12, C, D, E, K), minerals (Ca, Fe, K, Mg, P, Zn), fiber, sodium, sugars.
  name: 28+ Nutrients
- description: Recipes carry a CO2 emissions class (A+ through G) when beta=true is set.
  name: Carbon Footprint (CO2e)
- description: Submit a public image URL or base64 data URI to the Food Database API and receive detected food + nutrition estimates.
  name: AI Vision Food Recognition
- description: Submit raw recipe text (title + ingredient lines) to the Nutrition Analysis API and receive structured nutrient and label output.
  name: NLP Recipe Analysis
- description: Use the Edamam-Account-User header to bind per-user budgets and caching rights (required on Enterprise and Meal Planner plans).
  name: Active User Tracking
- description: Aggregate ingredient quantities across one or more recipes into a consolidated shopping list, with optional Instacart integration on Enterprise tiers.
  name: Shopping List Aggregation
- description: gzip supported via Accept-Encoding header.
  name: HTTP Compression
- description: _links.next on paged responses; _links.self on individual hits.
  name: HATEOAS Pagination
finops:
- name: Edamam Recipes Finops
  service_category: ''
  slug: edamam-recipes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edamam-recipes.png
integrations:
- description: Meal Planner Enterprise tiers integrate with Instacart for grocery fulfillment.
  name: Instacart
- description: Built-in chatbot UI for recipe / nutrition Q&A.
  name: Edamam Platform Assistant
- description: Recipe Management API integrates with the Recipe Search surface.
  name: Edamam Content Management
- description: Official Edamam Food MCP server at https://mcp.edamam.com/mcp/food exposes get_food_nutrition and analyze_food_image tools to LLM agents (Claude Code, etc.).
  name: Model Context Protocol (MCP)
json_schemas:
- name: Edamam Food
  property_count: 11
  slug: edamam-food
- name: Edamam Meal Plan
  property_count: 2
  slug: edamam-meal-plan
- name: Edamam Nutrient Info
  property_count: 3
  slug: edamam-nutrient-info
- name: Edamam Recipe
  property_count: 29
  slug: edamam-recipe
- name: Edamam Recipe Search Response
  property_count: 5
  slug: edamam-recipe-search-response
json_structures:
- name: Edamam Food Structure
  property_count: 11
  slug: edamam-food-structure
- name: Edamam Meal Plan Structure
  property_count: 2
  slug: edamam-meal-plan-structure
- name: Edamam Recipe Structure
  property_count: 29
  slug: edamam-recipe-structure
jsonld:
- class_count: 25
  name: Edamam Recipes Context
  property_count: 18
  slug: edamam-recipes-context
layout: provider
modified: '2026-05-30'
name: Edamam
nav: Providers
network: true
overview: 'Edamam publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Food Nutrition Request - AI Vision (Beta) API, Food Request Step 1 - Parser API, Food Request Step 2 - Nutrients API, and 7 more. Tagged areas include Food And Drink, Recipes, Nutrition, Diet, and Allergens.


  The Edamam catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Edamam''s developer surface includes authentication, documentation, signup flow, FAQ, support, tooling, and 13 more developer resources.'
plans:
- name: Edamam Recipes Plans Pricing
  plan_count: 0
  slug: edamam-recipes-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Edamam Recipes Rate Limits
  slug: edamam-recipes-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Edamam API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: edamam-recipes-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Edamam API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: edamam-recipes-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 28.8
    contract_quality: 63.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edamam-recipes/refs/heads/main/screenshots/edamam-recipes-2026-06-20T180448.png
security:
- kind: authentication
  name: Edamam Recipes Authentication
  slug: edamam-recipes-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Edamam Recipes Domain Security
  slug: edamam-recipes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edamam-recipes
solutions:
- description: $9/mo, 10,000 calls/mo, 10 calls/min, third-party web recipes, 10-day trial.
  name: Recipe Search Enterprise Basic
- description: $99/mo, 500,000 calls/mo, 100 calls/min.
  name: Recipe Search Enterprise Core
- description: $399/mo, 1,000,000 calls/mo, 300 calls/min, Edamam-owned recipes with cooking instructions, CO2e data.
  name: Recipe Search Enterprise Plus
- description: Custom — contact sales for unlimited usage and custom content.
  name: Recipe Search Enterprise Unlimited
- description: $14/mo, 100,000 calls + 500 Vision requests, includes MCP server access.
  name: Food Database Basic Vision
- description: $69/mo, 750,000 calls, pay-as-you-go Vision.
  name: Food Database Core
- description: $299/mo, 5,000,000 calls, 10,000 Vision requests.
  name: Food Database Plus
- description: Free, 10 MAU, 20 meal-plan calls/day, 300 recipe calls/min, non-commercial.
  name: Meal Planner Developer
- description: $300/mo, 1,000 MAU, 30 meal-plan calls/day, 5,000 recipe calls/min, Instacart integration.
  name: Meal Planner Enterprise Core
tags:
- Food And Drink
- Recipes
- Nutrition
- Diet
- Allergens
- Meal Planning
- Sustainability
- Carbon Footprint
- Public APIs
use_cases:
- description: Build consumer recipe search and discovery apps with rich filtering.
  name: Recipe Discovery Apps
- description: Power food logging and nutrition tracking with NLP-based ingredient analysis.
  name: Nutrition Tracking
- description: Generate diet- and health-aware meal plans for fitness, wellness, and clinical nutrition apps.
  name: Personalized Meal Planning
- description: Aggregate ingredients into shopping lists with optional Instacart fulfillment.
  name: Grocery and Shopping
- description: Edamam Platform Assistant chatbot and MCP server expose food/recipe tools to conversational agents.
  name: Chatbots and Voice
- description: Surface CO2e emissions class to promote lower-impact food choices.
  name: Sustainability Apps
website: https://www.edamam.com/
---
