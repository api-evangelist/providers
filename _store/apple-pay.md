---
name: Apple Pay
description: Apple Pay enables secure, frictionless payments in apps and on the web using the payment cards stored in users' Apple Wallet. It supports Touch ID, Face ID, and Apple Watch authentication for both in-person and online payments. Apple Pay is available on iOS, watchOS, macOS, and via Safari on the web through the Apple Pay JS API, with a PassKit native framework for iOS/watchOS app integration.
image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
created: '2024-01-01'
modified: '2026-04-19'
url: https://developer.apple.com/apple-pay/
specificationVersion: '0.18'
tags:
  - Apple
  - Contactless Payments
  - Digital Wallet
  - E-Commerce
  - Mobile Payments
  - Payments
apis:
  - name: Apple Pay JS API
    description: Server-side REST API for Apple Pay on the Web, enabling merchants to validate their identity with Apple and obtain payment sessions used by the ApplePaySession JavaScript API in Safari. Supports Touch ID and Face ID for frictionless web checkout.
    image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
    humanURL: https://developer.apple.com/documentation/apple_pay_on_the_web
    baseURL: https://apple-pay-gateway.apple.com
    tags:
      - Javascript
      - Safari
      - Web Payments
    properties:
      - type: Documentation
        url: https://developer.apple.com/documentation/apple_pay_on_the_web
      - type: GettingStarted
        url: https://developer.apple.com/apple-pay/implementation/
      - type: APIReference
        url: https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest
      - type: Sandbox
        url: https://developer.apple.com/apple-pay/sandbox-testing/
      - type: OpenAPI
        url: openapi/apple-pay-js-openapi.yml
      - type: JSONSchema
        url: json-schema/apple-pay-payment-request-schema.json
        title: Payment Request Schema
    contact:
      - FN: Apple Developer Support
        email: developer@apple.com
        url: https://developer.apple.com/contact/
  - name: PassKit Framework (Apple Pay)
    description: Native iOS, watchOS, and macOS framework for integrating Apple Pay into mobile and desktop applications. Provides PKPaymentRequest and PKPaymentAuthorizationViewController for in-app Apple Pay checkout.
    image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
    humanURL: https://developer.apple.com/documentation/passkit
    baseURL: Native Framework
    tags:
      - iOS
      - Mobile
      - Native
      - Swift
    properties:
      - type: Documentation
        url: https://developer.apple.com/documentation/passkit/apple_pay
      - type: APIReference
        url: https://developer.apple.com/documentation/passkit/pkpaymentrequest
      - type: CodeExamples
        url: https://developer.apple.com/documentation/passkit/apple_pay/offering_apple_pay
        title: Sample Code
      - type: YouTube
        url: https://developer.apple.com/videos/frameworks/wallet-and-apple-pay
  - name: Apple Pay Payment Token API
    description: Server-side specification for processing and decrypting Apple Pay payment tokens received from client applications. Tokens use EC_v1 or RSA_v1 encryption and contain the payment authorization data for charge processing.
    image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
    humanURL: https://developer.apple.com/documentation/passkit/apple_pay/payment_token_format_reference
    baseURL: Merchant Server
    tags:
      - Encryption
      - Payment Processing
      - Server-Side
    properties:
      - type: Documentation
        url: https://developer.apple.com/documentation/passkit/apple_pay/payment_token_format_reference
      - type: OpenAPI
        url: openapi/apple-pay-payment-token-openapi.yml
      - type: JSONSchema
        url: json-schema/apple-pay-payment-token-schema.json
        title: Payment Token Schema
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.apple.com/account/
  - type: Support
    url: https://developer.apple.com/support/apple-pay/
  - type: TermsOfService
    url: https://developer.apple.com/apple-pay/acceptable-use-guidelines/
  - type: GettingStarted
    url: https://developer.apple.com/apple-pay/get-started/
  - type: Branding
    url: https://developer.apple.com/apple-pay/marketing/
  - type: StatusPage
    url: https://developer.apple.com/system-status/
  - type: JSONLD
    url: json-ld/apple-pay-context.jsonld
  - type: SpectralRules
    url: rules/apple-pay-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apple-pay-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/apple-pay-js.yaml
    title: Apple Pay JS Shared Capability
  - type: NaftikoCapability
    url: capabilities/payment-processing.yaml
    title: Payment Processing Workflow
  - type: Features
    data:
      - name: Touch ID and Face ID Authentication
        description: Users authorize payments using biometric authentication on Apple devices
      - name: In-App Payments
        description: Native iOS and watchOS integration via PassKit framework
      - name: Web Payments
        description: Safari-based Apple Pay checkout via the ApplePaySession JavaScript API
      - name: Apple Watch Support
        description: Contactless payments from Apple Watch without needing iPhone
      - name: Multiple Card Networks
        description: Supports Visa, Mastercard, Amex, Discover, JCB, UnionPay, and more
      - name: Merchant Domain Verification
        description: Domain verification ensures only registered merchants can use Apple Pay
      - name: Recurring Payments
        description: Subscription and automatic payment support via automatic payment requests
      - name: Deferred Payments
        description: Support for deferred billing like hotel deposits and pre-orders
  - type: UseCases
    data:
      - name: E-Commerce Checkout
        description: One-tap checkout on web and mobile using saved payment cards
      - name: In-App Purchases
        description: Native iOS app purchases with Face ID or Touch ID authentication
      - name: Subscription Billing
        description: Setting up recurring subscription payments authorized by the user
      - name: Contactless In-Store Payments
        description: Tap-to-pay at point-of-sale terminals using iPhone or Apple Watch
      - name: Transit Payments
        description: Paying for transit and transportation with Express Mode
  - type: Integrations
    data:
      - name: Stripe
        description: Stripe Elements and Stripe.js support Apple Pay via the Payment Request Button
      - name: Braintree
        description: PayPal's Braintree SDK provides Apple Pay integration for iOS and web
      - name: Square
        description: Square's iOS SDK supports Apple Pay for in-app and contactless payments
      - name: Adyen
        description: Adyen payment platform supports Apple Pay for web and mobile checkout
      - name: Shopify
        description: Shopify natively supports Apple Pay for accelerated checkout
      - name: WooCommerce
        description: WooCommerce Stripe plugin enables Apple Pay on WordPress stores
---
