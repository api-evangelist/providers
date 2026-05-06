---
aid: veryfi
name: Veryfi
description: Veryfi provides AI-powered OCR APIs for extracting structured data from financial documents including receipts, invoices, bank statements, checks, W-2s, W-8s, W-9s, business cards, contracts, and custom documents. The platform captures line items, taxes, totals, barcodes, vendor details, and more across 91 currencies and 38 languages with enterprise-grade accuracy. Veryfi offers SDKs in Python, Node.js, Go, Java, Swift, C#, Ruby, PHP, Rust, Kotlin, and Dart, plus mobile SDKs (Veryfi Lens) for iOS, Android, React Native, Ionic, Xamarin, and Cordova.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Document Processing
  - Finance
  - Invoices
  - OCR
  - Receipts
  - Tax Forms
url: https://raw.githubusercontent.com/api-evangelist/veryfi/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: veryfi:ocr-api
    name: Veryfi OCR API
    description: The Veryfi OCR API (v8) provides AI-powered document data extraction across multiple document types. The base URL is https://api.veryfi.com/api/v8. Authentication uses CLIENT-ID header and AUTHORIZATION header with apikey USERNAME:API_KEY format, plus optional HMAC-SHA256 request signatures (X-Veryfi-Request-Signature and X-Veryfi-Request-Timestamp).
    humanURL: https://docs.veryfi.com/
    tags:
      - AI
      - Document Processing
      - OCR
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/
      - type: Reference
        url: https://docs.veryfi.com/api/
      - type: Authentication
        url: https://docs.veryfi.com/api/getting-started/authentication/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/veryfi/refs/heads/main/openapi/veryfi-ocr-openapi.yml
      - type: Console
        url: https://hub.veryfi.com/
  - aid: veryfi:receipts-invoices-api
    name: Veryfi Receipts & Invoices API
    description: The Veryfi Receipts & Invoices API uses AI-powered OCR to extract structured JSON data from receipts, invoices, bills, and other financial documents. It supports documents in PDF and image formats and returns line-item level data including taxes, totals, vendor details, and barcodes.
    humanURL: https://docs.veryfi.com/
    tags:
      - Document Processing
      - Invoices
      - OCR
      - Receipts
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/
      - type: Reference
        url: https://docs.veryfi.com/api/receipts-invoices/process-a-document/
  - aid: veryfi:bank-statements-api
    name: Veryfi Bank Statements API
    description: The Veryfi Bank Statements API extracts structured data from bank statements using AI-powered OCR, enabling automated reconciliation, fraud detection, and financial data capture workflows.
    humanURL: https://docs.veryfi.com/api/bank-statements/
    tags:
      - Bank Statements
      - Finance
      - OCR
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/api/bank-statements/
      - type: Reference
        url: https://docs.veryfi.com/api/bank-statements/get-a-bank-statement/
  - aid: veryfi:w2-api
    name: Veryfi W-2 API
    description: The Veryfi W-2 API extracts structured data from W-2 wage and tax statements using AI-powered OCR, enabling automated processing of employee wage and tax documents for tax preparation and loan approvals.
    humanURL: https://docs.veryfi.com/api/w2s/
    tags:
      - OCR
      - Tax Forms
      - W-2
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/api/w2s/
  - aid: veryfi:w9-api
    name: Veryfi W-9 API
    description: The Veryfi W-9 API extracts structured data from W-9 Request for Taxpayer Identification forms including TIN, entity type, and address information for HR and vendor management workflows.
    humanURL: https://docs.veryfi.com/api/w9s/
    tags:
      - HR
      - OCR
      - Tax Forms
      - W-9
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/api/w9s/
  - aid: veryfi:checks-api
    name: Veryfi Checks API
    description: The Veryfi Checks API extracts bank routing numbers, account numbers, check numbers, payee names, amounts, and dates from check images using AI-powered OCR.
    humanURL: https://docs.veryfi.com/api/checks/
    tags:
      - Banking
      - Checks
      - OCR
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/api/checks/
  - aid: veryfi:any-docs-api
    name: Veryfi Any Documents API
    description: The Veryfi ∀Docs (Any Documents) API extracts data from any custom document type using named blueprints. Supports contracts, custom forms, and any unstructured document where standard OCR APIs don't apply.
    humanURL: https://docs.veryfi.com/
    tags:
      - Contracts
      - Custom Documents
      - Document Processing
      - OCR
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/
  - aid: veryfi:classification-api
    name: Veryfi Classification API
    description: The Veryfi Classification API determines the document type before processing, enabling intelligent routing to the appropriate extraction endpoint.
    humanURL: https://docs.veryfi.com/
    tags:
      - Classification
      - Document Processing
      - OCR
    properties:
      - type: Documentation
        url: https://docs.veryfi.com/
common:
  - url: https://www.veryfi.com/
    name: Veryfi - OCR APIs for Invoices, Receipts, Checks
    type: Website
    description: Veryfi's main website for AI-powered OCR document extraction APIs.
  - url: https://docs.veryfi.com/
    name: Veryfi API Documentation
    type: Documentation
    description: Comprehensive API reference, tutorials, and integration guides.
  - url: https://hub.veryfi.com/
    name: Veryfi Interactive API Docs
    type: Console
    description: Interactive API explorer for testing Veryfi OCR endpoints.
  - url: https://app.veryfi.com/signup/api/
    name: Veryfi API Sign Up
    type: SignUp
    description: Register for a Veryfi API account.
  - url: https://faq.veryfi.com/
    name: Veryfi Help Center
    type: Support
    description: FAQs, guides, and support for Veryfi APIs.
  - url: https://github.com/veryfi
    name: Veryfi GitHub Organization
    type: GitHubOrganization
    description: Veryfi's GitHub organization hosting SDKs for Python, Node.js, Go, Java, Swift, C#, Ruby, PHP, Rust, Kotlin, Dart, and mobile SDKs (Veryfi Lens) for iOS, Android, React Native, Ionic, and Xamarin.
  - url: https://www.veryfi.com/privacy-policy/
    name: Veryfi Privacy Policy
    type: PrivacyPolicy
    description: Veryfi privacy policy for API data handling.
  - url: https://www.veryfi.com/terms-of-service/
    name: Veryfi Terms of Service
    type: TermsOfService
    description: Veryfi terms of service for API usage.
  - url: https://pypi.org/project/veryfi/
    name: Veryfi Python SDK (PyPI)
    type: SDK
    description: Official Veryfi Python SDK available on PyPI.
  - url: https://www.npmjs.com/package/veryfi
    name: Veryfi Node.js SDK (npm)
    type: SDK
    description: Official Veryfi Node.js SDK available on npm.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
