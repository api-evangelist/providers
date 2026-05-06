---
aid: affirm
url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/apis.yml
modified: '2026-04-19'
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
  - aid: affirm:cards-api
    name: Affirm Cards API
    tags:
      - Cards
      - Fintech
      - Payments
      - Virtual Card
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.affirm.com
    humanURL: https://docs.affirm.com/developers/reference/introduction
    properties:
      - url: https://docs.affirm.com/developers/reference/introduction
        type: Documentation
    description: The Affirm Cards API enables merchants to create and manage virtual card (VCN) transactions for Affirm Lite integrations. It supports creating, reading, finalizing, and canceling virtual cards that can be used anywhere major credit cards are accepted, providing a seamless buy now pay later experience without requiring direct API integration for the merchant's payment processor.
  - aid: affirm:files-api
    name: Affirm Files API
    tags:
      - Disputes
      - Files
      - Fintech
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.affirm.com
    humanURL: https://docs.affirm.com/developers/reference/introduction
    properties:
      - url: https://docs.affirm.com/developers/reference/introduction
        type: Documentation
    description: The Affirm Files API provides endpoints for uploading supporting documentation that can be attached as evidence when responding to payment disputes. It is used in conjunction with the Disputes API to submit files such as receipts, order confirmations, shipping records, or customer communications.
  - aid: affirm:prequal-api
    name: Affirm Prequalification API
    tags:
      - Buy Now Pay Later
      - Credit
      - Fintech
      - Prequalification
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.affirm.com
    humanURL: https://docs.affirm.com/developers/reference/introduction
    properties:
      - url: https://docs.affirm.com/developers/reference/introduction
        type: Documentation
    description: The Affirm Prequalification API allows merchants to check whether a customer is prequalified for Affirm financing before they reach checkout. This enables merchants to surface Affirm messaging and financing options only to eligible customers, improving conversion rates and customer experience across the shopping journey.
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
      - url: https://github.com/Affirm/affirm-merchant-sdk-ios
        type: SDK
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
      - url: https://github.com/Affirm/affirm-merchant-sdk-android
        type: SDK
    description: The Affirm Android SDK provides a native library for embedding the Affirm buy now pay later checkout experience into Android applications. It manages the checkout webview flow, handles deep link callbacks, and returns a checkout token to the host application upon successful customer authorization. The SDK supports Java and Kotlin and includes components for displaying Affirm promotional messaging within native Android UI.
common:
  - type: AsyncAPI
    url: asyncapi/affirm-webhooks-asyncapi.yml
  - type: JSON-LD
    url: json-ld/affirm-context.jsonld
  - type: Portal
    url: https://docs.affirm.com
  - type: GettingStarted
    url: https://docs.affirm.com/developers/docs/home-introduction
  - type: Authentication
    url: https://docs.affirm.com/developers/docs/authentication
  - type: RateLimits
    url: https://docs.affirm.com/developers/docs/rate-limits
  - type: SignUp
    url: https://www.affirm.com/business
  - type: StatusPage
    url: https://status.affirm.com
  - type: GitHubOrganization
    url: https://github.com/Affirm
  - type: TermsOfService
    url: https://www.affirm.com/merchant-tos
  - type: PrivacyPolicy
    url: https://www.affirm.com/privacy
  - type: Support
    url: https://docs.affirm.com/developers/docs/get-support
  - type: Features
    data:
      - name: Buy Now Pay Later
        description: Enable customers to split purchases into installments with 0% APR options and flexible financing terms at checkout.
      - name: Adaptive Checkout
        description: Dynamically present the best financing option (Installments, Pay in 4, etc.) to each customer based on eligibility.
      - name: Virtual Card Network
        description: Issue virtual cards via Affirm Lite so customers can use BNPL anywhere major credit cards are accepted without direct API integration.
      - name: Split Capture
        description: Capture funds from a single Affirm transaction across multiple shipments or fulfillment events.
      - name: Promotional Messaging
        description: Display "as low as" monthly payment messaging on product, cart, and homepage views to increase conversion.
      - name: Prequalification
        description: Check customer eligibility for Affirm financing before checkout to surface relevant offers and improve conversion.
      - name: Webhook Notifications
        description: Receive real-time event notifications for key transaction lifecycle events including authorization, capture, void, and refund.
      - name: Dispute Management
        description: Programmatically manage payment disputes by submitting evidence and tracking dispute status via API.
      - name: Global Integration
        description: Support for merchants in the USA, Canada, and UK with international market configuration.
  - type: UseCases
    data:
      - name: E-Commerce Checkout
        description: Embed Affirm BNPL directly in the checkout flow of an online store to offer customers flexible payment options at the point of purchase.
      - name: Mobile Commerce
        description: Integrate Affirm financing into iOS and Android apps using native mobile SDKs for a seamless in-app BNPL experience.
      - name: Telesales and Assisted Selling
        description: Send checkout links via SMS or email to allow customers to complete Affirm-financed purchases over the phone or remotely.
      - name: In-Store Retail
        description: Enable Affirm BNPL in physical retail environments using virtual card or POS integration flows.
      - name: Transaction Reconciliation
        description: Use the Transactions API to retrieve settlement events and reconcile captured payments against disbursements.
      - name: Dispute Resolution
        description: Automate dispute response workflows by programmatically fetching dispute records and submitting evidence via the Disputes API.
      - name: Promotional Marketing
        description: Use the Promos API to display dynamic financing terms on product pages to increase cart size and conversion.
  - type: Integrations
    data:
      - name: Shopify
        description: Affirm is available as a payment provider plugin for Shopify merchants, enabling BNPL at Shopify-powered checkouts.
      - name: BigCommerce
        description: Native Affirm integration for BigCommerce stores, providing BNPL checkout without custom API development.
      - name: WooCommerce
        description: Affirm plugin for WooCommerce-powered WordPress stores enables BNPL payment options.
      - name: Salesforce Commerce Cloud
        description: Affirm integration for Salesforce Commerce Cloud (SFCC) enterprise e-commerce deployments.
      - name: Magento
        description: Affirm integration for Magento (Adobe Commerce) merchants to enable BNPL checkout.
      - name: Stripe
        description: Affirm is available as a payment method through the Stripe payment platform.
      - name: Braintree
        description: Affirm BNPL is accessible via the Braintree payment gateway for merchants using PayPal infrastructure.
  - type: JSONSchema
    url: json-schema/affirm-checkout-schema.json
  - type: JSONSchema
    url: json-schema/affirm-dispute-schema.json
  - type: JSONSchema
    url: json-schema/affirm-transaction-schema.json
  - type: JSONSchema
    url: json-schema/checkout-address-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-checkout-request-schema.json
  - type: JSONSchema
    url: json-schema/checkout-checkout-schema.json
  - type: JSONSchema
    url: json-schema/checkout-contact-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-discount-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-item-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-merchant-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-name-object-schema.json
  - type: JSONSchema
    url: json-schema/checkout-store-object-schema.json
  - type: JSONSchema
    url: json-schema/direct-api-card-schema.json
  - type: JSONSchema
    url: json-schema/direct-api-file-object-schema.json
  - type: JSONSchema
    url: json-schema/direct-api-transaction-schema.json
  - type: JSONSchema
    url: json-schema/disputes-dispute-schema.json
  - type: JSONSchema
    url: json-schema/disputes-evidence-item-schema.json
  - type: JSONSchema
    url: json-schema/disputes-evidence-request-schema.json
  - type: JSONSchema
    url: json-schema/promos-financing-term-schema.json
  - type: JSONSchema
    url: json-schema/promos-offer-content-schema.json
  - type: JSONSchema
    url: json-schema/promos-promo-config-schema.json
  - type: JSONSchema
    url: json-schema/promos-promo-content-schema.json
  - type: JSONSchema
    url: json-schema/promos-promo-response-schema.json
  - type: JSONSchema
    url: json-schema/transactions-settlement-event-schema.json
  - type: JSONSchema
    url: json-schema/transactions-settlement-event-summary-schema.json
  - type: JSONSchema
    url: json-schema/transactions-transaction-event-schema.json
  - type: JSONSchema
    url: json-schema/transactions-transaction-schema.json
  - type: JSONStructure
    url: json-structure/affirm-checkout-structure.json
  - type: JSONStructure
    url: json-structure/affirm-dispute-structure.json
  - type: JSONStructure
    url: json-structure/affirm-transaction-structure.json
  - type: JSONStructure
    url: json-structure/checkout-address-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-checkout-request-structure.json
  - type: JSONStructure
    url: json-structure/checkout-checkout-structure.json
  - type: JSONStructure
    url: json-structure/checkout-contact-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-discount-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-item-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-merchant-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-name-object-structure.json
  - type: JSONStructure
    url: json-structure/checkout-store-object-structure.json
  - type: JSONStructure
    url: json-structure/direct-api-card-structure.json
  - type: JSONStructure
    url: json-structure/direct-api-file-object-structure.json
  - type: JSONStructure
    url: json-structure/direct-api-transaction-structure.json
  - type: JSONStructure
    url: json-structure/disputes-dispute-structure.json
  - type: JSONStructure
    url: json-structure/disputes-evidence-item-structure.json
  - type: JSONStructure
    url: json-structure/disputes-evidence-request-structure.json
  - type: JSONStructure
    url: json-structure/promos-financing-term-structure.json
  - type: JSONStructure
    url: json-structure/promos-offer-content-structure.json
  - type: JSONStructure
    url: json-structure/promos-promo-config-structure.json
  - type: JSONStructure
    url: json-structure/promos-promo-content-structure.json
  - type: JSONStructure
    url: json-structure/promos-promo-response-structure.json
  - type: JSONStructure
    url: json-structure/transactions-settlement-event-structure.json
  - type: JSONStructure
    url: json-structure/transactions-settlement-event-summary-structure.json
  - type: JSONStructure
    url: json-structure/transactions-transaction-event-structure.json
  - type: JSONStructure
    url: json-structure/transactions-transaction-structure.json
  - type: JSON-LD
    url: json-ld/affirm-checkout-context.jsonld
  - type: JSON-LD
    url: json-ld/affirm-direct-context.jsonld
  - type: JSON-LD
    url: json-ld/affirm-disputes-context.jsonld
  - type: JSON-LD
    url: json-ld/affirm-promos-context.jsonld
  - type: JSON-LD
    url: json-ld/affirm-transactions-context.jsonld
  - type: Example
    url: examples/affirm-checkout-example.json
  - type: Example
    url: examples/affirm-dispute-example.json
  - type: Example
    url: examples/affirm-transaction-example.json
  - type: Example
    url: examples/checkout-address-object-example.json
  - type: Example
    url: examples/checkout-checkout-example.json
  - type: Example
    url: examples/checkout-checkout-request-example.json
  - type: Example
    url: examples/checkout-contact-object-example.json
  - type: Example
    url: examples/checkout-discount-object-example.json
  - type: Example
    url: examples/checkout-item-object-example.json
  - type: Example
    url: examples/checkout-merchant-object-example.json
  - type: Example
    url: examples/checkout-name-object-example.json
  - type: Example
    url: examples/checkout-store-object-example.json
  - type: Example
    url: examples/direct-api-card-example.json
  - type: Example
    url: examples/direct-api-file-object-example.json
  - type: Example
    url: examples/direct-api-transaction-example.json
  - type: Example
    url: examples/disputes-dispute-example.json
  - type: Example
    url: examples/disputes-evidence-item-example.json
  - type: Example
    url: examples/disputes-evidence-request-example.json
  - type: Example
    url: examples/promos-financing-term-example.json
  - type: Example
    url: examples/promos-offer-content-example.json
  - type: Example
    url: examples/promos-promo-config-example.json
  - type: Example
    url: examples/promos-promo-content-example.json
  - type: Example
    url: examples/promos-promo-response-example.json
  - type: Example
    url: examples/transactions-settlement-event-example.json
  - type: Example
    url: examples/transactions-settlement-event-summary-example.json
  - type: Example
    url: examples/transactions-transaction-event-example.json
  - type: Example
    url: examples/transactions-transaction-example.json
  - type: SpectralRules
    url: rules/affirm-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/affirm-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/payment-management.yaml
description: Affirm is a financial technology company that provides buy now, pay later financing for consumers at the point of sale across thousands of online and in-store merchants. Affirm offers a suite of developer APIs and SDKs enabling merchants to embed flexible installment payment options directly into their checkout flows, mobile apps, and marketing experiences.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
