---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Toss Payments Agentic Access
  operation_count: 17
  slug: toss-payments-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 8
apis:
- description: 'Brandpay is Toss Payments'' embeddable in-merchant easy-pay wallet, letting customers register payment methods once and reuse them. Method and customer status changes are pushed via the METHOD_UPDATED '
  name: Toss Payments Brandpay API
  slug: toss-payments-brandpay-api
- description: Recurring (automatic) payments via billing keys.
  name: Toss Payments Billing API
  slug: toss-payments-billing-api
- description: Korean cash receipt (현금영수증) issuance and cancellation.
  name: Toss Payments Cash Receipts API
  slug: toss-payments-cash-receipts-api
- description: Confirm, retrieve, and cancel payments.
  name: Toss Payments Payments API
  slug: toss-payments-payments-api
- description: Marketplace balance and seller payouts (v2).
  name: Toss Payments Payouts API
  slug: toss-payments-payouts-api
- description: Settlement queries and manual settlement requests.
  name: Toss Payments Settlements API
  slug: toss-payments-settlements-api
- description: Transaction ledger queries.
  name: Toss Payments Transactions API
  slug: toss-payments-transactions-api
- description: Per-order virtual bank account issuance.
  name: Toss Payments Virtual Accounts API
  slug: toss-payments-virtual-accounts-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toss Payments Core Billing API
  slug: open-toss-payments-billing-api
- collection_type: open
  name: Toss Payments Core Billing Cash Receipts API
  slug: open-toss-payments-cash-receipts-api
- collection_type: open
  name: Toss Core Billing Payments API
  slug: open-toss-payments-payments-api
- collection_type: open
  name: Toss Payments Core Billing Payouts API
  slug: open-toss-payments-payouts-api
- collection_type: open
  name: Toss Payments Core Billing Settlements API
  slug: open-toss-payments-settlements-api
- collection_type: open
  name: Toss Payments Core Billing Transactions API
  slug: open-toss-payments-transactions-api
- collection_type: open
  name: Toss Payments Core Billing Virtual Accounts API
  slug: open-toss-payments-virtual-accounts-api
- collection_type: open
  name: Toss Payments Core API
  slug: open-toss-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toss-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toss-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toss-payments-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tosspayments
- group: company
  title: ''
  type: Website
  url: https://www.tosspayments.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tosspayments.com/en
- group: commercial
  title: ''
  type: Plans
  url: plans/toss-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toss-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/toss-payments-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tosspayments.com/blog
created: '2026-07-12'
description: Toss Payments is a South Korean payment gateway (PG) operated by Viva Republica, the company behind the Toss super-app. Its REST API lets merchants accept and manage online payments across cards, Korean easy-pay wallets (Toss Pay, KakaoPay, Naver Pay), virtual accounts, bank transfer, and mobile-phone billing. The Core API (base https://api.tosspayments.com) covers payment confirmation and cancellation, recurring billing keys, virtual account issuance, cash receipts, transaction and settlement queries, and seller payouts, with asynchronous results delivered by webhooks. Authentication is HTTP Basic using a secret API key.
finops:
- name: Toss Payments Finops
  service_category: Payments and Financial Services
  slug: toss-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toss-payments.png
layout: provider
modified: '2026-07-12'
name: Toss Payments
nav: Providers
network: true
overview: 'Toss Payments publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Cash Receipts API, Payments API, and 4 more. Tagged areas include Payments, Payment Gateway, South Korea, Cards, and Easy Pay.


  Toss Payments'' developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Toss Payments Plans Pricing
  plan_count: 3
  slug: toss-payments-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Toss Payments Rate Limits
  slug: toss-payments-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 58.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Toss Payments Authentication
  slug: toss-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Toss Payments Domain Security
  slug: toss-payments-domain-security
  summary_line: TLSv1.3 · DMARC
slug: toss-payments
tags:
- Payments
- Payment Gateway
- South Korea
- Cards
- Easy Pay
- Virtual Account
- Billing
- Checkout
- Fintech
website: https://www.tosspayments.com
---
