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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'RESTful web service for managing all aspects of a Shift4Shop online store including products, categories, orders, customers, coupons, and store configuration. Supports GET, POST, PUT, and DELETE HTTP '
  name: Shift4Shop REST API
  slug: shift4shop-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shift4shop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shift4shop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apirest.3dcart.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/3dcart
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shift4shop
- group: company
  title: ''
  type: Blog
  url: https://blog.shift4shop.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shift4shop.com/plans.html
- group: operate
  title: ''
  type: StatusPage
  url: https://shift4payments.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Shift4Shop
- group: commercial
  title: ''
  type: Plans
  url: plans/shift4shop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shift4shop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shift4shop-finops.yml
created: 2026-06-13
description: Shift4Shop (formerly 3dcart) is an e-commerce platform providing a REST API for managing products, categories, orders, customers, coupons, and store configuration data. The API enables developers to build integrations, automate fulfillment, synchronize inventory, and manage the full lifecycle of an online store programmatically.
finops:
- name: Shift4Shop Finops
  service_category: ''
  slug: shift4shop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shift4shop.png
layout: provider
modified: 2026-06-13
name: Shift4Shop
nav: Providers
network: true
overview: 'Shift4Shop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Shopping Cart, Products, Orders, and Customers.


  Shift4Shop''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Shift4Shop Plans Pricing
  plan_count: 5
  slug: shift4shop-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Shift4Shop Rate Limits
  slug: shift4shop-rate-limits
score:
  band: emerging
  composite: 24.5
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 26.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shift4shop/refs/heads/main/screenshots/shift4shop-2026-06-20T193805.png
security:
- kind: domain-security
  name: Shift4Shop Domain Security
  slug: shift4shop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shift4shop
tags:
- E-Commerce
- Shopping Cart
- Products
- Orders
- Customers
- Categories
- Coupons
- Inventory
website: https://www.shift4shop.com/
---
