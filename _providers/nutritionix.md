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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nutritionix Agentic Access
  operation_count: 6
  slug: nutritionix-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: Search the database of food and restaurant brands.
  name: Nutritionix Brands API
  slug: nutritionix-brands-api
- description: Look up detailed nutrition for branded and restaurant menu items.
  name: Nutritionix Item API
  slug: nutritionix-item-api
- description: Translate plain-text food and exercise phrases into structured nutrition data.
  name: Nutritionix Natural Language API
  slug: nutritionix-natural-language-api
- description: Search the nutrition database for common and branded foods.
  name: Nutritionix Search API
  slug: nutritionix-search-api
artifact_total: 70
collections:
- collection_type: open
  name: Nutritionix Track API v2
  slug: open-nutritionix-track
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutritionix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutritionix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutritionix-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nutritionix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nutritionix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nutritionix.com/docs/v2
- group: start
  title: ''
  type: Signup
  url: https://developer.nutritionix.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutritionix.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutritionix
- group: build
  title: API Documentation
  type: GitHubRepository
  url: https://github.com/nutritionix/api-documentation
- group: build
  title: Node.js Client Library (npm)
  type: SDKs
  url: https://www.npmjs.com/package/nutritionix
- group: build
  title: Nutrition Label Component
  type: Tools
  url: https://github.com/nutritionix/nutrition-label
- group: build
  title: Vue Nutrition Label Component
  type: Tools
  url: https://github.com/nutritionix/vue-nutrition-label
- group: build
  title: API Data Utilities
  type: Tools
  url: https://github.com/nutritionix/nutritionix-api-data-utilities
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/nutritionix/main/rules/nutritionix-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/nutritionix/main/vocabulary/nutritionix-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/nutritionix/main/json-ld/nutritionix-track-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/nutritionix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nutritionix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nutritionix-finops.yml
created: '2026-05-28'
description: Nutritionix operates the world's largest verified nutrition database, exposing a Track API (v2) that converts natural-language food and exercise descriptions into full nutrient analysis, and powers food search, branded item lookup, and restaurant menu data for diet, fitness, and health applications.
examples:
- key_count: 4
  name: Track Alt Measure Example
  slug: track-alt-measure-example
- key_count: 4
  name: Track Brand Example
  slug: track-brand-example
- key_count: 1
  name: Track Brand Search Response Example
  slug: track-brand-search-response-example
- key_count: 12
  name: Track Branded Food Example
  slug: track-branded-food-example
- key_count: 8
  name: Track Common Food Example
  slug: track-common-food-example
- key_count: 9
  name: Track Exercise Example
  slug: track-exercise-example
- key_count: 27
  name: Track Food Example
  slug: track-food-example
- key_count: 1
  name: Track Foods Response Example
  slug: track-foods-response-example
- key_count: 2
  name: Track Full Nutrient Example
  slug: track-full-nutrient-example
- key_count: 2
  name: Track Instant Search Response Example
  slug: track-instant-search-response-example
- key_count: 5
  name: Track Natural Exercise Request Example
  slug: track-natural-exercise-request-example
- key_count: 1
  name: Track Natural Exercise Response Example
  slug: track-natural-exercise-response-example
- key_count: 10
  name: Track Natural Nutrients Request Example
  slug: track-natural-nutrients-request-example
- key_count: 1
  name: Track Natural Nutrients Response Example
  slug: track-natural-nutrients-response-example
- key_count: 3
  name: Track Photo Example
  slug: track-photo-example
features:
- description: Convert free-text meal descriptions into full nutrient breakdowns including calories, macros, and micronutrients.
  name: Natural Language Nutrition
- description: Convert free-text activity descriptions into calorie-burn estimates personalized by gender, weight, height, and age.
  name: Natural Language Exercise
- description: Typeahead search returning matched common foods and branded foods for autocomplete experiences.
  name: Instant Food Search
- description: Retrieve detailed nutrition for branded grocery and restaurant menu items by nix_item_id or UPC.
  name: Branded & Restaurant Item Lookup
- description: Access the world's largest verified nutrition database, including USDA NDB-linked common foods and over a million branded items.
  name: Verified Nutrition Database
finops:
- name: Nutritionix Finops
  service_category: Data Services
  slug: nutritionix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutritionix.png
integrations:
- description: Common-food results are linked to USDA National Nutrient Database (NDB) numbers and nutrient attribute IDs.
  name: USDA NDB
- description: Nutritionix is part of Syndigo; developer documentation is hosted on the Syndigo docs platform.
  name: Syndigo / Riversand
json_schemas:
- name: AltMeasure
  property_count: 4
  slug: track-alt-measure
- name: Brand
  property_count: 4
  slug: track-brand
- name: BrandSearchResponse
  property_count: 1
  slug: track-brand-search-response
- name: BrandedFood
  property_count: 12
  slug: track-branded-food
- name: CommonFood
  property_count: 8
  slug: track-common-food
- name: Exercise
  property_count: 9
  slug: track-exercise
- name: Food
  property_count: 27
  slug: track-food
- name: FoodsResponse
  property_count: 1
  slug: track-foods-response
- name: FullNutrient
  property_count: 2
  slug: track-full-nutrient
- name: InstantSearchResponse
  property_count: 2
  slug: track-instant-search-response
- name: NaturalExerciseRequest
  property_count: 5
  slug: track-natural-exercise-request
- name: NaturalExerciseResponse
  property_count: 1
  slug: track-natural-exercise-response
- name: NaturalNutrientsRequest
  property_count: 10
  slug: track-natural-nutrients-request
- name: NaturalNutrientsResponse
  property_count: 1
  slug: track-natural-nutrients-response
- name: Photo
  property_count: 3
  slug: track-photo
json_structures:
- name: Track Alt Measure Structure
  property_count: 4
  slug: track-alt-measure-structure
- name: Track Brand Search Response Structure
  property_count: 1
  slug: track-brand-search-response-structure
- name: Track Brand Structure
  property_count: 4
  slug: track-brand-structure
- name: Track Branded Food Structure
  property_count: 12
  slug: track-branded-food-structure
- name: Track Common Food Structure
  property_count: 8
  slug: track-common-food-structure
- name: Track Exercise Structure
  property_count: 9
  slug: track-exercise-structure
- name: Track Food Structure
  property_count: 27
  slug: track-food-structure
- name: Track Foods Response Structure
  property_count: 1
  slug: track-foods-response-structure
- name: Track Full Nutrient Structure
  property_count: 2
  slug: track-full-nutrient-structure
- name: Track Instant Search Response Structure
  property_count: 2
  slug: track-instant-search-response-structure
- name: Track Natural Exercise Request Structure
  property_count: 5
  slug: track-natural-exercise-request-structure
- name: Track Natural Exercise Response Structure
  property_count: 1
  slug: track-natural-exercise-response-structure
- name: Track Natural Nutrients Request Structure
  property_count: 10
  slug: track-natural-nutrients-request-structure
- name: Track Natural Nutrients Response Structure
  property_count: 1
  slug: track-natural-nutrients-response-structure
- name: Track Photo Structure
  property_count: 3
  slug: track-photo-structure
jsonld:
- class_count: 15
  name: Nutritionix Track Context
  property_count: 69
  slug: nutritionix-track-context
layout: provider
modified: '2026-06-03'
name: Nutritionix
nav: Providers
network: true
overview: 'Nutritionix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Item API, Natural Language API, and 1 more. Tagged areas include Restaurant, Health, Nutrition, Food, and Fitness.


  The Nutritionix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nutritionix''s developer surface includes authentication, documentation, signup flow, pricing, tooling, and 16 more developer resources.'
plans:
- name: Nutritionix Plans Pricing
  plan_count: 2
  slug: nutritionix-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Nutritionix Rate Limits
  slug: nutritionix-rate-limits
rules:
- name: Nutritionix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nutritionix-jsonschema-spectral-rules
- name: Nutritionix API Rules
  rule_count: 33
  severity_counts:
    error: 8
    hint: 0
    info: 7
    warn: 18
  slug: nutritionix-rules
score:
  band: developing
  composite: 56.7
  delta: 4.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 80.5
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 52.1
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutritionix/refs/heads/main/screenshots/nutritionix-2026-06-20T190531.png
security:
- kind: authentication
  name: Nutritionix Authentication
  slug: nutritionix-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nutritionix Domain Security
  slug: nutritionix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nutritionix
tags:
- Restaurant
- Health
- Nutrition
- Food
- Fitness
- Public APIs
use_cases:
- description: Power food logging and calorie-counting apps with natural-language meal entry.
  name: Diet & Calorie Tracking
- description: Estimate calories burned from logged workouts and activities.
  name: Fitness & Activity Tracking
- description: Surface accurate nutrition facts for restaurant and chain menu items.
  name: Restaurant Menu Nutrition
- description: Generate FDA-style nutrition labels from API nutrient data.
  name: Nutrition Label Rendering
website: https://www.nutritionix.com/
---
