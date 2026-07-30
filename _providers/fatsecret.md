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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fatsecret Agentic Access
  operation_count: 23
  slug: fatsecret-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 8
apis:
- description: Daily exercise tracking
  name: FatSecret Exercise Diary API
  slug: fatsecret-exercise-diary-api
- description: Daily food entries and summaries
  name: FatSecret Food Diary API
  slug: fatsecret-food-diary-api
- description: Search and retrieve food nutrition data
  name: FatSecret Foods API
  slug: fatsecret-foods-api
- description: User-managed custom foods and favorites
  name: FatSecret Profile Foods API
  slug: fatsecret-profile-foods-api
- description: Saved meals and meal items
  name: FatSecret Profile Meals API
  slug: fatsecret-profile-meals-api
- description: Search and retrieve recipes
  name: FatSecret Recipes API
  slug: fatsecret-recipes-api
- description: Reference data for brands, categories, and exercises
  name: FatSecret Reference API
  slug: fatsecret-reference-api
- description: User weight history
  name: FatSecret Weight Tracking API
  slug: fatsecret-weight-tracking-api
artifact_total: 20
collections:
- collection_type: open
  name: FatSecret Platform API
  slug: open-fatsecret-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fatsecret-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fatsecret-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fatsecret-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fatsecret-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fatsecret-group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fatsecret
- group: company
  title: ''
  type: Website
  url: https://platform.fatsecret.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.fatsecret.com/platform-api
- group: start
  title: ''
  type: Signup
  url: https://platform.fatsecret.com/registration
- group: docs
  title: ''
  type: Guides
  url: https://platform.fatsecret.com/docs/guides
- group: company
  title: ''
  type: Blog
  url: https://blog.fatsecret.com/rss
created: '2025-03-01'
description: FatSecret is a global nutrition and wellness platform whose Platform API exposes a verified database of more than 1.9 million foods across 56 countries, plus recipes, exercises, and user-scoped food diary, exercise diary, and weight tracking. The API is used by more than 35,000 developers and serves over 700 million calls per month.
finops:
- name: Fatsecret Finops
  service_category: API
  slug: fatsecret-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fatsecret.png
json_schemas:
- name: FatSecret Food Diary Entry
  property_count: 11
  slug: fatsecret-food-entry
- name: FatSecret Food
  property_count: 6
  slug: fatsecret-food
- name: FatSecret Recipe
  property_count: 13
  slug: fatsecret-recipe
layout: provider
modified: '2026-05-19'
name: FatSecret
nav: Providers
network: true
overview: 'FatSecret publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Exercise Diary API, Food Diary API, Foods API, and 5 more. Tagged areas include Barcode Scanning, Calories, Diets, Exercise, and Fitness.


  The FatSecret catalog on APIs.io includes 1 Spectral governance ruleset.


  FatSecret''s developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Fatsecret Plans Pricing
  plan_count: 3
  slug: fatsecret-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Fatsecret Rate Limits
  slug: fatsecret-rate-limits
rules:
- name: FatSecret API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fatsecret-jsonschema-spectral-rules
scopes:
- name: Fatsecret Scopes
  scope_count: 2
  slug: fatsecret-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fatsecret/refs/heads/main/screenshots/fatsecret-2026-06-20T181056.png
security:
- kind: authentication
  name: Fatsecret Authentication
  slug: fatsecret-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fatsecret Domain Security
  slug: fatsecret-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fatsecret
tags:
- Barcode Scanning
- Calories
- Diets
- Exercise
- Fitness
- Food Diary
- Health
- Macronutrients
- Nutrition
- Recipes
- Weight Tracking
website: https://platform.fatsecret.com/
---
