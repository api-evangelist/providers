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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Subbly Agentic Access
  operation_count: 21
  slug: subbly-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 6
apis:
- description: 'Public Orders API for integrating Subbly orders directly with any third-party logistics (3PL) / fulfillment provider. Subbly states it will provide the Orders API documentation on request rather than '
  name: Subbly Orders API
  slug: subbly-orders-api
- description: In-app webhook platform that notifies external and internal services of Subbly events (order and subscription lifecycle) with configurable conditions and variables. Webhooks are configured in the Subb
  name: Subbly Webhooks
  slug: subbly-webhooks
- description: Cart and checkout operations (modeled from the SDK and SubblyCart.js).
  name: Subbly Cart API
  slug: subbly-cart-api
- description: Customer accounts, addresses, and payment methods (modeled from the SDK).
  name: Subbly Customers API
  slug: subbly-customers-api
- description: Storefront products and bundles (modeled from the SDK).
  name: Subbly Products API
  slug: subbly-products-api
- description: Customer subscriptions and preferences (modeled from the SDK).
  name: Subbly Subscriptions API
  slug: subbly-subscriptions-api
artifact_total: 13
collections:
- collection_type: open
  name: Subbly Storefront API (Modeled)
  slug: open-subbly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/subbly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subbly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/subbly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/subbly
- group: company
  title: ''
  type: Website
  url: https://www.subbly.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.subbly.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.subbly.dev/
- group: build
  title: ''
  type: SDK
  url: https://docs.subbly.dev/reference/subbly-sdk/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.subbly.co/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/subbly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/subbly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/subbly-finops.yml
- group: operate
  title: ''
  type: SupportHelpCenter
  url: https://support.subbly.co/
- group: company
  title: ''
  type: Blog
  url: https://www.subbly.co/blog
created: '2026-07-10'
description: 'Subbly is a subscription-first commerce platform for building and running subscription boxes, memberships, and recurring-product businesses without code. Alongside the no-code storefront and merchant admin, Subbly ships a developer surface for headless and custom builds: the SubblyCart.js embeddable cart widget and the Subbly.js SDK (@subbly/sdk), a browser-side client that talks to Subbly''s REST backend to manage products, bundles, carts, checkout and purchase, customers, and subscriptions. Subbly also exposes a public Orders API for integrating directly with any 3PL / fulfillment provider (documentation is provided by Subbly on request), plus an in-app webhook platform for notifying external services of order and subscription events. Subbly does not publish a fully open, self-serve REST reference or an OpenAPI definition; the SDK abstracts the underlying endpoints, so the API surface modeled here is derived from the documented SDK operations and is flagged as modeled.'
finops:
- name: Subbly Finops
  service_category: Ecommerce and Subscription Commerce
  slug: subbly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subbly.png
layout: provider
modified: '2026-07-10'
name: Subbly
nav: Providers
network: true
overview: 'Subbly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Customers API, Products API, and 1 more. Tagged areas include Subscriptions, Subscription Commerce, Ecommerce, Subscription Box, and Recurring Billing.


  Subbly''s developer surface includes authentication, documentation, SDKs, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Subbly Plans Pricing
  plan_count: 5
  slug: subbly-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 3
  name: Subbly Rate Limits
  slug: subbly-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.2
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Subbly Authentication
  slug: subbly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Subbly Domain Security
  slug: subbly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: subbly
tags:
- Subscriptions
- Subscription Commerce
- Ecommerce
- Subscription Box
- Recurring Billing
- Headless Commerce
- SDK
- Webhooks
website: https://www.subbly.co/
---
