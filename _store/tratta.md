---
aid: tratta
name: Tratta
description: Tratta is a debt collection and payment experience platform that provides REST APIs and webhooks for integrating payment plans, billing, customer session management, and collections workflows into existing tech stacks. The platform supports OAuth 2.0 / bearer token authentication and offers sandbox and production environments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Billing
  - Collections
  - Payments
  - Debt Collection
  - Fintech
created: '2025-02-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tratta/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tratta:tratta
    name: Tratta API
    description: REST API for Tratta's debt collection and payment platform. Enables programmatic management of debt accounts, payment plans, transactions, charges, customers, and webhooks for collections workflows.
    humanURL: https://docs.tratta.io/
    baseURL: https://api.tratta.io
    tags:
      - Billing
      - Collections
      - Payments
      - Debt Collection
      - Fintech
    properties:
      - type: Documentation
        url: https://docs.tratta.io/api.html
      - type: OpenAPI
        url: openapi/tratta-openapi.yml
      - type: JSONSchema
        url: json-schema/tratta-payment-plan-schema.json
      - type: JSONSchema
        url: json-schema/tratta-debt-account-schema.json
      - type: JSONStructure
        url: json-structure/tratta-payment-plan-structure.json
      - type: JSONLD
        url: json-ld/tratta-context.jsonld
      - type: SpectralRules
        url: rules/tratta-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/debt-collection-workflow.yaml
      - type: Vocabulary
        url: vocabulary/tratta-vocabulary.yml
    x-resources:
      - Customers
      - Debt Accounts
      - Payment Plans
      - Payment Methods
      - Charges
      - Transactions
      - Webhooks
      - Customer Sessions
      - Bulk Operations
      - Tickets
    x-authentication:
      type: Bearer Token
      description: Bearer token in Authorization header; OAuth 2.0 / API Key security
    x-rate-limits:
      default: 300 requests per minute
    x-integrations:
      - StratusPay
      - Cogent
      - Artiva
      - Snowflake
common:
  - type: Website
    url: https://www.tratta.io/
  - type: Documentation
    url: https://docs.tratta.io/
  - type: Sign Up
    url: https://www.tratta.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
