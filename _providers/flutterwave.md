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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Flutterwave Agentic Access
  operation_count: 57
  slug: flutterwave-agentic-access
  summary_line: 57 operations · 27 acting
api_count: 19
apis:
- description: Disburse funds globally across bank account transfers, mobile money transfers, and wallet-to-wallet transfers spanning 30+ African countries plus US/UK/EU/Asia corridors. Manage transfer recipients, t
  name: Flutterwave Transfers API
  slug: flutterwave-transfers-api
- description: Reconcile transaction volume with merchant payouts. Manage settlements, refunds, chargebacks (dispute handling), and fee computation for cards, mobile money, and other rails. The finance-and-ops surfa
  name: Flutterwave Settlements API
  slug: flutterwave-settlements-api
- description: Inspect multi-currency wallet balances, retrieve wallet statements, and resolve mobile money wallet account details. Backs the FAAS (Finance as a Service) and capital flows for merchants holding balan
  name: Flutterwave Wallets API
  slug: flutterwave-wallets-api
- description: Reference data for banks, bank branches, and mobile networks supported by country, plus bank account name-enquiry endpoints. Used to populate checkout dropdowns and validate destination accounts befor
  name: Flutterwave Banks API
  slug: flutterwave-banks-api
- description: Outbound webhook callbacks delivered by Flutterwave for charges, transfers, refunds, chargebacks, and virtual account funding. Receivers validate the `verif-hash` header against the merchant's configu
  name: Flutterwave Webhooks API
  slug: flutterwave-webhooks-api
- description: Bank account name resolution before initiating payouts.
  name: Flutterwave AccountResolution API
  slug: flutterwave-accountresolution-api
- description: Manage and respond to chargebacks raised by customers.
  name: Flutterwave Chargebacks API
  slug: flutterwave-chargebacks-api
- description: Create and manage charges across supported payment methods.
  name: Flutterwave Charges API
  slug: flutterwave-charges-api
- description: Create and manage customers that own charges, orders, and transfers.
  name: Flutterwave Customers API
  slug: flutterwave-customers-api
- description: Retrieve Flutterwave's fee calculation for a transaction.
  name: Flutterwave Fees API
  slug: flutterwave-fees-api
- description: Mobile money networks supported by country.
  name: Flutterwave MobileNetworks API
  slug: flutterwave-mobilenetworks-api
- description: Orchestrator helpers that combine customer, payment method, and charge in one call.
  name: Flutterwave Orchestration API
  slug: flutterwave-orchestration-api
- description: Server-side cart and order objects backing checkout sessions.
  name: Flutterwave Orders API
  slug: flutterwave-orders-api
- description: Tokenize, register, and look up payment methods (cards, mobile money, bank, USSD).
  name: Flutterwave PaymentMethods API
  slug: flutterwave-paymentmethods-api
- description: Real-time FX conversion rates for international transfers.
  name: Flutterwave Rates API
  slug: flutterwave-rates-api
- description: Manage transfer recipients (the destination of a payout).
  name: Flutterwave Recipients API
  slug: flutterwave-recipients-api
- description: Initiate and inspect refunds against successful charges.
  name: Flutterwave Refunds API
  slug: flutterwave-refunds-api
- description: Manage transfer senders (the originator of a cross-border payout).
  name: Flutterwave Senders API
  slug: flutterwave-senders-api
- description: Issue virtual NUBANs for pay-with-bank-transfer collections.
  name: Flutterwave VirtualAccounts API
  slug: flutterwave-virtualaccounts-api
arazzos:
- description: Look up supported banks for a country, resolve the destination account, then create a recipient and send a payout.
  name: Flutterwave Bank Directory Then Payout
  slug: flutterwave-bank-directory-then-payout-workflow
- description: Initiate a charge then poll the charge object to confirm its final settled status.
  name: Flutterwave Charge And Verify Status
  slug: flutterwave-charge-and-verify-status-workflow
- description: Confirm a charge succeeded, raise a chargeback against it, and submit evidence to contest it.
  name: Flutterwave Charge Then Dispute Chargeback
  slug: flutterwave-charge-then-dispute-chargeback-workflow
- description: Verify a charge succeeded, then create a refund against it and confirm the refund status.
  name: Flutterwave Charge Then Refund
  slug: flutterwave-charge-then-refund-workflow
- description: Create a transfer recipient, send a payout to it, then verify the transfer reached a final status.
  name: Flutterwave Create Recipient Transfer And Verify
  slug: flutterwave-create-recipient-transfer-verify-workflow
- description: Lock an FX rate, create a sender and recipient, then send a transfer at the locked rate and verify it.
  name: Flutterwave Cross-Border Rate-Locked Transfer
  slug: flutterwave-cross-border-rate-locked-transfer-workflow
- description: Initiate a one-call Orchestrator transfer with inline sender and recipient, then verify the payout status.
  name: Flutterwave Direct Orchestrator Transfer And Verify
  slug: flutterwave-direct-orchestrator-transfer-verify-workflow
- description: Resolve a mobile money wallet, create a mobile money recipient, then send and verify the payout.
  name: Flutterwave Mobile Money Payout
  slug: flutterwave-mobile-money-payout-workflow
- description: Initiate a one-call Orchestrator charge then verify the resulting charge status.
  name: Flutterwave Orchestrator Charge And Verify
  slug: flutterwave-orchestrator-charge-and-verify-workflow
- description: Initiate an order in one call with the Orchestrator helper, then retrieve it to confirm its status.
  name: Flutterwave Orchestrator Order And Verify
  slug: flutterwave-orchestrator-order-and-verify-workflow
- description: Create a customer, place a server-side order for them, then retrieve the order to confirm its status.
  name: Flutterwave Order Checkout And Verify
  slug: flutterwave-order-checkout-and-verify-workflow
- description: Retrieve the processing fee for an amount, create the customer, then charge and verify it.
  name: Flutterwave Quote Fee Then Charge
  slug: flutterwave-quote-fee-then-charge-workflow
- description: Resolve a destination bank account name, create a recipient for it, then send and verify a transfer.
  name: Flutterwave Resolve Account Then Payout
  slug: flutterwave-resolve-account-then-payout-workflow
- description: Retrieve a saved recipient to confirm it exists, then send a transfer to it and verify the payout.
  name: Flutterwave Reuse Recipient Payout
  slug: flutterwave-reuse-recipient-payout-workflow
- description: Retrieve a settlement, confirm a charge within it succeeded, then refund the charge and verify the refund.
  name: Flutterwave Settlement Reconciliation Refund
  slug: flutterwave-settlement-reconciliation-refund-workflow
- description: Tokenize a payment method, charge it for a customer, then verify the recurring charge status.
  name: Flutterwave Tokenized Recurring Charge
  slug: flutterwave-tokenized-recurring-charge-workflow
- description: Send a transfer, verify its status, and retry it automatically when it failed.
  name: Flutterwave Transfer Verify And Retry
  slug: flutterwave-transfer-verify-and-retry-workflow
- description: Search for a customer by email, create one only if missing, then charge that customer and verify it.
  name: Flutterwave Upsert Customer And Charge
  slug: flutterwave-upsert-customer-and-charge-workflow
- description: Create a customer, issue a dedicated virtual account for them, then verify the account is active.
  name: Flutterwave Virtual Account Collection
  slug: flutterwave-virtual-account-collection-workflow
- description: Check a currency wallet balance, then only send a transfer to an existing recipient when funds are sufficient.
  name: Flutterwave Wallet Balance Guarded Payout
  slug: flutterwave-wallet-balance-guarded-payout-workflow
artifact_total: 94
collections:
- collection_type: postman
  name: Flutterwave Banks API
  slug: postman-flutterwave-banks-api
- collection_type: postman
  name: Flutterwave Payments API
  slug: postman-flutterwave-payments-api
- collection_type: postman
  name: Flutterwave Settlements API
  slug: postman-flutterwave-settlements-api
- collection_type: postman
  name: Flutterwave Transfers API
  slug: postman-flutterwave-transfers-api
- collection_type: postman
  name: Flutterwave Wallets API
  slug: postman-flutterwave-wallets-api
- collection_type: postman
  name: Flutterwave Webhooks API
  slug: postman-flutterwave-webhooks-api
- collection_type: open
  name: Flutterwave Banks API
  slug: open-flutterwave-banks-api
- collection_type: open
  name: Flutterwave Payments API
  slug: open-flutterwave-payments-api
- collection_type: open
  name: Flutterwave Settlements API
  slug: open-flutterwave-settlements-api
- collection_type: open
  name: Flutterwave Transfers API
  slug: open-flutterwave-transfers-api
- collection_type: open
  name: Flutterwave Wallets API
  slug: open-flutterwave-wallets-api
- collection_type: open
  name: Flutterwave Webhooks API
  slug: open-flutterwave-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flutterwave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flutterwave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flutterwave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flutterwave-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/flutterwave/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-bank-directory-then-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-charge-and-verify-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-charge-then-dispute-chargeback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-charge-then-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-create-recipient-transfer-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-cross-border-rate-locked-transfer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-direct-orchestrator-transfer-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-mobile-money-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-orchestrator-charge-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-orchestrator-order-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-order-checkout-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-quote-fee-then-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-resolve-account-then-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-reuse-recipient-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-settlement-reconciliation-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-tokenized-recurring-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-transfer-verify-and-retry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-upsert-customer-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-virtual-account-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/flutterwave-wallet-balance-guarded-payout-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://flutterwave.com
- group: start
  title: ''
  type: Portal
  url: https://developer.flutterwave.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.flutterwave.com/docs/getting-started.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/authentication.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/api-headers.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/encryption.md
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.flutterwave.com/docs/common-errors.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/webhooks.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/idempotency.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/testing.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/best-practices.md
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flutterwave.com/docs/environments.md
- group: start
  title: ''
  type: Signup
  url: https://onboarding.flutterwave.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flutterwave.com
- group: operate
  title: ''
  type: Support
  url: https://support.flutterwave.com
- group: commercial
  title: ''
  type: Pricing
  url: https://flutterwave.com/us/pricing
- group: company
  title: ''
  type: Blog
  url: https://flutterwave.com/us/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flutterwave.com/us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flutterwave.com/us/privacy-notice
- group: operate
  title: ''
  type: Contact
  url: https://flutterwave.com/us/contact-sales
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flutterwave
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/theflutterwave
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flutterwave
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Node-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/PHP-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Python-v2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Ruby-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Java-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Dotnet-v2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/React-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Angular-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Vue-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/Flutter-v3
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/React-Native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/AndroidSDK
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Flutterwave/iOS-v3
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Flutterwave/WordPress-v2
- group: commercial
  title: ''
  type: Plans
  url: plans/flutterwave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flutterwave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flutterwave-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/flutterwave-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/flutterwave-vocabulary.yml
created: '2026-05-24'
description: Flutterwave is a pan-African payment infrastructure company providing the rails for businesses to accept, send, and manage money across Africa and globally. The Flutterwave for Business (F4B) v4 API exposes a unified surface for collections (cards, mobile money, bank transfer, USSD, OPay, virtual NUBANs), payouts (bank, mobile money, wallet-to-wallet across 30+ countries), real-time FX conversion, settlements, refunds, chargebacks, multi-currency wallets, KYC, card issuing, and bill payments. Flutterwave is one of the most valuable African fintech companies (unicorn status) and processes 20M+ API calls and 500k+ payments per day.
examples:
- key_count: 2
  name: Flutterwave Charge Completed Webhook Example
  slug: flutterwave-charge-completed-webhook-example
- key_count: 2
  name: Flutterwave Create Charge Example
  slug: flutterwave-create-charge-example
- key_count: 2
  name: Flutterwave Create Customer Example
  slug: flutterwave-create-customer-example
- key_count: 2
  name: Flutterwave Create Refund Example
  slug: flutterwave-create-refund-example
- key_count: 2
  name: Flutterwave Create Transfer Example
  slug: flutterwave-create-transfer-example
features:
- Accept payments via cards (local + international), mobile money (M-Pesa, MTN, Airtel, Tigo, Vodafone, OPay), bank transfers, USSD, and QR
- Real-time payouts to bank accounts and mobile wallets across 30+ African countries plus US/UK/EU/Asia corridors
- Virtual NUBANs (Nigerian Uniform Bank Account Numbers) for pay-with-bank-transfer collections
- Cross-border remittance with built-in KYC for senders and recipients
- Real-time FX conversion via the Transfer Rates endpoints
- Multi-currency wallets (30+ currencies) with statements and balance APIs
- Orchestrator helpers that combine customer creation, payment method tokenisation, and charge in one call
- Idempotency via `X-Idempotency-Key` (UUID) returned on retry with `X-Idempotency-Cache-Hit: true`
- AES-256 client-side encryption for sensitive card fields with a per-request 12-character nonce
- OAuth 2.0 Client Credentials with 10-minute bearer tokens issued by Keycloak IDP
- Webhooks for `charge.completed`, transfer completion, refunds, chargebacks, and virtual account funding
- Card Issuing (virtual cards) and Card Acquiring services
- Bill Payments and KYC services
- Settlements, refunds, chargebacks, and fee computation endpoints for finance and operations
- Industry solutions for Fintechs, Banks/OFIs, Travel/Hospitality, E-commerce, Remittance, Telecommunications, Loan Disbursements
- Hosted checkout via Payment Links and Standard payment flow
- Free ecommerce tooling (Store, Invoices, Disha) for SMEs
- Send App (consumer remittance), Swap (FX), Afritickets (event ticketing), Market (online marketplace), Tuition (school fees)
- Test card and test mobile money number library for sandbox validation
- Sandbox and production environments at `api.flutterwave.cloud/f4b/sandbox` and `.../production`
- Official SDKs for Node.js, PHP, Python, Ruby, Java, .NET plus frontend SDKs for React, Angular, Vue, Flutter, React Native, Android, iOS, and a WordPress plugin
finops:
- name: Flutterwave Finops
  service_category: Payments and Fintech Infrastructure
  slug: flutterwave-finops
graphqls:
- description: This document describes a GraphQL schema representation of the Flutterwave Payments API. Flutterwave's native interface is REST-based; this schema is a conceptual mapping of core domain types to Graph
  name: Flutterwave GraphQL Schema
  slug: flutterwave-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flutterwave.png
json_schemas:
- name: Flutterwave Charge
  property_count: 11
  slug: flutterwave-charge
- name: Flutterwave Customer
  property_count: 7
  slug: flutterwave-customer
- name: Flutterwave Settlement
  property_count: 10
  slug: flutterwave-settlement
- name: Flutterwave Transfer
  property_count: 12
  slug: flutterwave-transfer
- name: Flutterwave Wallet Balance
  property_count: 4
  slug: flutterwave-wallet
json_structures:
- name: Flutterwave Charge Structure
  property_count: 0
  slug: flutterwave-charge-structure
jsonld:
- class_count: 0
  name: Flutterwave Context
  property_count: 10
  slug: flutterwave-context
layout: provider
modified: '2026-05-30'
name: Flutterwave
nav: Providers
network: true
overview: 'Flutterwave publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Transfers API, Settlements API, Wallets API, and 16 more. Tagged areas include Payments, Payouts, Mobile Money, Cards, and Africa.


  The Flutterwave catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Flutterwave''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, support, pricing, and 63 more developer resources.'
plans:
- name: Flutterwave Plans Pricing
  plan_count: 9
  slug: flutterwave-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 0
  name: Flutterwave Rate Limits
  slug: flutterwave-rate-limits
rules:
- name: Flutterwave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: flutterwave-jsonschema-spectral-rules
- name: Flutterwave API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 7
  slug: flutterwave-rules
scopes:
- name: Flutterwave Scopes
  scope_count: 0
  slug: flutterwave-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.2
  delta: -6.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 71.2
    developer_ergonomics: 65.2
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/flutterwave/refs/heads/main/screenshots/flutterwave-2026-06-20T181343.png
security:
- kind: authentication
  name: Flutterwave Authentication
  slug: flutterwave-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Flutterwave Domain Security
  slug: flutterwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flutterwave
tags:
- Payments
- Payouts
- Mobile Money
- Cards
- Africa
- Fintech
- Remittance
- Virtual Accounts
- Chargebacks
- Multi-Currency
website: https://flutterwave.com
---
