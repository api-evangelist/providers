---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: D Local Agentic Access
  operation_count: 49
  slug: d-local-agentic-access
  summary_line: 49 operations · 27 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Create, retrieve, cancel, and authorize payments using 1,000+ local payment methods including cards, Pix, UPI, M-Pesa, Boleto, OXXO, SPEI, mobile money, cash vouchers, BNPL, wallets, and QR codes acro
  name: dLocal Payments API
  slug: d-local-payments-api
- description: Create, retrieve, and inspect refunds against previously successful payments. Refunds may be full or partial and are settled in the original payment currency.
  name: dLocal Refunds API
  slug: d-local-refunds-api
- description: Securely tokenize cards (server-side) for repeat usage. Returns a card_id token consumable by subsequent Payments and Authorizations.
  name: dLocal Cards API
  slug: d-local-cards-api
- description: Retrieve chargeback details and status, simulate chargebacks in the sandbox, and receive asynchronous chargeback notifications via webhook.
  name: dLocal Chargebacks API
  slug: d-local-chargebacks-api
- description: Enroll payers for recurring Pix Automático, Pix Biometrics, and SmartPix transactions. Once enrolled, payers can be charged repeatedly without re-authorization.
  name: dLocal Enrollments API
  slug: d-local-enrollments-api
- description: Create and manage sub-merchant accounts.
  name: dLocal Accounts API
  slug: d-local-accounts-api
- description: Authorize a card transaction and capture or cancel later.
  name: dLocal Authorizations API
  slug: d-local-authorizations-api
- description: Inspect available merchant balance for payouts.
  name: dLocal Balance API
  slug: d-local-balance-api
- description: Manage bank accounts attached to sub-merchant accounts.
  name: dLocal BankAccounts API
  slug: d-local-bankaccounts-api
- description: Upload and retrieve verification documents.
  name: dLocal Documents API
  slug: d-local-documents-api
- description: Retrieve real-time FX rates.
  name: dLocal ExchangeRates API
  slug: d-local-exchangerates-api
- description: Submit KYC data and documents for accounts.
  name: dLocal KYC API
  slug: d-local-kyc-api
- description: Request, retrieve, release, and cancel payouts.
  name: dLocal Payouts API
  slug: d-local-payouts-api
- description: Lock in an FX quote before requesting a payout.
  name: dLocal Quotes API
  slug: d-local-quotes-api
- description: Settle and transfer between accounts.
  name: dLocal Transfers API
  slug: d-local-transfers-api
- description: Create and inspect KYC verifications.
  name: dLocal Verifications API
  slug: d-local-verifications-api
arazzos:
- description: Authorize a card transaction, confirm the authorization, then capture the funds.
  name: dLocal Authorize and Capture Payment
  slug: d-local-authorize-and-capture-payment-workflow
- description: Create an alternative payment, check its status, and cancel it while it is still PENDING.
  name: dLocal Cancel Pending Payment
  slug: d-local-cancel-pending-payment-workflow
- description: Create a KYC verification, confirm it persisted, then branch on its status to update state or list documents.
  name: dLocal Create and Resolve KYC Verification
  slug: d-local-create-and-resolve-kyc-verification-workflow
- description: Discover a supported payment method, create a payment, then poll its status until it settles.
  name: dLocal Create Payment and Confirm Status
  slug: d-local-create-payment-and-confirm-status-workflow
- description: Enroll a payer for Pix Automatico, confirm the enrollment is ACTIVE, then place the first recurring charge.
  name: dLocal Enroll and Charge Recurring
  slug: d-local-enroll-and-charge-recurring-workflow
- description: Preview the exchange rate for a corridor, then create a payment in the local currency.
  name: dLocal FX Preview and Pay
  slug: d-local-fx-preview-and-pay-workflow
- description: Request a payout on hold, review it, then release or cancel based on the review.
  name: dLocal Hold and Release Payout
  slug: d-local-hold-and-release-payout-workflow
- description: Confirm a payment, list all refunds raised against it, then retrieve one refund in detail.
  name: dLocal List and Inspect Payment Refunds
  slug: d-local-list-payment-refunds-workflow
- description: Add a bank account to a sub-merchant, list the account's bank accounts, retrieve one, then disable it.
  name: dLocal Manage Account Bank Accounts
  slug: d-local-manage-account-bank-accounts-workflow
- description: Create a platform sub-merchant account, attach a bank account, then confirm KYC and balance.
  name: dLocal Onboard Sub-Merchant Account
  slug: d-local-onboard-submerchant-account-workflow
- description: Check balance, lock an FX quote, request a payout against the quote, then confirm its status.
  name: dLocal Quote and Request Payout
  slug: d-local-quote-and-request-payout-workflow
- description: Confirm a payment is PAID, issue a refund against it, then verify the refund status.
  name: dLocal Refund Payment and Confirm
  slug: d-local-refund-payment-and-confirm-workflow
- description: Check the source account balance, transfer funds to another account, then confirm the transfer.
  name: dLocal Settle Transfer Between Accounts
  slug: d-local-settle-transfer-between-accounts-workflow
- description: Create a payment, simulate a chargeback against it in sandbox, then inspect the chargeback and its status.
  name: dLocal Simulate and Inspect Chargeback
  slug: d-local-simulate-and-inspect-chargeback-workflow
- description: Tokenize a card, verify the stored token, then charge it in a card payment.
  name: dLocal Tokenize Card and Charge
  slug: d-local-tokenize-card-and-charge-workflow
artifact_total: 124
collections:
- collection_type: postman
  name: dLocal Cards API
  slug: postman-d-local-cards-api
- collection_type: postman
  name: dLocal Chargebacks API
  slug: postman-d-local-chargebacks-api
- collection_type: postman
  name: dLocal Enrollments API
  slug: postman-d-local-enrollments-api
- collection_type: postman
  name: dLocal Exchange Rates API
  slug: postman-d-local-exchange-rates-api
- collection_type: postman
  name: dLocal KYC Verifications API
  slug: postman-d-local-kyc-verifications-api
- collection_type: postman
  name: dLocal Payments API
  slug: postman-d-local-payments-api
- collection_type: postman
  name: dLocal Payouts V3 API
  slug: postman-d-local-payouts-v3-api
- collection_type: postman
  name: dLocal For Platforms API
  slug: postman-d-local-platforms-api
- collection_type: postman
  name: dLocal Refunds API
  slug: postman-d-local-refunds-api
- collection_type: open
  name: dLocal Cards API
  slug: open-d-local-cards-api
- collection_type: open
  name: dLocal Chargebacks API
  slug: open-d-local-chargebacks-api
- collection_type: open
  name: dLocal Enrollments API
  slug: open-d-local-enrollments-api
- collection_type: open
  name: dLocal Exchange Rates API
  slug: open-d-local-exchange-rates-api
- collection_type: open
  name: dLocal KYC Verifications API
  slug: open-d-local-kyc-verifications-api
- collection_type: open
  name: dLocal Payments API
  slug: open-d-local-payments-api
- collection_type: open
  name: dLocal Payouts V3 API
  slug: open-d-local-payouts-v3-api
- collection_type: open
  name: dLocal For Platforms API
  slug: open-d-local-platforms-api
- collection_type: open
  name: dLocal Refunds API
  slug: open-d-local-refunds-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/d-local-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/d-local-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/d-local-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dlocal/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-authorize-and-capture-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-cancel-pending-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-create-and-resolve-kyc-verification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-create-payment-and-confirm-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-enroll-and-charge-recurring-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-fx-preview-and-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-hold-and-release-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-list-payment-refunds-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-manage-account-bank-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-onboard-submerchant-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-quote-and-request-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-refund-payment-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-settle-transfer-between-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-simulate-and-inspect-chargeback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/d-local-tokenize-card-and-charge-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://dlocal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dlocal.com/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dlocal.com/docs/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dlocal.com/docs/make-a-test-payment
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/enable-live-mode
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/initial-settings
- group: auth
  title: ''
  type: Authentication
  url: https://docs.dlocal.com/docs/generate-signature
- group: auth
  title: ''
  type: Authentication
  url: https://docs.dlocal.com/docs/get-api-credentials-new
- group: auth
  title: ''
  type: Compliance
  url: https://docs.dlocal.com/docs/pci-compliance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/using-llms
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/llms.txt
- group: build
  title: ''
  type: SDKs
  url: https://docs.dlocal.com/reference/postman-api-collection
- group: operate
  title: ''
  type: StatusPage
  url: https://dlocal.statuspage.io/
- group: company
  title: ''
  type: Blog
  url: https://dlocal.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://dlocal.com/contact-sales/
- group: other
  title: ''
  type: Resources
  url: https://dlocal.com/careers/
- group: company
  title: ''
  type: Newsletter
  url: https://dlocal.com/press-releases/
- group: other
  title: ''
  type: Resources
  url: https://investor.dlocal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dlocal.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dlocal.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: http://intercom.help/end-user-team-faqs/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dlocal
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/mobile-checkout-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/mobile-checkout-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/web-drop-in-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/data-collector-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/data-collector-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-data-collector-capacitor-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dlocal/dlocal-direct-js-native-integration
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlocal/smart-fields-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dlocal/Starter-Code-Examples
- group: build
  title: ''
  type: SDKs
  url: https://docs.dlocal.com/reference/including-dlocaljs
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.dlocal.com/reference/troubleshooting-integration
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.dlocal.com/reference/troubleshooting-signature
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/reference/payment-status-codes
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-payments
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-refunds
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/http-errors-cards
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.dlocal.com/reference/error-codes-payouts-v3
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/reference/country-reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/overview-payins
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/overview-payouts-v3
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/platforms-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/overview-smart-fields
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/integrate-checkout
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/payment-links
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dlocal.com/docs/fraud-prevention
- group: design
  title: ''
  type: SpectralRules
  url: rules/d-local-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/d-local-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/d-local-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/d-local-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/d-local-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/d-local-finops.yml
created: '2026-05-24'
description: 'dLocal (NASDAQ: DLO) is a Uruguay-headquartered emerging-markets payment infrastructure platform connecting global merchants with billions of consumers across 60+ countries in Latin America, Africa, the Middle East, and Asia. dLocal exposes a unified set of REST APIs for accepting payments (Payins) via 1,000+ local methods, disbursing funds (Payouts V3) to beneficiaries via local rails, tokenizing cards, managing marketplace sub-merchants (dLocal for Platforms), performing KYC verifications, handling chargebacks, enrolling users for recurring Pix flows, and pulling real-time exchange rates. Native iOS and Android SDKs are published as open source on GitHub.'
examples:
- key_count: 2
  name: Cards Create Card Example
  slug: cards-create-card-example
- key_count: 2
  name: Exchange Rates Get Rate Example
  slug: exchange-rates-get-rate-example
- key_count: 2
  name: Kyc Create Verification Example
  slug: kyc-create-verification-example
- key_count: 2
  name: Payments Create Payment Example
  slug: payments-create-payment-example
- key_count: 2
  name: Payments Pix Example
  slug: payments-pix-example
- key_count: 2
  name: Payments Retrieve Payment Example
  slug: payments-retrieve-payment-example
- key_count: 2
  name: Payouts V3 Get Balance Example
  slug: payouts-v3-get-balance-example
- key_count: 2
  name: Payouts V3 Request Payout Example
  slug: payouts-v3-request-payout-example
- key_count: 2
  name: Platforms Create Account Example
  slug: platforms-create-account-example
- key_count: 2
  name: Refunds Make Refund Example
  slug: refunds-make-refund-example
features:
- 1,000+ local payment methods across 60+ countries in Latin America, Africa, the Middle East, and Asia
- Single REST API for Payins, Payouts, Refunds, Cards, Chargebacks, Enrollments, and Exchange Rates
- Payments API authenticated with V2-HMAC-SHA256 signature (X-Login, X-Trans-Key, X-Date)
- Payouts V3 API with OAuth2 Bearer tokens, quotes for FX lock-in, on-hold release, and explicit fee breakdown
- dLocal for Platforms (marketplace) API for sub-merchant onboarding, KYC, bank accounts, balances, and inter-account transfers
- KYC Verifications API for remitter, beneficiary, and standalone identity checks
- Brazilian Pix support including Pix Automático recurring, Pix Biometrics, and SmartPix
- India network tokenization for RBI-compliant card storage
- African Mobile Money (M-Pesa and equivalents) and Africa-specific instant payment rails
- Authorization and capture flow for delayed-capture card transactions
- 3D Secure 2.x authentication and card network token support
- SmartFields client-side field-level tokenization via dlocal.js
- SmartPix native and redirect flows for Brazilian recurring on-demand payments
- Defense Suite for fraud management and chargeback prevention
- Virtual Accounts for bank-transfer reconciliation
- Hosted Checkout (dLocal Go) and Payment Links
- dLocal Direct, Mobile Checkout, Web Drop-In, and Data Collector SDKs for iOS, Android, and Capacitor
- Postman Collection and llms.txt index of OpenAPI operations
- Built-in dLocal MCP Server for LLM-assisted integration
- Sandbox environment at sandbox.dlocal.com (and marketplace-api.dlocal-sbox.com) with chargeback simulation
- Webhook notifications for payments, refunds, chargebacks, payouts, verifications, and platform accounts
- Real-time exchange rate endpoint for quoting before payin/payout
- IP allow-list enforcement on production endpoints
finops:
- name: D Local Finops
  service_category: Financial Services / Payments
  slug: d-local-finops
image: https://avatars.githubusercontent.com/u/22692935
integrations:
- description: Native Pix, Pix Automático (recurring), Pix Biometrics, and SmartPix support.
  name: Brazil Pix
- description: UPI collect/intent flows plus RBI-compliant network tokenization.
  name: India UPI and network tokenization
- description: M-Pesa, MTN MoMo, Orange Money, and other Mobile Money rails.
  name: Africa M-Pesa and Mobile Money
- description: Bank transfer (SPEI) and cash voucher (OXXO) coverage.
  name: Mexico SPEI and OXXO
- description: Stablecoin Full product for crypto-rail settlement.
  name: Stablecoins
- description: Google Pay integration via the Paytm bridge.
  name: Google Pay (Paytm bridge)
- description: Device ID object support for fraud signals on Mercado Pago.
  name: Mercado Pago
- description: Official Postman collection covering the full REST API.
  name: Postman
- description: Built-in dLocal MCP server exposes API operations to LLM agents.
  name: Model Context Protocol (MCP)
json_schemas:
- name: dLocal Card Token
  property_count: 7
  slug: cards-card-token
- name: dLocal Payment
  property_count: 17
  slug: payments-payment
- name: dLocal Payout
  property_count: 16
  slug: payouts-v3-payout
- name: dLocal for Platforms Account
  property_count: 10
  slug: platforms-account
- name: dLocal Refund
  property_count: 8
  slug: refunds-refund
json_structures:
- name: Payments Payment Structure
  property_count: 0
  slug: payments-payment-structure
- name: Payouts V3 Payout Structure
  property_count: 0
  slug: payouts-v3-payout-structure
jsonld:
- class_count: 40
  name: D Local Context
  property_count: 7
  slug: d-local-context
layout: provider
modified: '2026-05-24'
name: dLocal
nav: Providers
network: true
overview: 'dLocal publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Payments API, Refunds API, Cards API, and 13 more. Tagged areas include Payments, Payouts, EmergingMarkets, LatAm, and Africa.


  The dLocal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  dLocal''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, engineering blog, signup flow, and 68 more developer resources.'
plans:
- name: D Local Plans Pricing
  plan_count: 5
  slug: d-local-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 4
  name: D Local Rate Limits
  slug: d-local-rate-limits
rules:
- name: dLocal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: d-local-jsonschema-spectral-rules
- name: dLocal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 2
    info: 0
    warn: 4
  slug: d-local-rules
score:
  band: strong
  composite: 63.5
  delta: -6.4
  facets:
    commercial_clarity: 68.4
    contract_quality: 65.8
    developer_ergonomics: 71.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/d-local/refs/heads/main/screenshots/d-local-2026-06-20T175421.png
security:
- kind: authentication
  name: D Local Authentication
  slug: d-local-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: D Local Domain Security
  slug: d-local-domain-security
  summary_line: TLSv1.3 · DMARC
slug: d-local
solutions:
- description: Accept local payment methods across 60+ countries.
  name: Payins
- description: Disburse funds via local rails to employees, contractors, partners, and consumers.
  name: Payouts
- description: Marketplace and platform multi-merchant payment solution.
  name: dLocal for Platforms
- description: Fraud-management and chargeback-prevention toolkit.
  name: Defense Suite
- description: Local-currency billing and collection.
  name: Invoice Collection
- description: Stablecoin payin/payout rails for cross-border settlement.
  name: Stablecoin Full
- description: Mobile SDK product for native iOS and Android in-app checkout.
  name: dLocal Direct
- description: Client-side field-level tokenization via dlocal.js.
  name: SmartFields
- description: Hosted checkout product.
  name: dLocal Go
- description: Shareable links for one-off collections.
  name: Payment Links
tags:
- Payments
- Payouts
- EmergingMarkets
- LatAm
- Africa
- Asia
- FX
- Fintech
use_cases:
- description: Charge LatAm, African, and Asian customers in their preferred local currency and method (Pix, UPI, mobile money) for SaaS, streaming, and gaming subscriptions.
  name: Global subscription billing in emerging markets
- description: Pay employees and contractors in 60+ countries using instant local rails, bank transfers, mobile money, and cash pick-up.
  name: Cross-border payroll and contractor payouts
- description: Onboard sub-merchants via dLocal for Platforms, split payments, and settle balances between accounts.
  name: Marketplace and platform payouts
- description: Power consumer remittance corridors with FX quoting, KYC verification, and local-currency disbursement.
  name: Remittances
- description: Enable global travel and mobility platforms to collect from local consumers and pay out to local drivers/hosts.
  name: Travel and ride-hailing
- description: Help global merchants like Amazon, Shein, and Shopify accept local methods such as Boleto, OXXO, SPEI, and Pix.
  name: E-commerce expansion
- description: Use Stablecoin Full for cross-border settlement when fiat rails are slow or expensive.
  name: Stablecoin settlement
website: https://dlocal.com/
---
