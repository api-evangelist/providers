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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Ecwid Agentic Access
  operation_count: 23
  slug: ecwid-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 7
apis:
- description: JSON REST API for managing Ecwid store data including products, categories, orders, customers, discount coupons, payment and shipping methods, application data, and storefront settings. Requests are m
  name: Ecwid REST API
  slug: rest-api
- description: The Categories API from Ecwid by Lightspeed — 2 operation(s) for categories.
  name: Ecwid by Lightspeed Categories API
  slug: ecwid-categories-api
- description: The Customers API from Ecwid by Lightspeed — 2 operation(s) for customers.
  name: Ecwid by Lightspeed Customers API
  slug: ecwid-customers-api
- description: The Discount Coupons API from Ecwid by Lightspeed — 1 operation(s) for discount coupons.
  name: Ecwid by Lightspeed Discount Coupons API
  slug: ecwid-discount-coupons-api
- description: The Orders API from Ecwid by Lightspeed — 2 operation(s) for orders.
  name: Ecwid by Lightspeed Orders API
  slug: ecwid-orders-api
- description: The Products API from Ecwid by Lightspeed — 2 operation(s) for products.
  name: Ecwid by Lightspeed Products API
  slug: ecwid-products-api
- description: The Profile API from Ecwid by Lightspeed — 1 operation(s) for profile.
  name: Ecwid by Lightspeed Profile API
  slug: ecwid-profile-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ecwid REST Categories API
  slug: open-ecwid-categories-api
- collection_type: open
  name: Ecwid REST Categories Customers API
  slug: open-ecwid-customers-api
- collection_type: open
  name: Ecwid REST Categories Discount Coupons API
  slug: open-ecwid-discount-coupons-api
- collection_type: open
  name: Ecwid REST Categories Orders API
  slug: open-ecwid-orders-api
- collection_type: open
  name: Ecwid REST Categories Products API
  slug: open-ecwid-products-api
- collection_type: open
  name: Ecwid REST Categories Profile API
  slug: open-ecwid-profile-api
- collection_type: open
  name: Ecwid REST API
  slug: open-ecwid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ecwid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecwid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecwid-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecwid
- group: company
  title: ''
  type: Website
  url: https://www.ecwid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ecwid.com
- group: docs
  title: ''
  type: API Documentation
  url: https://api-docs.ecwid.com/reference/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ecwid.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://my.ecwid.com/cp/?source=signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ecwid.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ecwid
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ecwid.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.ecwid.com/blog/feed
created: '2026-05-11'
description: Ecwid by Lightspeed is a multi-channel e-commerce platform that lets merchants launch a storefront and sell across websites, social media (Instagram, TikTok, Facebook, Pinterest, Snapchat), online marketplaces, and in-person via point-of-sale. The platform handles centralized inventory and order management, automated marketing, payments, shipping, tax, and domain management. The Ecwid REST API exposes products, categories, orders, customers, payment and shipping methods, and storefront settings using OAuth 2.0 authentication with public (read-only) or private access tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecwid.png
layout: provider
modified: '2026-05-11'
name: Ecwid by Lightspeed
nav: Providers
network: true
overview: 'Ecwid by Lightspeed publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Discount Coupons API, and 3 more. Tagged areas include E-Commerce, Online Store, Storefront, Retail, and Point-of-Sale.


  Ecwid by Lightspeed''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 39.2
  delta: 4.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 52.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecwid/refs/heads/main/screenshots/ecwid-2026-06-20T180440.png
security:
- kind: authentication
  name: Ecwid Authentication
  slug: ecwid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ecwid Domain Security
  slug: ecwid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecwid
tags:
- E-Commerce
- Online Store
- Storefront
- Retail
- Point-of-Sale
- Multi-Channel Commerce
website: https://www.ecwid.com
---
