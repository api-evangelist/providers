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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Now Payments Agentic Access
  operation_count: 12
  slug: now-payments-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 10
apis:
- description: 'Bulk cryptocurrency payout API enabling merchants to initiate thousands of transactions to different addresses in a single API call. Designed for payroll, affiliate rewards, and mass distribution. No '
  name: NOWPayments Mass Payouts API
  slug: nowpayments-mass-payouts-api
- description: Subscription-based recurring crypto billing API that automates payment flows for SaaS and membership platforms, allowing merchants to charge customers on scheduled intervals in cryptocurrency.
  name: NOWPayments Recurring Payments API
  slug: nowpayments-recurring-payments-api
- description: Fund custody management API enabling limitless off-chain operations, sub-account creation, and controlled fund management for B2B flows and platform operators managing multiple merchant wallets.
  name: NOWPayments Custody API
  slug: nowpayments-custody-api
- description: JWT authentication for mass payouts
  name: NOWPayments Authentication API
  slug: now-payments-authentication-api
- description: Supported cryptocurrency listings
  name: NOWPayments Currencies API
  slug: now-payments-currencies-api
- description: Price estimation and minimum amounts
  name: NOWPayments Estimates API
  slug: now-payments-estimates-api
- description: Invoice creation for crypto payments
  name: NOWPayments Invoices API
  slug: now-payments-invoices-api
- description: Payment creation and management
  name: NOWPayments Payments API
  slug: now-payments-payments-api
- description: Mass payouts and balance management
  name: NOWPayments Payouts API
  slug: now-payments-payouts-api
- description: API health and availability
  name: NOWPayments Status API
  slug: now-payments-status-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/now-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/now-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/now-payments-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nowpayments.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nowpayments.io/help/api
- group: company
  title: ''
  type: Blog
  url: https://nowpayments.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nowpayments.io/pricing
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.nowpayments.io
- group: build
  title: ''
  type: PostmanCollection
  url: https://documenter.getpostman.com/view/7907941/S1a32n38
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/now-payments/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/now-payments/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/now-payments/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nowpayments.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nowpayments.io/privacy
- group: operate
  title: ''
  type: Contact
  url: https://nowpayments.io/contacts
- group: other
  title: ''
  type: Email
  url: mailto:support@nowpayments.io
created: '2026-06-13'
description: NOWPayments is a crypto payment gateway that enables businesses to accept 300+ cryptocurrencies, create payment invoices, process recurring subscriptions, and manage merchant mass payouts. Founded in 2019, the platform processes over 30 million transactions monthly with 99.99% uptime and supports automatic coin conversion and fiat settlements.
examples:
- key_count: 4
  name: Create Invoice
  slug: create-invoice
- key_count: 4
  name: Create Payment
  slug: create-payment
- key_count: 4
  name: Mass Payout
  slug: mass-payout
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/now-payments.png
json_schemas:
- name: Invoice
  property_count: 12
  slug: invoice
- name: Payment
  property_count: 16
  slug: payment
- name: Payout
  property_count: 4
  slug: payout
layout: provider
modified: '2026-06-13'
name: NOWPayments
nav: Providers
network: true
overview: 'NOWPayments publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Mass Payouts API, Authentication API, Currencies API, and 5 more. Tagged areas include Crypto Payments, Cryptocurrency, Payment Gateway, Invoicing, and Subscriptions.


  The NOWPayments catalog on APIs.io includes 1 Spectral governance ruleset.


  NOWPayments'' developer surface includes authentication, engineering blog, pricing, sandbox, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 51
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: NOWPayments API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: now-payments-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: -5.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.8
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 51.4
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
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/now-payments/refs/heads/main/screenshots/now-payments-2026-06-20T190442.png
security:
- kind: authentication
  name: Now Payments Authentication
  slug: now-payments-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Now Payments Domain Security
  slug: now-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: now-payments
tags:
- Crypto Payments
- Cryptocurrency
- Payment Gateway
- Invoicing
- Subscriptions
- Mass Payouts
- Bitcoin
- Ethereum
website: https://nowpayments.io
---
