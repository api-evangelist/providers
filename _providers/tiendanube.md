---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tiendanube Agentic Access
  operation_count: 38
  slug: tiendanube-agentic-access
  summary_line: 38 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Categories API from Tiendanube — 2 operation(s) for categories.
  name: Tiendanube Categories API
  slug: tiendanube-categories-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Coupons API from Tiendanube — 2 operation(s) for coupons.
  name: Tiendanube Coupons API
  slug: tiendanube-coupons-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Customers API from Tiendanube — 2 operation(s) for customers.
  name: Tiendanube Customers API
  slug: tiendanube-customers-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Fulfillment Orders API from Tiendanube — 2 operation(s) for fulfillment orders.
  name: Tiendanube Fulfillment Orders API
  slug: tiendanube-fulfillment-orders-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Orders API from Tiendanube — 4 operation(s) for orders.
  name: Tiendanube Orders API
  slug: tiendanube-orders-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Payment Providers API from Tiendanube — 1 operation(s) for payment providers.
  name: Tiendanube Payment Providers API
  slug: tiendanube-payment-providers-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Product Images API from Tiendanube — 1 operation(s) for product images.
  name: Tiendanube Product Images API
  slug: tiendanube-product-images-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Product Variants API from Tiendanube — 2 operation(s) for product variants.
  name: Tiendanube Product Variants API
  slug: tiendanube-product-variants-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Products API from Tiendanube — 2 operation(s) for products.
  name: Tiendanube Products API
  slug: tiendanube-products-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Scripts API from Tiendanube — 1 operation(s) for scripts.
  name: Tiendanube Scripts API
  slug: tiendanube-scripts-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Shipping Carriers API from Tiendanube — 1 operation(s) for shipping carriers.
  name: Tiendanube Shipping Carriers API
  slug: tiendanube-shipping-carriers-api
- baseURL: https://api.tiendanube.com/v1/{store_id}
  baseurl_source: declared
  description: The Webhooks API from Tiendanube — 2 operation(s) for webhooks.
  name: Tiendanube Webhooks API
  slug: tiendanube-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tiendanube / Nuvemshop Categories API
  slug: open-tiendanube-categories-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Coupons API
  slug: open-tiendanube-coupons-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Customers API
  slug: open-tiendanube-customers-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Fulfillment Orders API
  slug: open-tiendanube-fulfillment-orders-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Orders API
  slug: open-tiendanube-orders-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Payment Providers API
  slug: open-tiendanube-payment-providers-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Product Images API
  slug: open-tiendanube-product-images-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Product Variants API
  slug: open-tiendanube-product-variants-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Products API
  slug: open-tiendanube-products-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Scripts API
  slug: open-tiendanube-scripts-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Shipping Carriers API
  slug: open-tiendanube-shipping-carriers-api
- collection_type: open
  name: Tiendanube / Nuvemshop Categories Webhooks API
  slug: open-tiendanube-webhooks-api
- collection_type: open
  name: Tiendanube / Nuvemshop API
  slug: open-tiendanube
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tiendanube-capability-edges.yml
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
overview: 'Tiendanube publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Coupons API, Customers API, and 9 more. Tagged areas include E-Commerce, Retail, Latin America, Storefront, and Product.


  Tiendanube''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Tiendanube Plans Pricing
  plan_count: 5
  slug: tiendanube-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Tiendanube Rate Limits
  slug: tiendanube-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiendanube/refs/heads/main/screenshots/tiendanube-2026-09-02T163724.png
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
- E-Commerce
- Retail
- Latin America
- Storefront
- Product
- Order
website: https://www.tiendanube.com/
---
