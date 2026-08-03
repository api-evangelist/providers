---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 10
  human_in_the_loop: 0
  name: Loyverse Agentic Access
  operation_count: 32
  slug: loyverse-agentic-access
  summary_line: 32 operations · 10 acting
api_count: 15
apis:
- description: Merchandising categories for items.
  name: Loyverse Categories API
  slug: loyverse-categories-api
- description: Customer directory and loyalty program.
  name: Loyverse Customers API
  slug: loyverse-customers-api
- description: Discount definitions applied at the POS.
  name: Loyverse Discounts API
  slug: loyverse-discounts-api
- description: Employees who operate the POS.
  name: Loyverse Employees API
  slug: loyverse-employees-api
- description: Stock levels per variant and store.
  name: Loyverse Inventory API
  slug: loyverse-inventory-api
- description: Product catalog items, variants, SKUs, and pricing.
  name: Loyverse Items API
  slug: loyverse-items-api
- description: Merchant account information.
  name: Loyverse Merchants API
  slug: loyverse-merchants-api
- description: Item modifiers and options.
  name: Loyverse Modifiers API
  slug: loyverse-modifiers-api
- description: Configured payment types.
  name: Loyverse Payment Types API
  slug: loyverse-payment-types-api
- description: Registered POS devices per store.
  name: Loyverse POS Devices API
  slug: loyverse-pos-devices-api
- description: Sales receipts with line items, payments, taxes, and refunds.
  name: Loyverse Receipts API
  slug: loyverse-receipts-api
- description: Cash register shifts.
  name: Loyverse Shifts API
  slug: loyverse-shifts-api
- description: Merchant stores (locations).
  name: Loyverse Stores API
  slug: loyverse-stores-api
- description: Suppliers for inventory and purchasing.
  name: Loyverse Suppliers API
  slug: loyverse-suppliers-api
- description: Tax definitions applied to items.
  name: Loyverse Taxes API
  slug: loyverse-taxes-api
artifact_total: 21
collections:
- collection_type: open
  name: Loyverse API
  slug: open-loyverse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loyverse-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loyverse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loyverse
- group: company
  title: ''
  type: Website
  url: https://loyverse.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.loyverse.com/docs/
- group: start
  title: ''
  type: SignUp
  url: https://developer.loyverse.com
- group: commercial
  title: ''
  type: Plans
  url: plans/loyverse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loyverse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loyverse-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://help.loyverse.com/help/api-marketplace
- group: operate
  title: ''
  type: Community
  url: https://loyverse.town/clubs/2-loyverse-api/
- group: company
  title: ''
  type: Blog
  url: https://loyverse.com/blog
created: '2026-07-11'
description: Loyverse is a free point of sale (POS) platform for small and independent retail stores, cafes, bars, and restaurants, spanning the Loyverse POS app, Back Office dashboard, Kitchen Display, and Customer Display. The Loyverse API is a documented REST API at https://api.loyverse.com/v1.0 that exposes the same POS data - items and variants, categories, receipts (sales), customers and loyalty, inventory levels, stores, employees, payment types, taxes, discounts, modifiers, suppliers, POS devices, and shifts - so developers can build integrations for accounting, e-commerce order sync, inventory synchronization, loyalty and marketing, e-invoicing compliance, and custom reporting. Authentication is by personal access token (Bearer) or OAuth 2.0 authorization-code flow with scoped permissions, and webhooks push events such as receipts and inventory changes to consumer endpoints.
finops:
- name: Loyverse Finops
  service_category: Point of Sale and Commerce
  slug: loyverse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loyverse.png
layout: provider
modified: '2026-07-11'
name: Loyverse
nav: Providers
network: true
overview: 'Loyverse publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Discounts API, and 12 more. Tagged areas include Point of Sale, POS, Retail, Inventory, and Cafe and Restaurant.


  Loyverse''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 7 more developer resources.'
plans:
- name: Loyverse Plans Pricing
  plan_count: 4
  slug: loyverse-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 3
  name: Loyverse Rate Limits
  slug: loyverse-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 59.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loyverse/refs/heads/main/screenshots/loyverse-2026-07-25T225626.png
security:
- kind: authentication
  name: Loyverse Authentication
  slug: loyverse-authentication
  summary_line: http/oauth2 · 2 schemes
slug: loyverse
tags:
- Point of Sale
- POS
- Retail
- Inventory
- Cafe and Restaurant
- Loyalty
- Payments
- Commerce
website: https://loyverse.com
---
