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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Nuvemshop Agentic Access
  operation_count: 56
  slug: nuvemshop-agentic-access
  summary_line: 56 operations · 33 acting
api_count: 10
apis:
- description: Hierarchical catalog categories.
  name: Nuvemshop / Tiendanube Categories API
  slug: nuvemshop-categories-api
- description: Discount coupons.
  name: Nuvemshop / Tiendanube Coupons API
  slug: nuvemshop-coupons-api
- description: Registered customer accounts.
  name: Nuvemshop / Tiendanube Customers API
  slug: nuvemshop-customers-api
- description: Customer purchases and their lifecycle.
  name: Nuvemshop / Tiendanube Orders API
  slug: nuvemshop-orders-api
- description: Images attached to a product.
  name: Nuvemshop / Tiendanube Product Images API
  slug: nuvemshop-product-images-api
- description: Option combinations (size, color, etc.) owned by a product.
  name: Nuvemshop / Tiendanube Product Variants API
  slug: nuvemshop-product-variants-api
- description: Items for sale in the store.
  name: Nuvemshop / Tiendanube Products API
  slug: nuvemshop-products-api
- description: Custom JavaScript injected into the storefront.
  name: Nuvemshop / Tiendanube Scripts API
  slug: nuvemshop-scripts-api
- description: Store settings and metadata.
  name: Nuvemshop / Tiendanube Store API
  slug: nuvemshop-store-api
- description: Event notification subscriptions.
  name: Nuvemshop / Tiendanube Webhooks API
  slug: nuvemshop-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Nuvemshop / Tiendanube Admin API
  slug: open-nuvemshop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuvemshop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvemshop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuvemshop-authentication.yml
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
  url: https://www.tiendanube.com
- group: docs
  title: ''
  type: Documentation
  url: https://tiendanube.github.io/api-documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/nuvemshop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nuvemshop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nuvemshop-finops.yml
created: '2026-07-12'
description: Nuvemshop (Tiendanube in Spanish-speaking markets) is the leading Latin American e-commerce platform, powering online stores for merchants across Brazil, Argentina, Mexico, Chile, and Colombia. Its public REST Admin API lets apps and integrations manage products, variants, images, categories, orders, customers, coupons, scripts, webhooks, and store settings on a per-store basis. Apps authenticate with OAuth 2 (authorization code grant) and pass a non-expiring access token in a non-standard `Authentication` header (lowercase bearer prefix) along with a required `User-Agent`. The API is store-scoped - every path is prefixed with the store id - and is rate limited with a per-store leaky bucket.
finops:
- name: Nuvemshop Finops
  service_category: E-commerce Platform (SaaS)
  slug: nuvemshop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuvemshop.png
layout: provider
modified: '2026-07-12'
name: Nuvemshop / Tiendanube
nav: Providers
network: true
overview: 'Nuvemshop / Tiendanube publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Coupons API, Customers API, and 7 more. Tagged areas include E-commerce, Online Store, Latin America, Brazil, and Argentina.


  Nuvemshop / Tiendanube''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Nuvemshop Plans Pricing
  plan_count: 6
  slug: nuvemshop-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 4
  name: Nuvemshop Rate Limits
  slug: nuvemshop-rate-limits
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Nuvemshop Authentication
  slug: nuvemshop-authentication
  summary_line: apiKey/oauth2 · 1 scheme
- kind: domain-security
  name: Nuvemshop Domain Security
  slug: nuvemshop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nuvemshop
tags:
- E-commerce
- Online Store
- Latin America
- Brazil
- Argentina
- Storefront
- Products
- Orders
- Merchants
- Webhooks
- SaaS
website: https://www.tiendanube.com
---
