---
aid: braintree
url: https://raw.githubusercontent.com/api-evangelist/braintree/refs/heads/main/apis.yml
apis:
- aid: braintree:payments-api
  name: Braintree Payments API
  tags:
  - Credit Cards
  - Payments
  - PayPal
  - Transactions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.braintreegateway.com
  humanURL: https://developer.paypal.com/braintree/docs/
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/overview
    type: Documentation
  - url: openapi/braintree-payments-openapi.yml
    type: OpenAPI
  description: The Braintree Payments API is the core server-side interface for accepting and processing payments through Braintree's gateway. It enables developers to create and manage transactions, handle authorizations and captures, and process refunds and voids. The API supports a wide range of payment methods including credit and debit cards, PayPal, Apple Pay, Google Pay, and Venmo. Server SDKs are available for Ruby, Python, PHP, Java, Node.js, and .NET to simplify integration with the REST-based API.
- aid: braintree:graphql-api
  name: Braintree GraphQL API
  tags:
  - GraphQL
  - Payment Methods
  - Payments
  - Transactions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://payments.braintree-api.com/graphql
  humanURL: https://developer.paypal.com/braintree/graphql/
  properties:
  - url: https://developer.paypal.com/braintree/graphql/guides/concepts/
    type: Documentation
  description: The Braintree GraphQL API provides a modern, flexible interface for interacting with the Braintree payment gateway. It exposes a single HTTP endpoint that handles all queries and mutations, allowing developers to request only the data they need. The API supports tokenizing payment methods, creating transactions, managing customer vaults, and handling disputes. A sandbox environment is available at payments.sandbox.braintree-api.com/graphql for testing integrations before going live.
- aid: braintree:javascript-client-sdk
  name: Braintree JavaScript Client SDK
  tags:
  - Browser
  - Client SDK
  - Drop-In UI
  - JavaScript
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/javascript/v3/
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/javascript/v3/
    type: Documentation
  description: The Braintree JavaScript Client SDK enables secure collection of payment information directly in the browser without sensitive card data touching your servers. It is organized into standalone modules for different payment methods including hosted fields, PayPal, Apple Pay, Google Pay, and three-D Secure. The SDK provides both a Drop-In UI component for rapid integration and lower-level APIs for fully customized payment forms.
- aid: braintree:ios-sdk
  name: Braintree iOS SDK
  tags:
  - iOS
  - Mobile
  - Objective-C
  - Payments
  - Swift
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/ios/v6
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/ios/v6
    type: Documentation
  description: The Braintree iOS SDK is a native library for accepting card and alternative payments within iOS applications. It supports Swift and Objective-C and provides modules for credit and debit card processing, PayPal, Venmo, Apple Pay, and three-D Secure authentication. The SDK tokenizes payment information collected from users and returns a payment method nonce that your server uses to complete the transaction. It is distributed via CocoaPods, Carthage, and Swift Package Manager.
- aid: braintree:android-sdk
  name: Braintree Android SDK
  tags:
  - Android
  - Java
  - Kotlin
  - Mobile
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/android/v4
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/client-sdk/setup/android/v4
    type: Documentation
  description: The Braintree Android SDK provides a native library for integrating payment acceptance into Android applications. It supports Java and Kotlin and includes modules for card payments, PayPal, Venmo, Google Pay, and three-D Secure verification. Like the iOS counterpart, the Android SDK tokenizes payment data on the client side and returns a payment method nonce for server-side transaction processing. The SDK is distributed through Maven Central and supports Android API level 21 and above.
- aid: braintree:webhooks
  name: Braintree Webhooks
  tags:
  - Disputes
  - Events
  - Notifications
  - Subscriptions
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/webhooks/overview
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/webhooks/overview
    type: Documentation
  - url: asyncapi/braintree-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Braintree Webhooks deliver automated HTTP POST notifications to your server when specific events occur within the payment gateway. Supported event types include subscription status changes, transaction settlements, disbursements, dispute openings and resolutions, and sub-merchant account status updates for Braintree Marketplace. Each webhook notification contains the event kind and the full Braintree object associated with the triggering event.
- aid: braintree:vault-api
  name: Braintree Vault API
  tags:
  - Customers
  - Payment Methods
  - PCI Compliance
  - Storage
  - Vault
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.braintreegateway.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/customers/overview
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/customers/overview
    type: Documentation
  - url: openapi/braintree-payments-openapi.yml
    type: OpenAPI
  description: The Braintree Vault API provides secure, PCI-compliant long-term storage of customer payment method data. It allows merchants to store credit card numbers, PayPal accounts, and other payment methods so that returning customers do not need to re-enter their information. The Vault supports customer records that can hold multiple payment methods, billing addresses, and associated transaction history.
- aid: braintree:subscriptions-api
  name: Braintree Subscriptions API
  tags:
  - Payments
  - Plans
  - Recurring Billing
  - Subscriptions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.braintreegateway.com
  humanURL: https://developer.paypal.com/braintree/docs/guides/recurring-billing/overview
  properties:
  - url: https://developer.paypal.com/braintree/docs/guides/recurring-billing/overview
    type: Documentation
  - url: openapi/braintree-subscriptions-openapi.yml
    type: OpenAPI
  description: The Braintree Subscriptions API enables merchants to manage recurring billing plans and customer subscriptions. Merchants define billing plans with configurable pricing, billing cycles, and trial periods, then subscribe customers using vaulted payment methods. The API handles automatic charge retries, prorated billing for mid-cycle changes, add-ons and discounts, and subscription lifecycle events.
name: Braintree
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Our mission is to empower developers with the tools, resources, and simple-to-use SDKs and APIs to build on one platform, so they can serve merchants from around the world.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

