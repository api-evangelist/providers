---
aid: stripe
url: >-

  https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md
apis:
  - aid: stripe:stripe-accounts-api
    name: Stripe Accounts API
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
    overlays:
      - url: overlays/accounts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/accounts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/accounts
        type: Documentation
      - url: openapi/accounts-openapi-original.yml
        type: OpenAPI
    description: |-

      This is an object representing a Stripe account. You can retrieve it to
      see properties on the account like its current requirements or if the
      account is enabled to make live charges or receive payouts.
  - aid: stripe:stripe-apple-pay-api
    name: Stripe Apple Pay API
    tags:
      - Apple
      - Domains
      - Pay
    overlays:
      - url: overlays/apple-pay-openapi-search.yml
        type: APIs.io Search
      - url: overlays/apple-pay-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/apple-pay
        type: Documentation
      - url: openapi/apple-pay-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe users can accept Apple Pay in iOS applications in iOS 9 and above,
      and on the web in Safari starting with iOS 10 or macOS Sierra. There are
      no additional fees to process Apple Pay payments, and the pricing is the
      same as other card transactions.
  - aid: stripe:stripe-application-fees-api
    name: Stripe Application Fees API
    tags:
      - Applications
      - Fees
      - Fee
      - Refunds
    overlays:
      - url: overlays/application-fees-openapi-search.yml
        type: APIs.io Search
      - url: overlays/application-fees-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/application_fees
        type: Documentation
      - url: openapi/application-fees-openapi-original.yml
        type: OpenAPI
    description: |-

      When you collect a transaction fee on top of a charge made for your user
      (using Connect), an Application Fee object is created in your account. You
      can list, retrieve, and refund application fees.
  - aid: stripe:stripe-application-secrets-api
    name: Stripe Application Secrets API
    tags:
      - Applications
      - Secrets
      - Find
    overlays:
      - url: overlays/application-secrets-openapi-search.yml
        type: APIs.io Search
      - url: overlays/application-secrets-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/secret_management
        type: Documentation
      - url: openapi/application-secrets-openapi-original.yml
        type: OpenAPI
    description: |-

      Secret Store is an API that allows Stripe Apps developers to securely
      persist secrets for use by UI Extensions and app backends.
  - aid: stripe:stripe-balance-api
    name: Stripe Balance API
    tags:
      - Balance
      - History
      - Transactions
    overlays:
      - url: overlays/balance-openapi-search.yml
        type: APIs.io Search
      - url: overlays/balance-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/balance
        type: Documentation
      - url: openapi/balance-openapi-original.yml
        type: OpenAPI
    description: |-

      This is an object representing your Stripe balance. You can retrieve it to
      see the balance currently on your Stripe account. You can also retrieve
      the balance history, which contains a list of transactions that
      contributed to the balance (charges, payouts, and so forth).
  - aid: stripe:stripe-billing-api
    name: Stripe Billing API
    tags:
      - Billing
      - Configurations
      - Portals
      - Sessions
    overlays:
      - url: overlays/billing-openapi-search.yml
        type: APIs.io Search
      - url: overlays/billing-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/billing
        type: Documentation
      - url: openapi/billing-openapi-original.yml
        type: OpenAPI
    description: |-

      Create and manage subscriptions, recurring payments, and recurring
      revenue.
  - aid: stripe:stripe-charges-api
    name: Stripe Charges API
    tags:
      - Charges
      - Search
      - Charge
      - Capture
      - Disputes
      - Close
      - Refunds
    overlays:
      - url: overlays/charges-openapi-search.yml
        type: APIs.io Search
      - url: overlays/charges-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/charges
        type: Documentation
      - url: openapi/charges-openapi-original.yml
        type: OpenAPI
    description: |-

      The Charge object represents a single attempt to move money into your
      Stripe account. PaymentIntent confirmation is the most common way to
      create Charges, but transferring money to a different Stripe account
      through Connect also creates Charges. Some legacy payment flows create
      Charges directly, which is not recommended for new integrations.
  - aid: stripe:stripe-checkout-api
    name: Stripe Checkout API
    tags:
      - Checkout
      - Sessions
      - Expire
      - Items
      - Line
    overlays:
      - url: overlays/checkout-openapi-search.yml
        type: APIs.io Search
      - url: overlays/checkout-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/payments/checkout
        type: Documentation
      - url: openapi/checkout-openapi-original.yml
        type: OpenAPI
    description: |-

      Checkout is a low-code payment integration that creates a customizable
      form for collecting payments. You can embed Checkout directly in your
      website or redirect customers to a Stripe-hosted payment page. It supports
      one-time payments and subscriptions and accepts over 40 local payment
      methods.
  - aid: stripe:stripe-climate-api
    name: Stripe Climate API
    tags:
      - Climate
      - Orders
      - Cancel
      - Products
      - Reservations
      - Confirm
      - Suppliers
      - Supplier
    overlays:
      - url: overlays/climate-openapi-search.yml
        type: APIs.io Search
      - url: overlays/climate-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/climate
        type: Documentation
      - url: openapi/climate-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe Climate is the easiest way to help promising permanent carbon
      removal technologies launch and scale. Join a growing group of ambitious
      businesses that are changing the course of carbon removal.
  - aid: stripe:stripe-country-api
    name: Stripe Country API
    tags:
      - Countries
      - Specs
    overlays:
      - url: overlays/country-openapi-search.yml
        type: APIs.io Search
      - url: overlays/country-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/country_specs
        type: Documentation
      - url: openapi/country-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe needs to collect certain pieces of information about each account
      created. These requirements can differ depending on the account's country.
      The Country Specs API makes these rules available to your integration.
  - aid: stripe:stripe-coupons-api
    name: Stripe Coupons API
    tags:
      - Coupons
    overlays:
      - url: overlays/coupons-openapi-search.yml
        type: APIs.io Search
      - url: overlays/coupons-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/coupons
        type: Documentation
      - url: openapi/coupons-openapi-original.yml
        type: OpenAPI
    description: |-

      A coupon contains information about a percent-off or amount-off discount
      you might want to apply to a customer. Coupons may be applied to
      subscriptions, invoices, checkout sessions, quotes, and more. Coupons do
      not work with conventional one-off charges or payment intents.
  - aid: stripe:stripe-credit-notes-api
    name: Stripe Credit Notes API
    tags:
      - Credit
      - Notes
      - Previews
      - Lines
    overlays:
      - url: overlays/credit-notes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/credit-notes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/credit_notes
        type: Documentation
      - url: openapi/credit-notes-openapi-original.yml
        type: OpenAPI
    description: |-

      Issue a credit note to adjust an invoice's amount after the invoice is
      finalized.
  - aid: stripe:stripe-customers-api
    name: Stripe Customers API
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
    overlays:
      - url: overlays/customers-openapi-search.yml
        type: APIs.io Search
      - url: overlays/customers-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/customers
        type: Documentation
      - url: openapi/customers-openapi-original.yml
        type: OpenAPI
    description: |-

      This object represents a customer of your business. Use it to create
      recurring charges and track payments that belong to the same customer.
  - aid: stripe:stripe-disputes-api
    name: Stripe Disputes API
    tags:
      - Disputes
      - Close
    overlays:
      - url: overlays/disputes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/disputes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/disputes
        type: Documentation
      - url: openapi/disputes-openapi-original.yml
        type: OpenAPI
    description: |-

      A dispute occurs when a customer questions your charge with their card
      issuer. When this happens, you have the opportunity to respond to the
      dispute with evidence that shows that the charge is legitimate.
  - aid: stripe:stripe-ephemeral-keys-api
    name: Stripe Ephemeral Keys API
    tags:
      - Ephemeral
      - Keys
    overlays:
      - url: overlays/ephemeral-keys-openapi-search.yml
        type: APIs.io Search
      - url: overlays/ephemeral-keys-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/issuing/elements
        type: Documentation
      - url: openapi/ephemeral-keys-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe.js uses ephemeral keys to securely retrieve Card information from
      the Stripe API without publicly exposing your secret keys. You need to do
      some of the ephemeral key exchange on the server-side to set this up.
  - aid: stripe:stripe-events-api
    name: Stripe Events API
    tags:
      - Events
    overlays:
      - url: overlays/events-openapi-search.yml
        type: APIs.io Search
      - url: overlays/events-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/events
        type: Documentation
      - url: openapi/events-openapi-original.yml
        type: OpenAPI
    description: |-

      Events are our way of letting you know when something interesting happens
      in your account. When an interesting event occurs, we create a new Event
      object.
  - aid: stripe:stripe-exchange-rates-api
    name: Stripe Exchange Rates API
    tags:
      - Exchange
      - Rates
    overlays:
      - url: overlays/exchange-rates-openapi-search.yml
        type: APIs.io Search
      - url: overlays/exchange-rates-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/currencies/conversions
        type: Documentation
      - url: openapi/exchange-rates-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe supports processing charges in 135+ currencies allowing you to
      present prices in a customer's native currency. Doing so can improve sales
      and help customers avoid conversion costs. In order to present prices in
      your customer's currency, you need to specify the presentment currency
      when creating a PaymentIntent or a charge.
  - aid: stripe:stripe-files-api
    name: Stripe Files API
    tags:
      - Files
      - File
    overlays:
      - url: overlays/files-openapi-search.yml
        type: APIs.io Search
      - url: overlays/files-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/files
        type: Documentation
      - url: openapi/files-openapi-original.yml
        type: OpenAPI
    description: |-

      This object represents files hosted on Stripe's servers. You can upload
      files with the create file request (for example, when uploading dispute
      evidence). Stripe also creates files independently (for example, the
      results of a Sigma scheduled query).
  - aid: stripe:stripe-financial-connections-api
    name: Stripe Financial Connections API
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
    overlays:
      - url: overlays/financial-connections-openapi-search.yml
        type: APIs.io Search
      - url: overlays/financial-connections-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/financial-connections
        type: Documentation
      - url: openapi/financial-connections-openapi-original.yml
        type: OpenAPI
    description: |-

      Financial Connections lets your users securely share their financial data
      by linking their financial accounts to your business. Use Financial
      Connections to access user-permissioned account data such as tokenized
      account and routing numbers, balances, ownerships details, and
      transactions.
  - aid: stripe:stripe-identity-api
    name: Stripe Identity API
    tags:
      - Entities
      - Identity
      - Reports
      - Verification
      - Sessions
      - Cancel
      - Redact
    overlays:
      - url: overlays/identity-openapi-search.yml
        type: APIs.io Search
      - url: overlays/identity-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/identity
        type: Documentation
      - url: openapi/identity-openapi-original.yml
        type: OpenAPI
    description: |-

      Use Stripe Identity to confirm the identity of global users to prevent
      fraud, streamline risk operations, and increase trust and safety.
  - aid: stripe:stripe-invoice-api
    name: Stripe Invoice API
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
    overlays:
      - url: overlays/invoice-openapi-search.yml
        type: APIs.io Search
      - url: overlays/invoice-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/invoices
        type: Documentation
      - url: openapi/invoice-openapi-original.yml
        type: OpenAPI
    description: |-

      Invoices are statements of amounts owed by a customer, and are either
      generated one-off, or generated periodically from a subscription.
  - aid: stripe:stripe-issuing-api
    name: Stripe Issuing API
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
    overlays:
      - url: overlays/issuing-openapi-search.yml
        type: APIs.io Search
      - url: overlays/issuing-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/issuing
        type: Documentation
      - url: openapi/issuing-openapi-original.yml
        type: OpenAPI
    description: |-

      An API for businesses to instantly create, manage, and distribute payment
      cards.
  - aid: stripe:stripe-link-api
    name: Stripe Link API
    tags:
      - Accounts
      - Link
      - Sessions
      - Linked
      - Disconnect
      - Owners
      - Refresh
    overlays:
      - url: overlays/link-openapi-search.yml
        type: APIs.io Search
      - url: overlays/link-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/payment-links/api
        type: Documentation
      - url: openapi/link-openapi-original.yml
        type: OpenAPI
    description: |-

      You can use the Payment Links API to create a payment link that you can
      share with your customers. Stripe redirects customers who open this link
      to a Stripe-hosted payment page.
  - aid: stripe:stripe-payment-intents-api
    name: Stripe Payment Intents API
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
    overlays:
      - url: overlays/payment-intents-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payment-intents-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/payment_intents
        type: Documentation
      - url: openapi/payment-intents-openapi-original.yml
        type: OpenAPI
    description: |-

      A PaymentIntent guides you through the process of collecting a payment
      from your customer. We recommend that you create exactly one PaymentIntent
      for each order or customer session in your system. You can reference the
      PaymentIntent later to see the history of payment attempts for a
      particular session.
  - aid: stripe:stripe-payment-links-api
    name: Stripe Payment Links API
    tags:
      - Links
      - Payments
      - Link
      - Items
      - Line
    overlays:
      - url: overlays/payment-links-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payment-links-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/payment_links/payment_links
        type: Documentation
      - url: openapi/payment-links-openapi-original.yml
        type: OpenAPI
    description: |-

      A payment link is a shareable URL that will take your customers to a
      hosted payment page. A payment link can be shared and used multiple times.
      When a customer opens a payment link it will open a new checkout session
      to render the payment page. You can use checkout session events to track
      payments through payment links.
  - aid: stripe:stripe-payment-method-api
    name: Stripe Payment Method API
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
    overlays:
      - url: overlays/payment-method-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payment-method-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/payments/payment-methods
        type: Documentation
      - url: openapi/payment-method-openapi-original.yml
        type: OpenAPI
    description: |-

      The Payment Methods API allows you to accept a variety of payment methods
      through a single API. A PaymentMethod object contains the payment method
      details to create payments.
  - aid: stripe:stripe-payouts-api
    name: Stripe Payouts API
    tags:
      - Payouts
      - Cancel
      - Reverse
    overlays:
      - url: overlays/payouts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payouts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/payouts
        type: Documentation
      - url: openapi/payouts-openapi-original.yml
        type: OpenAPI
    description: |-

      A Payout object is created when you receive funds from Stripe, or when you
      initiate a payout to either a bank account or debit card of a connected
      Stripe account. You can retrieve individual payouts, and list all payouts.
      Payouts are made on varying schedules, depending on your country and
      industry.
  - aid: stripe:stripe-plans-api
    name: Stripe Plans API
    tags:
      - Plans
      - Plan
    overlays:
      - url: overlays/plans-openapi-search.yml
        type: APIs.io Search
      - url: overlays/plans-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/plans
        type: Documentation
      - url: openapi/plans-openapi-original.yml
        type: OpenAPI
    description: |-

      You can now model subscriptions more flexibly using the Prices API. It
      replaces the Plans API and is backwards compatible to simplify your
      migration.
  - aid: stripe:stripe-prices-api
    name: Stripe Prices API
    tags:
      - Prices
      - Search
    overlays:
      - url: overlays/prices-openapi-search.yml
        type: APIs.io Search
      - url: overlays/prices-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/prices
        type: Documentation
      - url: openapi/prices-openapi-original.yml
        type: OpenAPI
    description: |-

      Prices define the unit cost, currency, and (optional) billing cycle for
      both recurring and one-time purchases of products. Products help you track
      inventory or provisioning, and prices help you track payment terms.
      Different physical goods or levels of service should be represented by
      products, and pricing options should be represented by prices. This
      approach lets you change prices without having to change your provisioning
      scheme.
  - aid: stripe:stripe-products-api
    name: Stripe Products API
    tags:
      - Products
      - Search
    overlays:
      - url: overlays/products-openapi-search.yml
        type: APIs.io Search
      - url: overlays/products-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/products
        type: Documentation
      - url: openapi/products-openapi-original.yml
        type: OpenAPI
    description: |-

      Products describe the specific goods or services you offer to your
      customers. For example, you might offer a Standard and Premium version of
      your goods or service; each version would be a separate Product. They can
      be used in conjunction with Prices to configure pricing in Payment Links,
      Checkout, and Subscriptions.
  - aid: stripe:stripe-promotion-codes-api
    name: Stripe Promotion Codes API
    tags:
      - Codes
      - Promotion
      - Code
    overlays:
      - url: overlays/promotion-codes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/promotion-codes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/promotion_codes
        type: Documentation
      - url: openapi/promotion-codes-openapi-original.yml
        type: OpenAPI
    description: |-

      A Promotion Code represents a customer-redeemable code for a coupon. It
      can be used to create multiple codes for a single coupon.
  - aid: stripe:stripe-quotes-api
    name: Stripe Quotes API
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
    overlays:
      - url: overlays/quotes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/quotes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/quotes
        type: Documentation
      - url: openapi/quotes-openapi-original.yml
        type: OpenAPI
    description: |-

      A Quote is a way to model prices that you'd like to provide to a customer.
      Once accepted, it will automatically create an invoice, subscription or
      subscription schedule.
  - aid: stripe:stripe-radar-api
    name: Stripe Radar API
    tags:
      - Early
      - Fraud
      - Radar
      - Warnings
      - Warning
      - Items
      - Value
    overlays:
      - url: overlays/radar-openapi-search.yml
        type: APIs.io Search
      - url: overlays/radar-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/radar
        type: Documentation
      - url: openapi/radar-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe Radar provides real-time fraud protection and requires no
      additional development time. Fraud professionals can add Radar for Fraud
      Teams to customize protection and get deeper insights.
  - aid: stripe:stripe-refunds-api
    name: Stripe Refunds API
    tags:
      - Refunds
      - Cancel
    overlays:
      - url: overlays/refunds-openapi-search.yml
        type: APIs.io Search
      - url: overlays/refunds-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/refunds
        type: Documentation
      - url: openapi/refunds-openapi-original.yml
        type: OpenAPI
    description: |-

      Refund objects allow you to refund a previously created charge that isn't
      refunded yet. Funds are refunded to the credit or debit card that's
      initially charged.
  - aid: stripe:stripe-reporting-api
    name: Stripe Reporting API
    tags:
      - Reporting
      - Reports
      - Runs
      - Types
    overlays:
      - url: overlays/reporting-openapi-search.yml
        type: APIs.io Search
      - url: overlays/reporting-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/reports/api
        type: Documentation
      - url: openapi/reporting-openapi-original.yml
        type: OpenAPI
    description: |-

      The financial reports in the Dashboard provide downloadable reports in CSV
      format for a variety of accounting and reconciliation tasks. These reports
      are also available through the API, so you can schedule them to run
      automatically or run them whenever you need to receive the associated
      report files for accounting purposes.
  - aid: stripe:stripe-reviews-api
    name: Stripe Reviews API
    tags:
      - Reviews
      - Approve
    overlays:
      - url: overlays/reviews-openapi-search.yml
        type: APIs.io Search
      - url: overlays/reviews-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/radar/reviews
        type: Documentation
      - url: openapi/reviews-openapi-original.yml
        type: OpenAPI
    description: |-

      Reviews can be used to supplement automated fraud detection with human
      expertise.
  - aid: stripe:stripe-setup-api
    name: Stripe Setup API
    tags:
      - Attempts
      - Setup
      - Intents
      - Intent
      - Cancel
      - Confirm
      - Microdeposits
      - Verify
    overlays:
      - url: overlays/setup-openapi-search.yml
        type: APIs.io Search
      - url: overlays/setup-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/payments/setup-intents
        type: Documentation
      - url: openapi/setup-openapi-original.yml
        type: OpenAPI
    description: |-

      Use the Setup Intents API to set up a payment method for future payments.
      It's similar to a payment, but no charge is created. Set up a payment
      method for future payments now.
  - aid: stripe:stripe-shipping-rates-api
    name: Stripe Shipping Rates API
    tags:
      - Rates
      - Shipping
      - Tokens
    overlays:
      - url: overlays/shipping-rates-openapi-search.yml
        type: APIs.io Search
      - url: overlays/shipping-rates-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/shipping_rates
        type: Documentation
      - url: openapi/shipping-rates-openapi-original.yml
        type: OpenAPI
    description: |-

      Shipping rates describe the price of shipping presented to your customers
      and applied to a purchase.
  - aid: stripe:stripe-sigma-api
    name: Stripe Sigma API
    tags:
      - Queries
      - Runs
      - Scheduled
    overlays:
      - url: overlays/sigma-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sigma-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/sigma/scheduled_queries
        type: Documentation
      - url: openapi/sigma-openapi-original.yml
        type: OpenAPI
    description: |-

      If you have scheduled a Sigma query, you'll receive a
      sigma.scheduled_query_run.created webhook each time the query runs. The
      webhook contains a ScheduledQueryRun object, which you can use to retrieve
      the query results.
  - aid: stripe:stripe-sources-api
    name: Stripe Sources API
    tags:
      - Sources
      - Mandate
      - Notifications
      - Transactions
      - Verify
    overlays:
      - url: overlays/sources-openapi-search.yml
        type: APIs.io Search
      - url: overlays/sources-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/sources
        type: Documentation
      - url: openapi/sources-openapi-original.yml
        type: OpenAPI
    description: |-

      Source objects allow you to accept a variety of payment methods. They
      represent a customer's payment instrument, and can be used with the Stripe
      API just like a Card object once chargeable, they can be charged, or can
      be attached to customers.
  - aid: stripe:stripe-subscription-api
    name: Stripe Subscription API
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
    overlays:
      - url: overlays/subscription-openapi-search.yml
        type: APIs.io Search
      - url: overlays/subscription-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/subscriptions
        type: Documentation
      - url: openapi/subscription-openapi-original.yml
        type: OpenAPI
    description: Subscriptions allow you to charge a customer on a recurring basis.
  - aid: stripe:stripe-tax-api
    name: Stripe Tax API
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
    overlays:
      - url: overlays/tax-openapi-search.yml
        type: APIs.io Search
      - url: overlays/tax-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/tax
        type: Documentation
      - url: openapi/tax-openapi-original.yml
        type: OpenAPI
    description: |-

      Automate sales tax, VAT, and GST compliance on all your transactions-low
      or no code integrations available.
  - aid: stripe:stripe-terminal-api
    name: Stripe Terminal API
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
    overlays:
      - url: overlays/terminal-openapi-search.yml
        type: APIs.io Search
      - url: overlays/terminal-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/terminal
        type: Documentation
      - url: openapi/terminal-openapi-original.yml
        type: OpenAPI
    description: |-

      Use Stripe Terminal to accept in-person payments and extend Stripe
      payments to your point of sale.
  - aid: stripe:stripe-test-helpers-api
    name: Stripe Test Helpers API
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
    overlays:
      - url: overlays/test-helpers-openapi-search.yml
        type: APIs.io Search
      - url: overlays/test-helpers-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/implementation-guides/billing/testing
        type: Documentation
      - url: openapi/test-helpers-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe provides a number of resources for testing your integration. Make
      sure to test the following use cases before launch, and use our Postman
      collection to make the testing process simpler.
  - aid: stripe:stripe-tokens-api
    name: Stripe Tokens API
    tags:
      - Tokens
    overlays:
      - url: overlays/tokens-openapi-search.yml
        type: APIs.io Search
      - url: overlays/tokens-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/tokens
        type: Documentation
      - url: openapi/tokens-openapi-original.yml
        type: OpenAPI
    description: |-

      Tokenization is the process Stripe uses to collect sensitive card or bank
      account details, or personally identifiable information (PII), directly
      from your customers in a secure manner. A token representing this
      information is returned to your server to use. Use our recommended
      payments integrations to perform this process on the client-side. This
      guarantees that no sensitive card data touches your server, and allows
      your integration to operate in a PCI-compliant way.
  - aid: stripe:stripe-topups-api
    name: Stripe Topups API
    tags:
      - Topups
      - Cancel
    overlays:
      - url: overlays/topups-openapi-search.yml
        type: APIs.io Search
      - url: overlays/topups-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/topups
        type: Documentation
      - url: openapi/topups-openapi-original.yml
        type: OpenAPI
    description: |-

      To top up your Stripe balance, you create a top-up object. You can
      retrieve individual top-ups, as well as list all top-ups. Top-ups are
      identified by a unique, random ID.
  - aid: stripe:stripe-transfers-api
    name: Stripe Transfers API
    tags:
      - Transfers
      - Reversals
    overlays:
      - url: overlays/transfers-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transfers-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/transfers
        type: Documentation
      - url: openapi/transfers-openapi-original.yml
        type: OpenAPI
    description: |-

      A Transfer object is created when you move funds between Stripe accounts
      as part of Connect.
  - aid: stripe:stripe-treasury-api
    name: Stripe Treasury API
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
    overlays:
      - url: overlays/treasury-openapi-search.yml
        type: APIs.io Search
      - url: overlays/treasury-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/treasury
        type: Documentation
      - url: openapi/treasury-openapi-original.yml
        type: OpenAPI
    description: |-

      Stripe Treasury is a banking-as-a-service API that lets you embed
      financial services in your product. With Stripe's API, you can enable
      businesses to hold funds, pay bills, earn yield, and manage their cash
      flow. Many users build Stripe Issuing in conjunction with Stripe Treasury
      to attach cards to spend funds in the account.
  - aid: stripe:stripe-webhook-api
    name: Stripe Webhook API
    tags:
      - Endpoints
      - Webhooks
    overlays:
      - url: overlays/webhook-openapi-search.yml
        type: APIs.io Search
      - url: overlays/webhook-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: https://stripe.com/docs/api/webhook_endpoints
        type: Documentation
      - url: openapi/webhook-openapi-original.yml
        type: OpenAPI
    description: |-

      You can configure webhook endpoints via the API to be notified about
      events that happen in your Stripe account or connected accounts.
name: Stripe
tags: []
common:
  - url: https://dashboard.stripe.com/register
    type: Sign Up
  - url: https://stripe.com/docs/api/authentication
    type: Authentication
  - url: https://stripe.com/blog
    type: Blog
  - url: https://status.stripe.com/
    type: Status
  - url: https://stripe.com/docs/upgrades#api-versions
    type: Change Log
  - url: https://stripe.com/privacy
    type: Terms of Service
  - url: https://support.stripe.com/
    type: Support
created: 2024/04/14
modified: '2024-07-03T00:00:00.000Z'
description: |-

  Millions of companies of all sizes use Stripe online and in person to accept
  payments, send payouts, automate financial processes, and ultimately grow
  revenue.
maintainers:
  - FN: APIs.json
    email: info@apis.io
specificationVersion: '0.18'

---