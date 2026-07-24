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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Bold Commerce Agentic Access
  operation_count: 29
  slug: bold-commerce-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 6
apis:
- description: Headless storefront checkout order operations.
  name: Bold Commerce Checkout API
  slug: bold-commerce-checkout-api
- description: Customer records tied to a shop.
  name: Bold Commerce Customers API
  slug: bold-commerce-customers-api
- description: Discounts, promotions, and dynamic pricing.
  name: Bold Commerce Price Rules API
  slug: bold-commerce-price-rules-api
- description: Product catalog for a shop.
  name: Bold Commerce Products API
  slug: bold-commerce-products-api
- description: Shop configuration and shop_identifier lookup.
  name: Bold Commerce Shops API
  slug: bold-commerce-shops-api
- description: Recurring orders, intervals, and subscription management.
  name: Bold Commerce Subscriptions API
  slug: bold-commerce-subscriptions-api
artifact_total: 14
collections:
- collection_type: open
  name: Bold Commerce API
  slug: open-bold-commerce
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bold-commerce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bold-commerce-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bold-commerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bold-commerce-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bold-commerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bold-commerce
- group: company
  title: ''
  type: Website
  url: https://boldcommerce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.boldcommerce.com
- group: commercial
  title: ''
  type: Plans
  url: plans/bold-commerce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bold-commerce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bold-commerce-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://boldcommerce.com/blog
created: '2026-07-10'
description: Bold Commerce builds modular e-commerce apps and headless commerce APIs for subscriptions, checkout, and pricing. Merchants and developers integrate Bold Subscriptions (recurring orders and branded customer portals), Bold Checkout (a headless, fully customizable checkout across Frontend, Backend, and Admin surfaces), and Bold Price Rules (discounts, promotions, and dynamic pricing), alongside supporting Products, Customers, and Shops APIs. Requests are made against api.boldcommerce.com and authenticated with an OAuth 2.0 access token (public integrations) or a scoped API access token (private integrations), passed as a Bearer token.
finops:
- name: Bold Commerce Finops
  service_category: E-Commerce and Commerce Platform
  slug: bold-commerce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bold-commerce.png
layout: provider
modified: '2026-07-10'
name: Bold Commerce
nav: Providers
network: true
overview: 'Bold Commerce publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Customers API, Price Rules API, and 3 more. Tagged areas include E-Commerce, Subscriptions, Checkout, Pricing, and Headless Commerce.


  Bold Commerce''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Bold Commerce Plans Pricing
  plan_count: 7
  slug: bold-commerce-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Bold Commerce Rate Limits
  slug: bold-commerce-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -0.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.0
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Bold Commerce Authentication
  slug: bold-commerce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bold Commerce Domain Security
  slug: bold-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bold Commerce Trust Center
  slug: bold-commerce-trust-center
  summary_line: PCI DSS, GDPR
slug: bold-commerce
tags:
- E-Commerce
- Subscriptions
- Checkout
- Pricing
- Headless Commerce
- Shopify
website: https://boldcommerce.com
---
