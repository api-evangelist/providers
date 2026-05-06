---
aid: decentro
name: Decentro
url: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Banking-as-a-Service
  - FinTech
  - India
  - KYC
  - Ledger
  - Payments
  - UPI
  - Virtual Accounts
created: '2025-02-24'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: 'Decentro is a banking-as-a-service platform that provides businesses with seamless integration to Indian banking infrastructure - including payments (UPI, IMPS, NEFT, RTGS), virtual accounts, KYC, ledger primitives, and credit-bureau data. Decentro publishes a developer portal and Postman collection covering six API categories: KYC & Onboarding, Bytes (alternate data), Scanner (forensics), Payments, Virtual Accounts, and Ledger.'
apis:
  - aid: decentro:kyc-api
    name: Decentro KYC & Onboarding API
    description: Identity verification, customer onboarding, DigiLocker integration, Aadhaar OTP, document classification, and face match.
    humanURL: https://docs.decentro.tech/
    baseURL: https://in.decentro.tech
    tags:
      - Aadhaar
      - DigiLocker
      - Forensics
      - KYC
      - Onboarding
    properties:
      - type: Documentation
        url: https://docs.decentro.tech/
      - type: OpenAPI
        url: openapi/decentro-kyc-api-openapi.yml
  - aid: decentro:payments-api
    name: Decentro Payments API
    description: Collections, payouts, ENACH mandates, UPI Autopay, settlements, and refunds for the Indian banking system.
    humanURL: https://docs.decentro.tech/
    baseURL: https://in.decentro.tech
    tags:
      - Collections
      - Mandates
      - Payouts
      - Settlements
      - UPI
    properties:
      - type: Documentation
        url: https://docs.decentro.tech/
      - type: OpenAPI
        url: openapi/decentro-payments-api-openapi.yml
      - type: JSONSchema
        url: json-schema/decentro-payout.json
      - type: Rules
        url: rules/decentro-payments-api-rules.yml
      - type: Capabilities
        url: capabilities/decentro-payments-api-capabilities.yml
  - aid: decentro:virtual-accounts-api
    name: Decentro Virtual Accounts API
    description: Create and manage virtual bank accounts, balances, statements, and remitter whitelisting for collections and reconciliation.
    humanURL: https://docs.decentro.tech/
    baseURL: https://in.decentro.tech
    tags:
      - Banking
      - Reconciliation
      - Virtual Accounts
    properties:
      - type: Documentation
        url: https://docs.decentro.tech/
      - type: OpenAPI
        url: openapi/decentro-virtual-accounts-api-openapi.yml
      - type: JSONSchema
        url: json-schema/decentro-virtual-account.json
  - aid: decentro:ledger-api
    name: Decentro Ledger API
    description: Double-entry accounting primitives for journals, ledger accounts, and transactions tied to Decentro virtual accounts and external counterparties.
    humanURL: https://docs.decentro.tech/
    baseURL: https://in.decentro.tech
    tags:
      - Accounts
      - Accounting
      - Ledger
      - Transactions
    properties:
      - type: Documentation
        url: https://docs.decentro.tech/
      - type: OpenAPI
        url: openapi/decentro-ledger-api-openapi.yml
common:
  - type: Website
    url: https://decentro.tech/
  - type: Portal
    url: https://docs.decentro.tech/
  - type: Reference
    url: https://docs.decentro.tech/reference
  - type: Blog
    url: https://decentro.tech/blog/
  - type: Pricing
    url: https://decentro.tech/pricing/
  - type: JSON-LD
    url: json-ld/decentro-context.jsonld
  - type: Vocabulary
    url: vocabulary/decentro-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
