---
aid: idenfy
name: iDenfy
description: iDenfy is an identity verification platform providing KYC, KYB, and AML compliance solutions. The iDenfy API enables businesses to verify identities, check for fraud, and comply with regulatory requirements through automated document verification, facial recognition, AML screening, business verification, and bank verification services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AML
  - Compliance
  - Fraud Detection
  - Identity Verification
  - KYB
  - KYC
created: '2024-11-13'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/idenfy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: idenfy:idenfy-verification-api
    name: iDenfy Identity Verification API
    description: The iDenfy Identity Verification (KYC) API provides document verification, selfie checks, and liveness detection through redirect, iFrame, mobile SDK, or direct API integration.
    humanURL: https://documentation.idenfy.com/
    tags:
      - Identity Verification
      - KYC
      - Liveness
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/
  - aid: idenfy:idenfy-business-verification-api
    name: iDenfy Business Verification API
    description: The iDenfy Business Verification (KYB) API enables company verification using registry lookups, ultimate beneficial owner identification, and credit report checks via redirect or iFrame integration.
    humanURL: https://documentation.idenfy.com/
    tags:
      - Business Verification
      - KYB
      - UBO
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/
  - aid: idenfy:idenfy-aml-screening-api
    name: iDenfy AML Screening API
    description: The iDenfy AML Screening API screens individuals and companies against sanctions lists, politically exposed persons (PEPs), and adverse media, with one-time and ongoing monitoring options.
    humanURL: https://documentation.idenfy.com/
    tags:
      - AML
      - Compliance
      - PEP
      - Sanctions
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/
  - aid: idenfy:idenfy-fraud-api
    name: iDenfy Fraud Prevention API
    description: The iDenfy Fraud Prevention API provides risk scoring, proxy detection, phone and address verification, and proof of address checks to identify and stop fraudulent activities.
    humanURL: https://documentation.idenfy.com/fraud/FraudApi/
    tags:
      - Fraud Detection
      - Identity Verification
      - Risk Scoring
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/fraud/FraudApi/
  - aid: idenfy:idenfy-face-authentication-api
    name: iDenfy Face Authentication API
    description: The iDenfy Face Authentication API re-authenticates returning users by comparing a live facial scan against a previously verified identity.
    humanURL: https://documentation.idenfy.com/
    tags:
      - Biometrics
      - Face Authentication
      - Identity Verification
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/
  - aid: idenfy:idenfy-bank-verification-api
    name: iDenfy Bank Verification API
    description: The iDenfy Bank Verification API verifies bank accounts via open banking connections to over 2,500 European banks.
    humanURL: https://documentation.idenfy.com/
    tags:
      - Bank Verification
      - Open Banking
    properties:
      - type: Documentation
        url: https://documentation.idenfy.com/
common:
  - type: Website
    url: https://www.idenfy.com/
  - type: Documentation
    url: https://documentation.idenfy.com/
  - type: Support
    url: https://www.idenfy.com/contact/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
