---
aid: avaloq
name: Avaloq
description: Avaloq is a leading provider of wealth management technology and digital banking solutions, offering over 7,500 REST API endpoints for financial services integration. The platform connects more than 170 financial institutions with 200+ fintech partners through Community APIs, Standard Adapters, and certified integrations for banking, wealth management, payments, and compliance.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Digital Banking
  - Financial Services
  - Fintech
  - Payments
  - Wealth Management
url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/apis.yml
created: '2024-01-20'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: avaloq:avaloq-banking-api
    name: Avaloq Banking API
    description: Core banking API providing access to account management, transactions, and customer data for wealth management and digital banking solutions. Supports over 7,500 REST API endpoints for comprehensive banking operations.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Accounts
      - Banking
      - Core Banking
      - Transactions
      - Wealth Management
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: GettingStarted
        url: https://developer.avaloq.com/web/developer-portal/getting-started/developing
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-banking-openapi.yml
  - aid: avaloq:avaloq-wealth-management-api
    name: Avaloq Wealth Management API
    description: Wealth management API providing investment portfolio management, client advisory, and asset management capabilities. Integrates with BlackRock Aladdin for institutional-grade investment management and risk analytics.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Asset Management
      - Investment Management
      - Portfolio Management
      - Wealth Management
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-wealth-management-openapi.yml
  - aid: avaloq:avaloq-payments-api
    name: Avaloq Payments API
    description: Payments processing API supporting domestic and international payment instructions, SEPA transfers, SWIFT messaging, and real-time payment rails for banking clients.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Banking
      - Payments
      - SEPA
      - SWIFT
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-payments-openapi.yml
  - aid: avaloq:avaloq-client-management-api
    name: Avaloq Client Management API
    description: Client onboarding, KYC, and relationship management API for banking and wealth management institutions. Provides customer data management, document collection, and compliance screening for financial services.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Client Management
      - Financial Services
      - KYC
      - Onboarding
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-client-management-openapi.yml
  - aid: avaloq:avaloq-trading-api
    name: Avaloq Trading API
    description: Order management and trading API for executing equity, fixed income, and multi-asset trades through the Avaloq banking platform. Supports order lifecycle management, execution, and settlement.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Banking
      - Financial Services
      - Order Management
      - Trading
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-trading-openapi.yml
  - aid: avaloq:avaloq-compliance-api
    name: Avaloq Compliance & Risk API
    description: Regulatory compliance and risk management API covering AML monitoring, sanctions screening, regulatory reporting, and treasury risk for banking institutions. Supports FINMA, MiFID II, and other regulatory frameworks.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - AML
      - Banking
      - Compliance
      - Regulatory Reporting
      - Risk Management
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-compliance-openapi.yml
  - aid: avaloq:avaloq-community-api
    name: Avaloq Community API
    description: Community APIs for fintech integration providing simplified REST endpoints for connecting third-party applications with the Avaloq banking platform. Pre-vetted by Avaloq for secure, standards-based integration.
    humanURL: https://developer.avaloq.com/
    baseURL: https://api.avaloq.com
    tags:
      - Banking
      - Community
      - Fintech
      - Integration
    properties:
      - type: Documentation
        url: https://developer.avaloq.com/
common:
  - type: Portal
    url: https://developer.avaloq.com/
  - type: Website
    url: https://www.avaloq.com/
  - type: GettingStarted
    url: https://developer.avaloq.com/web/developer-portal/getting-started/developing
  - type: Ecosystem
    url: https://www.avaloq.com/platform/ecosystem
  - type: Academy
    url: https://avaloq.academy/
  - type: Support
    url: https://www.avaloq.com/en/for-developers
  - type: GitHubOrganization
    url: https://github.com/avaloq
  - type: LinkedIn
    url: https://www.linkedin.com/company/avaloq/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/openapi/avaloq-banking-openapi.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/rules/avaloq-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/vocabulary/avaloq-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/avaloq/refs/heads/main/capabilities/avaloq-wealth-management.yaml
  - type: Features
    data:
      - name: 7500+ REST API Endpoints
        description: Over 7,500 REST API endpoints for comprehensive banking and wealth management operations.
      - name: Community APIs
        description: Pre-vetted REST APIs for seamless fintech integration with the Avaloq platform.
      - name: Standard and Certified Adapters
        description: Three adapter types (Standard, Certified, Project) enabling ecosystem connectivity.
      - name: Cloud Sandbox
        description: Sandbox access to Avaloq products in the cloud for integration testing.
      - name: Kafka Integration
        description: Event-driven integration via Apache Kafka for real-time data streaming alongside REST APIs.
      - name: SOAP and REST Support
        description: Dual protocol support for SOAP and REST through the AMI Web Services Framework.
      - name: BlackRock Aladdin Integration
        description: Built-in integration with BlackRock Aladdin for institutional investment management.
      - name: Multi-Jurisdiction Regulatory Support
        description: Support for FINMA, MiFID II, GDPR, and other regulatory frameworks.
  - type: UseCases
    data:
      - name: Wealth Management Platform Integration
        description: Connect advisory tools and portfolio management applications with core banking data.
      - name: Digital Banking Channels
        description: Build mobile and web banking experiences on top of Avaloq account and transaction APIs.
      - name: Fintech Partner Integration
        description: Onboard fintech partners into the banking ecosystem through Community APIs.
      - name: Regulatory Reporting Automation
        description: Automate MiFID II, FINMA, and other regulatory report generation and submission.
      - name: Payment Processing
        description: Integrate domestic SEPA and international SWIFT payment processing.
      - name: KYC and Client Onboarding
        description: Digitize client onboarding with KYC checks, document collection, and compliance screening.
      - name: Investment Portfolio Management
        description: Build robo-advisory and portfolio management tools using investment APIs.
      - name: Trade Order Management
        description: Execute and manage multi-asset trade orders through the Avaloq OMS.
  - type: Integrations
    data:
      - name: BlackRock Aladdin
        description: Native integration with Aladdin by BlackRock for institutional investment management.
      - name: Bloomberg
        description: Market data integration with Bloomberg for pricing and analytics.
      - name: SWIFT
        description: SWIFT messaging network integration for international payment processing.
      - name: SEPA
        description: SEPA credit transfer and direct debit support for European payments.
      - name: AWS
        description: Avaloq Model Bank available on AWS for simplified cloud deployment and testing.
      - name: Salesforce
        description: CRM integration with Salesforce for client relationship management.
      - name: FIX Protocol
        description: FIX protocol support for electronic trading and order routing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
