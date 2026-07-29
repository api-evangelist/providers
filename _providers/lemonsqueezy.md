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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Lemonsqueezy Agentic Access
  operation_count: 56
  slug: lemonsqueezy-agentic-access
  summary_line: 56 operations · 19 acting
api_count: 19
apis:
- description: The Checkouts API from Lemon Squeezy — 2 operation(s) for checkouts.
  name: Lemon Squeezy Checkouts API
  slug: lemonsqueezy-checkouts-api
- description: The Customers API from Lemon Squeezy — 2 operation(s) for customers.
  name: Lemon Squeezy Customers API
  slug: lemonsqueezy-customers-api
- description: The Discount Redemptions API from Lemon Squeezy — 2 operation(s) for discount redemptions.
  name: Lemon Squeezy Discount Redemptions API
  slug: lemonsqueezy-discount-redemptions-api
- description: The Discounts API from Lemon Squeezy — 2 operation(s) for discounts.
  name: Lemon Squeezy Discounts API
  slug: lemonsqueezy-discounts-api
- description: The Files API from Lemon Squeezy — 2 operation(s) for files.
  name: Lemon Squeezy Files API
  slug: lemonsqueezy-files-api
- description: The License API API from Lemon Squeezy — 3 operation(s) for license api.
  name: Lemon Squeezy License API API
  slug: lemonsqueezy-license-api-api
- description: The License Key Instances API from Lemon Squeezy — 2 operation(s) for license key instances.
  name: Lemon Squeezy License Key Instances API
  slug: lemonsqueezy-license-key-instances-api
- description: The License Keys API from Lemon Squeezy — 2 operation(s) for license keys.
  name: Lemon Squeezy License Keys API
  slug: lemonsqueezy-license-keys-api
- description: The Order Items API from Lemon Squeezy — 2 operation(s) for order items.
  name: Lemon Squeezy Order Items API
  slug: lemonsqueezy-order-items-api
- description: The Orders API from Lemon Squeezy — 4 operation(s) for orders.
  name: Lemon Squeezy Orders API
  slug: lemonsqueezy-orders-api
- description: The Prices API from Lemon Squeezy — 2 operation(s) for prices.
  name: Lemon Squeezy Prices API
  slug: lemonsqueezy-prices-api
- description: The Products API from Lemon Squeezy — 2 operation(s) for products.
  name: Lemon Squeezy Products API
  slug: lemonsqueezy-products-api
- description: The Stores API from Lemon Squeezy — 2 operation(s) for stores.
  name: Lemon Squeezy Stores API
  slug: lemonsqueezy-stores-api
- description: The Subscription Invoices API from Lemon Squeezy — 3 operation(s) for subscription invoices.
  name: Lemon Squeezy Subscription Invoices API
  slug: lemonsqueezy-subscription-invoices-api
- description: The Subscription Items API from Lemon Squeezy — 3 operation(s) for subscription items.
  name: Lemon Squeezy Subscription Items API
  slug: lemonsqueezy-subscription-items-api
- description: The Subscriptions API from Lemon Squeezy — 2 operation(s) for subscriptions.
  name: Lemon Squeezy Subscriptions API
  slug: lemonsqueezy-subscriptions-api
- description: The Usage Records API from Lemon Squeezy — 2 operation(s) for usage records.
  name: Lemon Squeezy Usage Records API
  slug: lemonsqueezy-usage-records-api
- description: The Variants API from Lemon Squeezy — 2 operation(s) for variants.
  name: Lemon Squeezy Variants API
  slug: lemonsqueezy-variants-api
- description: The Webhooks API from Lemon Squeezy — 2 operation(s) for webhooks.
  name: Lemon Squeezy Webhooks API
  slug: lemonsqueezy-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: Lemon Squeezy API
  slug: open-lemonsqueezy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lemonsqueezy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonsqueezy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemonsqueezy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lmsqueezy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemonsqueezy
- group: company
  title: ''
  type: Website
  url: https://www.lemonsqueezy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lemonsqueezy.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/lemonsqueezy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lemonsqueezy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lemonsqueezy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lemonsqueezy.com/blog
created: '2026-06-21'
description: Lemon Squeezy is a merchant-of-record platform for selling digital products, software, SaaS subscriptions, and license keys. As merchant of record it handles global sales tax, VAT, payments, and compliance on the seller's behalf. The REST API at https://api.lemonsqueezy.com/v1 uses the JSON:API specification with Bearer API key authentication to manage stores, products, variants, prices, customers, orders, subscriptions, license keys, checkouts, discounts, and webhooks. Lemon Squeezy was acquired by Stripe in July 2024.
finops:
- name: Lemonsqueezy Finops
  service_category: Commerce and Payments
  slug: lemonsqueezy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemonsqueezy.png
layout: provider
modified: '2026-06-21'
name: Lemon Squeezy
nav: Providers
network: true
overview: 'Lemon Squeezy publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Checkouts API, Customers API, Discount Redemptions API, and 16 more. Tagged areas include Payments, Merchant of Record, Subscriptions, Digital Products, and SaaS.


  Lemon Squeezy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Lemonsqueezy Plans Pricing
  plan_count: 2
  slug: lemonsqueezy-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Lemonsqueezy Rate Limits
  slug: lemonsqueezy-rate-limits
score:
  band: thin
  composite: 31.2
  delta: -2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonsqueezy/refs/heads/main/screenshots/lemonsqueezy-2026-07-25T224849.png
security:
- kind: authentication
  name: Lemonsqueezy Authentication
  slug: lemonsqueezy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lemonsqueezy Domain Security
  slug: lemonsqueezy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lemonsqueezy
tags:
- Payments
- Merchant of Record
- Subscriptions
- Digital Products
- SaaS
- Sales Tax
website: https://www.lemonsqueezy.com
---
