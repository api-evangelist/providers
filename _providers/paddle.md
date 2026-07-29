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
- acting_count: 25
  human_in_the_loop: 0
  name: Paddle Agentic Access
  operation_count: 53
  slug: paddle-agentic-access
  summary_line: 53 operations · 25 acting
api_count: 14
apis:
- description: The Addresses API from Paddle — 2 operation(s) for addresses.
  name: Paddle Addresses API
  slug: paddle-addresses-api
- description: The Adjustments API from Paddle — 2 operation(s) for adjustments.
  name: Paddle Adjustments API
  slug: paddle-adjustments-api
- description: The Businesses API from Paddle — 2 operation(s) for businesses.
  name: Paddle Businesses API
  slug: paddle-businesses-api
- description: The Customers API from Paddle — 2 operation(s) for customers.
  name: Paddle Customers API
  slug: paddle-customers-api
- description: The Discounts API from Paddle — 1 operation(s) for discounts.
  name: Paddle Discounts API
  slug: paddle-discounts-api
- description: The Event Types API from Paddle — 1 operation(s) for event types.
  name: Paddle Event Types API
  slug: paddle-event-types-api
- description: The Events API from Paddle — 1 operation(s) for events.
  name: Paddle Events API
  slug: paddle-events-api
- description: The Notification Settings API from Paddle — 2 operation(s) for notification settings.
  name: Paddle Notification Settings API
  slug: paddle-notification-settings-api
- description: The Notifications API from Paddle — 3 operation(s) for notifications.
  name: Paddle Notifications API
  slug: paddle-notifications-api
- description: The Prices API from Paddle — 3 operation(s) for prices.
  name: Paddle Prices API
  slug: paddle-prices-api
- description: The Products API from Paddle — 2 operation(s) for products.
  name: Paddle Products API
  slug: paddle-products-api
- description: The Reports API from Paddle — 3 operation(s) for reports.
  name: Paddle Reports API
  slug: paddle-reports-api
- description: The Subscriptions API from Paddle — 8 operation(s) for subscriptions.
  name: Paddle Subscriptions API
  slug: paddle-subscriptions-api
- description: The Transactions API from Paddle — 3 operation(s) for transactions.
  name: Paddle Transactions API
  slug: paddle-transactions-api
artifact_total: 22
collections:
- collection_type: open
  name: Paddle API
  slug: open-paddle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paddle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paddle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paddle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paddle-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaddleHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paddle
- group: company
  title: ''
  type: Website
  url: https://www.paddle.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paddle.com
- group: commercial
  title: ''
  type: Plans
  url: plans/paddle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paddle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paddle-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.paddle.com/blog
created: '2026-06-21'
description: Paddle is a merchant-of-record billing platform for SaaS and digital products. The Paddle Billing API manages the full revenue lifecycle - products, prices, customers, subscriptions, transactions, invoices, adjustments, and discounts - while Paddle handles global sales tax, payment processing, fraud, and compliance on the seller's behalf.
finops:
- name: Paddle Finops
  service_category: Billing and Payments
  slug: paddle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paddle.png
layout: provider
modified: '2026-06-21'
name: Paddle
nav: Providers
network: true
overview: 'Paddle publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Adjustments API, Businesses API, and 11 more. Tagged areas include Billing, Payments, Subscriptions, Merchant of Record, and SaaS.


  Paddle''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Paddle Plans Pricing
  plan_count: 2
  slug: paddle-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 4
  name: Paddle Rate Limits
  slug: paddle-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -3.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paddle Authentication
  slug: paddle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paddle Domain Security
  slug: paddle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paddle Vulnerability Disclosure
  slug: paddle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: paddle
tags:
- Billing
- Payments
- Subscriptions
- Merchant of Record
- SaaS
website: https://www.paddle.com
---
