---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Subbly Agentic Access
  operation_count: 21
  slug: subbly-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- description: 'Public Orders API for integrating Subbly orders directly with any third-party logistics (3PL) / fulfillment provider. Subbly states it will provide the Orders API documentation on request rather than '
  name: Subbly Orders API
  slug: subbly-orders-api
- description: In-app webhook platform that notifies external and internal services of Subbly events (order and subscription lifecycle) with configurable conditions and variables. Webhooks are configured in the Subb
  name: Subbly Webhooks
  slug: subbly-webhooks
- baseURL: https://api.subbly.example/v1
  baseurl_source: spec
  description: Cart and checkout operations (modeled from the SDK and SubblyCart.js).
  name: Subbly Cart API
  slug: subbly-cart-api
- baseURL: https://api.subbly.example/v1
  baseurl_source: spec
  description: Customer accounts, addresses, and payment methods (modeled from the SDK).
  name: Subbly Customers API
  slug: subbly-customers-api
- baseURL: https://api.subbly.example/v1
  baseurl_source: spec
  description: Storefront products and bundles (modeled from the SDK).
  name: Subbly Products API
  slug: subbly-products-api
- baseURL: https://api.subbly.example/v1
  baseurl_source: spec
  description: Customer subscriptions and preferences (modeled from the SDK).
  name: Subbly Subscriptions API
  slug: subbly-subscriptions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Subbly Storefront API (Modeled) Cart API
  slug: open-subbly-cart-api
- collection_type: open
  name: Subbly Storefront API (Modeled) Cart Customers API
  slug: open-subbly-customers-api
- collection_type: open
  name: Subbly Storefront API (Modeled) Cart Products API
  slug: open-subbly-products-api
- collection_type: open
  name: Subbly Storefront API (Modeled) Cart Subscriptions API
  slug: open-subbly-subscriptions-api
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
overview: 'Subbly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Customers API, Products API, and 1 more. Tagged areas include Subscription, Subscription Commerce, E-Commerce, Subscription Box, and Recurring Billing.


  Subbly''s developer surface includes authentication, documentation, SDKs, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Subbly Plans Pricing
  plan_count: 5
  slug: subbly-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Subbly Rate Limits
  slug: subbly-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/subbly/refs/heads/main/screenshots/subbly-2026-08-17T082145.png
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
- Subscription
- Subscription Commerce
- E-Commerce
- Subscription Box
- Recurring Billing
- Headless Commerce
- SDK
- Webhook
website: https://www.subbly.co/
---
