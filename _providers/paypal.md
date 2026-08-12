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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 75
  human_in_the_loop: 0
  name: Paypal Agentic Access
  operation_count: 111
  slug: paypal-agentic-access
  summary_line: 111 operations · 75 acting
api_count: 37
apis:
- description: The Activate API from PayPal — 2 operation(s) for activate.
  name: PayPal Activate API
  slug: paypal-activate-api
- description: Use the `/authorizations` resource to show details for, capture payment for, reauthorize, and void authorized payments.
  name: PayPal Authorizations API
  slug: paypal-authorizations-api
- description: Use the `/balances` resource to list balances.
  name: PayPal Balances API
  slug: paypal-balances-api
- description: The Billing API from PayPal — 13 operation(s) for billing.
  name: PayPal Billing API
  slug: paypal-billing-api
- description: The Cancel API from PayPal — 1 operation(s) for cancel.
  name: PayPal Cancel API
  slug: paypal-cancel-api
- description: The Capture API from PayPal — 1 operation(s) for capture.
  name: PayPal Capture API
  slug: paypal-capture-api
- description: Use the `/captures` resource to show details for and refund a captured payment.
  name: PayPal Captures API
  slug: paypal-captures-api
- description: The Deactivate API from PayPal — 1 operation(s) for deactivate.
  name: PayPal Deactivate API
  slug: paypal-deactivate-api
- description: Use the `/disputes` resource with a dispute ID and an action to:<ul><li>Accept a claim.</li><li>Accept an offer to resolve a dispute.</li><li>Acknowledge the return of an item related to a dispute.</l
  name: PayPal Disputes-Actions API
  slug: paypal-disputes-actions-api
- description: Use the `/disputes` resource to list disputes, create disputes, show dispute details, and partially a dispute. Normally, an agent at PayPal creates disputes but now you can run test cases in the sandb
  name: PayPal Disputes API
  slug: paypal-disputes-api
- description: Use the `/invoices` resource to create, update, and send invoices and invoice reminders. To manage invoices, you can also list invoices, show details for invoices, delete draft invoices, and cancel se
  name: PayPal Invoices API
  slug: paypal-invoices-api
- description: Use the `/orders` resource to create, update, retrieve, authorize, capture and track orders.
  name: PayPal Orders API
  slug: paypal-orders-api
- description: Enables you to create and get information about shared customer data.
  name: PayPal Partner-Referrals API
  slug: paypal-partner-referrals-api
- description: Use the `/vault/payment-tokens` resource to create, retrieve, and delete a payment token that may optionally be associated with a customer.
  name: PayPal Payment-Tokens API
  slug: paypal-payment-tokens-api
- description: Use the `/payouts` resource to create a batch payout, update the status for a batch payout, show the status of a batch payout with the transaction status and other data for individual payout items, an
  name: PayPal Payouts API
  slug: paypal-payouts-api
- description: Use the `/payouts-item` resource to show payout item details and cancel an unclaimed payout item.
  name: PayPal Payouts-Item API
  slug: paypal-payouts-item-api
- description: The Plans API from PayPal — 5 operation(s) for plans.
  name: PayPal Plans API
  slug: paypal-plans-api
- description: The Pricing API from PayPal — 1 operation(s) for pricing.
  name: PayPal Pricing API
  slug: paypal-pricing-api
- description: Use `/products` resource to create and manage products.
  name: PayPal Products API
  slug: paypal-products-api
- description: Use the `/refunds` resource to show refund details.
  name: PayPal Refunds API
  slug: paypal-refunds-api
- description: The Revise API from PayPal — 1 operation(s) for revise.
  name: PayPal Revise API
  slug: paypal-revise-api
- description: The Schemes API from PayPal — 1 operation(s) for schemes.
  name: PayPal Schemes API
  slug: paypal-schemes-api
- description: Use the `/search-invoices` resource to search for and list invoices that match search criteria.
  name: PayPal Search-Invoices API
  slug: paypal-search-invoices-api
- description: Use the `/vault/setup-tokens` resource to create and retrieve temporary vault payment methods.
  name: PayPal Setup-Tokens API
  slug: paypal-setup-tokens-api
- description: Use the `/simulate-event` resource to use a sample payload to simulate a webhook event. The events that this call generates only serve to validate the connection to the listener URL and to show how we
  name: PayPal Simulate-Event API
  slug: paypal-simulate-event-api
- description: The Subscriptions API from PayPal — 8 operation(s) for subscriptions.
  name: PayPal Subscriptions API
  slug: paypal-subscriptions-api
- description: The Suspend API from PayPal — 1 operation(s) for suspend.
  name: PayPal Suspend API
  slug: paypal-suspend-api
- description: 'Use the `/templates` resource to create, list, show details for, update, and delete invoice templates. Use the `/templates` resource when you create a third-party invoicing application. For instance, '
  name: PayPal Templates API
  slug: paypal-templates-api
- description: Use the `/trackers` resource to update and retrieve tracking information for PayPal orders.
  name: PayPal Trackers API
  slug: paypal-trackers-api
- description: Use the `/trackers-batch` resource to add tracking information for multiple PayPal transactions.
  name: PayPal Trackers-Batch API
  slug: paypal-trackers-batch-api
- description: The Transactions API from PayPal — 2 operation(s) for transactions.
  name: PayPal Transactions API
  slug: paypal-transactions-api
- description: Use the `/verify-webhook-signature` resource to verify a webhook signature.
  name: PayPal Verify-Webhook-Signature API
  slug: paypal-verify-webhook-signature-api
- description: Use the `/payment-experience/web-profiles` resource to create, show details for, list, update, partially update, and delete web experience profiles.
  name: PayPal Web-Profiles API
  slug: paypal-web-profiles-api
- description: Use the `/webhooks` resource to subscribe your webhook listener to events, list webhooks for an app, show details for, update, delete, and list event subscriptions for webhooks.
  name: PayPal Webhooks API
  slug: paypal-webhooks-api
- description: Use the `/webhooks-event-types` resource to list available events to which any webhook can subscribe.
  name: PayPal Webhooks-Event-Types API
  slug: paypal-webhooks-event-types-api
- description: Use the `/webhooks-events` resource to list, show details for, and resend event notifications.
  name: PayPal Webhooks-Events API
  slug: paypal-webhooks-events-api
- description: Use the `/webhooks-lookup` resource to create, list, show details for, and delete webhook lookups.
  name: PayPal Webhooks-Lookup API
  slug: paypal-webhooks-lookup-api
artifact_total: 709
collections:
- collection_type: postman
  name: Paypal Subscriptions Authorizations Activate API
  slug: postman-paypal-activate-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations API
  slug: postman-paypal-authorizations-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Balances API
  slug: postman-paypal-balances-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Billing API
  slug: postman-paypal-billing-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Cancel API
  slug: postman-paypal-cancel-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Capture API
  slug: postman-paypal-capture-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Captures API
  slug: postman-paypal-captures-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Deactivate API
  slug: postman-paypal-deactivate-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Disputes-Actions API
  slug: postman-paypal-disputes-actions-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Disputes API
  slug: postman-paypal-disputes-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Invoices API
  slug: postman-paypal-invoices-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Orders API
  slug: postman-paypal-orders-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Partner-Referrals API
  slug: postman-paypal-partner-referrals-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Payment-Tokens API
  slug: postman-paypal-payment-tokens-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Payouts API
  slug: postman-paypal-payouts-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Payouts-Item API
  slug: postman-paypal-payouts-item-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Plans API
  slug: postman-paypal-plans-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Pricing API
  slug: postman-paypal-pricing-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Products API
  slug: postman-paypal-products-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Refunds API
  slug: postman-paypal-refunds-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Revise API
  slug: postman-paypal-revise-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Schemes API
  slug: postman-paypal-schemes-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Search-Invoices API
  slug: postman-paypal-search-invoices-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Setup-Tokens API
  slug: postman-paypal-setup-tokens-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Simulate-Event API
  slug: postman-paypal-simulate-event-api
- collection_type: postman
  name: Paypal Authorizations Subscriptions API
  slug: postman-paypal-subscriptions-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Suspend API
  slug: postman-paypal-suspend-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Templates API
  slug: postman-paypal-templates-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Trackers API
  slug: postman-paypal-trackers-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Trackers-Batch API
  slug: postman-paypal-trackers-batch-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Transactions API
  slug: postman-paypal-transactions-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Verify-Webhook-Signature API
  slug: postman-paypal-verify-webhook-signature-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Web-Profiles API
  slug: postman-paypal-web-profiles-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Webhooks API
  slug: postman-paypal-webhooks-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Webhooks-Event-Types API
  slug: postman-paypal-webhooks-event-types-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Webhooks-Events API
  slug: postman-paypal-webhooks-events-api
- collection_type: postman
  name: Paypal Subscriptions Authorizations Webhooks-Lookup API
  slug: postman-paypal-webhooks-lookup-api
common:
- group: other
  title: ''
  type: Subsidiary
  url: https://www.braintreepayments.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://venmo.com/
- group: operate
  title: ''
  type: Community
  url: https://developer.paypal.com/community
- group: build
  title: ''
  type: SDKs
  url: https://developer.paypal.com/sdk/ios/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paypal/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paypal-agentic-access.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paypal-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paypal-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paypal-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/paypal-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paypal-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/paypal-decline-codes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paypal-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paypal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paypal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paypal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paypal-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paypal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paypal
- group: company
  title: ''
  type: Website
  url: https://www.paypal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.paypal.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paypal.com/api/rest/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.paypal.com/api/rest/authentication/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.paypal-status.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paypal.com/us/business/paypal-business-fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paypal.com/us/legalhub/useragreement-full
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paypal.com/us/legalhub/privacy-full
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.paypal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsroom.paypal-corp.com/news
created: '2024-04-14'
description: PayPal is a global online payment system that lets individuals and businesses send and receive money electronically. PayPal exposes a broad surface of REST APIs covering payments, orders, subscriptions, invoicing, payouts, disputes, payment tokens, shipping tracking, transaction reporting, partner referrals, payment experience, and webhook notifications.
examples:
- key_count: 6
  name: Paypal Authorizationscapture Example
  slug: paypal-authorizationscapture-example
- key_count: 6
  name: Paypal Authorizationsreauthorize Example
  slug: paypal-authorizationsreauthorize-example
- key_count: 6
  name: Paypal Capturesrefund Example
  slug: paypal-capturesrefund-example
- key_count: 6
  name: Paypal Customerpayment Tokensget Example
  slug: paypal-customerpayment-tokensget-example
- key_count: 6
  name: Paypal Disputesaccept Offer Example
  slug: paypal-disputesaccept-offer-example
- key_count: 6
  name: Paypal Disputesadjudicate Example
  slug: paypal-disputesadjudicate-example
- key_count: 6
  name: Paypal Disputesdeny Offer Example
  slug: paypal-disputesdeny-offer-example
- key_count: 6
  name: Paypal Disputesescalate Example
  slug: paypal-disputesescalate-example
- key_count: 6
  name: Paypal Disputesmake Offer Example
  slug: paypal-disputesmake-offer-example
- key_count: 6
  name: Paypal Disputesrequire Evidence Example
  slug: paypal-disputesrequire-evidence-example
- key_count: 6
  name: Paypal Ordersconfirm Example
  slug: paypal-ordersconfirm-example
- key_count: 6
  name: Paypal Orderscreate Example
  slug: paypal-orderscreate-example
- key_count: 6
  name: Paypal Orderstrackerspatch Example
  slug: paypal-orderstrackerspatch-example
- key_count: 6
  name: Paypal Partner Referralsread Example
  slug: paypal-partner-referralsread-example
- key_count: 6
  name: Paypal Payment Tokenscreate Example
  slug: paypal-payment-tokenscreate-example
- key_count: 6
  name: Paypal Payoutspost Example
  slug: paypal-payoutspost-example
- key_count: 6
  name: Paypal Planscreate Example
  slug: paypal-planscreate-example
- key_count: 6
  name: Paypal Plansupdate Pricing Schemes Example
  slug: paypal-plansupdate-pricing-schemes-example
- key_count: 6
  name: Paypal Productscreate Example
  slug: paypal-productscreate-example
- key_count: 6
  name: Paypal Productspatch Example
  slug: paypal-productspatch-example
- key_count: 6
  name: Paypal Setup Tokenscreate Example
  slug: paypal-setup-tokenscreate-example
- key_count: 6
  name: Paypal Simulate Eventpost Example
  slug: paypal-simulate-eventpost-example
- key_count: 6
  name: Paypal Subscriptionsactivate Example
  slug: paypal-subscriptionsactivate-example
- key_count: 6
  name: Paypal Subscriptionscancel Example
  slug: paypal-subscriptionscancel-example
- key_count: 6
  name: Paypal Subscriptionscapture Example
  slug: paypal-subscriptionscapture-example
- key_count: 6
  name: Paypal Subscriptionscreate Example
  slug: paypal-subscriptionscreate-example
- key_count: 6
  name: Paypal Subscriptionsrevise Example
  slug: paypal-subscriptionsrevise-example
- key_count: 6
  name: Paypal Subscriptionssuspend Example
  slug: paypal-subscriptionssuspend-example
- key_count: 6
  name: Paypal Verify Webhook Signaturepost Example
  slug: paypal-verify-webhook-signaturepost-example
- key_count: 6
  name: Paypal Web Profilepartial Update Example
  slug: paypal-web-profilepartial-update-example
- key_count: 6
  name: Paypal Webhookspost Example
  slug: paypal-webhookspost-example
features:
- 'PayPal Checkout: 3.49% + $0.49 per transaction'
- 'Standard Credit/Debit Card: 2.99% + $0.49'
- 'QR Code Transactions: 2.29% + $0.09'
- 'POS Card Present: 2.29% + $0.09'
- 'POS Manual Entry: 3.49% + $0.09'
- 'Invoicing ACH: 1% (capped $10)'
- 'International transactions: +1.50% surcharge'
- 200+ markets, 25 currencies
- REST API at api-m.paypal.com
- OAuth 2.0 client credentials
- Sandbox at 20 req/min for testing
- Webhooks for payment events (signed)
- Smart Payment Buttons (JS SDK)
- Hosted Card Fields and Advanced Credit/Debit Card
- Subscriptions and Recurring Billing
- Buyer and Seller Protection programs
finops:
- name: Paypal Finops
  service_category: Payments
  slug: paypal-finops
graphqls:
- description: This conceptual GraphQL schema represents the PayPal payments platform surface, covering REST APIs for Orders, Payments, Payouts, Subscriptions, Invoicing, Reporting, Disputes, Shipping Tracking, Vaul
  name: PayPal GraphQL Schema
  slug: paypal-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paypal.png
json_schemas:
- name: Accepted Response
  property_count: 1
  slug: paypal-202-response
- name: 3ds_result
  property_count: 0
  slug: paypal-3ds-result
- name: '400'
  property_count: 1
  slug: paypal-400
- name: '401'
  property_count: 1
  slug: paypal-401
- name: '403'
  property_count: 1
  slug: paypal-403
- name: '404'
  property_count: 1
  slug: paypal-404
- name: '409'
  property_count: 1
  slug: paypal-409
- name: '422'
  property_count: 1
  slug: paypal-422
- name: Accept Claim Response Options
  property_count: 1
  slug: paypal-accept-claim-response-options
- name: Accept Claim Type
  property_count: 0
  slug: paypal-accept-claim-type
- name: Accept Offer Request
  property_count: 1
  slug: paypal-accept-offer
- name: account_id-2
  property_count: 0
  slug: paypal-account-id-2
- name: PayPal Account Identifier
  property_count: 0
  slug: paypal-account-id
- name: Account
  property_count: 2
  slug: paypal-account
- name: ACH Debit Response
  property_count: 0
  slug: paypal-ach-debit-response-2
- name: ach_debit_response
  property_count: 0
  slug: paypal-ach-debit-response
- name: ach_debit_verification_status
  property_count: 0
  slug: paypal-ach-debit-verification-status
- name: Acknowledge Return Item Response Options
  property_count: 1
  slug: paypal-acknowledge-return-item-response-options
- name: Allowed Acknowledgement Type
  property_count: 0
  slug: paypal-acknowledgement-type
- name: Evidence Extensions
  property_count: 3
  slug: paypal-action-info
- name: Transaction Date and Time Stamps
  property_count: 2
  slug: paypal-activity-timestamps
- name: address_entity
  property_count: 0
  slug: paypal-address-entity
- name: Portable Postal Address (Medium-Grained)
  property_count: 10
  slug: paypal-address-portable-2
- name: Portable Postal Address (Medium-Grained)
  property_count: 10
  slug: paypal-address-portable
- name: Simple Postal Address (Coarse-Grained)
  property_count: 6
  slug: paypal-address
- name: Settle Request
  property_count: 1
  slug: paypal-adjudicate
- name: adjudication_reason
  property_count: 0
  slug: paypal-adjudication-reason
- name: Adjudication
  property_count: 4
  slug: paypal-adjudication
- name: adjudication_type
  property_count: 0
  slug: paypal-adjudication-type
- name: Aggregated Discount
  property_count: 2
  slug: paypal-aggregated-discount
- name: Agreed Refund Details
  property_count: 2
  slug: paypal-agreed-refund-details
- name: Allowed Response Options
  property_count: 3
  slug: paypal-allowed-response-options
- name: Alternate Notification Method
  property_count: 1
  slug: paypal-alternate-notification-method
- name: altpay_recurring_attributes_request
  property_count: 0
  slug: paypal-altpay-recurring-attributes-request
- name: altpay_recurring_attributes
  property_count: 0
  slug: paypal-altpay-recurring-attributes
- name: Amount Breakdown
  property_count: 7
  slug: paypal-amount-breakdown
- name: Amount Range
  property_count: 2
  slug: paypal-amount-range
- name: Invoice Amount Summary
  property_count: 3
  slug: paypal-amount-summary-detail
- name: Amount with Breakdown
  property_count: 6
  slug: paypal-amount-with-breakdown
- name: apple_pay_attributes
  property_count: 0
  slug: paypal-apple-pay-attributes
- name: Apple Pay Card
  property_count: 0
  slug: paypal-apple-pay-card
- name: Decrypted Apple Pay Token data.
  property_count: 5
  slug: paypal-apple-pay-decrypted-token-data
- name: Decrypted Apple Pay Payment details data.
  property_count: 4
  slug: paypal-apple-pay-payment-data
- name: Apple Pay Response
  property_count: 1
  slug: paypal-apple-pay-payment-token-response
- name: ApplePay payment request object
  property_count: 8
  slug: paypal-apple-pay-request
- name: Application Context
  property_count: 7
  slug: paypal-application-context
- name: Auction Information
  property_count: 4
  slug: paypal-auction-info
- name: authentication_flow
  property_count: 0
  slug: paypal-authentication-flow
- name: Authentication Response
  property_count: 2
  slug: paypal-authentication-response
- name: Authorization
  property_count: 0
  slug: paypal-authorization-2
- name: Authorization
  property_count: 0
  slug: paypal-authorization
- name: Auhorization Status Details
  property_count: 1
  slug: paypal-authorization-status-details
- name: Authorization Status
  property_count: 2
  slug: paypal-authorization-status
- name: Authorization with Additional Data
  property_count: 0
  slug: paypal-authorization-with-additional-data
- name: authorizations.reauthorize-400
  property_count: 1
  slug: paypal-authorizationsreauthorize-400
- name: authorizations.reauthorize-422
  property_count: 1
  slug: paypal-authorizationsreauthorize-422
- name: authorizations.void-422
  property_count: 1
  slug: paypal-authorizationsvoid-422
- name: Balance Information
  property_count: 5
  slug: paypal-balance-detail
- name: Balances Response
  property_count: 4
  slug: paypal-balances-response
- name: Bancontact payment object
  property_count: 4
  slug: paypal-bancontact-request
- name: Bancontact payment object
  property_count: 6
  slug: paypal-bancontact
- name: Bank Response
  property_count: 1
  slug: paypal-bank-response
- name: Bank Account
  property_count: 7
  slug: paypal-bank
- name: Batch status
  property_count: 0
  slug: paypal-batch-enum
- name: Batch Tracker Collection
  property_count: 3
  slug: paypal-batch-tracker-collection
- name: Beneficial_owners
  property_count: 2
  slug: paypal-beneficial-owners
- name: BIC
  property_count: 0
  slug: paypal-bic
- name: billing_agreement_id
  property_count: 0
  slug: paypal-billing-agreement-id
- name: Billing Agreement
  property_count: 5
  slug: paypal-billing-agreement
- name: Billing Cycle Override
  property_count: 3
  slug: paypal-billing-cycle-override
- name: Billing Cycle
  property_count: 5
  slug: paypal-billing-cycle
- name: Billing Disputes Properties
  property_count: 5
  slug: paypal-billing-disputes-properties
- name: Billing Experience Preference
  property_count: 2
  slug: paypal-billing-experience-preference
- name: Billing Information
  property_count: 0
  slug: paypal-billing-info
- name: Bin Details
  property_count: 4
  slug: paypal-bin-details
- name: Birth details
  property_count: 1
  slug: paypal-birth-details
- name: BLIK Experience Context
  property_count: 0
  slug: paypal-blik-experience-context
- name: BLIK one-click payment object
  property_count: 1
  slug: paypal-blik-one-click-response
- name: BLIK one-click payment object
  property_count: 4
  slug: paypal-blik-one-click
- name: BLIK payment object
  property_count: 6
  slug: paypal-blik-request
- name: BLIK payment object
  property_count: 4
  slug: paypal-blik
- name: BLIK level_0 payment object
  property_count: 1
  slug: paypal-blik-seamless
- name: Business_address_detail
  property_count: 0
  slug: paypal-business-address-detail
- name: Business address type
  property_count: 0
  slug: paypal-business-address-type
- name: Business_beneficial_owner
  property_count: 0
  slug: paypal-business-beneficial-owner
- name: Business document
  property_count: 0
  slug: paypal-business-document
- name: Document type
  property_count: 0
  slug: paypal-business-document-type
- name: Business_entity
  property_count: 0
  slug: paypal-business-entity
- name: Business_incorporation
  property_count: 3
  slug: paypal-business-incorporation
- name: Business industry
  property_count: 3
  slug: paypal-business-industry
- name: Business name
  property_count: 0
  slug: paypal-business-name-detail
- name: Business Name
  property_count: 1
  slug: paypal-business-name
- name: The business name type.
  property_count: 0
  slug: paypal-business-name-type
- name: Phone details
  property_count: 0
  slug: paypal-business-phone-detail
- name: Phone type
  property_count: 0
  slug: paypal-business-phone-type
- name: business
  property_count: 9
  slug: paypal-business
- name: The business sub type.
  property_count: 0
  slug: paypal-business-sub-type
- name: Business type information
  property_count: 2
  slug: paypal-business-type-info
- name: Business type
  property_count: 0
  slug: paypal-business-type
- name: buyer_escalation_reason
  property_count: 0
  slug: paypal-buyer-escalation-reason
- name: Customer
  property_count: 1
  slug: paypal-buyer
- name: Canceled Recurring Billing
  property_count: 2
  slug: paypal-canceled-recurring-billing
- name: Cancellation Details
  property_count: 4
  slug: paypal-cancellation-details
- name: Capability
  property_count: 0
  slug: paypal-capabilities
- name: Capture
  property_count: 0
  slug: paypal-capture-2
- name: Capture Request
  property_count: 0
  slug: paypal-capture-request
- name: Capture
  property_count: 0
  slug: paypal-capture
- name: Capture Status Details
  property_count: 1
  slug: paypal-capture-status-details
- name: Capture Status
  property_count: 2
  slug: paypal-capture-status
- name: captures.refund-400
  property_count: 1
  slug: paypal-capturesrefund-400
- name: captures.refund-422
  property_count: 1
  slug: paypal-capturesrefund-422
- name: Card Attributes Response
  property_count: 1
  slug: paypal-card-attributes-response
- name: Card Attributes
  property_count: 2
  slug: paypal-card-attributes
- name: Card Brand
  property_count: 0
  slug: paypal-card-brand
- name: Card Experience Context
  property_count: 2
  slug: paypal-card-experience-context
- name: Response of Card from Request
  property_count: 2
  slug: paypal-card-from-request
- name: Card Request
  property_count: 0
  slug: paypal-card-request
- name: Card Response
  property_count: 4
  slug: paypal-card-response
- name: Card Response with billing address and name
  property_count: 0
  slug: paypal-card-response-with-billing-address
- name: Card
  property_count: 8
  slug: paypal-card
- name: Card Stored Credential
  property_count: 4
  slug: paypal-card-stored-credential
- name: Card Supplementary Data
  property_count: 2
  slug: paypal-card-supplementary-data
- name: Card Type
  property_count: 0
  slug: paypal-card-type
- name: Card Verification Details
  property_count: 5
  slug: paypal-card-verification-details
- name: Card Verification Method
  property_count: 0
  slug: paypal-card-verification-method
- name: Card Verification Status
  property_count: 0
  slug: paypal-card-verification-status
- name: Carrier
  property_count: 0
  slug: paypal-carrier
- name: Cart Information
  property_count: 3
  slug: paypal-cart-info
- name: Checkout Option
  property_count: 2
  slug: paypal-checkout-option
- name: Checkout Payment Intent
  property_count: 0
  slug: paypal-checkout-payment-intent
- name: CLASSIC API integration
  property_count: 0
  slug: paypal-classic-api-integration
- name: cobranded card object
  property_count: 3
  slug: paypal-cobranded-card
- name: Contact Details
  property_count: 3
  slug: paypal-communication-details
- name: Configuration
  property_count: 0
  slug: paypal-configuration
- name: Confirm Order Request
  property_count: 3
  slug: paypal-confirm-order-request
- name: Contact Information
  property_count: 0
  slug: paypal-contact-name-address
- name: country_code-2
  property_count: 0
  slug: paypal-country-code-2
- name: country_code
  property_count: 0
  slug: paypal-country-code
- name: Requested country, transfer method and currency
  property_count: 2
  slug: paypal-country-transfer-method-currency-selection
- name: Create Payout Request
  property_count: 2
  slug: paypal-create-payout-request
- name: Create Referral Data Response
  property_count: 1
  slug: paypal-create-referral-data-response
- name: Credit Not Processed
  property_count: 6
  slug: paypal-credit-not-processed
- name: cryptocurrency_quantity
  property_count: 0
  slug: paypal-cryptocurrency-quantity
- name: Cryptocurrency
  property_count: 2
  slug: paypal-cryptocurrency
- name: cryptocurrency_symbol
  property_count: 0
  slug: paypal-cryptocurrency-symbol
- name: currency_code-2
  property_count: 0
  slug: paypal-currency-code-2
- name: currency_code
  property_count: 0
  slug: paypal-currency-code
- name: Currency Range
  property_count: 2
  slug: paypal-currency-range
- name: Currency
  property_count: 2
  slug: paypal-currency
- name: Custom Amount
  property_count: 2
  slug: paypal-custom-amount
- name: Customer information based on PayPal's system of record
  property_count: 3
  slug: paypal-customer
- name: Vault of a customer
  property_count: 5
  slug: paypal-customer-vault-payment-tokens-response
- name: Billing Cycle Execution Details
  property_count: 6
  slug: paypal-cycle-execution
- name: date_no_time
  property_count: 0
  slug: paypal-date-no-time
- name: Date Range
  property_count: 2
  slug: paypal-date-range
- name: Date and Time Range
  property_count: 2
  slug: paypal-date-time-range
- name: date_time
  property_count: 0
  slug: paypal-date-time
- name: date_year_month
  property_count: 0
  slug: paypal-date-year-month
- name: Deny Offer Request
  property_count: 1
  slug: paypal-deny-offer
- name: dependent_process
  property_count: 0
  slug: paypal-dependent-process
- name: Invoice_Detail
  property_count: 6
  slug: paypal-detail
- name: Disbursement Mode
  property_count: 0
  slug: paypal-disbursement-mode
- name: Discount
  property_count: 2
  slug: paypal-discount
- name: dispute_channel
  property_count: 0
  slug: paypal-dispute-channel
- name: Dispute Summary Information
  property_count: 13
  slug: paypal-dispute-info
- name: dispute_lifecycle_stage
  property_count: 0
  slug: paypal-dispute-lifecycle-stage
- name: Dispute Outcome
  property_count: 3
  slug: paypal-dispute-outcome
- name: Dispute Reason
  property_count: 0
  slug: paypal-dispute-reason
- name: Dispute Details
  property_count: 26
  slug: paypal-dispute
- name: Dispute Search Response
  property_count: 2
  slug: paypal-dispute-search
- name: Dispute State
  property_count: 0
  slug: paypal-dispute-state
- name: Document
  property_count: 2
  slug: paypal-document
- name: Duplicate Transaction
  property_count: 2
  slug: paypal-duplicate-transaction
- name: eci_flag
  property_count: 0
  slug: paypal-eci-flag
- name: email_address
  property_count: 0
  slug: paypal-email-address
- name: email
  property_count: 0
  slug: paypal-email
- name: enrolled
  property_count: 0
  slug: paypal-enrolled
- name: An eps payment object
  property_count: 3
  slug: paypal-eps-request
- name: An eps payment object
  property_count: 3
  slug: paypal-eps
- name: Bad Request Error
  property_count: 5
  slug: paypal-error-400
- name: Unauthorized Error
  property_count: 5
  slug: paypal-error-401
- name: Not Authorized Error
  property_count: 5
  slug: paypal-error-403
- name: Not found Error
  property_count: 5
  slug: paypal-error-404
- name: Resource Conflict Error
  property_count: 5
  slug: paypal-error-409
- name: Unsupported Media Type Error
  property_count: 5
  slug: paypal-error-415
- name: Unprocessable Entity Error
  property_count: 5
  slug: paypal-error-422
- name: Internal Server Error
  property_count: 4
  slug: paypal-error-500
- name: Service Unavailable Error
  property_count: 4
  slug: paypal-error-503
- name: error_default
  property_count: 0
  slug: paypal-error-default
- name: Error Details
  property_count: 5
  slug: paypal-error-details-2
- name: Error Details
  property_count: 5
  slug: paypal-error-details
- name: Link Description
  property_count: 3
  slug: paypal-error-link-description
- name: error_location
  property_count: 0
  slug: paypal-error-location
- name: Error
  property_count: 6
  slug: paypal-error
- name: Escalate Claim Request
  property_count: 2
  slug: paypal-escalate
- name: Event Resend
  property_count: 1
  slug: paypal-event-resend
- name: Event
  property_count: 9
  slug: paypal-event
- name: Event Type
  property_count: 4
  slug: paypal-event-type
- name: Event Version
  property_count: 0
  slug: paypal-event-version
- name: Event List
  property_count: 3
  slug: paypal-eventlist
- name: Event Type List
  property_count: 1
  slug: paypal-eventtypelist
- name: Evidence Information
  property_count: 2
  slug: paypal-evidence-info
- name: Evidence
  property_count: 10
  slug: paypal-evidence
- name: Exchange Rate
  property_count: 3
  slug: paypal-exchange-rate
- name: exemption_details
  property_count: 0
  slug: paypal-exemption-details
- name: Experience Context
  property_count: 5
  slug: paypal-experience-context-base
- name: Experience Context
  property_count: 6
  slug: paypal-experience-context
- name: Extensions
  property_count: 8
  slug: paypal-extensions
- name: Failed Payment Details
  property_count: 4
  slug: paypal-failed-payment-details
- name: Fee Policy
  property_count: 0
  slug: paypal-fee-policy
- name: File Reference
  property_count: 5
  slug: paypal-file-reference
- name: Financial instrument.
  property_count: 1
  slug: paypal-financial-instruments
- name: Billing Cycle Frequency
  property_count: 2
  slug: paypal-frequency
- name: full_name
  property_count: 0
  slug: paypal-full-name
- name: Funding source
  property_count: 0
  slug: paypal-funding-source
- name: A giropay payment object
  property_count: 3
  slug: paypal-giropay-request
- name: A giropay payment object
  property_count: 3
  slug: paypal-giropay
- name: google_pay_request
  property_count: 0
  slug: paypal-google-pay-request
- name: iban_last_chars
  property_count: 0
  slug: paypal-iban-last-chars
- name: The iDEAL payment object
  property_count: 5
  slug: paypal-ideal-request
- name: The iDEAL payment object
  property_count: 5
  slug: paypal-ideal
- name: Bank Account Identifier
  property_count: 2
  slug: paypal-identifier
- name: Incentive Details
  property_count: 4
  slug: paypal-incentive-detail
- name: Incentive Information
  property_count: 1
  slug: paypal-incentive-info
- name: Incorrect Transaction Amount
  property_count: 3
  slug: paypal-incorrect-transaction-amount
- name: Individual_beneficial_owner
  property_count: 0
  slug: paypal-individual-beneficial-owner
- name: Individual_owner
  property_count: 0
  slug: paypal-individual-owner
- name: Individual owner role type
  property_count: 0
  slug: paypal-individual-owner-type
- name: instrument_id
  property_count: 0
  slug: paypal-instrument-id
- name: Integration Details
  property_count: 2
  slug: paypal-integration-details
- name: Invoice Creation Flow
  property_count: 0
  slug: paypal-invoice-creation-flow
- name: Invoice Detail
  property_count: 0
  slug: paypal-invoice-detail
- name: Invoice Number
  property_count: 1
  slug: paypal-invoice-number
- name: Invoice Payment Term
  property_count: 0
  slug: paypal-invoice-payment-term
- name: Invoice
  property_count: 15
  slug: paypal-invoice
- name: Invoice Status
  property_count: 0
  slug: paypal-invoice-status
- name: Invoicer Information
  property_count: 0
  slug: paypal-invoicer-info
- name: Invoices
  property_count: 4
  slug: paypal-invoices
- name: invoices.cancel-400
  property_count: 1
  slug: paypal-invoicescancel-400
- name: invoices.cancel-422
  property_count: 1
  slug: paypal-invoicescancel-422
- name: invoices.create-400
  property_count: 1
  slug: paypal-invoicescreate-400
- name: invoices.generate-qr-code-400
  property_count: 1
  slug: paypal-invoicesgenerate-qr-code-400
- name: invoices.payments-400
  property_count: 1
  slug: paypal-invoicespayments-400
- name: invoices.payments-422
  property_count: 1
  slug: paypal-invoicespayments-422
- name: invoices.payments-delete-422
  property_count: 1
  slug: paypal-invoicespayments-delete-422
- name: invoices.refunds-400
  property_count: 1
  slug: paypal-invoicesrefunds-400
- name: invoices.refunds-422
  property_count: 1
  slug: paypal-invoicesrefunds-422
- name: invoices.remind-400
  property_count: 1
  slug: paypal-invoicesremind-400
- name: invoices.remind-422
  property_count: 1
  slug: paypal-invoicesremind-422
- name: invoices.search-invoices-400
  property_count: 1
  slug: paypal-invoicessearch-invoices-400
- name: invoices.update-400
  property_count: 1
  slug: paypal-invoicesupdate-400
- name: IP Address
  property_count: 0
  slug: paypal-ip-address
- name: item_agreed_refund_details
  property_count: 0
  slug: paypal-item-agreed-refund-details
- name: item_booking_details
  property_count: 0
  slug: paypal-item-booking-details
- name: item_cancellation_details
  property_count: 0
  slug: paypal-item-cancellation-details
- name: Item Details
  property_count: 19
  slug: paypal-item-detail
- name: Tax Amount
  property_count: 1
  slug: paypal-item-detail-tax-amount
- name: item_digital_download_details
  property_count: 0
  slug: paypal-item-digital-download-details
- name: Item Information
  property_count: 15
  slug: paypal-item-info
- name: item_product_details
  property_count: 0
  slug: paypal-item-product-details
- name: Item
  property_count: 7
  slug: paypal-item
- name: item_service_details
  property_count: 0
  slug: paypal-item-service-details
- name: Item Type
  property_count: 0
  slug: paypal-item-type
- name: language
  property_count: 0
  slug: paypal-language
- name: Last Payment Details
  property_count: 0
  slug: paypal-last-payment-details
- name: Legal Consent
  property_count: 2
  slug: paypal-legal-consent
- name: Level 2 Card Processing Data
  property_count: 2
  slug: paypal-level-2-card-processing-data
- name: Level 3 Card Processing Data
  property_count: 6
  slug: paypal-level-3-card-processing-data
- name: liability_shift
  property_count: 0
  slug: paypal-liability-shift
- name: Lineitem
  property_count: 0
  slug: paypal-line-item
- name: Link Description
  property_count: 3
  slug: paypal-link-description-2
- name: Link Description
  property_count: 3
  slug: paypal-link-description
- name: Make Offer Response Options
  property_count: 1
  slug: paypal-make-offer-response-options
- name: Make Offer Request
  property_count: 5
  slug: paypal-make-offer
- name: Mandate
  property_count: 1
  slug: paypal-mandate
- name: Merchandise Dispute Properties
  property_count: 5
  slug: paypal-merchandize-dispute-properties
- name: Merchant Contacted Method
  property_count: 0
  slug: paypal-merchant-contacted-mode
- name: Merchant Contacted Outcome
  property_count: 0
  slug: paypal-merchant-contacted-outcome
- name: merchant_partner_customer_id
  property_count: 0
  slug: paypal-merchant-partner-customer-id
- name: Message
  property_count: 4
  slug: paypal-message
- name: Metadata
  property_count: 0
  slug: paypal-metadata
- name: Money
  property_count: 2
  slug: paypal-money-2
- name: money_movement_reason
  property_count: 0
  slug: paypal-money-movement-reason
- name: Money movement
  property_count: 6
  slug: paypal-money-movement
- name: Money
  property_count: 2
  slug: paypal-money
- name: MyBank payment object
  property_count: 3
  slug: paypal-mybank-request
- name: MyBank payment object
  property_count: 4
  slug: paypal-mybank
- name: Name
  property_count: 6
  slug: paypal-name-2
- name: Name
  property_count: 7
  slug: paypal-name
- name: Net Amount Breakdown Item
  property_count: 3
  slug: paypal-net-amount-breakdown-item
- name: Network Token
  property_count: 5
  slug: paypal-network-token-request
- name: Network Transaction Reference
  property_count: 4
  slug: paypal-network-transaction-reference
- name: Notification
  property_count: 5
  slug: paypal-notification
- name: Offer History
  property_count: 7
  slug: paypal-offer-history
- name: Offer
  property_count: 4
  slug: paypal-offer
- name: Offer Type
  property_count: 0
  slug: paypal-offer-type
- name: Role type
  property_count: 0
  slug: paypal-office-bearer-role
- name: Office Bearers
  property_count: 0
  slug: paypal-office-bearer
- name: Operation
  property_count: 3
  slug: paypal-operation
- name: Application Context
  property_count: 9
  slug: paypal-order-application-context
- name: Authorize Request
  property_count: 1
  slug: paypal-order-authorize-request
- name: Order
  property_count: 0
  slug: paypal-order-authorize-response
- name: Order Capture Request
  property_count: 1
  slug: paypal-order-capture-request
- name: Confirm Application Context
  property_count: 5
  slug: paypal-order-confirm-application-context
- name: Order Request
  property_count: 5
  slug: paypal-order-request
- name: Order
  property_count: 0
  slug: paypal-order
- name: Order Status
  property_count: 0
  slug: paypal-order-status
- name: Order Tracker Request.
  property_count: 0
  slug: paypal-order-tracker-request
- name: orders.authorize-400
  property_count: 1
  slug: paypal-ordersauthorize-400
- name: orders.authorize-403
  property_count: 1
  slug: paypal-ordersauthorize-403
- name: orders.authorize-422
  property_count: 1
  slug: paypal-ordersauthorize-422
- name: orders.capture-400
  property_count: 1
  slug: paypal-orderscapture-400
- name: orders.capture-403
  property_count: 1
  slug: paypal-orderscapture-403
- name: orders.capture-422
  property_count: 1
  slug: paypal-orderscapture-422
- name: orders.confirm-400
  property_count: 1
  slug: paypal-ordersconfirm-400
- name: orders.confirm-422
  property_count: 1
  slug: paypal-ordersconfirm-422
- name: orders.patch-400
  property_count: 1
  slug: paypal-orderspatch-400
- name: orders.patch-422
  property_count: 1
  slug: paypal-orderspatch-422
- name: orders.track.create-400
  property_count: 1
  slug: paypal-orderstrackcreate-400
- name: orders.track.create-403
  property_count: 1
  slug: paypal-orderstrackcreate-403
- name: orders.track.create-422
  property_count: 1
  slug: paypal-orderstrackcreate-422
- name: orders.trackers.patch-400
  property_count: 1
  slug: paypal-orderstrackerspatch-400
- name: orders.trackers.patch-403
  property_count: 1
  slug: paypal-orderstrackerspatch-403
- name: orders.trackers.patch-404
  property_count: 1
  slug: paypal-orderstrackerspatch-404
- name: orders.trackers.patch-422
  property_count: 1
  slug: paypal-orderstrackerspatch-422
- name: ordinal
  property_count: 0
  slug: paypal-ordinal
- name: P24 payment object
  property_count: 4
  slug: paypal-p24-request
- name: P24 payment object
  property_count: 6
  slug: paypal-p24
- name: pares_status
  property_count: 0
  slug: paypal-pares-status
- name: Partial Payment
  property_count: 2
  slug: paypal-partial-payment
- name: Partner Configuration Override
  property_count: 5
  slug: paypal-partner-config-override
- name: Patch Request
  property_count: 0
  slug: paypal-patch-request
- name: Patch
  property_count: 4
  slug: paypal-patch
- name: Merchant Base
  property_count: 2
  slug: paypal-payee-base
- name: payee_payment_method_preference
  property_count: 0
  slug: paypal-payee-payment-method-preference
- name: Payee
  property_count: 0
  slug: paypal-payee
- name: Payer Base
  property_count: 2
  slug: paypal-payer-base
- name: Payer Information
  property_count: 8
  slug: paypal-payer-info
- name: Customer
  property_count: 0
  slug: paypal-payer
- name: Payment by Other Means
  property_count: 4
  slug: paypal-payment-by-other-means
- name: Payment Collection
  property_count: 3
  slug: paypal-payment-collection
- name: Payment Detail
  property_count: 7
  slug: paypal-payment-detail
- name: payment_initiator
  property_count: 0
  slug: paypal-payment-initiator
- name: Payment Instruction
  property_count: 1
  slug: paypal-payment-instruction-2
- name: Payment Instruction
  property_count: 4
  slug: paypal-payment-instruction
- name: Payment Method
  property_count: 3
  slug: paypal-payment-method
- name: Payment Preferences Override
  property_count: 4
  slug: paypal-payment-preferences-override
- name: Payment Preferences
  property_count: 4
  slug: paypal-payment-preferences
- name: payment_processor
  property_count: 0
  slug: paypal-payment-processor
- name: Payment Reference
  property_count: 1
  slug: paypal-payment-reference
- name: Payment Source Response
  property_count: 1
  slug: paypal-payment-source-response
- name: Payment Source
  property_count: 1
  slug: paypal-payment-source
- name: Payment Term
  property_count: 1
  slug: paypal-payment-term
- name: Payment Term Type
  property_count: 0
  slug: paypal-payment-term-type
- name: Payment Token Request
  property_count: 3
  slug: paypal-payment-token-request
- name: Payment Token Response
  property_count: 4
  slug: paypal-payment-token-response
- name: Payment Token Status
  property_count: 0
  slug: paypal-payment-token-status
- name: Payment Type
  property_count: 0
  slug: paypal-payment-type
- name: Payments
  property_count: 2
  slug: paypal-payments
- name: Payout Attributes
  property_count: 3
  slug: paypal-payout-attributes
- name: Payout Batch Header
  property_count: 9
  slug: paypal-payout-batch-header
- name: Payout Item
  property_count: 11
  slug: paypal-payout-batch-items
- name: Payout Batch
  property_count: 5
  slug: paypal-payout-batch
- name: Currency conversion resource
  property_count: 3
  slug: paypal-payout-currency-conversion
- name: Payout Header
  property_count: 4
  slug: paypal-payout-header
- name: Payout Item
  property_count: 12
  slug: paypal-payout-item-2
- name: Payout Item Detail
  property_count: 8
  slug: paypal-payout-item-detail
- name: Payout Item
  property_count: 10
  slug: paypal-payout-item
- name: Create Payout Response
  property_count: 2
  slug: paypal-payout
- name: Payout Sender Batch Header
  property_count: 4
  slug: paypal-payout-sender-batch-header
- name: PayPal Wallet Attributes Response
  property_count: 2
  slug: paypal-paypal-wallet-attributes-response
- name: PayPal Wallet Attributes
  property_count: 2
  slug: paypal-paypal-wallet-attributes
- name: Customer information based on PayPal's system of record
  property_count: 0
  slug: paypal-paypal-wallet-customer
- name: PayPal Wallet Experience Context
  property_count: 8
  slug: paypal-paypal-wallet-experience-context
- name: PayPal Wallet Request
  property_count: 0
  slug: paypal-paypal-wallet-request
- name: PayPal Wallet Response
  property_count: 10
  slug: paypal-paypal-wallet-response
- name: PayPal Wallet
  property_count: 10
  slug: paypal-paypal-wallet
- name: Saved PayPal Wallet Payment Source Response
  property_count: 0
  slug: paypal-paypal-wallet-vault-response
- name: percentage
  property_count: 0
  slug: paypal-percentage
- name: Person address detail
  property_count: 0
  slug: paypal-person-address-detail
- name: Person address type
  property_count: 0
  slug: paypal-person-address-type
- name: Person document
  property_count: 0
  slug: paypal-person-document
- name: Document type
  property_count: 0
  slug: paypal-person-document-type
- name: Person name
  property_count: 0
  slug: paypal-person-name
- name: Person name type
  property_count: 0
  slug: paypal-person-name-type
- name: Phone details
  property_count: 0
  slug: paypal-person-phone-detail
- name: Person
  property_count: 7
  slug: paypal-person
- name: Phone
  property_count: 1
  slug: paypal-phone-2
- name: Phone Detail
  property_count: 0
  slug: paypal-phone-detail
- name: Phone number tag
  property_count: 0
  slug: paypal-phone-number-tag
- name: Phone
  property_count: 3
  slug: paypal-phone
- name: Phone Type
  property_count: 0
  slug: paypal-phone-type-2
- name: Phone Type
  property_count: 0
  slug: paypal-phone-type
- name: Phone With Type
  property_count: 2
  slug: paypal-phone-with-type
- name: Plan Collection
  property_count: 4
  slug: paypal-plan-collection
- name: Plan Override
  property_count: 3
  slug: paypal-plan-override
- name: Create Plan Request
  property_count: 8
  slug: paypal-plan-request-post
- name: Plan
  property_count: 12
  slug: paypal-plan
- name: plans.activate-422
  property_count: 1
  slug: paypal-plansactivate-422
- name: plans.create-400
  property_count: 1
  slug: paypal-planscreate-400
- name: plans.deactivate-422
  property_count: 1
  slug: paypal-plansdeactivate-422
- name: plans.patch-400
  property_count: 1
  slug: paypal-planspatch-400
- name: plans.patch-422
  property_count: 1
  slug: paypal-planspatch-422
- name: plans.update-pricing-schemes-400
  property_count: 1
  slug: paypal-plansupdate-pricing-schemes-400
- name: plans.update-pricing-schemes-422
  property_count: 1
  slug: paypal-plansupdate-pricing-schemes-422
- name: Platform Fee
  property_count: 2
  slug: paypal-platform-fee
- name: Pricing Scheme
  property_count: 6
  slug: paypal-pricing-scheme
- name: Pricing Tier
  property_count: 3
  slug: paypal-pricing-tier
- name: Processing Instruction
  property_count: 0
  slug: paypal-processing-instruction
- name: Processor Response
  property_count: 4
  slug: paypal-processor-response
- name: Product Category
  property_count: 0
  slug: paypal-product-category
- name: Product Element
  property_count: 5
  slug: paypal-product-collection-element
- name: Product Collection
  property_count: 4
  slug: paypal-product-collection
- name: Product Details
  property_count: 7
  slug: paypal-product-details
- name: Create Product Request
  property_count: 7
  slug: paypal-product-request-post
- name: Product Details
  property_count: 10
  slug: paypal-product
- name: products.create-400
  property_count: 1
  slug: paypal-productscreate-400
- name: products.patch-400
  property_count: 1
  slug: paypal-productspatch-400
- name: products.patch-422
  property_count: 1
  slug: paypal-productspatch-422
- name: Purchase Unit Request
  property_count: 11
  slug: paypal-purchase-unit-request
- name: Purchase Unit
  property_count: 13
  slug: paypal-purchase-unit
- name: Purpose Code
  property_count: 0
  slug: paypal-purpose-code-enum
- name: Purpose
  property_count: 0
  slug: paypal-purpose-enum
- name: QR Configuration
  property_count: 3
  slug: paypal-qr-config
- name: Reauthorize Request
  property_count: 1
  slug: paypal-reauthorize-request
- name: Recipient type
  property_count: 0
  slug: paypal-recipient-enum
- name: Recipient Information
  property_count: 2
  slug: paypal-recipient-info
- name: Recipient wallet
  property_count: 0
  slug: paypal-recipient-wallet-enum
- name: Referral Data Response
  property_count: 4
  slug: paypal-referral-data-response
- name: Customer Data
  property_count: 0
  slug: paypal-referral-data
- name: Refund Detail
  property_count: 5
  slug: paypal-refund-detail
- name: Refund Details
  property_count: 1
  slug: paypal-refund-details
- name: Refund Payment Reference
  property_count: 1
  slug: paypal-refund-reference
- name: Refund Request
  property_count: 5
  slug: paypal-refund-request
- name: Refund
  property_count: 0
  slug: paypal-refund
- name: Refund Status Details
  property_count: 1
  slug: paypal-refund-status-details
- name: Refund Status
  property_count: 2
  slug: paypal-refund-status
- name: Refunds
  property_count: 2
  slug: paypal-refunds
- name: Related Identifiers
  property_count: 3
  slug: paypal-related-ids
- name: Require Evidence Request
  property_count: 1
  slug: paypal-require-evidence
- name: Resource Version
  property_count: 0
  slug: paypal-resource-version
- name: REST API Integration
  property_count: 4
  slug: paypal-rest-api-integration
- name: REST Endpoint Features
  property_count: 0
  slug: paypal-rest-endpoint-features-enum
- name: Return Details
  property_count: 5
  slug: paypal-return-details
- name: Search Data
  property_count: 16
  slug: paypal-search-data
- name: Search Response
  property_count: 9
  slug: paypal-search-response
- name: Seller Protection
  property_count: 2
  slug: paypal-seller-protection
- name: Seller Receivable Breakdown
  property_count: 7
  slug: paypal-seller-receivable-breakdown
- name: Merchant
  property_count: 3
  slug: paypal-seller
- name: Sender Batch Header
  property_count: 5
  slug: paypal-sender-batch-header
- name: Service Details
  property_count: 5
  slug: paypal-service-details
- name: Setup Token
  property_count: 3
  slug: paypal-setup-token-request
- name: Minimal Setup Token
  property_count: 6
  slug: paypal-setup-token-response
- name: Carrier.
  property_count: 0
  slug: paypal-shipment-carrier
- name: Shipment Tracker.
  property_count: 14
  slug: paypal-shipment-tracker
- name: Shipment Tracking Number Type.
  property_count: 0
  slug: paypal-shipment-tracking-number-type
- name: Shipment Tracking Status.
  property_count: 0
  slug: paypal-shipment-tracking-status
- name: Shipping Cost
  property_count: 2
  slug: paypal-shipping-cost
- name: Shipping Details
  property_count: 3
  slug: paypal-shipping-detail
- name: Shipping Information
  property_count: 4
  slug: paypal-shipping-info
- name: Shipping Option
  property_count: 5
  slug: paypal-shipping-option
- name: Shipping Type
  property_count: 0
  slug: paypal-shipping-type
- name: Order Shipping Details
  property_count: 0
  slug: paypal-shipping-with-tracking-details
- name: Simulate Event
  property_count: 4
  slug: paypal-simulate-event
- name: Sofort payment object
  property_count: 3
  slug: paypal-sofort-request
- name: Sofort payment object
  property_count: 4
  slug: paypal-sofort
- name: status
  property_count: 0
  slug: paypal-status
- name: store_in_vault_instruction
  property_count: 0
  slug: paypal-store-in-vault-instruction
- name: Store Information
  property_count: 2
  slug: paypal-store-info
- name: stored_payment_source_payment_type
  property_count: 0
  slug: paypal-stored-payment-source-payment-type
- name: Stored Payment Source
  property_count: 4
  slug: paypal-stored-payment-source
- name: stored_payment_source_usage_type
  property_count: 0
  slug: paypal-stored-payment-source-usage-type
- name: Subscriber Request Information
  property_count: 0
  slug: paypal-subscriber-request
- name: Subscriber Response Information
  property_count: 0
  slug: paypal-subscriber
- name: Activate Subscription Request
  property_count: 1
  slug: paypal-subscription-activate-request
- name: Subscription Billing Information
  property_count: 7
  slug: paypal-subscription-billing-info
- name: Cancel Subscription Request
  property_count: 1
  slug: paypal-subscription-cancel-request
- name: Charge Amount from Subscriber
  property_count: 3
  slug: paypal-subscription-capture-request
- name: Create Subscription Request
  property_count: 9
  slug: paypal-subscription-request-post
- name: Subscription Modify Plan Request
  property_count: 6
  slug: paypal-subscription-revise-request
- name: Update Product Quantity in Subscription Response
  property_count: 0
  slug: paypal-subscription-revise-response
- name: Subscription
  property_count: 0
  slug: paypal-subscription
- name: Subscription Status
  property_count: 3
  slug: paypal-subscription-status
- name: Suspend Subscription
  property_count: 1
  slug: paypal-subscription-suspend-request
- name: subscriptions.activate-400
  property_count: 1
  slug: paypal-subscriptionsactivate-400
- name: subscriptions.activate-422
  property_count: 1
  slug: paypal-subscriptionsactivate-422
- name: subscriptions.cancel-400
  property_count: 1
  slug: paypal-subscriptionscancel-400
- name: subscriptions.cancel-422
  property_count: 1
  slug: paypal-subscriptionscancel-422
- name: subscriptions.capture-400
  property_count: 1
  slug: paypal-subscriptionscapture-400
- name: subscriptions.capture-422
  property_count: 1
  slug: paypal-subscriptionscapture-422
- name: subscriptions.create-400
  property_count: 1
  slug: paypal-subscriptionscreate-400
- name: subscriptions.create-422
  property_count: 1
  slug: paypal-subscriptionscreate-422
- name: subscriptions.patch-400
  property_count: 1
  slug: paypal-subscriptionspatch-400
- name: subscriptions.patch-422
  property_count: 1
  slug: paypal-subscriptionspatch-422
- name: subscriptions.revise-400
  property_count: 1
  slug: paypal-subscriptionsrevise-400
- name: subscriptions.revise-404
  property_count: 1
  slug: paypal-subscriptionsrevise-404
- name: subscriptions.revise-422
  property_count: 1
  slug: paypal-subscriptionsrevise-422
- name: subscriptions.suspend-400
  property_count: 1
  slug: paypal-subscriptionssuspend-400
- name: subscriptions.suspend-422
  property_count: 1
  slug: paypal-subscriptionssuspend-422
- name: subscriptions.transactions-400
  property_count: 1
  slug: paypal-subscriptionstransactions-400
- name: Subsequent Action
  property_count: 1
  slug: paypal-subsequent-action
- name: Supplementary Data
  property_count: 1
  slug: paypal-supplementary-data
- name: Capture Identifier
  property_count: 2
  slug: paypal-supplementary-purchase-data
- name: Supporting Info
  property_count: 5
  slug: paypal-supporting-info
- name: Tax Information
  property_count: 2
  slug: paypal-tax-info
- name: Tax
  property_count: 3
  slug: paypal-tax
- name: Taxes Override
  property_count: 2
  slug: paypal-taxes-override
- name: Taxes
  property_count: 2
  slug: paypal-taxes
- name: Template Configuration
  property_count: 4
  slug: paypal-template-configuration
- name: Template Detail
  property_count: 0
  slug: paypal-template-detail
- name: Template Display Preference
  property_count: 1
  slug: paypal-template-display-preference
- name: Template Information
  property_count: 8
  slug: paypal-template-info
- name: Template Item Field
  property_count: 0
  slug: paypal-template-item-field
- name: Template Item Setting
  property_count: 2
  slug: paypal-template-item-setting
- name: Template Metadata
  property_count: 4
  slug: paypal-template-metadata
- name: Template
  property_count: 8
  slug: paypal-template
- name: Template Settings
  property_count: 2
  slug: paypal-template-settings
- name: Template Subtotal Field
  property_count: 0
  slug: paypal-template-subtotal-field
- name: Template Subtotal Setting
  property_count: 2
  slug: paypal-template-subtotal-setting
- name: Templates
  property_count: 5
  slug: paypal-templates
- name: templates.create-400
  property_count: 1
  slug: paypal-templatescreate-400
- name: templates.create-422
  property_count: 1
  slug: paypal-templatescreate-422
- name: templates.delete-403
  property_count: 1
  slug: paypal-templatesdelete-403
- name: templates.get-403
  property_count: 1
  slug: paypal-templatesget-403
- name: templates.update-400
  property_count: 1
  slug: paypal-templatesupdate-400
- name: templates.update-422
  property_count: 1
  slug: paypal-templatesupdate-422
- name: The 3D Secure Authentication Response
  property_count: 2
  slug: paypal-three-d-secure-authentication-response
- name: token_attributes
  property_count: 0
  slug: paypal-token-attributes
- name: Token Request
  property_count: 3
  slug: paypal-token-id-request
- name: Token
  property_count: 2
  slug: paypal-token
- name: Tracker Collection
  property_count: 2
  slug: paypal-tracker-collection
- name: Tracker Identifier Collection
  property_count: 2
  slug: paypal-tracker-identifier-collection
- name: Tracking Identifier
  property_count: 3
  slug: paypal-tracker-identifier
- name: Tracker Item
  property_count: 6
  slug: paypal-tracker-item
- name: Order Tracker Response.
  property_count: 0
  slug: paypal-tracker
- name: tracker_status
  property_count: 0
  slug: paypal-tracker-status
- name: Tracking Information
  property_count: 4
  slug: paypal-tracking-info
- name: Tracking Number Type
  property_count: 0
  slug: paypal-tracking-number-type
- name: Tracking Status
  property_count: 0
  slug: paypal-tracking-status
- name: Transaction Details
  property_count: 7
  slug: paypal-transaction-detail
- name: Transaction status
  property_count: 0
  slug: paypal-transaction-enum
- name: Transaction Information
  property_count: 13
  slug: paypal-transaction-info
- name: Transaction Details
  property_count: 0
  slug: paypal-transaction
- name: List Transactions
  property_count: 4
  slug: paypal-transactions-list
- name: Requested transfer method and currency for a country
  property_count: 2
  slug: paypal-transfer-method
- name: Trustly payment object
  property_count: 3
  slug: paypal-trustly-request
- name: Trustly payment object
  property_count: 4
  slug: paypal-trustly
- name: unit_of_measure
  property_count: 0
  slug: paypal-unit-of-measure
- name: universal_product_code
  property_count: 0
  slug: paypal-universal-product-code
- name: Update Pricing Scheme
  property_count: 2
  slug: paypal-update-pricing-scheme-request
- name: Update Pricing Scheme Request
  property_count: 1
  slug: paypal-update-pricing-schemes-list-request
- name: url
  property_count: 0
  slug: paypal-url
- name: Base Vault Instruction Parameters
  property_count: 1
  slug: paypal-v3-vault-instruction-base
- name: vault_id
  property_count: 0
  slug: paypal-vault-id
- name: Base vault Instruction parameters
  property_count: 1
  slug: paypal-vault-instruction-base
- name: Vault Instruction
  property_count: 0
  slug: paypal-vault-instruction
- name: vault_owner_id
  property_count: 0
  slug: paypal-vault-owner-id
- name: Vaulted PayPal Wallet Common Attributes
  property_count: 0
  slug: paypal-vault-paypal-wallet-base
- name: Saved Payment Source Response
  property_count: 4
  slug: paypal-vault-response
- name: Vaulted Venmo Wallet Common Attributes
  property_count: 0
  slug: paypal-vault-venmo-wallet-base
- name: Venmo Request
  property_count: 0
  slug: paypal-venmo-request
- name: Venmo Response
  property_count: 0
  slug: paypal-venmo-response
- name: Venmo Wallet Attributes Response
  property_count: 1
  slug: paypal-venmo-wallet-attributes-response
- name: Venmo Wallet Attributes
  property_count: 2
  slug: paypal-venmo-wallet-attributes
- name: Venmo Wallet Experience Context
  property_count: 2
  slug: paypal-venmo-wallet-experience-context
- name: Venmo payment request object
  property_count: 4
  slug: paypal-venmo-wallet-request
- name: Venmo Wallet Response Object
  property_count: 7
  slug: paypal-venmo-wallet-response
- name: Verify Webhook Signature Response
  property_count: 1
  slug: paypal-verify-webhook-signature-response
- name: Verify Webhook Signature
  property_count: 7
  slug: paypal-verify-webhook-signature
- name: Vaulted Digital Wallet Common Attributes
  property_count: 5
  slug: paypal-wallet-base
- name: Web Profile List
  property_count: 0
  slug: paypal-web-profile-list
- name: Web Profile
  property_count: 6
  slug: paypal-web-profile
- name: Webhook
  property_count: 4
  slug: paypal-webhook
- name: Webhook List
  property_count: 1
  slug: paypal-webhooklist
- name: Webhook Lookup List
  property_count: 1
  slug: paypal-webhooklookuplist
- name: Webhook Lookup
  property_count: 3
  slug: paypal-webhooks-lookup
json_structures:
- name: Paypal Structure
  property_count: 0
  slug: paypal-structure
layout: provider
modified: '2026-05-30'
name: PayPal
nav: Providers
network: true
overview: 'PayPal publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Activate API, Authorizations API, Balances API, and 34 more. Tagged areas include Billing, Commerce, Disputes, Invoices, and Orders.


  The PayPal catalog on APIs.io includes 1 Spectral governance ruleset.


  PayPal''s developer surface includes sandbox, changelog, authentication, documentation, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Paypal Plans Pricing
  plan_count: 7
  slug: paypal-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 3
  name: Paypal Rate Limits
  slug: paypal-rate-limits
rules:
- name: PayPal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: paypal-jsonschema-spectral-rules
scopes:
- name: Paypal Scopes
  scope_count: 39
  slug: paypal-scopes
  summary_line: 39 scopes · clientCredentials
score:
  band: strong
  composite: 59.0
  delta: -4.5
  facets:
    commercial_clarity: 55.3
    contract_quality: 63.9
    developer_ergonomics: 52.2
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 97.4
      derived: 0
      marker_coverage: 0.0
      total: 38
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 70.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paypal/refs/heads/main/screenshots/paypal-2026-06-20T191505.png
security:
- kind: authentication
  name: Paypal Authentication
  slug: paypal-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paypal Domain Security
  slug: paypal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Paypal Vulnerability Disclosure
  slug: paypal-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Paypal Trust Center
  slug: paypal-trust-center
  summary_line: PCI DSS, PCI P2PE, ISO/IEC 27001, SOC 1, SOC 2 Type II
slug: paypal
tags:
- Billing
- Commerce
- Disputes
- Invoices
- Orders
- Payments
- Payouts
- Subscriptions
- Tokens
- Webhooks
website: https://www.paypal.com
---
