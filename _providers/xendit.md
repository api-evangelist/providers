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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Xendit Agentic Access
  operation_count: 20
  slug: xendit-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Retrieve account balances by type and currency.
  name: Xendit Balance API
  slug: xendit-balance-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Create and manage customer records.
  name: Xendit Customers API
  slug: xendit-customers-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Xendit-hosted invoices / payment links.
  name: Xendit Invoices API
  slug: xendit-invoices-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Unified Payments API - charge end users across all channels.
  name: Xendit Payment Requests API
  slug: xendit-payment-requests-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Save reusable payment methods for future and recurring charges.
  name: Xendit Payment Tokens API
  slug: xendit-payment-tokens-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Disburse funds to bank accounts and e-wallets.
  name: Xendit Payouts API
  slug: xendit-payouts-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: Refund successful payment requests.
  name: Xendit Refunds API
  slug: xendit-refunds-api
- baseURL: https://api.xendit.co
  baseurl_source: declared
  description: List and retrieve money-movement transactions.
  name: Xendit Transactions API
  slug: xendit-transactions-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xendit Balance API
  slug: open-xendit-balance-api
- collection_type: open
  name: Xendit Balance Customers API
  slug: open-xendit-customers-api
- collection_type: open
  name: Xendit Balance Invoices API
  slug: open-xendit-invoices-api
- collection_type: open
  name: Xendit Balance Payment Requests API
  slug: open-xendit-payment-requests-api
- collection_type: open
  name: Xendit Balance Payment Tokens API
  slug: open-xendit-payment-tokens-api
- collection_type: open
  name: Xendit Balance Payouts API
  slug: open-xendit-payouts-api
- collection_type: open
  name: Xendit Balance Refunds API
  slug: open-xendit-refunds-api
- collection_type: open
  name: Xendit Balance Transactions API
  slug: open-xendit-transactions-api
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
random_paper: 1
rate_limits:
- limit_count: 4
  name: Xendit Rate Limits
  slug: xendit-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xendit/refs/heads/main/screenshots/xendit-2026-09-02T171119.png
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
