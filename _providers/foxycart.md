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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
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
overview: 'Foxy.io publishes 1 API on the [APIs.io](https://apis.io/) network: Foxy hAPI. Tagged areas include E-Commerce, Shopping Cart, Subscription, Payments, and Transaction.


  Foxy.io''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Foxycart Plans Pricing
  plan_count: 4
  slug: foxycart-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Foxycart Rate Limits
  slug: foxycart-rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 34.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Subscription
- Payments
- Transaction
- Customers
- Digital Products
website: https://www.foxy.io/
---
