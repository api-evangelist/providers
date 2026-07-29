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
- acting_count: 32
  human_in_the_loop: 0
  name: Paymob Agentic Access
  operation_count: 42
  slug: paymob-agentic-access
  summary_line: 42 operations · 32 acting
api_count: 18
apis:
- description: The v1 Intentions API is Paymob's modern entry point for payment acceptance. The merchant backend creates an intention with the secret key and an array of payment_methods (integration IDs or named met
  name: Paymob Intentions API
  slug: paymob-intentions-api
- description: The Subscriptions Module manages subscription plans (create, list, update, suspend, resume) and per-customer subscriptions billed against tokenised cards. Lifecycle operations cover suspend, resume, c
  name: Paymob Subscriptions API
  slug: paymob-subscriptions-api
- description: 'Tokenisation surface for the Paymob "Pay with saved card" flow. Lists and deletes tokenised cards and runs both customer-initiated (CIT) and merchant-initiated (MIT) transactions against saved tokens '
  name: Paymob Card Tokens API
  slug: paymob-card-tokens-api
- description: The Accounts API from Paymob — 1 operation(s) for accounts.
  name: Paymob Accounts API
  slug: paymob-accounts-api
- description: The Authentication API from Paymob — 3 operation(s) for authentication.
  name: Paymob Authentication API
  slug: paymob-authentication-api
- description: The Capture API from Paymob — 3 operation(s) for capture.
  name: Paymob Capture API
  slug: paymob-capture-api
- description: The Checkout API from Paymob — 1 operation(s) for checkout.
  name: Paymob Checkout API
  slug: paymob-checkout-api
- description: The Disbursement API from Paymob — 4 operation(s) for disbursement.
  name: Paymob Disbursement API
  slug: paymob-disbursement-api
- description: The Orders API from Paymob — 1 operation(s) for orders.
  name: Paymob Orders API
  slug: paymob-orders-api
- description: The Payment Keys API from Paymob — 1 operation(s) for payment keys.
  name: Paymob Payment Keys API
  slug: paymob-payment-keys-api
- description: The Payment Links API from Paymob — 2 operation(s) for payment links.
  name: Paymob Payment Links API
  slug: paymob-payment-links-api
- description: The Payments API from Paymob — 1 operation(s) for payments.
  name: Paymob Payments API
  slug: paymob-payments-api
- description: The Refund API from Paymob — 3 operation(s) for refund.
  name: Paymob Refund API
  slug: paymob-refund-api
- description: The Saved Card Payments API from Paymob — 2 operation(s) for saved card payments.
  name: Paymob Saved Card Payments API
  slug: paymob-saved-card-payments-api
- description: The Subscription Plans API from Paymob — 4 operation(s) for subscription plans.
  name: Paymob Subscription Plans API
  slug: paymob-subscription-plans-api
- description: The Topup API from Paymob — 2 operation(s) for topup.
  name: Paymob Topup API
  slug: paymob-topup-api
- description: The Transactions API from Paymob — 2 operation(s) for transactions.
  name: Paymob Transactions API
  slug: paymob-transactions-api
- description: The Void API from Paymob — 3 operation(s) for void.
  name: Paymob Void API
  slug: paymob-void-api
artifact_total: 99
collections:
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts API
  slug: postman-paymob-accounts-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Authentication API
  slug: postman-paymob-authentication-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Capture API
  slug: postman-paymob-capture-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Card Tokens API
  slug: postman-paymob-card-tokens-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Checkout API
  slug: postman-paymob-checkout-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Disbursement API
  slug: postman-paymob-disbursement-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Intentions API
  slug: postman-paymob-intentions-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Orders API
  slug: postman-paymob-orders-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Payment Keys API
  slug: postman-paymob-payment-keys-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Payment Links API
  slug: postman-paymob-payment-links-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Payments API
  slug: postman-paymob-payments-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Refund API
  slug: postman-paymob-refund-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Saved Card Payments API
  slug: postman-paymob-saved-card-payments-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Subscription Plans API
  slug: postman-paymob-subscription-plans-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Subscriptions API
  slug: postman-paymob-subscriptions-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Topup API
  slug: postman-paymob-topup-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Transactions API
  slug: postman-paymob-transactions-api
- collection_type: postman
  name: Paymob Accept Legacy (v2) Accounts Void API
  slug: postman-paymob-void-api
- collection_type: open
  name: Paymob Accept Legacy (v2) API
  slug: open-paymob-accept-api
- collection_type: open
  name: Paymob Card Tokens API
  slug: open-paymob-card-tokens-api
- collection_type: open
  name: Paymob Intentions API
  slug: open-paymob-intentions-api
- collection_type: open
  name: Paymob Payouts (Send) API
  slug: open-paymob-payouts-api
- collection_type: open
  name: Paymob Subscriptions API
  slug: open-paymob-subscriptions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paymob/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paymob-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paymob-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paymob-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://paymob.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.paymob.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.paymob.com/paymob-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.paymob.com/paymob-docs/getting-started/overview
- group: other
  title: ''
  type: Hub
  url: https://developers.paymob.com/hub/egypt
- group: other
  title: ''
  type: Hub
  url: https://developers.paymob.com/hub/sa
- group: other
  title: ''
  type: Hub
  url: https://paymob.ae
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paymob.com
- group: start
  title: ''
  type: Console
  url: https://accept.paymob.com/portal2/en/login
- group: start
  title: ''
  type: Signup
  url: https://accept.paymob.com/portal2/en/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paymob.com/en/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paymob.ae/en/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/paymob-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paymob-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: finops/paymob-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: rules/paymob-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: vocabulary/paymob-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/paymob-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaymobAccept
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/flutter_sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/paymob-reactnative-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/Android-SDK
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/Swift-iOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/accept-woocommerce
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/accept-magento2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/accept-opencart
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PaymobAccept/API-Postman-Collections
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaymobAccept/Paymob-Claude-Integration-Skill
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paymobcompany
- group: start
  title: ''
  type: Portal
  url: https://paymob.com/en/about-us
- group: operate
  title: ''
  type: Contact
  url: https://paymob.com/en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paymob.com/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paymob.com/en/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/paymob-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paymob-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: finops/paymob-finops.yml
created: '2026-05-24'
description: Paymob is a Cairo-headquartered, licensed payment infrastructure provider for the MENAP region. Serving roughly 390,000 merchants across Egypt, Saudi Arabia, the United Arab Emirates, Oman, and Pakistan (with Qatar announced), Paymob unifies card acquiring, regional mobile wallets (Vodafone Cash, Etisalat Cash, Orange Money, STC Pay, Oman Net, EasyPaisa, JazzCash), BNPL rails (Tabby, Tamara, valU, Souhoola, Forsa, Aman), Apple Pay, Google Pay, POS terminals, subscriptions, installments, marketplace payouts, mass disbursement (Paymob Send), and an end-to-end cashless commerce platform (Paymob Sync) behind a single Accept / Intentions API surface.
examples:
- key_count: 2
  name: Paymob Create Intention Example
  slug: paymob-create-intention-example
- key_count: 2
  name: Paymob Instant Cashin Example
  slug: paymob-instant-cashin-example
- key_count: 2
  name: Paymob Refund Transaction Example
  slug: paymob-refund-transaction-example
features:
- description: Hosted, fully-branded checkout supporting all regional payment methods from a single integration.
  name: Unified Checkout
- description: Embeddable checkout component for headless / custom-UI merchants.
  name: Pixel
- description: Modern backend-first intention creation with client_secret hand-off and multiple payment methods per intention.
  name: Intentions API (v1)
- description: V2 sharable payment links for social, email, SMS, and WhatsApp collection flows.
  name: Quick Link
- description: Plan and subscription management with suspend/resume/cancel and secondary card support.
  name: Subscriptions Module
- description: Tokenised card storage and one-click / merchant-initiated transactions.
  name: Saved Cards (CIT / MIT)
- description: Native routing to Tabby, Tamara, valU, Souhoola, Forsa, Aman across regional markets.
  name: Installments / BNPL routing
- description: Split-payment and downstream payout automation for marketplaces and platforms.
  name: Marketplace Payouts
- description: Mass disbursement to wallets, bank wallets, and bank cards with bulk and instant rails.
  name: Paymob Send (Payouts)
- description: End-to-end cashless commerce platform combining acceptance, payouts, and reconciliation.
  name: Paymob Sync
- description: Card data tokenised and stored in PCI-certified vaults; 3DS2 across regions.
  name: PCI-DSS certified infrastructure
- description: Integrated risk engine scoring transactions in real time.
  name: Machine-learning fraud detection
- description: Per-region Accept dashboards for transactions, settlements, refunds, payouts.
  name: Real-time merchant dashboards
- description: Local entities in Egypt, KSA, UAE, Oman, Pakistan (Qatar announced) for in-country settlement.
  name: Regional acquiring
- description: HMAC-signed callbacks for transaction lifecycle, disbursement status, and subscription events.
  name: Webhooks
- description: Native wallet integrations across MENAP markets.
  name: Apple Pay, Google Pay, STC Pay, Oman Net, EasyPaisa, JazzCash
finops:
- name: Paymob Finops
  service_category: Payments and Financial Services
  slug: paymob-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paymob.png
integrations:
- description: Official Accept Payments WooCommerce plugin.
  name: WooCommerce
- description: Official Magento 2 plugin for Accept Payments.
  name: Magento 2
- description: Official OpenCart plugin.
  name: OpenCart
- description: Paymob payment gateway available on Shopify.
  name: Shopify
- description: Paymob payment provider for Odoo 19.
  name: Odoo
- description: School fee payment integration.
  name: OpenEduCat
- description: Xero backend integration repository.
  name: Xero
- description: BNPL routing in KSA and UAE checkout.
  name: Tabby
- description: BNPL routing in KSA and UAE checkout.
  name: Tamara
- description: Installment and cash-collection partners across Egypt.
  name: valU / Souhoola / Forsa / Aman
- description: Native digital wallet acceptance across all live regions.
  name: Apple Pay / Google Pay
- description: National wallet acceptance in Saudi Arabia.
  name: STC Pay
- description: Domestic acquiring in Oman.
  name: Oman Net
- description: Pakistani mobile wallet acceptance.
  name: EasyPaisa / JazzCash
json_schemas:
- name: Paymob Disbursement
  property_count: 13
  slug: paymob-disbursement
- name: Paymob Intention
  property_count: 15
  slug: paymob-intention
- name: Paymob Transaction
  property_count: 16
  slug: paymob-transaction
jsonld:
- class_count: 0
  name: Paymob Context
  property_count: 7
  slug: paymob-context
layout: provider
modified: '2026-05-24'
name: Paymob
nav: Providers
network: true
overview: 'Paymob publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Intentions API, Subscriptions API, Card Tokens API, and 15 more. Tagged areas include Payments, Payment Gateway, Fintech, MENA, and MENAP.


  The Paymob catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Paymob''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, developer console, signup flow, and 38 more developer resources.'
plans:
- name: Paymob Plans Pricing
  plan_count: 3
  slug: paymob-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Paymob Rate Limits
  slug: paymob-rate-limits
rules:
- name: Paymob API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: paymob-jsonschema-spectral-rules
- name: Paymob API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: paymob-rules
score:
  band: strong
  composite: 59.7
  delta: -4.8
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.1
    developer_ergonomics: 71.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paymob/refs/heads/main/screenshots/paymob-2026-06-20T191508.png
security:
- kind: authentication
  name: Paymob Authentication
  slug: paymob-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Paymob Domain Security
  slug: paymob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paymob
solutions:
- description: Self-serve onboarding with per-transaction pricing for startups, SMBs, and SMEs.
  name: SMB Standard
- description: Custom MDR, dedicated account team, multi-region settlement, advanced fraud tooling.
  name: Enterprise
- description: Split payments, multi-merchant onboarding, and automated downstream payouts.
  name: Marketplace
- description: Sub-merchant onboarding and Paymob Sync for embedded payments.
  name: Platform / PSP
- description: Standalone Send deployment for businesses that need mass disbursement without acceptance.
  name: Payouts-only
tags:
- Payments
- Payment Gateway
- Fintech
- MENA
- MENAP
- Egypt
- Saudi Arabia
- UAE
- Pakistan
- Oman
- Card Payments
- Mobile Wallets
- BNPL
- Payouts
- Subscriptions
use_cases:
- description: Online stores accepting cards, wallets, and BNPL across MENAP through a single integration.
  name: E-commerce checkout
- description: Recurring billing for software and digital subscriptions with retry, suspend, and resume controls.
  name: SaaS subscription billing
- description: Mass payouts to drivers and couriers via instant cashin (Vodafone Cash, Etisalat Cash, bank wallets).
  name: Ride-hailing and delivery payouts
- description: Bulk transfers to employees and suppliers across wallets and bank cards.
  name: Payroll and supplier disbursements
- description: Automated split between platform and sellers with downstream payout.
  name: Marketplace split payments
- description: Subscription, utility, and installment collection across cards, wallets, and cash networks.
  name: Bill payments and recurring collections
- description: POS terminals plus online acceptance unified through Paymob Sync for end-to-end commerce.
  name: Omnichannel retail
- description: Single contractual surface with regional acquiring across Egypt, KSA, UAE, Oman, Pakistan.
  name: Cross-border MENAP expansion
website: https://developers.paymob.com
---
