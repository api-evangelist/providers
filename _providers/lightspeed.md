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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: REST API for Lightspeed Retail X-Series point-of-sale system enabling integrations for sales operations, product management, inventory updates, loyalty handling, and webhooks for retail merchants.
  name: Lightspeed Retail X-Series API
  slug: retail-x-series
- description: REST API for Lightspeed Retail R-Series (formerly Vend) providing access to sales, inventory, customers, products, and reporting data for retail point-of-sale systems.
  name: Lightspeed Retail R-Series API
  slug: retail-r-series
- description: REST API for Lightspeed eCom (C-Series) e-commerce platform providing endpoints for products, orders, customers, shipments, payments, and inventory management. Requires Advanced or Professional subscr
  name: Lightspeed eCom API
  slug: ecom-c-series
- description: REST API for Lightspeed Restaurant K-Series POS system, enabling approved partners to build integrations for restaurant operations including menu management, orders, and payments.
  name: Lightspeed Restaurant K-Series API
  slug: restaurant-k-series
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightspeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lightspeedhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lightspeedhq.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lightspeedpos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightspeedcommerce
- group: company
  title: ''
  type: Blog
  url: https://www.lightspeedhq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lightspeedhq.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightspeedhq.com/
- group: other
  title: ''
  type: X
  url: https://x.com/LightspeedHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/lightspeed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightspeed-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lightspeed-finops.yml
created: 2026-06-13
description: Omnichannel commerce platform with REST APIs for retail and restaurant POS, inventory management, loyalty programs, and e-commerce integrations. Lightspeed serves retailers and restaurateurs with cloud-based point-of-sale systems, enabling custom integrations through APIs for sales, inventory, customers, orders, payments, and loyalty programs across multiple product lines including Retail X-Series, Retail R-Series, Restaurant K-Series, and eCom.
finops:
- name: Lightspeed Finops
  service_category: ''
  slug: lightspeed-finops
graphqls:
- description: Lightspeed is a commerce platform for retail, restaurant, and golf businesses. The API covers product catalog, inventory management, orders, customers, suppliers, purchase orders, payments, and multi-
  name: Lightspeed Commerce GraphQL API
  slug: lightspeed-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightspeed.png
layout: provider
modified: 2026-06-13
name: Lightspeed Commerce
nav: Providers
network: true
overview: 'Lightspeed Commerce publishes 1 API on the [APIs.io](https://apis.io/) network: Lightspeed Retail X-Series API. Tagged areas include Commerce, Point of Sale, POS, Retail, and Restaurant.


  Lightspeed Commerce''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Lightspeed Plans Pricing
  plan_count: 0
  slug: lightspeed-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 0
  name: Lightspeed Rate Limits
  slug: lightspeed-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: -1.6
  facets:
    commercial_clarity: 18.4
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightspeed/refs/heads/main/screenshots/lightspeed-2026-06-20T184527.png
security:
- kind: domain-security
  name: Lightspeed Domain Security
  slug: lightspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightspeed
tags:
- Commerce
- Point of Sale
- POS
- Retail
- Restaurant
- Inventory
- Loyalty
- Payments
- E-Commerce
- Omnichannel
website: https://www.lightspeedhq.com/
---
