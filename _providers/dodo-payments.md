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
- acting_count: 25
  human_in_the_loop: 0
  name: Dodo Payments Agentic Access
  operation_count: 49
  slug: dodo-payments-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 12
apis:
- description: The Checkout Sessions API from Dodo Payments — 2 operation(s) for checkout sessions.
  name: Dodo Payments Checkout Sessions API
  slug: dodo-payments-checkout-sessions-api
- description: The Customers API from Dodo Payments — 3 operation(s) for customers.
  name: Dodo Payments Customers API
  slug: dodo-payments-customers-api
- description: The Discounts API from Dodo Payments — 2 operation(s) for discounts.
  name: Dodo Payments Discounts API
  slug: dodo-payments-discounts-api
- description: The Disputes API from Dodo Payments — 2 operation(s) for disputes.
  name: Dodo Payments Disputes API
  slug: dodo-payments-disputes-api
- description: The License Keys API from Dodo Payments — 2 operation(s) for license keys.
  name: Dodo Payments License Keys API
  slug: dodo-payments-license-keys-api
- description: The Licenses API from Dodo Payments — 3 operation(s) for licenses.
  name: Dodo Payments Licenses API
  slug: dodo-payments-licenses-api
- description: The Payments API from Dodo Payments — 4 operation(s) for payments.
  name: Dodo Payments Payments API
  slug: dodo-payments-payments-api
- description: The Payouts API from Dodo Payments — 1 operation(s) for payouts.
  name: Dodo Payments Payouts API
  slug: dodo-payments-payouts-api
- description: The Products API from Dodo Payments — 4 operation(s) for products.
  name: Dodo Payments Products API
  slug: dodo-payments-products-api
- description: The Refunds API from Dodo Payments — 2 operation(s) for refunds.
  name: Dodo Payments Refunds API
  slug: dodo-payments-refunds-api
- description: The Subscriptions API from Dodo Payments — 4 operation(s) for subscriptions.
  name: Dodo Payments Subscriptions API
  slug: dodo-payments-subscriptions-api
- description: The Webhooks API from Dodo Payments — 4 operation(s) for webhooks.
  name: Dodo Payments Webhooks API
  slug: dodo-payments-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Dodo Payments API
  slug: open-dodo-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dodo-payments-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dodo-payments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dodo-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dodo-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dodopayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dodopayments
- group: company
  title: ''
  type: Website
  url: https://dodopayments.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dodopayments.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dodo-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dodo-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dodo-payments-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dodopayments.com/rss.xml
created: '2026-06-21'
description: Dodo Payments is a merchant-of-record (MoR) payments platform for global digital businesses. Its REST API handles one-time payments, subscriptions, checkout sessions, customers, products, discounts, license keys, payouts, refunds, disputes, and webhooks, while Dodo acts as the seller of record and calculates, collects, and remits sales tax, VAT, and GST across 190+ jurisdictions.
finops:
- name: Dodo Payments Finops
  service_category: Payments and Commerce
  slug: dodo-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dodo-payments.png
layout: provider
modified: '2026-06-21'
name: Dodo Payments
nav: Providers
network: true
overview: 'Dodo Payments publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Checkout Sessions API, Customers API, Discounts API, and 9 more. Tagged areas include Payments, Merchant of Record, Subscriptions, Billing, and Global Commerce.


  Dodo Payments'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Dodo Payments Plans Pricing
  plan_count: 3
  slug: dodo-payments-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Dodo Payments Rate Limits
  slug: dodo-payments-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Dodo Payments Authentication
  slug: dodo-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dodo Payments Domain Security
  slug: dodo-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dodo Payments Vulnerability Disclosure
  slug: dodo-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dodo-payments
tags:
- Payments
- Merchant of Record
- Subscriptions
- Billing
- Global Commerce
website: https://dodopayments.com
---
