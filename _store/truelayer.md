---
aid: truelayer
name: TrueLayer
description: TrueLayer is Europe's leading open banking platform providing unified access to bank data, payments, payouts, refunds, and variable recurring payments across the UK and EU. TrueLayer connects to 69+ financial institutions and enables instant bank payments, data enrichment, and account verification through a single API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data API
  - Financial Services
  - Open Banking
  - Payments
  - PSD2
  - UK Banking
  - VRP
url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: truelayer:payments-api
    name: TrueLayer Payments API
    description: The TrueLayer Payments API v3 enables creation and management of open banking payments, payouts, refunds, and variable recurring payment mandates. Supports closed-loop pay-ins, single external payments, VRP mandates, merchant account management, and full webhook event coverage across UK and EU markets.
    humanURL: https://docs.truelayer.com/docs/payments-api-basics
    baseURL: https://api.truelayer.com
    tags:
      - Open Banking
      - Payments
      - Payouts
      - Refunds
      - VRP
    properties:
      - type: Documentation
        url: https://docs.truelayer.com/docs/payments-api-basics
      - type: Getting Started
        url: https://docs.truelayer.com/docs/create-a-payment
      - type: Webhooks
        url: https://docs.truelayer.com/docs/payments-api-webhook-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/openapi/truelayer-payments-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/rules/truelayer-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/capabilities/open-banking-payments.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/json-schema/truelayer-payment-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/json-ld/truelayer-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/vocabulary/truelayer-vocabulary.yml
  - aid: truelayer:data-api
    name: TrueLayer Data API
    description: The TrueLayer Data API provides access to bank account data including account information, balances, transactions, identity verification, and standing orders. Used for account verification, affordability assessments, and financial data enrichment.
    humanURL: https://docs.truelayer.com/docs/data-api-basics
    baseURL: https://api.truelayer.com
    tags:
      - Account Data
      - Bank Data
      - Data API
      - Identity Verification
      - Open Banking
    properties:
      - type: Documentation
        url: https://docs.truelayer.com/docs/data-api-basics
      - type: Reference
        url: https://docs.truelayer.com/reference
common:
  - type: Website
    url: https://truelayer.com/
  - type: Documentation
    url: https://docs.truelayer.com/
  - type: API Reference
    url: https://docs.truelayer.com/reference
  - type: GitHub Organization
    url: https://github.com/TrueLayer
  - type: Console
    url: https://console.truelayer.com/
  - type: Sandbox
    url: https://console.truelayer-sandbox.com/
  - type: SDKs
    url: https://docs.truelayer.com/docs/client-libraries
  - type: Changelog
    url: https://docs.truelayer.com/changelog
  - type: Blog
    url: https://truelayer.com/blog/
  - type: LinkedIn
    url: https://www.linkedin.com/company/truelayer/
  - type: Twitter
    url: https://twitter.com/TrueLayer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
