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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Foxy Hypermedia API (hAPI) is a RESTful hypermedia API implementing HATEOAS design, giving developers complete control over Foxy store accounts. Supports managing stores, customers, transactions, '
  name: Foxy hAPI
  slug: foxycart-hapi
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foxycart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.foxy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.foxycart.com/v/2.0/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Foxy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foxycart.com
- group: company
  title: ''
  type: Blog
  url: https://www.foxy.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.foxy.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.foxy.io/
- group: other
  title: ''
  type: X
  url: https://x.com/foxycart
- group: commercial
  title: ''
  type: Plans
  url: plans/foxycart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/foxycart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/foxycart-finops.yml
created: '2026-06-13'
description: Foxy.io (formerly FoxyCart) is a developer-focused shopping cart and e-commerce platform providing a hosted hypermedia REST API (hAPI) for managing products, customers, subscriptions, transactions, and order workflows. The platform supports physical products, digital goods, subscriptions, donations, and services, and integrates with 100+ payment gateways including Stripe, PayPal, and Square. The API uses HATEOAS design with OAuth 2.0 authentication and has processed over $3 billion in transactions globally.
finops:
- name: Foxycart Finops
  service_category: ''
  slug: foxycart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foxycart.png
layout: provider
modified: '2026-06-13'
name: Foxy.io
nav: Providers
network: true
overview: 'Foxy.io publishes 1 API on the [APIs.io](https://apis.io/) network: Foxy hAPI. Tagged areas include E-Commerce, Shopping Cart, Subscriptions, Payments, and Transactions.


  Foxy.io''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Foxycart Plans Pricing
  plan_count: 4
  slug: foxycart-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 0
  name: Foxycart Rate Limits
  slug: foxycart-rate-limits
score:
  band: emerging
  composite: 26.8
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foxycart/refs/heads/main/screenshots/foxycart-2026-06-20T181505.png
security:
- kind: domain-security
  name: Foxycart Domain Security
  slug: foxycart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: foxycart
tags:
- E-Commerce
- Shopping Cart
- Subscriptions
- Payments
- Transactions
- Customers
- Digital Products
website: https://www.foxy.io/
---
