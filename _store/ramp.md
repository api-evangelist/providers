---
aid: ramp
name: Ramp
description: Ramp is a finance automation platform that combines corporate cards, expense management, accounts payable, vendor management, and accounting integrations into a single product. The Ramp Developer API enables developers to access and manage Ramp account data, build applications for the Ramp App Center reaching over 25,000 Ramp customers, and automate financial workflows by integrating Ramp into existing systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Spend Management
  - Corporate Cards
  - Expense Management
  - Accounts Payable
  - Bill Pay
  - Accounting
  - Reimbursements
created: '2025-02-17'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/ramp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: ramp:ramp-developer-api
    name: Ramp Developer API
    description: The Ramp Developer API enables developers to programmatically access and manage Ramp account data, build applications for the Ramp App Center, and automate financial workflows. It provides resources for transactions, cards, users, departments, locations, vendors, accounting integrations, reimbursements, bills, and statements, supporting both reporting and automation use cases.
    humanURL: https://docs.ramp.com/developer-api/v1/overview/introduction
    baseURL: https://api.ramp.com/developer/v1
    tags:
      - Finance
      - Spend Management
      - Corporate Cards
      - Expense Management
      - Accounts Payable
      - Accounting
    properties:
      - type: Documentation
        url: https://docs.ramp.com/developer-api/v1/overview/introduction
      - type: OpenAPI
        url: openapi/ramp-developer-api-openapi.yml
      - type: JSONSchema
        url: json-schema/ramp-transaction.json
      - type: JSONSchema
        url: json-schema/ramp-card.json
      - type: JSONSchema
        url: json-schema/ramp-user.json
      - type: JSONLD
        url: json-ld/ramp-context.jsonld
      - type: JSONStructure
        url: json-structure/ramp-transaction-structure.json
      - type: JSONStructure
        url: json-structure/ramp-card-structure.json
      - type: JSONStructure
        url: json-structure/ramp-user-structure.json
      - type: Example
        url: examples/ramp-list-transactions-example.json
      - type: Example
        url: examples/ramp-list-cards-example.json
      - type: Example
        url: examples/ramp-list-users-example.json
      - type: SpectralRules
        url: rules/ramp-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/spend-management.yaml
      - type: NaftikoCapabilities
        url: capabilities/accounting-integration.yaml
common:
  - type: Website
    url: https://ramp.com/
  - type: Documentation
    url: https://docs.ramp.com/
  - type: Developer Portal
    url: https://docs.ramp.com/developer-api/v1/overview/introduction
  - type: Authentication
    url: https://docs.ramp.com/developer-api/v1/guides/authorization
  - type: Sign Up
    url: https://app.ramp.com/sign-up
  - type: Pricing
    url: https://ramp.com/pricing
  - type: Blog
    url: https://ramp.com/blog
  - type: Support
    url: https://support.ramp.com/
  - type: Status
    url: https://status.ramp.com/
  - type: Terms of Service
    url: https://ramp.com/legal/platform-agreement
  - type: Privacy Policy
    url: https://ramp.com/legal/privacy-policy
  - type: Vocabulary
    url: vocabulary/ramp-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
