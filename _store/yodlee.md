---
aid: yodlee
name: Yodlee
description: Yodlee (Envestnet | Yodlee) is a financial data aggregation platform providing unified API access to bank accounts, credit card transactions, investments, loans, and insurance data across thousands of financial institutions. The Yodlee Core APIs v1.1 enable secure account aggregation, transaction enrichment, risk analytics, consent management, and account verification for fintech applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Data
  - Data Aggregation
  - Banking
  - Fintech
  - Open Finance
created: '2026-03-27'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: yodlee:yodlee-core-api
    name: Yodlee Core API
    description: The Yodlee Core APIs v1.1 provide a flexible RESTful API for accessing personal financial data. Key capabilities include account aggregation across banks and brokerages, transaction history and enrichment, holdings and investment data, consent and provider account management, documents, statements, data extracts, risk analytics, and account verification. Supports 90% of top US, UK, Australia, and India financial institutions.
    humanURL: https://developer.yodlee.com/resources/yodlee/yodlee-api-overview/docs/overview
    baseURL: https://production.api.yodlee.com/ysl
    tags:
      - Financial Data
      - Aggregation
      - Transactions
      - Accounts
      - Banking
      - Investments
    properties:
      - type: Documentation
        url: https://developer.yodlee.com/resources/yodlee/yodlee-api-overview/docs/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/openapi/yodlee-core-openapi.yml
      - type: Getting Started
        url: https://developer.yodlee.com/docs/getting-started
  - aid: yodlee:yodlee-account-verification-api
    name: Yodlee Account Verification API
    description: The Yodlee Account Verification API enables real-time verification of bank account ownership and balance. Supports verification workflows via FastLink 4, holder profile retrieval, verified account status, and account classification summaries.
    humanURL: https://developer.yodlee.com/products/yodlee/account-aggregation/docs/api-reference
    baseURL: https://production.api.yodlee.com/ysl
    tags:
      - Account Verification
      - Banking
      - Fintech
      - KYC
    properties:
      - type: Documentation
        url: https://developer.yodlee.com/products/yodlee/account-aggregation/docs/api-reference
  - aid: yodlee:yodlee-fastlink
    name: Yodlee FastLink
    description: FastLink 4 is Yodlee's white-label account aggregation widget that enables users to securely link their financial accounts. Provides a customizable embedded UI for account login, MFA, account selection, verification, and consent management.
    humanURL: https://developer.yodlee.com/
    tags:
      - Account Linking
      - Widget
      - Embedded Finance
    properties:
      - type: Documentation
        url: https://developer.yodlee.com/
common:
  - type: Website
    url: https://www.yodlee.com/
  - type: Developer Portal
    url: https://developer.yodlee.com/
  - type: Documentation
    url: https://developer.yodlee.com/resources/yodlee/yodlee-api-overview/docs
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/openapi/yodlee-core-openapi.yml
  - type: GitHub Organization
    url: https://github.com/yodlee
  - type: SDK
    url: https://github.com/Yodlee/java-sdk
  - type: Getting Started
    url: https://developer.yodlee.com/docs/getting-started
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/vocabulary/yodlee-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
