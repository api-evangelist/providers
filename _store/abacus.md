---
aid: abacus
url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/apis.yml
name: Abacus
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting
  - Expense Management
  - Finance
  - Reimbursement
description: Abacus (now part of Emburse Spend) is an expense management platform that allows businesses to streamline expense reporting, receipts, and reimbursements. The Abacus API is available to partners and enterprise customers, providing programmatic access to member management and expense operations using OAuth 2.0 authentication.
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: abacus:abacus-api
    name: Abacus API
    tags:
      - Expenses
      - Finance
      - Members
      - Reimbursement
    humanURL: https://support.abacus.com/hc/en-us/articles/12493681200269-Abacus-API
    baseURL: https://api.abacus.com
    properties:
      - url: https://support.abacus.com/hc/en-us/articles/12493681200269-Abacus-API
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/openapi/abacus-api-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-member-schema.json
        type: JSONSchema
        title: Member
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-expense-schema.json
        type: JSONSchema
        title: Expense
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-invite-member-request-schema.json
        type: JSONSchema
        title: Invite Member Request
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-update-member-request-schema.json
        type: JSONSchema
        title: Update Member Request
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-member-list-response-schema.json
        type: JSONSchema
        title: Member List Response
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-expense-list-response-schema.json
        type: JSONSchema
        title: Expense List Response
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-oauth-token-request-schema.json
        type: JSONSchema
        title: OAuth Token Request
      - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-schema/abacus-oauth-token-response-schema.json
        type: JSONSchema
        title: OAuth Token Response
    description: The Abacus API provides programmatic access to expense management functionality, including inviting and suspending members, listing and retrieving expense reports, and integrating with third-party platforms. Available to partners and enterprise customers using OAuth 2.0 client credentials.
common:
  - type: Website
    url: https://www.abacus.com/
  - type: Documentation
    url: https://support.abacus.com/hc/en-us/articles/12493681200269-Abacus-API
  - type: Support
    url: https://support.abacus.com/
  - type: PrivacyPolicy
    url: https://legal.emburse.com/
  - type: TrustCenter
    url: https://trust.emburse.com/
  - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
    name: Abacus Spectral Rules
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/vocabulary/abacus-vocabulary.yaml
    name: Abacus Vocabulary
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/capabilities/expense-management.yaml
    name: Expense Management Capability
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-ld/abacus-api-context.jsonld
    name: Abacus API JSON-LD Context
    type: JSONLD
  - type: Features
    data:
      - name: Member Management
        description: Invite, update, and suspend organization members programmatically
      - name: Expense Tracking
        description: Retrieve and filter expense reports by status, member, and date range
      - name: OAuth 2.0 Authentication
        description: Secure API access using client credentials grant flow
      - name: Receipt Management
        description: Link receipts to expense reports via URL references
      - name: Multi-category Expenses
        description: Categorize expenses across meals, travel, lodging, office supplies, and software
      - name: Paginated Results
        description: Paginated API responses with configurable page sizes
  - type: UseCases
    data:
      - name: Employee Onboarding
        description: Automatically invite new employees to the expense platform via API
      - name: Employee Offboarding
        description: Programmatically suspend departed employees from expense access
      - name: Expense Reconciliation
        description: Retrieve and reconcile expense reports for accounting integration
      - name: Spend Analytics
        description: Pull expense data by category, member, or date range for reporting
      - name: Third-party Integration
        description: Connect Abacus expense data with ERP and accounting systems
  - type: Integrations
    data:
      - name: QuickBooks
        description: Sync expense data with QuickBooks for accounting reconciliation
      - name: Xero
        description: Integrate with Xero for automated expense accounting
      - name: NetSuite
        description: Connect expense reports with NetSuite ERP
      - name: Sage Intacct
        description: Sync expenses with Sage Intacct for financial management
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
