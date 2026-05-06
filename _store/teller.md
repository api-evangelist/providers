---
aid: teller
name: Teller
description: Teller is a unified banking API providing real-time access to bank accounts, transactions, balances, identity data, and payment initiation across US financial institutions. Connect to thousands of banks and credit unions through a single integration. Teller uses mutual TLS (mTLS) for application authentication and access tokens obtained via Teller Connect for per-account authorization.
url: https://raw.githubusercontent.com/api-evangelist/teller/refs/heads/main/apis.yml
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Banking
  - Financial Data
  - FinTech
  - Open Banking
  - Transactions
  - Unified API
apis:
  - aid: teller:teller-api
    name: Teller API
    description: Unified banking API for real-time access to accounts, transactions, balances, and identity data across US financial institutions. Supports account management, transaction history, balance retrieval, and account holder identity verification via a single REST API secured with mTLS and per-user access tokens.
    humanURL: https://teller.io/docs/api
    baseURL: https://api.teller.io
    tags:
      - Accounts
      - Balance
      - Banking
      - Financial Data
      - Identity
      - Open Banking
      - Transactions
    properties:
      - type: Documentation
        url: https://teller.io/docs/api
      - type: OpenAPI
        url: openapi/teller-openapi.yml
      - type: Getting Started
        url: https://teller.io/docs/guides/quickstart
      - type: Authentication
        url: https://teller.io/docs/api/authentication
      - type: SDK
        url: https://teller.io/docs/guides/sdks
common:
  - type: Website
    url: https://teller.io/
  - type: Documentation
    url: https://teller.io/docs
  - type: Developer Portal
    url: https://teller.io/docs/api
  - type: GitHub Organization
    url: https://github.com/tellerhq
  - type: SDK
    url: https://github.com/tellerhq/teller-ruby
  - type: SDK
    url: https://github.com/tellerhq/teller-connect-react
  - type: SDK
    url: https://github.com/tellerhq/iOS-SDK
  - type: SDK
    url: https://github.com/tellerhq/teller-connect-android
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
