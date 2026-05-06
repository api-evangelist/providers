---
aid: basiq
name: Basiq
description: Basiq is an Australian open banking and financial data API platform providing unified access to bank account data and enrichment services. It enables fintechs, lenders, and financial service providers to connect to 180+ Australian and New Zealand banks via CDR (Consumer Data Right) and third-party connectors. The Basiq API provides user management, bank connections, account balances, transaction history, income verification, and expense categorization. Uses JWT Bearer token authentication.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Australia
  - Banking
  - CDR
  - Financial Data
  - Fintech
  - Open Banking
  - Transactions
url: https://raw.githubusercontent.com/api-evangelist/basiq/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: basiq:basiq-api
    name: Basiq API
    description: The Basiq API provides open banking access to Australian and New Zealand bank data. Manage users, bank connections, accounts, transactions, and affordability data (income verification, expense categorization) via JWT Bearer token authentication.
    humanURL: https://api.basiq.io/reference
    tags:
      - Accounts
      - Australia
      - CDR
      - Financial Data
      - Open Banking
      - Transactions
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://au-api.basiq.io
    properties:
      - type: Documentation
        url: https://api.basiq.io/reference
      - type: Documentation
        url: https://api.basiq.io/reference/getting-started
        name: Getting Started
      - type: OpenAPI
        url: openapi/basiq-api-openapi.yml
common:
  - type: Website
    url: https://basiq.io/
    name: Basiq
  - type: Documentation
    url: https://api.basiq.io/reference
    name: API Reference
  - type: Website
    url: https://dashboard.basiq.io/
    name: Developer Dashboard
  - type: Website
    url: https://basiq.io/pricing/
    name: Pricing
  - type: Blog
    url: https://basiq.io/blog/
    name: Blog
  - type: Website
    url: https://github.com/basiqio
    name: GitHub Organization
  - type: TermsOfService
    url: https://basiq.io/legal/terms-of-use/
    name: Terms of Use
  - type: PrivacyPolicy
    url: https://basiq.io/legal/privacy-policy/
    name: Privacy Policy
  - type: SpectralRules
    url: rules/basiq-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/basiq-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/open-banking.yaml
  - type: JSON-LD
    url: json-ld/basiq-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Bank Connections
        description: Connect to 180+ Australian and New Zealand banks via CDR and third-party connectors.
      - name: Account Data
        description: Retrieve real-time account balances, available funds, and account metadata.
      - name: Transaction History
        description: Access enriched transaction history with categorization and merchant data.
      - name: Income Verification
        description: Automated income stream identification and regular/irregular income calculation.
      - name: Expense Categorization
        description: Transaction-based expense categorization for affordability and budgeting analysis.
      - name: CDR Compliance
        description: Consumer Data Right (CDR) compliant data access for Australian open banking.
      - name: Data Enrichment
        description: Transaction enrichment with merchant names, categories, and subcategories.
  - name: Use Cases
    type: UseCases
    data:
      - name: Lending and Credit Assessment
        description: Use income verification and expense data to assess creditworthiness and affordability.
      - name: Personal Finance Apps
        description: Aggregate bank accounts and transactions for budgeting and financial planning tools.
      - name: Mortgage Applications
        description: Automate bank statement verification and income confirmation for home loan applications.
      - name: BNPL Affordability
        description: Assess buy-now-pay-later affordability using real-time transaction and income data.
      - name: Financial Advisory
        description: Provide financial planners with complete client financial pictures across institutions.
      - name: Account Verification
        description: Verify bank account ownership for payment and identity verification workflows.
  - name: Integrations
    type: Integrations
    data:
      - name: Xero
      - name: MYOB
      - name: Salesforce
      - name: Zapier
      - name: Commonwealth Bank
      - name: ANZ
      - name: Westpac
      - name: NAB
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
