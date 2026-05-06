---
aid: lexisnexis
name: LexisNexis
description: LexisNexis is a global provider of legal, regulatory, and business information and analytics. Through the LexisNexis Developer Portal and LexisNexis Risk Solutions, partners can integrate access to legal research, fraud detection, identity verification, and risk assessment capabilities into their applications. Most LexisNexis APIs are partner-access only and require contractual agreements before credentials and OpenAPI specifications are released.
type: Index
position: Producer
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Legal
  - Risk
  - Identity Verification
  - Fraud Detection
  - Compliance
  - Analytics
  - Data
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lexisnexis/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lexisnexis:lexisnexis-developer-portal
    name: LexisNexis Developer Portal
    description: The LexisNexis Developer Portal provides access to legal research and content APIs, allowing partners to integrate LexisNexis legal data and services directly into customer workflows. Access requires a partner account and credentials.
    humanURL: https://dev.lexisnexis.com/
    tags:
      - Legal
      - Research
      - Content
      - Developer Portal
    properties:
      - type: Documentation
        url: https://dev.lexisnexis.com/
  - aid: lexisnexis:lexisnexis-risk-solutions
    name: LexisNexis Risk Solutions
    description: LexisNexis Risk Solutions offers fraud detection, identity verification, and risk orchestration capabilities through partner-accessed APIs, including the Dynamic Decision Platform, ThreatMetrix, and InstantID.
    humanURL: https://risk.lexisnexis.com/
    tags:
      - Risk
      - Fraud Detection
      - Identity Verification
      - Compliance
    properties:
      - type: Documentation
        url: https://risk.lexisnexis.com/products
  - aid: lexisnexis:lexisnexis-threatmetrix
    name: LexisNexis ThreatMetrix
    description: ThreatMetrix delivers digital identity intelligence and behavioral analytics for fraud prevention across user interactions, accounts, and channels. Integration is partner-only.
    humanURL: https://risk.lexisnexis.com/products/threatmetrix
    tags:
      - Fraud Detection
      - Digital Identity
      - Behavioral Analytics
    properties:
      - type: Documentation
        url: https://risk.lexisnexis.com/products/threatmetrix
common:
  - type: Website
    name: LexisNexis Website
    description: Main LexisNexis corporate website.
    url: https://www.lexisnexis.com/
  - type: Developer
    name: LexisNexis Developer Portal
    description: Developer portal for legal content and research APIs.
    url: https://dev.lexisnexis.com/
  - type: Documentation
    name: LexisNexis Risk Solutions Products
    description: Overview of LexisNexis Risk Solutions products and APIs.
    url: https://risk.lexisnexis.com/products
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
