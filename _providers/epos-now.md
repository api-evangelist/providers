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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Epos Now Agentic Access
  operation_count: 25
  slug: epos-now-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 6
apis:
- description: Categories that group products for the till and reporting.
  name: Epos Now Categories API
  slug: epos-now-categories-api
- description: Customer records for loyalty, accounts, and CRM.
  name: Epos Now Customers API
  slug: epos-now-customers-api
- description: Registered tills and API devices on the account.
  name: Epos Now Devices API
  slug: epos-now-devices-api
- description: The product catalog sold at the point of sale.
  name: Epos Now Products API
  slug: epos-now-products-api
- description: Product stock levels and stock control.
  name: Epos Now Stock API
  slug: epos-now-stock-api
- description: Sales records (orders) captured at the point of sale.
  name: Epos Now Transactions API
  slug: epos-now-transactions-api
artifact_total: 12
collections:
- collection_type: open
  name: EposNow HQ REST API
  slug: open-epos-now
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epos-now-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epos-now-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epos-now
- group: company
  title: ''
  type: Website
  url: https://www.eposnow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eposnowhq.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/epos-now-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epos-now-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/epos-now-finops.yml
created: '2026-07-11'
description: Epos Now is a cloud-based point of sale (POS) platform for retail and hospitality businesses, pairing countertop and mobile till hardware with a cloud Back Office for products, inventory, customers, staff, reporting, and payments. The EposNow HQ REST API lets developers programmatically read and write that cloud data - products, categories, transactions (sales), customers, stock, tax rates, and devices - using per-device Basic authentication, with Webhooks for event notifications. API access is enabled per registered API Device from the Back Office and is available through the Epos Now AppStore rather than sold as a standalone metered API product.
finops:
- name: Epos Now Finops
  service_category: Point of Sale and Commerce
  slug: epos-now-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epos-now.png
layout: provider
modified: '2026-07-11'
name: Epos Now
nav: Providers
network: true
overview: 'Epos Now publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Devices API, and 3 more. Tagged areas include Point of Sale, POS, Retail, Hospitality, and Payments.


  Epos Now''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Epos Now Plans Pricing
  plan_count: 4
  slug: epos-now-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 3
  name: Epos Now Rate Limits
  slug: epos-now-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epos-now/refs/heads/main/screenshots/epos-now-2026-07-25T213541.png
security:
- kind: authentication
  name: Epos Now Authentication
  slug: epos-now-authentication
  summary_line: http · 1 scheme
slug: epos-now
tags:
- Point of Sale
- POS
- Retail
- Hospitality
- Payments
- Inventory
- Commerce
- Ecommerce
website: https://www.eposnow.com/
---
