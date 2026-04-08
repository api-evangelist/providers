---
aid: affirm
url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/apis.yml
apis:
- aid: affirm:direct-api
  name: Affirm Direct API
  tags:
  - Buy Now Pay Later
  - Checkout
  - Fintech
  - Merchant
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.affirm.com
  humanURL: https://docs.affirm.com/payments/docs/direct-api-overview
  properties:
  - url: https://docs.affirm.com/payments/docs/direct-api-overview
    type: Documentation
  - url: openapi/affirm-direct-api-openapi.yml
    type: OpenAPI
  description: The Affirm Direct API is a flexible integration that allows merchants to embed the full Affirm checkout and payment authorization flow directly into their website, giving complete control over the front-end user experience and back-end transaction processing logic. It supports inline checkout via modal or redirect to affirm.com, and handles the full transaction lifecycle including authorization, capture, void, and refund operations.
- aid: affirm:checkout-api
  name: Affirm Checkout API
  tags:
  - Buy Now Pay Later
  - Checkout
  - Fintech
  - Merchant
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.affirm.com
  humanURL: https://docs.affirm.com/developers/docs/home-introduction
  properties:
  - url: https://docs.affirm.com/developers/docs/home-introduction
    type: Documentation
  - url: openapi/affirm-checkout-openapi.yml
    type: OpenAPI
  - url: json-schema/affirm-checkout-schema.json
    type: JSONSchema
  description: The Affirm Checkout API enables merchants to initiate and manage the Affirm buy now pay later checkout flow for customers at the point of purchase. It provides endpoints to create checkout sessions, read and update checkout objects, and store checkout tokens returned after a customer completes the Affirm financing application. The API supports both redirect and direct checkout integration patterns, and includes endpoints for resending checkout links via email or SMS.
- aid: affirm:transactions-api
  name: Affirm Transactions API
  tags:
  - Authorization
  - Capture
  - Fintech
  - Payments
  - Refunds
  - Transactions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.affirm.com
  humanURL: https://docs.affirm.com/developers/reference/introduction
  properties:
  - url: https://docs.affirm.com/developers/reference/introduction
    type: Documentation
  - url: openapi/affirm-transactions-openapi.yml
    type: OpenAPI
  - url: json-schema/affirm-transaction-schema.json
    type: JSONSchema
  description: The Affirm Transactions API provides server-side endpoints for managing the full lifecycle of Affirm payment transactions after a customer completes checkout. It supports authorization, capture, void, and refund operations, as well as listing and retrieving transaction details and associated settlement events. Merchants use this API to reconcile charges, process partial or full refunds, and track disbursement activity.
- aid: affirm:promos-api
  name: Affirm Promos API
  tags:
  - Buy Now Pay Later
  - Marketing
  - Merchant
  - Messaging
  - Promotions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://www.affirm.com/api/promos/v2
  humanURL: https://docs.affirm.com/developers/docs/promos-api-integration-overview
  properties:
  - url: https://docs.affirm.com/developers/docs/promos-api-integration-overview
    type: Documentation
  - url: openapi/affirm-promos-openapi.yml
    type: OpenAPI
  description: The Affirm Promos API is a server-side endpoint that enables merchants to render dynamic promotional pricing text and present Affirm-hosted educational modals on their website. It accepts a purchase amount and returns financing terms, "as low as" monthly payment messaging, APR rates, and modal content including headlines, descriptions, and legal disclosures. The API supports multiple installment term options and page-type context (product, cart, homepage) to customize the displayed messaging.
- aid: affirm:disputes-api
  name: Affirm Disputes API
  tags:
  - Chargebacks
  - Disputes
  - Fintech
  - Merchant
  - Payments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.affirm.com
  humanURL: https://docs.affirm.com/developers/reference/introduction
  properties:
  - url: https://docs.affirm.com/developers/reference/introduction
    type: Documentation
  - url: openapi/affirm-disputes-openapi.yml
    type: OpenAPI
  - url: json-schema/affirm-dispute-schema.json
    type: JSONSchema
  description: The Affirm Disputes API (V3) provides merchants with programmatic access to manage payment disputes initiated by customers. It supports listing and retrieving individual dispute records, submitting evidence to contest a dispute, and closing disputes. The API integrates with the file upload capability so merchants can attach supporting documentation as evidence when responding to disputes.
- aid: affirm:mobile-sdk-ios
  name: Affirm iOS SDK
  tags:
  - Buy Now Pay Later
  - iOS
  - Mobile
  - Objective-C
  - SDK
  - Swift
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.affirm.com/developers/docs/ios-sdk-overview
  properties:
  - url: https://docs.affirm.com/developers/docs/ios-sdk-overview
    type: Documentation
  description: The Affirm iOS SDK provides a native library for integrating Affirm buy now pay later checkout into iOS applications. It handles presenting the Affirm checkout flow within a mobile webview and returning the checkout token to the host app upon customer authorization. The SDK supports Swift and Objective-C and includes components for rendering Affirm promotional messaging within native iOS UI.
- aid: affirm:mobile-sdk-android
  name: Affirm Android SDK
  tags:
  - Android
  - Buy Now Pay Later
  - Java
  - Kotlin
  - Mobile
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.affirm.com/developers/docs/android-sdk-overview
  properties:
  - url: https://docs.affirm.com/developers/docs/android-sdk-overview
    type: Documentation
  description: The Affirm Android SDK provides a native library for embedding the Affirm buy now pay later checkout experience into Android applications. It manages the checkout webview flow, handles deep link callbacks, and returns a checkout token to the host application upon successful customer authorization. The SDK supports Java and Kotlin and includes components for displaying Affirm promotional messaging within native Android UI.
name: Affirm
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Affirm is a financial technology company that provides buy now, pay later financing for consumers at the point of sale across thousands of online and in-store merchants.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

