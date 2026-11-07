---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Logmeal Agentic Access
  operation_count: 4
  slug: logmeal-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that provide information about the available versions of the API and our Models.<br/>Available to both APICompany ⚫ and APIUser 🔴 tokens
  name: LogMeal API and Models Versioning Functions API
  slug: logmeal-api-and-models-versioning-functions-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the APIUser's favorite meals.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal APIUser Favorite Meals API
  slug: logmeal-apiuser-favorite-meals-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that allow APICompanies to manage their APIUsers.<br/>Limited to APICompany ⚫ tokens
  name: LogMeal APIUsers Management API
  slug: logmeal-apiusers-management-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that allow APIUsers to get and modify their profiles.<br/>Limited to APIUser 🔴 tokens
  name: LogMeal APIUsers Profile Management API
  slug: logmeal-apiusers-profile-management-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints to manage body measures.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Body Measures API
  slug: logmeal-body-measures-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to managing custom nutritional indicators.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Custom Nutritional Indicators API
  slug: logmeal-custom-nutritional-indicators-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to managing custom occasions.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Custom Occasions API
  slug: logmeal-custom-occasions-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Create and assign custom recipes accessible by all the users in the company.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Custom Recipes API
  slug: logmeal-custom-recipes-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the APIUser's daily nutritional goal management.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Daily Nutritional Goal API
  slug: logmeal-daily-nutritional-goal-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that provide information about our datasets
  name: LogMeal Dataset Information, Recognized Dishes and Others API
  slug: logmeal-dataset-information-recognized-dishes-and-others-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Allows users to provide feedback about food stickiness and swallowing ease.<br/>⚡ Custom plans only ⚡
  name: LogMeal Dysphagia User Feedback API
  slug: logmeal-dysphagia-user-feedback-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that allow managing the APIUserManagers.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal External Management API
  slug: logmeal-external-management-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to applying food segmentation and quantity detection on images.<br/>⚡ Recommend plan or above ⚡
  name: LogMeal Food Quantity Detection API
  slug: logmeal-food-quantity-detection-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints for connecting the APIUsers to the Kiosk Customers that will be making use of the Food Recognition Kiosk devices.<br/>⚡ Custom plans only ⚡
  name: LogMeal Food Recognition Kiosk Integration API
  slug: logmeal-food-recognition-kiosk-integration-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Food waste detection for dish leftovers and stored food waste disposal.<br/>⚡ Recommend plan or above ⚡
  name: LogMeal Food Waste Detection API
  slug: logmeal-food-waste-detection-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to applying food recognition on images.<br/>These endpoints are all limited to APIUser 🔴 tokens
  name: LogMeal Image-based Food Recognition API
  slug: logmeal-image-based-food-recognition-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints that provide useful information about the Food AI Engine API.
  name: LogMeal Informative Endpoints API
  slug: logmeal-informative-endpoints-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the nutritional information services.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Ingredients and Nutritional Information API
  slug: logmeal-ingredients-and-nutritional-information-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the APIUser's intake history management and visualization.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Intake History API
  slug: logmeal-intake-history-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the APIUser's intake variety and Nutri-Score services.<br/>⚡ Recommend plan or above ⚡
  name: LogMeal Intake Variety Score and Nutri-Scores API
  slug: logmeal-intake-variety-score-and-nutri-scores-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the available nutritional plans and their management.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Nutritional Plans API
  slug: logmeal-nutritional-plans-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints related to the APIUser's recipe and dish recommendations services.<br/>⚡ Recommend plan or above ⚡
  name: LogMeal Recipe and Dish Recommendations API
  slug: logmeal-recipe-and-dish-recommendations-api
- baseURL: https://api.logmeal.com
  baseurl_source: declared
  description: Endpoints with information about cooking measures and easy modulation.<br/>⚡ Monitor plan or above ⚡
  name: LogMeal Units of Measurement and Easy Modulation API
  slug: logmeal-units-of-measurement-and-easy-modulation-api
artifact_total: 34
collections:
- collection_type: open
  name: LogMeal Food Recognition API
  slug: open-logmeal-food-recognition-api
- collection_type: open
  name: LogMeal Food Recognition History API
  slug: open-logmeal-history-api
- collection_type: open
  name: LogMeal Food Recognition History Image Recognition API
  slug: open-logmeal-image-recognition-api
- collection_type: open
  name: LogMeal Food Recognition History Nutrition API
  slug: open-logmeal-nutrition-api
common:
- group: commercial
  href: https://artifacts.apis.io/logmeal/plans/logmeal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logmeal-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/logmeal/rate-limits/logmeal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logmeal-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/logmeal/finops/logmeal-finops.yml
  title: ''
  type: FinOps
  url: finops/logmeal-finops.yml
- group: agent
  href: https://artifacts.apis.io/logmeal/agentic-access/logmeal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logmeal-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/logmeal/security/logmeal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logmeal-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/logmeal/authentication/logmeal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logmeal-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logmeal
- group: company
  title: ''
  type: Website
  url: https://logmeal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logmeal.com
- group: start
  title: ''
  type: Portal
  url: https://logmeal.com/api/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.logmeal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.logmeal.com/feed/
created: '2025-03-01'
description: LogMeal provides a Food Recognition Image API that detects foods, drinks, vegetables, fruits and prepared dishes from images. The platform offers semantic tagging including food group, dish and ingredients recognition, as well as nutritional information analysis with 35+ nutritional indicators and user intake history tracking.
finops:
- has_sources: false
  method: generated
  name: Logmeal Finops
  primary_unit: request
  service_category: API
  slug: logmeal-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logmeal.png
layout: provider
modified: '2026-05-19'
name: LogMeal
nav: Providers
network: true
overview: 'LogMeal publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including API and Models Versioning Functions API, APIUser Favorite Meals API, APIUsers Management API, and 20 more. Tagged areas include Computer Vision, Food, Image Recognition, Nutrition, and Semantic Tagging.


  The LogMeal catalog on APIs.io includes 1 Spectral governance ruleset.


  LogMeal''s developer surface includes authentication, documentation, developer portal, engineering blog, and 8 more developer resources.'
plans:
- name: Logmeal Plans Pricing
  plan_count: 3
  slug: logmeal-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Logmeal Rate Limits
  slug: logmeal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: LogMeal API Rules
  rule_count: 63
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 12
  slug: logmeal-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 58.5
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.2
      total: 27
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/logmeal/logmeal-2026-06-20T184658.png
security:
- kind: authentication
  name: Logmeal Authentication
  slug: logmeal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Logmeal Domain Security
  slug: logmeal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: logmeal
tags:
- Computer Vision
- Food
- Image Recognition
- Nutrition
- Semantic Tagging
website: https://logmeal.com
---
