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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/plans/qxo-building-products-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qxo-building-products-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/rate-limits/qxo-building-products-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qxo-building-products-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/finops/qxo-building-products-finops.yml
  title: ''
  type: FinOps
  url: finops/qxo-building-products-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/security/qxo-building-products-domain-security.yml
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
- has_sources: false
  method: generated
  name: Qxo Building Products Finops
  primary_unit: ''
  service_category: API
  slug: qxo-building-products-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qxo-building-products.png
layout: provider
modified: '2026-04-28'
name: QXO Building Products
nav: Providers
network: true
overview: 'QXO Building Products is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Building Products, Distribution, B2B, Construction, and Fortune 500.


  QXO Building Products'' developer surface includes signup flow and 7 more developer resources.'
plans:
- name: Qxo Building Products Plans Pricing
  plan_count: 3
  slug: qxo-building-products-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Qxo Building Products Rate Limits
  slug: qxo-building-products-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 7.9
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
