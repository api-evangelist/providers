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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 120
  human_in_the_loop: 6
  name: Paystack Agentic Access
  operation_count: 240
  slug: paystack-agentic-access
  summary_line: 240 operations · 120 acting · 6 human-in-the-loop
api_count: 21
apis:
- description: Outbound webhook surface that notifies a single merchant-configured POST endpoint of transaction, dispute, refund, transfer, subscription, invoice, payment request, customer identification, and dedica
  name: Paystack Webhooks
  slug: paystack-webhooks
- description: The Balance API from Paystack — 2 operation(s) for balance.
  name: Paystack Balance API
  slug: paystack-balance-api
- description: The Bulk Charge API from Paystack — 5 operation(s) for bulk charge.
  name: Paystack Bulk Charge API
  slug: paystack-bulk-charge-api
- description: The Charge API from Paystack — 7 operation(s) for charge.
  name: Paystack Charge API
  slug: paystack-charge-api
- description: The Customer API from Paystack — 5 operation(s) for customer.
  name: Paystack Customer API
  slug: paystack-customer-api
- description: The Dedicated Virtual Account API from Paystack — 4 operation(s) for dedicated virtual account.
  name: Paystack Dedicated Virtual Account API
  slug: paystack-dedicated-virtual-account-api
- description: The Dispute API from Paystack — 7 operation(s) for dispute.
  name: Paystack Dispute API
  slug: paystack-dispute-api
- description: The Integration API from Paystack — 1 operation(s) for integration.
  name: Paystack Integration API
  slug: paystack-integration-api
- description: The Page API from Paystack — 4 operation(s) for page.
  name: Paystack Page API
  slug: paystack-page-api
- description: The Payment Request API from Paystack — 7 operation(s) for payment request.
  name: Paystack Payment Request API
  slug: paystack-payment-request-api
- description: The Plan API from Paystack — 2 operation(s) for plan.
  name: Paystack Plan API
  slug: paystack-plan-api
- description: The Product API from Paystack — 2 operation(s) for product.
  name: Paystack Product API
  slug: paystack-product-api
- description: The Refund API from Paystack — 2 operation(s) for refund.
  name: Paystack Refund API
  slug: paystack-refund-api
- description: The Settlement API from Paystack — 2 operation(s) for settlement.
  name: Paystack Settlement API
  slug: paystack-settlement-api
- description: The Split API from Paystack — 4 operation(s) for split.
  name: Paystack Split API
  slug: paystack-split-api
- description: The Subaccount API from Paystack — 2 operation(s) for subaccount.
  name: Paystack Subaccount API
  slug: paystack-subaccount-api
- description: The Subscription API from Paystack — 6 operation(s) for subscription.
  name: Paystack Subscription API
  slug: paystack-subscription-api
- description: The Transaction API from Paystack — 12 operation(s) for transaction.
  name: Paystack Transaction API
  slug: paystack-transaction-api
- description: The Transfer API from Paystack — 10 operation(s) for transfer.
  name: Paystack Transfer API
  slug: paystack-transfer-api
- description: The Transfer Recipient API from Paystack — 3 operation(s) for transfer recipient.
  name: Paystack Transfer Recipient API
  slug: paystack-transfer-recipient-api
- description: The Verification API from Paystack — 7 operation(s) for verification.
  name: Paystack Verification API
  slug: paystack-verification-api
arazzos:
- description: Create a new subaccount, add it to an existing transaction split, then fetch the split to confirm membership.
  name: Paystack Add a Subaccount to an Existing Split
  slug: paystack-add-subaccount-to-split-workflow
- description: List the disputes raised against a transaction, fetch the customer, then blacklist them and deactivate the card authorization.
  name: Paystack Blacklist a Customer After a Dispute
  slug: paystack-blacklist-customer-after-dispute-workflow
- description: Bulk-create transfer recipients, list them to confirm registration, then initiate a bulk transfer to pay them all.
  name: Paystack Bulk Recipients and Bulk Transfer
  slug: paystack-bulk-recipients-and-bulk-transfer-workflow
- description: Initialize and verify a transaction, then create a refund against it and fetch the refund status.
  name: Paystack Charge and Refund a Transaction
  slug: paystack-charge-and-refund-transaction-workflow
- description: Create a direct charge, branch when an OTP is required, submit the OTP, then check the final charge status.
  name: Paystack Create Charge and Submit OTP
  slug: paystack-charge-and-submit-otp-workflow
- description: Create a direct card charge, branch when a PIN is required, submit the PIN, then check the final charge status.
  name: Paystack Create Charge and Submit PIN
  slug: paystack-charge-and-submit-pin-workflow
- description: Check that an authorization can bear a charge, then take a partial debit against it for whatever is available.
  name: Paystack Check Authorization and Partial Debit
  slug: paystack-check-authorization-and-partial-debit-workflow
- description: Create a customer, initialize a first transaction, verify it to obtain an authorization, then charge that authorization for a recurring debit.
  name: Paystack Create Customer and Charge Authorization
  slug: paystack-create-customer-and-charge-authorization-workflow
- description: Create a customer, raise an invoice-style payment request for them, send the email notification, then verify the request.
  name: Paystack Create Customer and Send Payment Request
  slug: paystack-create-customer-and-payment-request-workflow
- description: Look up an available bank provider, create a customer, assign a dedicated NUBAN virtual account, then fetch its details.
  name: Paystack Provision a Dedicated Virtual Account
  slug: paystack-create-customer-dedicated-virtual-account-workflow
- description: Create a customer, define a billing plan, then subscribe the customer to the plan for recurring charges.
  name: Paystack Create Customer, Plan and Subscription
  slug: paystack-create-customer-plan-and-subscription-workflow
- description: Create a product, check a page slug is available, create a hosted payment page, then attach the product to the page.
  name: Paystack Create Product and Payment Page
  slug: paystack-create-product-and-payment-page-workflow
- description: Create a transfer recipient from bank details, initiate a transfer to it, then verify the transfer by reference.
  name: Paystack Create Recipient and Initiate Transfer
  slug: paystack-create-recipient-and-initiate-transfer-workflow
- description: Create a subaccount, build a transaction split that pays it, then initialize a transaction against the split.
  name: Paystack Create Subaccount and Transaction Split
  slug: paystack-create-subaccount-and-split-workflow
- description: Fetch a subscription to read its email token, disable it, then re-enable it using the same code and token.
  name: Paystack Disable and Re-enable a Subscription
  slug: paystack-disable-and-reenable-subscription-workflow
- description: Fetch a dispute, attach evidence to it, request an upload URL for supporting files, then resolve the dispute.
  name: Paystack Submit Dispute Evidence and Resolve
  slug: paystack-dispute-evidence-and-resolve-workflow
- description: Create a draft payment request, finalize it to issue the invoice, verify it, then archive it once handled.
  name: Paystack Finalize and Archive a Draft Payment Request
  slug: paystack-finalize-and-archive-payment-request-workflow
- description: Initialize a checkout transaction and then verify its final status by reference.
  name: Paystack Initialize and Verify Transaction
  slug: paystack-initialize-and-verify-transaction-workflow
- description: Initiate a transfer, finalize it with the OTP sent to the business phone, then verify the completed transfer.
  name: Paystack Initiate and Finalize Transfer with OTP
  slug: paystack-initiate-and-finalize-transfer-workflow
- description: Initiate a bulk charge batch against saved authorizations, fetch the batch, then list the charges in the batch.
  name: Paystack Initiate and Monitor a Bulk Charge
  slug: paystack-initiate-and-monitor-bulk-charge-workflow
- description: Resolve a bank account number to confirm the account name, then create a transfer recipient and initiate a transfer.
  name: Paystack Resolve Account and Create Transfer Recipient
  slug: paystack-resolve-account-and-create-recipient-workflow
- description: Resolve a card BIN to learn the card brand and country, then charge a saved authorization for that card.
  name: Paystack Resolve Card BIN and Charge Authorization
  slug: paystack-resolve-card-bin-and-charge-workflow
- description: Fetch settlement records, then list the transactions that make up a chosen settlement payout.
  name: Paystack Settlement Reconciliation
  slug: paystack-settlement-reconciliation-workflow
- description: Create a subscription, fetch it to read its status, then generate a self-service management link for the customer.
  name: Paystack Subscribe and Generate a Management Link
  slug: paystack-subscribe-and-generate-manage-link-workflow
- description: Create a customer, resolve their BVN, then submit a bank-account identification to validate the customer.
  name: Paystack Create and Validate Customer (KYC)
  slug: paystack-validate-customer-kyc-workflow
artifact_total: 148
asyncapis:
- description: AsyncAPI 2.6 description of Paystack's outbound webhook surface. Paystack notifies a single merchant-configured POST endpoint (the "webhook URL") whenever an event occurs against your integration. Eve
  name: Paystack Webhooks
  slug: paystack-webhooks-asyncapi
collections:
- collection_type: postman
  name: Paystack Accept Payments API
  slug: postman-paystack-accept-payments
- collection_type: postman
  name: Paystack Balance API
  slug: postman-paystack-balance
- collection_type: postman
  name: Paystack Customers API
  slug: postman-paystack-customers
- collection_type: postman
  name: Paystack Dedicated Virtual Accounts API
  slug: postman-paystack-dedicated-virtual-accounts
- collection_type: postman
  name: Paystack Integration Settings API
  slug: postman-paystack-integration
- collection_type: postman
  name: Paystack Payment Requests API
  slug: postman-paystack-payment-requests
- collection_type: postman
  name: Paystack Products and Payment Pages API
  slug: postman-paystack-products-pages
- collection_type: postman
  name: Paystack Refunds and Disputes API
  slug: postman-paystack-refunds-disputes
- collection_type: postman
  name: Paystack Settlements API
  slug: postman-paystack-settlements
- collection_type: postman
  name: Paystack Splits and Subaccounts API
  slug: postman-paystack-splits-subaccounts
- collection_type: postman
  name: Paystack Subscriptions API
  slug: postman-paystack-subscriptions
- collection_type: postman
  name: Paystack Transfers API
  slug: postman-paystack-transfers
- collection_type: postman
  name: Paystack Verification API
  slug: postman-paystack-verification
- collection_type: open
  name: Paystack Accept Payments API
  slug: open-paystack-accept-payments
- collection_type: open
  name: Paystack Balance API
  slug: open-paystack-balance
- collection_type: open
  name: Paystack Customers API
  slug: open-paystack-customers
- collection_type: open
  name: Paystack Dedicated Virtual Accounts API
  slug: open-paystack-dedicated-virtual-accounts
- collection_type: open
  name: Paystack Integration Settings API
  slug: open-paystack-integration
- collection_type: open
  name: Paystack Payment Requests API
  slug: open-paystack-payment-requests
- collection_type: open
  name: Paystack Products and Payment Pages API
  slug: open-paystack-products-pages
- collection_type: open
  name: Paystack Refunds and Disputes API
  slug: open-paystack-refunds-disputes
- collection_type: open
  name: Paystack Settlements API
  slug: open-paystack-settlements
- collection_type: open
  name: Paystack Splits and Subaccounts API
  slug: open-paystack-splits-subaccounts
- collection_type: open
  name: Paystack Subscriptions API
  slug: open-paystack-subscriptions
- collection_type: open
  name: Paystack Transfers API
  slug: open-paystack-transfers
- collection_type: open
  name: Paystack Verification API
  slug: open-paystack-verification
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paystack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paystack-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paystack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paystack-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paystack/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-add-subaccount-to-split-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-blacklist-customer-after-dispute-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-bulk-recipients-and-bulk-transfer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-charge-and-refund-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-charge-and-submit-otp-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-charge-and-submit-pin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-check-authorization-and-partial-debit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-customer-and-charge-authorization-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-customer-and-payment-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-customer-dedicated-virtual-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-customer-plan-and-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-product-and-payment-page-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-recipient-and-initiate-transfer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-create-subaccount-and-split-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-disable-and-reenable-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-dispute-evidence-and-resolve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-finalize-and-archive-payment-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-initialize-and-verify-transaction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-initiate-and-finalize-transfer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-initiate-and-monitor-bulk-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-resolve-account-and-create-recipient-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-resolve-card-bin-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-settlement-reconciliation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-subscribe-and-generate-manage-link-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/paystack-validate-customer-kyc-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://paystack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://paystack.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://paystack.com/docs/api/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PaystackHQ/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://paystack.com/docs/payments/accept-payments/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.paystack.com/#/signup
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.paystack.com/
- group: auth
  title: ''
  type: Authentication
  url: https://paystack.com/docs/api/#authentication
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.paystack.com/#/settings/developers
- group: docs
  title: ''
  type: Documentation
  url: https://paystack.com/docs/payments/webhooks/
- group: docs
  title: ''
  type: Documentation
  url: https://paystack.com/docs/payments/test-payments/
- group: docs
  title: ''
  type: Documentation
  url: https://paystack.com/docs/api/errors/
- group: operate
  title: ''
  type: ChangeLog
  url: https://paystack.com/docs/changelog/api/
- group: company
  title: ''
  type: Blog
  url: https://paystack.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/paystack-engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paystack.com/
- group: operate
  title: ''
  type: Support
  url: https://support.paystack.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/ng/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/gh/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/za/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/ke/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/ci/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://paystack.com/eg/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paystack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paystack.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://paystack.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaystackHQ
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaystackHQ/paystack-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaystackHQ/paystack-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaystackHQ/paystack-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaystackHQ/paystack-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PaystackHQ/omnipay-paystack
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-woocommerce
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-magento-2
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-prestashop-1.7
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-opencart
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-whmcs
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/moodle-enrol_paystack
- group: build
  title: ''
  type: Plugins
  url: https://github.com/PaystackHQ/plugin-odoo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PaystackHQ/PaystackJS-Sample-code
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PaystackHQ/sample-charge-card-backend
- group: design
  title: ''
  type: SpectralRules
  url: rules/paystack-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/paystack-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/paystack-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/paystack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paystack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paystack-finops.yml
created: '2026-05-24'
description: Paystack is an African payment processor (acquired by Stripe in 2020) that lets businesses accept payments in Nigeria, Ghana, South Africa, Kenya, Côte d'Ivoire, and Egypt across cards, bank transfers, USSD, QR, EFT, and mobile money channels. Its single REST API covers one-time charges, recurring subscriptions, marketplace splits, dedicated virtual accounts, invoices, transfers (payouts), refunds, disputes, settlements, and KYC/identity verification — all wrapped in a developer experience that has made it one of the most respected public APIs on the continent.
examples:
- key_count: 4
  name: Paystack Create Dedicated Account Example
  slug: paystack-create-dedicated-account-example
- key_count: 4
  name: Paystack Create Split Example
  slug: paystack-create-split-example
- key_count: 4
  name: Paystack Create Subscription Example
  slug: paystack-create-subscription-example
- key_count: 4
  name: Paystack Initialize Transaction Example
  slug: paystack-initialize-transaction-example
- key_count: 4
  name: Paystack Initiate Transfer Example
  slug: paystack-initiate-transfer-example
- key_count: 4
  name: Paystack Verify Transaction Example
  slug: paystack-verify-transaction-example
features:
- description: Paystack-hosted authorization URL that handles PCI, SCA, OTP, USSD, QR, and 3DS flows for you.
  name: Hosted Checkout
- description: Initiate charges programmatically with structured PIN, OTP, phone, birthday, and address challenge steps.
  name: Direct Charge API
- description: Plans plus subscriptions with self-service customer management and email/SMS invoice notifications.
  name: Recurring Subscriptions
- description: Route a single payment to multiple subaccounts on a percentage or flat basis for marketplaces.
  name: Transaction Splits
- description: Vendor or merchant profiles with their own settlement bank and percentage charge.
  name: Subaccounts
- description: NUBAN virtual accounts assigned to individual customers for bank-transfer-based payments with auto-reconciliation.
  name: Dedicated Virtual Accounts
- description: No-code Paystack-hosted pages for selling products or accepting donations.
  name: Payment Pages
- description: Email-based invoices with verification, notification, finalization, and archive flows.
  name: Payment Requests
- description: Pay out from balance to bank accounts and mobile money wallets, one at a time or as batches.
  name: Single and Bulk Transfers
- description: Charge many stored authorizations in a single batch with pause and resume controls.
  name: Bulk Charge
- description: Partial or full refunds with merchant and customer notes.
  name: Refunds
- description: Programmatic dispute response with signed evidence-upload URLs and resolution workflow.
  name: Disputes and Chargebacks
- description: Read net settlement payouts and drill down into the transactions that composed each batch.
  name: Settlements
- description: BVN match, BVN resolution, account number resolution, card BIN lookup, country/bank lookup, and AVS state lists.
  name: Identity Verification
- description: Accept NGN, GHS, ZAR, KES, XOF, EGP, and USD across supported markets.
  name: Multi-Currency
- description: Card, bank transfer, USSD, QR, mobile money (M-Pesa, MTN MoMo, Orange Money, Wave), EFT, Apple Pay, Visa QR.
  name: Multi-Channel
- description: Signed webhook deliveries for transaction, dispute, refund, transfer, subscription, and invoice events with 72-hour retries.
  name: Webhooks
- description: A complete test environment with test cards covering success, decline, OTP, PIN, and 3DS flows.
  name: Test Mode
- description: First-class merchant dashboard for transactions, customers, subscriptions, transfers, settlements, and disputes.
  name: Dashboard
finops:
- name: Paystack Finops
  service_category: Financial Services — Payment Processing
  slug: paystack-finops
graphqls:
- description: This document describes a GraphQL schema that represents the Paystack REST API domain model. Paystack is a Nigerian payments platform (acquired by Stripe in 2020) that provides payment processing acro
  name: Paystack GraphQL Schema
  slug: paystack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paystack.png
integrations:
- description: Official Paystack payment gateway for WooCommerce stores.
  name: WooCommerce
- description: Official Magento extensions for Paystack acceptance.
  name: Magento and Magento 2
- description: Plugins for PrestaShop 1.6 and 1.7.
  name: PrestaShop
- description: OpenCart extensions for Paystack.
  name: OpenCart
- description: Hosting and billing platform integration.
  name: WHMCS
- description: Course enrolment via Paystack.
  name: Moodle
- description: Payment gateway integration for Odoo 14.
  name: Odoo
- description: Paystack gateway driver for the PHP Omnipay payment-abstraction library.
  name: Omnipay
- description: Community and official plugins across major CMS platforms.
  name: Joomla, Drupal, Ghost, Wordpress
- description: Paystack is a Stripe subsidiary; merchants can operate in Stripe-aligned multi-region setups.
  name: Stripe
json_schemas:
- name: Paystack Customer
  property_count: 11
  slug: paystack-customer
- name: Paystack Dispute
  property_count: 13
  slug: paystack-dispute
- name: Paystack Plan
  property_count: 12
  slug: paystack-plan
- name: Paystack Refund
  property_count: 12
  slug: paystack-refund
- name: Paystack Transaction Split
  property_count: 12
  slug: paystack-split
- name: Paystack Subaccount
  property_count: 16
  slug: paystack-subaccount
- name: Paystack Subscription
  property_count: 12
  slug: paystack-subscription
- name: Paystack Transaction
  property_count: 14
  slug: paystack-transaction
- name: Paystack Transfer
  property_count: 12
  slug: paystack-transfer
json_structures:
- name: Paystack Customer Structure
  property_count: 11
  slug: paystack-customer-structure
- name: Paystack Split Structure
  property_count: 12
  slug: paystack-split-structure
- name: Paystack Subscription Structure
  property_count: 12
  slug: paystack-subscription-structure
- name: Paystack Transaction Structure
  property_count: 14
  slug: paystack-transaction-structure
- name: Paystack Transfer Structure
  property_count: 12
  slug: paystack-transfer-structure
jsonld:
- class_count: 41
  name: Paystack Context
  property_count: 4
  slug: paystack-context
layout: provider
modified: '2026-05-30'
name: Paystack
nav: Providers
network: true
overview: 'Paystack publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Balance API, Bulk Charge API, and 18 more. Tagged areas include Payments, Africa, Fintech, Recurring Billing, and Marketplaces.


  The Paystack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Paystack''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, changelog, and 70 more developer resources.'
plans:
- name: Paystack Plans Pricing
  plan_count: 8
  slug: paystack-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 6
  name: Paystack Rate Limits
  slug: paystack-rate-limits
rules:
- name: Paystack API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: paystack-asyncapi-spectral-rules
- name: Paystack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: paystack-jsonschema-spectral-rules
- name: Paystack API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 7
  slug: paystack-rules
score:
  band: exemplar
  composite: 68.2
  delta: -4.2
  facets:
    commercial_clarity: 78.9
    contract_quality: 78.6
    developer_ergonomics: 71.7
    discoverability: 59.3
    governance: 52.1
    operational_transparency: 68.4
  previous_composite: 72.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paystack/refs/heads/main/screenshots/paystack-2026-06-20T191508.png
security:
- kind: authentication
  name: Paystack Authentication
  slug: paystack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paystack Domain Security
  slug: paystack-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Paystack Trust Center
  slug: paystack-trust-center
  summary_line: ISO 27001
slug: paystack
solutions:
- description: Hosted checkout for e-commerce and SaaS.
  name: Online Businesses
- description: Splits + subaccounts for multi-vendor platforms.
  name: Marketplaces
- description: Plans, subscriptions, and dunning for recurring revenue.
  name: Subscription Businesses
- description: Transfers, dedicated virtual accounts, and identity verification for fintech and platform builds.
  name: Platforms and Apps
- description: Payment Pages and Payment Requests for donations and tuition collection.
  name: Education and Nonprofits
tags:
- Payments
- Africa
- Fintech
- Recurring Billing
- Marketplaces
- Payouts
- Mobile Money
- Stripe
use_cases:
- description: Drop-in checkout for online stores accepting cards, USSD, bank transfer, and mobile money across Africa.
  name: E-commerce Checkout
- description: Subscription-based revenue with plans, automatic renewal, self-service updates, and dunning.
  name: SaaS Recurring Billing
- description: Split-payment routing to vendor subaccounts with platform fee retention.
  name: Marketplaces and Multi-Vendor Platforms
- description: Accept cards from international customers while settling locally.
  name: Cross-Border Payments
- description: M-Pesa, MTN, Orange Money, Wave acceptance in Ghana, Kenya, Côte d'Ivoire.
  name: Mobile Money Acceptance
- description: Dedicated virtual accounts auto-reconcile inbound NUBAN transfers.
  name: Bank Transfer Acceptance
- description: Single and bulk transfers to bank or mobile money for gig platforms and payroll-light apps.
  name: Payouts and Vendor Disbursement
- description: Issue payment requests by email with verification and reminders.
  name: Invoicing and B2B Collections
- description: Payment Pages for one-off donations or product sales without writing checkout code.
  name: Donations and Crowdfunding
website: https://paystack.com/
---
