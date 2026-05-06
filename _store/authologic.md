---
aid: authologic
name: Authologic
description: |
  Authologic is an identity verification platform providing businesses with a single API to aggregate multiple ID verification methods including government-issued digital IDs, Bank IDs, document OCR, liveness checks, and AML screening. It supports seamless KYC/KYB workflow integration for businesses across multiple countries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AML
  - Digital Identity
  - eID
  - Identity Verification
  - KYB
  - KYC
  - Liveness Check
url: https://raw.githubusercontent.com/api-evangelist/authologic/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: authologic:authologic-identity-api
    name: Authologic Identity API
    description: |
      The Authologic Identity API enables businesses to initiate identity verification processes and receive results programmatically. Supports document verification, eID, Bank ID, and biometric liveness check methods via a single integration.
    humanURL: https://developer.authologic.com/docs/developer-documentation/product-identity-api-integration
    baseURL: https://api.authologic.com
    tags:
      - eID
      - Identity Verification
      - KYC
      - Liveness
    properties:
      - type: Documentation
        url: https://developer.authologic.com/docs/developer-documentation/product-identity-api-integration
      - type: GettingStarted
        url: https://developer.authologic.com/docs/developer-documentation/integration-overview
  - aid: authologic:authologic-aml-api
    name: Authologic AML API
    description: |
      The Authologic AML API enables Anti-Money Laundering screening combined with identity verification in a single integrated flow for KYC/AML compliance.
    humanURL: https://developer.authologic.com/docs/developer-documentation/product-aml-api-integration-with-identity
    baseURL: https://api.authologic.com
    tags:
      - AML
      - Compliance
      - Identity Verification
      - KYC
    properties:
      - type: Documentation
        url: https://developer.authologic.com/docs/developer-documentation/product-aml-api-integration-with-identity
  - aid: authologic:authologic-data-verification-api
    name: Authologic Data Verification API
    description: |
      The Authologic Data Verification API enables verification of personal data against authoritative sources including government databases and credit bureaus.
    humanURL: https://developer.authologic.com/docs/developer-documentation/product-data-verification-api-integration
    baseURL: https://api.authologic.com
    tags:
      - Data Verification
      - Identity
      - KYC
    properties:
      - type: Documentation
        url: https://developer.authologic.com/docs/developer-documentation/product-data-verification-api-integration
  - aid: authologic:authologic-enquiry-api
    name: Authologic Enquiry API
    description: |
      The Authologic Enquiry API enables background checks and identity enquiries against national and international data sources for enhanced due diligence.
    humanURL: https://developer.authologic.com/docs/developer-documentation/product-enquiry-api-integration
    baseURL: https://api.authologic.com
    tags:
      - Background Check
      - Identity
      - KYB
    properties:
      - type: Documentation
        url: https://developer.authologic.com/docs/developer-documentation/product-enquiry-api-integration
common:
  - type: Website
    url: https://authologic.com/
  - type: Portal
    url: https://developer.authologic.com/
  - type: Documentation
    url: https://developer.authologic.com/docs/developer-documentation/integration-overview
  - type: GettingStarted
    url: https://developer.authologic.com/docs/developer-documentation/integration-overview
  - type: Blog
    url: https://authologic.com/blog/
  - type: SignUp
    url: https://authologic.com/
  - type: PrivacyPolicy
    url: https://authologic.com/privacy-policy/
  - type: Features
    data:
      - name: Single API Integration
        description: One API integration provides access to multiple identity verification methods without separate integrations per provider.
      - name: eID and Bank ID Support
        description: Native support for government-issued digital IDs and Bank IDs across multiple European countries for high-trust verification.
      - name: Document OCR and Liveness
        description: Automated document scanning with OCR and biometric liveness detection to prevent spoofing and fraud.
      - name: AML Screening
        description: Integrated anti-money laundering screening against sanctions lists, PEP databases, and adverse media sources.
      - name: OmniLink
        description: No-integration verification flow using a hosted link for simple verification without technical implementation.
      - name: Modular Workflows
        description: Compose verification workflows from modular steps combining document, biometric, data, and AML checks.
  - type: UseCases
    data:
      - name: Customer Onboarding KYC
        description: Verify customer identities during registration and onboarding for financial services, fintech, and regulated industries.
      - name: AML Compliance
        description: Combine identity verification with AML screening to meet financial institution compliance requirements.
      - name: Business Verification (KYB)
        description: Verify business identities and beneficial owners for B2B onboarding and corporate due diligence.
      - name: Age Verification
        description: Verify user ages using official ID documents for age-restricted products and services.
  - type: Integrations
    data:
      - name: European eID Networks
        description: Integration with national eID infrastructures across multiple European countries for government-backed identity verification.
      - name: Bank ID Systems
        description: Connection to Bank ID systems in Poland, Sweden, Norway, and other markets for bank-verified identity assurance.
      - name: Existing KYC Workflows
        description: Designed to integrate alongside existing KYC/AML infrastructure as modular workflow components.
  - type: Solutions
    data:
      - name: Financial Services KYC
        description: Complete KYC solution for banks, fintechs, and payment providers with AML screening and document verification.
      - name: Digital Identity Verification
        description: Aggregate multiple ID verification methods via single API for flexible identity assurance across user populations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
