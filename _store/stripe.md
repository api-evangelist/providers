---
specificationVersion: '0.18'
aid: stripe
name: Stripe
description: >-
  Millions of companies of all sizes use Stripe online and in person to accept
  payments, send payouts, automate financial processes, and ultimately grow
  revenue.
url: >-
  https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md
created: 2024/04/14
modified: 2024-07-03T00:00:00.000Z
tags: []
apis:
  - aid: stripe:stripe-accounts-api
    name: Stripe Accounts API
    description: >-
      This is an object representing a Stripe account. You can retrieve it to
      see properties on the account like its current requirements or if the
      account is enabled to make live charges or receive payouts.
    tags:
      - Accounts
      - Bank
      - Capabilities
      - External
      - Links
      - Login
      - People
      - Person
      - Persons
      - Reject
      - Sessions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/accounts
      - type: OpenAPI
        url: openapi/accounts-openapi-original.yml
  - aid: stripe:stripe-apple-pay-api
    name: Stripe Apple Pay API
    description: >-
      Stripe users can accept Apple Pay in iOS applications in iOS 9 and above,
      and on the web in Safari starting with iOS 10 or macOS Sierra. There are
      no additional fees to process Apple Pay payments, and the pricing is the
      same as other card transactions.
    tags:
      - Apple
      - Domains
      - Pay
    properties:
      - type: Documentation
        url: https://stripe.com/docs/apple-pay
      - type: OpenAPI
        url: openapi/apple-pay-openapi-original.yml
  - aid: stripe:stripe-application-fees-api
    name: Stripe Application Fees API
    description: >-
      When you collect a transaction fee on top of a charge made for your user
      (using Connect), an Application Fee object is created in your account. You
      can list, retrieve, and refund application fees.
    tags:
      - Applications
      - Fees
      - Fee
      - Refunds
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/application_fees
      - type: OpenAPI
        url: openapi/application-fees-openapi-original.yml
  - aid: stripe:stripe-application-secrets-api
    name: Stripe Application Secrets API
    description: >-
      Secret Store is an API that allows Stripe Apps developers to securely
      persist secrets for use by UI Extensions and app backends.
    tags:
      - Applications
      - Secrets
      - Find
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/secret_management
      - type: OpenAPI
        url: openapi/application-secrets-openapi-original.yml
  - aid: stripe:stripe-balance-api
    name: Stripe Balance API
    description: >-
      This is an object representing your Stripe balance. You can retrieve it to
      see the balance currently on your Stripe account. You can also retrieve
      the balance history, which contains a list of transactions that
      contributed to the balance (charges, payouts, and so forth).
    tags:
      - Balance
      - History
      - Transactions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/balance
      - type: OpenAPI
        url: openapi/balance-openapi-original.yml
  - aid: stripe:stripe-billing-api
    name: Stripe Billing API
    description: >-
      Create and manage subscriptions, recurring payments, and recurring
      revenue.
    tags:
      - Billing
      - Configurations
      - Portals
      - Sessions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/billing
      - type: OpenAPI
        url: openapi/billing-openapi-original.yml
  - aid: stripe:stripe-charges-api
    name: Stripe Charges API
    description: >-
      The Charge object represents a single attempt to move money into your
      Stripe account. PaymentIntent confirmation is the most common way to
      create Charges, but transferring money to a different Stripe account
      through Connect also creates Charges. Some legacy payment flows create
      Charges directly, which is not recommended for new integrations.
    tags:
      - Charges
      - Search
      - Charge
      - Capture
      - Disputes
      - Close
      - Refunds
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/charges
      - type: OpenAPI
        url: openapi/charges-openapi-original.yml
  - aid: stripe:stripe-checkout-api
    name: Stripe Checkout API
    description: >-
      Checkout is a low-code payment integration that creates a customizable
      form for collecting payments. You can embed Checkout directly in your
      website or redirect customers to a Stripe-hosted payment page. It supports
      one-time payments and subscriptions and accepts over 40 local payment
      methods.
    tags:
      - Checkout
      - Sessions
      - Expire
      - Items
      - Line
    properties:
      - type: Documentation
        url: https://stripe.com/docs/payments/checkout
      - type: OpenAPI
        url: openapi/checkout-openapi-original.yml
  - aid: stripe:stripe-climate-api
    name: Stripe Climate API
    description: >-
      Stripe Climate is the easiest way to help promising permanent carbon
      removal technologies launch and scale. Join a growing group of ambitious
      businesses that are changing the course of carbon removal.
    tags:
      - Climate
      - Orders
      - Cancel
      - Products
      - Reservations
      - Confirm
      - Suppliers
      - Supplier
    properties:
      - type: Documentation
        url: https://stripe.com/climate
      - type: OpenAPI
        url: openapi/climate-openapi-original.yml
  - aid: stripe:stripe-country-api
    name: Stripe Country API
    description: >-
      Stripe needs to collect certain pieces of information about each account
      created. These requirements can differ depending on the account's country.
      The Country Specs API makes these rules available to your integration.
    tags:
      - Countries
      - Specs
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/country_specs
      - type: OpenAPI
        url: openapi/country-openapi-original.yml
  - aid: stripe:stripe-coupons-api
    name: Stripe Coupons API
    description: >-
      A coupon contains information about a percent-off or amount-off discount
      you might want to apply to a customer. Coupons may be applied to
      subscriptions, invoices, checkout sessions, quotes, and more. Coupons do
      not work with conventional one-off charges or payment intents.
    tags:
      - Coupons
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/coupons
      - type: OpenAPI
        url: openapi/coupons-openapi-original.yml
  - aid: stripe:stripe-credit-notes-api
    name: Stripe Credit Notes API
    description: >-
      Issue a credit note to adjust an invoice's amount after the invoice is
      finalized.
    tags:
      - Credit
      - Notes
      - Previews
      - Lines
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/credit_notes
      - type: OpenAPI
        url: openapi/credit-notes-openapi-original.yml
  - aid: stripe:stripe-customers-api
    name: Stripe Customers API
    description: >-
      This object represents a customer of your business. Use it to create
      recurring charges and track payments that belong to the same customer.
    tags:
      - Customers
      - Search
      - Balance
      - Transactions
      - Accounts
      - Bank
      - Verify
      - Cards
      - Cash
      - Discount
      - Funding
      - Instructions
      - Methods
      - Payments
      - Sources
      - Subscriptions
      - Exposed
      - Ids
      - Taxes
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/customers
      - type: OpenAPI
        url: openapi/customers-openapi-original.yml
  - aid: stripe:stripe-disputes-api
    name: Stripe Disputes API
    description: >-
      A dispute occurs when a customer questions your charge with their card
      issuer. When this happens, you have the opportunity to respond to the
      dispute with evidence that shows that the charge is legitimate.
    tags:
      - Disputes
      - Close
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/disputes
      - type: OpenAPI
        url: openapi/disputes-openapi-original.yml
  - aid: stripe:stripe-ephemeral-keys-api
    name: Stripe Ephemeral Keys API
    description: >-
      Stripe.js uses ephemeral keys to securely retrieve Card information from
      the Stripe API without publicly exposing your secret keys. You need to do
      some of the ephemeral key exchange on the server-side to set this up.
    tags:
      - Ephemeral
      - Keys
    properties:
      - type: Documentation
        url: https://stripe.com/docs/issuing/elements
      - type: OpenAPI
        url: openapi/ephemeral-keys-openapi-original.yml
  - aid: stripe:stripe-events-api
    name: Stripe Events API
    description: >-
      Events are our way of letting you know when something interesting happens
      in your account. When an interesting event occurs, we create a new Event
      object.
    tags:
      - Events
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/events
      - type: OpenAPI
        url: openapi/events-openapi-original.yml
  - aid: stripe:stripe-exchange-rates-api
    name: Stripe Exchange Rates API
    description: >-
      Stripe supports processing charges in 135+ currencies allowing you to
      present prices in a customer's native currency. Doing so can improve sales
      and help customers avoid conversion costs. In order to present prices in
      your customer's currency, you need to specify the presentment currency
      when creating a PaymentIntent or a charge.
    tags:
      - Exchange
      - Rates
    properties:
      - type: Documentation
        url: https://stripe.com/docs/currencies/conversions
      - type: OpenAPI
        url: openapi/exchange-rates-openapi-original.yml
  - aid: stripe:stripe-files-api
    name: Stripe Files API
    description: >-
      This object represents files hosted on Stripe's servers. You can upload
      files with the create file request (for example, when uploading dispute
      evidence). Stripe also creates files independently (for example, the
      results of a Sigma scheduled query).
    tags:
      - Files
      - File
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/files
      - type: OpenAPI
        url: openapi/files-openapi-original.yml
  - aid: stripe:stripe-financial-connections-api
    name: Stripe Financial Connections API
    description: >-
      Financial Connections lets your users securely share their financial data
      by linking their financial accounts to your business. Use Financial
      Connections to access user-permissioned account data such as tokenized
      account and routing numbers, balances, ownerships details, and
      transactions.
    tags:
      - Accounts
      - Connections
      - Financial
      - Disconnect
      - Owners
      - Refresh
      - Subscribe
      - Unsubscribe
      - Sessions
      - Transactions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/financial-connections
      - type: OpenAPI
        url: openapi/financial-connections-openapi-original.yml
  - aid: stripe:stripe-identity-api
    name: Stripe Identity API
    description: >-
      Use Stripe Identity to confirm the identity of global users to prevent
      fraud, streamline risk operations, and increase trust and safety.
    tags:
      - Entities
      - Identity
      - Reports
      - Verification
      - Sessions
      - Cancel
      - Redact
    properties:
      - type: Documentation
        url: https://stripe.com/docs/identity
      - type: OpenAPI
        url: openapi/identity-openapi-original.yml
  - aid: stripe:stripe-invoice-api
    name: Stripe Invoice API
    description: >-
      Invoices are statements of amounts owed by a customer, and are either
      generated one-off, or generated periodically from a subscription.
    tags:
      - Invoice Items
      - Invoices
      - Search
      - Upcoming
      - Lines
      - Finalize
      - Items
      - Line
      - Mark
      - Uncollectible
      - Pay
      - Send
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/invoices
      - type: OpenAPI
        url: openapi/invoice-openapi-original.yml
  - aid: stripe:stripe-issuing-api
    name: Stripe Issuing API
    description: >-
      An API for businesses to instantly create, manage, and distribute payment
      cards.
    tags:
      - Authorization
      - Issuing
      - Approve
      - Decline
      - Card Holders
      - Cards
      - Disputes
      - Submit
      - Settlements
      - Tokens
      - Transactions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/issuing
      - type: OpenAPI
        url: openapi/issuing-openapi-original.yml
  - aid: stripe:stripe-link-api
    name: Stripe Link API
    description: >-
      You can use the Payment Links API to create a payment link that you can
      share with your customers. Stripe redirects customers who open this link
      to a Stripe-hosted payment page.
    tags:
      - Accounts
      - Link
      - Sessions
      - Linked
      - Disconnect
      - Owners
      - Refresh
    properties:
      - type: Documentation
        url: https://stripe.com/docs/payment-links/api
      - type: OpenAPI
        url: openapi/link-openapi-original.yml
  - aid: stripe:stripe-payment-intents-api
    name: Stripe Payment Intents API
    description: >-
      A PaymentIntent guides you through the process of collecting a payment
      from your customer. We recommend that you create exactly one PaymentIntent
      for each order or customer session in your system. You can reference the
      PaymentIntent later to see the history of payment attempts for a
      particular session.
    tags:
      - Intents
      - Payments
      - Search
      - Intent
      - Balance
      - Customers
      - Cancel
      - Capture
      - Confirm
      - Authorization
      - Increment
      - Microdeposits
      - Verify
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/payment_intents
      - type: OpenAPI
        url: openapi/payment-intents-openapi-original.yml
  - aid: stripe:stripe-payment-links-api
    name: Stripe Payment Links API
    description: >-
      A payment link is a shareable URL that will take your customers to a
      hosted payment page. A payment link can be shared and used multiple times.
      When a customer opens a payment link it will open a new checkout session
      to render the payment page. You can use checkout session events to track
      payments through payment links.
    tags:
      - Links
      - Payments
      - Link
      - Items
      - Line
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/payment_links/payment_links
      - type: OpenAPI
        url: openapi/payment-links-openapi-original.yml
  - aid: stripe:stripe-payment-method-api
    name: Stripe Payment Method API
    description: >-
      The Payment Methods API allows you to accept a variety of payment methods
      through a single API. A PaymentMethod object contains the payment method
      details to create payments.
    tags:
      - Configurations
      - Methods
      - Payments
      - Domains
      - Ate
      - Val
      - Validate
      - Attach
      - Detach
    properties:
      - type: Documentation
        url: https://stripe.com/docs/payments/payment-methods
      - type: OpenAPI
        url: openapi/payment-method-openapi-original.yml
  - aid: stripe:stripe-payouts-api
    name: Stripe Payouts API
    description: >-
      A Payout object is created when you receive funds from Stripe, or when you
      initiate a payout to either a bank account or debit card of a connected
      Stripe account. You can retrieve individual payouts, and list all payouts.
      Payouts are made on varying schedules, depending on your country and
      industry.
    tags:
      - Payouts
      - Cancel
      - Reverse
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/payouts
      - type: OpenAPI
        url: openapi/payouts-openapi-original.yml
  - aid: stripe:stripe-plans-api
    name: Stripe Plans API
    description: >-
      You can now model subscriptions more flexibly using the Prices API. It
      replaces the Plans API and is backwards compatible to simplify your
      migration.
    tags:
      - Plans
      - Plan
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/plans
      - type: OpenAPI
        url: openapi/plans-openapi-original.yml
  - aid: stripe:stripe-prices-api
    name: Stripe Prices API
    description: >-
      Prices define the unit cost, currency, and (optional) billing cycle for
      both recurring and one-time purchases of products. Products help you track
      inventory or provisioning, and prices help you track payment terms.
      Different physical goods or levels of service should be represented by
      products, and pricing options should be represented by prices. This
      approach lets you change prices without having to change your provisioning
      scheme.
    tags:
      - Prices
      - Search
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/prices
      - type: OpenAPI
        url: openapi/prices-openapi-original.yml
  - aid: stripe:stripe-products-api
    name: Stripe Products API
    description: >-
      Products describe the specific goods or services you offer to your
      customers. For example, you might offer a Standard and Premium version of
      your goods or service; each version would be a separate Product. They can
      be used in conjunction with Prices to configure pricing in Payment Links,
      Checkout, and Subscriptions.
    tags:
      - Products
      - Search
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/products
      - type: OpenAPI
        url: openapi/products-openapi-original.yml
  - aid: stripe:stripe-promotion-codes-api
    name: Stripe Promotion Codes API
    description: >-
      A Promotion Code represents a customer-redeemable code for a coupon. It
      can be used to create multiple codes for a single coupon.
    tags:
      - Codes
      - Promotion
      - Code
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/promotion_codes
      - type: OpenAPI
        url: openapi/promotion-codes-openapi-original.yml
  - aid: stripe:stripe-quotes-api
    name: Stripe Quotes API
    description: >-
      A Quote is a way to model prices that you'd like to provide to a customer.
      Once accepted, it will automatically create an invoice, subscription or
      subscription schedule.
    tags:
      - Quotes
      - Accept
      - Cancel
      - Computed
      - Items
      - Line
      - Upfront
      - Finalize
      - PDF
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/quotes
      - type: OpenAPI
        url: openapi/quotes-openapi-original.yml
  - aid: stripe:stripe-radar-api
    name: Stripe Radar API
    description: >-
      Stripe Radar provides real-time fraud protection and requires no
      additional development time. Fraud professionals can add Radar for Fraud
      Teams to customize protection and get deeper insights.
    tags:
      - Early
      - Fraud
      - Radar
      - Warnings
      - Warning
      - Items
      - Value
    properties:
      - type: Documentation
        url: https://stripe.com/docs/radar
      - type: OpenAPI
        url: openapi/radar-openapi-original.yml
  - aid: stripe:stripe-refunds-api
    name: Stripe Refunds API
    description: >-
      Refund objects allow you to refund a previously created charge that isn't
      refunded yet. Funds are refunded to the credit or debit card that's
      initially charged.
    tags:
      - Refunds
      - Cancel
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/refunds
      - type: OpenAPI
        url: openapi/refunds-openapi-original.yml
  - aid: stripe:stripe-reporting-api
    name: Stripe Reporting API
    description: >-
      The financial reports in the Dashboard provide downloadable reports in CSV
      format for a variety of accounting and reconciliation tasks. These reports
      are also available through the API, so you can schedule them to run
      automatically or run them whenever you need to receive the associated
      report files for accounting purposes.
    tags:
      - Reporting
      - Reports
      - Runs
      - Types
    properties:
      - type: Documentation
        url: https://stripe.com/docs/reports/api
      - type: OpenAPI
        url: openapi/reporting-openapi-original.yml
  - aid: stripe:stripe-reviews-api
    name: Stripe Reviews API
    description: >-
      Reviews can be used to supplement automated fraud detection with human
      expertise.
    tags:
      - Reviews
      - Approve
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/radar/reviews
      - type: OpenAPI
        url: openapi/reviews-openapi-original.yml
  - aid: stripe:stripe-setup-api
    name: Stripe Setup API
    description: >-
      Use the Setup Intents API to set up a payment method for future payments.
      It's similar to a payment, but no charge is created. Set up a payment
      method for future payments now.
    tags:
      - Attempts
      - Setup
      - Intents
      - Intent
      - Cancel
      - Confirm
      - Microdeposits
      - Verify
    properties:
      - type: Documentation
        url: https://stripe.com/docs/payments/setup-intents
      - type: OpenAPI
        url: openapi/setup-openapi-original.yml
  - aid: stripe:stripe-shipping-rates-api
    name: Stripe Shipping Rates API
    description: >-
      Shipping rates describe the price of shipping presented to your customers
      and applied to a purchase.
    tags:
      - Rates
      - Shipping
      - Tokens
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/shipping_rates
      - type: OpenAPI
        url: openapi/shipping-rates-openapi-original.yml
  - aid: stripe:stripe-sigma-api
    name: Stripe Sigma API
    description: >-
      If you have scheduled a Sigma query, you'll receive a
      sigma.scheduled_query_run.created webhook each time the query runs. The
      webhook contains a ScheduledQueryRun object, which you can use to retrieve
      the query results.
    tags:
      - Queries
      - Runs
      - Scheduled
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/sigma/scheduled_queries
      - type: OpenAPI
        url: openapi/sigma-openapi-original.yml
  - aid: stripe:stripe-sources-api
    name: Stripe Sources API
    description: >-
      Source objects allow you to accept a variety of payment methods. They
      represent a customer's payment instrument, and can be used with the Stripe
      API just like a Card object once chargeable, they can be charged, or can
      be attached to customers.
    tags:
      - Sources
      - Mandate
      - Notifications
      - Transactions
      - Verify
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/sources
      - type: OpenAPI
        url: openapi/sources-openapi-original.yml
  - aid: stripe:stripe-subscription-api
    name: Stripe Subscription API
    description: Subscriptions allow you to charge a customer on a recurring basis.
    tags:
      - Items
      - Subscriptions
      - Record
      - Summaries
      - Usage
      - Records
      - Schedules
      - Cancel
      - Releases
      - Search
      - Exposed
      - Discount
      - Resume
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/subscriptions
      - type: OpenAPI
        url: openapi/subscription-openapi-original.yml
  - aid: stripe:stripe-tax-api
    name: Stripe Tax API
    description: >-
      Automate sales tax, VAT, and GST compliance on all your transactions-low
      or no code integrations available.
    tags:
      - Calculations
      - Taxes
      - Items
      - Line
      - Registrations
      - Settings
      - Transactions
      - Reversals
      - Codes
      - Rates
    properties:
      - type: Documentation
        url: https://stripe.com/docs/tax
      - type: OpenAPI
        url: openapi/tax-openapi-original.yml
  - aid: stripe:stripe-terminal-api
    name: Stripe Terminal API
    description: >-
      Use Stripe Terminal to accept in-person payments and extend Stripe
      payments to your point of sale.
    tags:
      - Configurations
      - Terminal
      - Connections
      - Tokens
      - Locations
      - Readers
      - Actions
      - Cancel
      - Intent
      - Payments
      - Process
      - Setup
      - Refunds
      - Display
      - Sets
    properties:
      - type: Documentation
        url: https://stripe.com/docs/terminal
      - type: OpenAPI
        url: openapi/terminal-openapi-original.yml
  - aid: stripe:stripe-test-helpers-api
    name: Stripe Test Helpers API
    description: >-
      Stripe provides a number of resources for testing your integration. Make
      sure to test the following use cases before launch, and use our Postman
      collection to make the testing process simpler.
    tags:
      - Balance
      - Cash
      - Customers
      - Funds
      - Helpers
      - Tests
      - Authorization
      - Issuing
      - Capture
      - Expire
      - Increment
      - Reverse
      - Cards
      - Deliveries
      - Shipping
      - Fail
      - Returns
      - Ship
      - Force
      - Transactions
      - Refunds
      - Unlinked
      - Methods
      - Payments
      - Present
      - Readers
      - Terminal
      - Clocks
      - Clock
      - Advance
      - Inbound
      - Transfers
      - Treasury
      - Succeed
      - Outbound
      - Posts
      - Credits
      - Received
      - Debits
    properties:
      - type: Documentation
        url: https://stripe.com/docs/implementation-guides/billing/testing
      - type: OpenAPI
        url: openapi/test-helpers-openapi-original.yml
  - aid: stripe:stripe-tokens-api
    name: Stripe Tokens API
    description: >-
      Tokenization is the process Stripe uses to collect sensitive card or bank
      account details, or personally identifiable information (PII), directly
      from your customers in a secure manner. A token representing this
      information is returned to your server to use. Use our recommended
      payments integrations to perform this process on the client-side. This
      guarantees that no sensitive card data touches your server, and allows
      your integration to operate in a PCI-compliant way.
    tags:
      - Tokens
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/tokens
      - type: OpenAPI
        url: openapi/tokens-openapi-original.yml
  - aid: stripe:stripe-topups-api
    name: Stripe Topups API
    description: >-
      To top up your Stripe balance, you create a top-up object. You can
      retrieve individual top-ups, as well as list all top-ups. Top-ups are
      identified by a unique, random ID.
    tags:
      - Topups
      - Cancel
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/topups
      - type: OpenAPI
        url: openapi/topups-openapi-original.yml
  - aid: stripe:stripe-transfers-api
    name: Stripe Transfers API
    description: >-
      A Transfer object is created when you move funds between Stripe accounts
      as part of Connect.
    tags:
      - Transfers
      - Reversals
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/transfers
      - type: OpenAPI
        url: openapi/transfers-openapi-original.yml
  - aid: stripe:stripe-treasury-api
    name: Stripe Treasury API
    description: >-
      Stripe Treasury is a banking-as-a-service API that lets you embed
      financial services in your product. With Stripe's API, you can enable
      businesses to hold funds, pay bills, earn yield, and manage their cash
      flow. Many users build Stripe Issuing in conjunction with Stripe Treasury
      to attach cards to spend funds in the account.
    tags:
      - Credit
      - Reversals
      - Treasury
      - Debit
      - Accounts
      - Financial
      - Features
      - Inbound
      - Transfers
      - Cancel
      - Outbound
      - Payments
      - Credits
      - Received
      - Debits
      - Entries
      - Transactions
    properties:
      - type: Documentation
        url: https://stripe.com/docs/treasury
      - type: OpenAPI
        url: openapi/treasury-openapi-original.yml
  - aid: stripe:stripe-webhook-api
    name: Stripe Webhook API
    description: >-
      You can configure webhook endpoints via the API to be notified about
      events that happen in your Stripe account or connected accounts.
    tags:
      - Endpoints
      - Webhooks
    properties:
      - type: Documentation
        url: https://stripe.com/docs/api/webhook_endpoints
      - type: OpenAPI
        url: openapi/webhook-openapi-original.yml
maintainers:
  - FN: APIs.json
    email: info@apis.io
common:
  - type: Sign Up
    url: https://dashboard.stripe.com/register
  - type: Authentication
    url: https://stripe.com/docs/api/authentication
  - type: Blog
    url: https://stripe.com/blog
  - type: Status
    url: https://status.stripe.com/
  - type: Change Log
    url: https://stripe.com/docs/upgrades#api-versions
  - type: Terms of Service
    url: https://stripe.com/privacy
  - type: Support
    url: https://support.stripe.com/
---