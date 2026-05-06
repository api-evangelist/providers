---
aid: seon-docs
name: SEON
description: SEON is a fraud prevention and AML compliance platform that provides a modular API architecture for fraud detection, identity verification, email enrichment, phone analysis, IP analysis, device fingerprinting, and AML screening. The platform enables businesses to combine multiple fraud signals to score risk and prevent fraudulent transactions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AML Compliance
  - Fraud Prevention
  - Identity Verification
  - Risk Scoring
url: https://raw.githubusercontent.com/api-evangelist/seon-docs/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: seon-docs:fraud-api
    name: SEON Fraud API
    description: The SEON Fraud API is a modular API that combines email, phone number, IP, BIN, and AML APIs with device fingerprinting so you can request and receive enriched data, rules, and scoring in a single API call to detect and prevent fraud.
    humanURL: https://docs.seon.io/api-reference/fraud-api
    tags:
      - Fraud Detection
      - Identity
      - Risk Scoring
    properties:
      - type: Documentation
        url: https://docs.seon.io/api-reference
      - type: Getting Started
        url: https://docs.seon.io/getting-started
      - type: Authentication
        url: https://docs.seon.io/api-reference/introduction
  - aid: seon-docs:email-api
    name: SEON Email API
    description: The SEON Email API is a standalone email enrichment tool that helps identify the approximate minimum age of an email address, its provider, and any connected online profiles.
    humanURL: https://docs.seon.io/api-reference
    tags:
      - Email
      - Enrichment
      - Fraud Prevention
    properties:
      - type: Documentation
        url: https://docs.seon.io/api-reference
  - aid: seon-docs:phone-api
    name: SEON Phone API
    description: The SEON Phone API unlocks insights into a user's phone number history and social or digital profiles connected to it, helping detect fraud and verify user identity.
    humanURL: https://docs.seon.io/api-reference
    tags:
      - Enrichment
      - Fraud Prevention
      - Phone
    properties:
      - type: Documentation
        url: https://docs.seon.io/api-reference
common:
  - type: Portal
    url: https://docs.seon.io/
  - type: Documentation
    url: https://docs.seon.io/api-reference
  - type: Getting Started
    url: https://docs.seon.io/getting-started
  - type: Website
    url: https://seon.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
