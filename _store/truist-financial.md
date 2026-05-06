---
aid: truist-financial
url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/apis.yml
name: Truist Financial
description: Truist Financial Corporation is a purpose-driven financial services company headquartered in Charlotte, North Carolina, formed by the merger of BB&T and SunTrust Banks in 2019. As one of the ten largest commercial banks in the United States, Truist offers a comprehensive suite of developer APIs through its Developer Center, enabling financial institutions, fintech companies, and enterprise clients to integrate banking capabilities into their applications. The platform covers personal and small business banking, commercial accounts, transactions, open banking, and association services, with OAuth 2.0 and API key authentication. Truist launched FDX-compliant open banking in 2026, partnering with Mastercard and Plaid to enable secure, tokenized financial data sharing for consumers and businesses.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Financial Services
  - Open Banking
  - Commercial Banking
  - Personal Banking
  - Payments
  - Accounts
  - Transactions
  - Fortune 500
access: 3rd-Party
created: '2026-03-21'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: truist-financial:truist-personal-small-business-accounts-api
    name: Truist Personal and Small Business Accounts API
    tags:
      - Accounts
      - Personal Banking
      - Small Business
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/personal-and-small-business-accounts/overview
    properties:
      - url: https://developer.truist.com/api/personal-and-small-business-accounts/overview
        type: Documentation
      - url: https://developer.truist.com/api/personal-and-small-business-accounts/documentation
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/openapi/truist-personal-small-business-accounts-openapi.yml
        type: OpenAPI
    description: The Truist Personal and Small Business Accounts API provides programmatic access to consumer and small business deposit account information, including account details, balances, account types, and ownership information. Developers can retrieve account lists for authenticated clients, access individual account details, and retrieve balance information for checking, savings, and money market accounts. The API supports OAuth 2.0 authentication and is designed for fintech integrations, account aggregation platforms, and personal finance management applications.
  - aid: truist-financial:truist-personal-small-business-transactions-api
    name: Truist Personal and Small Business Transactions API
    tags:
      - Transactions
      - Personal Banking
      - Small Business
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/personal-and-small-business-transactions/overview
    properties:
      - url: https://developer.truist.com/api/personal-and-small-business-transactions/overview
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/openapi/truist-personal-small-business-transactions-openapi.yml
        type: OpenAPI
    description: The Truist Personal and Small Business Transactions API enables retrieval of transaction history for personal and small business accounts. Developers can access posted and pending transactions, filter by date range, and retrieve transaction details including merchant information, amounts, and transaction categories. The API supports OAuth 2.0 authentication and is suitable for personal finance management tools, accounting integrations, and expense tracking applications.
  - aid: truist-financial:truist-personal-small-business-client-contact-api
    name: Truist Personal and Small Business Client Contact API
    tags:
      - Client Management
      - Personal Banking
      - Small Business
      - Contact Information
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/personal-and-small-business-client-contact/overview
    properties:
      - url: https://developer.truist.com/api/personal-and-small-business-client-contact/overview
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
    description: The Truist Personal and Small Business Client Contact API provides access to client contact information associated with personal and small business accounts, including address, phone number, and email address data. This API enables authorized applications to retrieve and manage contact details for authenticated Truist clients, supporting CRM integrations and account management workflows.
  - aid: truist-financial:truist-commercial-accounts-api
    name: Truist Commercial Accounts API
    tags:
      - Accounts
      - Commercial Banking
      - Treasury
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/commercial-accounts/overview
    properties:
      - url: https://developer.truist.com/api/commercial-accounts/overview
        type: Documentation
      - url: https://developer.truist.com/api/commercial-accounts/documentation
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/openapi/truist-commercial-accounts-openapi.yml
        type: OpenAPI
    description: The Truist Commercial Accounts API provides programmatic access to commercial deposit account information, including account balances, account details, and account summary data for commercial and corporate clients. The API supports treasury management integrations, ERP system connectivity, and cash management platforms. It enables real-time balance reporting, account hierarchy retrieval, and integration with commercial banking operations. OAuth 2.0 and API key authentication are supported.
  - aid: truist-financial:truist-commercial-account-transactions-api
    name: Truist Commercial Account Transactions API
    tags:
      - Transactions
      - Commercial Banking
      - Treasury
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/commercial-account-transactions/overview
    properties:
      - url: https://developer.truist.com/api/commercial-account-transactions/overview
        type: Documentation
      - url: https://developer.truist.com/api/commercial-account-transactions/documentation
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/openapi/truist-commercial-account-transactions-openapi.yml
        type: OpenAPI
    description: The Truist Commercial Account Transactions API enables programmatic retrieval of commercial account transaction data including ACH credits and debits, wire transfers, checks, and other payment types. The API supports filtering by date range and transaction type, enabling ERP integrations, cash flow reconciliation, and automated accounting workflows. It is designed for treasury teams, corporate finance applications, and commercial banking integrations.
  - aid: truist-financial:truist-commercial-account-transaction-image-api
    name: Truist Commercial Account Transaction Image API
    tags:
      - Transactions
      - Check Images
      - Commercial Banking
      - Documents
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/api/commercial-account-transaction-image/overview
    properties:
      - url: https://developer.truist.com/api/commercial-account-transaction-image/overview
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
    description: The Truist Commercial Account Transaction Image API provides access to check images and transaction document images associated with commercial account transactions. Developers can retrieve front and back images of checks, deposit slips, and other payment documents by transaction reference. The API supports document archiving, audit workflows, and automated reconciliation integrations for commercial banking clients.
  - aid: truist-financial:truist-open-banking-api
    name: Truist Open Banking API
    tags:
      - Open Banking
      - FDX
      - Financial Data Exchange
      - Accounts
      - Banking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://truist-1132.my.site.com/truist/s/
    properties:
      - url: https://truist-1132.my.site.com/truist/s/
        type: Portal
      - url: https://truist-1132.my.site.com/truist/s/subscriptions
        type: Documentation
      - url: https://www.prnewswire.com/news-releases/truist-launches-secure-open-banking-experience-302685248.html
        type: Announcement
    description: The Truist Open Banking API provides secure, FDX-compliant (Financial Data Exchange) access to consumer and small business financial data, enabling authorized fintech applications to retrieve account balances, transaction history, and payment information with client consent. Launched in February 2026 in partnership with Mastercard's open finance platform, the API replaces credential sharing with tokenized, permission-based access. Truist expanded the program through a Plaid data-access agreement in March 2026, enabling clients to manage and revoke third-party data access through a centralized consent portal. The API supports account information, transaction data, investment data, and loan data per FDX standards.
  - aid: truist-financial:truist-association-services-api
    name: Truist Association Services API
    tags:
      - Association Services
      - Community Banking
      - Banking
      - Payments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.truist.com/v1
    humanURL: https://developer.truist.com/categories/association-services
    properties:
      - url: https://developer.truist.com/categories/association-services
        type: Documentation
      - url: https://developer.truist.com/api/working-with-truist
        type: Authentication
    description: The Truist Association Services API provides banking and payment capabilities tailored for associations, non-profit organizations, and community groups. The API supports dues collection, payment processing, member account management, and reporting for trade associations, homeowners associations, and membership organizations that bank with Truist. It enables integration of banking workflows into association management platforms and member portals.
common:
  - url: https://www.truist.com
    name: Truist Website
    type: Website
  - url: https://developer.truist.com/
    name: Developer Center
    type: Portal
  - url: https://developer.truist.com/api/working-with-truist
    name: Getting Started
    type: GettingStarted
  - url: https://developer.truist.com/api/working-with-truist
    name: Authentication
    type: Authentication
  - url: https://truist-1132.my.site.com/truist/s/
    name: Open Banking Portal
    type: Portal
  - url: https://raw.githubusercontent.com/api-evangelist/truist-financial/refs/heads/main/rules/truist-financial-rules.yml
    name: Spectral Rules
    type: SpectralRules
  - url: https://investor.truist.com/
    name: Investor Relations
    type: InvestorRelations
  - url: https://www.truist.com/about-truist
    name: About Truist
    type: About
  - url: https://ir.truist.com/news-releases
    name: Press Releases
    type: Blog
  - url: https://www.linkedin.com/company/truistfinancial
    name: Truist on LinkedIn
    type: LinkedIn
  - url: https://twitter.com/Truist
    name: Truist on X (Twitter)
    type: X
  - url: https://github.com/truistbank
    name: Truist on GitHub
    type: GitHub
  - url: https://www.truist.com/privacy-security
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.truist.com/about-truist/terms-conditions
    name: Terms of Service
    type: TermsOfService
  - type: Features
    data:
      - 'Truist Financial: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Truist banking APIs are commercial banking integrations available to enterprise treasury management customers.
    sources:
      - https://www.truist.com/business/treasury-management
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
