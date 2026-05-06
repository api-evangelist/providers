---
aid: chase
name: Chase
description: JPMorgan Chase Bank, N.A. is a leading US financial institution providing consumer and commercial banking, credit cards, mortgages, and merchant services. The Chase Developer Portal exposes APIs for FDX-aligned account aggregation, customer consent, rewards balances, and the Loyalty Pay with Points platform that lets enrolled merchants and partners enable customers to redeem Ultimate Rewards points at checkout.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chase/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Account Aggregation
  - Banking
  - Consent
  - Credit Cards
  - FDX
  - Financial Services
  - Loyalty
  - Open Banking
  - Pay with Points
  - Rewards
created: '2025-02-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chase:account-and-customer-information-api
    name: Chase Account and Customer Information API
    description: FDX-aligned API that allows authorized data recipients to securely retrieve account and customer information for Chase customers. Supports account profiles, balances, transactions, statements, and customer details using OAuth 2.0 with FDX consent flows.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/aggregation-fdx/
    baseURL: https://api.chase.com/aggregation/fdx
    tags:
      - Account Aggregation
      - FDX
      - Open Banking
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/aggregation-fdx/guides/using-the-account-and-customer-information-api/
      - type: OpenAPI
        url: openapi/chase-account-and-customer-information-api-openapi.yml
  - aid: chase:account-aggregation-user-consent-api
    name: Chase Account Aggregation User Consent API
    description: Consent management API used to obtain, store, and revoke customer consent for sharing account information with authorized third-party data recipients. Implements the FDX consent model.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/aggregation-consent/
    baseURL: https://api.chase.com/aggregation/consent
    tags:
      - Consent
      - FDX
      - Open Banking
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/aggregation-consent/
      - type: OpenAPI
        url: openapi/chase-account-aggregation-user-consent-api-openapi.yml
  - aid: chase:rewards-balance-api
    name: Chase Rewards Balance API
    description: API that allows merchant and partner systems to retrieve a Chase cardholder's current rewards points balance for use in loyalty experiences and Pay with Points checkouts.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/rewards-balance-api/
    baseURL: https://api.chase.com/loyalty/rewards-balance
    tags:
      - Loyalty
      - Rewards
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/rewards-balance-api/specification
      - type: OpenAPI
        url: openapi/chase-rewards-balance-api-openapi.yml
  - aid: chase:loyalty-pay-with-points-order-service-api
    name: Chase Loyalty Pay with Points Order Service API
    description: API that lets merchants accept Chase Ultimate Rewards points as payment at checkout. Supports order creation, redemption, capture, refund, and reversal flows for the Pay with Points program.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/loyalty-pay-with-points-order-service/
    baseURL: https://api.chase.com/loyalty/pay-with-points/orders
    tags:
      - Loyalty
      - Payments
      - Rewards
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/loyalty-pay-with-points-order-service/
      - type: OpenAPI
        url: openapi/chase-loyalty-pay-with-points-order-service-api-openapi.yml
  - aid: chase:loyalty-pay-with-points-enrollment-service-api
    name: Chase Loyalty Pay with Points Enrollment Service API
    description: API that allows merchants and partners to enroll customer payment cards in the Chase Pay with Points program so points can be redeemed against future purchases.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/loyalty-pay-with-points-enrollment-service/
    baseURL: https://api.chase.com/loyalty/pay-with-points/enrollment
    tags:
      - Loyalty
      - Payments
      - Rewards
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/loyalty-pay-with-points-enrollment-service/
      - type: OpenAPI
        url: openapi/chase-loyalty-pay-with-points-enrollment-service-api-openapi.yml
  - aid: chase:loyalty-pci-merchant-relationship-manager-api
    name: Chase Loyalty PCI Merchant Relationship Manager API
    description: API for managing PCI-compliant merchant relationships for the Chase loyalty platform, supporting onboarding, profile updates, and configuration of merchant integrations.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.chase.com/products/loyalty-pci-merchant-relation-manager/
    baseURL: https://api.chase.com/loyalty/merchant-relationship-manager
    tags:
      - Loyalty
      - Merchants
      - PCI
    properties:
      - type: Documentation
        url: https://developer.chase.com/products/loyalty-pci-merchant-relation-manager/
      - type: OpenAPI
        url: openapi/chase-loyalty-pci-merchant-relationship-manager-api-openapi.yml
common:
  - type: Website
    url: https://www.chase.com/
  - type: DeveloperPortal
    url: https://developer.chase.com/
  - type: Portal
    url: https://developer.chase.com/
  - type: Demo
    url: https://apidemo.chase.com/
  - type: FAQ
    url: https://developer.chase.com/support/faqs
  - type: Glossary
    url: https://developer.chase.com/support/glossary/
  - type: Support
    url: https://developer.chase.com/support
  - type: TermsOfService
    url: https://developer.chase.com/terms
  - type: PrivacyPolicy
    url: https://www.chase.com/digital/resources/privacy-security
  - type: JSONLD
    url: json-ld/chase-context.jsonld
  - type: JSONSchema
    url: json-schema/chase-account-schema.json
  - type: JSONSchema
    url: json-schema/chase-rewards-balance-schema.json
  - type: Spectral
    url: spectral/chase-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/chase-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
