---
aid: nomba
name: Nomba
description: Nomba is a Nigerian fintech platform that provides payment infrastructure for businesses, offering APIs for payment acceptance, transfers, virtual accounts, and cross-border payouts. Their developer platform enables merchants and platforms to integrate card payments, bank transfers, USSD, and QR code payments into applications.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/nomba/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Payments
  - Fintech
  - Banking
  - Transfers
  - Virtual Accounts
  - Checkout
  - Cross-Border Payments
  - Cards
apis:
  - aid: nomba:authentication
    name: Nomba Authentication API
    description: 'The Nomba Authentication API provides OAuth2-based authentication for accessing all Nomba API endpoints. It supports two authentication methods: Client-Credentials for server-to-server integrations and PKCE (Proof Key for Code Exchange) for client-side applications. Developers obtain HTTP bearer tokens that are used to authorize subsequent API calls across the Nomba platform.'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/authenticate/obtain-access-token
    baseURL: https://api.nomba.com
    tags:
      - Authentication
      - OAuth2
      - Security
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/authenticate/obtain-access-token
      - type: OpenAPI
        url: openapi/nomba-authentication-openapi.yml
  - aid: nomba:accounts
    name: Nomba Accounts API
    description: The Nomba Accounts API enables developers to manage business accounts on the Nomba platform. It provides endpoints for retrieving account details, fetching terminals assigned to an account, and managing account-level configurations. This API serves as the foundation for account management operations within the Nomba ecosystem.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/accounts/fetch-terminals-assigned-to-an-account
    baseURL: https://api.nomba.com
    tags:
      - Accounts
      - Financial Services
      - Terminals
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/accounts/fetch-terminals-assigned-to-an-account
      - type: OpenAPI
        url: openapi/nomba-accounts-openapi.yml
  - aid: nomba:virtual-accounts
    name: Nomba Virtual Accounts API
    description: The Nomba Virtual Accounts API allows developers to create and manage virtual bank accounts for receiving payments. There is no fixed limit to the number of virtual accounts that can be created for customers. The API supports creating, expiring, and managing virtual accounts, enabling businesses to collect payments via bank transfers with unique account numbers assigned to individual customers or transactions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/virtual-accounts/create-virtual-account
    baseURL: https://api.nomba.com
    tags:
      - Virtual Accounts
      - Payments
      - Collections
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/virtual-accounts/create-virtual-account
      - type: OpenAPI
        url: openapi/nomba-virtual-accounts-openapi.yml
  - aid: nomba:transfers
    name: Nomba Transfers API
    description: The Nomba Transfers API provides endpoints for initiating and managing fund transfers. Developers can look up bank codes and names, verify account details, and initiate transfers to Nigerian bank accounts. The API supports domestic money transfers and provides the necessary bank metadata for building payment flows within applications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/transfers/fetch-bank-codes-and-names
    baseURL: https://api.nomba.com
    tags:
      - Transfers
      - Payments
      - Banking
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/transfers/fetch-bank-codes-and-names
      - type: OpenAPI
        url: openapi/nomba-transfers-openapi.yml
  - aid: nomba:online-checkout
    name: Nomba Online Checkout API
    description: The Nomba Online Checkout API enables developers to create checkout orders and process payments through multiple channels. It supports Visa, Verve, and Mastercard payments, as well as USSD, bank transfers, and Nomba QR payments. The API includes tokenized card payment capabilities, allowing merchants to charge returning customers without requiring them to re-enter card details.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/online-checkout/create-an-online-checkout-order
    baseURL: https://api.nomba.com
    tags:
      - Checkout
      - Payments
      - E-Commerce
      - Cards
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/online-checkout/create-an-online-checkout-order
      - type: OpenAPI
        url: openapi/nomba-online-checkout-openapi.yml
  - aid: nomba:charge
    name: Nomba Charge API
    description: The Nomba Charge API provides direct card charging capabilities for developers building payment solutions. It supports OTP submission for card transactions, retrieval of user saved cards, and tokenized card charging. This API is designed for merchants and platforms that need programmatic control over the card payment flow, including handling 3D Secure authentication steps.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/nomba-api-reference/charge/submit-customer-card-otp
    baseURL: https://api.nomba.com
    tags:
      - Payments
      - Cards
      - Tokenization
    properties:
      - type: Documentation
        url: https://developer.nomba.com/nomba-api-reference/charge/submit-customer-card-otp
      - type: OpenAPI
        url: openapi/nomba-charge-openapi.yml
  - aid: nomba:transactions
    name: Nomba Transactions API
    description: The Nomba Transactions API allows developers to retrieve and manage transaction records. It provides endpoints for fetching account transaction history, querying transaction details, and processing refunds. This API is essential for building reporting dashboards, reconciliation tools, and transaction monitoring systems on top of the Nomba platform.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/products/transactions/fetch-account-transactions
    baseURL: https://api.nomba.com
    tags:
      - Transactions
      - Reporting
      - Financial Data
    properties:
      - type: Documentation
        url: https://developer.nomba.com/products/transactions/fetch-account-transactions
      - type: OpenAPI
        url: openapi/nomba-transactions-openapi.yml
  - aid: nomba:global-payout
    name: Nomba Global Payout API
    description: The Nomba Global Payout API is a single integration point that enables cross-border payment operators, remittance platforms, and fintechs to collect funds in Nigerian Naira or stablecoins (USDT/USDC) and trigger instant disbursements to the United Kingdom via Faster Payments, Europe via SEPA, Canada via Interac and bank transfer, and the Democratic Republic of Congo via Mobile Money. The API embeds FX sourcing and compliance directly into the technical layer, eliminating the need for operators to manage foreign exchange processes. It solves capital lockups in cross-border trade by handling currency conversion automatically when funds land in a virtual account.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/docs/products/global-payout/introduction
    baseURL: https://api.nomba.com
    tags:
      - Cross-Border Payments
      - Payouts
      - Foreign Exchange
      - Stablecoins
      - Remittance
    properties:
      - type: Documentation
        url: https://developer.nomba.com/docs/products/global-payout/introduction
      - type: OpenAPI
        url: openapi/nomba-global-payout-openapi.yml
  - aid: nomba:checkout-sdk
    name: Nomba Checkout SDK
    description: The Nomba Checkout SDK provides pre-built plugins and client libraries for integrating Nomba payment acceptance into websites and mobile applications. It includes an iOS SDK and e-commerce plugins such as a WooCommerce gateway for WordPress. The SDK supports Visa, Verve, and Mastercard payments along with USSD, bank transfers, and Nomba QR, enabling merchants to quickly add payment capabilities without building a custom checkout flow.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nomba.com/plugins-and-sdk/overview
    baseURL: https://api.nomba.com
    tags:
      - SDK
      - Checkout
      - Plugins
      - E-Commerce
    properties:
      - type: Documentation
        url: https://developer.nomba.com/plugins-and-sdk/overview
common:
  - type: Website
    url: https://nomba.com
  - type: Developer Portal
    url: https://developer.nomba.com
  - type: Blog
    url: https://nomba-developers.hashnode.dev
  - type: AsyncAPI
    url: asyncapi/nomba-webhooks-asyncapi.yml
  - type: JSONSchema
    url: json-schema/nomba-webhook-event-schema.json
  - type: JSONSchema
    url: json-schema/nomba-virtual-account-schema.json
  - type: JSONSchema
    url: json-schema/nomba-transaction-schema.json
  - type: JSONSchema
    url: json-schema/nomba-checkout-order-schema.json
  - type: JSON-LD
    url: json-ld/nomba-context.jsonld
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---
