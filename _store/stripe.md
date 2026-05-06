---
aid: stripe
url: https://raw.githubusercontent.com/api-search/payments/main/_apis/stripe/apis.md
apis:
  - aid: stripe:stripe-accounts-api
    name: Stripe Accounts API
    tags:
      - Accounts
    properties:
      - url: https://stripe.com/docs/api/accounts
        type: Documentation
      - url: https://docs.stripe.com/api/accounts
        type: API Reference
      - url: properties/stripe-accounts-api-openapi.yml
        type: OpenAPI
    description: This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.
  - aid: stripe:stripe-apple-pay-api
    name: Stripe Apple Pay API
    tags:
      - Apple
      - Apply Pay
      - Payments
    properties:
      - url: https://stripe.com/docs/apple-pay
        type: Documentation
      - url: properties/stripe-apple-pay-api-openapi.yml
        type: OpenAPI
    description: Stripe users can accept Apple Pay in iOS applications in iOS 9 and above, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the pricing is the same as other card transactions.
  - aid: stripe:stripe-application-fees-api
    name: Stripe Application Fees API
    tags:
      - Applications
      - Fees
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/application_fees
        type: Documentation
      - url: https://docs.stripe.com/api/application_fees
        type: API Reference
      - url: properties/stripe-application-fees-api-openapi.yml
        type: OpenAPI
    description: When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.
  - aid: stripe:stripe-application-secrets-api
    name: Stripe Application Secrets API
    tags:
      - Applications
      - Secrets
    properties:
      - url: https://stripe.com/docs/api/secret_management
        type: Documentation
      - url: openapi/stripe-application-secrets-api-openapi.yml
        type: OpenAPI
    description: Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.
  - aid: stripe:stripe-balance-api
    name: Stripe Balance API
    tags:
      - Balance
      - History
      - Transactions
    properties:
      - url: https://stripe.com/docs/api/balance
        type: Documentation
      - url: https://docs.stripe.com/api/balance
        type: API Reference
      - url: openapi/stripe-balance-api-openapi.yml
        type: OpenAPI
    description: This is an object representing your Stripe balance. You can retrieve it to see the balance currently on your Stripe account. You can also retrieve the balance history, which contains a list of transactions that contributed to the balance (charges, payouts, and so forth).
  - aid: stripe:stripe-billing-api
    name: Stripe Billing API
    tags:
      - Billing
    properties:
      - url: https://stripe.com/docs/billing
        type: Documentation
      - url: openapi/stripe-billing-api-openapi.yml
        type: OpenAPI
    description: Create and manage subscriptions, recurring payments, and recurring revenue.
  - aid: stripe:stripe-charges-api
    name: Stripe Charges API
    tags:
      - Charges
      - Disputes
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/charges
        type: Documentation
      - url: https://docs.stripe.com/api/charges
        type: API Reference
      - url: openapi/stripe-charges-api-openapi.yml
        type: OpenAPI
    description: The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe account through Connect also creates Charges. Some legacy payment flows create Charges directly, which is not recommended for new integrations.
  - aid: stripe:stripe-checkout-api
    name: Stripe Checkout API
    tags:
      - Checkout
    properties:
      - url: https://stripe.com/docs/payments/checkout
        type: Documentation
      - url: openapi/stripe-checkout-api-openapi.yml
        type: OpenAPI
    description: Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment page. It supports one-time payments and subscriptions and accepts over 40 local payment methods.
  - aid: stripe:stripe-climate-api
    name: Stripe Climate API
    tags:
      - Carbon
      - Climate
    properties:
      - url: https://stripe.com/climate
        type: Documentation
      - url: openapi/stripe-climate-api-openapi.yml
        type: OpenAPI
    description: Stripe Climate is the easiest way to help promising permanent carbon removal technologies launch and scale. Join a growing group of ambitious businesses that are changing the course of carbon removal.
  - aid: stripe:stripe-country-api
    name: Stripe Country API
    tags:
      - Countries
    properties:
      - url: https://stripe.com/docs/api/country_specs
        type: Documentation
      - url: openapi/stripe-country-api-openapi.yml
        type: OpenAPI
    description: Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account's country. The Country Specs API makes these rules available to your integration.
  - aid: stripe:stripe-coupons-api
    name: Stripe Coupons API
    tags:
      - Coupons
    properties:
      - url: https://stripe.com/docs/api/coupons
        type: Documentation
      - url: openapi/stripe-coupons-api-openapi.yml
        type: OpenAPI
    description: A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.
  - aid: stripe:stripe-credit-notes-api
    name: Stripe Credit Notes API
    tags:
      - Credit
      - Notes
    properties:
      - url: https://stripe.com/docs/api/credit_notes
        type: Documentation
      - url: openapi/stripe-credit-notes-api-openapi.yml
        type: OpenAPI
    description: Issue a credit note to adjust an invoice's amount after the invoice is finalized.
  - aid: stripe:stripe-customers-api
    name: Stripe Customers API
    tags:
      - Customers
    properties:
      - url: https://stripe.com/docs/api/customers
        type: Documentation
      - url: https://docs.stripe.com/api/customers
        type: API Reference
      - url: openapi/stripe-customers-api-openapi.yml
        type: OpenAPI
    description: This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.
  - aid: stripe:stripe-disputes-api
    name: Stripe Disputes API
    tags:
      - Disputes
    properties:
      - url: https://stripe.com/docs/api/disputes
        type: Documentation
      - url: https://docs.stripe.com/api/disputes
        type: API Reference
      - url: openapi/stripe-disputes-api-openapi.yml
        type: OpenAPI
    description: A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.
  - aid: stripe:stripe-ephemeral-keys-api
    name: Stripe Ephemeral Keys API
    tags:
      - Ephemeral
      - Keys
    properties:
      - url: https://stripe.com/docs/issuing/elements
        type: Documentation
      - url: openapi/stripe-ephemeral-keys-api-openapi.yml
        type: OpenAPI
    description: Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side to set this up.
  - aid: stripe:stripe-events-api
    name: Stripe Events API
    tags:
      - Events
    properties:
      - url: https://stripe.com/docs/api/events
        type: Documentation
      - url: https://docs.stripe.com/api/events
        type: API Reference
      - url: openapi/stripe-events-api-openapi.yml
        type: OpenAPI
    description: Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object.
  - aid: stripe:stripe-exchange-rates-api
    name: Stripe Exchange Rates API
    tags:
      - Exchanges
      - Rates
    properties:
      - url: https://stripe.com/docs/currencies/conversions
        type: Documentation
      - url: openapi/stripe-exchange-rates-api-openapi.yml
        type: OpenAPI
    description: Stripe supports processing charges in 135+ currencies allowing you to present prices in a customer's native currency. Doing so can improve sales and help customers avoid conversion costs. In order to present prices in your customer's currency, you need to specify the presentment currency when creating a PaymentIntent or a charge.
  - aid: stripe:stripe-files-api
    name: Stripe Files API
    tags:
      - Files
    properties:
      - url: https://stripe.com/docs/api/files
        type: Documentation
      - url: https://docs.stripe.com/api/files
        type: API Reference
      - url: openapi/stripe-files-api-openapi.yml
        type: OpenAPI
    description: This object represents files hosted on Stripe's servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).
  - aid: stripe:stripe-financial-connections-api
    name: Stripe Financial Connections API
    tags:
      - Connections
      - Financial
    properties:
      - url: https://stripe.com/docs/financial-connections
        type: Documentation
      - url: openapi/stripe-financial-connections-api-openapi.yml
        type: OpenAPI
    description: Financial Connections lets your users securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access user-permissioned account data such as tokenized account and routing numbers, balances, ownerships details, and transactions.
  - aid: stripe:stripe-identity-api
    name: Stripe Identity API
    tags:
      - Cancel
      - Entities
      - Identity
      - Redact
      - Reports
      - Sessions
      - Verification
    properties:
      - url: https://stripe.com/docs/identity
        type: Documentation
      - url: openapi/stripe-identity-api-openapi.yml
        type: OpenAPI
    description: Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety.
  - aid: stripe:stripe-invoice-api
    name: Stripe Invoice API
    tags:
      - Invoices
    properties:
      - url: https://stripe.com/docs/api/invoices
        type: Documentation
      - url: https://docs.stripe.com/api/invoices
        type: API Reference
      - url: openapi/stripe-invoice-api-openapi.yml
        type: OpenAPI
    description: Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.
  - aid: stripe:stripe-issuing-api
    name: Stripe Issuing API
    tags:
      - Cards
      - Issuing
    properties:
      - url: https://stripe.com/docs/issuing
        type: Documentation
      - url: openapi/stripe-issuing-api-openapi.yml
        type: OpenAPI
    description: An API for businesses to instantly create, manage, and distribute payment cards.
  - aid: stripe:stripe-link-api
    name: Stripe Link API
    tags:
      - Links
      - Payments
    properties:
      - url: https://stripe.com/docs/payment-links/api
        type: Documentation
      - url: openapi/stripe-link-api-openapi.yml
        type: OpenAPI
    description: You can use the Payment Links API to create a payment link that you can share with your customers. Stripe redirects customers who open this link to a Stripe-hosted payment page.
  - aid: stripe:stripe-payment-intents-api
    name: Stripe Payment Intents API
    tags:
      - Intent
      - Intents
      - Payments
    properties:
      - url: https://stripe.com/docs/api/payment_intents
        type: Documentation
      - url: https://docs.stripe.com/api/payment_intents
        type: API Reference
      - url: openapi/stripe-payment-intents-api-openapi.yml
        type: OpenAPI
    description: A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.
  - aid: stripe:stripe-payment-links-api
    name: Stripe Payment Links API
    tags:
      - Link
      - Links
      - Payments
    properties:
      - url: https://stripe.com/docs/api/payment_links/payment_links
        type: Documentation
      - url: openapi/stripe-payment-links-api-openapi.yml
        type: OpenAPI
    description: A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times. When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.
  - aid: stripe:stripe-payment-method-api
    name: Stripe Payment Method API
    tags:
      - Detach
      - Methods
      - Payments
    properties:
      - url: https://stripe.com/docs/payments/payment-methods
        type: Documentation
      - url: openapi/stripe-payment-method-api-openapi.yml
        type: OpenAPI
    description: The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments.
  - aid: stripe:stripe-payouts-api
    name: Stripe Payouts API
    tags:
      - Payouts
    properties:
      - url: https://stripe.com/docs/api/payouts
        type: Documentation
      - url: https://docs.stripe.com/api/payouts
        type: API Reference
      - url: openapi/stripe-payouts-api-openapi.yml
        type: OpenAPI
    description: A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.
  - aid: stripe:stripe-plans-api
    name: Stripe Plans API
    tags:
      - Plan
      - Plans
    properties:
      - url: https://stripe.com/docs/api/plans
        type: Documentation
      - url: openapi/stripe-plans-api-openapi.yml
        type: OpenAPI
    description: You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.
  - aid: stripe:stripe-prices-api
    name: Stripe Prices API
    tags:
      - Prices
    properties:
      - url: https://stripe.com/docs/api/prices
        type: Documentation
      - url: https://docs.stripe.com/api/prices
        type: API Reference
      - url: openapi/stripe-prices-api-openapi.yml
        type: OpenAPI
    description: Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.
  - aid: stripe:stripe-products-api
    name: Stripe Products API
    tags:
      - Products
    properties:
      - url: https://stripe.com/docs/api/products
        type: Documentation
      - url: https://docs.stripe.com/api/products
        type: API Reference
      - url: openapi/stripe-products-api-openapi.yml
        type: OpenAPI
    description: Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.
  - aid: stripe:stripe-promotion-codes-api
    name: Stripe Promotion Codes API
    tags:
      - Codes
      - Promotion
      - Promotions
    properties:
      - url: https://stripe.com/docs/api/promotion_codes
        type: Documentation
      - url: openapi/stripe-promotion-codes-api-openapi.yml
        type: OpenAPI
    description: A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.
  - aid: stripe:stripe-quotes-api
    name: Stripe Quotes API
    tags:
      - Quotes
    properties:
      - url: https://stripe.com/docs/api/quotes
        type: Documentation
      - url: openapi/stripe-quotes-api-openapi.yml
        type: OpenAPI
    description: A Quote is a way to model prices that you'd like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.
  - aid: stripe:stripe-radar-api
    name: Stripe Radar API
    tags:
      - Fraud
      - Radar
    properties:
      - url: https://stripe.com/docs/radar
        type: Documentation
      - url: openapi/stripe-radar-api-openapi.yml
        type: OpenAPI
    description: Stripe Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.
  - aid: stripe:stripe-refunds-api
    name: Stripe Refunds API
    tags:
      - Refunds
    properties:
      - url: https://stripe.com/docs/api/refunds
        type: Documentation
      - url: https://docs.stripe.com/api/refunds
        type: API Reference
      - url: openapi/stripe-refunds-api-openapi.yml
        type: OpenAPI
    description: Refund objects allow you to refund a previously created charge that isn't refunded yet. Funds are refunded to the credit or debit card that's initially charged.
  - aid: stripe:stripe-reporting-api
    name: Stripe Reporting API
    tags:
      - Reporting
      - Reports
    properties:
      - url: https://stripe.com/docs/reports/api
        type: Documentation
      - url: openapi/stripe-reporting-api-openapi.yml
        type: OpenAPI
    description: The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.
  - aid: stripe:stripe-reviews-api
    name: Stripe Reviews API
    tags:
      - Reviews
    properties:
      - url: https://stripe.com/docs/api/radar/reviews
        type: Documentation
      - url: openapi/stripe-reviews-api-openapi.yml
        type: OpenAPI
    description: Reviews can be used to supplement automated fraud detection with human expertise.
  - aid: stripe:stripe-setup-api
    name: Stripe Setup API
    tags:
      - Intent
      - Intents
      - Setup
    properties:
      - url: https://stripe.com/docs/payments/setup-intents
        type: Documentation
      - url: openapi/stripe-setup-api-openapi.yml
        type: OpenAPI
    description: Use the Setup Intents API to set up a payment method for future payments. It's similar to a payment, but no charge is created. Set up a payment method for future payments now.
  - aid: stripe:stripe-shipping-rates-api
    name: Stripe Shipping Rates API
    tags:
      - Rates
      - Shipping
    properties:
      - url: https://stripe.com/docs/api/shipping_rates
        type: Documentation
      - url: openapi/stripe-shipping-rates-api-openapi.yml
        type: OpenAPI
    description: Shipping rates describe the price of shipping presented to your customers and applied to a purchase.
  - aid: stripe:stripe-sigma-api
    name: Stripe Sigma API
    tags:
      - Sigma
    properties:
      - url: https://stripe.com/docs/api/sigma/scheduled_queries
        type: Documentation
      - url: openapi/stripe-sigma-api-openapi.yml
        type: OpenAPI
    description: If you have scheduled a Sigma query, you'll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.
  - aid: stripe:stripe-sources-api
    name: Stripe Sources API
    tags:
      - Sources
      - Transactions
    properties:
      - url: https://stripe.com/docs/api/sources
        type: Documentation
      - url: openapi/stripe-sources-api-openapi.yml
        type: OpenAPI
    description: Source objects allow you to accept a variety of payment methods. They represent a customer's payment instrument, and can be used with the Stripe API just like a Card object once chargeable, they can be charged, or can be attached to customers.
  - aid: stripe:stripe-subscription-api
    name: Stripe Subscription API
    tags:
      - Recurring
      - Subscriptions
    properties:
      - url: https://stripe.com/docs/api/subscriptions
        type: Documentation
      - url: https://docs.stripe.com/api/subscriptions
        type: API Reference
      - url: openapi/stripe-subscription-api-openapi.yml
        type: OpenAPI
    description: Subscriptions allow you to charge a customer on a recurring basis.
  - aid: stripe:stripe-tax-api
    name: Stripe Tax API
    tags:
      - Taxes
    properties:
      - url: https://stripe.com/docs/tax
        type: Documentation
      - url: openapi/stripe-tax-api-openapi.yml
        type: OpenAPI
    description: Automate sales tax, VAT, and GST compliance on all your transactions-low or no code integrations available.
  - aid: stripe:stripe-terminal-api
    name: Stripe Terminal API
    tags:
      - Point of Sale
      - Terminal
      - Terminals
    properties:
      - url: https://stripe.com/docs/terminal
        type: Documentation
      - url: openapi/stripe-terminal-api-openapi.yml
        type: OpenAPI
    description: Use Stripe Terminal to accept in-person payments and extend Stripe payments to your point of sale.
  - aid: stripe:stripe-test-helpers-api
    name: Stripe Test Helpers API
    tags:
      - Synthetic
      - Testing
      - Virtualization
    properties:
      - url: https://stripe.com/docs/implementation-guides/billing/testing
        type: Documentation
      - url: openapi/stripe-test-helpers-api-openapi.yml
        type: OpenAPI
    description: Stripe provides a number of resources for testing your integration. Make sure to test the following use cases before launch, and use our Postman collection to make the testing process simpler.
  - aid: stripe:stripe-tokens-api
    name: Stripe Tokens API
    tags:
      - Tokens
    properties:
      - url: https://stripe.com/docs/api/tokens
        type: Documentation
      - url: https://docs.stripe.com/api/tokens
        type: API Reference
      - url: openapi/stripe-tokens-api-openapi.yml
        type: OpenAPI
    description: Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.
  - aid: stripe:stripe-topups-api
    name: Stripe Topups API
    tags:
      - Topups
    properties:
      - url: https://stripe.com/docs/api/topups
        type: Documentation
      - url: https://docs.stripe.com/api/topups
        type: API Reference
      - url: openapi/stripe-topups-api-openapi.yml
        type: OpenAPI
    description: To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.
  - aid: stripe:stripe-transfers-api
    name: Stripe Transfers API
    tags:
      - Transfers
    properties:
      - url: https://stripe.com/docs/api/transfers
        type: Documentation
      - url: https://docs.stripe.com/api/transfers
        type: API Reference
      - url: openapi/stripe-transfers-api-openapi.yml
        type: OpenAPI
    description: A Transfer object is created when you move funds between Stripe accounts as part of Connect.
  - aid: stripe:stripe-treasury-api
    name: Stripe Treasury API
    tags:
      - Treasury
    properties:
      - url: https://stripe.com/docs/treasury
        type: Documentation
      - url: openapi/stripe-treasury-api-openapi.yml
        type: OpenAPI
    description: Stripe Treasury is a banking-as-a-service API that lets you embed financial services in your product. With Stripe's API, you can enable businesses to hold funds, pay bills, earn yield, and manage their cash flow. Many users build Stripe Issuing in conjunction with Stripe Treasury to attach cards to spend funds in the account.
  - aid: stripe:stripe-webhook-api
    name: Stripe Webhook API
    tags:
      - Webhooks
    properties:
      - url: https://stripe.com/docs/api/webhook_endpoints
        type: Documentation
      - url: https://docs.stripe.com/api/webhook_endpoints
        type: API Reference
      - url: openapi/stripe-webhook-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/stripe-webhooks-asyncapi.yml
        type: AsyncAPI
    description: You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.
  - aid: stripe:stripe-connect-api
    name: Stripe Connect API
    tags:
      - Connect
      - Marketplaces
      - Platforms
    properties:
      - url: https://docs.stripe.com/connect
        type: Documentation
      - url: https://docs.stripe.com/api/connected-accounts
        type: API Reference
      - url: openapi/stripe-connect-api-openapi.yml
        type: OpenAPI
    description: Stripe Connect is a set of programmable APIs and tools that lets you facilitate payments on your software platform, build a marketplace, and pay out sellers or service providers globally.
  - aid: stripe:stripe-customer-portal-api
    name: Stripe Customer Portal API
    tags:
      - Billing
      - Customers
      - Portal
      - Subscriptions
    properties:
      - url: https://docs.stripe.com/customer-management
        type: Documentation
      - url: https://docs.stripe.com/api/customer_portal
        type: API Reference
      - url: openapi/stripe-customer-portal-api-openapi.yml
        type: OpenAPI
    description: The Billing customer portal is a Stripe-hosted UI for subscription and billing management. A portal session describes the instantiation of the customer portal for a particular customer. By visiting the session URL, the customer can manage their subscriptions and billing details.
  - aid: stripe:stripe-entitlements-api
    name: Stripe Entitlements API
    tags:
      - Billing
      - Entitlements
      - Features
    properties:
      - url: https://docs.stripe.com/billing/entitlements
        type: Documentation
      - url: https://docs.stripe.com/api/entitlements/active-entitlement
        type: API Reference
      - url: openapi/stripe-entitlements-api-openapi.yml
        type: OpenAPI
    description: Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access according to your customers subscription status.
  - aid: stripe:stripe-forwarding-api
    name: Stripe Forwarding API
    tags:
      - Cards
      - Forwarding
      - Vault
    properties:
      - url: https://docs.stripe.com/payments/vault-and-forward
        type: Documentation
      - url: https://docs.stripe.com/api/forwarding/request
        type: API Reference
      - url: openapi/stripe-forwarding-api-openapi.yml
        type: OpenAPI
    description: The Vault and Forward API allows you to tokenize and store card details in Stripes PCI-compliant vault and forward that data to supported third-party processors or endpoints.
  - aid: stripe:stripe-crypto-onramp-api
    name: Stripe Crypto Onramp API
    tags:
      - Crypto
      - Onramp
      - Payments
    properties:
      - url: https://docs.stripe.com/crypto/onramp
        type: Documentation
      - url: https://docs.stripe.com/api/crypto/onramp_sessions
        type: API Reference
      - url: openapi/stripe-crypto-onramp-api-openapi.yml
        type: OpenAPI
    description: The Stripe fiat-to-crypto onramp lets your customers securely purchase and exchange cryptocurrencies directly from your platform or decentralized application at checkout.
  - aid: stripe:stripe-revenue-recognition-api
    name: Stripe Revenue Recognition API
    tags:
      - Accounting
      - Recognition
      - Revenue
    properties:
      - url: https://docs.stripe.com/revenue-recognition
        type: Documentation
      - url: https://docs.stripe.com/revenue-recognition/api
        type: API Reference
      - url: openapi/stripe-revenue-recognition-api-openapi.yml
        type: OpenAPI
    description: Automate your accrual accounting process with Stripe Revenue Recognition. Import transaction data, set up rules, and download revenue reports for compliance with accounting standards like ASC 606.
  - aid: stripe:stripe-billing-meters-api
    name: Stripe Billing Meters API
    tags:
      - Billing
      - Meters
      - Usage-Based
    properties:
      - url: https://docs.stripe.com/api/billing/meter
        type: API Reference
      - url: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api
        type: Documentation
      - url: https://docs.stripe.com/api/v2/billing-meter
        type: API Reference
      - url: https://docs.stripe.com/api/v2/billing-meter-stream
        type: API Reference
      - url: openapi/stripe-billing-meters-api-openapi.yml
        type: OpenAPI
    description: Meters specify how to aggregate meter events over a billing period for usage-based pricing. Meter events represent customer actions and support up to 10,000 events per second via the V2 meter event streams API.
  - aid: stripe:stripe-payment-method-configurations-api
    name: Stripe Payment Method Configurations API
    tags:
      - Configuration
      - Payments
    properties:
      - url: https://docs.stripe.com/api/payment_method_configurations
        type: API Reference
      - url: https://docs.stripe.com/connect/payment-method-configurations
        type: Documentation
      - url: openapi/stripe-payment-method-configurations-api-openapi.yml
        type: OpenAPI
    description: Payment method configurations allow you to configure which payment methods are available to your customers during checkout. Manage payment method availability across multiple Connect accounts.
name: Stripe
tags:
  - Commerce
  - Financial Services
  - Fintech
  - Payments
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://dashboard.stripe.com/register
    type: Sign Up
  - url: https://dashboard.stripe.com
    type: Portal
  - url: https://docs.stripe.com/
    type: Documentation
  - url: https://docs.stripe.com/get-started
    type: Getting Started
  - url: https://docs.stripe.com/api
    type: API Reference
  - url: https://stripe.com/docs/api/authentication
    type: Authentication
  - url: https://docs.stripe.com/api/errors
    type: Errors
  - url: https://docs.stripe.com/sdks
    type: SDKs
  - url: https://docs.stripe.com/stripe-cli
    type: CLI
  - url: https://stripe.com/blog
    type: Blog
  - url: https://docs.stripe.com/changelog
    type: Change Log
  - url: https://docs.stripe.com/upgrades
    type: API Versioning
  - url: https://status.stripe.com/
    type: Status
  - url: https://docs.stripe.com/rate-limits
    type: Rate Limits
  - url: https://docs.stripe.com/security
    type: Security
  - url: https://stripe.com/privacy
    type: Privacy Policy
  - url: https://stripe.com/legal/ssa
    type: Terms of Service
  - url: https://stripe.com/pricing
    type: Pricing
  - url: https://support.stripe.com/
    type: Support
  - url: https://discord.com/invite/stripe
    type: Discord
  - url: https://github.com/stripe
    type: GitHub Organization
  - url: https://github.com/stripe/openapi
    type: OpenAPI Source
  - url: https://www.postman.com/stripedev/workspace/stripe-developers/overview
    type: Postman Workspace
  - url: https://github.com/stripe/stripe-node
    type: Node.js SDK
  - url: https://github.com/stripe/stripe-python
    type: Python SDK
  - url: https://github.com/stripe/stripe-php
    type: PHP SDK
  - url: https://github.com/stripe/stripe-ruby
    type: Ruby SDK
  - url: https://github.com/stripe/stripe-java
    type: Java SDK
  - url: https://github.com/stripe/stripe-go
    type: Go SDK
  - url: https://github.com/stripe/stripe-dotnet
    type: .NET SDK
  - url: https://github.com/stripe/stripe-ios
    type: iOS SDK
  - url: https://github.com/stripe/stripe-android
    type: Android SDK
  - url: https://x.com/stripe
    type: X (Twitter)
  - url: https://x.com/StripeDev
    type: X (Twitter) Developer
  - url: https://docs.stripe.com/webhooks
    type: Webhooks
  - url: https://docs.stripe.com/testing
    type: Testing
  - url: https://docs.stripe.com/api/expanding_objects
    type: Expanding Objects
  - url: https://docs.stripe.com/api/pagination
    type: Pagination
  - url: https://docs.stripe.com/api/idempotent_requests
    type: Idempotent Requests
  - url: https://docs.stripe.com/api/metadata
    type: Metadata
  - url: https://docs.stripe.com/building-extensions/stripe-apps
    type: Stripe Apps
  - url: https://marketplace.stripe.com/
    type: Marketplace
  - url: https://www.youtube.com/@StripeDevelopers
    type: YouTube
  - url: https://stackoverflow.com/questions/tagged/stripe-payments
    type: Stack Overflow
  - url: https://stripe.com
    type: Website
  - url: https://dashboard.stripe.com/login
    type: Login
  - url: https://docs.stripe.com/samples
    type: Code Samples
  - url: https://docs.stripe.com/keys
    type: API Keys
  - url: asyncapi/stripe-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/stripe-customer.json
    type: JSON Schema
  - url: json-schema/stripe-payment-intent.json
    type: JSON Schema
  - url: json-schema/stripe-subscription.json
    type: JSON Schema
  - url: json-schema/stripe-charge.json
    type: JSON Schema
  - url: json-schema/stripe-invoice.json
    type: JSON Schema
  - url: json-schema/stripe-event.json
    type: JSON Schema
  - url: json-schema/stripe-product.json
    type: JSON Schema
  - url: json-schema/stripe-price.json
    type: JSON Schema
  - url: json-ld/stripe-context.jsonld
    type: JSON-LD Context
  - url: rules/stripe-rules.yml
    type: Spectral Rules
  - url: capabilities/payment-processing.yaml
    type: Naftiko Capability
  - url: capabilities/subscription-billing.yaml
    type: Naftiko Capability
  - url: capabilities/financial-operations.yaml
    type: Naftiko Capability
  - url: vocabulary/stripe-vocabulary.yml
    type: Vocabulary
  - url: json-structure/stripe-payment-intent-structure.json
    type: JSON Structure
  - url: json-structure/stripe-customer-structure.json
    type: JSON Structure
  - url: json-structure/stripe-invoice-structure.json
    type: JSON Structure
  - url: examples/stripe-create-payment-intent-example.json
    type: Example
  - url: examples/stripe-create-checkout-session-example.json
    type: Example
  - url: examples/stripe-create-customer-example.json
    type: Example
  - type: Features
    data:
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
    sources:
      - https://stripe.com/pricing
    updated: '2026-05-04'
created: 2024/04/14
modified: '2026-05-04'
position: Consuming
description: Online payment processing for internet businesses. Stripe is a suite of payment APIs that powers commerce for online businesses of all sizes.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - FN: APIs.json
    email: info@apis.io
  - name: Stripe
    email: support@stripe.com
    url: https://stripe.com
specificationVersion: '0.18'
image: https://stripe.com/img/about/logos/logos/blue.png
---
