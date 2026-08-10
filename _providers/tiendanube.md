---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tiendanube Agentic Access
  operation_count: 38
  slug: tiendanube-agentic-access
  summary_line: 38 operations · 20 acting
api_count: 12
apis:
- description: The Categories API from Tiendanube — 2 operation(s) for categories.
  name: Tiendanube Categories API
  slug: tiendanube-categories-api
- description: The Coupons API from Tiendanube — 2 operation(s) for coupons.
  name: Tiendanube Coupons API
  slug: tiendanube-coupons-api
- description: The Customers API from Tiendanube — 2 operation(s) for customers.
  name: Tiendanube Customers API
  slug: tiendanube-customers-api
- description: The Fulfillment Orders API from Tiendanube — 2 operation(s) for fulfillment orders.
  name: Tiendanube Fulfillment Orders API
  slug: tiendanube-fulfillment-orders-api
- description: The Orders API from Tiendanube — 4 operation(s) for orders.
  name: Tiendanube Orders API
  slug: tiendanube-orders-api
- description: The Payment Providers API from Tiendanube — 1 operation(s) for payment providers.
  name: Tiendanube Payment Providers API
  slug: tiendanube-payment-providers-api
- description: The Product Images API from Tiendanube — 1 operation(s) for product images.
  name: Tiendanube Product Images API
  slug: tiendanube-product-images-api
- description: The Product Variants API from Tiendanube — 2 operation(s) for product variants.
  name: Tiendanube Product Variants API
  slug: tiendanube-product-variants-api
- description: The Products API from Tiendanube — 2 operation(s) for products.
  name: Tiendanube Products API
  slug: tiendanube-products-api
- description: The Scripts API from Tiendanube — 1 operation(s) for scripts.
  name: Tiendanube Scripts API
  slug: tiendanube-scripts-api
- description: The Shipping Carriers API from Tiendanube — 1 operation(s) for shipping carriers.
  name: Tiendanube Shipping Carriers API
  slug: tiendanube-shipping-carriers-api
- description: The Webhooks API from Tiendanube — 2 operation(s) for webhooks.
  name: Tiendanube Webhooks API
  slug: tiendanube-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Tiendanube / Nuvemshop API
  slug: open-tiendanube
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiendanube-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tiendanube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiendanube-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiendanube-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TiendaNube
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiendanube
- group: company
  title: ''
  type: Website
  url: https://www.tiendanube.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tiendanube.github.io/api-documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/tiendanube-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiendanube-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tiendanube-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tiendanube.com/blog
created: '2026-07-01'
description: Tiendanube (branded Nuvemshop in Brazil) is the leading e-commerce platform for small and medium-sized businesses across Latin America. Its REST API lets partner applications manage a merchant's store data - products, variants, categories, orders, customers, coupons, webhooks, scripts, fulfillment orders, and payment/shipping providers - using OAuth 2.0 and a per-store authentication token.
finops:
- name: Tiendanube Finops
  service_category: E-commerce Platform
  slug: tiendanube-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiendanube.png
layout: provider
modified: '2026-07-01'
name: Tiendanube
nav: Providers
network: true
overview: 'Tiendanube publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Coupons API, Customers API, and 9 more. Tagged areas include E-commerce, Retail, Latin America, Storefront, and Products.


  Tiendanube''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Tiendanube Plans Pricing
  plan_count: 5
  slug: tiendanube-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Tiendanube Rate Limits
  slug: tiendanube-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tiendanube Authentication
  slug: tiendanube-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tiendanube Domain Security
  slug: tiendanube-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tiendanube Vulnerability Disclosure
  slug: tiendanube-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tiendanube
tags:
- E-commerce
- Retail
- Latin America
- Storefront
- Products
- Orders
website: https://www.tiendanube.com/
---
