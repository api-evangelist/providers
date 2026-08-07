---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 483
  human_in_the_loop: 2
  name: Stripe Agentic Access
  operation_count: 910
  slug: stripe-agentic-access
  summary_line: 910 operations · 483 acting · 2 human-in-the-loop
api_count: 159
apis:
- description: This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts
  name: Stripe Accounts API
  slug: stripe-accounts-api
- description: This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transac
  name: Stripe Balance API
  slug: stripe-balance-api
- description: Create and manage subscriptions, recurring payments, and recurring revenue.
  name: Stripe Billing API
  slug: stripe-billing-api
- description: 'The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe '
  name: Stripe Charges API
  slug: stripe-charges-api
- description: Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment pa
  name: Stripe Checkout API
  slug: stripe-checkout-api
- description: Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.
  name: Stripe Climate API
  slug: stripe-climate-api
- description: Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to
  name: Stripe Country API
  slug: stripe-country-api
- description: 'A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. '
  name: Stripe Coupons API
  slug: stripe-coupons-api
- description: Issue a credit note to adjust an invoice's amount after the invoice is finalized.
  name: Stripe Credit Notes API
  slug: stripe-credit-notes-api
- description: This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.
  name: Stripe Customers API
  slug: stripe-customers-api
- description: A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitim
  name: Stripe Disputes API
  slug: stripe-disputes-api
- description: Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side
  name: Stripe Ephemeral Keys API
  slug: stripe-ephemeral-keys-api
- description: Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.
  name: Stripe Events API
  slug: stripe-events-api
- description: 'Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer''s native currency. Doing so can improve sales and help customers avoid conversion costs. In order to '
  name: Stripe Exchange Rates API
  slug: stripe-exchange-rates-api
- description: 'This object represents files hosted on Stripe''s servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for '
  name: Stripe Files API
  slug: stripe-files-api
- description: 'Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such '
  name: Stripe Financial Connections API
  slug: stripe-financial-connections-api
- description: Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.
  name: Stripe Identity API
  slug: stripe-identity-api
- description: Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.
  name: Stripe Invoice API
  slug: stripe-invoice-api
- description: An API for businesses to instantly create, manage, and distribute payment cards.
  name: Stripe Issuing API
  slug: stripe-issuing-api
- description: You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.
  name: Stripe Link API
  slug: stripe-link-api
- description: A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You
  name: Stripe Payment Intents API
  slug: stripe-payment-intents-api
- description: 'A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new '
  name: Stripe Payment Links API
  slug: stripe-payment-links-api
- description: 'A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, '
  name: Stripe Payouts API
  slug: stripe-payouts-api
- description: You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.
  name: Stripe Plans API
  slug: stripe-plans-api
- description: 'Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track '
  name: Stripe Prices API
  slug: stripe-prices-api
- description: Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Pro
  name: Stripe Products API
  slug: stripe-products-api
- description: A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.
  name: Stripe Promotion Codes API
  slug: stripe-promotion-codes-api
- description: A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.
  name: Stripe Quotes API
  slug: stripe-quotes-api
- description: Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.
  name: Stripe Radar API
  slug: stripe-radar-api
- description: Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.
  name: Stripe Refunds API
  slug: stripe-refunds-api
- description: The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can sch
  name: Stripe Reporting API
  slug: stripe-reporting-api
- description: Reviews can be used to supplement automated fraud detection with human expertise.
  name: Stripe Reviews API
  slug: stripe-reviews-api
- description: Shipping rates describe the price of shipping presented to your customers and applied to a purchase.
  name: Stripe Shipping Rates API
  slug: stripe-shipping-rates-api
- description: If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve
  name: Stripe Sigma API
  slug: stripe-sigma-api
- description: Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can b
  name: Stripe Sources API
  slug: stripe-sources-api
- description: Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.
  name: Stripe Tax API
  slug: stripe-tax-api
- description: Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.
  name: Stripe Terminal API
  slug: stripe-terminal-api
- description: Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.
  name: Stripe Test Helpers API
  slug: stripe-test-helpers-api
- description: Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token repres
  name: Stripe Tokens API
  slug: stripe-tokens-api
- description: To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.
  name: Stripe Topups API
  slug: stripe-topups-api
- description: A Transfer object is created when you move funds between Stripe accounts as part of Connect.
  name: Stripe Transfers API
  slug: stripe-transfers-api
- description: Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage thei
  name: Stripe Treasury API
  slug: stripe-treasury-api
- description: Stripe Connect is a set of programmable APIs and tools that lets you facilitate payments on your software platform, build a marketplace, and pay out sellers or service providers globally.
  name: Stripe Connect API
  slug: stripe-connect-api
- description: The Billing customer portal is a Stripe-hosted UI for subscription and billing management. A portal session describes the instantiation of the customer portal for a particular customer. By visiting th
  name: Stripe Customer Portal API
  slug: stripe-customer-portal-api
- description: Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access according to yo
  name: Stripe Entitlements API
  slug: stripe-entitlements-api
- description: The Vault and Forward API allows you to tokenize and store card details in Stripes PCI-compliant vault and forward that data to supported third-party processors or endpoints.
  name: Stripe Forwarding API
  slug: stripe-forwarding-api
- description: The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application at checkout.
  name: Stripe Crypto Onramp API
  slug: stripe-crypto-onramp-api
- description: Automate your accrual accounting process with Stripe Revenue Recognition. Import transaction data, set up rules, and download revenue reports for compliance with accounting standards like ASC 606.
  name: Stripe Revenue Recognition API
  slug: stripe-revenue-recognition-api
- description: Meters specify how to aggregate meter events over a billing period for usage-based pricing. Meter events represent customer actions and support up to 10,000 events per second via the V2 meter event st
  name: Stripe Billing Meters API
  slug: stripe-billing-meters-api
- description: Payment method configurations allow you to configure which payment methods are available to your customers during checkout. Manage payment method availability across multiple Connect accounts.
  name: Stripe Payment Method Configurations API
  slug: stripe-payment-method-configurations-api
- description: The Account API from Stripe — 12 operation(s) for account.
  name: Stripe Account API
  slug: stripe-account-api
- description: The Apple API from Stripe — 2 operation(s) for apple.
  name: Stripe Apple API
  slug: stripe-apple-api
- description: The Applications API from Stripe — 8 operation(s) for applications.
  name: Stripe Applications API
  slug: stripe-applications-api
- description: The Apply API from Stripe — 1 operation(s) for apply.
  name: Stripe Apply API
  slug: stripe-apply-api
- description: The Approve API from Stripe — 1 operation(s) for approve.
  name: Stripe Approve API
  slug: stripe-approve-api
- description: The Attach API from Stripe — 1 operation(s) for attach.
  name: Stripe Attach API
  slug: stripe-attach-api
- description: The Authorization API from Stripe — 5 operation(s) for authorization.
  name: Stripe Authorization API
  slug: stripe-authorization-api
- description: The Balance Transactions API from Stripe — 2 operation(s) for balance transactions.
  name: Stripe Balance Transactions API
  slug: stripe-balance-transactions-api
- description: The Bank API from Stripe — 5 operation(s) for bank.
  name: Stripe Bank API
  slug: stripe-bank-api
- description: The Billing Portal API from Stripe — 3 operation(s) for billing portal.
  name: Stripe Billing Portal API
  slug: stripe-billing-portal-api
- description: The Cancel API from Stripe — 3 operation(s) for cancel.
  name: Stripe Cancel API
  slug: stripe-cancel-api
- description: The Capabilities API from Stripe — 1 operation(s) for capabilities.
  name: Stripe Capabilities API
  slug: stripe-capabilities-api
- description: The Capability API from Stripe — 1 operation(s) for capability.
  name: Stripe Capability API
  slug: stripe-capability-api
- description: The Capture API from Stripe — 1 operation(s) for capture.
  name: Stripe Capture API
  slug: stripe-capture-api
- description: The Card API from Stripe — 1 operation(s) for card.
  name: Stripe Card API
  slug: stripe-card-api
- description: The Cards API from Stripe — 4 operation(s) for cards.
  name: Stripe Cards API
  slug: stripe-cards-api
- description: The Cash API from Stripe — 3 operation(s) for cash.
  name: Stripe Cash API
  slug: stripe-cash-api
- description: The Close API from Stripe — 1 operation(s) for close.
  name: Stripe Close API
  slug: stripe-close-api
- description: The Configuration API from Stripe — 1 operation(s) for configuration.
  name: Stripe Configuration API
  slug: stripe-configuration-api
- description: The Configurations API from Stripe — 4 operation(s) for configurations.
  name: Stripe Configurations API
  slug: stripe-configurations-api
- description: The Confirm API from Stripe — 1 operation(s) for confirm.
  name: Stripe Confirm API
  slug: stripe-confirm-api
- description: The Connections API from Stripe — 11 operation(s) for connections.
  name: Stripe Connections API
  slug: stripe-connections-api
- description: The Country Specs API from Stripe — 2 operation(s) for country specs.
  name: Stripe Country Specs API
  slug: stripe-country-specs-api
- description: The Coupon API from Stripe — 1 operation(s) for coupon.
  name: Stripe Coupon API
  slug: stripe-coupon-api
- description: The Create API from Stripe — 10 operation(s) for create.
  name: Stripe Create API
  slug: stripe-create-api
- description: The Credit API from Stripe — 6 operation(s) for credit.
  name: Stripe Credit API
  slug: stripe-credit-api
- description: The Customer API from Stripe — 24 operation(s) for customer.
  name: Stripe Customer API
  slug: stripe-customer-api
- description: The Decline API from Stripe — 1 operation(s) for decline.
  name: Stripe Decline API
  slug: stripe-decline-api
- description: The Delete API from Stripe — 20 operation(s) for delete.
  name: Stripe Delete API
  slug: stripe-delete-api
- description: The Detach API from Stripe — 1 operation(s) for detach.
  name: Stripe Detach API
  slug: stripe-detach-api
- description: The Disconnect API from Stripe — 2 operation(s) for disconnect.
  name: Stripe Disconnect API
  slug: stripe-disconnect-api
- description: The Discount API from Stripe — 2 operation(s) for discount.
  name: Stripe Discount API
  slug: stripe-discount-api
- description: The Dispute API from Stripe — 2 operation(s) for dispute.
  name: Stripe Dispute API
  slug: stripe-dispute-api
- description: The Domain API from Stripe — 2 operation(s) for domain.
  name: Stripe Domain API
  slug: stripe-domain-api
- description: The Domains API from Stripe — 4 operation(s) for domains.
  name: Stripe Domains API
  slug: stripe-domains-api
- description: The Exchange API from Stripe — 2 operation(s) for exchange.
  name: Stripe Exchange API
  slug: stripe-exchange-api
- description: The Expire API from Stripe — 1 operation(s) for expire.
  name: Stripe Expire API
  slug: stripe-expire-api
- description: The External API from Stripe — 2 operation(s) for external.
  name: Stripe External API
  slug: stripe-external-api
- description: The Fee API from Stripe — 4 operation(s) for fee.
  name: Stripe Fee API
  slug: stripe-fee-api
- description: The Finalize API from Stripe — 1 operation(s) for finalize.
  name: Stripe Finalize API
  slug: stripe-finalize-api
- description: The Financial API from Stripe — 11 operation(s) for financial.
  name: Stripe Financial API
  slug: stripe-financial-api
- description: The Find API from Stripe — 1 operation(s) for find.
  name: Stripe Find API
  slug: stripe-find-api
- description: The Funding API from Stripe — 1 operation(s) for funding.
  name: Stripe Funding API
  slug: stripe-funding-api
- description: The Get API from Stripe — 106 operation(s) for get.
  name: Stripe Get API
  slug: stripe-get-api
- description: The History API from Stripe — 2 operation(s) for history.
  name: Stripe History API
  slug: stripe-history-api
- description: The Identifiers API from Stripe — 15 operation(s) for identifiers.
  name: Stripe Identifiers API
  slug: stripe-identifiers-api
- description: The Increment API from Stripe — 1 operation(s) for increment.
  name: Stripe Increment API
  slug: stripe-increment-api
- description: The Intents API from Stripe — 9 operation(s) for intents.
  name: Stripe Intents API
  slug: stripe-intents-api
- description: The Invoiceitems API from Stripe — 2 operation(s) for invoiceitems.
  name: Stripe Invoiceitems API
  slug: stripe-invoiceitems-api
- description: The Invoices API from Stripe — 12 operation(s) for invoices.
  name: Stripe Invoices API
  slug: stripe-invoices-api
- description: The Item API from Stripe — 1 operation(s) for item.
  name: Stripe Item API
  slug: stripe-item-api
- description: The Items API from Stripe — 4 operation(s) for items.
  name: Stripe Items API
  slug: stripe-items-api
- description: The Keys API from Stripe — 2 operation(s) for keys.
  name: Stripe Keys API
  slug: stripe-keys-api
- description: The Line API from Stripe — 3 operation(s) for line.
  name: Stripe Line API
  slug: stripe-line-api
- description: The Lines API from Stripe — 5 operation(s) for lines.
  name: Stripe Lines API
  slug: stripe-lines-api
- description: The Link Account Sessions API from Stripe — 2 operation(s) for link account sessions.
  name: Stripe Link Account Sessions API
  slug: stripe-link-account-sessions-api
- description: The Linked Accounts API from Stripe — 5 operation(s) for linked accounts.
  name: Stripe Linked Accounts API
  slug: stripe-linked-accounts-api
- description: The Linked API from Stripe — 5 operation(s) for linked.
  name: Stripe Linked API
  slug: stripe-linked-api
- description: The Links API from Stripe — 3 operation(s) for links.
  name: Stripe Links API
  slug: stripe-links-api
- description: The Lists API from Stripe — 8 operation(s) for lists.
  name: Stripe Lists API
  slug: stripe-lists-api
- description: The Login API from Stripe — 1 operation(s) for login.
  name: Stripe Login API
  slug: stripe-login-api
- description: The Mark API from Stripe — 1 operation(s) for mark.
  name: Stripe Mark API
  slug: stripe-mark-api
- description: The Method API from Stripe — 6 operation(s) for method.
  name: Stripe Method API
  slug: stripe-method-api
- description: The Methods API from Stripe — 6 operation(s) for methods.
  name: Stripe Methods API
  slug: stripe-methods-api
- description: The Microdeposits API from Stripe — 1 operation(s) for microdeposits.
  name: Stripe Microdeposits API
  slug: stripe-microdeposits-api
- description: The Note API from Stripe — 1 operation(s) for note.
  name: Stripe Note API
  slug: stripe-note-api
- description: The Notes API from Stripe — 6 operation(s) for notes.
  name: Stripe Notes API
  slug: stripe-notes-api
- description: The Owners API from Stripe — 2 operation(s) for owners.
  name: Stripe Owners API
  slug: stripe-owners-api
- description: The Pay API from Stripe — 3 operation(s) for pay.
  name: Stripe Pay API
  slug: stripe-pay-api
- description: The Payment Method Domains API from Stripe — 3 operation(s) for payment method domains.
  name: Stripe Payment Method Domains API
  slug: stripe-payment-method-domains-api
- description: The Payment Methods API from Stripe — 4 operation(s) for payment methods.
  name: Stripe Payment Methods API
  slug: stripe-payment-methods-api
- description: The Payments API from Stripe — 23 operation(s) for payments.
  name: Stripe Payments API
  slug: stripe-payments-api
- description: The Person API from Stripe — 4 operation(s) for person.
  name: Stripe Person API
  slug: stripe-person-api
- description: The Persons API from Stripe — 2 operation(s) for persons.
  name: Stripe Persons API
  slug: stripe-persons-api
- description: The Post API from Stripe — 95 operation(s) for post.
  name: Stripe Post API
  slug: stripe-post-api
- description: The Preview API from Stripe — 2 operation(s) for preview.
  name: Stripe Preview API
  slug: stripe-preview-api
- description: The Rate API from Stripe — 1 operation(s) for rate.
  name: Stripe Rate API
  slug: stripe-rate-api
- description: The Rates API from Stripe — 2 operation(s) for rates.
  name: Stripe Rates API
  slug: stripe-rates-api
- description: The Redact API from Stripe — 1 operation(s) for redact.
  name: Stripe Redact API
  slug: stripe-redact-api
- description: The Refresh API from Stripe — 2 operation(s) for refresh.
  name: Stripe Refresh API
  slug: stripe-refresh-api
- description: The Refund API from Stripe — 3 operation(s) for refund.
  name: Stripe Refund API
  slug: stripe-refund-api
- description: The Reject API from Stripe — 1 operation(s) for reject.
  name: Stripe Reject API
  slug: stripe-reject-api
- description: The Reports API from Stripe — 2 operation(s) for reports.
  name: Stripe Reports API
  slug: stripe-reports-api
- description: The Retrieve API from Stripe — 10 operation(s) for retrieve.
  name: Stripe Retrieve API
  slug: stripe-retrieve-api
- description: The Reverse API from Stripe — 1 operation(s) for reverse.
  name: Stripe Reverse API
  slug: stripe-reverse-api
- description: The Search API from Stripe — 4 operation(s) for search.
  name: Stripe Search API
  slug: stripe-search-api
- description: The Secrets API from Stripe — 3 operation(s) for secrets.
  name: Stripe Secrets API
  slug: stripe-secrets-api
- description: The Send API from Stripe — 1 operation(s) for send.
  name: Stripe Send API
  slug: stripe-send-api
- description: The Sessions API from Stripe — 14 operation(s) for sessions.
  name: Stripe Sessions API
  slug: stripe-sessions-api
- description: The Settlement API from Stripe — 1 operation(s) for settlement.
  name: Stripe Settlement API
  slug: stripe-settlement-api
- description: The Settlements API from Stripe — 2 operation(s) for settlements.
  name: Stripe Settlements API
  slug: stripe-settlements-api
- description: The Setup Attempts API from Stripe — 1 operation(s) for setup attempts.
  name: Stripe Setup Attempts API
  slug: stripe-setup-attempts-api
- description: The Setup Intents API from Stripe — 6 operation(s) for setup intents.
  name: Stripe Setup Intents API
  slug: stripe-setup-intents-api
- description: The Subscribe API from Stripe — 1 operation(s) for subscribe.
  name: Stripe Subscribe API
  slug: stripe-subscribe-api
- description: The Subscription Items API from Stripe — 4 operation(s) for subscription items.
  name: Stripe Subscription Items API
  slug: stripe-subscription-items-api
- description: The Subscription Schedules API from Stripe — 4 operation(s) for subscription schedules.
  name: Stripe Subscription Schedules API
  slug: stripe-subscription-schedules-api
- description: The Subscriptions API from Stripe — 8 operation(s) for subscriptions.
  name: Stripe Subscriptions API
  slug: stripe-subscriptions-api
- description: The Tax Codes API from Stripe — 2 operation(s) for tax codes.
  name: Stripe Tax Codes API
  slug: stripe-tax-codes-api
- description: The Tax Rates API from Stripe — 2 operation(s) for tax rates.
  name: Stripe Tax Rates API
  slug: stripe-tax-rates-api
- description: The Transaction API from Stripe — 3 operation(s) for transaction.
  name: Stripe Transaction API
  slug: stripe-transaction-api
- description: The Transactions API from Stripe — 10 operation(s) for transactions.
  name: Stripe Transactions API
  slug: stripe-transactions-api
- description: The Unsubscribe API from Stripe — 1 operation(s) for unsubscribe.
  name: Stripe Unsubscribe API
  slug: stripe-unsubscribe-api
- description: The Upcoming API from Stripe — 2 operation(s) for upcoming.
  name: Stripe Upcoming API
  slug: stripe-upcoming-api
- description: The Update API from Stripe — 7 operation(s) for update.
  name: Stripe Update API
  slug: stripe-update-api
- description: The Validate API from Stripe — 1 operation(s) for validate.
  name: Stripe Validate API
  slug: stripe-validate-api
- description: The Verification API from Stripe — 6 operation(s) for verification.
  name: Stripe Verification API
  slug: stripe-verification-api
- description: The Verify API from Stripe — 3 operation(s) for verify.
  name: Stripe Verify API
  slug: stripe-verify-api
- description: The Void API from Stripe — 2 operation(s) for void.
  name: Stripe Void API
  slug: stripe-void-api
- description: The Webhook Endpoints API from Stripe — 2 operation(s) for webhook endpoints.
  name: Stripe Webhook Endpoints API
  slug: stripe-webhook-endpoints-api
arazzos:
- description: Add an item to a subscription, then update its quantity.
  name: Stripe Add and Scale Subscription Item
  slug: stripe-add-and-scale-subscription-item-workflow
- description: Create a payment method, attach it to a customer, then list the customer's saved methods.
  name: Stripe Attach Payment Method
  slug: stripe-attach-payment-method-workflow
- description: Authorize a payment with manual capture, poll until ready, then capture the funds.
  name: Stripe Authorize and Capture Payment
  slug: stripe-authorize-and-capture-payment-workflow
- description: Calculate tax for a set of line items, then record a Tax transaction from that calculation.
  name: Stripe Calculate and Settle Tax
  slug: stripe-calculate-and-settle-tax-workflow
- description: Retrieve a subscription to confirm it is active, then cancel it.
  name: Stripe Cancel Subscription
  slug: stripe-cancel-subscription-workflow
- description: Open a manual-capture PaymentIntent and cancel it to release the authorization.
  name: Stripe Cancel Uncaptured Payment
  slug: stripe-cancel-uncaptured-payment-workflow
- description: Create an uncaptured charge, capture it, then partially refund the captured amount.
  name: Stripe Capture and Partial Refund
  slug: stripe-capture-and-partial-refund-workflow
- description: Create a direct charge, then refund all or part of it.
  name: Stripe Charge and Refund
  slug: stripe-charge-and-refund-workflow
- description: Create a hosted Checkout Session, retrieve it, then list its line items.
  name: Stripe Checkout Session and Line Items
  slug: stripe-checkout-session-and-lineitems-workflow
- description: Create a Connect connected account, then mint an account link to start Stripe-hosted onboarding.
  name: Stripe Connect Onboard Account
  slug: stripe-connect-onboard-account-workflow
- description: Create a payout to a bank account, then cancel it while still pending.
  name: Stripe Create and Cancel Payout
  slug: stripe-create-and-cancel-payout-workflow
- description: Create a draft invoice, add a line item, then finalize it.
  name: Stripe Create and Finalize Invoice
  slug: stripe-create-and-finalize-invoice-workflow
- description: Create a customer, open a PaymentIntent for them, then confirm it to take payment.
  name: Stripe Create Customer and Pay
  slug: stripe-create-customer-and-pay-workflow
- description: Create a Product, then attach a reusable Price to it.
  name: Stripe Create Product and Price
  slug: stripe-create-product-and-price-workflow
- description: Create a Checkout Session and then expire it to prevent further use.
  name: Stripe Expire Checkout Session
  slug: stripe-expire-checkout-session-workflow
- description: Draft an invoice, add an item, finalize it, then charge it immediately.
  name: Stripe Invoice and Collect
  slug: stripe-invoice-and-collect-workflow
- description: Create an Issuing cardholder, then issue a virtual card to that cardholder.
  name: Stripe Issue Card to Cardholder
  slug: stripe-issue-card-to-cardholder-workflow
- description: Create a recurring product and price, then subscribe a customer to it.
  name: Stripe Launch Subscription
  slug: stripe-launch-subscription-workflow
- description: Create a Financial Connections session for an account holder, then list the accounts linked through it.
  name: Stripe Link Financial Account
  slug: stripe-link-financial-account-workflow
- description: Create a customer, save a payment method to them, then subscribe them to a plan.
  name: Stripe Onboard Customer to Plan
  slug: stripe-onboard-customer-to-plan-workflow
- description: Retrieve a subscription, pause its billing collection, then resume it.
  name: Stripe Pause and Resume Subscription
  slug: stripe-pause-and-resume-subscription-workflow
- description: Create a quote for a customer, finalize it, then accept it to generate the resulting invoice.
  name: Stripe Quote to Paid Invoice
  slug: stripe-quote-to-paid-invoice-workflow
- description: Confirm a PaymentIntent charge, then refund it via the Refunds API.
  name: Stripe Refund Payment Intent
  slug: stripe-refund-payment-intent-workflow
- description: Create a payout, retrieve it to confirm settlement, then reverse it back to the balance.
  name: Stripe Reverse Payout
  slug: stripe-reverse-payout-workflow
- description: Create a payment method, attach it to a customer, then charge it via a PaymentIntent.
  name: Stripe Save Card and Charge
  slug: stripe-save-card-and-charge-workflow
- description: Draft an invoice, add an item, finalize it, then email it to the customer.
  name: Stripe Send Invoice
  slug: stripe-send-invoice-workflow
- description: Create a SetupIntent to save a payment method for future off-session use, then confirm it.
  name: Stripe Set Up Future Payment
  slug: stripe-setup-future-payment-workflow
- description: Confirm a customer exists, then subscribe them to an existing price.
  name: Stripe Subscribe Existing Customer
  slug: stripe-subscribe-existing-customer-workflow
- description: Create an Identity VerificationSession, then retrieve it to read the verification outcome.
  name: Stripe Verify Identity
  slug: stripe-verify-identity-workflow
- description: Create and finalize an invoice, then void it to cancel the bill.
  name: Stripe Void Invoice
  slug: stripe-void-invoice-workflow
- description: Create and finalize an invoice, then mark it uncollectible.
  name: Stripe Write Off Invoice
  slug: stripe-write-off-invoice-workflow
artifact_total: 350
asyncapis:
- description: Stripe uses webhooks to notify your application when an event happens in your account. Webhooks are particularly useful for asynchronous events like when a customer's bank confirms a payment, a custom
  name: Stripe Webhooks
  slug: stripe-webhooks-asyncapi
collections:
- collection_type: postman
  name: Stripe Application Secrets API
  slug: postman-stripe-application-secrets-api
- collection_type: postman
  name: Stripe Balance API
  slug: postman-stripe-balance-api
- collection_type: postman
  name: Stripe Billing API
  slug: postman-stripe-billing-api
- collection_type: postman
  name: Stripe Billing Meters API
  slug: postman-stripe-billing-meters-api
- collection_type: postman
  name: Stripe Charges API
  slug: postman-stripe-charges-api
- collection_type: postman
  name: Stripe Checkout API
  slug: postman-stripe-checkout-api
- collection_type: postman
  name: Stripe Climate API
  slug: postman-stripe-climate-api
- collection_type: postman
  name: Stripe Connect API
  slug: postman-stripe-connect-api
- collection_type: postman
  name: Stripe Country API
  slug: postman-stripe-country-api
- collection_type: postman
  name: Stripe Coupons API
  slug: postman-stripe-coupons-api
- collection_type: postman
  name: Stripe Credit Notes API
  slug: postman-stripe-credit-notes-api
- collection_type: postman
  name: Stripe Crypto Onramp API
  slug: postman-stripe-crypto-onramp-api
- collection_type: postman
  name: Stripe Customer Portal API
  slug: postman-stripe-customer-portal-api
- collection_type: postman
  name: Stripe Customers API
  slug: postman-stripe-customers-api
- collection_type: postman
  name: Stripe Disputes API
  slug: postman-stripe-disputes-api
- collection_type: postman
  name: Stripe Entitlements API
  slug: postman-stripe-entitlements-api
- collection_type: postman
  name: Stripe Ephemeral Keys API
  slug: postman-stripe-ephemeral-keys-api
- collection_type: postman
  name: Stripe Events API
  slug: postman-stripe-events-api
- collection_type: postman
  name: Stripe Exchange Rates API
  slug: postman-stripe-exchange-rates-api
- collection_type: postman
  name: Stripe Files API
  slug: postman-stripe-files-api
- collection_type: postman
  name: Stripe Financial Connections API
  slug: postman-stripe-financial-connections-api
- collection_type: postman
  name: Stripe Forwarding API
  slug: postman-stripe-forwarding-api
- collection_type: postman
  name: Stripe Identity API
  slug: postman-stripe-identity-api
- collection_type: postman
  name: Stripe Invoice API
  slug: postman-stripe-invoice-api
- collection_type: postman
  name: Stripe Issuing API
  slug: postman-stripe-issuing-api
- collection_type: postman
  name: Stripe Link API
  slug: postman-stripe-link-api
- collection_type: postman
  name: Stripe Payment Intents API
  slug: postman-stripe-payment-intents-api
- collection_type: postman
  name: Stripe Payment Links API
  slug: postman-stripe-payment-links-api
- collection_type: postman
  name: Stripe Payment Method API
  slug: postman-stripe-payment-method-api
- collection_type: postman
  name: Stripe Payment Method Configurations API
  slug: postman-stripe-payment-method-configurations-api
- collection_type: postman
  name: Stripe Payouts API
  slug: postman-stripe-payouts-api
- collection_type: postman
  name: Stripe Plans API
  slug: postman-stripe-plans-api
- collection_type: postman
  name: Stripe Prices API
  slug: postman-stripe-prices-api
- collection_type: postman
  name: Stripe Products API
  slug: postman-stripe-products-api
- collection_type: postman
  name: Stripe Promotion Codes API
  slug: postman-stripe-promotion-codes-api
- collection_type: postman
  name: Stripe Quotes API
  slug: postman-stripe-quotes-api
- collection_type: postman
  name: Stripe Radar API
  slug: postman-stripe-radar-api
- collection_type: postman
  name: Stripe Refunds API
  slug: postman-stripe-refunds-api
- collection_type: postman
  name: Stripe Reporting API
  slug: postman-stripe-reporting-api
- collection_type: postman
  name: Stripe Revenue Recognition API
  slug: postman-stripe-revenue-recognition-api
- collection_type: postman
  name: Stripe Reviews API
  slug: postman-stripe-reviews-api
- collection_type: postman
  name: Stripe Setup API
  slug: postman-stripe-setup-api
- collection_type: postman
  name: Stripe Shipping Rates API
  slug: postman-stripe-shipping-rates-api
- collection_type: postman
  name: Stripe Sources API
  slug: postman-stripe-sigma-api
- collection_type: postman
  name: Stripe Sources API
  slug: postman-stripe-sources-api
- collection_type: postman
  name: Stripe Subscription API
  slug: postman-stripe-subscription-api
- collection_type: postman
  name: Stripe Tax API
  slug: postman-stripe-tax-api
- collection_type: postman
  name: Stripe Terminal API
  slug: postman-stripe-terminal-api
- collection_type: postman
  name: Stripe Test Helpers API
  slug: postman-stripe-test-helpers-api
- collection_type: postman
  name: Stripe Tokens API
  slug: postman-stripe-tokens-api
- collection_type: postman
  name: Stripe Transfers API
  slug: postman-stripe-topups-api
- collection_type: postman
  name: Stripe Transfers API
  slug: postman-stripe-transfers-api
- collection_type: postman
  name: Stripe Treasury API
  slug: postman-stripe-treasury-api
- collection_type: postman
  name: Stripe Webhook API
  slug: postman-stripe-webhook-api
- collection_type: open
  name: Stripe Payment Intents API
  slug: open-openapi:stripe-payment-intents-api
- collection_type: open
  name: Stripe Accounts API
  slug: open-stripe-accounts-api
- collection_type: open
  name: Stripe Apple Pay API
  slug: open-stripe-apple-pay-api
- collection_type: open
  name: Stripe Application Fees API
  slug: open-stripe-application-fees-api
- collection_type: open
  name: Stripe Application Secrets API
  slug: open-stripe-application-secrets-api
- collection_type: open
  name: Stripe Balance API
  slug: open-stripe-balance-api
- collection_type: open
  name: Stripe Billing API
  slug: open-stripe-billing-api
- collection_type: open
  name: Stripe Billing Meters API
  slug: open-stripe-billing-meters-api
- collection_type: open
  name: Stripe Charges API
  slug: open-stripe-charges-api
- collection_type: open
  name: Stripe Checkout API
  slug: open-stripe-checkout-api
- collection_type: open
  name: Stripe Climate API
  slug: open-stripe-climate-api
- collection_type: open
  name: Stripe Connect API
  slug: open-stripe-connect-api
- collection_type: open
  name: Stripe Country API
  slug: open-stripe-country-api
- collection_type: open
  name: Stripe Coupons API
  slug: open-stripe-coupons-api
- collection_type: open
  name: Stripe Credit Notes API
  slug: open-stripe-credit-notes-api
- collection_type: open
  name: Stripe Crypto Onramp API
  slug: open-stripe-crypto-onramp-api
- collection_type: open
  name: Stripe Customer Portal API
  slug: open-stripe-customer-portal-api
- collection_type: open
  name: Stripe Customers API
  slug: open-stripe-customers-api
- collection_type: open
  name: Stripe Disputes API
  slug: open-stripe-disputes-api
- collection_type: open
  name: Stripe Entitlements API
  slug: open-stripe-entitlements-api
- collection_type: open
  name: Stripe Ephemeral Keys API
  slug: open-stripe-ephemeral-keys-api
- collection_type: open
  name: Stripe Events API
  slug: open-stripe-events-api
- collection_type: open
  name: Stripe Exchange Rates API
  slug: open-stripe-exchange-rates-api
- collection_type: open
  name: Stripe Files API
  slug: open-stripe-files-api
- collection_type: open
  name: Stripe Financial Connections API
  slug: open-stripe-financial-connections-api
- collection_type: open
  name: Stripe Forwarding API
  slug: open-stripe-forwarding-api
- collection_type: open
  name: Stripe Identity API
  slug: open-stripe-identity-api
- collection_type: open
  name: Stripe Invoice API
  slug: open-stripe-invoice-api
- collection_type: open
  name: Stripe Issuing API
  slug: open-stripe-issuing-api
- collection_type: open
  name: Stripe Link API
  slug: open-stripe-link-api
- collection_type: open
  name: Stripe Payment Intents API
  slug: open-stripe-payment-intents-api
- collection_type: open
  name: Stripe Payment Links API
  slug: open-stripe-payment-links-api
- collection_type: open
  name: Stripe Payment Method API
  slug: open-stripe-payment-method-api
- collection_type: open
  name: Stripe Payment Method Configurations API
  slug: open-stripe-payment-method-configurations-api
- collection_type: open
  name: Stripe Payouts API
  slug: open-stripe-payouts-api
- collection_type: open
  name: Stripe Plans API
  slug: open-stripe-plans-api
- collection_type: open
  name: Stripe Prices API
  slug: open-stripe-prices-api
- collection_type: open
  name: Stripe Products API
  slug: open-stripe-products-api
- collection_type: open
  name: Stripe Promotion Codes API
  slug: open-stripe-promotion-codes-api
- collection_type: open
  name: Stripe Quotes API
  slug: open-stripe-quotes-api
- collection_type: open
  name: Stripe Radar API
  slug: open-stripe-radar-api
- collection_type: open
  name: Stripe Refunds API
  slug: open-stripe-refunds-api
- collection_type: open
  name: Stripe Reporting API
  slug: open-stripe-reporting-api
- collection_type: open
  name: Stripe Revenue Recognition API
  slug: open-stripe-revenue-recognition-api
- collection_type: open
  name: Stripe Setup API
  slug: open-stripe-setup-api
- collection_type: open
  name: Stripe Shipping Rates API
  slug: open-stripe-shipping-rates-api
- collection_type: open
  name: Stripe Sources API
  slug: open-stripe-sigma-api
- collection_type: open
  name: Stripe Sources API
  slug: open-stripe-sources-api
- collection_type: open
  name: Stripe Subscription API
  slug: open-stripe-subscription-api
- collection_type: open
  name: Stripe Tax API
  slug: open-stripe-tax-api
- collection_type: open
  name: Stripe Terminal API
  slug: open-stripe-terminal-api
- collection_type: open
  name: Stripe Test Helpers API
  slug: open-stripe-test-helpers-api
- collection_type: open
  name: Stripe Tokens API
  slug: open-stripe-tokens-api
- collection_type: open
  name: Stripe Transfers API
  slug: open-stripe-topups-api
- collection_type: open
  name: Stripe Transfers API
  slug: open-stripe-transfers-api
- collection_type: open
  name: Stripe Treasury API
  slug: open-stripe-treasury-api
- collection_type: open
  name: Stripe Webhook API
  slug: open-stripe-webhook-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stripe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stripe-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stripe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stripe-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stripe-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stripe-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stripe-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stripe-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stripe-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/stripe-cli.yml
- group: design
  title: ''
  type: Components
  url: components/stripe-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stripe-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/stripe-decline-codes.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.stripe.com
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stripe/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-add-and-scale-subscription-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-attach-payment-method-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-authorize-and-capture-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-cancel-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-cancel-uncaptured-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-capture-and-partial-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-charge-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-checkout-session-and-lineitems-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-and-cancel-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-and-finalize-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-customer-and-pay-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-product-and-price-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-expire-checkout-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-invoice-and-collect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-launch-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-onboard-customer-to-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-pause-and-resume-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-refund-payment-intent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-reverse-payout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-save-card-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-send-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-subscribe-existing-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-void-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-write-off-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-connect-onboard-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-issue-card-to-cardholder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-verify-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-link-financial-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-setup-future-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-calculate-and-settle-tax-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/stripe-quote-to-paid-invoice-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stripe
- group: start
  title: ''
  type: Signup
  url: https://dashboard.stripe.com/register
- group: start
  title: ''
  type: Portal
  url: https://dashboard.stripe.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stripe.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stripe.com/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stripe.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://stripe.com/docs/api/authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.stripe.com/api/errors
- group: build
  title: ''
  type: SDKs
  url: https://docs.stripe.com/sdks
- group: build
  title: ''
  type: CLI
  url: https://docs.stripe.com/stripe-cli
- group: company
  title: ''
  type: Blog
  url: https://stripe.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.stripe.com/changelog
- group: design
  title: ''
  type: Versioning
  url: https://docs.stripe.com/upgrades
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stripe.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.stripe.com/rate-limits
- group: auth
  title: ''
  type: Security
  url: https://docs.stripe.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stripe.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stripe.com/legal/ssa
- group: commercial
  title: ''
  type: Pricing
  url: https://stripe.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.stripe.com/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/stripe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stripe
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/stripe/openapi
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/stripedev/workspace/stripe-developers/overview
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/stripe/stripe-node
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/stripe/stripe-python
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/stripe/stripe-php
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/stripe/stripe-ruby
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/stripe/stripe-java
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/stripe/stripe-go
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/stripe/stripe-dotnet
- group: build
  title: ''
  type: iOS SDK
  url: https://github.com/stripe/stripe-ios
- group: build
  title: ''
  type: Android SDK
  url: https://github.com/stripe/stripe-android
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/stripe
- group: company
  title: ''
  type: X (Twitter) Developer
  url: https://x.com/StripeDev
- group: design
  title: ''
  type: Webhooks
  url: https://docs.stripe.com/webhooks
- group: design
  title: ''
  type: Testing
  url: https://docs.stripe.com/testing
- group: design
  title: ''
  type: Expanding Objects
  url: https://docs.stripe.com/api/expanding_objects
- group: design
  title: ''
  type: Pagination
  url: https://docs.stripe.com/api/pagination
- group: design
  title: ''
  type: Idempotent Requests
  url: https://docs.stripe.com/api/idempotent_requests
- group: design
  title: ''
  type: Metadata
  url: https://docs.stripe.com/api/metadata
- group: other
  title: ''
  type: Stripe Apps
  url: https://docs.stripe.com/building-extensions/stripe-apps
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.stripe.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@StripeDevelopers
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/stripe-payments
- group: company
  title: ''
  type: Website
  url: https://stripe.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.stripe.com/login
- group: build
  title: ''
  type: Code Samples
  url: https://docs.stripe.com/samples
- group: auth
  title: ''
  type: API Keys
  url: https://docs.stripe.com/keys
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/stripe-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-customer.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-payment-intent.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-subscription.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-charge.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-invoice.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-event.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-product.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stripe-price.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/stripe-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/stripe-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stripe-vocabulary.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stripe-payment-intent-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stripe-customer-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stripe-invoice-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/stripe-create-payment-intent-example.json
- group: build
  title: ''
  type: Examples
  url: examples/stripe-create-checkout-session-example.json
- group: build
  title: ''
  type: Examples
  url: examples/stripe-create-customer-example.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stripe.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stripe-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stripe-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stripe-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stripe-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stripe-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/stripe-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stripe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stripe-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.stripe.com/upgrades
- group: design
  title: ''
  type: Idempotency
  url: conventions/stripe-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.stripe.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: 2024/04/14
description: Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes.
examples:
- key_count: 2
  name: Stripe Create Checkout Session Example
  slug: stripe-create-checkout-session-example
- key_count: 2
  name: Stripe Create Customer Example
  slug: stripe-create-customer-example
- key_count: 2
  name: Stripe Create Payment Intent Example
  slug: stripe-create-payment-intent-example
features:
- Payments API for one-time and saved payment methods (100+ payment methods)
- Payment Intents API for SCA-compliant card flows
- Setup Intents for save-card-without-charge
- Subscriptions and Invoicing via Billing API
- Pay-as-you-go Billing at 0.7% of volume, or $620+/mo flat
- 'Stripe Tax: automated tax calculation, registration, and filing in 90+ countries'
- Connect for marketplaces and platforms
- Issuing for virtual and physical card programs
- Identity for KYC document verification
- Treasury for embedded banking-as-a-service
- Climate for carbon removal
- Sigma for SQL analytics on your Stripe data ($15/mo)
- Data Pipeline for warehouse delivery ($65/mo)
- Radar for fraud prevention with ML risk scoring (free or per-screened)
- 100 RPS read/write in live mode, 25 RPS in test mode
- Idempotency-Key support for safe retries
- Webhooks with signed event payloads
- Custom interchange-plus pricing for high-volume merchants
finops:
- name: Stripe Finops
  service_category: Payments
  slug: stripe-finops
graphqls:
- description: Stripe does not offer a public GraphQL API. Its developer-facing surface is entirely REST-based
  name: Stripe GraphQL
  slug: stripe-graphql
image: https://stripe.com/img/about/logos/logos/blue.png
json_schemas:
- name: Stripe Charge
  property_count: 44
  slug: stripe-charge
- name: Stripe Customer
  property_count: 25
  slug: stripe-customer
- name: Stripe Event
  property_count: 10
  slug: stripe-event
- name: Stripe Invoice
  property_count: 43
  slug: stripe-invoice
- name: Stripe Payment Intent
  property_count: 37
  slug: stripe-payment-intent
- name: Stripe Price
  property_count: 21
  slug: stripe-price
- name: Stripe Product
  property_count: 19
  slug: stripe-product
- name: Stripe Subscription
  property_count: 43
  slug: stripe-subscription
json_structures:
- name: Stripe Customer Structure
  property_count: 16
  slug: stripe-customer-structure
- name: Stripe Invoice Structure
  property_count: 21
  slug: stripe-invoice-structure
- name: Stripe Payment Intent Structure
  property_count: 17
  slug: stripe-payment-intent-structure
jsonld:
- class_count: 0
  name: Stripe Context
  property_count: 8
  slug: stripe-context
layout: provider
mcp_servers:
- description: Stripe's remote MCP server exposes the Stripe API and knowledge base to MCP clients over OAuth or restricted API keys; npx @stripe/mcp for local use.
  name: MCP Server
  slug: mcp-server
- description: ''
  name: Stripe MCP Server manifest
  slug: stripe-mcp-server-manifest
modified: '2026-07-17'
name: Stripe
nav: Providers
network: true
overview: 'Stripe publishes 159 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balance API, Billing API, and 156 more. Tagged areas include Commerce, Financial Services, Fintech, Payments, and T1.


  The Stripe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Stripe''s developer surface includes authentication, sandbox, changelog, CLI, signup flow, developer portal, documentation, and 119 more developer resources.'
plans:
- name: Stripe Plans Pricing
  plan_count: 9
  slug: stripe-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 6
  name: Stripe Rate Limits
  slug: stripe-rate-limits
rules:
- name: Stripe API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: stripe-asyncapi-spectral-rules
- name: Stripe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stripe-jsonschema-spectral-rules
- name: Stripe API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 3
    info: 0
    warn: 5
  slug: stripe-rules
scopes:
- name: Stripe Scopes
  scope_count: 2
  slug: stripe-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 84.7
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 72.9
    developer_ergonomics: 95.1
    discoverability: 59.3
    governance: 63.5
    operational_transparency: 94.7
  previous_composite: 84.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 159
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 93.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stripe/refs/heads/main/screenshots/stripe-2026-06-20T161306.png
security:
- kind: authentication
  name: Stripe Authentication
  slug: stripe-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Stripe Domain Security
  slug: stripe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stripe Vulnerability Disclosure
  slug: stripe-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Stripe Trust Center
  slug: stripe-trust-center
  summary_line: PCI DSS, SOC 1 Type II, SOC 2 Type II, SOC 3, EMVCo Level 1 and 2, PCI PA-DSS, NIST Cybersecurity Framework, APEC CBPR and PRP, EU-US Data Privacy Framework
slug: stripe
tags:
- Commerce
- Financial Services
- Fintech
- Payments
- T1
website: https://stripe.com
---
