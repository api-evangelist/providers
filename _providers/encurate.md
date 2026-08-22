---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Keto Diet REST API providing over 450 recipes across 11 categories with structured nutritional values (calories, fats, carbohydrates, proteins) returned as JSON, designed for integration into health, '
  name: Encurate Keto Diet API
  slug: encurate-keto-diet-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encurate-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encurate
- group: company
  title: ''
  type: Website
  url: https://encurate.app/
created: '2024-03-30'
description: Encurate provides a Keto Diet API offering over 450 keto recipes across 11 categories (drinks, smoothies, staples, dips, desserts, soups, fish, beef, appetizers, snacks, and breakfast) with structured nutritional values including calories, fats, carbohydrates, and proteins. The REST API returns JSON and is distributed via RapidAPI with a free testing tier and a paid unlimited production tier for integration into health, fitness, and nutrition applications.
finops:
- name: Encurate Finops
  service_category: API
  slug: encurate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encurate.png
layout: provider
modified: '2026-04-28'
name: Encurate
nav: Providers
network: true
overview: Encurate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Diet, Food, Keto, Nutrition, and Recipes.
plans:
- name: Encurate Plans Pricing
  plan_count: 3
  slug: encurate-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Encurate Rate Limits
  slug: encurate-rate-limits
score:
  band: minimal
  composite: 9.2
  delta: -1.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encurate/refs/heads/main/screenshots/encurate-2026-06-20T180653.png
security:
- kind: domain-security
  name: Encurate Domain Security
  slug: encurate-domain-security
  summary_line: TLSv1.3
slug: encurate
tags:
- Diet
- Food
- Keto
- Nutrition
- Recipes
- Health
- Fitness
website: https://encurate.app/
---
