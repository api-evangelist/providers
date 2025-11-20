---
aid: stripe
url: >-
  https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md
apis:
  - aid: stripe:stripe-accounts-api
    name: Stripe Accounts API
    tags:
      - Accounts
    properties:
      - url: https://stripe.com/docs/api/accounts
        type: Documentation
      - url: properties/stripe-accounts-api-openapi.yml
        type: OpenAPI
    description: >-
      This is an object representing a Stripe account. You can retrieve it to
      see properties on the account like its current requirements or if the
      account is enabled to make live charges or receive payouts.
  - aid: stripe:stripe-apple-pay-api
    name: Stripe Apple Pay API
    tags:
      - Apple
      - Apply Pay
      - Payments
    properties:
      - url: https://stripe.com/docs/apple-pay
        type: Documentation
      - url: openapi/apple-pay-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe users can accept Apple Pay in iOS applications in iOS 9 and above,
      and on the web in Safari starting with iOS 10 or macOS Sierra. There are
      no additional fees to process Apple Pay payments, and the pricing is the
      same as other card transactions.
  - aid: stripe:stripe-application-fees-api
    name: Stripe Application Fees API
    tags:
      - Applications
      - Fees
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/application_fees
        type: Documentation
      - url: openapi/application-fees-openapi-original.yml
        type: OpenAPI
    description: >-
      When you collect a transaction fee on top of a charge made for your user
      (using Connect), an Application Fee object is created in your account. You
      can list, retrieve, and refund application fees.
  - aid: stripe:stripe-application-secrets-api
    name: Stripe Application Secrets API
    tags:
      - Applications
      - Secrets
    properties:
      - url: https://stripe.com/docs/api/secret_management
        type: Documentation
      - url: openapi/application-secrets-openapi-original.yml
        type: OpenAPI
    description: >-
      Secret Store is an API that allows Stripe Apps developers to securely
      persist secrets for use by UI Extensions and app backends.
  - aid: stripe:stripe-balance-api
    name: Stripe Balance API
    tags:
      - Balance
      - History
      - Transactions
    properties:
      - url: https://stripe.com/docs/api/balance
        type: Documentation
      - url: openapi/balance-openapi-original.yml
        type: OpenAPI
    description: >-
      This is an object representing your Stripe balance. You can retrieve it to
      see the balance currently on your Stripe account. You can also retrieve
      the balance history, which contains a list of transactions that
      contributed to the balance (charges, payouts, and so forth).
  - aid: stripe:stripe-billing-api
    name: Stripe Billing API
    tags:
      - Billing
    properties:
      - url: https://stripe.com/docs/billing
        type: Documentation
      - url: openapi/billing-openapi-original.yml
        type: OpenAPI
    description: >-
      Create and manage subscriptions, recurring payments, and recurring
      revenue.
  - aid: stripe:stripe-charges-api
    name: Stripe Charges API
    tags:
      - Charges
      - Disputes
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/charges
        type: Documentation
      - url: openapi/charges-openapi-original.yml
        type: OpenAPI
    description: >-
      The Charge object represents a single attempt to move money into your
      Stripe account. PaymentIntent confirmation is the most common way to
      create Charges, but transferring money to a different Stripe account
      through Connect also creates Charges. Some legacy payment flows create
      Charges directly, which is not recommended for new integrations.
  - aid: stripe:stripe-checkout-api
    name: Stripe Checkout API
    tags:
      - Checkout
    properties:
      - url: https://stripe.com/docs/payments/checkout
        type: Documentation
      - url: openapi/checkout-openapi-original.yml
        type: OpenAPI
    description: >-
      Checkout is a low-code payment integration that creates a customizable
      form for collecting payments. You can embed Checkout directly in your
      website or redirect customers to a Stripe-hosted payment page. It supports
      one-time payments and subscriptions and accepts over 40 local payment
      methods.
  - aid: stripe:stripe-climate-api
    name: Stripe Climate API
    tags:
      - Climate
      - Carbon
    properties:
      - url: https://stripe.com/climate
        type: Documentation
      - url: openapi/climate-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe Climate is the easiest way to help promising permanent carbon
      removal technologies launch and scale. Join a growing group of ambitious
      businesses that are changing the course of carbon removal.
  - aid: stripe:stripe-country-api
    name: Stripe Country API
    tags:
      - Countries
    properties:
      - url: https://stripe.com/docs/api/country_specs
        type: Documentation
      - url: openapi/country-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe needs to collect certain pieces of information about each account
      created. These requirements can differ depending on the account's country.
      The Country Specs API makes these rules available to your integration.
  - aid: stripe:stripe-coupons-api
    name: Stripe Coupons API
    tags:
      - Coupons
    properties:
      - url: https://stripe.com/docs/api/coupons
        type: Documentation
      - url: openapi/coupons-openapi-original.yml
        type: OpenAPI
    description: >-
      A coupon contains information about a percent-off or amount-off discount
      you might want to apply to a customer. Coupons may be applied to
      subscriptions, invoices, checkout sessions, quotes, and more. Coupons do
      not work with conventional one-off charges or payment intents.
  - aid: stripe:stripe-credit-notes-api
    name: Stripe Credit Notes API
    tags:
      - Credit
      - Notes
    properties:
      - url: https://stripe.com/docs/api/credit_notes
        type: Documentation
      - url: openapi/credit-notes-openapi-original.yml
        type: OpenAPI
    description: >-
      Issue a credit note to adjust an invoice's amount after the invoice is
      finalized.
  - aid: stripe:stripe-customers-api
    name: Stripe Customers API
    tags:
      - Customers
    properties:
      - url: https://stripe.com/docs/api/customers
        type: Documentation
      - url: openapi/customers-openapi-original.yml
        type: OpenAPI
    description: >-
      This object represents a customer of your business. Use it to create
      recurring charges and track payments that belong to the same customer.
  - aid: stripe:stripe-disputes-api
    name: Stripe Disputes API
    tags:
      - Disputes
    properties:
      - url: https://stripe.com/docs/api/disputes
        type: Documentation
      - url: openapi/disputes-openapi-original.yml
        type: OpenAPI
    description: >-
      A dispute occurs when a customer questions your charge with their card
      issuer. When this happens, you have the opportunity to respond to the
      dispute with evidence that shows that the charge is legitimate.
  - aid: stripe:stripe-ephemeral-keys-api
    name: Stripe Ephemeral Keys API
    tags:
      - Ephemeral
      - Keys
    properties:
      - url: https://stripe.com/docs/issuing/elements
        type: Documentation
      - url: openapi/ephemeral-keys-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe.js uses ephemeral keys to securely retrieve Card information from
      the Stripe API without publicly exposing your secret keys. You need to do
      some of the ephemeral key exchange on the server-side to set this up.
  - aid: stripe:stripe-events-api
    name: Stripe Events API
    tags:
      - Events
    properties:
      - url: https://stripe.com/docs/api/events
        type: Documentation
      - url: openapi/events-openapi-original.yml
        type: OpenAPI
    description: >-
      Events are our way of letting you know when something interesting happens
      in your account. When an interesting event occurs, we create a new Event
      object.
  - aid: stripe:stripe-exchange-rates-api
    name: Stripe Exchange Rates API
    tags:
      - Rates
      - Exchanges
    properties:
      - url: https://stripe.com/docs/currencies/conversions
        type: Documentation
      - url: openapi/exchange-rates-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe supports processing charges in 135+ currencies allowing you to
      present prices in a customer's native currency. Doing so can improve sales
      and help customers avoid conversion costs. In order to present prices in
      your customer's currency, you need to specify the presentment currency
      when creating a PaymentIntent or a charge.
  - aid: stripe:stripe-files-api
    name: Stripe Files API
    tags:
      - Files
    properties:
      - url: https://stripe.com/docs/api/files
        type: Documentation
      - url: openapi/files-openapi-original.yml
        type: OpenAPI
    description: >-
      This object represents files hosted on Stripe's servers. You can upload
      files with the create file request (for example, when uploading dispute
      evidence). Stripe also creates files independently (for example, the
      results of a Sigma scheduled query).
  - aid: stripe:stripe-financial-connections-api
    name: Stripe Financial Connections API
    tags:
      - Connections
      - Financial
    properties:
      - url: https://stripe.com/docs/financial-connections
        type: Documentation
      - url: openapi/financial-connections-openapi-original.yml
        type: OpenAPI
    description: >-
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
    properties:
      - url: https://stripe.com/docs/identity
        type: Documentation
      - url: openapi/identity-openapi-original.yml
        type: OpenAPI
    description: >-
      Use Stripe Identity to confirm the identity of global users to prevent
      fraud, streamline risk operations, and increase trust and safety.
  - aid: stripe:stripe-invoice-api
    name: Stripe Invoice API
    tags:
      - Invoices
    properties:
      - url: https://stripe.com/docs/api/invoices
        type: Documentation
      - url: openapi/invoice-openapi-original.yml
        type: OpenAPI
    description: >-
      Invoices are statements of amounts owed by a customer, and are either
      generated one-off, or generated periodically from a subscription.
  - aid: stripe:stripe-issuing-api
    name: Stripe Issuing API
    tags:
      - Issuing
      - Cards
    properties:
      - url: https://stripe.com/docs/issuing
        type: Documentation
      - url: openapi/issuing-openapi-original.yml
        type: OpenAPI
    description: >-
      An API for businesses to instantly create, manage, and distribute payment
      cards.
  - aid: stripe:stripe-link-api
    name: Stripe Link API
    tags:
      - Payments
      - Links
    properties:
      - url: https://stripe.com/docs/payment-links/api
        type: Documentation
      - url: openapi/link-openapi-original.yml
        type: OpenAPI
    description: >-
      You can use the Payment Links API to create a payment link that you can
      share with your customers. Stripe redirects customers who open this link
      to a Stripe-hosted payment page.
  - aid: stripe:stripe-payment-intents-api
    name: Stripe Payment Intents API
    tags:
      - Intents
      - Payments
      - Intent
    properties:
      - url: https://stripe.com/docs/api/payment_intents
        type: Documentation
      - url: openapi/payment-intents-openapi-original.yml
        type: OpenAPI
    description: >-
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
    properties:
      - url: https://stripe.com/docs/api/payment_links/payment_links
        type: Documentation
      - url: openapi/payment-links-openapi-original.yml
        type: OpenAPI
    description: >-
      A payment link is a shareable URL that will take your customers to a
      hosted payment page. A payment link can be shared and used multiple times.
      When a customer opens a payment link it will open a new checkout session
      to render the payment page. You can use checkout session events to track
      payments through payment links.
  - aid: stripe:stripe-payment-method-api
    name: Stripe Payment Method API
    tags:
      - Methods
      - Payments
      - Detach
    properties:
      - url: https://stripe.com/docs/payments/payment-methods
        type: Documentation
      - url: openapi/payment-method-openapi-original.yml
        type: OpenAPI
    description: >-
      The Payment Methods API allows you to accept a variety of payment methods
      through a single API. A PaymentMethod object contains the payment method
      details to create payments.
  - aid: stripe:stripe-payouts-api
    name: Stripe Payouts API
    tags:
      - Payouts
    properties:
      - url: https://stripe.com/docs/api/payouts
        type: Documentation
      - url: openapi/payouts-openapi-original.yml
        type: OpenAPI
    description: >-
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
    properties:
      - url: https://stripe.com/docs/api/plans
        type: Documentation
      - url: openapi/plans-openapi-original.yml
        type: OpenAPI
    description: >-
      You can now model subscriptions more flexibly using the Prices API. It
      replaces the Plans API and is backwards compatible to simplify your
      migration.
  - aid: stripe:stripe-prices-api
    name: Stripe Prices API
    tags:
      - Prices
    properties:
      - url: https://stripe.com/docs/api/prices
        type: Documentation
      - url: openapi/prices-openapi-original.yml
        type: OpenAPI
    description: >-
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
    properties:
      - url: https://stripe.com/docs/api/products
        type: Documentation
      - url: openapi/products-openapi-original.yml
        type: OpenAPI
    description: >-
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
      - Promotions
    properties:
      - url: https://stripe.com/docs/api/promotion_codes
        type: Documentation
      - url: openapi/promotion-codes-openapi-original.yml
        type: OpenAPI
    description: >-
      A Promotion Code represents a customer-redeemable code for a coupon. It
      can be used to create multiple codes for a single coupon.
  - aid: stripe:stripe-quotes-api
    name: Stripe Quotes API
    tags:
      - Quotes
    properties:
      - url: https://stripe.com/docs/api/quotes
        type: Documentation
      - url: openapi/quotes-openapi-original.yml
        type: OpenAPI
    description: >-
      A Quote is a way to model prices that you'd like to provide to a customer.
      Once accepted, it will automatically create an invoice, subscription or
      subscription schedule.
  - aid: stripe:stripe-radar-api
    name: Stripe Radar API
    tags:
      - Fraud
      - Radar
    properties:
      - url: https://stripe.com/docs/radar
        type: Documentation
      - url: openapi/radar-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe Radar provides real-time fraud protection and requires no
      additional development time. Fraud professionals can add Radar for Fraud
      Teams to customize protection and get deeper insights.
  - aid: stripe:stripe-refunds-api
    name: Stripe Refunds API
    tags:
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/refunds
        type: Documentation
      - url: openapi/refunds-openapi-original.yml
        type: OpenAPI
    description: >-
      Refund objects allow you to refund a previously created charge that isn't
      refunded yet. Funds are refunded to the credit or debit card that's
      initially charged.
  - aid: stripe:stripe-reporting-api
    name: Stripe Reporting API
    tags:
      - Reporting
      - Reports
    properties:
      - url: https://stripe.com/docs/reports/api
        type: Documentation
      - url: openapi/reporting-openapi-original.yml
        type: OpenAPI
    description: >-
      The financial reports in the Dashboard provide downloadable reports in CSV
      format for a variety of accounting and reconciliation tasks. These reports
      are also available through the API, so you can schedule them to run
      automatically or run them whenever you need to receive the associated
      report files for accounting purposes.
  - aid: stripe:stripe-reviews-api
    name: Stripe Reviews API
    tags:
      - Reviews
    properties:
      - url: https://stripe.com/docs/api/radar/reviews
        type: Documentation
      - url: openapi/reviews-openapi-original.yml
        type: OpenAPI
    description: >-
      Reviews can be used to supplement automated fraud detection with human
      expertise.
  - aid: stripe:stripe-setup-api
    name: Stripe Setup API
    tags:
      - Setup
      - Intents
      - Intent
    properties:
      - url: https://stripe.com/docs/payments/setup-intents
        type: Documentation
      - url: openapi/setup-openapi-original.yml
        type: OpenAPI
    description: >-
      Use the Setup Intents API to set up a payment method for future payments.
      It's similar to a payment, but no charge is created. Set up a payment
      method for future payments now.
  - aid: stripe:stripe-shipping-rates-api
    name: Stripe Shipping Rates API
    tags:
      - Rates
      - Shipping
    properties:
      - url: https://stripe.com/docs/api/shipping_rates
        type: Documentation
      - url: openapi/shipping-rates-openapi-original.yml
        type: OpenAPI
    description: >-
      Shipping rates describe the price of shipping presented to your customers
      and applied to a purchase.
  - aid: stripe:stripe-sigma-api
    name: Stripe Sigma API
    tags:
      - Sigma
    properties:
      - url: https://stripe.com/docs/api/sigma/scheduled_queries
        type: Documentation
      - url: openapi/sigma-openapi-original.yml
        type: OpenAPI
    description: >-
      If you have scheduled a Sigma query, you'll receive a
      sigma.scheduled_query_run.created webhook each time the query runs. The
      webhook contains a ScheduledQueryRun object, which you can use to retrieve
      the query results.
  - aid: stripe:stripe-sources-api
    name: Stripe Sources API
    tags:
      - Sources
      - Transactions
    properties:
      - url: https://stripe.com/docs/api/sources
        type: Documentation
      - url: openapi/sources-openapi-original.yml
        type: OpenAPI
    description: >-
      Source objects allow you to accept a variety of payment methods. They
      represent a customer's payment instrument, and can be used with the Stripe
      API just like a Card object once chargeable, they can be charged, or can
      be attached to customers.
  - aid: stripe:stripe-subscription-api
    name: Stripe Subscription API
    tags:
      - Subscriptions
      - Recurring
    properties:
      - url: https://stripe.com/docs/api/subscriptions
        type: Documentation
      - url: openapi/subscription-openapi-original.yml
        type: OpenAPI
    description: Subscriptions allow you to charge a customer on a recurring basis.
  - aid: stripe:stripe-tax-api
    name: Stripe Tax API
    tags:
      - Taxes
    properties:
      - url: https://stripe.com/docs/tax
        type: Documentation
      - url: openapi/tax-openapi-original.yml
        type: OpenAPI
    description: >-
      Automate sales tax, VAT, and GST compliance on all your transactions-low
      or no code integrations available.
  - aid: stripe:stripe-terminal-api
    name: Stripe Terminal API
    tags:
      - Terminal
      - Terminals
      - Point of Sale
    properties:
      - url: https://stripe.com/docs/terminal
        type: Documentation
      - url: openapi/terminal-openapi-original.yml
        type: OpenAPI
    description: >-
      Use Stripe Terminal to accept in-person payments and extend Stripe
      payments to your point of sale.
  - aid: stripe:stripe-test-helpers-api
    name: Stripe Test Helpers API
    tags:
      - Synthetic
      - Virtualization
      - Testing
    properties:
      - url: https://stripe.com/docs/implementation-guides/billing/testing
        type: Documentation
      - url: openapi/test-helpers-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe provides a number of resources for testing your integration. Make
      sure to test the following use cases before launch, and use our Postman
      collection to make the testing process simpler.
  - aid: stripe:stripe-tokens-api
    name: Stripe Tokens API
    tags:
      - Tokens
    properties:
      - url: https://stripe.com/docs/api/tokens
        type: Documentation
      - url: openapi/tokens-openapi-original.yml
        type: OpenAPI
    description: >-
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
    properties:
      - url: https://stripe.com/docs/api/topups
        type: Documentation
      - url: openapi/topups-openapi-original.yml
        type: OpenAPI
    description: >-
      To top up your Stripe balance, you create a top-up object. You can
      retrieve individual top-ups, as well as list all top-ups. Top-ups are
      identified by a unique, random ID.
  - aid: stripe:stripe-transfers-api
    name: Stripe Transfers API
    tags:
      - Transfers
    properties:
      - url: https://stripe.com/docs/api/transfers
        type: Documentation
      - url: openapi/transfers-openapi-original.yml
        type: OpenAPI
    description: >-
      A Transfer object is created when you move funds between Stripe accounts
      as part of Connect.
  - aid: stripe:stripe-treasury-api
    name: Stripe Treasury API
    tags:
      - Treasury
    properties:
      - url: https://stripe.com/docs/treasury
        type: Documentation
      - url: openapi/treasury-openapi-original.yml
        type: OpenAPI
    description: >-
      Stripe Treasury is a banking-as-a-service API that lets you embed
      financial services in your product. With Stripe's API, you can enable
      businesses to hold funds, pay bills, earn yield, and manage their cash
      flow. Many users build Stripe Issuing in conjunction with Stripe Treasury
      to attach cards to spend funds in the account.
  - aid: stripe:stripe-webhook-api
    name: Stripe Webhook API
    tags:
      - Webhooks
    properties:
      - url: https://stripe.com/docs/api/webhook_endpoints
        type: Documentation
      - url: openapi/webhook-openapi-original.yml
        type: OpenAPI
    description: >-
      You can configure webhook endpoints via the API to be notified about
      events that happen in your Stripe account or connected accounts.
name: Stripe
tags:
  - Payments
  - T1
type: Contract
access: 3rd-Party
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
modified: '2025-10-17'
position: Consuming
description: >-
  Stripe is a technology company that provides a platform for online payment
  processing. They offer a secure and seamless way for businesses to accept
  payments from customers, handling transactions in multiple currencies and
  payment methods. Stripe's software and APIs make it easy for businesses of all
  sizes to manage their online payments, track transactions, and analyze their
  revenue streams. With features such as fraud prevention, subscription billing,
  and mobile payment options, Stripe is a valuable tool for e-commerce
  businesses looking to streamline their payment processes and provide a better
  user experience for their customers.
maintainers:
  - FN: APIs.json
    email: info@apis.io
specificationVersion: '0.18'
---