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
- description: Provides access to Dietagram's extensive food database and nutritional standards for integrating nutrition data into applications.
  name: Dietagram Nutrition API
  slug: dietagram
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutrition-exercise-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://dietagram.com/
created: '2024-03-30'
description: The Dietagram Nutrition API is designed to simplify the integration of your application with Dietagram's extensive food database and nutritional standards. Rather than developing and maintaining your own nutrient database, you can rely on Dietagram for high-quality source data.
finops:
- name: Nutrition Exercise Api Finops
  service_category: API
  slug: nutrition-exercise-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutrition-exercise-api.png
layout: provider
modified: '2026-04-28'
name: Nutrition & Exercise API
nav: Providers
network: true
overview: Nutrition & Exercise API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Exercise, Food, Health, and Nutrition.
plans:
- name: Nutrition Exercise Api Plans Pricing
  plan_count: 3
  slug: nutrition-exercise-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Nutrition Exercise Api Rate Limits
  slug: nutrition-exercise-api-rate-limits
score:
  band: minimal
  composite: 7.5
  delta: -1.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutrition-exercise-api/refs/heads/main/screenshots/nutrition-exercise-api-2026-06-20T190533.png
security:
- kind: domain-security
  name: Nutrition Exercise Api Domain Security
  slug: nutrition-exercise-api-domain-security
  summary_line: no transport/DNS hardening detected
slug: nutrition-exercise-api
tags:
- Exercise
- Food
- Health
- Nutrition
website: http://dietagram.com/
---
