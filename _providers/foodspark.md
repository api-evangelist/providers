---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
- description: Foodspark provides a restaurant data API, food and grocery pricing API, restaurant menu API, and aggregated food-delivery data sourced from 100+ platforms. Endpoint and authentication details are prov
  name: Foodspark Food Data Service
  slug: foodspark-data
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foodspark-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foodspark
- group: company
  title: ''
  type: Website
  url: https://www.foodspark.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.foodspark.io/food-data-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.foodspark.io/pricing/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.foodspark.io/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.foodspark.io/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/foodspark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/foodspark-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/foodspark-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.foodspark.io/blog/
created: '2025-03-01'
description: Foodspark is a data-as-a-service platform that delivers real-time grocery, restaurant, and food-delivery data extracted from 100+ platforms including DoorDash, Uber Eats, Grubhub, Instacart, McDonald's, Starbucks, and many others. Foodspark sells access to curated food and grocery datasets rather than a publicly documented self-serve API.
finops:
- name: Foodspark Finops
  service_category: Data-as-a-Service
  slug: foodspark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foodspark.png
layout: provider
modified: '2026-06-02'
name: Foodspark
nav: Providers
network: true
overview: 'Foodspark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Food, Groceries, Menus, and Restaurant.


  Foodspark''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Foodspark Plans Pricing
  plan_count: 1
  slug: foodspark-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Foodspark Rate Limits
  slug: foodspark-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foodspark/refs/heads/main/screenshots/foodspark-2026-06-20T181412.png
security:
- kind: domain-security
  name: Foodspark Domain Security
  slug: foodspark-domain-security
  summary_line: TLSv1.3 · DMARC
slug: foodspark
tags:
- Data
- Food
- Groceries
- Menus
- Restaurant
- Food Delivery
- Web Scraping
website: https://www.foodspark.io/
---
