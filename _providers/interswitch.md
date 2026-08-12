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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Interswitch Agentic Access
  operation_count: 55
  slug: interswitch-agentic-access
  summary_line: 55 operations · 31 acting · 1 human-in-the-loop
api_count: 32
apis:
- description: Quickteller Send Money APIs covering Single Transfer (POST /quicktellerservice/api/v5/transactions/TransferFunds), Bulk Transfer, Name Inquiry, and Bank Code Resolution. Used by banks, fintechs, and P
  name: Interswitch Transfers API
  slug: interswitch-transfers-api
- description: Refund successful Quickteller Business transactions in full or in part via `POST /paymentgateway/api/v1/refunds`. Tracks refund lifecycle through SUCCESS, PENDING, PROCESSING, COMPLETE, COMPLETE_MANUA
  name: Interswitch Refunds API
  slug: interswitch-refunds-api
- description: The Airtime API from Interswitch — 3 operation(s) for airtime.
  name: Interswitch Airtime API
  slug: interswitch-airtime-api
- description: The Balance API from Interswitch — 1 operation(s) for balance.
  name: Interswitch Balance API
  slug: interswitch-balance-api
- description: The Bank Codes API from Interswitch — 1 operation(s) for bank codes.
  name: Interswitch Bank Codes API
  slug: interswitch-bank-codes-api
- description: The Billers API from Interswitch — 3 operation(s) for billers.
  name: Interswitch Billers API
  slug: interswitch-billers-api
- description: The Bulk Transfers API from Interswitch — 1 operation(s) for bulk transfers.
  name: Interswitch Bulk Transfers API
  slug: interswitch-bulk-transfers-api
- description: The Cards API from Interswitch — 5 operation(s) for cards.
  name: Interswitch Cards API
  slug: interswitch-cards-api
- description: Hosted checkout payment initiation
  name: Interswitch Checkout API
  slug: interswitch-checkout-api
- description: The Customer Validation API from Interswitch — 1 operation(s) for customer validation.
  name: Interswitch Customer Validation API
  slug: interswitch-customer-validation-api
- description: The Customers API from Interswitch — 2 operation(s) for customers.
  name: Interswitch Customers API
  slug: interswitch-customers-api
- description: The Demography API from Interswitch — 1 operation(s) for demography.
  name: Interswitch Demography API
  slug: interswitch-demography-api
- description: The Detail API from Interswitch — 1 operation(s) for detail.
  name: Interswitch Detail API
  slug: interswitch-detail-api
- description: The E-Pins API from Interswitch — 1 operation(s) for e-pins.
  name: Interswitch E-Pins API
  slug: interswitch-e-pins-api
- description: The Financial Habits API from Interswitch — 1 operation(s) for financial habits.
  name: Interswitch Financial Habits API
  slug: interswitch-financial-habits-api
- description: The Financial History API from Interswitch — 2 operation(s) for financial history.
  name: Interswitch Financial History API
  slug: interswitch-financial-history-api
- description: Card data tokenization
  name: Interswitch Hosted Fields API
  slug: interswitch-hosted-fields-api
- description: The Linking API from Interswitch — 1 operation(s) for linking.
  name: Interswitch Linking API
  slug: interswitch-linking-api
- description: The Loans API from Interswitch — 3 operation(s) for loans.
  name: Interswitch Loans API
  slug: interswitch-loans-api
- description: The Name Inquiry API from Interswitch — 1 operation(s) for name inquiry.
  name: Interswitch Name Inquiry API
  slug: interswitch-name-inquiry-api
- description: The Offers API from Interswitch — 2 operation(s) for offers.
  name: Interswitch Offers API
  slug: interswitch-offers-api
- description: The Payment Items API from Interswitch — 1 operation(s) for payment items.
  name: Interswitch Payment Items API
  slug: interswitch-payment-items-api
- description: Hosted payment link generation
  name: Interswitch Payment Links API
  slug: interswitch-payment-links-api
- description: The Payments API from Interswitch — 5 operation(s) for payments.
  name: Interswitch Payments API
  slug: interswitch-payments-api
- description: The PIN API from Interswitch — 1 operation(s) for pin.
  name: Interswitch PIN API
  slug: interswitch-pin-api
- description: The Providers API from Interswitch — 1 operation(s) for providers.
  name: Interswitch Providers API
  slug: interswitch-providers-api
- description: The Recurring Charges API from Interswitch — 1 operation(s) for recurring charges.
  name: Interswitch Recurring Charges API
  slug: interswitch-recurring-charges-api
- description: The Search API from Interswitch — 3 operation(s) for search.
  name: Interswitch Search API
  slug: interswitch-search-api
- description: Step-up authentication
  name: Interswitch Three-D Secure API
  slug: interswitch-three-d-secure-api
- description: The Tokenization API from Interswitch — 1 operation(s) for tokenization.
  name: Interswitch Tokenization API
  slug: interswitch-tokenization-api
- description: The Tokens API from Interswitch — 4 operation(s) for tokens.
  name: Interswitch Tokens API
  slug: interswitch-tokens-api
- description: Transaction status query
  name: Interswitch Transactions API
  slug: interswitch-transactions-api
arazzos:
- description: Discover an airtime telco, pick a denomination, and recharge a phone number.
  name: Interswitch Airtime Recharge
  slug: interswitch-airtime-recharge-workflow
- description: Look up a biller's payment item, validate the customer, then submit a bill payment advice.
  name: Interswitch Validate Customer And Pay Bill
  slug: interswitch-bill-payment-validate-and-pay-workflow
- description: Authorize a card payment, step up to 3D Secure when required, then confirm the final payment status.
  name: Interswitch Card Payment With 3D Secure
  slug: interswitch-card-payment-with-3ds-workflow
- description: Open a hosted-fields session to collect card data out of PCI scope, then confirm the resulting payment.
  name: Interswitch Hosted Fields Checkout
  slug: interswitch-hosted-fields-checkout-workflow
- description: Issue a new card to a customer, set its PIN, then read back the activated card.
  name: Interswitch Issue And Activate Card
  slug: interswitch-issue-and-activate-card-workflow
- description: Generate a lending payment token, confirm it with an OTP, then debit a loan repayment with it.
  name: Interswitch Lending Enroll Payment Method
  slug: interswitch-lending-enroll-payment-method-workflow
- description: Fetch a customer's loan offers, accept one, fund the loan, then confirm the customer's loan status.
  name: Interswitch Lending Offer To Disbursement
  slug: interswitch-lending-offer-to-disbursement-workflow
- description: Validate a card PAN, link it to a customer, then read the linked card's balance.
  name: Interswitch Link And Check Card Balance
  slug: interswitch-link-and-check-card-balance-workflow
- description: Generate a cardless Paycode token, poll its status, and cancel it if it is not yet used.
  name: Interswitch Paycode Generate And Track
  slug: interswitch-paycode-generate-and-track-workflow
- description: Confirm an original payment, raise a refund against it, then poll the refund to a terminal state.
  name: Interswitch Payment Refund And Track
  slug: interswitch-payment-refund-workflow
- description: Tokenize a card once, then charge the stored token for a recurring payment.
  name: Interswitch Recurring Tokenize And Charge
  slug: interswitch-recurring-tokenize-and-charge-workflow
- description: Find a transaction by merchant reference, then pull its full detail for reconciliation.
  name: Interswitch Transaction Reconciliation
  slug: interswitch-transaction-reconciliation-workflow
- description: Resolve a bank code, confirm the recipient account name, then send a single transfer.
  name: Interswitch Transfer With Name Inquiry
  slug: interswitch-transfer-with-name-inquiry-workflow
- description: Initiate a hosted Web Redirect payment, then server-side requery to confirm before delivering value.
  name: Interswitch Web Checkout And Confirm
  slug: interswitch-web-checkout-confirm-workflow
artifact_total: 101
collections:
- collection_type: postman
  name: Interswitch Airtime Recharge API
  slug: postman-interswitch-airtime-recharge-api
- collection_type: postman
  name: Interswitch Bills Payment API
  slug: postman-interswitch-bills-payment-api
- collection_type: postman
  name: Interswitch Card 360 API
  slug: postman-interswitch-card-360-api
- collection_type: postman
  name: Interswitch Customer Insights API
  slug: postman-interswitch-customer-insights-api
- collection_type: postman
  name: Interswitch Lending API
  slug: postman-interswitch-lending-api
- collection_type: postman
  name: Interswitch Paycode API
  slug: postman-interswitch-paycode-api
- collection_type: postman
  name: Interswitch Payment Gateway API
  slug: postman-interswitch-payment-gateway-api
- collection_type: postman
  name: Interswitch Recurring Payments API
  slug: postman-interswitch-recurring-payments-api
- collection_type: postman
  name: Interswitch Refunds API
  slug: postman-interswitch-refunds-api
- collection_type: postman
  name: Interswitch Transaction Search API
  slug: postman-interswitch-transaction-search-api
- collection_type: postman
  name: Interswitch Transfers API
  slug: postman-interswitch-transfers-api
- collection_type: postman
  name: Interswitch Web Checkout API
  slug: postman-interswitch-web-checkout-api
- collection_type: open
  name: Interswitch Airtime Recharge API
  slug: open-interswitch-airtime-recharge-api
- collection_type: open
  name: Interswitch Bills Payment API
  slug: open-interswitch-bills-payment-api
- collection_type: open
  name: Interswitch Card 360 API
  slug: open-interswitch-card-360-api
- collection_type: open
  name: Interswitch Customer Insights API
  slug: open-interswitch-customer-insights-api
- collection_type: open
  name: Interswitch Lending API
  slug: open-interswitch-lending-api
- collection_type: open
  name: Interswitch Paycode API
  slug: open-interswitch-paycode-api
- collection_type: open
  name: Interswitch Payment Gateway API
  slug: open-interswitch-payment-gateway-api
- collection_type: open
  name: Interswitch Recurring Payments API
  slug: open-interswitch-recurring-payments-api
- collection_type: open
  name: Interswitch Refunds API
  slug: open-interswitch-refunds-api
- collection_type: open
  name: Interswitch Transaction Search API
  slug: open-interswitch-transaction-search-api
- collection_type: open
  name: Interswitch Transfers API
  slug: open-interswitch-transfers-api
- collection_type: open
  name: Interswitch Web Checkout API
  slug: open-interswitch-web-checkout-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/interswitch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interswitch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interswitch-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/interswitch/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-airtime-recharge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-bill-payment-validate-and-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-card-payment-with-3ds-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-hosted-fields-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-issue-and-activate-card-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-lending-enroll-payment-method-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-lending-offer-to-disbursement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-link-and-check-card-balance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-paycode-generate-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-payment-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-recurring-tokenize-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-transaction-reconciliation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-transfer-with-name-inquiry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/interswitch-web-checkout-confirm-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.interswitchgroup.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.interswitchgroup.com/docs/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.interswitchgroup.com/reference
- group: start
  title: ''
  type: Signup
  url: https://developer.interswitchgroup.com
- group: start
  title: ''
  type: Portal
  url: https://developer.interswitchgroup.com/marketplace
- group: auth
  title: ''
  type: Authentication
  url: https://docs.interswitchgroup.com/docs/authentication
- group: auth
  title: ''
  type: Authentication
  url: https://passport-sandbox.interswitchng.com/passport/oauth/token
- group: design
  title: ''
  type: Webhooks
  url: https://docs.interswitchgroup.com/docs/webhooks
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.interswitchgroup.com/docs/response-codes
- group: docs
  title: ''
  type: Documentation
  url: https://docs.interswitchgroup.com/llms.txt
- group: operate
  title: ''
  type: Forums
  url: https://join.slack.com/t/iswdevelopercommunity/shared_invite/zt-2lbdgbkjq-7Byrv6unYM2nX5RwK4MQ7g
- group: company
  title: ''
  type: Blog
  url: https://www.interswitchgroup.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://www.interswitchgroup.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.interswitchgroup.com/support
- group: company
  title: ''
  type: Careers
  url: https://www.interswitchgroup.com/company/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.interswitchgroup.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.interswitchgroup.com/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.interswitchgroup.com/compliance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/interswitch-group
- group: company
  title: ''
  type: Twitter
  url: https://x.com/interswitchgrp
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@InterswitchGroup
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/techquest/integrating-to-ipg
- group: build
  title: ''
  type: SDKs
  url: https://github.com/techquest/payment_php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/techquest/isw-laravel-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/techquest/isw-react-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/akinmail/isw-payment-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/akinmail/isw-payment-sdk-ios
- group: commercial
  title: ''
  type: Plans
  url: plans/interswitch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/interswitch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/interswitch-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/interswitch-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/interswitch-rules.yml
created: '2026-05-24'
description: Interswitch is Nigeria's foundational digital payments and transaction-switching company, founded in 2002 and regulated by the Central Bank of Nigeria. It owns the Verve card scheme (Africa's first domestic EMV chip-and-PIN brand), the Quickteller consumer and business payments platform, the Webpay / Web Checkout gateway, the Paycode cardless service, and the underlying transaction switch that connects Nigerian banks, fintechs, billers, and merchants. The Interswitch developer platform exposes REST APIs for accepting payments, sending transfers, paying bills, recharging airtime, generating cardless tokens, issuing Verve cards (Card 360), originating loans, accessing customer insights, and searching transactions — all under OAuth 2.0 client-credentials authentication via the Passport token service and HMAC-SHA512-signed webhooks. The company is expanding from Nigeria into Ghana, Kenya, Uganda, and other African markets.
examples:
- key_count: 5
  name: Interswitch Web Checkout Example
  slug: interswitch-web-checkout-example
features:
- Verve — Africa's first and largest domestic EMV chip-and-PIN card scheme, accepted at Interswitch-acquired ATMs, POS terminals, and online merchants across Nigeria
- Quickteller — multi-rail consumer and business payments platform spanning bills, airtime, transfers, and merchant payments
- Quickteller Business — merchant dashboard for collections, payment links, invoices, refunds, and webhooks
- Web Checkout (Webpay) — hosted payment page with inline JavaScript popup and Web Redirect modes; Verve, Visa, and Mastercard acceptance
- Payment Gateway — server-to-server card payments, Hosted Fields, 3D Secure, Google Pay
- Transfers — Single, Bulk, Name Inquiry, and Bank Code Resolution endpoints over the NIBSS Instant Payment rails
- Bills Payment — hundreds of Nigerian billers (DSTV, GOTV, PHCN, school fees, TSA government payments)
- Airtime & Data Recharge — direct top-up and e-pin voucher delivery for MTN, Airtel, Glo, and 9mobile
- Paycode (Pay with Mobile) — cardless ATM withdrawal and merchant token generation, single and bulk
- Card 360 — issuer-processor card management for Verve, debit, and prepaid cards (create, PIN, block, link, balance)
- Lending Service — nano loans, salary lending, value financing under `/lending-service/api/v1` and `/v3`
- Customer Insights — demography, financial history, and financial-habit data products for credit decisioning
- Transaction Search — Quick, Reference, Bulk, and Detail lookups for back-office reconciliation
- Recurring Payments — Verve / Visa / Mastercard tokenization plus scheduled charges for subscriptions
- Refunds — full and partial refund lifecycle with T+1 auto-settlement
- Webhooks — HMAC-SHA512-signed events for TRANSACTION, SUBSCRIPTION, PAYMENT LINKS, and INVOICES
- Authentication — OAuth 2.0 client-credentials via the Passport token service plus legacy InterswitchAuth signature scheme (SHA1-signed headers)
- Sandbox environment at `sandbox.interswitchng.com` and `qa.interswitchng.com` with public test credentials
- Smartfuel, Quickteller Homes, Smart City, and TransSwitch verticals served by the same core APIs
- QR code interoperability across Nigerian banks
finops:
- name: Interswitch Finops
  service_category: Financial Services
  slug: interswitch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/interswitch.png
json_schemas:
- name: Interswitch Payment
  property_count: 0
  slug: interswitch-payment
jsonld:
- class_count: 0
  name: Interswitch Context
  property_count: 7
  slug: interswitch-context
layout: provider
modified: '2026-05-24'
name: Interswitch
nav: Providers
network: true
overview: 'Interswitch publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Transfers API, Refunds API, Airtime API, and 29 more. Tagged areas include Payments, Payment Infrastructure, Card Network, Verve, and Quickteller.


  The Interswitch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Interswitch''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, support, YouTube channel, and 43 more developer resources.'
plans:
- name: Interswitch Plans Pricing
  plan_count: 5
  slug: interswitch-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Interswitch Rate Limits
  slug: interswitch-rate-limits
rules:
- name: Interswitch API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: interswitch-jsonschema-spectral-rules
- name: Interswitch API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 3
  slug: interswitch-rules
score:
  band: strong
  composite: 59.8
  delta: 1.8
  facets:
    commercial_clarity: 81.6
    contract_quality: 62.2
    developer_ergonomics: 54.3
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interswitch/refs/heads/main/screenshots/interswitch-2026-06-20T183513.png
security:
- kind: authentication
  name: Interswitch Authentication
  slug: interswitch-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Interswitch Domain Security
  slug: interswitch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: interswitch
tags:
- Payments
- Payment Infrastructure
- Card Network
- Verve
- Quickteller
- Webpay
- Bills Payment
- Transfers
- Lending
- Fintech
- Africa
- Nigeria
website: https://www.interswitchgroup.com
---
