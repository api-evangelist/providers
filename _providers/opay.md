---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Opay Agentic Access
  operation_count: 5
  slug: opay-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 3
apis:
- description: 'The OPay Cashier API is the primary merchant payment API behind OPay Checkout. It exposes a hosted Express Checkout endpoint (cashier/create returning a cashierUrl), server-to-server payment creation '
  name: OPay Cashier API
  slug: opay-cashier-api
- description: Server-to-server payment creation across payment methods.
  name: OPay Payments API
  slug: opay-payments-api
- description: Refund creation and status.
  name: OPay Refunds API
  slug: opay-refunds-api
artifact_total: 43
collections:
- collection_type: open
  name: OPay Cashier API
  slug: open-opay-cashier-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.opayweb.com/
- group: start
  title: ''
  type: Portal
  url: https://documentation.opaycheckout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.opaycheckout.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.opaycheckout.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.opaycheckout.com/server-apis-overview
- group: auth
  title: ''
  type: Authentication
  url: https://documentation.opaycheckout.com/payment-authentication
- group: design
  title: ''
  type: Webhooks
  url: https://documentation.opaycheckout.com/payment-notifications
- group: design
  title: ''
  type: ErrorCodes
  url: https://documentation.opaycheckout.com/error-codes
- group: start
  title: ''
  type: Sandbox
  url: https://testapi.opaycheckout.com/api/v1/international
- group: start
  title: ''
  type: Signup
  url: https://merchant.opaycheckout.com/register
- group: start
  title: ''
  type: Console
  url: https://merchant.opaycheckout.com/login
- group: other
  title: ''
  type: Dashboard
  url: https://merchant.opaycheckout.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.opaycheckout.com/support/ticket
- group: other
  title: ''
  type: BusinessSolutions
  url: https://opaybusiness.opayweb.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opay
- group: build
  title: ''
  type: SDKs
  url: https://github.com/opay/lib.gateway.php
- group: build
  title: ''
  type: Plugin
  url: https://documentation.opaycheckout.com/woocommerce
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opayweb.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opayweb.com/terms-and-conditions
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OPay_NG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opayinc/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@OPayNigeria
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/OPayNigeria/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/opaynigeria/
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/ng/app/opay-mobile-money-app/id1500386156
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=team.opay.pay
created: '2026-05-24'
description: OPay is a Nigerian mobile money and fintech super-app operated by Blue Ridge Microfinance Bank (OPay Digital Services Limited) and majority-owned by Opera Limited with backing from SoftBank Vision Fund 2, Sequoia China, DragonBall Capital, and 9F Group. Launched in 2018 and headquartered in Lagos, OPay serves tens of millions of Nigerian consumers, merchants, and agents with wallet accounts, free interbank transfers, the OPay Debit Card, OWealth (daily-interest savings powered by OPay Microfinance Bank), bill payments, airtime/data top-ups, BNPL (OBuy / OPay Easy Buy), and the OPay POS / agent banking network. For developers and merchants, OPay exposes the OPay Cashier / OPay Checkout API — a REST API for accepting payments via 3DS bank cards, bank transfer, USSD, bank account, POS, OPay wallet QR, and reference codes, with hosted Express Checkout, server-to-server APIs, callback webhooks, refund and query operations, a PHP gateway SDK, and a WooCommerce plugin. Sandbox and
  production environments are available at testapi.opaycheckout.com and liveapi.opaycheckout.com, with HMAC-SHA512 signature authentication and per-merchant public/private key pairs issued from the OPay merchant dashboard.
features:
- description: Hosted, OPay-branded checkout page returned via cashier/create — customers complete payment on OPay-managed UI and are redirected back to the merchant returnUrl.
  name: Express Checkout
- description: Direct server-to-server card acceptance with 3-D Secure step-up (REDIRECT_3DS nextAction) for Nigerian and international card schemes.
  name: 3DS Card Payments
- description: Generate a dynamic virtual account (transferAccountNumber + transferBankName) per order; OPay reconciles inbound transfer and settles the merchant.
  name: Bank Transfer
- description: Customer pays by dialling a *USSD* code on their mobile phone; common in Nigeria where USSD banking is dominant.
  name: Bank USSD Payment
- description: Direct debit from the customer's bank account.
  name: Bank Account Payment
- description: Card-present payment from an OPay POS terminal.
  name: POS Payment
- description: Customer scans a QR code in the OPay app to pay from their wallet.
  name: OPay Wallet QR Payment
- description: Customer pays at an OPay agent using a reference code.
  name: Reference Code Payment
- description: Full or partial refunds with refund status query.
  name: Refunds
- description: Synchronous query for order status by merchant reference or OPay orderNo.
  name: Payment Status Query
- description: Server-to-server callback notifications on terminal transaction state changes (SUCCESS, FAIL, CLOSE), signed and retried by OPay.
  name: Callback Webhooks
- description: All non-cashier-create endpoints authenticate via a SHA-512 HMAC signature over the JSON body using the merchant's private key, plus a MerchantId header.
  name: HMAC-SHA512 Signature Authentication
- description: testapi.opaycheckout.com sandbox with trigger-error-by-amount testing.
  name: Sandbox Environment
- description: Drop-in WooCommerce plugin for WordPress storefronts.
  name: WooCommerce Plugin
- description: Official open-source PHP gateway library at github.com/opay/lib.gateway.php.
  name: PHP Gateway SDK
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opay.png
integrations:
- description: Official OPay WooCommerce plugin for WordPress.
  name: WooCommerce
- description: OPay was originally incubated inside Opera Limited and integrates with Opera browser payment flows.
  name: Opera Browser
- description: Card acquiring on the Visa network.
  name: Visa
- description: Card acquiring on the Mastercard network.
  name: Mastercard
- description: Card acquiring on the Nigerian Verve network.
  name: Verve
- description: Bank transfer rails and USSD banking via NIBSS.
  name: Nigerian Interbank Settlement System (NIBSS)
- description: Partner bank for virtual-account bank-transfer settlement (referenced in API responses).
  name: Wema Bank
layout: provider
modified: '2026-05-24'
name: OPay
nav: Providers
network: true
overview: 'OPay publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cashier API, Payments API, and Refunds API. Tagged areas include Payments, Mobile Money, Fintech, Super App, and Nigeria.


  OPay''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, sandbox, signup flow, and 22 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 38.8
  delta: -4.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 56.8
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opay/refs/heads/main/screenshots/opay-2026-06-20T190727.png
security:
- kind: authentication
  name: Opay Authentication
  slug: opay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opay Domain Security
  slug: opay-domain-security
  summary_line: TLSv1.3
slug: opay
solutions:
- description: Consumer super-app for wallet, transfers, OWealth savings, debit card, bill pay.
  name: OPay Personal App
- description: Merchant suite — Cashier API, POS terminals, agent banking, payouts.
  name: OPay Business
- description: Daily-interest savings powered by OPay Microfinance Bank Limited (CBN licensed, NDIC insured).
  name: OWealth
- description: Instant-issuance debit card accepted on ATM, POS, and online.
  name: OPay Debit Card
- description: Buy-now-pay-later product for OPay app users.
  name: OBuy / OPay Easy Buy
- description: POS terminal network for merchants and agents.
  name: OPay POS
tags:
- Payments
- Mobile Money
- Fintech
- Super App
- Nigeria
- Africa
- Wallet
- Savings
- BNPL
- Bank Transfer
- Card Payments
- USSD
- Agent Banking
- POS
- Bill Payments
- Airtime
- Cashier
- Checkout
- Merchant Acquiring
use_cases:
- description: Accept local payment methods (card, bank transfer, USSD, OPay wallet) on Nigerian e-commerce sites via Express Checkout or server APIs.
  name: Nigerian E-commerce Checkout
- description: Sell into Nigeria from international storefronts via OPay International APIs.
  name: Cross-Border Online Merchants
- description: Pay agents, riders, and sellers via OPay transfers.
  name: Marketplace Payouts
- description: Top up airtime/data and pay utility bills from within partner apps.
  name: Bill Payment & Airtime Aggregation
- description: Fund OPay wallets from cards or bank transfers.
  name: Wallet Top-Up
- description: Offer BNPL via OBuy / OPay Easy Buy at checkout.
  name: Buy-Now-Pay-Later Checkout
- description: Leverage the OPay agent network for cash deposits and withdrawals.
  name: Agent Banking & Cash-In/Cash-Out
- description: Card-present acceptance via OPay POS terminals.
  name: POS Acceptance
website: https://www.opayweb.com/
---
