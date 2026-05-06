---
aid: authorize-net
name: Authorize.net
description: |
  Authorize.net is a leading payment gateway providing secure online payment processing for merchants. It offers a POST-based XML/JSON API, Accept.js hosted payment forms, the Accept Hosted solution, recurring billing (ARB), customer profile management (CIM), advanced fraud detection, and webhooks. Official SDKs are available for PHP, .NET, Java, Ruby, Python, and Node.js.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accept.js
  - Credit Cards
  - eChecks
  - Fraud Detection
  - Payment Gateway
  - Payments
  - Recurring Billing
  - Transactions
url: https://raw.githubusercontent.com/api-evangelist/authorize-net/refs/heads/main/apis.yml
created: '2025-02-17'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: authorize-net:authorize-net-payment-api
    name: Authorize.net Payment API
    description: |
      The Authorize.net Payment API enables merchants to process credit card, debit card, eCheck, Apple Pay, Google Pay, and PayPal transactions via a POST-based XML/JSON API with API Login ID and Transaction Key authentication.
    humanURL: https://developer.authorize.net/api/reference/
    baseURL: https://api.authorize.net/xml/v1/request.api
    tags:
      - Credit Cards
      - eChecks
      - Payment Gateway
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.authorize.net/api/reference/
      - type: GettingStarted
        url: https://developer.authorize.net/hello_world/
      - type: Authentication
        url: https://developer.authorize.net/api/reference/features/authentication.html
      - type: APIReference
        url: https://developer.authorize.net/api/reference/
      - type: Sandbox
        url: https://sandbox.authorize.net/
  - aid: authorize-net:authorize-net-recurring-billing-api
    name: Authorize.net Recurring Billing API
    description: |
      The Authorize.net Automated Recurring Billing (ARB) API enables merchants to create, update, and cancel subscription-based payment schedules for recurring charges.
    humanURL: https://developer.authorize.net/api/reference/features/recurring_billing.html
    baseURL: https://api.authorize.net/xml/v1/request.api
    tags:
      - Payment Gateway
      - Recurring Billing
      - Subscriptions
    properties:
      - type: Documentation
        url: https://developer.authorize.net/api/reference/features/recurring_billing.html
  - aid: authorize-net:authorize-net-customer-profiles-api
    name: Authorize.net Customer Profiles API
    description: |
      The Authorize.net Customer Information Manager (CIM) API enables secure storage and management of customer payment profiles including credit cards and bank accounts for reuse in future transactions.
    humanURL: https://developer.authorize.net/api/reference/features/customer_profiles.html
    baseURL: https://api.authorize.net/xml/v1/request.api
    tags:
      - Customer Profiles
      - Payment Gateway
      - Tokenization
    properties:
      - type: Documentation
        url: https://developer.authorize.net/api/reference/features/customer_profiles.html
  - aid: authorize-net:authorize-net-webhooks
    name: Authorize.net Webhooks
    description: |
      Authorize.net Webhooks deliver real-time event notifications for transaction, subscription, and fraud management events to merchant-configured HTTP endpoints.
    humanURL: https://developer.authorize.net/api/reference/features/webhooks.html
    baseURL: https://api.authorize.net/rest/v1
    tags:
      - Events
      - Payment Gateway
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.authorize.net/api/reference/features/webhooks.html
common:
  - type: Website
    url: https://www.authorize.net/
  - type: Documentation
    url: https://developer.authorize.net/
  - type: Portal
    url: https://developer.authorize.net/
  - type: Blog
    url: https://developer.authorize.net/blog/
  - type: Sign Up
    url: https://www.authorize.net/sign-up/
  - type: Login
    url: https://account.authorize.net/
  - type: Pricing
    url: https://www.authorize.net/sign-up/pricing/
  - type: Support
    url: https://support.authorize.net/
  - type: Status
    url: https://status.authorize.net/
  - type: Terms of Service
    url: https://www.authorize.net/company/terms/
  - type: Privacy Policy
    url: https://www.authorize.net/company/privacy/
  - type: GitHub Organization
    url: https://github.com/AuthorizeNet
  - type: SDK
    title: PHP SDK
    url: https://github.com/AuthorizeNet/sdk-php
  - type: SDK
    title: .NET SDK
    url: https://github.com/AuthorizeNet/sdk-dotnet
  - type: SDK
    title: Java SDK
    url: https://github.com/AuthorizeNet/sdk-java
  - type: SDK
    title: Ruby SDK
    url: https://github.com/AuthorizeNet/sdk-ruby
  - type: SDK
    title: Python SDK
    url: https://github.com/AuthorizeNet/sdk-python
  - type: SDK
    title: Node.js SDK
    url: https://github.com/AuthorizeNet/sdk-node
  - type: Features
    data:
      - name: Payment Processing
        description: Accept credit cards, debit cards, eChecks, Apple Pay, Google Pay, and PayPal via a single unified API.
      - name: Accept.js
        description: Client-side JavaScript library that tokenizes payment data in the browser to keep merchant servers out of PCI scope.
      - name: Accept Hosted
        description: Fully hosted payment form that redirects customers to Authorize.net for payment collection with iframe support.
      - name: Recurring Billing (ARB)
        description: Automated recurring billing for subscriptions and installment plans with flexible scheduling options.
      - name: Customer Profiles (CIM)
        description: Securely vault customer payment methods for future charges without storing sensitive card data.
      - name: Fraud Detection Suite
        description: Advanced fraud detection tools including velocity controls, IP blocking, card security code verification, and address verification.
      - name: Webhooks
        description: Real-time event notifications for transaction completions, declines, fraud holds, and subscription events.
      - name: MCP Server
        description: Official Authorize.net MCP server for AI-assisted payment processing integration at github.com/AuthorizeNet/authorize-net-mcp.
  - type: UseCases
    data:
      - name: E-Commerce Payment Processing
        description: Accept payments on web storefronts using Accept.js or Accept Hosted for PCI-compliant card processing.
      - name: Subscription Billing
        description: Manage recurring charges for SaaS, membership, and subscription-based business models using ARB.
      - name: Mobile Payments
        description: Accept Apple Pay and Google Pay in mobile apps using the in-person and mobile payment SDKs.
      - name: Point-of-Sale Integration
        description: Integrate card-present transactions via the iOS, Android, or Windows in-person payment SDKs.
      - name: B2B and eCheck Payments
        description: Process ACH/eCheck payments for B2B invoicing and recurring bank account debit scenarios.
  - type: Integrations
    data:
      - name: WooCommerce
        description: Official Authorize.net WooCommerce payment plugin for WordPress-based e-commerce stores.
      - name: Medusa
        description: Official Authorize.net Medusa payment plugin for headless commerce implementations.
      - name: Visa and Mastercard Networks
        description: Direct connection to major card networks for authorization and settlement of card-based transactions.
      - name: NACHA ACH Network
        description: eCheck processing through the NACHA ACH network for bank-to-bank payment transfers.
  - type: Solutions
    data:
      - name: Payment Gateway
        description: Comprehensive payment gateway solution connecting merchants to card networks with fraud protection and reporting.
      - name: PCI-Compliant Payments
        description: Reduce PCI scope using Accept.js or Accept Hosted to tokenize payment data without touching card numbers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
