---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Calorie Ninjas Agentic Access
  operation_count: 3
  slug: calorie-ninjas-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.calorieninjas.com/v1
  baseurl_source: declared
  description: The Imagetextnutrition API from CalorieNinjas — 1 operation(s) for imagetextnutrition.
  name: CalorieNinjas Imagetextnutrition API
  slug: calorie-ninjas-imagetextnutrition-api
- baseURL: https://api.calorieninjas.com/v1
  baseurl_source: declared
  description: The Nutrition API from CalorieNinjas — 1 operation(s) for nutrition.
  name: CalorieNinjas Nutrition API
  slug: calorie-ninjas-nutrition-api
- baseURL: https://api.calorieninjas.com/v1
  baseurl_source: declared
  description: The Recipe API from CalorieNinjas — 1 operation(s) for recipe.
  name: CalorieNinjas Recipe API
  slug: calorie-ninjas-recipe-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CalorieNinjas Imagetextnutrition API
  slug: open-calorie-ninjas-imagetextnutrition-api
- collection_type: open
  name: CalorieNinjas Imagetextnutrition Nutrition API
  slug: open-calorie-ninjas-nutrition-api
- collection_type: open
  name: CalorieNinjas Imagetextnutrition Recipe API
  slug: open-calorie-ninjas-recipe-api
- collection_type: open
  name: CalorieNinjas
  slug: open-calorieninjas
common:
- group: company
  title: ''
  type: Website
  url: https://www.calorieninjas.com/
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


  CalorieNinjas'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, and 7 more developer resources.'
plans:
- name: Calorie Ninjas Plans Pricing
  plan_count: 3
  slug: calorie-ninjas-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Calorie Ninjas Rate Limits
  slug: calorie-ninjas-rate-limits
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
website: https://www.calorieninjas.com/
---
