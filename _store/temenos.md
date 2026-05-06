---
name: Temenos
description: APIs for Temenos banking and financial services platform, providing cloud-native, cloud-agnostic, API-first banking solutions including core banking, digital banking, payments, wealth management, financial crime mitigation, and more.
image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
url: https://www.temenos.com
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.18'
apis:
  - name: Temenos Transact API
    description: Core banking system API for managing accounts, transactions, and customer data. Covers enterprise, holdings, meta, order, party, product, reference, settings, and system API categories with over 290 endpoints spanning retail, corporate, wealth, treasury, and Islamic banking.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/core-banking/
    baseURL: https://api.temenos.com/transact
    tags:
      - Accounts
      - Banking
      - Core Banking
      - Deposits
      - Loans
      - Transactions
      - Treasury
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact-apis
      - type: OpenAPI
        url: https://developer.temenos.com/transact/openapi.json
      - type: Authentication
        url: https://developer.temenos.com/transact/authentication
      - type: SDKs
        url: https://developer.temenos.com/transact/sdks
      - type: GettingStarted
        url: https://developer.temenos.com/article/sandbox-quick-guide
      - type: PostmanCollection
        url: https://www.postman.com/temenos-devex/temenos-essential-apis/collection/sd6uv6m/temenos-essential-apis
      - type: OpenAPI
        url: openapi/temenos-transact-openapi.yml
  - name: Temenos Infinity API
    description: Digital banking platform API for omnichannel customer experiences across retail and business banking channels, including integration with Temenos Fabric and Temenos Visualizer.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/digital-banking/
    baseURL: https://api.temenos.com/infinity
    tags:
      - Business Banking
      - Customer Experience
      - Digital Banking
      - Mobile Banking
      - Omnichannel
      - Retail Banking
    properties:
      - type: Documentation
        url: https://developer.temenos.com/infinity/apis
      - type: OpenAPI
        url: https://developer.temenos.com/infinity/openapi.json
      - type: Portal
        url: https://developer.temenos.com/infinity
      - type: OpenAPI
        url: openapi/temenos-infinity-openapi.yml
  - name: Temenos Payments API
    description: Payment processing and management API supporting multiple payment types including SEPA, SWIFT, PSD2, request-to-pay, bulk payment initiation, direct debit management, and payment stop requests.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/payments/
    baseURL: https://api.temenos.com/payments
    tags:
      - Bulk Payments
      - Direct Debit
      - Open Banking
      - Payment Processing
      - Payments
      - PSD2
      - Real-Time Payments
      - SEPA
      - SWIFT
    properties:
      - type: Documentation
        url: https://developer.temenos.com/open-banking&payments
      - type: OpenAPI
        url: https://developer.temenos.com/payments/openapi.json
      - type: Sandbox
        url: https://sandbox.temenos.com/payments
      - type: OpenAPI
        url: openapi/temenos-payments-openapi.yml
  - name: Temenos Fund Administration API
    description: Investment fund management and administration API powered by Temenos Multifonds for fund accounting, transfer agency, and investor servicing.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/multifonds/
    baseURL: https://api.temenos.com/funds
    tags:
      - Asset Management
      - Fund Accounting
      - Fund Management
      - Investment
      - Wealth Management
    properties:
      - type: Documentation
        url: https://developer.temenos.com/funds/apis
      - type: OpenAPI
        url: https://developer.temenos.com/funds/openapi.json
      - type: OpenAPI
        url: openapi/temenos-fund-administration-openapi.yml
  - name: Temenos Financial Crime Mitigation API
    description: API for anti-money laundering, fraud detection, and compliance including KYC, sanctions screening, and transaction monitoring.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/core-banking/regulatory-compliance/financial-crime-mitigation/
    baseURL: https://api.temenos.com/fcm
    tags:
      - AML
      - Compliance
      - Fraud Detection
      - KYC
      - Risk Management
      - Sanctions Screening
    properties:
      - type: Documentation
        url: https://developer.temenos.com/fcm/apis
      - type: OpenAPI
        url: https://developer.temenos.com/fcm/openapi.json
      - type: OpenAPI
        url: openapi/temenos-financial-crime-mitigation-openapi.yml
  - name: Temenos Transact Data Hub API
    description: High-performance APIs built on the near real-time Analytics Data Store (ADS) and Operational Data Store (ODS), providing banking-specific analytical data for comprehensive intra-day and historical analysis.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/core-banking/analytics/
    baseURL: https://api.temenos.com/transact-data-hub
    tags:
      - Analytics
      - Business Intelligence
      - Data Hub
      - Operational Data
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact-data-hub
      - type: OpenAPI
        url: openapi/temenos-data-hub-openapi.yml
  - name: Temenos Wealth API
    description: Integrated portfolio management and securities trading platform APIs for wealth managers and private bankers, including holdings, inventory, order, party, reference, meta, and system enterprise APIs.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/wealth-management/
    baseURL: https://api.temenos.com/wealth
    tags:
      - Investment Management
      - Portfolio Management
      - Private Banking
      - Securities Trading
      - Wealth Management
    properties:
      - type: Documentation
        url: https://developer.temenos.com/wealth-api
      - type: OpenAPI
        url: openapi/temenos-wealth-openapi.yml
  - name: Temenos Enterprise Product and Pricing API
    description: APIs for product pricing, quotation simulation, package arrangements, pricing adjustments, transparency details, and promotions management for banking products and services.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/core-banking/
    baseURL: https://api.temenos.com/enterprise-pricing
    tags:
      - Banking Products
      - Package Management
      - Product Pricing
      - Promotions
      - Quotation
    properties:
      - type: Documentation
        url: https://developer.temenos.com/temenos-enterprise-product-pricing-apis
      - type: OpenAPI
        url: openapi/temenos-enterprise-product-pricing-openapi.yml
  - name: Temenos Cloud Banking (CMB) API
    description: Country-specific commercial and cloud banking APIs delivering front-to-back services for accounts, deposits, lending, trade finance, and payments with pre-wired APIs and regional regulatory compliance for markets including Australia, Canada, Mexico, UK, US, and more.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/core-banking/
    baseURL: https://api.temenos.com/cmb
    tags:
      - Cloud Banking
      - Commercial Banking
      - Deposits
      - Lending
      - Regional Banking
      - Regulatory Compliance
      - Trade Finance
    properties:
      - type: Documentation
        url: https://developer.temenos.com/cmb
      - type: OpenAPI
        url: openapi/temenos-cloud-banking-openapi.yml
  - name: Temenos Lifecycle Management Suite API
    description: APIs for rapid omnichannel product origination including instant decisioning, covering origination, collections, and middleware integration modules.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/lifecycle-management-suite/
    baseURL: https://api.temenos.com/lms
    tags:
      - Account Origination
      - Collections
      - Decisioning
      - Lifecycle Management
      - Loan Origination
    properties:
      - type: Documentation
        url: https://developer.temenos.com/lifecycle-management-suite
  - name: Temenos Journey Manager API
    description: REST APIs for customer journey orchestration, allowing external systems to integrate with Journey Manager for digital onboarding, form processing, and workflow management. Includes Workspaces API, Transact Fluent API, and Maestro API.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://www.temenos.com/products/journey-manager/
    baseURL: https://journey.temenos.com/api
    tags:
      - Customer Journeys
      - Digital Forms
      - Onboarding
      - Orchestration
      - Workflow
    properties:
      - type: Documentation
        url: https://journey.temenos.com/api/
      - type: GettingStarted
        url: https://journey.temenos.com/docs/LandingPages/GettingStartedLanding.htm
      - type: SDKs
        url: https://journey.temenos.com/api/sdk/introduction/
      - type: Change Log
        url: https://journey.temenos.com/index.php/resources/release-notes
      - type: OpenAPI
        url: openapi/temenos-journey-manager-openapi.yml
  - name: Temenos Transact Microservices API
    description: Cloud-native microservices APIs for Temenos Transact, providing callback registry for long-running transactions, event store for business and system events, configuration management, user entitlements, service orchestration, application metering, and traceability for non-repudiation across all API services.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://developer.temenos.com/transact-microservice-apis
    baseURL: https://api.temenos.com/transact/microservices
    tags:
      - Configuration
      - Entitlements
      - Event Store
      - Microservices
      - Service Orchestration
    properties:
      - type: Documentation
        url: https://developer.temenos.com/transact-microservice-apis
      - type: OpenAPI
        url: openapi/temenos-microservices-openapi.yml
      - type: AsyncAPI
        url: asyncapi/temenos-events-asyncapi.yml
  - name: Temenos Ecosystem API
    description: Composable ecosystem APIs enabling deployment of additional banking solutions from third-party and Exchange providers. Includes adapter and provider contracts for cards fulfillment, digital asset custody, document management, and international payments integrations.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://developer.temenos.com/ecosystem-apis
    baseURL: https://api.temenos.com/ecosystem
    tags:
      - Cards
      - Digital Assets
      - Document Management
      - Ecosystem
      - Integrations
    properties:
      - type: Documentation
        url: https://developer.temenos.com/ecosystem-apis
  - name: Temenos Buy Now Pay Later API
    description: APIs for buy now pay later services with embedded Explainable AI for automated decisioning and credit offer matching. Supports interest-free and interest-bearing BNPL products with point-of-sale integration and full loan lifecycle management. Core banking agnostic and deployable on Temenos Banking Cloud.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://developer.temenos.com/service/buy-now-pay-later
    baseURL: https://api.temenos.com/bnpl
    tags:
      - Buy Now Pay Later
      - Consumer Lending
      - Decisioning
      - Point of Sale
    properties:
      - type: Documentation
        url: https://developer.temenos.com/service/buy-now-pay-later
      - type: OpenAPI
        url: openapi/temenos-bnpl-openapi.yml
  - name: Temenos Explorer API
    description: APIs for the Temenos Explorer framework, providing an API gateway for server-to-server API calls with Keycloak-based authentication, plugin development methods, and customizable banking solution exploration interfaces. Handles authentication, roles, permissions, and CORS management for banking application integration.
    image: https://www.temenos.com/wp-content/uploads/2025/04/Temenos_Logo.png
    humanURL: https://developer.temenos.com/temenos-explorer/docs/guides/overview/
    baseURL: https://api.temenos.com/explorer
    tags:
      - API Gateway
      - Developer Tools
      - Explorer
      - Plugins
    properties:
      - type: Documentation
        url: https://developer.temenos.com/temenos-explorer/docs/guides/developer-guide/
      - type: GettingStarted
        url: https://developer.temenos.com/temenos-explorer/docs/guides/getting-started
      - type: Reference
        url: https://developer.temenos.com/temenos-explorer/docs/developer/plugin-csa/api-methods/
common:
  - type: Developer Portal
    url: https://developer.temenos.com
  - type: Portal
    url: https://apidocs.temenos.com/getting-started
  - type: Getting Started
    url: https://developer.temenos.com/article/welcome-developers
  - type: Authentication
    url: https://developer.temenos.com/authentication
  - type: Rate Limits
    url: https://developer.temenos.com/rate-limits
  - type: Support
    url: https://www.temenos.com/customer-support/
  - type: Terms of Service
    url: https://www.temenos.com/legal-information/website-terms-and-conditions/
  - type: Privacy Policy
    url: https://www.temenos.com/legal-information/privacy-policy/
  - type: Status Page
    url: https://status.temenos.com
  - type: Sandbox
    url: https://sandbox.temenos.com
  - type: SandboxGuide
    url: https://developer.temenos.com/article/sandbox-quick-guide
  - type: Blog
    url: https://www.temenos.com/news
  - type: Guides
    url: https://developer.temenos.com/guides
  - type: APICatalog
    url: https://developer.temenos.com/all-product-apis
  - type: PostmanCollection
    url: https://www.postman.com/temenos-devex/temenos-essential-apis/documentation/sd6uv6m/temenos-essential-apis
  - type: Events
    url: https://developer.temenos.com/article/events-overview
  - type: WebComponents
    url: https://developer.temenos.com/uux/
  - type: GitHubOrganization
    url: https://github.com/temenos
  - type: Community
    url: https://basecamp.temenos.com/s/
  - type: LegalInformation
    url: https://www.temenos.com/legal-information/
  - type: Login
    url: https://basecamp.temenos.com/login
  - type: Sign Up
    url: https://developer.temenos.com/article/get-an-api-key
  - type: Website
    url: https://www.temenos.com
  - type: Documentation
    url: https://docs.temenos.com/
  - type: Change Log
    url: https://developer.temenos.com/release-notes
  - type: Marketplace
    url: https://www.temenos.com/community/marketplace/
  - type: Stacks
    url: https://developer.temenos.com/stacks
  - type: TermsOfUse
    url: https://developer.temenos.com/temenos-developer-community-terms-use
  - type: JSON-LD
    url: json-ld/temenos-context.jsonld
  - type: JSONSchema
    url: json-schema/temenos-account-schema.json
  - type: JSONSchema
    url: json-schema/temenos-customer-schema.json
  - type: JSONSchema
    url: json-schema/temenos-payment-order-schema.json
  - type: JSONSchema
    url: json-schema/temenos-event-schema.json
  - type: JSONStructure
    url: json-structure/temenos-account-structure.json
  - type: JSONStructure
    url: json-structure/temenos-payment-order-structure.json
  - type: JSONStructure
    url: json-structure/temenos-customer-structure.json
  - type: SpectralRules
    url: rules/temenos-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/core-banking.yaml
  - type: NaftikoCapabilities
    url: capabilities/compliance-and-risk.yaml
  - type: NaftikoCapabilities
    url: capabilities/wealth-management.yaml
  - type: Vocabulary
    url: vocabulary/temenos-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Banking
  - Cloud Banking
  - Core Banking
  - Digital Banking
  - Financial Services
  - Fintech
  - Open Banking
  - Payments
  - Wealth Management
---
