---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/platejoy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://platejoy.com
created: '2026-07-17'
description: PlateJoy is a personalized digital meal-planning and nutrition subscription service that generates customized weekly meal plans, recipes, and auto-built grocery lists from a detailed dietary and lifestyle questionnaire, with grocery-delivery hand-off. Founded in 2012 and later acquired into the Health.com / Dotdash Meredith consumer-health portfolio, it operates as a consumer-facing web and mobile app. As of this enrichment pass PlateJoy exposes no public developer API, OpenAPI, or documentation surface. The apex domain has no live web host and the www endpoint resolves to a dangling AWS load balancer, so only domain-level DNS/email security could be probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/platejoy.png
layout: provider
modified: '2026-07-20'
name: PlateJoy
nav: Providers
network: true
overview: PlateJoy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meal Planning, Nutrition, Recipes, and Health.
random_paper: 25
score:
  band: minimal
  composite: 5.4
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Platejoy Domain Security
  slug: platejoy-domain-security
  summary_line: DMARC
slug: platejoy
tags:
- Company
- Meal Planning
- Nutrition
- Recipes
- Health
- Food
- Grocery
- Subscription
- Consumer
website: https://platejoy.com
---
