---
aid: bancontact
name: Bancontact
description: Bancontact is Belgium's most popular electronic payment system, operating through the Bancontact Payconiq Company (now transitioning to Bancontact Pro brand). The platform provides debit card payments, QR code payments, and mobile payments via the Payconiq by Bancontact app. The REST API enables merchants to accept payments online, in-app, and via QR codes with settlement in Belgian bank accounts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Belgium
  - Debit Cards
  - E-Commerce
  - Fintech
  - Payments
url: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: bancontact:payconiq-acceptance-api
    name: Bancontact Payconiq Acceptance API
    description: REST API for accepting Bancontact payments online and via QR code. Enables merchants to create payment transactions, generate QR codes, handle callbacks, and process refunds. The API is organized around REST with HTTP response codes, header authentication, and standard HTTP verbs. Transitioning to Bancontact Pro branding in 2026.
    humanURL: https://docs.bancontactpro.com/
    tags:
      - Checkout
      - Payments
      - QR Code
      - Transactions
      - Refunds
    properties:
      - type: Documentation
        url: https://docs.bancontactpro.com/
      - type: Documentation
        url: https://docs.payconiq.be/
        name: Legacy Payconiq Documentation
common:
  - type: Website
    url: https://www.bancontact.com/
    name: Bancontact
  - type: Documentation
    url: https://docs.bancontactpro.com/
    name: Bancontact Pro Developer Portal
  - type: SpectralRules
    url: rules/bancontact-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bancontact-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/bancontact-payment-capability.yaml
  - type: JSON-LD
    url: json-ld/bancontact-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Online Payments
        description: Accept Bancontact debit card payments in e-commerce checkouts.
      - name: QR Code Payments
        description: Generate QR codes for in-store and contactless payment acceptance.
      - name: Mobile App Payments
        description: Payconiq by Bancontact app integration for mobile checkout.
      - name: Webhooks
        description: Real-time payment status notifications via webhook callbacks.
      - name: Refunds
        description: Programmatic refund processing for completed transactions.
      - name: Multi-currency
        description: EUR-denominated payments with Belgian bank account settlement.
      - name: Deep Links
        description: Mobile deep links to open the Payconiq app directly from merchant checkout.
  - name: UseCases
    type: UseCases
    data:
      - name: E-Commerce Checkout
        description: Accept Bancontact as a local Belgian payment method at checkout.
      - name: QR Code POS
        description: In-store and restaurant QR code payment acceptance.
      - name: Mobile In-App Payments
        description: Integrate Bancontact into iOS and Android apps.
      - name: Invoice Payments
        description: Payment links and QR codes for invoicing and B2C collections.
      - name: Subscription Billing
        description: Recurring payment collection from Belgian consumers.
  - name: Integrations
    type: Integrations
    data:
      - name: Adyen
        description: Accept Bancontact via Adyen payment gateway.
      - name: Computop
        description: Accept Bancontact via Computop payment platform.
      - name: PPRO
        description: Access Bancontact via PPRO's local payment method network.
      - name: Stripe
        description: Accept Bancontact via Stripe payment infrastructure.
      - name: Mollie
        description: Accept Bancontact via Mollie payment service.
      - name: MultiSafepay
        description: Accept Bancontact via MultiSafepay payment gateway.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
