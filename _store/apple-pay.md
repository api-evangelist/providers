---
aid: apple-pay
url: https://raw.githubusercontent.com/api-evangelist/apple-pay/refs/heads/main/apis.yml
apis:
- name: Apple Pay JS API
  description: Use Apple Pay on the web to accept payments in Safari on iOS, iPadOS, and macOS. It allows users to authorize payments using Touch ID or Face ID.
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
  - type: Getting Started
    url: https://developer.apple.com/apple-pay/implementation/
  - type: Merchant Guide
    url: https://developer.apple.com/documentation/passkit/apple_pay/setting_up_apple_pay
  - type: API Reference
    url: https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest
  - type: Sandbox
    url: https://developer.apple.com/apple-pay/sandbox-testing/
  - type: OpenAPI
    url: openapi/apple-pay-js-openapi.yml
- name: PassKit Framework (Apple Pay)
  description: Native API for integrating Apple Pay into iOS, watchOS, and macOS applications using PassKit framework.
  image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
  humanURL: https://developer.apple.com/documentation/passkit
  baseURL: Native Framework
  tags:
  - Ios
  - Mobile
  - Native
  - Swift
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/passkit/apple_pay
  - type: API Reference
    url: https://developer.apple.com/documentation/passkit/pkpaymentrequest
  - type: Sample Code
    url: https://developer.apple.com/documentation/passkit/apple_pay/offering_apple_pay
  - type: WWDC Videos
    url: https://developer.apple.com/videos/frameworks/wallet-and-apple-pay
  - type: Human Interface Guidelines
    url: https://developer.apple.com/design/human-interface-guidelines/apple-pay
- name: Apple Pay Payment Token API
  description: Server-side API for processing and decrypting Apple Pay payment tokens received from client applications.
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
  - type: Specification
    url: https://developer.apple.com/library/archive/documentation/PassKit/Reference/PaymentTokenJSON/PaymentTokenJSON.html
  - type: OpenAPI
    url: openapi/apple-pay-payment-token-openapi.yml
name: Apple Pay
tags:
- Contactless Payments
- Digital Wallet
- E-Commerce
- Mobile Payments
- Payments
type: Contract
image: https://developer.apple.com/assets/elements/icons/apple-pay/apple-pay-96x96.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apple Pay enables secure, simple checkouts in your app or website. Customers can purchase physical goods and services using the payment cards they've securely stored in their Wallet app.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

