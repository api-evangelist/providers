---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: Server-side API for generating signed payment requests that redirect customers to the LiqPay hosted checkout page. Supports one-time payments, donations, split payments, two-stage holds, and QR-code p
  name: LiqPay Checkout API
  slug: liqpay-checkout-api
- description: Server-to-server API for retrieving the current status and details of a payment by order ID. Returns action, amount, currency, payment status (success, failure, reversed, error), payment method, 3DS f
  name: LiqPay Payment Status API
  slug: liqpay-payment-status-api
- description: API for creating and managing recurring payment subscriptions. Supports daily, weekly, monthly, and yearly billing cycles. Merchants can create subscriptions using a card token, update subscription am
  name: LiqPay Subscriptions API
  slug: liqpay-subscriptions-api
- description: Server-to-server API for initiating full or partial refunds on previously completed payments. Refunds are returned to the original payment method (card or Privat24). Requires the original order ID and
  name: LiqPay Refunds API
  slug: liqpay-refunds-api
- description: API for generating and sending payment invoices to customers by email or phone number. Invoices include itemized goods lists, expiration dates, and selectable payment actions (pay, hold, subscribe, do
  name: LiqPay Invoice API
  slug: liqpay-invoice-api
- description: API for card-to-card (P2P) money transfers between individuals. Supports transfers by card number, card token, Privat24 account, mobile phone number, or recipient email. Settlement is near-instant for
  name: LiqPay P2P Transfers API
  slug: liqpay-p2p-transfers-api
- description: API for merchant-initiated payouts (credit transfers) to customer cards or accounts. Used for marketplace disbursements, cashback, and refund-style credit operations. Supports UAH, USD, and EUR.
  name: LiqPay Payouts API
  slug: liqpay-payouts-api
- description: Server-to-server callback notifications sent by LiqPay to the merchant server_url on payment events including successful payment, failure, chargeback, and reversal. Callback payloads are base64-encode
  name: LiqPay Webhooks (Callbacks)
  slug: liqpay-webhooks-callbacks
- description: Informational API for retrieving a full archive of accepted payments for the merchant account within a specified date range. Used for reconciliation, reporting, and accounting.
  name: LiqPay Payment Archive API
  slug: liqpay-payment-archive-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liqpay-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.liqpay.ua/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.liqpay.ua/documentation/en
- group: start
  title: ''
  type: Sandbox
  url: https://www.liqpay.ua/documentation/en
- group: auth
  title: ''
  type: Authentication
  url: https://www.liqpay.ua/documentation/en
- group: build
  title: ''
  type: SDKs
  url: https://github.com/liqpay
- group: build
  title: ''
  type: SDKs
  url: https://github.com/liqpay/sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/liqpay/sdk-python
- group: operate
  title: ''
  type: Status
  url: https://www.liqpay.ua/en/support
- group: operate
  title: ''
  type: Support
  url: https://www.liqpay.ua/en/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liqpay.ua/en/doc/informations
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/liqpay/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/liqpay/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/liqpay/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: LiqPay is a Ukrainian payment platform operated by PrivatBank that provides REST APIs for accepting card payments, creating hosted payment pages, processing subscriptions, managing refunds, sending invoices, and conducting card-to-card transfers. It supports Mastercard, Visa, Apple Pay, Google Pay, and Privat24 wallets across 120+ countries, with full fiscalization (RRO) support for Ukrainian merchants.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/liqpay.png
layout: provider
modified: '2026-06-13'
name: LiqPay
nav: Providers
network: true
overview: 'LiqPay publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Fintech, Ukraine, Cards, and Subscriptions.


  LiqPay''s developer surface includes developer portal, documentation, sandbox, authentication, status page, support, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 40
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 26.0
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Liqpay Domain Security
  slug: liqpay-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: liqpay
tags:
- Payments
- Fintech
- Ukraine
- Cards
- Subscriptions
- Invoicing
- P2P Transfers
- PrivatBank
website: https://www.liqpay.ua/en/developers
---
