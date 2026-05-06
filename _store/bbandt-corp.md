---
aid: bbandt-corp
url: https://raw.githubusercontent.com/api-evangelist/bbandt-corp/refs/heads/main/apis.yml
name: BB&T Corp (Truist)
description: BB&T Corporation was a major financial services holding company that merged with SunTrust Banks in December 2019 to form Truist Financial Corporation. The combined entity operates as Truist Bank and maintains a developer portal at developer.truist.com offering REST APIs for account information, transaction data, and banking services for personal, small business, and commercial customers. The APIs support open banking integrations and financial technology applications.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Financial Services
  - Open Banking
  - Truist
  - BB&T
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-21'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: bbandt-corp:personal-small-business-accounts
    name: Truist Personal and Small Business Accounts API
    description: Provides access to personal and small business account data including account balances, account details, and account lists for authenticated customers. Supports open banking use cases for fintech applications.
    humanURL: https://developer.truist.com/api/personal-and-small-business-accounts/overview
    tags:
      - Banking
      - Accounts
      - Personal Banking
      - Small Business
    properties:
      - type: Documentation
        url: https://developer.truist.com/api/personal-and-small-business-accounts/overview
  - aid: bbandt-corp:personal-small-business-transactions
    name: Truist Personal and Small Business Transactions API
    description: Provides access to transaction history and transaction details for personal and small business bank accounts. Enables fintech applications to retrieve customer transaction data with proper authorization.
    humanURL: https://developer.truist.com/api/personal-and-small-business-transactions/overview
    tags:
      - Banking
      - Transactions
      - Personal Banking
      - Small Business
    properties:
      - type: Documentation
        url: https://developer.truist.com/api/personal-and-small-business-transactions/overview
  - aid: bbandt-corp:commercial-accounts
    name: Truist Commercial Accounts API
    description: Provides access to commercial banking account data including account balances, account details, and account management for business customers. Supports treasury management and commercial banking integrations.
    humanURL: https://developer.truist.com/api/commercial-accounts/overview
    tags:
      - Banking
      - Accounts
      - Commercial Banking
    properties:
      - type: Documentation
        url: https://developer.truist.com/api/commercial-accounts/overview
  - aid: bbandt-corp:commercial-account-transactions
    name: Truist Commercial Account Transactions API
    description: Provides access to transaction history and transaction details for commercial bank accounts. Supports enterprise financial applications, ERP integrations, and treasury management workflows.
    humanURL: https://developer.truist.com/api/commercial-account-transactions/overview
    tags:
      - Banking
      - Transactions
      - Commercial Banking
    properties:
      - type: Documentation
        url: https://developer.truist.com/api/commercial-account-transactions/overview
  - aid: bbandt-corp:association-services
    name: Truist Association Services API
    description: Provides banking and payment services APIs for associations, HOAs, and membership organizations. Supports dues collection, payment processing, and financial management for association management companies.
    humanURL: https://developer.truist.com/categories/association-services
    tags:
      - Banking
      - Association Services
      - Payments
    properties:
      - type: Documentation
        url: https://developer.truist.com/categories/association-services
common:
  - type: Portal
    url: https://developer.truist.com/
  - type: Website
    url: https://www.truist.com/
  - type: Documentation
    url: https://developer.truist.com/api/view-api
  - type: GettingStarted
    url: https://developer.truist.com/api/working-with-truist
  - type: TermsOfService
    url: https://www.truist.com/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.truist.com/privacy-security
  - type: SpectralRules
    url: rules/bbandt-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bbandt-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/open-banking.yaml
  - type: JSON-LD
    url: json-ld/bbandt-context.jsonld
  - type: Features
    data:
      - name: Open Banking APIs
        description: REST APIs enabling fintech applications to access account and transaction data with customer consent.
      - name: Personal Banking APIs
        description: APIs for personal and small business banking account access including balances and transaction history.
      - name: Commercial Banking APIs
        description: APIs for commercial account management, treasury operations, and enterprise banking integrations.
      - name: Association Services
        description: Specialized APIs for association management companies to handle dues, payments, and financial reporting.
      - name: OAuth 2.0 Authentication
        description: Secure OAuth 2.0 based authentication for customer data access with proper consent flows.
  - type: UseCases
    data:
      - name: Personal Finance Apps
        description: Build personal finance management apps that aggregate account and transaction data for Truist customers.
      - name: Accounting Software Integration
        description: Integrate Truist commercial accounts with accounting software like QuickBooks or Xero.
      - name: Treasury Management
        description: Enable enterprise treasury teams to access real-time commercial account balances and transaction data.
      - name: Association Management
        description: Automate dues collection and financial reporting for homeowners associations and membership organizations.
  - type: Integrations
    data:
      - name: Plaid
        description: Third-party data aggregator providing alternative connectivity to Truist account data.
      - name: Tink
        description: Open banking platform providing access to Truist banking data via aggregation.
      - name: QuickBooks
        description: Accounting software integration for Truist commercial banking customers.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
