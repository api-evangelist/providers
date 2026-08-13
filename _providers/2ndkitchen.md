---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-12'
api_count: 12
apis:
- description: The Authentication API from 2ndKitchen — 5 operation(s) for authentication.
  name: 2ndKitchen Authentication API
  slug: 2ndkitchen-authentication-api
- description: The Brand API from 2ndKitchen — 1 operation(s) for brand.
  name: 2ndKitchen Brand API
  slug: 2ndkitchen-brand-api
- description: The Business API from 2ndKitchen — 1 operation(s) for business.
  name: 2ndKitchen Business API
  slug: 2ndkitchen-business-api
- description: The Coupons API from 2ndKitchen — 1 operation(s) for coupons.
  name: 2ndKitchen Coupons API
  slug: 2ndkitchen-coupons-api
- description: The Deliveries API from 2ndKitchen — 1 operation(s) for deliveries.
  name: 2ndKitchen Deliveries API
  slug: 2ndkitchen-deliveries-api
- description: The Orders API from 2ndKitchen — 3 operation(s) for orders.
  name: 2ndKitchen Orders API
  slug: 2ndkitchen-orders-api
- description: The Payment API from 2ndKitchen — 1 operation(s) for payment.
  name: 2ndKitchen Payment API
  slug: 2ndkitchen-payment-api
- description: The Product API from 2ndKitchen — 4 operation(s) for product.
  name: 2ndKitchen Product API
  slug: 2ndkitchen-product-api
- description: The Products API from 2ndKitchen — 1 operation(s) for products.
  name: 2ndKitchen Products API
  slug: 2ndkitchen-products-api
- description: The Restaurant API from 2ndKitchen — 1 operation(s) for restaurant.
  name: 2ndKitchen Restaurant API
  slug: 2ndkitchen-restaurant-api
- description: The Restaurants API from 2ndKitchen — 1 operation(s) for restaurants.
  name: 2ndKitchen Restaurants API
  slug: 2ndkitchen-restaurants-api
- description: The Users API from 2ndKitchen — 4 operation(s) for users.
  name: 2ndKitchen Users API
  slug: 2ndkitchen-users-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/2ndkitchen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/2ndkitchen-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/2ndkitchen-data-model.yml
- group: company
  title: ''
  type: Website
  url: https://2ndkitchen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.2ndkitchen.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.2ndkitchen.com/
created: '2026-07-17'
description: 2ndKitchen was a Chicago-based food-technology startup (Techstars '18) that let businesses without an on-site kitchen — bars, breweries, hotels, and apartment communities — offer custom food menus sourced from nearby partner restaurants, handling ordering, pricing, payment, and delivery on their behalf. The company was acquired by REEF Technology in December 2021 and its 2ndkitchen.com domain now redirects to reeftechnology.com. This API Evangelist profile captures the set of nine microservice OpenAPI definitions still published on the legacy Swagger UI at docs.2ndkitchen.com (authentication, business, user, restaurant, order, pricing, payment, delivery, and indexing services), preserved here as a historical record of the platform's API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/2ndkitchen.png
layout: provider
modified: '2026-07-17'
name: 2ndKitchen
nav: Providers
network: true
overview: '2ndKitchen publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Brand API, Business API, and 9 more. Tagged areas include Company, Food Technology, Ghost Kitchen, Restaurant, and Food Delivery.


  2ndKitchen''s developer surface includes authentication, documentation, API reference, and 3 more developer resources.'
random_paper: 42
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 45.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/2ndkitchen/refs/heads/main/screenshots/2ndkitchen-2026-07-25T181134.png
security:
- kind: authentication
  name: 2Ndkitchen Authentication
  slug: 2ndkitchen-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 2Ndkitchen Domain Security
  slug: 2ndkitchen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 2ndkitchen
tags:
- Company
- Food Technology
- Ghost Kitchen
- Restaurant
- Food Delivery
- Ordering
- Payments
- Hospitality
- Techstars
- Acquired
website: https://2ndkitchen.com/
---
