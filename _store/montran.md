---
aid: montran
specificationVersion: '0.19'
name: Montran
description: Montran Corporation provides technologically advanced critical payments, cash management, and securities solutions to commercial banks, corporates, central banks, and clearing institutions in over 90 countries. With more than 45 years of innovation, Montran offers market infrastructure solutions including RTGS, ACH, instant payments, and central securities depository systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.montran.com
created: '2025'
modified: '2026-04-28'
tags:
  - Banking
  - Central Banking
  - Financial Services
  - ISO 20022
  - Market Infrastructure
  - Messaging
  - Payments
  - Real-Time Payments
  - SWIFT
apis:
  - name: Montran Global Payments Hub
    description: A global, highly secure payment solution that consolidates all payment infrastructures into a payment hub supporting multiple banks, branches, countries, currencies, and languages. Processes clearing and settlement transactions including SEPA, Target2, Fedwire, CHIPS, RTGS, ACH, and cross-border payments.
    image: https://www.montran.com/images/payment-api.png
    humanURL: https://www.montran.com/solutions/global-payments-hub/
    tags:
      - Clearing
      - Cross-Border
      - Multi-Currency
      - Payments
      - Settlement
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/global-payments-hub/
      - type: OpenAPI
        url: openapi/montran-global-payments-hub-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-payment-schema.json
      - type: JSONSchema
        url: json-schema/montran-account-schema.json
      - type: JSONSchema
        url: json-schema/montran-transaction-schema.json
      - type: JSONSchema
        url: json-schema/montran-financial-institution-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Instant Payments Gateway
    description: Enables participants in an instant payments ecosystem to support high volumes of instant payments in a high availability environment. Complies with PSD2 Open API requirements and offers a unified API available 24x7 based on the ISO 20022 messaging standard.
    image: https://www.montran.com/images/messaging-api.png
    humanURL: https://www.montran.com/solutions/instant-payments-gateway/
    tags:
      - Instant Payments
      - ISO 20022
      - Open API
      - PSD2
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/instant-payments-gateway/
      - type: OpenAPI
        url: openapi/montran-instant-payments-gateway-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-payment-schema.json
      - type: JSONSchema
        url: json-schema/montran-account-schema.json
      - type: JSONSchema
        url: json-schema/montran-transaction-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Instant Payments System
    description: A robust 24/7, high-capacity, retail-focused payment solution that processes individual payments in real-time with guaranteed end-to-end payment processing latency of a few seconds. Designed for central banks and payment system operators.
    humanURL: https://www.montran.com/solutions/instant-real-time-payments/
    tags:
      - Central Banking
      - Clearing
      - Instant Payments
      - Market Infrastructure
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/instant-real-time-payments/
  - name: Montran Payments Connectivity
    description: Allows commercial banks to connect to multiple clearing and settlement systems and messaging systems such as SWIFT. Provides a single point of integration between back-office applications and the external world, supporting APIs (REST, SOAP), queue-based, and file-based protocols.
    humanURL: https://www.montran.com/solutions/payments-connectivity/
    tags:
      - Connectivity
      - Integration
      - ISO 20022
      - Messaging
      - SWIFT
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/payments-connectivity/
      - type: OpenAPI
        url: openapi/montran-payments-connectivity-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-financial-institution-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Real-Time Gross Settlement
    description: Provides secure, real-time settlement of high-value interbank payments. Holds a perfect security track record with no successful attacks on any Montran RTGS customer over the past decade.
    humanURL: https://www.montran.com/solutions/real-time-gross-settlement/
    tags:
      - Central Banking
      - High-Value Payments
      - Market Infrastructure
      - RTGS
      - Settlement
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/real-time-gross-settlement/
  - name: Montran Automated Clearing House
    description: An electronic clearing system that enables the full spectrum of payment instructions to be exchanged among financial institutions. Powers some of the largest clearing houses worldwide with support for credit transfers, direct debits, and cheques.
    humanURL: https://www.montran.com/solutions/automated-clearing-house/
    tags:
      - ACH
      - Clearing
      - Credit Transfers
      - Direct Debits
      - Payments
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/automated-clearing-house/
  - name: Montran Automated Transfer System
    description: Handles very high volumes of both high-value and low-value payments such as credit transfers, direct debits, and cheques. Provides a unified clearing and settlement platform for diverse payment types.
    humanURL: https://www.montran.com/solutions/automated-transfer-system/
    tags:
      - Clearing
      - High-Value
      - Low-Value
      - Payments
      - Settlement
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/automated-transfer-system/
  - name: Montran Central Securities Depository
    description: A 24/7, ISO 20022 compliant platform that facilitates safekeeping of dematerialized financial instruments, settlement of trades free or against payment, and calculation and distribution of corporate action entitlements.
    humanURL: https://www.montran.com/solutions/central-securities-depository/
    tags:
      - Corporate Actions
      - Depository
      - Market Infrastructure
      - Securities
      - Settlement
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/central-securities-depository/
  - name: Montran Trading System
    description: Provides a fast, secure, and innovative platform that facilitates the multi-currency trading of financial instruments including debt instruments and equities.
    humanURL: https://www.montran.com/solutions/trading-system/
    tags:
      - Capital Markets
      - Financial Instruments
      - Multi-Currency
      - Securities
      - Trading
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/trading-system/
  - name: Montran Corporate Payments Portal
    description: Enables corporates to exercise complete control over accounts at their various bank relationships, with the ability to make secure payments over the Internet. Supports SWIFT payments and local clearing delivery through API integration and H2H protocols.
    humanURL: https://www.montran.com/solutions/corporate-payments-portal/
    tags:
      - Banking
      - Cash Management
      - Corporate Payments
      - Multi-Bank
      - Treasury
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/corporate-payments-portal/
      - type: OpenAPI
        url: openapi/montran-corporate-payments-portal-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-payment-schema.json
      - type: JSONSchema
        url: json-schema/montran-account-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Virtual Accounts
    description: A bank-agnostic Virtual Account Management platform that enables rapid deployment of virtual account structures for POBO/COBO services, in-house banking, treasury centralization, liquidity management, and escrow services. Provides full Virtual IBAN Management and Open Banking capability.
    humanURL: https://www.montran.com/solutions/virtual-accounts/
    tags:
      - Cash Management
      - Open Banking
      - POBO
      - Treasury
      - Virtual Accounts
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/virtual-accounts/
      - type: OpenAPI
        url: openapi/montran-virtual-accounts-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-account-schema.json
      - type: JSONSchema
        url: json-schema/montran-transaction-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Intraday Liquidity Management
    description: An enterprise-level system delivering real-time liquidity management with live monitoring, an intuitive user interface for granular insight into cash positions, and complete control over cash movement anytime, anywhere.
    humanURL: https://www.montran.com/solutions/intraday-liquidity-management/
    tags:
      - Banking
      - Cash Management
      - Liquidity
      - Monitoring
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/intraday-liquidity-management/
  - name: Montran Cash Pool Engine
    description: Provides multi-currency cash concentration and notional pooling, generating end-of-day or real-time sweeps from accounts held within the bank, its branches, or third-party banks. Supports ZBA, target, threshold, and collar balancing.
    humanURL: https://www.montran.com/solutions/cash-pool-engine/
    tags:
      - Cash Pooling
      - Liquidity
      - Multi-Currency
      - Sweeping
      - Treasury
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/cash-pool-engine/
  - name: Montran Sanctions Screening
    description: Enhanced Filtering System (EFS) providing comprehensive payments filtering and sanctions screening. Supports multiple compliance lists including OFAC, European OFAC, Lloyds MIU, and OFSI. Designed for instant payments with native ISO 20022 support.
    humanURL: https://www.montran.com/solutions/sanctions-screening/
    tags:
      - AML
      - Compliance
      - Risk Management
      - Sanctions
      - Screening
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/sanctions-screening/
      - type: OpenAPI
        url: openapi/montran-sanctions-screening-openapi.yml
      - type: JSONSchema
        url: json-schema/montran-screening-result-schema.json
      - type: JSONLD
        url: json-ld/montran-context.jsonld
  - name: Montran Payments and Collections Factory
    description: A multi-bank POBO/COBO platform using Virtual Account Management to allow corporations to centralize collection and payment-on-behalf-of operations regionally or globally. Available as SaaS or on-premise.
    humanURL: https://www.montran.com/solutions/payments-and-collections-factory/
    tags:
      - COBO
      - Collections
      - Corporate Payments
      - Multi-Bank
      - POBO
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/payments-and-collections-factory/
  - name: Montran In-House Bank
    description: Enables banks to offer in-house banking capability to global corporate customers, providing centralization of operations and controls, bank account rationalization, liquidity optimization, and automation of treasury policy.
    humanURL: https://www.montran.com/solutions/in-house-bank/
    tags:
      - Centralization
      - Corporate
      - In-House Banking
      - Liquidity
      - Treasury
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/in-house-bank/
  - name: Montran Mandate Management
    description: A 24/7, ISO 20022 based, paperless centralized platform for electronic mandates for direct debits and credit transfers. Stores and validates mandates to decrease risks associated with direct debit payments including fraud and operational errors.
    humanURL: https://www.montran.com/solutions/mandate-management/
    tags:
      - Compliance
      - Direct Debits
      - Mandates
      - Payments
      - Risk Management
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/mandate-management/
  - name: Montran Case Management
    description: An online system for the automatic processing of all inquiries related to payments, both foreign and domestic. Provides investigation and compensation capabilities for payment exceptions and disputes.
    humanURL: https://www.montran.com/solutions/case-management/
    tags:
      - Case Management
      - Compensation
      - Disputes
      - Investigation
      - Payments
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/case-management/
  - name: Montran Dispute Management
    description: Provides comprehensive dispute resolution capabilities for payment transactions, enabling financial institutions to manage and resolve payment disputes efficiently.
    humanURL: https://www.montran.com/solutions/dispute-management/
    tags:
      - Banking
      - Case Management
      - Disputes
      - Payments
      - Resolution
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/dispute-management/
  - name: Montran Backup RTGS
    description: A backup real-time gross settlement solution providing business continuity for critical payment infrastructure, ensuring settlement operations continue even during primary system outages.
    humanURL: https://www.montran.com/solutions/backup-rtgs/
    tags:
      - Backup
      - Business Continuity
      - Market Infrastructure
      - RTGS
      - Settlement
    properties:
      - type: Documentation
        url: https://www.montran.com/solutions/backup-rtgs/
common:
  - type: Portal
    url: https://www.montran.com/solutions/
  - type: Documentation
    url: https://www.montran.com/solutions/
  - type: Blog
    url: https://www.montran.com/news-and-insights/
  - type: Support
    url: https://www.montran.com/contact-us/
  - type: Terms of Service
    url: https://www.montran.com/terms-conditions/
  - type: Privacy Policy
    url: https://www.montran.com/privacy-policy/
  - type: Contact
    url: https://www.montran.com/contact-us/
  - type: Website
    url: https://www.montran.com/
  - type: About
    url: https://www.montran.com/company/
  - type: LinkedIn
    url: https://www.linkedin.com/company/montran
  - type: X
    url: https://x.com/montrancorp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://www.montran.com
---
