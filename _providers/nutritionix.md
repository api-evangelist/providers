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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nutritionix Agentic Access
  operation_count: 6
  slug: nutritionix-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- baseURL: https://trackapi.nutritionix.com/v2
  baseurl_source: declared
  description: Search the database of food and restaurant brands.
  name: Nutritionix Brands API
  slug: nutritionix-brands-api
- baseURL: https://trackapi.nutritionix.com/v2
  baseurl_source: declared
  description: Look up detailed nutrition for branded and restaurant menu items.
  name: Nutritionix Item API
  slug: nutritionix-item-api
- baseURL: https://trackapi.nutritionix.com/v2
  baseurl_source: declared
  description: Translate plain-text food and exercise phrases into structured nutrition data.
  name: Nutritionix Natural Language API
  slug: nutritionix-natural-language-api
- baseURL: https://trackapi.nutritionix.com/v2
  baseurl_source: declared
  description: Search the nutrition database for common and branded foods.
  name: Nutritionix Search API
  slug: nutritionix-search-api
artifact_total: 75
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nutritionix Track API v2 Brands API
  slug: open-nutritionix-brands-api
- collection_type: open
  name: Nutritionix Track API v2 Brands Item API
  slug: open-nutritionix-item-api
- collection_type: open
  name: Nutritionix Track API v2 Brands Natural Language API
  slug: open-nutritionix-natural-language-api
- collection_type: open
  name: Nutritionix Track API v2 Brands Search API
  slug: open-nutritionix-search-api
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
random_paper: 11
rate_limits:
- limit_count: 3
  name: Nutritionix Rate Limits
  slug: nutritionix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nutritionix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nutritionix-jsonschema-spectral-rules
- effective_rule_count: 33
  extends: []
  name: Nutritionix API Rules
  rule_count: 33
  severity_counts:
    error: 8
    hint: 0
    info: 7
    warn: 18
  slug: nutritionix-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 93.5
    catalog_earned_first_party: 0.0
    catalog_gap: 21.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 32.4
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
