---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 483
  human_in_the_loop: 2
  name: Stripe Agentic Access
  operation_count: 910
  slug: stripe-agentic-access
  summary_line: 910 operations · 483 acting · 2 human-in-the-loop
api_count: 47
apis:
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts
  name: Stripe Accounts API
  phrasing_intents:
  - id: GetAccounts
    intent: List connected accounts
    question: How do I see all the accounts connected to my platform?
  - id: GetAccountsAccountExternalAccounts
    intent: List a connected account's payout accounts
    question: How do I see the bank accounts and cards a connected account gets paid out to?
  phrasing_ops: 2
  slug: stripe-accounts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transac
  name: Stripe Balance API
  phrasing_intents:
  - id: GetBalance
    intent: Check my account balance
    question: How much money is currently in my Stripe balance?
  - id: GetBalanceHistory
    intent: List balance transactions
    question: How do I see every transaction that changed my balance?
  - id: GetBalanceHistoryId
    intent: Retrieve a balance transaction
    question: How do I see the fee and net amount for one balance transaction?
  phrasing_ops: 3
  slug: stripe-balance-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe '
  name: Stripe Charges API
  phrasing_intents:
  - id: GetCharges
    intent: List charges
    question: How do I see all the charges I've made, newest first?
  - id: PostCharges
    intent: Charge a card or payment source
    question: How do I charge a customer's saved card directly?
  - id: GetChargesSearch
    intent: Search charges
    question: How do I find charges matching an amount, status or metadata value?
  - id: GetChargesCharge
    intent: Get a charge
    question: How do I look up the details of one charge?
  - id: PostChargesCharge
    intent: Update a charge
    question: How do I change the description or receipt email on a charge?
  - id: PostChargesChargeCapture
    intent: Capture an authorized charge
    question: How do I capture a charge I only authorized earlier?
  - id: GetChargesChargeDispute
    intent: Get the dispute on a charge
    question: How do I see whether a customer disputed a specific charge?
  - id: PostChargesChargeDispute
    intent: Submit evidence for a charge's dispute
    question: How do I respond to a chargeback on a specific charge?
  phrasing_ops: 14
  slug: stripe-charges-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment pa
  name: Stripe Checkout API
  phrasing_intents:
  - id: GetCheckoutSessions
    intent: List Checkout Sessions
    question: How do I list the checkout sessions my customers have started?
  - id: PostCheckoutSessions
    intent: Create a Checkout Session
    question: How do I send a customer to a hosted payment page?
  - id: GetCheckoutSessionsSession
    intent: Retrieve a Checkout Session
    question: How do I check whether a customer finished paying on the checkout page?
  - id: PostCheckoutSessionsSessionExpire
    intent: Expire an open Checkout Session
    question: How do I stop a customer from completing an open checkout?
  - id: GetCheckoutSessionsSessionLineItems
    intent: List a Checkout Session's line items
    question: How do I see exactly what a customer bought in a checkout session?
  phrasing_ops: 5
  slug: stripe-checkout-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.
  name: Stripe Climate API
  phrasing_intents:
  - id: GetClimateOrders
    intent: List carbon removal orders
    question: How do I see all the carbon removal I've ordered?
  - id: PostClimateOrders
    intent: Buy carbon removal
    question: How do I buy carbon removal for my business?
  - id: GetClimateOrdersOrder
    intent: Get a carbon removal order
    question: How do I check the status of a carbon removal order?
  - id: PostClimateOrdersOrder
    intent: Update a carbon removal order
    question: How do I change who gets credit for a carbon removal order?
  - id: PostClimateOrdersOrderCancel
    intent: Cancel a carbon removal order
    question: How do I cancel a carbon removal order?
  - id: GetClimateProducts
    intent: List carbon removal products
    question: What carbon removal products can I buy?
  - id: GetClimateProductsProduct
    intent: Get a carbon removal product
    question: How do I see the price and availability of one carbon removal product?
  - id: GetClimateReservations
    intent: List carbon removal reservations
    question: How do I see the carbon removal I've reserved but may not have confirmed?
  phrasing_ops: 15
  slug: stripe-climate-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. '
  name: Stripe Coupons API
  phrasing_intents:
  - id: GetCoupons
    intent: List coupons
    question: What coupons have I created?
  - id: PostCoupons
    intent: Create a coupon
    question: How do I create a percentage-off discount?
  - id: DeleteCouponsCoupon
    intent: Delete a coupon
    question: How do I stop a coupon from being used by new customers?
  - id: GetCouponsCoupon
    intent: Get a coupon
    question: How do I check the terms of a coupon?
  - id: PostCouponsCoupon
    intent: Rename or tag a coupon
    question: How do I rename a coupon?
  phrasing_ops: 5
  slug: stripe-coupons-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Issue a credit note to adjust an invoice's amount after the invoice is finalized.
  name: Stripe Credit Notes API
  phrasing_intents:
  - id: GetCreditNotes
    intent: List credit notes
    question: How do I see all the credit notes I've issued against invoices?
  - id: PostCreditNotes
    intent: Issue a credit note on an invoice
    question: How do I reduce what a customer owes on a finalized invoice?
  - id: GetCreditNotesPreview
    intent: Preview a credit note before issuing it
    question: Can I see what a credit note would look like before I actually issue it?
  - id: GetCreditNotesPreviewLines
    intent: List line items of a credit note preview
    question: How do I page through every line item in a previewed credit note?
  - id: GetCreditNotesCreditNoteLines
    intent: List line items on a credit note
    question: How do I get every line item on a credit note I already issued?
  - id: GetCreditNotesId
    intent: Look up a credit note
    question: How do I view the details of one credit note?
  - id: PostCreditNotesId
    intent: Update a credit note's memo
    question: Can I change the memo on a credit note after it's issued?
  - id: PostCreditNotesIdVoid
    intent: Void a credit note
    question: How do I cancel a credit note I issued by mistake?
  phrasing_ops: 8
  slug: stripe-credit-notes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.
  name: Stripe Customers API
  phrasing_intents:
  - id: GetCustomers
    intent: List customers
    question: How do I pull a list of all my customers, newest first?
  - id: PostCustomers
    intent: Create a customer
    question: How do I add a new customer record in Stripe?
  - id: GetCustomersSearch
    intent: Search customers with a query
    question: How do I search my customers by name, email or metadata?
  - id: DeleteCustomersCustomer
    intent: Permanently delete a customer
    question: How do I permanently remove a customer?
  - id: GetCustomersCustomer
    intent: Retrieve a customer
    question: How do I fetch the full details of one customer?
  - id: PostCustomersCustomer
    intent: Update a customer's details
    question: How do I change a customer's email or address?
  - id: GetCustomersCustomerBalanceTransactions
    intent: List a customer's credit balance changes
    question: How do I see every change made to a customer's credit balance?
  - id: PostCustomersCustomerBalanceTransactions
    intent: Adjust a customer's credit balance
    question: How do I give a customer account credit?
  phrasing_ops: 47
  slug: stripe-customers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitim
  name: Stripe Disputes API
  phrasing_intents:
  - id: GetDisputes
    intent: List disputes
    question: How do I see all chargebacks against my account?
  - id: GetDisputesDispute
    intent: Get a dispute
    question: How do I check the status and deadline of a dispute?
  - id: PostDisputesDispute
    intent: Add or submit dispute evidence
    question: How do I fight a chargeback with evidence?
  - id: PostDisputesDisputeClose
    intent: Accept a dispute
    question: How do I concede a dispute I have no evidence for?
  phrasing_ops: 4
  slug: stripe-disputes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side
  name: Stripe Ephemeral Keys API
  phrasing_intents:
  - id: PostEphemeralKeys
    intent: Create a short-lived client key
    question: How do I give a mobile app temporary access to a customer's saved payment details?
  - id: DeleteEphemeralKeysKey
    intent: Revoke a short-lived client key
    question: How do I invalidate an ephemeral key before it expires?
  phrasing_ops: 2
  slug: stripe-ephemeral-keys-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.
  name: Stripe Events API
  phrasing_intents:
  - id: GetEvents
    intent: List account events
    question: How do I see what happened on my account recently?
  - id: GetEventsId
    intent: Get an event
    question: How do I fetch the full event behind a webhook I received?
  phrasing_ops: 2
  slug: stripe-events-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer''s native currency. Doing so can improve sales and help customers avoid conversion costs. In order to '
  name: Stripe Exchange Rates API
  phrasing_intents:
  - id: GetExchangeRates
    intent: List currency exchange rates
    question: What exchange rates are used to convert between supported currencies?
  - id: GetExchangeRatesRateId
    intent: Get conversion rates from one currency
    question: What is the current conversion rate from one currency to the others?
  phrasing_ops: 2
  slug: stripe-exchange-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'This object represents files hosted on Stripe''s servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for '
  name: Stripe Files API
  phrasing_intents:
  - id: GetFiles
    intent: List uploaded files
    question: What files have been uploaded to my account?
  - id: PostFiles
    intent: Upload a file
    question: How do I upload a document like dispute evidence or an ID?
  - id: GetFilesFile
    intent: Get an uploaded file
    question: How do I look up a file I uploaded earlier?
  phrasing_ops: 3
  slug: stripe-files-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such '
  name: Stripe Financial Connections API
  phrasing_intents:
  - id: GetFinancialConnectionsAccounts
    intent: List linked bank accounts
    question: How do I see all the bank accounts my customers have linked?
  - id: GetFinancialConnectionsAccountsAccount
    intent: Look up a linked bank account
    question: How do I see the details of one bank account a customer linked?
  - id: PostFinancialConnectionsAccountsAccountDisconnect
    intent: Disconnect a linked bank account
    question: How do I stop accessing a customer's linked bank account?
  - id: GetFinancialConnectionsAccountsAccountOwners
    intent: List owners of a linked bank account
    question: How do I find out who owns a bank account a customer linked?
  - id: PostFinancialConnectionsAccountsAccountRefresh
    intent: Refresh data on a linked bank account
    question: How do I pull the latest balance for a customer's linked bank account?
  - id: PostFinancialConnectionsAccountsAccountSubscribe
    intent: Subscribe to ongoing account data refreshes
    question: How do I keep a linked bank account's transactions updated automatically?
  - id: PostFinancialConnectionsAccountsAccountUnsubscribe
    intent: Stop ongoing account data refreshes
    question: How do I stop automatic transaction refreshes on a linked bank account?
  - id: PostFinancialConnectionsSessions
    intent: Start a bank account linking session
    question: How do I let a customer securely link their bank account?
  phrasing_ops: 11
  slug: stripe-financial-connections-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.
  name: Stripe Identity API
  phrasing_intents:
  - id: GetIdentityVerificationReports
    intent: List identity verification reports
    question: How do I see the results of all identity checks I've run?
  - id: GetIdentityVerificationReportsReport
    intent: Retrieve an identity verification report
    question: How do I read the outcome of one identity verification?
  - id: GetIdentityVerificationSessions
    intent: List identity verification sessions
    question: How do I list all the identity verification sessions I've started?
  - id: PostIdentityVerificationSessions
    intent: Start an identity verification
    question: How do I verify a user's identity with a photo ID?
  - id: GetIdentityVerificationSessionsSession
    intent: Retrieve an identity verification session
    question: How do I check where a user is in the identity verification process?
  - id: PostIdentityVerificationSessionsSession
    intent: Update an identity verification session
    question: How do I change the type of check on a verification that needs more input?
  - id: PostIdentityVerificationSessionsSessionCancel
    intent: Cancel an identity verification
    question: How do I stop a user from completing an identity verification?
  - id: PostIdentityVerificationSessionsSessionRedact
    intent: Redact an identity verification's data
    question: How do I delete the personal data collected during an identity check?
  phrasing_ops: 8
  slug: stripe-identity-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.
  name: Stripe Invoice API
  phrasing_intents:
  - id: postInvoiceItems
    intent: Add a charge to a customer's invoice
    question: How do I add a one-off charge to a customer's next invoice?
  - id: postInvoiceItemsInvoiceitem
    intent: Update an invoice item
    question: How do I change the amount of a pending invoice item?
  phrasing_ops: 2
  slug: stripe-invoice-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: An API for businesses to instantly create, manage, and distribute payment cards.
  name: Stripe Issuing API
  phrasing_intents:
  - id: GetIssuingAuthorizations
    intent: List card authorization requests
    question: How do I see every authorization attempt made on the cards I've issued?
  - id: GetIssuingAuthorizationsAuthorization
    intent: Look up one card authorization
    question: How do I pull up the details of a single authorization on an issued card?
  - id: PostIssuingAuthorizationsAuthorization
    intent: Tag a card authorization with metadata
    question: Can I attach my own reference data to an issued-card authorization?
  - id: PostIssuingAuthorizationsAuthorizationApprove
    intent: Approve a pending card authorization
    question: How do I approve a pending purchase on one of my issued cards in real time?
  - id: PostIssuingAuthorizationsAuthorizationDecline
    intent: Decline a pending card authorization
    question: How do I decline a purchase attempt on an issued card before it goes through?
  - id: GetIssuingCardholders
    intent: List cardholders
    question: How do I see all the people and companies I've set up to receive issued cards?
  - id: PostIssuingCardholders
    intent: Create a cardholder
    question: How do I register a person or company so I can issue them a card?
  - id: GetIssuingCardholdersCardholder
    intent: Look up a cardholder
    question: How do I view the profile and billing details of one cardholder?
  phrasing_ops: 27
  slug: stripe-issuing-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You
  name: Stripe Payment Intents API
  phrasing_intents:
  - id: GetPaymentIntents
    intent: List payments in progress and completed
    question: How do I list recent PaymentIntents on my account?
  - id: PostPaymentIntents
    intent: Start a payment for an amount
    question: How do I start collecting a payment from a customer in Stripe?
  - id: GetPaymentIntentsSearch
    intent: Search payments with a query
    question: How do I search for payments by status, amount or metadata?
  - id: GetPaymentIntentsIntent
    intent: Get a PaymentIntent
    question: How do I check the status of one payment?
  - id: PostPaymentIntentsIntent
    intent: Change a payment before it is confirmed
    question: How do I change the amount of a payment before the customer pays?
  - id: PostPaymentIntentsIntentApplyCustomerBalance
    intent: Pay a PaymentIntent from the customer's cash balance
    question: How do I use money in a customer's cash balance to settle a payment?
  - id: PostPaymentIntentsIntentCancel
    intent: Cancel a payment
    question: How do I cancel a payment the customer hasn't finished?
  - id: PostPaymentIntentsIntentCapture
    intent: Capture an authorized payment
    question: How do I collect the money from a payment I only authorized?
  phrasing_ops: 11
  slug: stripe-payment-intents-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new '
  name: Stripe Payment Links API
  phrasing_intents:
  - id: GetPaymentLinks
    intent: List payment links
    question: How do I see all the payment links I've created?
  - id: PostPaymentLinks
    intent: Create a payment link
    question: How do I create a shareable link customers can use to pay me?
  - id: GetPaymentLinksPaymentLink
    intent: Retrieve a payment link
    question: How do I look up the settings of one payment link?
  - id: PostPaymentLinksPaymentLink
    intent: Update or deactivate a payment link
    question: How do I turn off a payment link so nobody can use it?
  - id: GetPaymentLinksPaymentLinkLineItems
    intent: List a payment link's line items
    question: How do I see which products a payment link sells?
  phrasing_ops: 5
  slug: stripe-payment-links-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, '
  name: Stripe Payouts API
  phrasing_intents:
  - id: GetPayouts
    intent: List payouts
    question: How do I see all the payouts sent to my bank account?
  - id: PostPayouts
    intent: Pay out funds to a bank account
    question: How do I send money from my balance to my bank account?
  - id: GetPayoutsPayout
    intent: Retrieve a payout
    question: How do I check the status of a specific payout?
  - id: PostPayoutsPayout
    intent: Update a payout's metadata
    question: Can I add my own reference data to a payout that already exists?
  - id: PostPayoutsPayoutCancel
    intent: Cancel a pending payout
    question: How do I stop a payout that hasn't been paid out yet?
  - id: PostPayoutsPayoutReverse
    intent: Reverse a completed payout
    question: How do I pull back a payout that already reached a bank account?
  phrasing_ops: 6
  slug: stripe-payouts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.
  name: Stripe Plans API
  phrasing_intents:
  - id: GetPlans
    intent: List subscription plans
    question: How do I see all the subscription plans I've set up?
  - id: PostPlans
    intent: Create a subscription plan
    question: How do I create a monthly or yearly plan to bill subscribers?
  - id: DeletePlansPlan
    intent: Delete a subscription plan
    question: How do I stop new customers from signing up to an old plan?
  - id: GetPlansPlan
    intent: Look up a subscription plan
    question: How do I check the price and billing interval of one plan?
  - id: PostPlansPlan
    intent: Update a subscription plan
    question: Can I change a plan's price or billing cycle after creating it?
  phrasing_ops: 5
  slug: stripe-plans-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: 'Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track '
  name: Stripe Prices API
  phrasing_intents:
  - id: GetPrices
    intent: List prices
    question: How do I see all the prices I've set up for my products?
  - id: PostPrices
    intent: Create a price for a product
    question: How do I add a monthly subscription price to a product?
  - id: GetPricesSearch
    intent: Search prices with a query
    question: How do I search my prices by metadata or amount?
  - id: GetPricesPrice
    intent: Get a price
    question: How do I look up one price's amount and billing interval?
  - id: PostPricesPrice
    intent: Update or archive a price
    question: How do I stop a price from being used for new purchases?
  phrasing_ops: 5
  slug: stripe-prices-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Pro
  name: Stripe Products API
  phrasing_intents:
  - id: GetProducts
    intent: List products
    question: How do I see everything in my product catalog?
  - id: PostProducts
    intent: Create a product
    question: How do I add a new product to my catalog?
  - id: GetProductsSearch
    intent: Search products
    question: How do I find products by name or metadata?
  - id: DeleteProductsId
    intent: Delete a product
    question: How do I delete a product from my catalog?
  - id: GetProductsId
    intent: Get a product
    question: How do I look up the details of one product?
  - id: PostProductsId
    intent: Update a product
    question: How do I rename a product or change its description?
  phrasing_ops: 6
  slug: stripe-products-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.
  name: Stripe Promotion Codes API
  phrasing_intents:
  - id: GetPromotionCodes
    intent: List promotion codes
    question: What promotion codes do I have running?
  - id: PostPromotionCodes
    intent: Create a promotion code
    question: How do I create a code customers can type at checkout?
  - id: GetPromotionCodesPromotionCode
    intent: Get a promotion code
    question: How do I see a promotion code's restrictions and redemptions?
  - id: PostPromotionCodesPromotionCode
    intent: Update a promotion code
    question: How do I deactivate a promotion code?
  phrasing_ops: 4
  slug: stripe-promotion-codes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.
  name: Stripe Quotes API
  phrasing_intents:
  - id: GetQuotes
    intent: List quotes
    question: How do I see all the quotes I've created?
  - id: PostQuotes
    intent: Create a quote
    question: How do I create a price quote for a customer?
  - id: GetQuotesQuote
    intent: Retrieve a quote
    question: How do I look up a single quote?
  - id: PostQuotesQuote
    intent: Edit a quote
    question: How do I change the line items on a draft quote?
  - id: PostQuotesQuoteAccept
    intent: Accept a quote
    question: How do I record that a customer accepted a quote?
  - id: PostQuotesQuoteCancel
    intent: Cancel a quote
    question: How do I cancel a quote the customer won't be accepting?
  - id: GetQuotesQuoteComputedUpfrontLineItems
    intent: List a quote's upfront line items
    question: How do I see what a customer pays upfront when accepting a quote?
  - id: PostQuotesQuoteFinalize
    intent: Finalize a quote
    question: How do I finalize a quote so I can send it to the customer?
  phrasing_ops: 10
  slug: stripe-quotes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.
  name: Stripe Radar API
  phrasing_intents:
  - id: GetRadarEarlyFraudWarnings
    intent: List early fraud warnings
    question: How do I see which payments card issuers have flagged as likely fraud?
  - id: GetRadarEarlyFraudWarningsEarlyFraudWarning
    intent: Look up an early fraud warning
    question: How do I see the details of one early fraud warning?
  - id: GetRadarValueListItems
    intent: List entries in a fraud value list
    question: How do I see every email, card or IP on one of my block or allow lists?
  - id: PostRadarValueListItems
    intent: Add an entry to a fraud value list
    question: How do I block a suspicious email address or card fingerprint?
  - id: DeleteRadarValueListItemsItem
    intent: Remove an entry from a fraud value list
    question: How do I unblock a value that I added to a block list by mistake?
  - id: GetRadarValueListItemsItem
    intent: Look up a fraud value list entry
    question: How do I see the details of a single entry on a block or allow list?
  - id: GetRadarValueLists
    intent: List fraud value lists
    question: How do I see all the block and allow lists I've created for my fraud rules?
  - id: PostRadarValueLists
    intent: Create a fraud value list
    question: How do I create a list of blocked emails or IP addresses to use in fraud rules?
  phrasing_ops: 11
  slug: stripe-radar-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.
  name: Stripe Refunds API
  phrasing_intents:
  - id: GetRefunds
    intent: List refunds
    question: How do I see all the refunds I've issued?
  - id: PostRefunds
    intent: Refund a payment
    question: How do I refund a customer's payment?
  - id: GetRefundsRefund
    intent: Retrieve a refund
    question: How do I check the status of a refund?
  - id: PostRefundsRefund
    intent: Update a refund's metadata
    question: Can I add my own reference data to a refund I already issued?
  - id: PostRefundsRefundCancel
    intent: Cancel a pending refund
    question: How do I cancel a refund that's waiting on customer action?
  phrasing_ops: 5
  slug: stripe-refunds-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can sch
  name: Stripe Reporting API
  phrasing_intents:
  - id: GetReportingReportRuns
    intent: List report runs
    question: How do I see the financial reports I've run?
  - id: PostReportingReportRuns
    intent: Run a financial report
    question: How do I generate a balance or payout reconciliation report?
  - id: GetReportingReportRunsReportRun
    intent: Get a report run
    question: How do I check if my report has finished and get the file?
  - id: GetReportingReportTypes
    intent: List available report types
    question: What kinds of financial reports can I run?
  - id: GetReportingReportTypesReportType
    intent: Get a report type
    question: What date range of data does a report type cover?
  phrasing_ops: 5
  slug: stripe-reporting-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Reviews can be used to supplement automated fraud detection with human expertise.
  name: Stripe Reviews API
  phrasing_intents:
  - id: GetReviews
    intent: List payments awaiting fraud review
    question: How do I see the payments my fraud rules have held for manual review?
  - id: GetReviewsReview
    intent: Look up a fraud review
    question: How do I see why a particular payment was flagged for review?
  - id: PostReviewsReviewApprove
    intent: Approve a payment held for review
    question: How do I clear a payment that was held for fraud review?
  phrasing_ops: 3
  slug: stripe-reviews-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Shipping rates describe the price of shipping presented to your customers and applied to a purchase.
  name: Stripe Shipping Rates API
  phrasing_intents:
  - id: GetShippingRates
    intent: List shipping rates
    question: Which shipping options have I set up for checkout?
  - id: PostShippingRates
    intent: Create a shipping rate
    question: How do I add a flat-rate shipping option to checkout?
  - id: GetShippingRatesShippingRateToken
    intent: Get a shipping rate
    question: How do I look up the cost and name of one shipping rate?
  - id: PostShippingRatesShippingRateToken
    intent: Update or archive a shipping rate
    question: How do I retire a shipping option so it's no longer offered?
  phrasing_ops: 4
  slug: stripe-shipping-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve
  name: Stripe Sigma API
  phrasing_intents:
  - id: GetSigmaScheduledQueryRuns
    intent: List scheduled report query runs
    question: How do I see the results of my scheduled SQL reports?
  - id: GetSigmaScheduledQueryRunsScheduledQueryRun
    intent: Look up a scheduled query run
    question: How do I get the result file from one scheduled query run?
  phrasing_ops: 2
  slug: stripe-sigma-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can b
  name: Stripe Sources API
  phrasing_intents:
  - id: PostSources
    intent: Create a payment source
    question: How do I create a payment source for a customer to pay with?
  - id: GetSourcesSource
    intent: Retrieve a payment source
    question: How do I check the current status of a payment source?
  - id: PostSourcesSource
    intent: Update a payment source
    question: How do I change the owner details on a payment source?
  - id: GetSourcesSourceMandateNotificationsMandateNotification
    intent: Retrieve a source mandate notification
    question: How do I look up a mandate notification sent for a source?
  - id: GetSourcesSourceSourceTransactions
    intent: List transactions on a payment source
    question: How do I see the funds pushed to a source, like a credit transfer?
  - id: GetSourcesSourceSourceTransactionsSourceTransaction
    intent: Retrieve one source transaction
    question: How do I look up a single transaction on a payment source?
  - id: PostSourcesSourceVerify
    intent: Verify a payment source
    question: How do I verify a payment source that needs confirmation values?
  phrasing_ops: 7
  slug: stripe-sources-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.
  name: Stripe Tax API
  phrasing_intents:
  - id: PostTaxCalculations
    intent: Calculate tax for a sale
    question: How do I work out how much tax to charge on an order?
  - id: GetTaxCalculationsCalculationLineItems
    intent: List line items of a tax calculation
    question: How do I see the tax breakdown per line item in a calculation?
  - id: GetTaxRegistrations
    intent: List tax registrations
    question: Where am I registered to collect tax?
  - id: PostTaxRegistrations
    intent: Register to collect tax in a country
    question: How do I start collecting tax in a new country?
  - id: PostTaxRegistrationsId
    intent: Change or end a tax registration
    question: How do I stop collecting tax in a country I'm registered in?
  - id: GetTaxSettings
    intent: Get your tax settings
    question: What head office address and default tax behavior do I have set?
  - id: PostTaxSettings
    intent: Update your tax settings
    question: How do I set my head office address for tax calculations?
  - id: PostTaxTransactionsCreateFromCalculation
    intent: Record tax from a calculation
    question: How do I record the tax I actually collected on an order?
  phrasing_ops: 11
  slug: stripe-tax-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.
  name: Stripe Terminal API
  phrasing_intents:
  - id: GetTerminalConfigurations
    intent: List reader configurations
    question: How do I see all the configurations I've set up for my in-person card readers?
  - id: PostTerminalConfigurations
    intent: Create a reader configuration
    question: How do I set up tipping options for my in-store card readers?
  - id: DeleteTerminalConfigurationsConfiguration
    intent: Delete a reader configuration
    question: How do I remove a reader configuration I no longer use?
  - id: GetTerminalConfigurationsConfiguration
    intent: Look up a reader configuration
    question: How do I check the tipping and offline settings in one reader configuration?
  - id: PostTerminalConfigurationsConfiguration
    intent: Update a reader configuration
    question: How do I change the tipping percentages on an existing reader configuration?
  - id: PostTerminalConnectionTokens
    intent: Create a reader connection token
    question: How does my point-of-sale app get a token to connect to a card reader?
  - id: GetTerminalLocations
    intent: List store locations
    question: How do I see all the physical store locations where I run card readers?
  - id: PostTerminalLocations
    intent: Create a store location
    question: How do I add a new physical store where I'll use card readers?
  phrasing_ops: 21
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
  phrasing_intents:
  - id: PostTokens
    intent: Tokenize sensitive details
    question: How do I turn bank account details into a single-use token?
  - id: GetTokensToken
    intent: Get a token
    question: How do I check what a token represents?
  phrasing_ops: 2
  slug: stripe-tokens-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: A Transfer object is created when you move funds between Stripe accounts as part of Connect.
  name: Stripe Transfers API
  phrasing_intents:
  - id: GetTransfers
    intent: List transfers to connected accounts
    question: How do I see the money I've sent to connected accounts?
  - id: PostTransfers
    intent: Send funds to a connected account
    question: How do I pay out part of a sale to a seller's connected account?
  - id: GetTransfersIdReversals
    intent: List reversals of a transfer
    question: How do I see every reversal made against a transfer?
  - id: PostTransfersIdReversals
    intent: Reverse a transfer to a connected account
    question: How do I pull money back from a connected account after a transfer?
  - id: GetTransfersTransfer
    intent: Get a transfer
    question: How do I look up the details of one transfer?
  - id: PostTransfersTransfer
    intent: Update a transfer's description or metadata
    question: How do I add my own notes or metadata to an existing transfer?
  - id: GetTransfersTransferReversalsId
    intent: Get one reversal of a transfer
    question: How do I look up a specific reversal on a transfer?
  - id: PostTransfersTransferReversalsId
    intent: Update a transfer reversal's metadata
    question: How do I annotate a transfer reversal with metadata?
  phrasing_ops: 8
  slug: stripe-transfers-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage thei
  name: Stripe Treasury API
  phrasing_intents:
  - id: GetTreasuryCreditReversals
    intent: List credit reversals on a financial account
    question: How do I see which incoming credits I've sent back to the sender?
  - id: PostTreasuryCreditReversals
    intent: Reverse a received credit
    question: How do I send an incoming credit back to where it came from?
  - id: GetTreasuryCreditReversalsCreditReversal
    intent: Get a credit reversal
    question: How do I check the status of a single credit reversal?
  - id: GetTreasuryDebitReversals
    intent: List debit reversals on a financial account
    question: How do I see the pulled debits I've disputed or reversed?
  - id: PostTreasuryDebitReversals
    intent: Reverse a received debit
    question: How do I reverse a debit someone pulled from my treasury account?
  - id: GetTreasuryDebitReversalsDebitReversal
    intent: Get a debit reversal
    question: How do I look up one debit reversal and its outcome?
  - id: GetTreasuryFinancialAccounts
    intent: List treasury financial accounts
    question: How do I see all the treasury financial accounts on my platform?
  - id: PostTreasuryFinancialAccounts
    intent: Open a treasury financial account
    question: How do I open a financial account to hold money for a connected account?
  phrasing_ops: 32
  slug: stripe-treasury-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access according to yo
  name: Stripe Entitlements API
  phrasing_intents:
  - id: GetEntitlementsActiveEntitlements
    intent: List a customer's active entitlements
    question: Which features does a customer currently have access to?
  - id: GetEntitlementsActiveEntitlementsId
    intent: Get an active entitlement
    question: How do I look up a single active entitlement?
  - id: GetEntitlementsFeatures
    intent: List entitlement features
    question: Which features have I defined for gating access by plan?
  - id: PostEntitlementsFeatures
    intent: Create a feature customers can be entitled to
    question: How do I define a feature I want to gate behind a plan?
  - id: GetEntitlementsFeaturesId
    intent: Get a feature
    question: How do I look up one feature's name and lookup key?
  - id: PostEntitlementsFeaturesId
    intent: Update or archive a feature
    question: How do I rename a feature?
  phrasing_ops: 6
  slug: stripe-entitlements-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Vault and Forward API allows you to tokenize and store card details in Stripes PCI-compliant vault and forward that data to supported third-party processors or endpoints.
  name: Stripe Forwarding API
  phrasing_intents:
  - id: GetForwardingRequests
    intent: List forwarded card requests
    question: How do I see the requests where I've forwarded card details to another endpoint?
  - id: PostForwardingRequests
    intent: Forward saved card details to a destination URL
    question: How do I send a stored card's details to another endpoint without touching raw card data?
  - id: GetForwardingRequestsId
    intent: Get a forwarding request
    question: How do I see what came back from a forwarded card request?
  phrasing_ops: 3
  slug: stripe-forwarding-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application at checkout.
  name: Stripe Crypto Onramp API
  phrasing_intents:
  - id: PostCryptoOnrampSessions
    intent: Start a session for a customer to buy crypto
    question: How do I let a customer buy crypto with regular money in my app?
  - id: GetCryptoOnrampSessions
    intent: List crypto onramp sessions
    question: How do I see the crypto purchase sessions my customers have started?
  - id: GetCryptoOnrampSessionsOnrampSession
    intent: Get a crypto onramp session
    question: How do I check whether a customer finished buying crypto?
  phrasing_ops: 3
  slug: stripe-crypto-onramp-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Meters specify how to aggregate meter events over a billing period for usage-based pricing. Meter events represent customer actions and support up to 10,000 events per second via the V2 meter event st
  name: Stripe Billing Meters API
  phrasing_intents:
  - id: GetBillingMeters
    intent: List usage billing meters
    question: Which billing meters have I set up for usage-based pricing?
  - id: PostBillingMeters
    intent: Create a usage billing meter
    question: How do I start metering usage so I can bill customers for it?
  - id: GetBillingMetersId
    intent: Get a billing meter
    question: How do I see how a billing meter is configured?
  - id: PostBillingMetersId
    intent: Rename a billing meter
    question: How do I change the display name of a billing meter?
  - id: PostBillingMetersIdDeactivate
    intent: Deactivate a billing meter
    question: How do I stop a billing meter from being used?
  - id: PostBillingMetersIdReactivate
    intent: Reactivate a billing meter
    question: How do I bring a deactivated billing meter back?
  - id: GetBillingMetersIdEventSummaries
    intent: Summarize a customer's metered usage
    question: How much usage has a customer recorded on a meter this period?
  - id: PostBillingMeterEvents
    intent: Record a usage event
    question: How do I report customer usage so it can be billed?
  phrasing_ops: 8
  slug: stripe-billing-meters-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: Payment method configurations allow you to configure which payment methods are available to your customers during checkout. Manage payment method availability across multiple Connect accounts.
  name: Stripe Payment Method Configurations API
  phrasing_intents:
  - id: GetPaymentMethodConfigurations
    intent: List payment method configurations
    question: How do I see which sets of payment methods I've configured for checkout?
  - id: PostPaymentMethodConfigurations
    intent: Create a payment method configuration
    question: How do I choose which payment methods, like cards or bank debits, customers see at checkout?
  - id: GetPaymentMethodConfigurationsConfiguration
    intent: Look up a payment method configuration
    question: How do I check which payment methods are turned on in one configuration?
  - id: PostPaymentMethodConfigurationsConfiguration
    intent: Update a payment method configuration
    question: How do I turn a payment method on or off in an existing checkout configuration?
  phrasing_ops: 4
  slug: stripe-payment-method-configurations-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Account API from Stripe — 12 operation(s) for account.
  name: Stripe Account API
  phrasing_intents:
  - id: GetAccount
    intent: Get my own account details
    question: How do I check the details of my own Stripe account through the API?
  - id: PostAccountLinks
    intent: Create an onboarding link for a connected account
    question: How do I send a connected account user through hosted onboarding?
  - id: PostAccountSessions
    intent: Create a session for embedded account components
    question: How do I give my front end client-side access for a connected account?
  - id: PostAccounts
    intent: Create a connected account
    question: How do I create accounts for the sellers or users on my platform?
  - id: DeleteAccountsAccount
    intent: Delete a connected account
    question: How do I delete a connected account I manage?
  - id: GetAccountsAccount
    intent: Get a connected account
    question: How do I look up one of my connected accounts?
  - id: PostAccountsAccount
    intent: Update a connected account
    question: How do I change information on a connected account?
  - id: PostAccountsAccountBankAccounts
    intent: Add a bank account to a connected account
    question: How do I add a bank account for payouts to a connected account?
  phrasing_ops: 16
  slug: stripe-account-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Apple API from Stripe — 2 operation(s) for apple.
  name: Stripe Apple API
  phrasing_intents:
  - id: GetApplePayDomains
    intent: List registered Apple Pay domains
    question: How do I see which of my websites are registered for Apple Pay?
  - id: PostApplePayDomains
    intent: Register a domain for Apple Pay
    question: How do I enable Apple Pay on my website's domain?
  - id: DeleteApplePayDomainsDomain
    intent: Unregister an Apple Pay domain
    question: How do I stop accepting Apple Pay on a website I no longer run?
  - id: GetApplePayDomainsDomain
    intent: Retrieve an Apple Pay domain
    question: How do I look up one registered Apple Pay domain?
  phrasing_ops: 4
  slug: stripe-apple-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Applications API from Stripe — 8 operation(s) for applications.
  name: Stripe Applications API
  phrasing_intents:
  - id: GetApplicationFees
    intent: List collected application fees
    question: How much have I collected in platform application fees?
  - id: GetApplicationFeesFeeRefundsId
    intent: Get one refund of an application fee
    question: How do I look up a specific refund made on an application fee?
  - id: PostApplicationFeesFeeRefundsId
    intent: Update an application fee refund's metadata
    question: How do I tag an application fee refund with my own metadata?
  - id: GetApplicationFeesId
    intent: Get an application fee
    question: How do I look up the details of one application fee?
  - id: PostApplicationFeesIdRefund
    intent: Refund an application fee (legacy endpoint)
    question: Is there an older endpoint for refunding an application fee?
  - id: GetApplicationFeesIdRefunds
    intent: List refunds of an application fee
    question: How do I see every refund made against an application fee?
  - id: PostApplicationFeesIdRefunds
    intent: Refund an application fee
    question: How do I give back an application fee I collected from a connected account?
  - id: getAppsSecrets
    intent: List secrets in an app's secret store
    question: How do I see which secrets my app has stored?
  phrasing_ops: 11
  slug: stripe-applications-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Balance Transactions API from Stripe — 2 operation(s) for balance transactions.
  name: Stripe Balance Transactions API
  phrasing_intents:
  - id: GetBalanceTransactions
    intent: List balance transactions
    question: How do I see every movement in and out of my account balance?
  - id: GetBalanceTransactionsId
    intent: Get a balance transaction
    question: How do I see fees and net amount for one balance transaction?
  phrasing_ops: 2
  slug: stripe-balance-transactions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Billing Portal API from Stripe — 3 operation(s) for billing portal.
  name: Stripe Billing Portal API
  phrasing_intents:
  - id: GetBillingPortalConfigurations
    intent: List customer portal configurations
    question: How do I see the different setups I have for the self-service billing portal?
  - id: PostBillingPortalConfigurations
    intent: Create a customer portal configuration
    question: How do I set up a self-service portal where customers manage their own subscriptions and invoices?
  - id: GetBillingPortalConfigurationsConfiguration
    intent: Look up a customer portal configuration
    question: How do I check which features a particular portal configuration turns on?
  - id: PostBillingPortalConfigurationsConfiguration
    intent: Update a customer portal configuration
    question: How do I change what customers can do in an existing billing portal setup?
  - id: PostBillingPortalSessions
    intent: Open the billing portal for a customer
    question: How do I send a customer to a page where they can manage their subscription and billing?
  phrasing_ops: 5
  slug: stripe-billing-portal-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Capabilities API from Stripe — 1 operation(s) for capabilities.
  name: Stripe Capabilities API
  phrasing_intents:
  - id: GetAccountsAccountCapabilities
    intent: List a connected account's capabilities
    question: Which payment capabilities does a connected account have?
  phrasing_ops: 1
  slug: stripe-capabilities-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Capability API from Stripe — 1 operation(s) for capability.
  name: Stripe Capability API
  phrasing_intents:
  - id: GetAccountsAccountCapabilitiesCapability
    intent: Check one capability on a connected account
    question: How do I check whether a connected account can accept card payments yet?
  - id: PostAccountsAccountCapabilitiesCapability
    intent: Request or remove a connected account capability
    question: How do I turn on a new payment capability for a connected account?
  phrasing_ops: 2
  slug: stripe-capability-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Country Specs API from Stripe — 2 operation(s) for country specs.
  name: Stripe Country Specs API
  phrasing_intents:
  - id: GetCountrySpecs
    intent: List supported country requirements
    question: Which countries can connected accounts be based in?
  - id: GetCountrySpecsCountry
    intent: Look up requirements for one country
    question: What currencies and payment methods are supported for accounts in a given country?
  phrasing_ops: 2
  slug: stripe-country-specs-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Create API from Stripe — 10 operation(s) for create.
  name: Stripe Create API
  phrasing_intents:
  - id: PostAccountsAccountLoginLinks
    intent: Create a dashboard login link
    question: How do I let an Express connected account sign in to its dashboard?
  - id: PostAccountsAccountPeople
    intent: Add a person to a connected account
    question: How do I add an owner or representative to a connected account?
  - id: PostAccountsAccountPersons
    intent: Create a person on a connected account
    question: How do I create a person record for a connected account's director?
  phrasing_ops: 3
  slug: stripe-create-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Delete API from Stripe — 20 operation(s) for delete.
  name: Stripe Delete API
  phrasing_intents:
  - id: DeleteAccountsAccountPeoplePerson
    intent: Remove a person from a connected account
    question: How do I remove an owner or representative from a connected account?
  - id: DeleteAccountsAccountPersonsPerson
    intent: Remove a person via the persons path
    question: Is there a persons endpoint for removing someone from a connected account?
  - id: deleteInvoiceItemsInvoiceitem
    intent: Delete an invoice item
    question: How do I remove a pending charge from a customer's next invoice?
  phrasing_ops: 3
  slug: stripe-delete-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Get API from Stripe — 106 operation(s) for get.
  name: Stripe Get API
  phrasing_intents:
  - id: getInvoiceItems
    intent: List invoice items
    question: How do I see the one-off charges queued up for customers' invoices?
  - id: getInvoiceItemsInvoiceitem
    intent: Look up an invoice item
    question: How do I get the details of a single invoice item by its ID?
  phrasing_ops: 2
  slug: stripe-get-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Invoices API from Stripe — 12 operation(s) for invoices.
  name: Stripe Invoices API
  phrasing_intents:
  - id: GetInvoices
    intent: List invoices
    question: How do I list all the invoices I've issued?
  - id: PostInvoices
    intent: Create a draft invoice
    question: How do I create an invoice for a customer?
  - id: GetInvoicesSearch
    intent: Search invoices with a query
    question: How do I search invoices by amount, status or metadata?
  - id: GetInvoicesUpcoming
    intent: Preview a customer's upcoming invoice
    question: How do I preview what a customer will be billed on their next invoice?
  - id: GetInvoicesUpcomingLines
    intent: List line items on an upcoming invoice
    question: How do I page through every line item on a customer's next invoice?
  - id: DeleteInvoicesInvoice
    intent: Delete a draft invoice
    question: How do I throw away a draft invoice I don't need?
  - id: GetInvoicesInvoice
    intent: Retrieve an invoice
    question: How do I look up a single invoice?
  - id: PostInvoicesInvoice
    intent: Edit an invoice
    question: How do I change an invoice before it's finalized?
  phrasing_ops: 15
  slug: stripe-invoices-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Link Account Sessions API from Stripe — 2 operation(s) for link account sessions.
  name: Stripe Link Account Sessions API
  phrasing_intents:
  - id: PostLinkAccountSessions
    intent: Start a bank account linking session
    question: How do I let a customer connect their bank account?
  - id: GetLinkAccountSessionsSession
    intent: Get a bank account linking session
    question: How do I see which accounts a customer linked in a session?
  phrasing_ops: 2
  slug: stripe-link-account-sessions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Linked Accounts API from Stripe — 5 operation(s) for linked accounts.
  name: Stripe Linked Accounts API
  phrasing_intents:
  - id: GetLinkedAccounts
    intent: List linked financial accounts
    question: Which bank accounts have my customers linked through Financial Connections?
  - id: GetLinkedAccountsAccount
    intent: Get a linked financial account
    question: How do I look up the details of one linked bank account?
  - id: PostLinkedAccountsAccountDisconnect
    intent: Disconnect a linked financial account
    question: How do I give up my access to a customer's linked bank account?
  - id: GetLinkedAccountsAccountOwners
    intent: List owners of a linked financial account
    question: How do I see who owns a linked bank account?
  - id: PostLinkedAccountsAccountRefresh
    intent: Refresh data on a linked financial account
    question: How do I get fresh balance or ownership data for a linked account?
  phrasing_ops: 5
  slug: stripe-linked-accounts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Lists API from Stripe — 8 operation(s) for lists.
  name: Stripe Lists API
  phrasing_intents:
  - id: GetAccountsAccountPeople
    intent: List people on a connected account
    question: Who are the people tied to a connected account's business?
  - id: GetAccountsAccountPersons
    intent: List persons on a connected account's legal entity
    question: How do I list the persons attached to a connected account's legal entity?
  phrasing_ops: 2
  slug: stripe-lists-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Payment Method Domains API from Stripe — 3 operation(s) for payment method domains.
  name: Stripe Payment Method Domains API
  phrasing_intents:
  - id: GetPaymentMethodDomains
    intent: List payment method domains
    question: Which domains have I registered to show wallet payment methods?
  - id: PostPaymentMethodDomains
    intent: Register a domain for payment methods
    question: How do I register my checkout domain so wallet buttons show up?
  - id: GetPaymentMethodDomainsPaymentMethodDomain
    intent: Get a payment method domain
    question: How do I see which payment methods are available on a registered domain?
  - id: PostPaymentMethodDomainsPaymentMethodDomain
    intent: Enable or disable a payment method domain
    question: How do I stop showing payment methods on one of my domains?
  - id: PostPaymentMethodDomainsPaymentMethodDomainValidate
    intent: Re-verify a payment method domain
    question: How do I retry domain verification after fixing the setup?
  phrasing_ops: 5
  slug: stripe-payment-method-domains-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Payment Methods API from Stripe — 4 operation(s) for payment methods.
  name: Stripe Payment Methods API
  phrasing_intents:
  - id: GetPaymentMethods
    intent: List payment methods
    question: How do I list the payment methods on my account, like cards or bank accounts?
  - id: PostPaymentMethods
    intent: Create a payment method
    question: How do I create a card or bank account payment method from my server?
  - id: GetPaymentMethodsPaymentMethod
    intent: Look up a payment method
    question: How do I see the details of a single saved payment method, like its brand and expiry?
  - id: PostPaymentMethodsPaymentMethod
    intent: Update a payment method
    question: How do I update the billing address or card expiry on a saved payment method?
  - id: PostPaymentMethodsPaymentMethodAttach
    intent: Save a payment method to a customer
    question: How do I attach a card to a customer so I can charge it again later?
  - id: PostPaymentMethodsPaymentMethodDetach
    intent: Remove a payment method from a customer
    question: How do I remove a saved card from a customer?
  phrasing_ops: 6
  slug: stripe-payment-methods-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Person API from Stripe — 4 operation(s) for person.
  name: Stripe Person API
  phrasing_intents:
  - id: GetAccountsAccountPeoplePerson
    intent: Retrieve a person on a connected account
    question: How do I look up an owner or representative on a connected account?
  - id: PostAccountsAccountPeoplePerson
    intent: Update a person on a connected account
    question: How do I update a representative's details on a connected account?
  - id: GetAccountsAccountPersonsPerson
    intent: Look up a person via the persons path
    question: Is there another path to fetch a person on a connected account?
  - id: PostAccountsAccountPersonsPerson
    intent: Update a person via the persons path
    question: Can I update a person through the account's persons list instead?
  phrasing_ops: 4
  slug: stripe-person-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Setup Attempts API from Stripe — 1 operation(s) for setup attempts.
  name: Stripe Setup Attempts API
  phrasing_intents:
  - id: GetSetupAttempts
    intent: List attempts to save a payment method
    question: How do I see each try a customer made to save their payment method?
  phrasing_ops: 1
  slug: stripe-setup-attempts-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Setup Intents API from Stripe — 6 operation(s) for setup intents.
  name: Stripe Setup Intents API
  phrasing_intents:
  - id: GetSetupIntents
    intent: List SetupIntents
    question: How do I see all the attempts to save customers' payment details for later?
  - id: PostSetupIntents
    intent: Start saving a payment method for later
    question: How do I save a customer's card so I can charge them later without them present?
  - id: GetSetupIntentsIntent
    intent: Look up a SetupIntent
    question: How do I check whether a customer finished saving their payment method?
  - id: PostSetupIntentsIntent
    intent: Update a SetupIntent
    question: Can I change the customer or payment method on a SetupIntent before confirming it?
  - id: PostSetupIntentsIntentCancel
    intent: Cancel a SetupIntent
    question: How do I abandon saving a customer's payment method?
  - id: PostSetupIntentsIntentConfirm
    intent: Confirm saving a payment method
    question: What do I call when the customer clicks Save on my payment details page?
  - id: PostSetupIntentsIntentVerifyMicrodeposits
    intent: Verify bank account microdeposits
    question: How do I verify a customer's bank account using the small test deposits?
  phrasing_ops: 7
  slug: stripe-setup-intents-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscription Items API from Stripe — 4 operation(s) for subscription items.
  name: Stripe Subscription Items API
  phrasing_intents:
  - id: GetSubscriptionItems
    intent: List items on a subscription
    question: How do I see every price and quantity on a subscription?
  - id: PostSubscriptionItems
    intent: Add an item to a subscription
    question: How do I add an add-on to an existing subscription?
  - id: DeleteSubscriptionItemsItem
    intent: Remove an item from a subscription
    question: How do I remove an add-on without canceling the whole subscription?
  - id: GetSubscriptionItemsItem
    intent: Get a subscription item
    question: How do I look up one line item on a subscription?
  - id: PostSubscriptionItemsItem
    intent: Change a subscription item
    question: How do I change the quantity of seats on a subscription?
  - id: GetSubscriptionItemsSubscriptionItemUsageRecordSummaries
    intent: Get usage totals for a subscription item
    question: How much metered usage has a subscription item recorded this period?
  - id: PostSubscriptionItemsSubscriptionItemUsageRecords
    intent: Report metered usage
    question: How do I report usage for a metered subscription?
  phrasing_ops: 7
  slug: stripe-subscription-items-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscription Schedules API from Stripe — 4 operation(s) for subscription schedules.
  name: Stripe Subscription Schedules API
  phrasing_intents:
  - id: GetSubscriptionSchedules
    intent: List subscription schedules
    question: How do I see all the subscription changes I've scheduled?
  - id: PostSubscriptionSchedules
    intent: Schedule a subscription with future phases
    question: How do I set up a subscription that changes price on a future date?
  - id: GetSubscriptionSchedulesSchedule
    intent: Get a subscription schedule
    question: How do I see the phases planned for a subscription schedule?
  - id: PostSubscriptionSchedulesSchedule
    intent: Change a subscription schedule's phases
    question: How do I change the upcoming phases of a scheduled subscription?
  - id: PostSubscriptionSchedulesScheduleCancel
    intent: Cancel a subscription schedule and its subscription
    question: How do I cancel a scheduled subscription immediately?
  - id: PostSubscriptionSchedulesScheduleRelease
    intent: Release a subscription from its schedule
    question: How do I stop a schedule but keep the customer's subscription running?
  phrasing_ops: 6
  slug: stripe-subscription-schedules-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Subscriptions API from Stripe — 8 operation(s) for subscriptions.
  name: Stripe Subscriptions API
  phrasing_intents:
  - id: GetSubscriptions
    intent: List subscriptions
    question: How do I see all active subscriptions for a customer?
  - id: PostSubscriptions
    intent: Start a subscription for a customer
    question: How do I sign a customer up for a recurring plan?
  - id: GetSubscriptionsSearch
    intent: Search subscriptions
    question: How do I find subscriptions matching a status or metadata value?
  - id: DeleteSubscriptionsSubscriptionExposedId
    intent: Cancel a subscription now
    question: How do I cancel a customer's subscription immediately?
  - id: GetSubscriptionsSubscriptionExposedId
    intent: Get a subscription
    question: How do I check a subscription's status and next renewal?
  - id: PostSubscriptionsSubscriptionExposedId
    intent: Change a subscription
    question: How do I upgrade or downgrade a customer's subscription?
  - id: DeleteSubscriptionsSubscriptionExposedIdDiscount
    intent: Remove a subscription's discount
    question: How do I take a discount off a subscription?
  - id: PostSubscriptionsSubscriptionResume
    intent: Resume a paused subscription
    question: How do I restart a subscription that's paused?
  phrasing_ops: 8
  slug: stripe-subscriptions-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Tax Codes API from Stripe — 2 operation(s) for tax codes.
  name: Stripe Tax Codes API
  phrasing_intents:
  - id: GetTaxCodes
    intent: List product tax codes
    question: Which tax codes can I assign to my products?
  - id: GetTaxCodesId
    intent: Retrieve a tax code
    question: How do I see what a specific tax code covers?
  phrasing_ops: 2
  slug: stripe-tax-codes-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Tax Rates API from Stripe — 2 operation(s) for tax rates.
  name: Stripe Tax Rates API
  phrasing_intents:
  - id: GetTaxRates
    intent: List tax rates
    question: How do I see all the tax rates I've set up for invoices and subscriptions?
  - id: PostTaxRates
    intent: Create a tax rate
    question: How do I add a sales tax or VAT rate to apply to my invoices?
  - id: GetTaxRatesTaxRate
    intent: Look up a tax rate
    question: How do I check the percentage and jurisdiction of one tax rate?
  - id: PostTaxRatesTaxRate
    intent: Update a tax rate
    question: How do I archive a tax rate I no longer charge?
  phrasing_ops: 4
  slug: stripe-tax-rates-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Webhook Endpoints API from Stripe — 2 operation(s) for webhook endpoints.
  name: Stripe Webhook Endpoints API
  phrasing_intents:
  - id: GetWebhookEndpoints
    intent: List webhook endpoints
    question: Which URLs am I sending webhook events to?
  - id: PostWebhookEndpoints
    intent: Create a webhook endpoint
    question: How do I get notified at my server when a payment succeeds?
  - id: DeleteWebhookEndpointsWebhookEndpoint
    intent: Delete a webhook endpoint
    question: How do I stop sending events to an old webhook URL for good?
  - id: GetWebhookEndpointsWebhookEndpoint
    intent: Get a webhook endpoint
    question: How do I check which events a webhook endpoint listens for?
  - id: PostWebhookEndpointsWebhookEndpoint
    intent: Update or disable a webhook endpoint
    question: How do I change the events a webhook endpoint receives?
  phrasing_ops: 5
  slug: stripe-webhook-endpoints-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Invoice Items API from Stripe — 2 operation(s) for invoice items.
  name: Stripe Invoice Items API
  slug: stripe-invoice-items-api
- baseURL: https://api.stripe.com/
  baseurl_source: spec
  description: The Top Ups API from Stripe — 3 operation(s) for top ups.
  name: Stripe Top Ups API
  slug: stripe-top-ups-api
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
artifact_total: 554
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
- group: design
  href: https://artifacts.apis.io/stripe/rules/stripe-rules.yml
  title: ''
  type: Spectral
  url: rules/stripe-rules.yml
- group: design
  href: https://artifacts.apis.io/stripe/rules/stripe-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/stripe-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/stripe/rules/stripe-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/stripe-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/stripe/json-ld/stripe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stripe-context.jsonld
- group: design
  href: https://artifacts.apis.io/stripe/asyncapi/stripe-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/stripe-webhooks-asyncapi.yml
- group: other
  href: https://artifacts.apis.io/stripe/hosts/stripe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stripe-hosts.yml
- group: build
  href: https://artifacts.apis.io/stripe/integrations/stripe-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/stripe-integration-edges.yml
- group: company
  title: ''
  type: Newsroom
  url: https://stripe.com/se/newsroom
- group: commercial
  href: https://artifacts.apis.io/stripe/finops/stripe-finops.yml
  title: ''
  type: FinOps
  url: finops/stripe-finops.yml
- group: operate
  href: https://artifacts.apis.io/stripe/rate-limits/stripe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stripe-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://stripe.com/pricing
- group: commercial
  href: https://artifacts.apis.io/stripe/plans/stripe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stripe-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-topups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-topups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-billing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-billing-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-country-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-country-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-link-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-link-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-connect-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-customer-portal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-customer-portal-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/overlays/stripe-revenue-recognition-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stripe-revenue-recognition-overlay.yaml
- group: other
  href: https://artifacts.apis.io/stripe/capabilities/stripe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stripe-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/stripe/skills/stripe-calculate-and-settle-tax.md
  title: ''
  type: AgentSkill
  url: skills/stripe-calculate-and-settle-tax.md
- group: operate
  title: ''
  type: Roadmap
  url: https://stripe.com/roadmap
- group: agent
  href: https://artifacts.apis.io/stripe/agentic-access/stripe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stripe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/stripe/security/stripe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stripe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/stripe/security/stripe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stripe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stripe/security/stripe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stripe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stripe/authentication/stripe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stripe-authentication.yml
- group: auth
  href: https://artifacts.apis.io/stripe/scopes/stripe-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/stripe-scopes.yml
- group: start
  href: https://artifacts.apis.io/stripe/sandbox/stripe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stripe-sandbox.yml
- group: design
  href: https://artifacts.apis.io/stripe/conventions/stripe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stripe-conventions.yml
- group: operate
  href: https://artifacts.apis.io/stripe/changelog/stripe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stripe-changelog.yml
- group: build
  href: https://artifacts.apis.io/stripe/cli/stripe-cli.yml
  title: ''
  type: CLI
  url: cli/stripe-cli.yml
- group: design
  href: https://artifacts.apis.io/stripe/components/stripe-components.yml
  title: ''
  type: Components
  url: components/stripe-components.yml
- group: design
  href: https://artifacts.apis.io/stripe/data-model/stripe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stripe-data-model.yml
- group: build
  href: https://artifacts.apis.io/stripe/errors/stripe-decline-codes.yml
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
  href: https://artifacts.apis.io/stripe/arazzo/stripe-add-and-scale-subscription-item-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-add-and-scale-subscription-item-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-attach-payment-method-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-attach-payment-method-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-authorize-and-capture-payment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-authorize-and-capture-payment-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-cancel-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-cancel-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-cancel-uncaptured-payment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-cancel-uncaptured-payment-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-capture-and-partial-refund-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-capture-and-partial-refund-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-charge-and-refund-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-charge-and-refund-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-checkout-session-and-lineitems-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-checkout-session-and-lineitems-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-create-and-cancel-payout-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-and-cancel-payout-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-create-and-finalize-invoice-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-and-finalize-invoice-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-create-customer-and-pay-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-customer-and-pay-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-create-product-and-price-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-create-product-and-price-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-expire-checkout-session-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-expire-checkout-session-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-invoice-and-collect-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-invoice-and-collect-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-launch-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-launch-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-onboard-customer-to-plan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-onboard-customer-to-plan-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-pause-and-resume-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-pause-and-resume-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-refund-payment-intent-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-refund-payment-intent-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-reverse-payout-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-reverse-payout-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-save-card-and-charge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-save-card-and-charge-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-send-invoice-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-send-invoice-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-subscribe-existing-customer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-subscribe-existing-customer-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-void-invoice-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-void-invoice-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-write-off-invoice-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-write-off-invoice-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-connect-onboard-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-connect-onboard-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-issue-card-to-cardholder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-issue-card-to-cardholder-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-verify-identity-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-verify-identity-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-link-financial-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-link-financial-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-setup-future-payment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-setup-future-payment-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-calculate-and-settle-tax-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/stripe-calculate-and-settle-tax-workflow.yml
- group: design
  href: https://artifacts.apis.io/stripe/arazzo/stripe-quote-to-paid-invoice-workflow.yml
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
  href: https://artifacts.apis.io/stripe/asyncapi/stripe-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/stripe-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-customer.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-customer.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-payment-intent.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-payment-intent.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-subscription.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-subscription.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-charge.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-charge.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-invoice.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-invoice.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-event.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-event.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-product.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-product.json
- group: docs
  href: https://artifacts.apis.io/stripe/json-schema/stripe-price.json
  title: ''
  type: JSONSchema
  url: json-schema/stripe-price.json
- group: design
  href: https://artifacts.apis.io/stripe/json-ld/stripe-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/stripe-context.jsonld
- group: design
  href: https://artifacts.apis.io/stripe/rules/stripe-rules.yml
  title: ''
  type: SpectralRules
  url: rules/stripe-rules.yml
- group: design
  href: https://artifacts.apis.io/stripe/vocabulary/stripe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stripe-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stripe/json-structure/stripe-payment-intent-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/stripe-payment-intent-structure.json
- group: design
  href: https://artifacts.apis.io/stripe/json-structure/stripe-customer-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/stripe-customer-structure.json
- group: design
  href: https://artifacts.apis.io/stripe/json-structure/stripe-invoice-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/stripe-invoice-structure.json
- group: build
  href: https://artifacts.apis.io/stripe/examples/stripe-create-payment-intent-example.json
  title: ''
  type: Examples
  url: examples/stripe-create-payment-intent-example.json
- group: build
  href: https://artifacts.apis.io/stripe/examples/stripe-create-checkout-session-example.json
  title: ''
  type: Examples
  url: examples/stripe-create-checkout-session-example.json
- group: build
  href: https://artifacts.apis.io/stripe/examples/stripe-create-customer-example.json
  title: ''
  type: Examples
  url: examples/stripe-create-customer-example.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stripe.com/llms.txt
- group: build
  href: https://artifacts.apis.io/stripe/packages/stripe-packages.yml
  title: ''
  type: Packages
  url: packages/stripe-packages.yml
- group: agent
  href: https://artifacts.apis.io/stripe/well-known/stripe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stripe-well-known.yml
- group: auth
  href: https://artifacts.apis.io/stripe/well-known/stripe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stripe-security.txt
- group: agent
  href: https://artifacts.apis.io/stripe/mcp/stripe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stripe-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stripe/llms/stripe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stripe-llms.txt
- group: design
  href: https://artifacts.apis.io/stripe/conformance/stripe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stripe-conformance.yml
- group: design
  href: https://artifacts.apis.io/stripe/errors/stripe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stripe-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stripe/lifecycle/stripe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stripe-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.stripe.com/upgrades
- group: design
  href: https://artifacts.apis.io/stripe/conventions/stripe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stripe-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.stripe.com/security
- group: agent
  href: https://artifacts.apis.io/stripe/skills/_index.yml
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
- has_sources: true
  method: derived
  name: Stripe Finops
  primary_unit: transaction
  service_category: ''
  slug: stripe-finops
  template: false
image: https://stripe.com/img/about/logos/logos/blue.png
json_schemas:
- name: AccountList
  property_count: 0
  slug: stripe-account-list
- name: APIMethodRefundList
  property_count: 4
  slug: stripe-apimethod-refund-list
- name: ApmsSourcesSourceTransactionList
  property_count: 4
  slug: stripe-apms-sources-source-transaction-list
- name: Balance
  property_count: 7
  slug: stripe-balance
- name: BalanceTransaction
  property_count: 15
  slug: stripe-balance-transaction
- name: BalanceTransactionsList
  property_count: 4
  slug: stripe-balance-transactions-list
- name: BankConnectionsResourceLinkedAccountList
  property_count: 4
  slug: stripe-bank-connections-resource-linked-account-list
- name: BankConnectionsResourceTransactionList
  property_count: 4
  slug: stripe-bank-connections-resource-transaction-list
- name: Card
  property_count: 28
  slug: stripe-card
- name: Charge
  property_count: 45
  slug: stripe-charge
- name: Stripe Charge
  property_count: 44
  slug: stripe-charge
- name: Session
  property_count: 54
  slug: stripe-checkout-session
- name: ClimateRemovalsOrders
  property_count: 22
  slug: stripe-climate-order
- name: ClimateRemovalsProducts
  property_count: 9
  slug: stripe-climate-product
- name: ClimateRemovalsSuppliers
  property_count: 7
  slug: stripe-climate-supplier
- name: Coupon
  property_count: 17
  slug: stripe-coupon
- name: CouponsResourceCouponList
  property_count: 4
  slug: stripe-coupons-resource-coupon-list
- name: CreditNoteLinesList
  property_count: 4
  slug: stripe-credit-note-lines-list
- name: CreditNote
  property_count: 30
  slug: stripe-credit-note
- name: CreditNotesList
  property_count: 4
  slug: stripe-credit-notes-list
- name: Customer
  property_count: 28
  slug: stripe-customer
- name: Stripe Customer
  property_count: 25
  slug: stripe-customer
- name: DeleteCouponsCouponRequest
  property_count: 0
  slug: stripe-delete-coupons-coupon-request
- name: DeleteEphemeralKeysKeyRequest
  property_count: 1
  slug: stripe-delete-ephemeral-keys-key-request
- name: DeletePlansPlanRequest
  property_count: 0
  slug: stripe-delete-plans-plan-request
- name: DeletedCoupon
  property_count: 3
  slug: stripe-deleted-coupon
- name: DeletedPlan
  property_count: 3
  slug: stripe-deleted-plan
- name: DeletedProduct
  property_count: 3
  slug: stripe-deleted-product
- name: DisputeList
  property_count: 4
  slug: stripe-dispute-list
- name: Dispute
  property_count: 16
  slug: stripe-dispute
- name: EphemeralKey
  property_count: 6
  slug: stripe-ephemeral-key
- name: NotificationEvent
  property_count: 10
  slug: stripe-event
- name: Stripe Event
  property_count: 10
  slug: stripe-event
- name: ExchangeRateList
  property_count: 4
  slug: stripe-exchange-rate-list
- name: ExchangeRate
  property_count: 3
  slug: stripe-exchange-rate
- name: ExternalAccountList
  property_count: 0
  slug: stripe-external-account-list
- name: File
  property_count: 11
  slug: stripe-file
- name: BankConnectionsResourceLinkedAccount
  property_count: 19
  slug: stripe-financial-connections-account
- name: BankConnectionsResourceLinkAccountSession
  property_count: 10
  slug: stripe-financial-connections-session
- name: BankConnectionsResourceTransaction
  property_count: 12
  slug: stripe-financial-connections-transaction
- name: FinancialReportingFinanceReportRunList
  property_count: 4
  slug: stripe-financial-reporting-finance-report-run-list
- name: FinancialReportingFinanceReportTypeList
  property_count: 4
  slug: stripe-financial-reporting-finance-report-type-list
- name: GelatoVerificationReportList
  property_count: 4
  slug: stripe-gelato-verification-report-list
- name: GelatoVerificationSessionList
  property_count: 4
  slug: stripe-gelato-verification-session-list
- name: GetAccountsAccountExternalAccountsRequest
  property_count: 0
  slug: stripe-get-accounts-account-external-accounts-request
- name: GetAccountsRequest
  property_count: 0
  slug: stripe-get-accounts-request
- name: GetBalanceHistoryIdRequest
  property_count: 0
  slug: stripe-get-balance-history-id-request
- name: GetBalanceHistoryRequest
  property_count: 0
  slug: stripe-get-balance-history-request
- name: GetBalanceRequest
  property_count: 0
  slug: stripe-get-balance-request
- name: GetCheckoutSessionsRequest
  property_count: 0
  slug: stripe-get-checkout-sessions-request
- name: GetDisputesDisputeRequest
  property_count: 0
  slug: stripe-get-disputes-dispute-request
- name: GetDisputesRequest
  property_count: 0
  slug: stripe-get-disputes-request
- name: GetEventsIdRequest
  property_count: 0
  slug: stripe-get-events-id-request
- name: GetEventsRequest
  property_count: 0
  slug: stripe-get-events-request
- name: GetExchangeRatesRateIdRequest
  property_count: 0
  slug: stripe-get-exchange-rates-rate-id-request
- name: GetExchangeRatesRequest
  property_count: 0
  slug: stripe-get-exchange-rates-request
- name: GetPaymentLinksPaymentLinkLineItemsRequest
  property_count: 0
  slug: stripe-get-payment-links-payment-link-line-items-request
- name: GetPricesPriceRequest
  property_count: 0
  slug: stripe-get-prices-price-request
- name: GetPromotionCodesPromotionCodeRequest
  property_count: 0
  slug: stripe-get-promotion-codes-promotion-code-request
- name: GetPromotionCodesRequest
  property_count: 0
  slug: stripe-get-promotion-codes-request
- name: GetRefundsRefundRequest
  property_count: 0
  slug: stripe-get-refunds-refund-request
- name: GetReportingReportRunsReportRunRequest
  property_count: 0
  slug: stripe-get-reporting-report-runs-report-run-request
- name: GetReviewsRequest
  property_count: 0
  slug: stripe-get-reviews-request
- name: GetReviewsReviewRequest
  property_count: 0
  slug: stripe-get-reviews-review-request
- name: GetSigmaScheduledQueryRunsRequest
  property_count: 0
  slug: stripe-get-sigma-scheduled-query-runs-request
- name: GetSigmaScheduledQueryRunsScheduledQueryRunRequest
  property_count: 0
  slug: stripe-get-sigma-scheduled-query-runs-scheduled-query-run-request
- name: GelatoVerificationReport
  property_count: 10
  slug: stripe-identity-verification-report
- name: GelatoVerificationSession
  property_count: 14
  slug: stripe-identity-verification-session
- name: Stripe Invoice
  property_count: 43
  slug: stripe-invoice
- name: InvoiceItem
  property_count: 22
  slug: stripe-invoiceitem
- name: IssuingAuthorization
  property_count: 25
  slug: stripe-issuing-authorization
- name: NotificationEventList
  property_count: 4
  slug: stripe-notification-event-list
- name: PaymentIntent
  property_count: 39
  slug: stripe-payment-intent
- name: Stripe Payment Intent
  property_count: 37
  slug: stripe-payment-intent
- name: PaymentLink
  property_count: 33
  slug: stripe-payment-link
- name: PaymentLinksResourceListLineItems
  property_count: 4
  slug: stripe-payment-links-resource-list-line-items
- name: PaymentLinksResourcePaymentLinkList
  property_count: 4
  slug: stripe-payment-links-resource-payment-link-list
- name: PaymentPagesCheckoutSessionListLineItems
  property_count: 4
  slug: stripe-payment-pages-checkout-session-list-line-items
- name: PaymentPagesCheckoutSessionList
  property_count: 4
  slug: stripe-payment-pages-checkout-session-list
- name: PayoutList
  property_count: 4
  slug: stripe-payout-list
- name: Payout
  property_count: 23
  slug: stripe-payout
- name: PlanList
  property_count: 4
  slug: stripe-plan-list
- name: Plan
  property_count: 20
  slug: stripe-plan
- name: PostChargesChargeDisputeRequest
  property_count: 4
  slug: stripe-post-charges-charge-dispute-request
- name: PostChargesChargeRequest
  property_count: 8
  slug: stripe-post-charges-charge-request
- name: PostChargesRequest
  property_count: 20
  slug: stripe-post-charges-request
- name: PostCheckoutSessionsRequest
  property_count: 38
  slug: stripe-post-checkout-sessions-request
- name: PostCheckoutSessionsSessionExpireRequest
  property_count: 1
  slug: stripe-post-checkout-sessions-session-expire-request
- name: PostClimateOrdersOrderRequest
  property_count: 3
  slug: stripe-post-climate-orders-order-request
- name: PostClimateOrdersRequest
  property_count: 7
  slug: stripe-post-climate-orders-request
- name: PostClimateReservationsRequest
  property_count: 7
  slug: stripe-post-climate-reservations-request
- name: PostCouponsCouponRequest
  property_count: 4
  slug: stripe-post-coupons-coupon-request
- name: PostCouponsRequest
  property_count: 13
  slug: stripe-post-coupons-request
- name: PostCreditNotesIdRequest
  property_count: 3
  slug: stripe-post-credit-notes-id-request
- name: PostCreditNotesIdVoidRequest
  property_count: 1
  slug: stripe-post-credit-notes-id-void-request
- name: PostCreditNotesRequest
  property_count: 13
  slug: stripe-post-credit-notes-request
- name: PostCustomersCustomerRequest
  property_count: 25
  slug: stripe-post-customers-customer-request
- name: PostCustomersCustomerSubscriptionsRequest
  property_count: 29
  slug: stripe-post-customers-customer-subscriptions-request
- name: PostCustomersCustomerSubscriptionsSubscriptionExposedIdRequest
  property_count: 29
  slug: stripe-post-customers-customer-subscriptions-subscription-exposed-id-request
- name: PostDisputesDisputeCloseRequest
  property_count: 1
  slug: stripe-post-disputes-dispute-close-request
- name: PostDisputesDisputeRequest
  property_count: 4
  slug: stripe-post-disputes-dispute-request
- name: PostEphemeralKeysRequest
  property_count: 5
  slug: stripe-post-ephemeral-keys-request
- name: PostFilesRequest
  property_count: 4
  slug: stripe-post-files-request
- name: PostFinancialConnectionsSessionsRequest
  property_count: 6
  slug: stripe-post-financial-connections-sessions-request
- name: PostIdentityVerificationSessionsRequest
  property_count: 5
  slug: stripe-post-identity-verification-sessions-request
- name: PostIdentityVerificationSessionsSessionRequest
  property_count: 4
  slug: stripe-post-identity-verification-sessions-session-request
- name: PostInvoice_ItemsInvoiceitemRequest
  property_count: 15
  slug: stripe-post-invoice-items-invoiceitem-request
- name: PostInvoice_ItemsRequest
  property_count: 19
  slug: stripe-post-invoice-items-request
- name: PostIssuingCardholdersCardholderRequest
  property_count: 10
  slug: stripe-post-issuing-cardholders-cardholder-request
- name: PostIssuingCardholdersRequest
  property_count: 12
  slug: stripe-post-issuing-cardholders-request
- name: PostIssuingCardsCardRequest
  property_count: 6
  slug: stripe-post-issuing-cards-card-request
- name: PostIssuingCardsRequest
  property_count: 11
  slug: stripe-post-issuing-cards-request
- name: PostIssuingDisputesRequest
  property_count: 6
  slug: stripe-post-issuing-disputes-request
- name: PostPaymentIntentsIntentCaptureRequest
  property_count: 8
  slug: stripe-post-payment-intents-intent-capture-request
- name: PostPaymentIntentsIntentConfirmRequest
  property_count: 17
  slug: stripe-post-payment-intents-intent-confirm-request
- name: PostPaymentIntentsIntentIncrementAuthorizationRequest
  property_count: 7
  slug: stripe-post-payment-intents-intent-increment-authorization-request
- name: PostPaymentIntentsIntentRequest
  property_count: 20
  slug: stripe-post-payment-intents-intent-request
- name: PostPaymentIntentsRequest
  property_count: 31
  slug: stripe-post-payment-intents-request
- name: PostPaymentLinksPaymentLinkRequest
  property_count: 19
  slug: stripe-post-payment-links-payment-link-request
- name: PostPaymentLinksRequest
  property_count: 28
  slug: stripe-post-payment-links-request
- name: PostPayoutsPayoutCancelRequest
  property_count: 1
  slug: stripe-post-payouts-payout-cancel-request
- name: PostPayoutsPayoutRequest
  property_count: 2
  slug: stripe-post-payouts-payout-request
- name: PostPayoutsPayoutReverseRequest
  property_count: 2
  slug: stripe-post-payouts-payout-reverse-request
- name: PostPayoutsRequest
  property_count: 9
  slug: stripe-post-payouts-request
- name: PostPlansPlanRequest
  property_count: 6
  slug: stripe-post-plans-plan-request
- name: PostPlansRequest
  property_count: 18
  slug: stripe-post-plans-request
- name: PostPricesPriceRequest
  property_count: 8
  slug: stripe-post-prices-price-request
- name: PostPricesRequest
  property_count: 19
  slug: stripe-post-prices-request
- name: PostProductsIdRequest
  property_count: 14
  slug: stripe-post-products-id-request
- name: PostProductsRequest
  property_count: 15
  slug: stripe-post-products-request
- name: PostPromotionCodesPromotionCodeRequest
  property_count: 4
  slug: stripe-post-promotion-codes-promotion-code-request
- name: PostPromotionCodesRequest
  property_count: 9
  slug: stripe-post-promotion-codes-request
- name: PostQuotesQuoteFinalizeRequest
  property_count: 2
  slug: stripe-post-quotes-quote-finalize-request
- name: PostQuotesQuoteRequest
  property_count: 18
  slug: stripe-post-quotes-quote-request
- name: PostQuotesRequest
  property_count: 20
  slug: stripe-post-quotes-request
- name: PostRadarValueListsRequest
  property_count: 5
  slug: stripe-post-radar-value-lists-request
- name: PostRadarValueListsValueListRequest
  property_count: 4
  slug: stripe-post-radar-value-lists-value-list-request
- name: PostRefundsRefundCancelRequest
  property_count: 1
  slug: stripe-post-refunds-refund-cancel-request
- name: PostRefundsRefundRequest
  property_count: 2
  slug: stripe-post-refunds-refund-request
- name: PostRefundsRequest
  property_count: 12
  slug: stripe-post-refunds-request
- name: PostReportingReportRunsRequest
  property_count: 3
  slug: stripe-post-reporting-report-runs-request
- name: PostReviewsReviewApproveRequest
  property_count: 1
  slug: stripe-post-reviews-review-approve-request
- name: PostSourcesRequest
  property_count: 16
  slug: stripe-post-sources-request
- name: PostSourcesSourceRequest
  property_count: 6
  slug: stripe-post-sources-source-request
- name: PostTaxCalculationsRequest
  property_count: 7
  slug: stripe-post-tax-calculations-request
- name: PostTaxRegistrationsRequest
  property_count: 5
  slug: stripe-post-tax-registrations-request
- name: PostTaxTransactionsCreateReversalRequest
  property_count: 8
  slug: stripe-post-tax-transactions-create-reversal-request
- name: PostTerminalConfigurationsConfigurationRequest
  property_count: 5
  slug: stripe-post-terminal-configurations-configuration-request
- name: PostTerminalConfigurationsRequest
  property_count: 5
  slug: stripe-post-terminal-configurations-request
- name: PostTerminalLocationsRequest
  property_count: 5
  slug: stripe-post-terminal-locations-request
- name: PostTerminalReadersReaderRefundPaymentRequest
  property_count: 7
  slug: stripe-post-terminal-readers-reader-refund-payment-request
- name: PostTestHelpersIssuingAuthorizationsRequest
  property_count: 11
  slug: stripe-post-test-helpers-issuing-authorizations-request
- name: PostTestHelpersIssuingTransactionsCreateUnlinkedRefundRequest
  property_count: 6
  slug: stripe-post-test-helpers-issuing-transactions-create-unlinked-refund-request
- name: PriceList
  property_count: 4
  slug: stripe-price-list
- name: Price
  property_count: 21
  slug: stripe-price
- name: Stripe Price
  property_count: 21
  slug: stripe-price
- name: ProductList
  property_count: 4
  slug: stripe-product-list
- name: Product
  property_count: 18
  slug: stripe-product
- name: Stripe Product
  property_count: 19
  slug: stripe-product
- name: PromotionCode
  property_count: 13
  slug: stripe-promotion-code
- name: PromotionCodesResourcePromotionCodeList
  property_count: 4
  slug: stripe-promotion-codes-resource-promotion-code-list
- name: Quote
  property_count: 35
  slug: stripe-quote
- name: QuotesResourceListLineItems
  property_count: 4
  slug: stripe-quotes-resource-list-line-items
- name: QuotesResourceQuoteList
  property_count: 4
  slug: stripe-quotes-resource-quote-list
- name: RadarEarlyFraudWarningList
  property_count: 4
  slug: stripe-radar-early-fraud-warning-list
- name: RadarEarlyFraudWarning
  property_count: 8
  slug: stripe-radar-early-fraud-warning
- name: RadarReviewList
  property_count: 4
  slug: stripe-radar-review-list
- name: RadarListListItem
  property_count: 7
  slug: stripe-radar-value-list-item
- name: RadarListList
  property_count: 10
  slug: stripe-radar-value-list
- name: Refund
  property_count: 20
  slug: stripe-refund
- name: reporting_report_run
  property_count: 10
  slug: stripe-reporting-report-run
- name: reporting_report_type
  property_count: 9
  slug: stripe-reporting-report-type
- name: RadarReview
  property_count: 14
  slug: stripe-review
- name: ScheduledQueryRun
  property_count: 11
  slug: stripe-scheduled-query-run
- name: SearchResult
  property_count: 6
  slug: stripe-search-result
- name: ShippingRate
  property_count: 12
  slug: stripe-shipping-rate
- name: SigmaScheduledQueryRunList
  property_count: 4
  slug: stripe-sigma-scheduled-query-run-list
- name: SourceMandateNotification
  property_count: 12
  slug: stripe-source-mandate-notification
- name: Source
  property_count: 37
  slug: stripe-source
- name: SourceTransaction
  property_count: 14
  slug: stripe-source-transaction
- name: Subscription
  property_count: 43
  slug: stripe-subscription
- name: Stripe Subscription
  property_count: 43
  slug: stripe-subscription
- name: TaxProductResourceTaxCalculation
  property_count: 14
  slug: stripe-tax-calculation
- name: TaxProductRegistrationsResourceTaxRegistration
  property_count: 9
  slug: stripe-tax-registration
- name: TaxProductResourceTaxTransaction
  property_count: 14
  slug: stripe-tax-transaction
- name: TerminalLocationLocation
  property_count: 7
  slug: stripe-terminal-location
- name: TerminalReaderReader
  property_count: 12
  slug: stripe-terminal-reader
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
modified: '2026-09-16'
name: Stripe
nav: Providers
network: true
overview: 'Stripe publishes 71 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Balance API, Charges API, and 68 more. Tagged areas include Commerce, Financial Services, Fintech, Payments, and T1.


  The Stripe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Stripe''s developer surface includes pricing, authentication, sandbox, changelog, CLI, signup flow, developer portal, and 141 more developer resources.'
plans:
- name: Stripe Plans Pricing
  plan_count: 48
  slug: stripe-plans-pricing
- name: Stripe Price Estimates
  plan_count: 0
  slug: stripe-price-estimates
random_paper: 15
rate_limits:
- limit_count: 16
  name: Stripe Rate Limits
  slug: stripe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Stripe — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: stripe-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Stripe — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stripe-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
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
  composite: 81.5
  coverage:
    artifact_dirs: 45
    catalog_earned: 71.8
    catalog_earned_first_party: 24.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 94.7
    contract_governance: 22.0
    contract_quality: 72.1
    developer_ergonomics: 94.6
    discoverability: 55.8
    operational_transparency: 100.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 71
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
    score: 53.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stripe/stripe-2026-08-17T125440.png
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
skill_count: 6
skills:
- name: stripe-calculate-and-settle-tax
  slug: stripe-calculate-and-settle-tax
- name: stripe-connect-onboard-account
  slug: stripe-connect-onboard-account
- name: stripe-create-customer-and-charge
  slug: stripe-create-customer-and-charge
- name: stripe-launch-subscription
  slug: stripe-launch-subscription
- name: stripe-refund-payment
  slug: stripe-refund-payment
- name: stripe-verify-identity
  slug: stripe-verify-identity
slug: stripe
tags:
- Commerce
- Financial Services
- Fintech
- Payments
- T1
- Stripe
- Agentic Commerce
- Point-of-Sale
- Payment Processing
website: https://stripe.com
---
