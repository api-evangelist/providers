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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Foodvisor Vision API performs food detection and nutritional analysis from images. It is provisioned under a commercial agreement; endpoint and authentication details are shared with customers and
  name: Foodvisor Vision API
  slug: vision
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foodvisor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Foodvisor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foodvisor
- group: company
  title: ''
  type: Website
  url: https://www.foodvisor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.foodvisor.io/en/vision/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.foodvisor.io/en/vision/#contact
created: '2025-03-01'
description: Foodvisor is a mobile nutrition platform whose Vision API uses computer vision and AI to identify food items from photographs and return nutritional information including calories, macronutrients, and serving estimates. The Vision API is offered to enterprise developers under a commercial agreement.
finops:
- name: Foodvisor Finops
  service_category: API
  slug: foodvisor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foodvisor.png
layout: provider
modified: '2026-04-28'
name: Foodvisor
nav: Providers
network: true
overview: 'Foodvisor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Computer Vision, Food, Health, and Nutrition.


  Foodvisor''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Foodvisor Plans Pricing
  plan_count: 3
  slug: foodvisor-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Foodvisor Rate Limits
  slug: foodvisor-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foodvisor/refs/heads/main/screenshots/foodvisor-2026-06-20T181405.png
security:
- kind: domain-security
  name: Foodvisor Domain Security
  slug: foodvisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foodvisor
tags:
- AI
- Computer Vision
- Food
- Health
- Nutrition
- Mobile
website: https://www.foodvisor.io/
---
