---
name: Temenos Transact
description: Core banking APIs from Temenos Transact, providing comprehensive banking functionality including accounts, transactions, payments, loans, and customer management.
image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
url: https://www.temenos.com/products/transact/
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
apis:
  - name: Temenos Transact Core Banking API
    description: RESTful APIs for core banking operations including account management, customer data, transactions, and payment processing.
    image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
    humanURL: https://www.temenos.com/products/transact/
    baseURL: https://api.temenos.com/transact/v1
    tags:
      - Accounts
      - Banking
      - Core Banking
      - Customers
      - Payments
      - Transactions
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact/documentation
      - type: OpenAPI
        url: https://developer.temenos.com/transact/openapi.json
      - type: Authentication
        url: https://developer.temenos.com/transact/authentication
      - type: Sandbox
        url: https://sandbox.temenos.com/transact
      - type: SDK
        url: https://developer.temenos.com/transact/sdks
      - type: TermsOfService
        url: https://www.temenos.com/terms-of-service/
      - type: PrivacyPolicy
        url: https://www.temenos.com/privacy-policy/
      - type: Support
        url: https://support.temenos.com
      - type: StatusPage
        url: https://status.temenos.com
      - type: ChangeLog
        url: https://developer.temenos.com/transact/changelog
      - type: OpenAPI
        url: openapi/temenos-transact-core-banking-openapi.yml
      - type: JSONSchema
        url: json-schema/temenos-transaction-schema.json
      - type: JSONLD
        url: json-ld/temenos-transact-context.jsonld
    contact:
      - type: Support
        url: https://support.temenos.com
      - type: Email
        email: api.support@temenos.com
      - type: Sales
        url: https://www.temenos.com/contact/
  - name: Temenos Transact Microservices APIs
    description: APIs for Temenos Transact microservices including callback registry, configuration management, user entitlements, and service orchestration for building event-driven and composable banking applications.
    image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
    humanURL: https://developer.temenos.com/transact-microservice-apis
    baseURL: https://api.temenos.com/transact/v1
    tags:
      - Configuration
      - Entitlements
      - Microservices
      - Orchestration
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact-microservice-apis
  - name: Temenos Transact Data Hub APIs
    description: High-performance APIs built on the near real-time Analytics Data Store and Operational Data Store from Temenos Transact Data Hub, providing banking-specific analytical and operational data for reporting and integration use cases.
    image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
    humanURL: https://developer.temenos.com/transact-data-hub
    baseURL: https://api.temenos.com/transact/v1
    tags:
      - Analytics
      - Data Hub
      - Data Store
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact-data-hub
  - name: Temenos Operational Data Store APIs
    description: APIs built on the near real-time Operational Data Store from Temenos Transact Data Hub, presenting data in specific formats for operational and API use cases utilizing real-time data streams and ETL transformations.
    image: https://www.temenos.com/wp-content/uploads/2023/01/temenos-logo.svg
    humanURL: https://developer.temenos.com/operational-data-store
    baseURL: https://api.temenos.com/transact/v1
    tags:
      - Data Streams
      - ETL
      - Operational Data
      - Real-Time
    properties:
      - type: Documentation
        url: https://developer.temenos.com/operational-data-store
common:
  - type: Portal
    url: https://developer.temenos.com/
  - type: GettingStarted
    url: https://developer.temenos.com/article/sandbox-quick-guide
  - type: Documentation
    url: https://developer.temenos.com/guides
  - type: Blog
    url: https://www.temenos.com/blog/the-modern-developer-portal/
  - type: Community
    url: https://basecamp.temenos.com/s/
  - type: Sign Up
    url: https://tcsp-signup.temenos.com/signup/communityregistration
  - type: GitHubOrganization
    url: https://github.com/temenostech
  - type: Website
    url: https://www.temenos.com/
  - type: Support
    url: https://support.temenos.com
  - type: TermsOfService
    url: https://www.temenos.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.temenos.com/privacy-policy/
  - type: PostmanCollection
    url: https://www.postman.com/temenos-devex/temenos-essential-apis/documentation/sd6uv6m/temenos-essential-apis
  - type: Features
    data:
      - name: Arrangement Architecture
        description: Modular, component-based framework enabling reusable product components across retail, corporate, treasury, wealth, and Islamic banking.
      - name: Multi-Currency Support
        description: Full support for multi-currency accounts, payments, and exchange rate management with ISO 4217 compliance.
      - name: KYC and AML Compliance
        description: Built-in customer verification, AML checks, and compliance tracking for regulatory requirements.
      - name: Real-Time Payments
        description: Support for SEPA, SWIFT, ACH, RTGS, and domestic clearing payment types with real-time processing.
      - name: Product Catalog
        description: Configurable product catalog with conditions, eligibility criteria, and arrangement details for banking products.
  - type: UseCases
    data:
      - name: Digital Banking
        description: Build digital banking apps with account management, transaction history, and payment initiation APIs.
      - name: Open Banking
        description: Enable third-party access to banking data and payment services through standardized APIs.
      - name: Loan Origination
        description: Automate loan application, credit assessment, and disbursement workflows through API integration.
      - name: Customer Onboarding
        description: Streamline customer registration with KYC verification, account opening, and beneficiary setup.
  - type: Integrations
    data:
      - name: Payment Networks
        description: Integration with SWIFT, SEPA, ACH, and domestic clearing networks for cross-border and local payments.
      - name: Card Processing
        description: Integration with card issuance and processing networks for debit and credit card operations.
      - name: Regulatory Reporting
        description: Integration with regulatory bodies for compliance reporting, AML screening, and KYC verification.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Banking
  - Core Banking
  - Digital Banking
  - Enterprise
  - Financial Services
  - Fintech
---
