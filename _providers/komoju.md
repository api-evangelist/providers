---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
- acting_count: 16
  human_in_the_loop: 0
  name: Komoju Agentic Access
  operation_count: 28
  slug: komoju-agentic-access
  summary_line: 28 operations · 16 acting
api_count: 8
apis:
- description: Konbini payment barcodes for compatible convenience-store payments.
  name: KOMOJU Barcodes API
  slug: komoju-barcodes-api
- description: Store and manage customers with saved payment details for reuse.
  name: KOMOJU Customers API
  slug: komoju-customers-api
- description: Webhook events emitted by KOMOJU, queryable after the fact.
  name: KOMOJU Events API
  slug: komoju-events-api
- description: List the payment methods available to the authenticated merchant.
  name: KOMOJU Payment Methods API
  slug: komoju-payment-methods-api
- description: Create, capture, refund, cancel, and query payments across all payment methods.
  name: KOMOJU Payments API
  slug: komoju-payments-api
- description: Hosted checkout sessions that collect payment or customer details.
  name: KOMOJU Sessions API
  slug: komoju-sessions-api
- description: Recurring payments charged against a saved customer.
  name: KOMOJU Subscriptions API
  slug: komoju-subscriptions-api
- description: Tokenize payment details (short-term tokens and 3DS secure tokens).
  name: KOMOJU Tokens API
  slug: komoju-tokens-api
artifact_total: 15
collections:
- collection_type: open
  name: KOMOJU API
  slug: open-komoju
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/komoju-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komoju-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/komoju-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komoju
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/komoju
- group: company
  title: ''
  type: Website
  url: https://en.komoju.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.komoju.com
- group: commercial
  title: ''
  type: Plans
  url: plans/komoju-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/komoju-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/komoju-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://en.komoju.com/blog/
created: '2026-07-12'
description: KOMOJU is a Japan-focused global payment gateway operated by Degica. Its REST API lets web and e-commerce merchants accept a wide range of local and international payment methods through one interface - credit cards, convenience store (konbini) cash payments, bank transfer, Pay-easy (ATM), and e-money / mobile wallets such as PayPay, Merpay, au PAY, Rakuten Pay, LINE Pay, Alipay, and WeChat Pay - plus a hosted checkout (Sessions), tokenization, saved customers, subscriptions, and webhook events. Base URL is https://komoju.com/api/v1 with HTTP Basic authentication using a secret or publishable API key.
finops:
- name: Komoju Finops
  service_category: Payments and Financial Services
  slug: komoju-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/komoju.png
layout: provider
modified: '2026-07-12'
name: KOMOJU
nav: Providers
network: true
overview: 'KOMOJU publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Barcodes API, Customers API, Events API, and 5 more. Tagged areas include Payments, Payment Gateway, Japan, Konbini, and Cards.


  KOMOJU''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Komoju Plans Pricing
  plan_count: 3
  slug: komoju-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Komoju Rate Limits
  slug: komoju-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komoju/refs/heads/main/screenshots/komoju-2026-07-25T224141.png
security:
- kind: authentication
  name: Komoju Authentication
  slug: komoju-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Komoju Domain Security
  slug: komoju-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: komoju
tags:
- Payments
- Payment Gateway
- Japan
- Konbini
- Cards
- PayPay
- Bank Transfer
- E-Money
- Checkout
- Fintech
website: https://en.komoju.com
---
