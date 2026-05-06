---
aid: bloomberg-proprietary-technologies
name: Bloomberg Proprietary Technologies
description: Bloomberg Proprietary Technologies encompasses the internally developed technology innovations that power Bloomberg's products and services. This includes Bloomberg's proprietary data network, the BLPAPI connectivity protocol, BQL query language, B-PIPE data distribution technology, FIGI (Financial Instrument Global Identifier) system, and the Bloomberg Generative AI capabilities integrated into its financial data platform.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-proprietary-technologies/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Proprietary Technology
  - BLPAPI
  - BQL
  - FIGI
  - B-PIPE
  - Financial Technology
  - Bloomberg
apis:
  - aid: bloomberg-proprietary-technologies:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: Bloomberg's proprietary socket-based API protocol for accessing Bloomberg data, providing a high-performance connectivity layer between client applications and Bloomberg's data infrastructure.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - BLPAPI
      - Protocol
      - Proprietary API
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-proprietary-technologies:figi-api
    name: Bloomberg FIGI API
    description: The Financial Instrument Global Identifier (FIGI) is Bloomberg's open standard for identifying financial instruments. The OpenFIGI API allows free mapping of tickers, ISINs, CUSIPs, and other identifiers to FIGI codes.
    humanURL: https://www.openfigi.com/api
    baseURL: https://api.openfigi.com
    tags:
      - FIGI
      - Financial Identifiers
      - OpenFIGI
      - Mapping
    properties:
      - type: Documentation
        url: https://www.openfigi.com/api
      - type: OpenAPI
        url: https://api.openfigi.com/schema/openapi.json
  - aid: bloomberg-proprietary-technologies:bql
    name: Bloomberg Query Language (BQL)
    description: Bloomberg's proprietary query language enabling flexible data requests with filtering, aggregation, and calculated field capabilities across Bloomberg's data universe.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: bql://bloomberg.com
    tags:
      - BQL
      - Query Language
      - Proprietary
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: BLPAPI Protocol
        description: Proprietary socket protocol for high-performance Bloomberg data connectivity.
      - name: Bloomberg Query Language
        description: Proprietary query language for flexible financial data requests.
      - name: FIGI Identifier System
        description: Open standard financial instrument identifier with free API access.
      - name: B-PIPE Distribution
        description: Proprietary managed data distribution technology for enterprise.
      - name: Bloomberg AI/ML
        description: Machine learning and AI capabilities integrated into Bloomberg data products.
      - name: Bloomberg Cloud Infrastructure
        description: Cloud-native infrastructure enabling Bloomberg data access from major cloud platforms.
  - type: UseCases
    data:
      - name: Instrument Identification
        description: Map and resolve financial instrument identifiers using FIGI.
      - name: Custom Data Queries
        description: Build custom data requests using Bloomberg Query Language.
      - name: System Integration
        description: Connect enterprise systems to Bloomberg data via BLPAPI.
        url: https://bloomberg.github.io/blpapi-docs/
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
