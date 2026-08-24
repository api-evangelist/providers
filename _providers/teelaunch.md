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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Teelaunch Agentic Access
  operation_count: 36
  slug: teelaunch-agentic-access
  summary_line: 36 operations · 12 acting
api_count: 11
apis:
- description: Account
  name: Teelaunch Account API
  slug: teelaunch-account-api
- description: Account Payment
  name: Teelaunch Account Payment API
  slug: teelaunch-account-payment-api
- description: Account Settings
  name: Teelaunch Account Settings API
  slug: teelaunch-account-settings-api
- description: Blank
  name: Teelaunch Blank API
  slug: teelaunch-blank-api
- description: Blank Category
  name: Teelaunch Blank Category API
  slug: teelaunch-blank-category-api
- description: Orders
  name: Teelaunch Orders API
  slug: teelaunch-orders-api
- description: Platform Store Product Variants
  name: Teelaunch Platform Store Product Variants API
  slug: teelaunch-platform-store-product-variants-api
- description: Platform Store Products
  name: Teelaunch Platform Store Products API
  slug: teelaunch-platform-store-products-api
- description: Platform Stores
  name: Teelaunch Platform Stores API
  slug: teelaunch-platform-stores-api
- description: Platforms
  name: Teelaunch Platforms API
  slug: teelaunch-platforms-api
- description: Products
  name: Teelaunch Products API
  slug: teelaunch-products-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: teelaunch Account API
  slug: open-teelaunch-account-api
- collection_type: open
  name: teelaunch Account Account Payment API
  slug: open-teelaunch-account-payment-api
- collection_type: open
  name: teelaunch Account Account Settings API
  slug: open-teelaunch-account-settings-api
- collection_type: open
  name: teelaunch Account Blank API
  slug: open-teelaunch-blank-api
- collection_type: open
  name: teelaunch Account Blank Category API
  slug: open-teelaunch-blank-category-api
- collection_type: open
  name: teelaunch Account Orders API
  slug: open-teelaunch-orders-api
- collection_type: open
  name: teelaunch Account Platform Store Product Variants API
  slug: open-teelaunch-platform-store-product-variants-api
- collection_type: open
  name: teelaunch Account Platform Store Products API
  slug: open-teelaunch-platform-store-products-api
- collection_type: open
  name: teelaunch Account Platform Stores API
  slug: open-teelaunch-platform-stores-api
- collection_type: open
  name: teelaunch Account Platforms API
  slug: open-teelaunch-platforms-api
- collection_type: open
  name: teelaunch Account Products API
  slug: open-teelaunch-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teelaunch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teelaunch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teelaunch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teelaunch
- group: company
  title: ''
  type: Website
  url: https://teelaunch.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.teelaunch.com/documentation
- group: auth
  title: ''
  type: Authentication
  url: https://support.teelaunch.com/portal/en/kb/articles/api-token
- group: commercial
  title: ''
  type: Plans
  url: plans/teelaunch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teelaunch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/teelaunch-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.teelaunch.com
created: '2026-07-11'
description: Teelaunch is a print-on-demand (POD) platform that lets creators design, produce, and dropship custom products - apparel, drinkware, jewelry, home goods, tech accessories, and more - through connected sales channels like Shopify, Etsy, and BigCommerce. Beyond its storefront apps, Teelaunch publishes a documented public REST API (base https://api.teelaunch.com/api/v1, Bearer/JWT auth) that lets developers and high-volume merchants automate the full POD workflow - reading the blank product catalog, creating products, submitting and managing orders, and retrieving shipment tracking - independent of any storefront app.
finops:
- name: Teelaunch Finops
  service_category: Ecommerce and Print-on-Demand Fulfillment
  slug: teelaunch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teelaunch.png
layout: provider
modified: '2026-07-11'
name: Teelaunch
nav: Providers
network: true
overview: 'Teelaunch publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Payment API, Account Settings API, and 8 more. Tagged areas include Print on Demand, POD, E-Commerce, Fulfillment, and Dropshipping.


  Teelaunch''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Teelaunch Plans Pricing
  plan_count: 2
  slug: teelaunch-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Teelaunch Rate Limits
  slug: teelaunch-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Teelaunch Authentication
  slug: teelaunch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teelaunch Domain Security
  slug: teelaunch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teelaunch
tags:
- Print on Demand
- POD
- E-Commerce
- Fulfillment
- Dropshipping
- Order
- Shipping
website: https://teelaunch.com
---
