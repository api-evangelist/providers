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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Calorie Ninjas Agentic Access
  operation_count: 3
  slug: calorie-ninjas-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: The Imagetextnutrition API from CalorieNinjas — 1 operation(s) for imagetextnutrition.
  name: CalorieNinjas Imagetextnutrition API
  slug: calorie-ninjas-imagetextnutrition-api
- description: The Nutrition API from CalorieNinjas — 1 operation(s) for nutrition.
  name: CalorieNinjas Nutrition API
  slug: calorie-ninjas-nutrition-api
- description: The Recipe API from CalorieNinjas — 1 operation(s) for recipe.
  name: CalorieNinjas Recipe API
  slug: calorie-ninjas-recipe-api
artifact_total: 10
collections:
- collection_type: open
  name: CalorieNinjas
  slug: open-calorieninjas
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calorie-ninjas-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calorie-ninjas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calorie-ninjas-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://calorieninjas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://calorieninjas.com/api
- group: start
  title: ''
  type: Login
  url: https://calorieninjas.com/signin
- group: start
  title: ''
  type: Signup
  url: https://calorieninjas.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calorieninjas.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calorieninjas.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://calorieninjas.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://calorieninjas.com/llms.txt
created: '2024-03-30'
description: CalorieNinjas provides an easy, free Nutrition Facts and Recipe API. Developers can retrieve nutrition information for over 100,000 foods and beverages using natural language queries, extract nutrition information from images of food-related text (menus, recipes, food journals), and search recipes matching search queries. All endpoints use a simple API key authentication model via the X-Api-Key header.
finops:
- name: Calorie Ninjas Finops
  service_category: API
  slug: calorie-ninjas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calorie-ninjas.png
layout: provider
modified: '2026-05-19'
name: CalorieNinjas
nav: Providers
network: true
overview: 'CalorieNinjas publishes 3 APIs on the [APIs.io](https://apis.io/) network: Imagetextnutrition API, Nutrition API, and Recipe API. Tagged areas include Beverages, Foods, Image Recognition, Nutrition, and Recipes.


  CalorieNinjas'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, and 6 more developer resources.'
plans:
- name: Calorie Ninjas Plans Pricing
  plan_count: 3
  slug: calorie-ninjas-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 5
  name: Calorie Ninjas Rate Limits
  slug: calorie-ninjas-rate-limits
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 58.9
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calorie-ninjas/refs/heads/main/screenshots/calorie-ninjas-2026-06-20T173849.png
security:
- kind: authentication
  name: Calorie Ninjas Authentication
  slug: calorie-ninjas-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Calorie Ninjas Domain Security
  slug: calorie-ninjas-domain-security
  summary_line: TLSv1.3
slug: calorie-ninjas
tags:
- Beverages
- Foods
- Image Recognition
- Nutrition
- Recipes
website: https://calorieninjas.com/
---
