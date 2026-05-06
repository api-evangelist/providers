---
aid: paypal
name: PayPal
description: PayPal is a global online payment system that lets individuals and businesses send and receive money electronically. PayPal exposes a broad surface of REST APIs covering payments, orders, subscriptions, invoicing, payouts, disputes, payment tokens, shipping tracking, transaction reporting, partner referrals, payment experience, and webhook notifications.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
created: '2024-04-14'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/paypal/refs/heads/main/apis.yml
specificationVersion: '0.20'
apis:
  - aid: paypal:paypal-billing-subscriptions-api
    name: PayPal Billing Subscriptions API
    description: The PayPal Billing Subscriptions API enables businesses to create and manage subscription plans, activate, suspend, cancel, capture, and revise customer subscriptions, and track recurring payments.
    humanURL: https://developer.paypal.com/docs/api/subscriptions/v1/
    tags:
      - Activate
      - Billing
      - Cancel
      - Capture
      - Plans
      - Subscriptions
      - Suspend
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/subscriptions/v1/
      - type: OpenAPI
        url: openapi/paypal-billing-subscriptions-openapi-original.yml
  - aid: paypal:paypal-products-api
    name: PayPal Catalog Products API
    description: The PayPal Catalog Products API lets merchants create and manage product definitions used across orders, subscriptions, and invoicing.
    humanURL: https://developer.paypal.com/docs/api/catalog-products/v1/
    tags:
      - Catalog
      - Products
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/catalog-products/v1/
      - type: OpenAPI
        url: openapi/paypal-catalog-products-openapi-original.yml
  - aid: paypal:paypal-orders-api
    name: PayPal Orders API
    description: The PayPal Orders API lets merchants create, update, authorize, capture, and manage orders for accepting payments through PayPal Checkout.
    humanURL: https://developer.paypal.com/docs/api/orders/v2/
    tags:
      - Checkout
      - Orders
      - Payments
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/orders/v2/
      - type: OpenAPI
        url: openapi/paypal-checkout-orders-openapi-original.yml
  - aid: paypal:paypal-disputes-api
    name: PayPal Customer Disputes API
    description: The PayPal Customer Disputes API allows merchants to retrieve, respond to, escalate, and settle disputes raised on transactions, including providing evidence and managing dispute lifecycles.
    humanURL: https://developer.paypal.com/docs/disputes/integration-guide/
    tags:
      - Disputes
      - Evidence
      - Resolution
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/disputes/integration-guide/
      - type: OpenAPI
        url: openapi/paypal-customer-disputes-openapi-original.yml
  - aid: paypal:paypal-partner-referrals-api
    name: PayPal Partner Referrals API
    description: The PayPal Partner Referrals API enables platforms and marketplaces to onboard merchants onto PayPal, generate referral links, and track partner account creation status.
    humanURL: https://developer.paypal.com/docs/api/partner-referrals/v1/
    tags:
      - Onboarding
      - Partner
      - Referrals
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/partner-referrals/v1/
      - type: OpenAPI
        url: openapi/paypal-customer-partner-referrals-openapi-original.yml
  - aid: paypal:paypal-invoicing-api
    name: PayPal Invoicing API
    description: The PayPal Invoicing API allows merchants to create, send, schedule, track, and manage invoices, including reminders and payment status.
    humanURL: https://developer.paypal.com/docs/api/invoicing/v2/
    tags:
      - Billing
      - Invoices
      - Payments
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/invoicing/v2/
      - type: OpenAPI
        url: openapi/paypal-invoicing-openapi-original.yml
  - aid: paypal:paypal-notification-webhooks-api
    name: PayPal Notification Webhooks API
    description: The PayPal Notification Webhooks API lets developers subscribe to and manage webhook event notifications for payments, refunds, disputes, and other PayPal account activity.
    humanURL: https://developer.paypal.com/api/rest/webhooks/
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.paypal.com/api/rest/webhooks/
      - type: OpenAPI
        url: openapi/paypal-notification-webhooks-openapi-original.yml
  - aid: paypal:paypal-payment-experience-api
    name: PayPal Payment Experience API
    description: The PayPal Payment Experience API lets merchants create web experience profiles to customize the look, feel, and flow of PayPal checkout pages.
    humanURL: https://developer.paypal.com/docs/payment-experience/
    tags:
      - Checkout
      - Customization
      - Experience
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/payment-experience/
      - type: OpenAPI
        url: openapi/paypal-payment-experience-openapi-original.yml
  - aid: paypal:paypal-payments-api
    name: PayPal Payments API
    description: The PayPal Payments API lets businesses authorize, capture, refund, void, and reauthorize payments, supporting credit and debit cards as well as PayPal and Venmo wallets.
    humanURL: https://developer.paypal.com/api/rest/
    tags:
      - Authorizations
      - Captures
      - Payments
      - Refunds
    properties:
      - type: Documentation
        url: https://developer.paypal.com/api/rest/
      - type: OpenAPI
        url: openapi/paypal-payments-openapi-original.yml
  - aid: paypal:paypal-payouts-api
    name: PayPal Payouts API
    description: The PayPal Payouts API lets businesses send mass payments to multiple recipients with a single API call, useful for marketplaces, affiliates, rewards programs, and contractor payouts.
    humanURL: https://developer.paypal.com/docs/api/payments.payouts-batch/v1/
    tags:
      - Mass Pay
      - Payouts
      - Transfers
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/payments.payouts-batch/v1/
      - type: OpenAPI
        url: openapi/paypal-payouts-openapi-original.yml
  - aid: paypal:paypal-reporting-transactions-api
    name: PayPal Transaction Search (Reporting) API
    description: The PayPal Transaction Search API provides access to historical transaction details, balances, and account activity for reporting, reconciliation, and accounting use cases.
    humanURL: https://developer.paypal.com/docs/api/transaction-search/v1/
    tags:
      - Reconciliation
      - Reporting
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/transaction-search/v1/
      - type: OpenAPI
        url: openapi/paypal-reporting-transactions-openapi-original.yml
  - aid: paypal:paypal-shipping-tracking-api
    name: PayPal Shipping Tracking API
    description: The PayPal Shipping Tracking API lets merchants attach, update, and retrieve tracking information on PayPal transactions for faster dispute resolution and improved buyer transparency.
    humanURL: https://developer.paypal.com/docs/tracking/tracking-api/
    tags:
      - Carriers
      - Shipping
      - Tracking
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/tracking/tracking-api/
      - type: OpenAPI
        url: openapi/paypal-shipping-tracking-openapi-original.yml
  - aid: paypal:paypal-payment-tokens-api
    name: PayPal Vault Payment Tokens API
    description: The PayPal Vault Payment Tokens API lets merchants securely store and reuse customer payment instruments as tokens for repeat billing and one-click checkout flows.
    humanURL: https://developer.paypal.com/docs/api/payment-tokens/v3/
    tags:
      - Tokens
      - Vault
      - Wallet
    properties:
      - type: Documentation
        url: https://developer.paypal.com/docs/api/payment-tokens/v3/
      - type: OpenAPI
        url: openapi/paypal-vault-payment-tokens-openapi-original.yml
common:
  - type: Website
    url: https://www.paypal.com
  - type: Developer Portal
    url: https://developer.paypal.com
  - type: Documentation
    url: https://developer.paypal.com/api/rest/
  - type: Authentication
    url: https://developer.paypal.com/api/rest/authentication/
  - type: Status
    url: https://www.paypal-status.com/
  - type: Pricing
    url: https://www.paypal.com/us/business/paypal-business-fees
  - type: Terms of Service
    url: https://www.paypal.com/us/legalhub/useragreement-full
  - type: Privacy Policy
    url: https://www.paypal.com/us/legalhub/privacy-full
  - type: Features
    data:
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
    sources:
      - https://www.paypal.com/us/business/paypal-business-fees
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
