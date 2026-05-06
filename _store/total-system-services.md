---
aid: total-system-services
url: https://raw.githubusercontent.com/api-evangelist/total-system-services/refs/heads/main/apis.yml
apis:
  - aid: total-system-services:tsys-payment-gateway
    name: TSYS Payment Gateway
    tags:
      - Payments
      - Payment Processing
      - Credit Card
      - Transactions
      - POS
    humanURL: https://developers.tsys.com/
    properties:
      - url: https://developers.tsys.com/
        type: Documentation
      - url: openapi/tsys-payment-gateway-openapi.yml
        type: OpenAPI
    description: TSYS Payment Gateway API enables merchants to process credit, debit, and prepaid card transactions. Supports authorization, capture, void, and refund operations for card-present and card-not-present payment scenarios.
  - aid: total-system-services:tsys-issuing
    name: TSYS Issuing Platform
    tags:
      - Payments
      - Card Issuing
      - Account Management
      - Digital Payments
      - Fintech
    humanURL: https://www.tsys.com/platform
    properties:
      - url: https://www.tsys.com/platform
        type: Documentation
      - url: openapi/tsys-issuing-openapi.yml
        type: OpenAPI
    description: TSYS Issuing Platform provides an API-driven payment stack for financial institutions and fintechs to issue debit and credit cards, manage cardholder accounts, set spending controls, and handle transaction disputes.
  - aid: total-system-services:tsys-merchant
    name: TSYS Merchant Services
    tags:
      - Payments
      - Merchant Management
      - Acquiring
      - Boarding
      - Settlement
    humanURL: https://docs.tsysmerchant.com/
    properties:
      - url: https://docs.tsysmerchant.com/
        type: Documentation
      - url: openapi/tsys-merchant-openapi.yml
        type: OpenAPI
    description: TSYS Merchant Services API provides merchant boarding, account management, reporting, and settlement services for acquirers and payment facilitators integrating with the TSYS acquiring platform.
common:
  - type: Website
    url: https://www.tsys.com/
  - type: Developer
    url: https://developers.tsys.com/
  - type: Documentation
    url: https://docs.tsysmerchant.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/tsys
  - type: Rules
    url: rules/tsys-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/total-system-services-vocabulary.yml
  - type: JSONLDContext
    url: json-ld/total-system-services-context.jsonld
name: Total System Services
tags:
  - Payments
  - Payment Processing
  - Card Issuing
  - Merchant Services
  - Fintech
  - Financial Services
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-24'
modified: '2026-05-03'
position: Consumer
description: Total System Services (TSYS) was a leading global payment solutions provider offering payment processing services to financial and nonfinancial institutions before merging with Global Payments in 2019. TSYS provides an end-to-end payment stack spanning payment gateway services for merchants, card issuing for banks and fintechs, merchant acquiring and boarding, virtual card programs, and comprehensive reporting. The TSYS developer portal provides APIs for transaction processing, cardholder management, merchant services, and commercial virtual solutions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
