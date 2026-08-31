---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Edamam Agentic Access
  operation_count: 7
  slug: edamam-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: The Edamam Nutrition Analysis API provides detailed nutrition data for recipes and food items. Send a recipe or food description and receive comprehensive nutritional information including calories, m
  name: Edamam Nutrition Analysis API
  slug: edamam-nutrition-analysis-api
- description: The Edamam Recipe Search API provides access to over 2 million recipes with full nutritional analysis, diet and health labels, ingredient details, and cuisine type.
  name: Edamam Recipe Search API
  slug: edamam-recipe-search-api
- description: The Edamam Meal Planner API provides personalized meal planning capabilities based on dietary preferences, nutrition goals, and available ingredients.
  name: Edamam Meal Planner API
  slug: edamam-meal-planner-api
- description: Search foods by keyword or barcode and resolve nutrition.
  name: Edamam Food Database API
  slug: edamam-food-database-api
artifact_total: 79
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Edamam Food and Grocery Database API
  slug: open-edamam-food-and-grocery-database-api
- collection_type: open
  name: Edamam Food and Grocery Database Food Database API
  slug: open-edamam-food-database-api
- collection_type: open
  name: Edamam Food and Grocery Database Food Database Meal Planner API
  slug: open-edamam-meal-planner-api
- collection_type: open
  name: Edamam Food and Grocery Database Food Database Nutrition Analysis API
  slug: open-edamam-nutrition-analysis-api
- collection_type: open
  name: Edamam Food and Grocery Database Food Database Recipe Search API
  slug: open-edamam-recipe-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edamam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edamam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edamam-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edamam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edamam
- group: build
  title: MCP Server (Food Database)
  type: Tools
  url: https://github.com/edamam-llc/mcp-edamam-food
- group: build
  title: ''
  type: Tools
  url: https://developer.edamam.com/mcp-edamam-food
- group: build
  title: Java Demo (Nutrition Analysis API)
  type: CodeExamples
  url: https://github.com/edamam-llc/edamam-api-demo
- group: design
  title: Edamam Spectral Rules
  type: Spectral
  url: rules/edamam-spectral-rules.yml
- group: design
  title: Edamam Vocabulary
  type: Vocabulary
  url: vocabulary/edamam-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/edamam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edamam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edamam-finops.yml
- group: design
  title: Nutrition Analysis Context
  type: JSONLD
  url: json-ld/edamam-nutrition-analysis-api-context.jsonld
- group: design
  title: Food Database Context
  type: JSONLD
  url: json-ld/edamam-food-and-grocery-database-api-context.jsonld
- group: design
  title: Recipe Search Context
  type: JSONLD
  url: json-ld/edamam-recipe-search-api-context.jsonld
- group: design
  title: Meal Planner Context
  type: JSONLD
  url: json-ld/edamam-meal-planner-api-context.jsonld
- group: operate
  title: ''
  type: FAQ
  url: https://developer.edamam.com/api/faq
- group: other
  title: ''
  type: Attribution
  url: https://developer.edamam.com/attribution
- group: other
  title: ''
  type: DataLicensing
  url: https://www.edamam.com/data-licensing/
- group: company
  title: ''
  type: Partners
  url: https://www.edamam.com/partners/
- group: start
  title: ''
  type: Portal
  url: https://www.edamam.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edamam.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edamam.com/terms/api/
created: '2024-11-13'
description: Edamam is a leading provider of nutrition data and analytics. They offer nutrition analysis, food database, recipe search, and meal planning APIs that power thousands of health, fitness, and food apps. Their databases contain close to 900,000 foods, over 2 million recipes, and comprehensive nutritional information.
examples:
- key_count: 7
  name: Food And Grocery Database Api Food Example
  slug: food-and-grocery-database-api-food-example
- key_count: 2
  name: Food And Grocery Database Api Food Hint Example
  slug: food-and-grocery-database-api-food-hint-example
- key_count: 3
  name: Food And Grocery Database Api Measure Example
  slug: food-and-grocery-database-api-measure-example
- key_count: 3
  name: Food And Grocery Database Api Nutrient Example
  slug: food-and-grocery-database-api-nutrient-example
- key_count: 1
  name: Food And Grocery Database Api Nutrients Request Example
  slug: food-and-grocery-database-api-nutrients-request-example
- key_count: 7
  name: Food And Grocery Database Api Nutrients Response Example
  slug: food-and-grocery-database-api-nutrients-response-example
- key_count: 4
  name: Food And Grocery Database Api Parser Response Example
  slug: food-and-grocery-database-api-parser-response-example
- key_count: 1
  name: Meal Planner Api Constraint Example
  slug: meal-planner-api-constraint-example
- key_count: 2
  name: Meal Planner Api Meal Plan Request Example
  slug: meal-planner-api-meal-plan-request-example
- key_count: 2
  name: Meal Planner Api Meal Plan Response Example
  slug: meal-planner-api-meal-plan-response-example
- key_count: 2
  name: Meal Planner Api Nutrient Range Example
  slug: meal-planner-api-nutrient-range-example
- key_count: 2
  name: Meal Planner Api Section Example
  slug: meal-planner-api-section-example
- key_count: 3
  name: Nutrition Analysis Api Nutrient Example
  slug: nutrition-analysis-api-nutrient-example
- key_count: 10
  name: Nutrition Analysis Api Nutrition Response Example
  slug: nutrition-analysis-api-nutrition-response-example
- key_count: 6
  name: Nutrition Analysis Api Recipe Request Example
  slug: nutrition-analysis-api-recipe-request-example
- key_count: 3
  name: Recipe Search Api Nutrient Example
  slug: recipe-search-api-nutrient-example
- key_count: 19
  name: Recipe Search Api Recipe Example
  slug: recipe-search-api-recipe-example
- key_count: 2
  name: Recipe Search Api Recipe Hit Example
  slug: recipe-search-api-recipe-hit-example
- key_count: 5
  name: Recipe Search Api Recipe Search Response Example
  slug: recipe-search-api-recipe-search-response-example
finops:
- name: Edamam Finops
  service_category: Developer Tools / API
  slug: edamam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edamam.png
json_schemas:
- name: FoodHint
  property_count: 2
  slug: food-and-grocery-database-api-food-hint
- name: Food
  property_count: 7
  slug: food-and-grocery-database-api-food
- name: Measure
  property_count: 3
  slug: food-and-grocery-database-api-measure
- name: Nutrient
  property_count: 3
  slug: food-and-grocery-database-api-nutrient
- name: NutrientsRequest
  property_count: 1
  slug: food-and-grocery-database-api-nutrients-request
- name: NutrientsResponse
  property_count: 7
  slug: food-and-grocery-database-api-nutrients-response
- name: ParserResponse
  property_count: 4
  slug: food-and-grocery-database-api-parser-response
- name: Constraint
  property_count: 1
  slug: meal-planner-api-constraint
- name: MealPlanRequest
  property_count: 2
  slug: meal-planner-api-meal-plan-request
- name: MealPlanResponse
  property_count: 2
  slug: meal-planner-api-meal-plan-response
- name: NutrientRange
  property_count: 2
  slug: meal-planner-api-nutrient-range
- name: Section
  property_count: 2
  slug: meal-planner-api-section
- name: Nutrient
  property_count: 3
  slug: nutrition-analysis-api-nutrient
- name: NutritionResponse
  property_count: 10
  slug: nutrition-analysis-api-nutrition-response
- name: RecipeRequest
  property_count: 6
  slug: nutrition-analysis-api-recipe-request
- name: Nutrient
  property_count: 3
  slug: recipe-search-api-nutrient
- name: RecipeHit
  property_count: 2
  slug: recipe-search-api-recipe-hit
- name: Recipe
  property_count: 19
  slug: recipe-search-api-recipe
- name: RecipeSearchResponse
  property_count: 5
  slug: recipe-search-api-recipe-search-response
json_structures:
- name: Food And Grocery Database Api Food Hint Structure
  property_count: 2
  slug: food-and-grocery-database-api-food-hint-structure
- name: Food And Grocery Database Api Food Structure
  property_count: 7
  slug: food-and-grocery-database-api-food-structure
- name: Food And Grocery Database Api Measure Structure
  property_count: 3
  slug: food-and-grocery-database-api-measure-structure
- name: Food And Grocery Database Api Nutrient Structure
  property_count: 3
  slug: food-and-grocery-database-api-nutrient-structure
- name: Food And Grocery Database Api Nutrients Request Structure
  property_count: 1
  slug: food-and-grocery-database-api-nutrients-request-structure
- name: Food And Grocery Database Api Nutrients Response Structure
  property_count: 7
  slug: food-and-grocery-database-api-nutrients-response-structure
- name: Food And Grocery Database Api Parser Response Structure
  property_count: 4
  slug: food-and-grocery-database-api-parser-response-structure
- name: Meal Planner Api Constraint Structure
  property_count: 1
  slug: meal-planner-api-constraint-structure
- name: Meal Planner Api Meal Plan Request Structure
  property_count: 2
  slug: meal-planner-api-meal-plan-request-structure
- name: Meal Planner Api Meal Plan Response Structure
  property_count: 2
  slug: meal-planner-api-meal-plan-response-structure
- name: Meal Planner Api Nutrient Range Structure
  property_count: 2
  slug: meal-planner-api-nutrient-range-structure
- name: Meal Planner Api Section Structure
  property_count: 2
  slug: meal-planner-api-section-structure
- name: Nutrition Analysis Api Nutrient Structure
  property_count: 3
  slug: nutrition-analysis-api-nutrient-structure
- name: Nutrition Analysis Api Nutrition Response Structure
  property_count: 10
  slug: nutrition-analysis-api-nutrition-response-structure
- name: Nutrition Analysis Api Recipe Request Structure
  property_count: 6
  slug: nutrition-analysis-api-recipe-request-structure
- name: Recipe Search Api Nutrient Structure
  property_count: 3
  slug: recipe-search-api-nutrient-structure
- name: Recipe Search Api Recipe Hit Structure
  property_count: 2
  slug: recipe-search-api-recipe-hit-structure
- name: Recipe Search Api Recipe Search Response Structure
  property_count: 5
  slug: recipe-search-api-recipe-search-response-structure
- name: Recipe Search Api Recipe Structure
  property_count: 19
  slug: recipe-search-api-recipe-structure
jsonld:
- class_count: 7
  name: Edamam Food And Grocery Database Api Context
  property_count: 25
  slug: edamam-food-and-grocery-database-api-context
- class_count: 5
  name: Edamam Meal Planner Api Context
  property_count: 14
  slug: edamam-meal-planner-api-context
- class_count: 3
  name: Edamam Nutrition Analysis Api Context
  property_count: 18
  slug: edamam-nutrition-analysis-api-context
- class_count: 4
  name: Edamam Recipe Search Api Context
  property_count: 27
  slug: edamam-recipe-search-api-context
layout: provider
modified: '2026-06-02'
name: Edamam
nav: Providers
network: true
overview: 'Edamam publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Nutrition Analysis API, Recipe Search API, Meal Planner API, and 1 more. Tagged areas include Restaurant, Food, Nutrition, and UPC.


  The Edamam catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Edamam''s developer surface includes authentication, tooling, code examples, FAQ, developer portal, and 19 more developer resources.'
plans:
- name: Edamam Plans Pricing
  plan_count: 4
  slug: edamam-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 11
  name: Edamam Rate Limits
  slug: edamam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Edamam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: edamam-jsonschema-spectral-rules
- effective_rule_count: 85
  extends:
  - spectral:oas
  name: Edamam API Rules
  rule_count: 44
  severity_counts:
    error: 8
    hint: 0
    info: 16
    warn: 20
  slug: edamam-spectral-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 25.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edamam/refs/heads/main/screenshots/edamam-2026-06-20T180443.png
security:
- kind: authentication
  name: Edamam Authentication
  slug: edamam-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Edamam Domain Security
  slug: edamam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edamam
tags:
- Restaurant
- Food
- Nutrition
- UPC
website: https://www.edamam.com/
---
