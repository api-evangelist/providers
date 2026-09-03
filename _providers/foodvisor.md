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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
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
overview: 'Foodvisor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Computer-Vision, Food, Health, and Nutrition.


  Foodvisor''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Foodvisor Plans Pricing
  plan_count: 3
  slug: foodvisor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Foodvisor Rate Limits
  slug: foodvisor-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foodvisor/refs/heads/main/screenshots/foodvisor-2026-06-20T181405.png
security:
- kind: domain-security
  name: Foodvisor Domain Security
  slug: foodvisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foodvisor
tags:
- Artificial Intelligence
- Computer-Vision
- Food
- Health
- Nutrition
- Mobile
website: https://www.foodvisor.io/
---
