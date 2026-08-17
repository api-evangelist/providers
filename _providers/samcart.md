---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Samcart Agentic Access
  operation_count: 16
  slug: samcart-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 6
apis:
- description: Individual charges, including failed charges.
  name: SamCart Charges API
  slug: samcart-charges-api
- description: Customers who have purchased in a marketplace.
  name: SamCart Customers API
  slug: samcart-customers-api
- description: Orders placed in a SamCart marketplace.
  name: SamCart Orders API
  slug: samcart-orders-api
- description: Products sold through SamCart checkout pages.
  name: SamCart Products API
  slug: samcart-products-api
- description: Refunds issued against charges.
  name: SamCart Refunds API
  slug: samcart-refunds-api
- description: Recurring subscriptions and payment plans.
  name: SamCart Subscriptions API
  slug: samcart-subscriptions-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SamCart Public Charges API
  slug: open-samcart-charges-api
- collection_type: open
  name: SamCart Public Charges Customers API
  slug: open-samcart-customers-api
- collection_type: open
  name: SamCart Public Charges Orders API
  slug: open-samcart-orders-api
- collection_type: open
  name: SamCart Public Charges Products API
  slug: open-samcart-products-api
- collection_type: open
  name: SamCart Public Charges Refunds API
  slug: open-samcart-refunds-api
- collection_type: open
  name: SamCart Public Charges Subscriptions API
  slug: open-samcart-subscriptions-api
- collection_type: open
  name: SamCart Public API
  slug: open-samcart
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/samcart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samcart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samcart-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/samcart
- group: company
  title: ''
  type: Website
  url: https://www.samcart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.samcart.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/samcart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/samcart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/samcart-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.samcart.com/blog
created: '2026-07-05'
description: SamCart is a checkout and e-commerce platform for selling digital products, courses, memberships, and physical goods directly to customers, built around a high-converting CheckoutOS checkout, one-click upsells, subscriptions, and a courses/members area. The SamCart Public API (v1) is a REST API at https://api.samcart.com/v1 that gives programmatic read access to a marketplace's orders, products, customers, subscriptions, charges, and refunds, plus write actions to cancel or schedule cancellation of subscriptions, refund charges, and update order custom fields. Authentication is via an sc-api API key header, and API access is provisioned by the SamCart Support team rather than fully self-serve.
finops:
- name: Samcart Finops
  service_category: E-Commerce and Checkout
  slug: samcart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samcart.png
layout: provider
modified: '2026-07-05'
name: SamCart
nav: Providers
network: true
overview: 'SamCart publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Charges API, Customers API, Orders API, and 3 more. Tagged areas include E-commerce, Checkout, Payments, Subscriptions, and Digital Products.


  SamCart''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Samcart Plans Pricing
  plan_count: 6
  slug: samcart-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Samcart Rate Limits
  slug: samcart-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.9
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
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Samcart Authentication
  slug: samcart-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Samcart Domain Security
  slug: samcart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: samcart
tags:
- E-commerce
- Checkout
- Payments
- Subscriptions
- Digital Products
- Courses
website: https://www.samcart.com/
---
