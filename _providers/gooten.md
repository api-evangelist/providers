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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Gooten Agentic Access
  operation_count: 17
  slug: gooten-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 4
apis:
- description: Submit, retrieve, search, and update manufacturing orders.
  name: Gooten Orders API
  slug: gooten-orders-api
- description: Product templates and print-ready product (PRP) management.
  name: Gooten Print Assets API
  slug: gooten-print-assets-api
- description: Catalog products, per-region SKUs, supported countries and currencies.
  name: Gooten Products API
  slug: gooten-products-api
- description: Shipping option lookup and order price estimates for a cart.
  name: Gooten Shipping API
  slug: gooten-shipping-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gooten Orders API
  slug: open-gooten-orders-api
- collection_type: open
  name: Gooten Orders Print Assets API
  slug: open-gooten-print-assets-api
- collection_type: open
  name: Gooten Orders Products API
  slug: open-gooten-products-api
- collection_type: open
  name: Gooten Orders Shipping API
  slug: open-gooten-shipping-api
- collection_type: open
  name: Gooten API
  slug: open-gooten
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gooten-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gooten-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gooten-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gooten.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gooten
- group: docs
  title: ''
  type: Documentation
  url: https://www.gooten.com/api-documentation/getting-started/
- group: operate
  title: ''
  type: SupportCenter
  url: https://help.gooten.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/gooten-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gooten-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gooten-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gooten.com/blog/
created: '2026-07-11'
description: Gooten is a print-on-demand and global manufacturing and fulfillment platform for custom products - apparel, wall art, drinkware, home goods, and more. Its REST API (hosted at api.print.io, the platform Gooten was built on) lets ecommerce brands and developers browse the product catalog and per-region SKUs, retrieve print templates, create print-ready products from artwork, quote shipping and order prices, and submit and manage manufacturing orders routed across Gooten's distributed vendor network. Requests are authenticated with a public RecipeID and, for order and billing operations, a private PartnerBillingKey. There are no setup or monthly fees - you pay the per-order production and shipping cost only when an item is manufactured and shipped.
finops:
- name: Gooten Finops
  service_category: Manufacturing and Fulfillment
  slug: gooten-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gooten.png
layout: provider
modified: '2026-07-11'
name: Gooten
nav: Providers
network: true
overview: 'Gooten publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Print Assets API, Products API, and 1 more. Tagged areas include Print on Demand, Fulfillment, Manufacturing, Ecommerce, and Dropshipping.


  Gooten''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Gooten Plans Pricing
  plan_count: 2
  slug: gooten-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 3
  name: Gooten Rate Limits
  slug: gooten-rate-limits
score:
  band: thin
  composite: 36.3
  delta: -0.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gooten/refs/heads/main/screenshots/gooten-2026-07-25T220114.png
security:
- kind: authentication
  name: Gooten Authentication
  slug: gooten-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gooten Domain Security
  slug: gooten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gooten
tags:
- Print on Demand
- Fulfillment
- Manufacturing
- Ecommerce
- Dropshipping
- Custom Products
website: https://www.gooten.com
---
