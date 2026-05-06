---
aid: bank-of-america
url: https://raw.githubusercontent.com/api-evangelist/bank-of-america/refs/heads/main/apis.yml
name: Bank of America
tags:
  - Banking
  - Corporate Banking
  - Finance
  - Payments
  - Treasury
  - CashPro
modified: '2026-04-21'
description: Bank of America is a multinational investment bank and financial services holding company providing consumer banking, wealth management, corporate banking, and investment banking services worldwide. The CashPro Developer Studio provides REST APIs for corporate treasury clients to automate account management, payments, balance reporting, and statement access, supporting over 350 payment types and integration with TMS and ERP platforms.
apis:
  - aid: bank-of-america:cashpro-api
    name: Bank of America CashPro API
    tags:
      - Accounts
      - Balances
      - Banking
      - Corporate Banking
      - Payments
      - Statements
      - Treasury
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.bankofamerica.com/cashpro/v1
    humanURL: https://developer.bankofamerica.com/
    properties:
      - url: https://developer.bankofamerica.com/
        type: Documentation
      - url: openapi/bank-of-america-cashpro-api-openapi.yml
        type: OpenAPI
    description: The Bank of America CashPro API enables corporate treasury clients to programmatically access banking services including payments, account information, balance reporting, and transaction history. The API supports over 350 payment types and integrates with Treasury Management Systems (TMS) and ERP platforms.
common:
  - type: Website
    url: https://www.bankofamerica.com/
    name: Bank of America
  - type: Documentation
    url: https://developer.bankofamerica.com/
    name: CashPro Developer Studio
  - type: SignUp
    url: https://developer.bankofamerica.com/
    name: Developer Portal
  - type: Blog
    url: https://newsroom.bankofamerica.com/
    name: Newsroom
  - type: TermsOfService
    url: https://www.bankofamerica.com/online-banking/digital-banking-agreement.go
    name: Digital Banking Agreement
  - type: PrivacyPolicy
    url: https://www.bankofamerica.com/security-center/overview.go
    name: Privacy Policy
  - type: SpectralRules
    url: rules/bank-of-america-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bank-of-america-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/treasury-banking.yaml
  - type: JSON-LD
    url: json-ld/bank-of-america-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Account Management
        description: Programmatic access to CashPro account details and metadata.
      - name: Balance Reporting
        description: Real-time ledger, available, and collected balance queries.
      - name: Transaction History
        description: Paginated transaction history with date range filtering.
      - name: Payment Initiation
        description: Initiate payments across 350+ payment types including ACH, wire, SWIFT, and RTP.
      - name: Payment Status Tracking
        description: Real-time payment status monitoring and cancellation support.
      - name: Statement Access
        description: Programmatic retrieval of monthly account statements.
      - name: OAuth2 Security
        description: Client credentials OAuth2 flow for secure API access.
      - name: TMS/ERP Integration
        description: Pre-built connectors for 28+ Treasury Management and ERP platforms.
      - name: Sandbox Environment
        description: Developer sandbox for testing and accelerated onboarding.
  - name: Use Cases
    type: UseCases
    data:
      - name: Treasury Automation
        description: Automate daily cash positioning, balance reporting, and payment workflows.
      - name: ERP Integration
        description: Connect SAP, Oracle, or other ERP systems to Bank of America CashPro.
      - name: Payments Hub
        description: Centralize payment initiation across ACH, wire, SWIFT, and real-time payment rails.
      - name: Liquidity Management
        description: Real-time visibility into global account balances for liquidity decisions.
      - name: Reconciliation
        description: Automated transaction download for account reconciliation workflows.
      - name: Cash Concentration
        description: Sweep and concentration account management via API.
  - name: Integrations
    type: Integrations
    data:
      - name: SAP
      - name: Oracle
      - name: Kyriba
      - name: Sage Intacct
      - name: Microsoft Dynamics
      - name: Coupa
      - name: Workday
created: '2024-01-01'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
