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
api_count: 4
apis:
- description: GraphQL queries for the dispensaries/retailers connected to your Dutchie Plus account - retailer metadata, address, hours, accepted order types (pickup/delivery), and pricing types (recreational/medic
  name: Dutchie Plus Retailers API
  slug: dutchie-plus-retailers-api
- description: The core headless-storefront query. `menu(filter, pagination)` returns a retailer's live product catalog - each Product carries brand, category, strainType, description, image, CBD/THC potency, and pr
  name: Dutchie Plus Menu API
  slug: dutchie-plus-menu-api
- description: GraphQL queries for a retailer's active specials, deals, and promotions - the discount programs surfaced on the menu that produce the special variant prices (specialPriceRec / specialPriceMed) returne
  name: Dutchie Plus Specials API
  slug: dutchie-plus-specials-api
- description: The stateful cart and order lifecycle via GraphQL mutations - `createCheckout`, `addItem`, `updateQuantity`, `removeItem`, and `updateCheckout` (order type / pricing type), plus the `checkout(id)` que
  name: Dutchie Plus Checkout API
  slug: dutchie-plus-checkout-api
artifact_total: 11
collections:
- collection_type: open
  name: Dutchie Plus GraphQL API
  slug: open-dutchie
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dutchie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dutchie-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetDutchie
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dutchie
- group: company
  title: ''
  type: Website
  url: https://dutchie.com
- group: docs
  title: ''
  type: Documentation
  url: https://plus.dutchie.com/plus/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/dutchie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dutchie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dutchie-finops.yml
created: '2026-07-03'
description: Dutchie is a cannabis retail technology platform providing point of sale, ecommerce, and payments for dispensaries. Its headless commerce product, Dutchie Plus, exposes a GraphQL API (endpoint https://plus.dutchie.com/plus/2021-07/graphql) that lets developers build fully custom, branded dispensary storefronts against Dutchie's ecommerce backend - querying retailer menus, products, variants, potency, and specials, and driving a stateful cart/checkout that respects cannabis compliance, inventory, taxes, and per-state rules. Requests are GraphQL POST operations authenticated with a per-retailer Bearer API key. Note - Dutchie has announced a 2026 sunset/deprecation of the Plus headless commerce API.
finops:
- name: Dutchie Finops
  service_category: Commerce and Retail
  slug: dutchie-finops
graphqls:
- description: Dutchie Plus is Dutchie's headless cannabis-commerce API. It lets developers build
  name: Dutchie Plus GraphQL API
  slug: dutchie-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dutchie.png
layout: provider
modified: '2026-07-03'
name: Dutchie
nav: Providers
network: true
overview: 'Dutchie publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cannabis, Dispensary, Retail, Ecommerce, and Point of Sale.


  Dutchie''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Dutchie Plans Pricing
  plan_count: 2
  slug: dutchie-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Dutchie Rate Limits
  slug: dutchie-rate-limits
score:
  band: emerging
  composite: 27.6
  delta: 5.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: domain-security
  name: Dutchie Domain Security
  slug: dutchie-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dutchie Vulnerability Disclosure
  slug: dutchie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dutchie
tags:
- Cannabis
- Dispensary
- Retail
- Ecommerce
- Point of Sale
- Headless Commerce
- GraphQL
- Menu
- Checkout
website: https://dutchie.com
---
