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
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Moniepoint Agentic Access
  operation_count: 63
  slug: moniepoint-agentic-access
  summary_line: 63 operations · 33 acting
api_count: 19
apis:
- description: Asynchronous server-to-server notifications for nine event categories — successful collection, successful / failed / reversed disbursement, successful / failed refund, settlement completion, mandate s
  name: Monnify Webhooks
  slug: monnify-webhooks
- description: Obtain a Bearer access token for the Monnify API.
  name: Moniepoint Authentication API
  slug: moniepoint-authentication-api
- description: NIP bank directory and account validation.
  name: Moniepoint Banks API
  slug: moniepoint-banks-api
- description: Bill categories, billers, validation, processing, and status.
  name: Moniepoint Bills Payment API
  slug: moniepoint-bills-payment-api
- description: Initiate and query bulk transfer batches.
  name: Moniepoint Bulk Transfers API
  slug: moniepoint-bulk-transfers-api
- description: Initiate debits against an active mandate.
  name: Moniepoint Debits API
  slug: moniepoint-debits-api
- description: Create, list, and manage invoices.
  name: Moniepoint Invoices API
  slug: moniepoint-invoices-api
- description: Per-account transaction limit profiles.
  name: Moniepoint Limit Profiles API
  slug: moniepoint-limit-profiles-api
- description: Create and manage direct-debit mandates.
  name: Moniepoint Mandates API
  slug: moniepoint-mandates-api
- description: Initiate push payments to a registered POS terminal.
  name: Moniepoint Push Payments API
  slug: moniepoint-push-payments-api
- description: Initiate and query refunds.
  name: Moniepoint Refunds API
  slug: moniepoint-refunds-api
- description: Manage dedicated and invoice reserved NUBAN accounts.
  name: Moniepoint Reserved Accounts API
  slug: moniepoint-reserved-accounts-api
- description: Settlement batches and transactions reporting.
  name: Moniepoint Settlements API
  slug: moniepoint-settlements-api
- description: Initiate, authorize, and query single transfers.
  name: Moniepoint Single Transfers API
  slug: moniepoint-single-transfers-api
- description: Manage settlement sub-accounts.
  name: Moniepoint Sub-Accounts API
  slug: moniepoint-sub-accounts-api
- description: Initialize, charge, query, and list collection transactions.
  name: Moniepoint Transactions API
  slug: moniepoint-transactions-api
- description: Identity, BVN, NIN, and account verification.
  name: Moniepoint Verification API
  slug: moniepoint-verification-api
- description: Disbursement wallet balance and metadata.
  name: Moniepoint Wallet API
  slug: moniepoint-wallet-api
- description: Manage wallets and sub-wallets.
  name: Moniepoint Wallets API
  slug: moniepoint-wallets-api
arazzos:
- description: Initiate a batch of transfers, poll the batch summary to completion, then list per-item results.
  name: Moniepoint Bulk Disbursement
  slug: moniepoint-bulk-disbursement-workflow
- description: Initialize a transaction, capture a card, branch on the 3-D Secure / OTP step, and confirm.
  name: Moniepoint Card Charge With OTP
  slug: moniepoint-card-charge-otp-workflow
- description: Initialize a collection, generate a one-time NUBAN to pay it, then poll the transaction until paid.
  name: Moniepoint Collect Via Bank Transfer
  slug: moniepoint-collect-bank-transfer-workflow
- description: Match a customer BVN to their bank account, then reserve a KYC-bound virtual account and confirm it.
  name: Moniepoint KYC Verified Virtual Account
  slug: moniepoint-kyc-reserve-account-workflow
- description: List billers for a category, validate the customer, process the bill, then poll the bill status.
  name: Moniepoint Pay A Bill
  slug: moniepoint-pay-bill-workflow
- description: Push a payment request to a Moniepoint POS terminal, then poll the terminal until the customer completes it.
  name: Moniepoint POS Push Payment
  slug: moniepoint-pos-push-payment-workflow
- description: Create a direct-debit mandate, activate it, debit it, then read the mandate back.
  name: Moniepoint Recurring Mandate Debit
  slug: moniepoint-recurring-mandate-debit-workflow
- description: Confirm a collection is paid, initiate a refund against it, then poll the refund to completion.
  name: Moniepoint Refund A Collected Payment
  slug: moniepoint-refund-collected-payment-workflow
- description: Reserve a permanent NUBAN virtual account for a customer, confirm it, and read its inbound transactions.
  name: Moniepoint Reserve Virtual Account
  slug: moniepoint-reserve-virtual-account-workflow
- description: Initiate a single transfer, branch on whether OTP authorization is required, authorize it, and confirm.
  name: Moniepoint Single Transfer With OTP
  slug: moniepoint-single-transfer-otp-workflow
- description: Name-inquiry a beneficiary bank account, then disburse to it and poll the transfer to a final state.
  name: Moniepoint Verify And Disburse
  slug: moniepoint-verify-and-disburse-workflow
- description: Define a transaction limit profile, then reserve a virtual account bound to that profile.
  name: Moniepoint Virtual Account With Limit Profile
  slug: moniepoint-virtual-account-with-limit-workflow
- description: Create a customer wallet, read its available and ledger balance, then list its transactions.
  name: Moniepoint Create Wallet And Check Balance
  slug: moniepoint-wallet-balance-check-workflow
artifact_total: 97
collections:
- collection_type: postman
  name: Moniepoint POS Push Payment API
  slug: postman-moniepoint-pos-api
- collection_type: postman
  name: Monnify Authentication API
  slug: postman-monnify-authentication-api
- collection_type: postman
  name: Monnify Bills Payment API
  slug: postman-monnify-bills-payment-api
- collection_type: postman
  name: Monnify Collections API
  slug: postman-monnify-collections-api
- collection_type: postman
  name: Monnify Direct Debit API
  slug: postman-monnify-direct-debit-api
- collection_type: postman
  name: Monnify Disbursements API
  slug: postman-monnify-disbursements-api
- collection_type: postman
  name: Monnify Invoices API
  slug: postman-monnify-invoices-api
- collection_type: postman
  name: Monnify Refunds API
  slug: postman-monnify-refunds-api
- collection_type: postman
  name: Monnify Reserved Accounts API
  slug: postman-monnify-reserved-accounts-api
- collection_type: postman
  name: Monnify Settlements API
  slug: postman-monnify-settlements-api
- collection_type: postman
  name: Monnify Sub-Accounts API
  slug: postman-monnify-sub-accounts-api
- collection_type: postman
  name: Monnify Verification API
  slug: postman-monnify-verification-api
- collection_type: postman
  name: Monnify Wallets API
  slug: postman-monnify-wallets-api
- collection_type: open
  name: Moniepoint POS Push Payment API
  slug: open-moniepoint-pos-api
- collection_type: open
  name: Monnify Authentication API
  slug: open-monnify-authentication-api
- collection_type: open
  name: Monnify Bills Payment API
  slug: open-monnify-bills-payment-api
- collection_type: open
  name: Monnify Collections API
  slug: open-monnify-collections-api
- collection_type: open
  name: Monnify Direct Debit API
  slug: open-monnify-direct-debit-api
- collection_type: open
  name: Monnify Disbursements API
  slug: open-monnify-disbursements-api
- collection_type: open
  name: Monnify Invoices API
  slug: open-monnify-invoices-api
- collection_type: open
  name: Monnify Refunds API
  slug: open-monnify-refunds-api
- collection_type: open
  name: Monnify Reserved Accounts API
  slug: open-monnify-reserved-accounts-api
- collection_type: open
  name: Monnify Settlements API
  slug: open-monnify-settlements-api
- collection_type: open
  name: Monnify Sub-Accounts API
  slug: open-monnify-sub-accounts-api
- collection_type: open
  name: Monnify Verification API
  slug: open-monnify-verification-api
- collection_type: open
  name: Monnify Wallets API
  slug: open-monnify-wallets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moniepoint-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moniepoint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moniepoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moniepoint-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/moniepoint/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-bulk-disbursement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-card-charge-otp-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-collect-bank-transfer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-kyc-reserve-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-pay-bill-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-pos-push-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-recurring-mandate-debit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-refund-collected-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-reserve-virtual-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-single-transfer-otp-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-verify-and-disburse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-virtual-account-with-limit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moniepoint-wallet-balance-check-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://moniepoint.com
- group: start
  title: ''
  type: Portal
  url: https://developers.monnify.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.monnify.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pos.moniepoint.com
- group: docs
  title: ''
  type: Documentation
  url: https://teamapt.atlassian.net/wiki/spaces/MON/pages
- group: docs
  title: ''
  type: Documentation
  url: https://teamapt.atlassian.net/wiki/spaces/EI/pages
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.monnify.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.monnify.com/docs/change-logs
- group: company
  title: ''
  type: Blog
  url: https://developers.monnify.com/blog
- group: company
  title: ''
  type: Blog
  url: https://engineering.moniepoint.com
- group: company
  title: ''
  type: Blog
  url: https://moniepoint.com/blog
- group: company
  title: ''
  type: Press
  url: https://moniepoint.com/press
- group: operate
  title: ''
  type: Support
  url: https://support.moniepoint.com
- group: learn
  title: ''
  type: Training
  url: https://learning.moniepoint.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.moniepoint.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moniepoint.com/ng/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moniepoint.com/ng/terms-of-service
- group: start
  title: ''
  type: Signup
  url: https://app.monnify.com/create-account
- group: start
  title: ''
  type: Signup
  url: https://app.moniepoint.com/signup
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.monnify.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Moniepoint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moniepoint
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/moniepointNG
- group: company
  title: ''
  type: Careers
  url: https://moniepoint.com/careers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Moniepoint/dart-flow
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cla-bit/MonnifyEase
- group: build
  title: ''
  type: SDKs
  url: https://github.com/abdsalam/laravel-monnify
- group: design
  title: ''
  type: Webhooks
  url: https://developers.monnify.com/docs/webhooks
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.monnify.com/docs/getting-started/errors
- group: auth
  title: ''
  type: Authentication
  url: https://developers.monnify.com/docs/getting-started/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.monnify.com/docs/rate-limits
- group: design
  title: ''
  type: Versioning
  url: https://developers.monnify.com/docs/getting-started/versioning
- group: commercial
  title: ''
  type: Plans
  url: plans/moniepoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moniepoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moniepoint-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/moniepoint-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/moniepoint-rules.yml
created: '2026-05-24T00:00:00.000Z'
description: Moniepoint is Africa's all-in-one financial platform for small and medium-sized businesses and individuals — Nigeria's largest merchant acquirer, with about 10 million business and individual accounts, $17B in monthly transaction volume, and 26M daily payments processed. Founded as TeamApt and rebranded under the Moniepoint name, the company became Africa's most valuable fintech unicorn after a 2024 raise led by Google, then expanded into Kenya and cross-border payments. The Monnify developer platform exposes the rails to third parties through a comprehensive REST API for authentication, collections (cards, bank transfer, USSD, reserved accounts), disbursements (single and bulk NIP), sub-accounts and settlement, direct-debit mandates, invoices, bills payment, KYC verification, wallets, refunds, and signed webhooks; the separate Moniepoint POS API enables push payments to registered terminals. Underlying products also include business bank accounts, working-capital credit, expense
  cards, and business-management tools.
examples:
- key_count: 4
  name: Moniepoint Push Payment Example
  slug: moniepoint-push-payment-example
- key_count: 4
  name: Monnify Initialize Transaction Example
  slug: monnify-initialize-transaction-example
- key_count: 4
  name: Monnify Reserve Account Example
  slug: monnify-reserve-account-example
- key_count: 4
  name: Monnify Single Transfer Example
  slug: monnify-single-transfer-example
- key_count: 4
  name: Monnify Webhook Successful Collection Example
  slug: monnify-webhook-successful-collection-example
features:
- Africa's largest merchant acquirer — ~10M business and individual accounts, $17B monthly TPV, 26M daily payments processed
- POS terminal acquiring across Nigeria for in-person card and bank-transfer collections
- Monnify developer platform (formerly TeamApt) — embedded payments, banking, and disbursements for Nigerian businesses
- Collections API with Monnify Checkout, server-to-server card capture (3-D Secure / OTP), pay-with-transfer, and USSD
- Permanent NUBAN virtual accounts (Reserved Accounts) with V2 limit profiles, KYC, and income-split routing
- Single and bulk NIP transfers with mandatory name-inquiry pre-flight (April 2026) and sender-information support
- Sub-accounts for marketplaces, franchises, and multi-tenant settlement with per-transaction split percentages
- Direct-debit mandates with smart routing (TeamApt primary, NIBSS fallback) and incomeSplit on debit
- Static and dynamic invoices with hosted payment pages and per-invoice reserved accounts
- Unified Bills Payment service — airtime, data, electricity, cable TV, betting, education
- Verification services — bank account name inquiry, BVN-account match, NIN verification
- Wallet APIs for main and sub-wallet balances, statements, and transactions
- HMAC-SHA-512 signed webhooks across nine event categories including new low_balance_alert (Sept 2025)
- Sandbox environment at sandbox.monnify.com with separate API key / secret pair
- OAuth-style flow — Basic auth to /api/v1/auth/login returns short-lived Bearer accessToken
- Standard response envelope { requestSuccessful, responseMessage, responseCode, responseBody }
- Community SDKs and wrappers for PHP, Laravel, Python; official Dart utility library (dart-flow)
- Moniepoint POS Push Payment API for ISV-initiated payments to registered terminal serial numbers
- Working-capital credit, business bank accounts, expense cards, and bookkeeping tools alongside the payments rails
- Cross-border payments and Kenya expansion (2024-2026) extending the Nigerian core
finops:
- name: Moniepoint Finops
  service_category: Financial Services
  slug: moniepoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moniepoint.png
json_schemas:
- name: Monnify Reserved Account
  property_count: 15
  slug: monnify-reserved-account
- name: Monnify Transaction
  property_count: 20
  slug: monnify-transaction
- name: Monnify Transfer
  property_count: 14
  slug: monnify-transfer
- name: Monnify Webhook Notification
  property_count: 2
  slug: monnify-webhook
jsonld:
- class_count: 0
  name: Moniepoint Context
  property_count: 7
  slug: moniepoint-context
layout: provider
modified: '2026-05-24'
name: Moniepoint
nav: Providers
network: true
overview: 'Moniepoint publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Banks API, Bills Payment API, and 15 more. Tagged areas include Africa, Nigeria, Payments, Banking, and Fintech.


  The Moniepoint catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Moniepoint''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, support, and 48 more developer resources.'
plans:
- name: Moniepoint Plans Pricing
  plan_count: 3
  slug: moniepoint-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 9
  name: Moniepoint Rate Limits
  slug: moniepoint-rate-limits
rules:
- name: Moniepoint API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: moniepoint-jsonschema-spectral-rules
- name: Moniepoint API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 1
    info: 0
    warn: 3
  slug: moniepoint-rules
score:
  band: exemplar
  composite: 70.3
  delta: 2.9
  facets:
    commercial_clarity: 68.4
    contract_quality: 67.7
    developer_ergonomics: 71.7
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 60.5
  previous_composite: 67.4
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moniepoint/refs/heads/main/screenshots/moniepoint-2026-06-20T185727.png
security:
- kind: authentication
  name: Moniepoint Authentication
  slug: moniepoint-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Moniepoint Domain Security
  slug: moniepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Moniepoint Trust Center
  slug: moniepoint-trust-center
  summary_line: SOC 2, ISO 27001
slug: moniepoint
tags:
- Africa
- Nigeria
- Payments
- Banking
- Fintech
- Acquiring
- POS
- Collections
- Disbursements
- Virtual Accounts
- Direct Debit
- Bills Payment
- SMB
- Working Capital
- Unicorn
website: https://moniepoint.com
---
