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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-11'
api_count: 9
apis:
- description: The core REST API to process payments from customers across multiple payment methods including credit and debit cards, bank transfers (BLIK, EPS, iDEAL, Interac e-Transfer, ACH, SEPA), cash vouchers (
  name: Paysafe Payments API
  slug: paysafe-payments-api
- description: The 3D Secure v2 API provides strong customer authentication (SCA) for card transactions in line with PSD2 mandates. Merchants can initiate device fingerprinting and authentication flows, look up auth
  name: Paysafe 3D Secure API
  slug: paysafe-3ds-api
- description: A REST API for creating and managing recurring payment plans and customer subscriptions. Merchants define billing plans (interval, amount, currency) and subscribe customers to them. Supports full CRUD
  name: Paysafe Payment Scheduler API
  slug: paysafe-payment-scheduler-api
- description: A REST API that allows platforms and payment facilitators to create white-labelled merchant onboarding experiences. Supports creating, updating, and submitting merchant applications, uploading support
  name: Paysafe Applications API
  slug: paysafe-applications-api
- description: A REST API enabling platforms to embed digital wallet functionality directly into their products. Customers can add funds, spend, withdraw, and manage virtual and physical prepaid cards. Supports card
  name: Paysafe Embedded Wallets API
  slug: paysafe-embedded-wallets-api
- description: The PaysafeCard REST API enables online merchants to accept PaysafeCard prepaid voucher payments, payouts, and refunds. PaysafeCard is a global prepaid payment method available in 43+ countries, using
  name: PaysafeCard REST API
  slug: paysafe-paysafecard-api
- description: A REST API for payment facilitators to onboard sub-merchants for payment processing capabilities. Enables platforms acting as PayFacs to manage sub-merchant accounts under their master merchant accoun
  name: Paysafe PayFac Sub-merchant API
  slug: paysafe-payfac-submerchant-api
- description: A compliance API that screens prospective sub-merchants against the Mastercard MATCH Pro and Visa terminated merchant databases before onboarding. Helps payment facilitators identify high-risk merchan
  name: Paysafe Merchant Termination Inquiry API
  slug: paysafe-merchant-termination-inquiry-api
- description: A value-added REST API providing foreign exchange rate data to support multi-currency payment processing and dynamic currency conversion. Used in conjunction with the Payments API to present pricing t
  name: Paysafe FX Rates API
  slug: paysafe-fx-rates-api
artifact_total: 39
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paysafe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paysafe.com
- group: start
  title: ''
  type: Portal
  url: https://developer.paysafe.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paysafe.com/en/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paysafe.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.paysafe.com/en/support/reference-information/documentation-changelog/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.paysafe.com/en/support/reference-information/rest-api-architecture/
- group: other
  title: ''
  type: Dashboard
  url: https://merchant.paysafe.com/portal
- group: start
  title: ''
  type: Sandbox
  url: https://merchant.test.paysafe.com/portal/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paysafe.com/en/paysafegroup/comprehensive-privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.paysafe.com/en/information/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paysafegroup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paysafecard
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/paysafecard/api-documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/paysafe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paysafe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paysafe-finops.yml
created: '2026-06-13'
description: Paysafe is an integrated payment platform providing businesses with REST APIs for online payments, digital wallets, prepaid cards, pay-by-cash processing, and merchant account management. The platform supports a broad range of payment methods including credit and debit cards, ACH/SEPA direct debit, alternative payment methods, PaysafeCash, PaysafeCard vouchers, and embedded digital wallet solutions. Paysafe specializes in high-risk and regulated industries and offers white-label merchant onboarding, 3D Secure authentication, recurring payment scheduling, and FX rates for global commerce.
features:
- Single REST API integration for 100+ payment methods globally
- Supports cards, ACH, SEPA, BACS, EFT, iDEAL, BLIK, and more bank transfers
- PaysafeCash and PaysafeCard prepaid/cash-based payment methods
- Digital wallets including Apple Pay, Google Pay, PayPal, Skrill, Neteller, Venmo
- Crypto on-ramp for purchasing cryptocurrencies with fiat via Skrill
- 3D Secure v2 (PSD2 SCA compliant) authentication
- Recurring payment scheduling and subscription management
- White-label merchant onboarding via Applications API
- PayFac sub-merchant management and MATCH Pro screening
- Embedded digital wallet with prepaid card issuance (virtual and physical)
- Mobile wallet tokenization (Google Pay, Apple Pay, Samsung Pay)
- FX rates and multi-currency support
- Webhook notifications for transaction events
- Basic Access Authorization using Base64-encoded API key
- Test environment at api.test.paysafe.com
- Shopify and WooCommerce integrations available
- React Native, iOS, and Android mobile SDKs
- Server-side SDKs for Java and PHP
finops:
- name: Paysafe Finops
  service_category: Payments
  slug: paysafe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paysafe.png
layout: provider
modified: '2026-06-13'
name: Paysafe
nav: Providers
network: true
overview: 'Paysafe publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Digital Wallets, Prepaid Cards, Financial Services, and Fintech.


  Paysafe''s developer surface includes developer portal, documentation, changelog, authentication, sandbox, and 12 more developer resources.'
plans:
- name: Paysafe Plans Pricing
  plan_count: 5
  slug: paysafe-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Paysafe Rate Limits
  slug: paysafe-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paysafe/refs/heads/main/screenshots/paysafe-2026-06-20T191509.png
security:
- kind: domain-security
  name: Paysafe Domain Security
  slug: paysafe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paysafe
tags:
- Payments
- Digital Wallets
- Prepaid Cards
- Financial Services
- Fintech
- High-Risk Payments
use_cases:
- description: Accept payments across credit cards, debit cards, bank transfers, vouchers, and digital wallets through a single Payments API integration on web or mobile.
  name: Online Payment Acceptance
- description: Enable customers without bank accounts or cards to pay with PaysafeCash at retail locations or with PaysafeCard prepaid vouchers purchased at convenience stores.
  name: Pay-by-Cash and Vouchers
- description: Create subscription plans and manage customer billing cycles with the Payment Scheduler API for SaaS, media, and membership businesses.
  name: Recurring Billing and Subscriptions
- description: Build white-label merchant onboarding flows using the Applications API for PayFac and ISO platforms managing hundreds or thousands of sub-merchants.
  name: Platform Merchant Onboarding
- description: Embed digital wallets with stored value, prepaid card issuance, and crypto on-ramp into consumer apps and fintech platforms via the Embedded Wallets API.
  name: Embedded Wallet as a Service
- description: Process payments for high-risk and regulated industries (gaming, crypto, adult) with Paysafe's specialized risk and compliance infrastructure.
  name: High-Risk Merchant Processing
- description: Accept payments in 43+ countries using local payment methods and the FX Rates API for dynamic currency conversion and transparent pricing.
  name: International and Multi-Currency Commerce
- description: Add PSD2-compliant strong customer authentication to card transactions with the 3DS API, reducing fraud liability for EU and UK merchants.
  name: 3D Secure Authentication
website: https://www.paysafe.com
---
