---
aid: google-pay
name: Google Pay
description: Google Pay APIs enable payment processing and digital wallet functionality for apps and websites.
image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
url: https://developers.google.com/pay/api
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Contactless Payments
  - Digital Wallet
  - Mobile Payments
  - Payments
apis:
  - name: Google Pay API
    description: Enables integration of the Google Pay payment method into web applications, allowing merchants to accept payments from cards saved to Google Accounts. The API provides JavaScript client methods for implementing a seamless checkout experience on websites.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay
    baseURL: https://pay.google.com/gp/v/
    tags:
      - Checkout
      - Payments
      - Web
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/api/web
      - type: OpenAPI
        url: https://developers.google.com/pay/api/web/reference/rest
      - type: Authentication
        url: https://developers.google.com/pay/api/web/guides/setup
      - type: Errors
        url: https://developers.google.com/pay/api/web/reference/error-codes
      - type: Sandbox
        url: https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist
      - type: Reference
        url: https://developers.google.com/pay/api/web/reference/client
      - type: Getting Started
        url: https://developers.google.com/pay/api/web/guides/tutorial
      - type: Change Log
        url: https://developers.google.com/pay/api/web/support/release-notes
    contact:
      - type: Support
        url: https://developers.google.com/pay/api/web/support
      - type: Twitter
        url: https://twitter.com/googlepay
  - name: Google Pay API for Android
    description: Enables integration of Google Pay into Android applications, allowing users to pay with cards saved to their Google Account. The API provides methods to check payment readiness and load payment data for seamless in-app checkout experiences.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/api/android/overview
    baseURL: https://pay.google.com/gp/v/
    tags:
      - Android
      - Checkout
      - Mobile
      - Payments
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/api/android/overview
      - type: Reference
        url: https://developers.google.com/pay/api/android/reference/client
      - type: Getting Started
        url: https://developers.google.com/pay/api/android/guides/tutorial
      - type: Authentication
        url: https://developers.google.com/pay/api/android/guides/setup
      - type: Change Log
        url: https://developers.google.com/pay/api/android/support/release-notes
      - type: Sandbox
        url: https://developers.google.com/pay/api/android/guides/test-and-deploy/integration-checklist
  - name: Google Wallet API
    description: APIs for creating and managing digital passes for Google Wallet, including loyalty cards, event tickets, boarding passes, transit tickets, gift cards, offers, and generic passes. Issuers can define pass classes and objects via REST API or the Google Wallet Business Console.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/wallet
    baseURL: https://walletobjects.googleapis.com/
    tags:
      - Loyalty
      - Passes
      - Tickets
      - Wallet
    properties:
      - type: Documentation
        url: https://developers.google.com/wallet/generic/rest
      - type: OpenAPI
        url: https://developers.google.com/wallet/generic/rest/v1
      - type: Authentication
        url: https://developers.google.com/wallet/generic/rest/prerequisites
      - type: Reference
        url: https://developers.google.com/wallet/reference/rest
      - type: Getting Started
        url: https://developers.google.com/wallet/generic/getting-started/auth/rest
      - type: Change Log
        url: https://developers.google.com/wallet/docs/release-notes
      - type: Client Libraries
        url: https://developers.google.com/wallet/generic/resources/libraries
  - name: Google Pay Facilitated Transaction Event API
    description: Provides services hosted by Google for processing facilitated payment events as part of Google Standard Payments. Payment integrators use this API to report and manage transaction events within the Google payments ecosystem.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/facilitated-transaction-event-v2/concepts/intro
    baseURL: https://pay.google.com/
    tags:
      - Payment Integrators
      - Payments
      - Transactions
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/facilitated-transaction-event-v2/concepts/intro
      - type: Reference
        url: https://developers.google.com/pay/facilitated-transaction-event-v2/google-facilitated-transaction-event-api
  - name: Google Pay Virtual Cards API
    description: Enables payment integrators to enroll cards, retrieve virtual card numbers, manage transactions, and handle authentication challenges for virtual card payments. Used by issuers and payment service providers to support virtual card number generation and lifecycle management.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/virtual-cards-v1/payment-integrator-virtual-cards-api
    baseURL: https://pay.google.com/
    tags:
      - Card Issuance
      - Payments
      - Virtual Cards
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/virtual-cards-v1/payment-integrator-virtual-cards-api
      - type: Reference
        url: https://developers.google.com/pay/virtual-cards-v1/google-virtual-cards-api
  - name: Google Pay Push Provisioning API
    description: Allows card issuers to provision payment cards directly into Google Pay and Google Wallet from their own applications. Issuers can set default payment tokens, manage token lifecycle, and enable push provisioning flows for their cardholders.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/issuers/apis/push-provisioning/server
    baseURL: https://pay.google.com/
    tags:
      - Card Provisioning
      - Issuers
      - Payments
      - Tokenization
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/issuers/apis/push-provisioning/server
      - type: Getting Started
        url: https://developers.google.com/pay/issuers/overview/get-started
  - name: Google Pay Payment Card Recognition API
    description: Enables Android applications to scan credit and debit cards using the device camera to extract card number and expiration date through on-device optical character recognition. Processing occurs entirely on-device via Google Play Services without requiring camera permissions in the app.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition
    baseURL: https://pay.google.com/
    tags:
      - Android
      - Card Recognition
      - OCR
      - Payments
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/payment-card-recognition/debit-credit-card-recognition
  - name: Google Pay India Merchant SDK
    description: A toolkit for developers in India to integrate their Android, iOS, and web applications with Google Pay for accepting UPI and card-based payments. Supports merchant onboarding, payment initiation, and transaction status verification through the Google Pay for Business program.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/pay/india/api
    baseURL: https://pay.google.com/
    tags:
      - India
      - Merchant SDK
      - Payments
      - UPI
    properties:
      - type: Documentation
        url: https://developers.google.com/pay/india/api/merchant-sdk/guides/overview
      - type: Reference
        url: https://developers.google.com/pay/india/api/merchant-sdk/reference/api
      - type: Getting Started
        url: https://developers.google.com/pay/india/api/merchant-sdk/guides/integration
      - type: Authentication
        url: https://developers.google.com/pay/india/api/merchant-sdk/guides/setup
  - name: Google Universal Commerce Protocol
    description: A standard for securely and efficiently exchanging commerce data between merchant and platform systems to enable checkout experiences directly on Google surfaces including Search and Gemini. Merchants implement REST endpoints for session creation, updates, and completion.
    image: https://developers.google.com/pay/api/images/brand-guidelines/google-pay-mark.png
    humanURL: https://developers.google.com/merchant/ucp
    baseURL: https://pay.google.com/
    tags:
      - Agentic Commerce
      - Checkout
      - Commerce
      - Merchants
    properties:
      - type: Documentation
        url: https://developers.google.com/merchant/ucp/guides
      - type: Getting Started
        url: https://developers.google.com/pay/api/universal-commerce-protocol/overview
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developers.google.com/pay
  - type: Brand Guidelines
    url: https://developers.google.com/pay/api/web/guides/brand-guidelines
  - type: Terms of Service
    url: https://payments.developers.google.com/terms/sellertos
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Getting Started
    url: https://developers.google.com/pay/api/web/guides/tutorial
  - type: SDK
    url: https://developers.google.com/pay/api/web/guides/resources
  - type: Console
    url: https://pay.google.com/business/console/
  - type: Status
    url: https://developers.google.com/pay/api/status
  - type: Support
    url: https://developers.google.com/pay/api/web/support
  - type: Blog
    url: https://developers.googleblog.com/
  - type: Change Log
    url: https://developers.google.com/pay/api/web/support/release-notes
  - type: GitHub Organization
    url: https://github.com/google-pay
  - type: FAQ
    url: https://developers.google.com/pay/api/web/support/faq
---
