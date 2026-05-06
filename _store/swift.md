---
aid: swift
name: SWIFT
description: SWIFT (Society for Worldwide Interbank Financial Telecommunication) is a global member-owned cooperative providing secure financial messaging services and reference data to financial institutions worldwide. SWIFT offers REST APIs for cross-border payment tracking (GPI), payment pre-validation, reference data lookup (SwiftRef), transaction screening, instant payments, and more. APIs use OAuth 2.0 authentication and are documented using OpenAPI 3.0.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Cross-Border Payments
  - Financial Messaging
  - Financial Services
  - GPI
  - ISO 20022
  - Payments
url: https://raw.githubusercontent.com/api-evangelist/swift/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: swift:swiftref-api
    name: SwiftRef API
    description: The SwiftRef API provides automated real-time lookup and validation of payments reference data including BICs, IBANs, LEIs, National IDs, country codes, and currency codes. Enables straight-through processing by validating financial identifiers before payment execution.
    humanURL: https://developer.swift.com/apis/swiftref-api
    baseURL: https://api.swift.com/swiftrefdata
    properties:
      - type: Documentation
        url: https://developer.swift.com/apis/swiftref-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swift/refs/heads/main/openapi/swift-swiftref-api-openapi.yml
    tags:
      - BIC Validation
      - Financial Reference Data
      - IBAN Validation
      - LEI Validation
      - Reference Data
      - SwiftRef
  - aid: swift:swift-gpi-api
    name: SWIFT GPI API
    description: The SWIFT GPI (Global Payments Innovation) API enables financial institutions to track cross-border payment transactions in real time, update payment statuses, and manage stop-and-recall requests. Uses Unique End-to-End Transaction Reference (UETR) for tracking. Requires OAuth 2.0 authentication via JWT-Bearer grant type (RFC 7523).
    humanURL: https://developer.swift.com/apis/gpi-apis
    baseURL: https://api.swift.com/swift-apigateway
    properties:
      - type: Documentation
        url: https://developer.swift.com/apis/gpi-apis
    tags:
      - Cross-Border Payments
      - GPI
      - ISO 20022
      - Payment Tracking
      - Payments
      - UETR
  - aid: swift:payment-pre-validation-api
    name: Payment Pre-validation API
    description: The SWIFT Payment Pre-validation API allows financial institutions and PSPs to verify payment instruction data against reference data and counterparty information before executing a payment. Checks account numbers, country codes, routing information, and beneficiary account validity to reduce failed payments.
    humanURL: https://developer.swift.com/apis/payment-pre-validation-api
    tags:
      - Compliance
      - Payment Pre-validation
      - Payments
      - Risk Management
      - Straight-Through Processing
    properties:
      - type: Documentation
        url: https://developer.swift.com/apis/payment-pre-validation-api
      - type: ProductPage
        url: https://www.swift.com/products/payment-pre-validation
  - aid: swift:transaction-screening-api
    name: Transaction Screening API
    description: The SWIFT Transaction Screening API enables financial institutions to submit transactions to the SWIFT Transaction Screening Service (TSS) for sanctions and compliance screening before processing. Returns screening results with match details.
    humanURL: https://developer.swift.com/
    tags:
      - AML
      - Compliance
      - Payments
      - Sanctions Screening
      - Transaction Screening
common:
  - type: Website
    url: https://www.swift.com
  - type: DeveloperPortal
    url: https://developer.swift.com
  - type: APIDocumentation
    url: https://developer.swift.com/apis
  - type: APIReference
    url: https://developer.swift.com/reference
  - type: GitHubOrganization
    url: https://github.com/swiftinc
  - type: Sandbox
    url: https://sandbox.swift.com
  - type: ProductPage
    url: https://www.swift.com/products/swift-apis
  - type: Support
    url: https://www.swift.com/contact-us
  - type: TermsOfService
    url: https://developer.swift.com/terms
  - type: PrivacyPolicy
    url: https://www.swift.com/privacy-legal
  - type: ISO20022
    url: https://www.swift.com/standards/iso-20022
  - type: SwiftRef
    url: https://www.swift.com/products/swiftref
  - type: GPI
    url: https://www.swift.com/products/swift-gpi
  - type: PostmanCollection
    url: https://www.postman.com/swift-developer-support/swift-api-sandbox-collections
  - type: Login
    url: https://developer.swift.com/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
