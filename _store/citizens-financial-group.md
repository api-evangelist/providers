---
aid: citizens-financial-group
name: Citizens Financial Group
url: https://raw.githubusercontent.com/api-evangelist/citizens-financial-group/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Banking
  - Buy Now Pay Later
  - Financial Services
  - FDX
  - Locator
  - Open Banking
  - Payments
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations through Citizens Bank and its subsidiaries. Citizens exposes a public developer portal at developer.citizensbank.com with REST APIs for accounts, statements, branch and ATM lookup, and a sandbox powered by the Open Bank Project. In 2025 Citizens launched a new FDX-aligned Open Banking API providing business, commercial, wealth, and private-banking customers with a single endpoint for sharing account, balance, and transaction data with authorized third parties. A separate Citizens Pay developer portal exposes Buy-Now-Pay-Later integration APIs.
apis:
  - aid: citizens-financial-group:citizens-open-banking-api
    name: Citizens Open Banking API
    tags:
      - Accounts
      - Balances
      - FDX
      - Open Banking
      - Transactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citizensbank.com/
    properties:
      - url: https://developer.citizensbank.com/
        type: Documentation
      - url: https://investor.citizensbank.com/about-us/newsroom/latest-news/2025/2025-03-27.aspx
        type: Announcement
    description: Citizens Open Banking API is the FDX-aligned API surface launched in Q1 2025 that gives business, commercial, wealth, and private- banking customers a single endpoint to share account balances, transactions, and other financial data with authorized third-party platforms.
  - aid: citizens-financial-group:citizens-accounts-api
    name: Citizens Accounts API
    tags:
      - Accounts
      - Balances
      - Banking
      - Transactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citizensbank.com/api
    properties:
      - url: https://developer.citizensbank.com/api
        type: Documentation
    description: The Citizens Accounts API enables authorized retrieval of Citizens Bank customer account and transaction information for use in third-party financial applications and aggregation platforms.
  - aid: citizens-financial-group:citizens-statements-api
    name: Citizens Statements API
    tags:
      - Banking
      - Documents
      - Statements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citizensbank.com/api
    properties:
      - url: https://developer.citizensbank.com/api
        type: Documentation
    description: The Citizens Statements API enables authorized retrieval of Citizens Bank customer monthly statements for personal financial management and document workflows.
  - aid: citizens-financial-group:citizens-atm-locator-api
    name: Citizens ATM Locator API
    tags:
      - ATM
      - Geo Search
      - Locator
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citizensbank.com/
    properties:
      - url: https://developer.citizensbank.com/
        type: Documentation
    description: The Citizens ATM Locator API enables searching for Citizens Bank ATMs throughout the USA using zip code, street address, or geographical coordinates.
  - aid: citizens-financial-group:citizens-branch-locator-api
    name: Citizens Branch Locator API
    tags:
      - Branch
      - Geo Search
      - Locator
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.citizensbank.com/
    properties:
      - url: https://developer.citizensbank.com/
        type: Documentation
    description: The Citizens Branch Locator API enables searching for Citizens Bank branches throughout the USA using zip code, street address, or geographical coordinates.
  - aid: citizens-financial-group:citizens-pay-api
    name: Citizens Pay API
    tags:
      - BNPL
      - Buy Now Pay Later
      - Citizens Pay
      - Embedded Finance
      - Lending
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer-citizenspay.citizensbank.com/
    properties:
      - url: https://developer-citizenspay.citizensbank.com/
        type: Documentation
    description: Citizens Pay is the buy-now-pay-later embedded financing platform offered by Citizens Bank. The Citizens Pay developer portal exposes APIs for merchant integration, underwriting, and installment-loan lifecycle management.
common:
  - type: Website
    url: https://www.citizensbank.com
  - type: Portal
    url: https://developer.citizensbank.com/
  - type: Sandbox
    url: https://sandboxdeveloper.citizensbank.com/
  - type: Open Bank Project Sandbox
    url: https://citizensbank.openbankproject.com/
  - type: Citizens Pay Portal
    url: https://developer-citizenspay.citizensbank.com/
  - type: Investor Relations
    url: https://investor.citizensbank.com/
  - type: Open Banking Announcement
    url: https://investor.citizensbank.com/about-us/newsroom/latest-news/2025/2025-03-27.aspx
  - type: Privacy Policy
    url: https://www.citizensbank.com/account-safeguards/privacy.aspx
  - type: Terms of Service
    url: https://www.citizensbank.com/customer-service/online-banking-service-agreement.aspx
  - type: Support
    url: https://www.citizensbank.com/customer-service/overview.aspx
  - type: JSON-LD
    url: json-ld/citizens-financial-group-context.jsonld
  - type: Spectral
    url: rules/citizens-financial-group-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/citizens-financial-group-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
