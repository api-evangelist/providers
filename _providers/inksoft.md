---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: Retrieve a web store's product catalog for building custom catalog and product-detail pages. Documented API 2 methods include GetProductCategoryList (all categories and subcategories in a store with c
  name: InkSoft Stores & Products API
  slug: inksoft-stores-products-api
- description: Browse and search the design and clip-art libraries that back the InkSoft Design Studio. Documented API 2 methods include GetStoreDesignCategoryList, GetStoreDesignList (designs in a category or match
  name: InkSoft Designs & Art API
  slug: inksoft-designs-art-api
- description: Drive an external cart and checkout flow against an InkSoft store. Documented API 2 methods include GetCart (cart contents with designs, product images, styles, sizes, and pricing), SaveCartItemNotes,
  name: InkSoft Cart & Orders API
  slug: inksoft-cart-orders-api
- description: Provision and link InkSoft user accounts for single sign-on. The documented CreateUser method creates an InkSoft account alongside your own user record and returns an InkSoft UserID, which you then pa
  name: InkSoft Users & SSO API
  slug: inksoft-users-sso-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inksoft-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InkSoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inksoft
- group: company
  title: ''
  type: Website
  url: https://www.inksoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.inksoft.com/hc/en-us/categories/8146540560795-InkSoft-API
- group: docs
  title: ''
  type: APIReference
  url: https://demo.inksoft.com/demo?Page=Api2
- group: commercial
  title: ''
  type: Plans
  url: plans/inksoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inksoft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inksoft-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inksoft.com/blog/
created: '2026-07-11'
description: InkSoft is a custom apparel e-commerce, online store, and design platform for screen printers, embroiderers, and print shops - part of the Inktavo family alongside Printful and GraphicsFlow. It provides hosted online stores, a browser-based Design Studio, product catalogs, art/clip-art libraries, and order management. InkSoft exposes a documented but license-gated developer surface, the InkSoft API 2, a per-store RPC-style HTTP API returning XML or JSON with CORS support. It lets partners and store owners build custom storefronts, product catalog pages, design galleries, cart and checkout flows, and single sign-on against a specific web store. API access requires an InkSoft Unlimited license and an additional monthly fee, so the reference is public but production use is account-gated.
finops:
- name: Inksoft Finops
  service_category: ''
  slug: inksoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inksoft.png
layout: provider
modified: '2026-07-11'
name: InkSoft
nav: Providers
network: true
overview: 'InkSoft publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Custom Apparel, E-Commerce, Online Stores, Print Shop, and Design Studio.


  InkSoft''s developer surface includes documentation, API reference, engineering blog, and 7 more developer resources.'
plans:
- name: Inksoft Plans Pricing
  plan_count: 3
  slug: inksoft-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Inksoft Rate Limits
  slug: inksoft-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inksoft/refs/heads/main/screenshots/inksoft-2026-07-25T222447.png
security:
- kind: domain-security
  name: Inksoft Domain Security
  slug: inksoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inksoft
tags:
- Custom Apparel
- E-Commerce
- Online Stores
- Print Shop
- Design Studio
- Screen Printing
- Product Catalog
website: https://www.inksoft.com
---
