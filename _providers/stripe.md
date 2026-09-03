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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 483
  human_in_the_loop: 2
  name: Stripe Agentic Access
  operation_count: 910
  slug: stripe-agentic-access
  summary_line: 910 operations · 483 acting · 2 human-in-the-loop
api_count: 48
apis:
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts
  name: Stripe Accounts API
  slug: stripe-accounts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transac
  name: Stripe Balance API
  slug: stripe-balance-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Create and manage subscriptions, recurring payments, and recurring revenue.
  name: Stripe Billing API
  slug: stripe-billing-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe '
  name: Stripe Charges API
  slug: stripe-charges-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment pa
  name: Stripe Checkout API
  slug: stripe-checkout-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.
  name: Stripe Climate API
  slug: stripe-climate-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to
  name: Stripe Country API
  slug: stripe-country-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. '
  name: Stripe Coupons API
  slug: stripe-coupons-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Issue a credit note to adjust an invoice's amount after the invoice is finalized.
  name: Stripe Credit Notes API
  slug: stripe-credit-notes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.
  name: Stripe Customers API
  slug: stripe-customers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitim
  name: Stripe Disputes API
  slug: stripe-disputes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side
  name: Stripe Ephemeral Keys API
  slug: stripe-ephemeral-keys-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.
  name: Stripe Events API
  slug: stripe-events-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer''s native currency. Doing so can improve sales and help customers avoid conversion costs. In order to '
  name: Stripe Exchange Rates API
  slug: stripe-exchange-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'This object represents files hosted on Stripe''s servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for '
  name: Stripe Files API
  slug: stripe-files-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such '
  name: Stripe Financial Connections API
  slug: stripe-financial-connections-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.
  name: Stripe Identity API
  slug: stripe-identity-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.
  name: Stripe Invoice API
  slug: stripe-invoice-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: An API for businesses to instantly create, manage, and distribute payment cards.
  name: Stripe Issuing API
  slug: stripe-issuing-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.
  name: Stripe Link API
  slug: stripe-link-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You
  name: Stripe Payment Intents API
  slug: stripe-payment-intents-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new '
  name: Stripe Payment Links API
  slug: stripe-payment-links-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, '
  name: Stripe Payouts API
  slug: stripe-payouts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.
  name: Stripe Plans API
  slug: stripe-plans-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track '
  name: Stripe Prices API
  slug: stripe-prices-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Pro
  name: Stripe Products API
  slug: stripe-products-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.
  name: Stripe Promotion Codes API
  slug: stripe-promotion-codes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.
  name: Stripe Quotes API
  slug: stripe-quotes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.
  name: Stripe Radar API
  slug: stripe-radar-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.
  name: Stripe Refunds API
  slug: stripe-refunds-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can sch
  name: Stripe Reporting API
  slug: stripe-reporting-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Reviews can be used to supplement automated fraud detection with human expertise.
  name: Stripe Reviews API
  slug: stripe-reviews-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Shipping rates describe the price of shipping presented to your customers and applied to a purchase.
  name: Stripe Shipping Rates API
  slug: stripe-shipping-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve
  name: Stripe Sigma API
  slug: stripe-sigma-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can b
  name: Stripe Sources API
  slug: stripe-sources-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.
  name: Stripe Tax API
  slug: stripe-tax-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.
  name: Stripe Terminal API
  slug: stripe-terminal-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.
  name: Stripe Test Helpers API
  slug: stripe-test-helpers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token repres
  name: Stripe Tokens API
  slug: stripe-tokens-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.
  name: Stripe Topups API
  slug: stripe-topups-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Transfer object is created when you move funds between Stripe accounts as part of Connect.
  name: Stripe Transfers API
  slug: stripe-transfers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage thei
  name: Stripe Treasury API
  slug: stripe-treasury-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Connect is a set of programmable APIs and tools that lets you facilitate payments on your software platform, build a marketplace, and pay out sellers or service providers globally.
  name: Stripe Connect API
  slug: stripe-connect-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Billing customer portal is a Stripe-hosted UI for subscription and billing management. A portal session describes the instantiation of the customer portal for a particular customer. By visiting th
  name: Stripe Customer Portal API
  slug: stripe-customer-portal-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access according to yo
  name: Stripe Entitlements API
  slug: stripe-entitlements-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Vault and Forward API allows you to tokenize and store card details in Stripes PCI-compliant vault and forward that data to supported third-party processors or endpoints.
  name: Stripe Forwarding API
  slug: stripe-forwarding-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application at checkout.
  name: Stripe Crypto Onramp API
  slug: stripe-crypto-onramp-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Automate your accrual accounting process with Stripe Revenue Recognition. Import transaction data, set up rules, and download revenue reports for compliance with accounting standards like ASC 606.
  name: Stripe Revenue Recognition API
  slug: stripe-revenue-recognition-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Meters specify how to aggregate meter events over a billing period for usage-based pricing. Meter events represent customer actions and support up to 10,000 events per second via the V2 meter event st
  name: Stripe Billing Meters API
  slug: stripe-billing-meters-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Payment method configurations allow you to configure which payment methods are available to your customers during checkout. Manage payment method availability across multiple Connect accounts.
  name: Stripe Payment Method Configurations API
  slug: stripe-payment-method-configurations-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Account API from Stripe — 12 operation(s) for account.
  name: Stripe Account API
  slug: stripe-account-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Apple API from Stripe — 2 operation(s) for apple.
  name: Stripe Apple API
  slug: stripe-apple-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Applications API from Stripe — 8 operation(s) for applications.
  name: Stripe Applications API
  slug: stripe-applications-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Apply API from Stripe — 1 operation(s) for apply.
  name: Stripe Apply API
  slug: stripe-apply-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Approve API from Stripe — 1 operation(s) for approve.
  name: Stripe Approve API
  slug: stripe-approve-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Attach API from Stripe — 1 operation(s) for attach.
  name: Stripe Attach API
  slug: stripe-attach-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Authorization API from Stripe — 5 operation(s) for authorization.
  name: Stripe Authorization API
  slug: stripe-authorization-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Balance Transactions API from Stripe — 2 operation(s) for balance transactions.
  name: Stripe Balance Transactions API
  slug: stripe-balance-transactions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Bank API from Stripe — 5 operation(s) for bank.
  name: Stripe Bank API
  slug: stripe-bank-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Billing Portal API from Stripe — 3 operation(s) for billing portal.
  name: Stripe Billing Portal API
  slug: stripe-billing-portal-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Cancel API from Stripe — 3 operation(s) for cancel.
  name: Stripe Cancel API
  slug: stripe-cancel-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Capabilities API from Stripe — 1 operation(s) for capabilities.
  name: Stripe Capabilities API
  slug: stripe-capabilities-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Capability API from Stripe — 1 operation(s) for capability.
  name: Stripe Capability API
  slug: stripe-capability-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Capture API from Stripe — 1 operation(s) for capture.
  name: Stripe Capture API
  slug: stripe-capture-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Card API from Stripe — 1 operation(s) for card.
  name: Stripe Card API
  slug: stripe-card-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Cards API from Stripe — 4 operation(s) for cards.
  name: Stripe Cards API
  slug: stripe-cards-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Cash API from Stripe — 3 operation(s) for cash.
  name: Stripe Cash API
  slug: stripe-cash-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Close API from Stripe — 1 operation(s) for close.
  name: Stripe Close API
  slug: stripe-close-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Configuration API from Stripe — 1 operation(s) for configuration.
  name: Stripe Configuration API
  slug: stripe-configuration-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Configurations API from Stripe — 4 operation(s) for configurations.
  name: Stripe Configurations API
  slug: stripe-configurations-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Confirm API from Stripe — 1 operation(s) for confirm.
  name: Stripe Confirm API
  slug: stripe-confirm-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Connections API from Stripe — 11 operation(s) for connections.
  name: Stripe Connections API
  slug: stripe-connections-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Country Specs API from Stripe — 2 operation(s) for country specs.
  name: Stripe Country Specs API
  slug: stripe-country-specs-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Coupon API from Stripe — 1 operation(s) for coupon.
  name: Stripe Coupon API
  slug: stripe-coupon-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Create API from Stripe — 10 operation(s) for create.
  name: Stripe Create API
  slug: stripe-create-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Credit API from Stripe — 6 operation(s) for credit.
  name: Stripe Credit API
  slug: stripe-credit-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Customer API from Stripe — 24 operation(s) for customer.
  name: Stripe Customer API
  slug: stripe-customer-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Decline API from Stripe — 1 operation(s) for decline.
  name: Stripe Decline API
  slug: stripe-decline-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Delete API from Stripe — 20 operation(s) for delete.
  name: Stripe Delete API
  slug: stripe-delete-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Detach API from Stripe — 1 operation(s) for detach.
  name: Stripe Detach API
  slug: stripe-detach-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Disconnect API from Stripe — 2 operation(s) for disconnect.
  name: Stripe Disconnect API
  slug: stripe-disconnect-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Discount API from Stripe — 2 operation(s) for discount.
  name: Stripe Discount API
  slug: stripe-discount-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Dispute API from Stripe — 2 operation(s) for dispute.
  name: Stripe Dispute API
  slug: stripe-dispute-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Domain API from Stripe — 2 operation(s) for domain.
  name: Stripe Domain API
  slug: stripe-domain-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Domains API from Stripe — 4 operation(s) for domains.
  name: Stripe Domains API
  slug: stripe-domains-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Exchange API from Stripe — 2 operation(s) for exchange.
  name: Stripe Exchange API
  slug: stripe-exchange-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Expire API from Stripe — 1 operation(s) for expire.
  name: Stripe Expire API
  slug: stripe-expire-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The External API from Stripe — 2 operation(s) for external.
  name: Stripe External API
  slug: stripe-external-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Fee API from Stripe — 4 operation(s) for fee.
  name: Stripe Fee API
  slug: stripe-fee-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Finalize API from Stripe — 1 operation(s) for finalize.
  name: Stripe Finalize API
  slug: stripe-finalize-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Financial API from Stripe — 11 operation(s) for financial.
  name: Stripe Financial API
  slug: stripe-financial-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Find API from Stripe — 1 operation(s) for find.
  name: Stripe Find API
  slug: stripe-find-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Funding API from Stripe — 1 operation(s) for funding.
  name: Stripe Funding API
  slug: stripe-funding-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Get API from Stripe — 106 operation(s) for get.
  name: Stripe Get API
  slug: stripe-get-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The History API from Stripe — 2 operation(s) for history.
  name: Stripe History API
  slug: stripe-history-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Identifiers API from Stripe — 15 operation(s) for identifiers.
  name: Stripe Identifiers API
  slug: stripe-identifiers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Increment API from Stripe — 1 operation(s) for increment.
  name: Stripe Increment API
  slug: stripe-increment-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Intents API from Stripe — 9 operation(s) for intents.
  name: Stripe Intents API
  slug: stripe-intents-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Invoiceitems API from Stripe — 2 operation(s) for invoiceitems.
  name: Stripe Invoiceitems API
  slug: stripe-invoiceitems-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Invoices API from Stripe — 12 operation(s) for invoices.
  name: Stripe Invoices API
  slug: stripe-invoices-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Item API from Stripe — 1 operation(s) for item.
  name: Stripe Item API
  slug: stripe-item-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Items API from Stripe — 4 operation(s) for items.
  name: Stripe Items API
  slug: stripe-items-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Keys API from Stripe — 2 operation(s) for keys.
  name: Stripe Keys API
  slug: stripe-keys-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Line API from Stripe — 3 operation(s) for line.
  name: Stripe Line API
  slug: stripe-line-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Lines API from Stripe — 5 operation(s) for lines.
  name: Stripe Lines API
  slug: stripe-lines-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Link Account Sessions API from Stripe — 2 operation(s) for link account sessions.
  name: Stripe Link Account Sessions API
  slug: stripe-link-account-sessions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Linked Accounts API from Stripe — 5 operation(s) for linked accounts.
  name: Stripe Linked Accounts API
  slug: stripe-linked-accounts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Linked API from Stripe — 5 operation(s) for linked.
  name: Stripe Linked API
  slug: stripe-linked-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Links API from Stripe — 3 operation(s) for links.
  name: Stripe Links API
  slug: stripe-links-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Lists API from Stripe — 8 operation(s) for lists.
  name: Stripe Lists API
  slug: stripe-lists-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Login API from Stripe — 1 operation(s) for login.
  name: Stripe Login API
  slug: stripe-login-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Mark API from Stripe — 1 operation(s) for mark.
  name: Stripe Mark API
  slug: stripe-mark-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Method API from Stripe — 6 operation(s) for method.
  name: Stripe Method API
  slug: stripe-method-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Methods API from Stripe — 6 operation(s) for methods.
  name: Stripe Methods API
  slug: stripe-methods-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Microdeposits API from Stripe — 1 operation(s) for microdeposits.
  name: Stripe Microdeposits API
  slug: stripe-microdeposits-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Note API from Stripe — 1 operation(s) for note.
  name: Stripe Note API
  slug: stripe-note-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Notes API from Stripe — 6 operation(s) for notes.
  name: Stripe Notes API
  slug: stripe-notes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Owners API from Stripe — 2 operation(s) for owners.
  name: Stripe Owners API
  slug: stripe-owners-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Pay API from Stripe — 3 operation(s) for pay.
  name: Stripe Pay API
  slug: stripe-pay-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Payment Method Domains API from Stripe — 3 operation(s) for payment method domains.
  name: Stripe Payment Method Domains API
  slug: stripe-payment-method-domains-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Payment Methods API from Stripe — 4 operation(s) for payment methods.
  name: Stripe Payment Methods API
  slug: stripe-payment-methods-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Payments API from Stripe — 23 operation(s) for payments.
  name: Stripe Payments API
  slug: stripe-payments-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Person API from Stripe — 4 operation(s) for person.
  name: Stripe Person API
  slug: stripe-person-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Persons API from Stripe — 2 operation(s) for persons.
  name: Stripe Persons API
  slug: stripe-persons-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Post API from Stripe — 95 operation(s) for post.
  name: Stripe Post API
  slug: stripe-post-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Preview API from Stripe — 2 operation(s) for preview.
  name: Stripe Preview API
  slug: stripe-preview-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Rate API from Stripe — 1 operation(s) for rate.
  name: Stripe Rate API
  slug: stripe-rate-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Rates API from Stripe — 2 operation(s) for rates.
  name: Stripe Rates API
  slug: stripe-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Redact API from Stripe — 1 operation(s) for redact.
  name: Stripe Redact API
  slug: stripe-redact-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Refresh API from Stripe — 2 operation(s) for refresh.
  name: Stripe Refresh API
  slug: stripe-refresh-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Refund API from Stripe — 3 operation(s) for refund.
  name: Stripe Refund API
  slug: stripe-refund-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Reject API from Stripe — 1 operation(s) for reject.
  name: Stripe Reject API
  slug: stripe-reject-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Reports API from Stripe — 2 operation(s) for reports.
  name: Stripe Reports API
  slug: stripe-reports-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Retrieve API from Stripe — 10 operation(s) for retrieve.
  name: Stripe Retrieve API
  slug: stripe-retrieve-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Reverse API from Stripe — 1 operation(s) for reverse.
  name: Stripe Reverse API
  slug: stripe-reverse-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Search API from Stripe — 4 operation(s) for search.
  name: Stripe Search API
  slug: stripe-search-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Secrets API from Stripe — 3 operation(s) for secrets.
  name: Stripe Secrets API
  slug: stripe-secrets-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Send API from Stripe — 1 operation(s) for send.
  name: Stripe Send API
  slug: stripe-send-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Sessions API from Stripe — 14 operation(s) for sessions.
  name: Stripe Sessions API
  slug: stripe-sessions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Settlement API from Stripe — 1 operation(s) for settlement.
  name: Stripe Settlement API
  slug: stripe-settlement-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Settlements API from Stripe — 2 operation(s) for settlements.
  name: Stripe Settlements API
  slug: stripe-settlements-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Setup Attempts API from Stripe — 1 operation(s) for setup attempts.
  name: Stripe Setup Attempts API
  slug: stripe-setup-attempts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Setup Intents API from Stripe — 6 operation(s) for setup intents.
  name: Stripe Setup Intents API
  slug: stripe-setup-intents-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscribe API from Stripe — 1 operation(s) for subscribe.
  name: Stripe Subscribe API
  slug: stripe-subscribe-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscription Items API from Stripe — 4 operation(s) for subscription items.
  name: Stripe Subscription Items API
  slug: stripe-subscription-items-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscription Schedules API from Stripe — 4 operation(s) for subscription schedules.
  name: Stripe Subscription Schedules API
  slug: stripe-subscription-schedules-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscriptions API from Stripe — 8 operation(s) for subscriptions.
  name: Stripe Subscriptions API
  slug: stripe-subscriptions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Tax Codes API from Stripe — 2 operation(s) for tax codes.
  name: Stripe Tax Codes API
  slug: stripe-tax-codes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Tax Rates API from Stripe — 2 operation(s) for tax rates.
  name: Stripe Tax Rates API
  slug: stripe-tax-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Transaction API from Stripe — 3 operation(s) for transaction.
  name: Stripe Transaction API
  slug: stripe-transaction-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Transactions API from Stripe — 10 operation(s) for transactions.
  name: Stripe Transactions API
  slug: stripe-transactions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Unsubscribe API from Stripe — 1 operation(s) for unsubscribe.
  name: Stripe Unsubscribe API
  slug: stripe-unsubscribe-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Upcoming API from Stripe — 2 operation(s) for upcoming.
  name: Stripe Upcoming API
  slug: stripe-upcoming-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Update API from Stripe — 7 operation(s) for update.
  name: Stripe Update API
  slug: stripe-update-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Validate API from Stripe — 1 operation(s) for validate.
  name: Stripe Validate API
  slug: stripe-validate-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Verification API from Stripe — 6 operation(s) for verification.
  name: Stripe Verification API
  slug: stripe-verification-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Verify API from Stripe — 3 operation(s) for verify.
  name: Stripe Verify API
  slug: stripe-verify-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Void API from Stripe — 2 operation(s) for void.
  name: Stripe Void API
  slug: stripe-void-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Webhook Endpoints API from Stripe — 2 operation(s) for webhook endpoints.
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
artifact_total: 459
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stripe Payment Intents API
  slug: open-openapi:stripe-payment-intents-api
- collection_type: open
  name: Stripe Accounts Account API
  slug: open-stripe-account-api
- collection_type: open
  name: Stripe Account Accounts API
  slug: open-stripe-accounts-api
- collection_type: open
  name: Stripe Accounts Account Apple API
  slug: open-stripe-apple-api
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
  name: Stripe Accounts Account Applications API
  slug: open-stripe-applications-api
- collection_type: open
  name: Stripe Accounts Account Apply API
  slug: open-stripe-apply-api
- collection_type: open
  name: Stripe Accounts Account Approve API
  slug: open-stripe-approve-api
- collection_type: open
  name: Stripe Accounts Account Attach API
  slug: open-stripe-attach-api
- collection_type: open
  name: Stripe Accounts Account Authorization API
  slug: open-stripe-authorization-api
- collection_type: open
  name: Stripe Accounts Account Balance API
  slug: open-stripe-balance-api
- collection_type: open
  name: Stripe Accounts Account Balance Transactions API
  slug: open-stripe-balance-transactions-api
- collection_type: open
  name: Stripe Accounts Account Bank API
  slug: open-stripe-bank-api
- collection_type: open
  name: Stripe Accounts Account Billing API
  slug: open-stripe-billing-api
- collection_type: open
  name: Stripe Accounts Account Billing Meters API
  slug: open-stripe-billing-meters-api
- collection_type: open
  name: Stripe Accounts Account Billing Portal API
  slug: open-stripe-billing-portal-api
- collection_type: open
  name: Stripe Accounts Account Cancel API
  slug: open-stripe-cancel-api
- collection_type: open
  name: Stripe Accounts Account Capabilities API
  slug: open-stripe-capabilities-api
- collection_type: open
  name: Stripe Accounts Account Capability API
  slug: open-stripe-capability-api
- collection_type: open
  name: Stripe Accounts Account Capture API
  slug: open-stripe-capture-api
- collection_type: open
  name: Stripe Accounts Account Card API
  slug: open-stripe-card-api
- collection_type: open
  name: Stripe Accounts Account Cards API
  slug: open-stripe-cards-api
- collection_type: open
  name: Stripe Accounts Account Cash API
  slug: open-stripe-cash-api
- collection_type: open
  name: Stripe Accounts Account Charges API
  slug: open-stripe-charges-api
- collection_type: open
  name: Stripe Accounts Account Checkout API
  slug: open-stripe-checkout-api
- collection_type: open
  name: Stripe Accounts Account Climate API
  slug: open-stripe-climate-api
- collection_type: open
  name: Stripe Accounts Account Close API
  slug: open-stripe-close-api
- collection_type: open
  name: Stripe Accounts Account Configuration API
  slug: open-stripe-configuration-api
- collection_type: open
  name: Stripe Accounts Account Configurations API
  slug: open-stripe-configurations-api
- collection_type: open
  name: Stripe Accounts Account Confirm API
  slug: open-stripe-confirm-api
- collection_type: open
  name: Stripe Accounts Account Connect API
  slug: open-stripe-connect-api
- collection_type: open
  name: Stripe Accounts Account Connections API
  slug: open-stripe-connections-api
- collection_type: open
  name: Stripe Accounts Account Country API
  slug: open-stripe-country-api
- collection_type: open
  name: Stripe Accounts Account Country Specs API
  slug: open-stripe-country-specs-api
- collection_type: open
  name: Stripe Accounts Account Coupon API
  slug: open-stripe-coupon-api
- collection_type: open
  name: Stripe Accounts Account Coupons API
  slug: open-stripe-coupons-api
- collection_type: open
  name: Stripe Accounts Account Create API
  slug: open-stripe-create-api
- collection_type: open
  name: Stripe Accounts Account Credit API
  slug: open-stripe-credit-api
- collection_type: open
  name: Stripe Accounts Account Credit Notes API
  slug: open-stripe-credit-notes-api
- collection_type: open
  name: Stripe Accounts Account Crypto Onramp API
  slug: open-stripe-crypto-onramp-api
- collection_type: open
  name: Stripe Accounts Account Customer API
  slug: open-stripe-customer-api
- collection_type: open
  name: Stripe Accounts Account Customer Portal API
  slug: open-stripe-customer-portal-api
- collection_type: open
  name: Stripe Accounts Account Customers API
  slug: open-stripe-customers-api
- collection_type: open
  name: Stripe Accounts Account Decline API
  slug: open-stripe-decline-api
- collection_type: open
  name: Stripe Accounts Account Delete API
  slug: open-stripe-delete-api
- collection_type: open
  name: Stripe Accounts Account Detach API
  slug: open-stripe-detach-api
- collection_type: open
  name: Stripe Accounts Account Disconnect API
  slug: open-stripe-disconnect-api
- collection_type: open
  name: Stripe Accounts Account Discount API
  slug: open-stripe-discount-api
- collection_type: open
  name: Stripe Accounts Account Dispute API
  slug: open-stripe-dispute-api
- collection_type: open
  name: Stripe Accounts Account Disputes API
  slug: open-stripe-disputes-api
- collection_type: open
  name: Stripe Accounts Account Domain API
  slug: open-stripe-domain-api
- collection_type: open
  name: Stripe Accounts Account Domains API
  slug: open-stripe-domains-api
- collection_type: open
  name: Stripe Accounts Account Entitlements API
  slug: open-stripe-entitlements-api
- collection_type: open
  name: Stripe Accounts Account Ephemeral Keys API
  slug: open-stripe-ephemeral-keys-api
- collection_type: open
  name: Stripe Accounts Account Events API
  slug: open-stripe-events-api
- collection_type: open
  name: Stripe Accounts Account Exchange API
  slug: open-stripe-exchange-api
- collection_type: open
  name: Stripe Accounts Account Exchange Rates API
  slug: open-stripe-exchange-rates-api
- collection_type: open
  name: Stripe Accounts Account Expire API
  slug: open-stripe-expire-api
- collection_type: open
  name: Stripe Accounts Account External API
  slug: open-stripe-external-api
- collection_type: open
  name: Stripe Accounts Account Fee API
  slug: open-stripe-fee-api
- collection_type: open
  name: Stripe Accounts Account Files API
  slug: open-stripe-files-api
- collection_type: open
  name: Stripe Accounts Account Finalize API
  slug: open-stripe-finalize-api
- collection_type: open
  name: Stripe Accounts Account Financial API
  slug: open-stripe-financial-api
- collection_type: open
  name: Stripe Accounts Account Financial Connections API
  slug: open-stripe-financial-connections-api
- collection_type: open
  name: Stripe Accounts Account Find API
  slug: open-stripe-find-api
- collection_type: open
  name: Stripe Accounts Account Forwarding API
  slug: open-stripe-forwarding-api
- collection_type: open
  name: Stripe Accounts Account Funding API
  slug: open-stripe-funding-api
- collection_type: open
  name: Stripe Accounts Account Get API
  slug: open-stripe-get-api
- collection_type: open
  name: Stripe Accounts Account History API
  slug: open-stripe-history-api
- collection_type: open
  name: Stripe Accounts Account Identifiers API
  slug: open-stripe-identifiers-api
- collection_type: open
  name: Stripe Accounts Account Identity API
  slug: open-stripe-identity-api
- collection_type: open
  name: Stripe Accounts Account Increment API
  slug: open-stripe-increment-api
- collection_type: open
  name: Stripe Accounts Account Intents API
  slug: open-stripe-intents-api
- collection_type: open
  name: Stripe Accounts Account Invoice API
  slug: open-stripe-invoice-api
- collection_type: open
  name: Stripe Accounts Account Invoiceitems API
  slug: open-stripe-invoiceitems-api
- collection_type: open
  name: Stripe Accounts Account Invoices API
  slug: open-stripe-invoices-api
- collection_type: open
  name: Stripe Accounts Account Issuing API
  slug: open-stripe-issuing-api
- collection_type: open
  name: Stripe Accounts Account Item API
  slug: open-stripe-item-api
- collection_type: open
  name: Stripe Accounts Account Items API
  slug: open-stripe-items-api
- collection_type: open
  name: Stripe Accounts Account Keys API
  slug: open-stripe-keys-api
- collection_type: open
  name: Stripe Accounts Account Line API
  slug: open-stripe-line-api
- collection_type: open
  name: Stripe Accounts Account Lines API
  slug: open-stripe-lines-api
- collection_type: open
  name: Stripe Accounts Account Link Account Sessions API
  slug: open-stripe-link-account-sessions-api
- collection_type: open
  name: Stripe Accounts Account Link API
  slug: open-stripe-link-api
- collection_type: open
  name: Stripe Accounts Account Linked Accounts API
  slug: open-stripe-linked-accounts-api
- collection_type: open
  name: Stripe Accounts Account Linked API
  slug: open-stripe-linked-api
- collection_type: open
  name: Stripe Accounts Account Links API
  slug: open-stripe-links-api
- collection_type: open
  name: Stripe Accounts Account Lists API
  slug: open-stripe-lists-api
- collection_type: open
  name: Stripe Accounts Account Login API
  slug: open-stripe-login-api
- collection_type: open
  name: Stripe Accounts Account Mark API
  slug: open-stripe-mark-api
- collection_type: open
  name: Stripe Accounts Account Method API
  slug: open-stripe-method-api
- collection_type: open
  name: Stripe Accounts Account Methods API
  slug: open-stripe-methods-api
- collection_type: open
  name: Stripe Accounts Account Microdeposits API
  slug: open-stripe-microdeposits-api
- collection_type: open
  name: Stripe Accounts Account Note API
  slug: open-stripe-note-api
- collection_type: open
  name: Stripe Accounts Account Notes API
  slug: open-stripe-notes-api
- collection_type: open
  name: Stripe Accounts Account Owners API
  slug: open-stripe-owners-api
- collection_type: open
  name: Stripe Accounts Account Pay API
  slug: open-stripe-pay-api
- collection_type: open
  name: Stripe Accounts Account Payment Intents API
  slug: open-stripe-payment-intents-api
- collection_type: open
  name: Stripe Accounts Account Payment Links API
  slug: open-stripe-payment-links-api
- collection_type: open
  name: Stripe Payment Method API
  slug: open-stripe-payment-method-api
- collection_type: open
  name: Stripe Accounts Account Payment Method Configurations API
  slug: open-stripe-payment-method-configurations-api
- collection_type: open
  name: Stripe Accounts Account Payment Method Domains API
  slug: open-stripe-payment-method-domains-api
- collection_type: open
  name: Stripe Accounts Account Payment Methods API
  slug: open-stripe-payment-methods-api
- collection_type: open
  name: Stripe Accounts Account Payments API
  slug: open-stripe-payments-api
- collection_type: open
  name: Stripe Accounts Account Payouts API
  slug: open-stripe-payouts-api
- collection_type: open
  name: Stripe Accounts Account Person API
  slug: open-stripe-person-api
- collection_type: open
  name: Stripe Accounts Account Persons API
  slug: open-stripe-persons-api
- collection_type: open
  name: Stripe Accounts Account Plans API
  slug: open-stripe-plans-api
- collection_type: open
  name: Stripe Accounts Account Post API
  slug: open-stripe-post-api
- collection_type: open
  name: Stripe Accounts Account Prices API
  slug: open-stripe-prices-api
- collection_type: open
  name: Stripe Accounts Account Products API
  slug: open-stripe-products-api
- collection_type: open
  name: Stripe Accounts Account Promotion Codes API
  slug: open-stripe-promotion-codes-api
- collection_type: open
  name: Stripe Accounts Account Quotes API
  slug: open-stripe-quotes-api
- collection_type: open
  name: Stripe Accounts Account Radar API
  slug: open-stripe-radar-api
- collection_type: open
  name: Stripe Accounts Account Rate API
  slug: open-stripe-rate-api
- collection_type: open
  name: Stripe Accounts Account Rates API
  slug: open-stripe-rates-api
- collection_type: open
  name: Stripe Accounts Account Redact API
  slug: open-stripe-redact-api
- collection_type: open
  name: Stripe Accounts Account Refresh API
  slug: open-stripe-refresh-api
- collection_type: open
  name: Stripe Accounts Account Refund API
  slug: open-stripe-refund-api
- collection_type: open
  name: Stripe Accounts Account Refunds API
  slug: open-stripe-refunds-api
- collection_type: open
  name: Stripe Accounts Account Reject API
  slug: open-stripe-reject-api
- collection_type: open
  name: Stripe Accounts Account Reporting API
  slug: open-stripe-reporting-api
- collection_type: open
  name: Stripe Accounts Account Reports API
  slug: open-stripe-reports-api
- collection_type: open
  name: Stripe Accounts Account Retrieve API
  slug: open-stripe-retrieve-api
- collection_type: open
  name: Stripe Accounts Account Revenue Recognition API
  slug: open-stripe-revenue-recognition-api
- collection_type: open
  name: Stripe Accounts Account Reverse API
  slug: open-stripe-reverse-api
- collection_type: open
  name: Stripe Accounts Account Search API
  slug: open-stripe-search-api
- collection_type: open
  name: Stripe Accounts Account Secrets API
  slug: open-stripe-secrets-api
- collection_type: open
  name: Stripe Accounts Account Send API
  slug: open-stripe-send-api
- collection_type: open
  name: Stripe Accounts Account Sessions API
  slug: open-stripe-sessions-api
- collection_type: open
  name: Stripe Accounts Account Settlement API
  slug: open-stripe-settlement-api
- collection_type: open
  name: Stripe Accounts Account Settlements API
  slug: open-stripe-settlements-api
- collection_type: open
  name: Stripe Setup API
  slug: open-stripe-setup-api
- collection_type: open
  name: Stripe Accounts Account Setup Attempts API
  slug: open-stripe-setup-attempts-api
- collection_type: open
  name: Stripe Accounts Account Setup Intents API
  slug: open-stripe-setup-intents-api
- collection_type: open
  name: Stripe Accounts Account Shipping Rates API
  slug: open-stripe-shipping-rates-api
- collection_type: open
  name: Stripe Accounts Account Sigma API
  slug: open-stripe-sigma-api
- collection_type: open
  name: Stripe Accounts Account Sources API
  slug: open-stripe-sources-api
- collection_type: open
  name: Stripe Accounts Account Subscribe API
  slug: open-stripe-subscribe-api
- collection_type: open
  name: Stripe Subscription API
  slug: open-stripe-subscription-api
- collection_type: open
  name: Stripe Accounts Account Subscription Items API
  slug: open-stripe-subscription-items-api
- collection_type: open
  name: Stripe Accounts Account Subscription Schedules API
  slug: open-stripe-subscription-schedules-api
- collection_type: open
  name: Stripe Accounts Account Subscriptions API
  slug: open-stripe-subscriptions-api
- collection_type: open
  name: Stripe Accounts Account Tax API
  slug: open-stripe-tax-api
- collection_type: open
  name: Stripe Accounts Account Tax Codes API
  slug: open-stripe-tax-codes-api
- collection_type: open
  name: Stripe Accounts Account Tax Rates API
  slug: open-stripe-tax-rates-api
- collection_type: open
  name: Stripe Accounts Account Terminal API
  slug: open-stripe-terminal-api
- collection_type: open
  name: Stripe Accounts Account Test Helpers API
  slug: open-stripe-test-helpers-api
- collection_type: open
  name: Stripe Accounts Account Tokens API
  slug: open-stripe-tokens-api
- collection_type: open
  name: Stripe Accounts Account Topups API
  slug: open-stripe-topups-api
- collection_type: open
  name: Stripe Accounts Account Transaction API
  slug: open-stripe-transaction-api
- collection_type: open
  name: Stripe Accounts Account Transactions API
  slug: open-stripe-transactions-api
- collection_type: open
  name: Stripe Accounts Account Transfers API
  slug: open-stripe-transfers-api
- collection_type: open
  name: Stripe Accounts Account Treasury API
  slug: open-stripe-treasury-api
- collection_type: open
  name: Stripe Accounts Account Unsubscribe API
  slug: open-stripe-unsubscribe-api
- collection_type: open
  name: Stripe Accounts Account Upcoming API
  slug: open-stripe-upcoming-api
- collection_type: open
  name: Stripe Accounts Account Update API
  slug: open-stripe-update-api
- collection_type: open
  name: Stripe Accounts Account Validate API
  slug: open-stripe-validate-api
- collection_type: open
  name: Stripe Accounts Account Verification API
  slug: open-stripe-verification-api
- collection_type: open
  name: Stripe Accounts Account Verify API
  slug: open-stripe-verify-api
- collection_type: open
  name: Stripe Accounts Account Void API
  slug: open-stripe-void-api
- collection_type: open
  name: Stripe Webhook API
  slug: open-stripe-webhook-api
- collection_type: open
  name: Stripe Accounts Account Webhook Endpoints API
  slug: open-stripe-webhook-endpoints-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/stripe-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stripe-calculate-and-settle-tax.md
- group: operate
  title: ''
  type: Roadmap
  url: https://stripe.com/roadmap
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
  type: CodeExamples
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
  type: DeprecationPolicy
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
  type: AgentSkills
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
- description: 'Stripe operates an official remote MCP server at https://mcp.stripe.com, authenticated with OAuth (RFC 9728 protected resource; authorization server https://access.stripe.com/mcp) or a restricted API '
  name: Stripe MCP Server manifest
  slug: stripe-mcp-server-manifest
modified: '2026-07-17'
name: Stripe
nav: Providers
network: true
overview: 'Stripe publishes 159 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balance API, Billing API, and 156 more. Tagged areas include Commerce, Financial-Services, Fintech, Payments, and T1.


  The Stripe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Stripe''s developer surface includes authentication, sandbox, changelog, CLI, signup flow, developer portal, documentation, and 122 more developer resources.'
plans:
- name: Stripe Plans Pricing
  plan_count: 9
  slug: stripe-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Stripe Rate Limits
  slug: stripe-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Stripe API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: stripe-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Stripe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stripe-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Stripe API Rules
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
  composite: 80.4
  coverage:
    artifact_dirs: 41
    catalog_gap: 69.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 33.3
    contract_quality: 73.2
    developer_ergonomics: 94.6
    discoverability: 48.1
    governance: 33.3
    operational_transparency: 76.3
  previous_composite: 80.4
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
    jurisdictions:
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 93.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stripe/refs/heads/main/screenshots/stripe-2026-08-17T125440.png
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
- Financial-Services
- Fintech
- Payments
- T1
website: https://stripe.com
---
