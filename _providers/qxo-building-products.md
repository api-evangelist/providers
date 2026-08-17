---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: Enables customers to place material orders and track order status and deliveries within their own systems.
  name: QXO Order API
  slug: order-api
- description: Provides real-time pricing information for single or multiple QXO products to simplify the process of generating estimates.
  name: QXO Pricing API
  slug: pricing-api
- description: Provides access to customer account information including billing addresses, contacts, and other account details.
  name: QXO Account API
  slug: account-api
- description: Browse the QXO product catalog to access product details and check availability across multiple product hierarchies.
  name: QXO Product API
  slug: product-api
- description: Track material order status and receive delivery photos via email for project management.
  name: QXO Delivery Tracking API
  slug: delivery-tracking-api
- description: Provides access to invoices, payment status, and financial information.
  name: QXO Invoice API
  slug: invoice-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qxo-building-products-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qxoinc
- group: company
  title: ''
  type: Website
  url: https://www.qxo.com
- group: other
  title: ''
  type: Developer
  url: https://www.qxo.com/customapi
- group: start
  title: ''
  type: Signup
  url: https://go.qxo.com/qxoapi
created: '2026-03-21'
description: QXO is a publicly traded company focused on building a tech-forward leader in the building products distribution industry through acquisitions and operational improvements. QXO offers a suite of customer-facing APIs for ordering, pricing, account management, product catalog, delivery tracking, and invoicing.
finops:
- name: Qxo Building Products Finops
  service_category: API
  slug: qxo-building-products-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qxo-building-products.png
layout: provider
modified: '2026-04-28'
name: QXO Building Products
nav: Providers
network: true
overview: 'QXO Building Products publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Building Products, Distribution, B2B, Construction, and Fortune 500.


  QXO Building Products'' developer surface includes signup flow and 4 more developer resources.'
plans:
- name: Qxo Building Products Plans Pricing
  plan_count: 3
  slug: qxo-building-products-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Qxo Building Products Rate Limits
  slug: qxo-building-products-rate-limits
score:
  band: emerging
  composite: 13.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/screenshots/qxo-building-products-2026-06-20T192500.png
security:
- kind: domain-security
  name: Qxo Building Products Domain Security
  slug: qxo-building-products-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qxo-building-products
tags:
- Building Products
- Distribution
- B2B
- Construction
- Fortune 500
website: https://www.qxo.com
---
