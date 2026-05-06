---
aid: frankieone
name: FrankieOne
description: FrankieOne is an identity verification, compliance, and fraud prevention platform connecting applications to hundreds of global data sources through a single API for KYC, KYB, document IDV, ongoing monitoring, and matchlist management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-28'
position: Consumer
tags:
  - Identity Verification
  - KYC
  - KYB
  - AML
  - Fraud
  - Compliance
url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: frankieone:kyc-v2
    name: FrankieOne KYC V2 API
    description: KYC V2 API for managing individuals, profiles, workflows, results, and documents. Supports identity verification, AML screening, IDV, fraud checks, duplicate detection, matchlist matching, and ongoing monitoring.
    humanURL: https://docs.frankieone.com/v1.14.1/docs/welcome-to-frankie
    baseURL: https://api.frankie.one
    tags:
      - Identity Verification
      - KYC
      - AML
      - IDV
      - Documents
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.frankieone.com/v1.14.1/docs/welcome-to-frankie
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/openapi/kyc-v2-openapi.json
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/capabilities/frankieone-kyc-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/rules/frankieone-kyc-rules.yml
  - aid: frankieone:core-v2
    name: FrankieOne Core V2 API
    description: Core V2 API for platform-level operations including audit retrieval, workflow discovery, background request status, and matchlist management.
    humanURL: https://docs.frankieone.com/
    baseURL: https://api.frankie.one
    tags:
      - Audit
      - Workflows
      - Matchlists
      - Compliance
    properties:
      - type: Documentation
        url: https://docs.frankieone.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/openapi/core-v2-openapi.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/capabilities/frankieone-core-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/frankieone/refs/heads/main/rules/frankieone-core-rules.yml
common:
  - type: Website
    url: https://www.frankieone.com/
  - type: Documentation
    url: https://docs.frankieone.com/
  - type: SignUp
    url: https://www.frankieone.com/contact-us
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
