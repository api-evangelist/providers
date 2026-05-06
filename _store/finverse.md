---
aid: finverse
name: Finverse
description: Finverse is a unified open finance API platform providing aggregated access to banking data, payments, and financial services across Asia-Pacific. Often described as the Plaid for Asia, it connects to over 40 banks across Hong Kong, Singapore, Philippines, Vietnam, and other Southeast Asian markets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Aggregation
  - Asia Pacific
  - Financial Data
  - Open Banking
  - Open Finance
  - Payments
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/finverse/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: finverse:bank-data-api
    name: Finverse Bank Data API
    description: Retrieve real-time financial account information with user consent from over 40 Asian banks. Returns key financial data including real-time account balances, transaction and balance history for up to 24 months, bank statements, account holder identity, and estimated income.
    humanURL: https://www.finverse.com/bank-data-api
    tags:
      - Bank Accounts
      - Financial Data
      - KYC
      - Open Banking
      - Transactions
    properties:
      - type: Documentation
        url: https://docs.finverse.com
      - type: Website
        url: https://www.finverse.com/bank-data-api
  - aid: finverse:payments-api
    name: Finverse Collect API
    description: Automate bank payment collection in Hong Kong and Singapore. Enable customers to pay directly from their bank accounts, cutting transaction fees by up to 85%. Supports payment links, mandates, and direct bank transfers.
    humanURL: https://www.finverse.com/payments-api
    tags:
      - Bank Transfers
      - Open Banking
      - Payment Collection
      - Payments
    properties:
      - type: Documentation
        url: https://docs.finverse.com
      - type: Website
        url: https://www.finverse.com/payments-api
common:
  - type: Website
    url: https://www.finverse.com
  - type: Documentation
    url: https://docs.finverse.com
  - type: Developer Portal
    url: https://dashboard.finverse.com
  - type: Support Email
    url: mailto:support@finverse.com
  - type: Payment Links
    url: https://www.finverse.com/payment-links
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
