---
aid: pin-payments
name: Pin Payments
description: A complete payments solution, built for speed and simplicity around your unique business needs. The Pin Payments API enables developers to charge cards, manage customers, store payment sources, issue refunds, and run subscriptions through a RESTful JSON interface secured with HTTP Basic authentication.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Payments
  - Cards
  - Subscriptions
  - Refunds
created: '2025-02-17'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/pin-payments/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pin-payments:pin-payments
    name: Pin Payments API
    description: The Pin Payments API exposes resources for charges, customers, cards, refunds, and subscriptions. It is a RESTful JSON API authenticated with HTTP Basic using your API key as the username and an empty string as the password. Live and test environments are available at api.pinpayments.com and test-api.pinpayments.com respectively.
    humanURL: https://pinpayments.com/
    baseURL: https://api.pinpayments.com/1
    tags:
      - Payments
      - Charges
      - Customers
      - Cards
      - Refunds
    properties:
      - type: Documentation
        url: https://pinpayments.com/developers/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pin-payments/refs/heads/main/openapi/pin-payments-openapi.yaml
common:
  - type: Website
    url: https://pinpayments.com/
  - type: Documentation
    url: https://pinpayments.com/developers/api-reference
  - type: Pricing
    url: https://pinpayments.com/pricing
  - type: SignUp
    url: https://dashboard.pinpayments.com/sign_up
  - type: Login
    url: https://dashboard.pinpayments.com/sign_in
  - type: TermsOfService
    url: https://pinpayments.com/legals/terms-of-use
  - type: PrivacyPolicy
    url: https://pinpayments.com/legals/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
