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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Xendit Agentic Access
  operation_count: 20
  slug: xendit-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 8
apis:
- description: Retrieve account balances by type and currency.
  name: Xendit Balance API
  slug: xendit-balance-api
- description: Create and manage customer records.
  name: Xendit Customers API
  slug: xendit-customers-api
- description: Xendit-hosted invoices / payment links.
  name: Xendit Invoices API
  slug: xendit-invoices-api
- description: Unified Payments API - charge end users across all channels.
  name: Xendit Payment Requests API
  slug: xendit-payment-requests-api
- description: Save reusable payment methods for future and recurring charges.
  name: Xendit Payment Tokens API
  slug: xendit-payment-tokens-api
- description: Disburse funds to bank accounts and e-wallets.
  name: Xendit Payouts API
  slug: xendit-payouts-api
- description: Refund successful payment requests.
  name: Xendit Refunds API
  slug: xendit-refunds-api
- description: List and retrieve money-movement transactions.
  name: Xendit Transactions API
  slug: xendit-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Xendit API
  slug: open-xendit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xendit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xendit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xendit-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xendit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xendit
- group: company
  title: ''
  type: Website
  url: https://www.xendit.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xendit.co
- group: commercial
  title: ''
  type: Plans
  url: plans/xendit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xendit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/xendit-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.xendit.co/en/blog/
created: '2026-07-12'
description: Xendit is a payments infrastructure provider for Southeast Asia, giving businesses in Indonesia, the Philippines, and the wider region a single REST API to accept payments, disburse funds, and manage money movement. The unified Payments API accepts virtual accounts, e-wallets (OVO, DANA, GoPay, ShopeePay, GCash, GrabPay, Maya), QR (QRIS / QR Ph), cards, direct debit, and retail outlets through Payment Requests and Payment Tokens; complementary APIs cover hosted Invoices, Payouts / disbursements, Balance, Transactions, Customers, and Refunds. All requests are authenticated with a secret API key over HTTP Basic against the base host https://api.xendit.co.
finops:
- name: Xendit Finops
  service_category: Payments and Financial Infrastructure
  slug: xendit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xendit.png
layout: provider
modified: '2026-07-12'
name: Xendit
nav: Providers
network: true
overview: 'Xendit publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Customers API, Invoices API, and 5 more. Tagged areas include Payments, Fintech, Payment Gateway, Southeast Asia, and Indonesia.


  Xendit''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Xendit Plans Pricing
  plan_count: 2
  slug: xendit-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 4
  name: Xendit Rate Limits
  slug: xendit-rate-limits
score:
  band: thin
  composite: 37.5
  delta: 2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Xendit Authentication
  slug: xendit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xendit Domain Security
  slug: xendit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xendit
tags:
- Payments
- Fintech
- Payment Gateway
- Southeast Asia
- Indonesia
- Philippines
- Disbursements
- E-Wallet
- Virtual Accounts
- Cards
- Financial Infrastructure
website: https://www.xendit.co
---
