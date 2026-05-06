---
aid: bloomberg-applications
name: Bloomberg Applications
description: Collection of Bloomberg's financial data and application APIs for accessing market data, terminal connectivity, real-time streaming feeds, and server-side data access.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise API
  - Financial Analytics
  - Financial Services
  - Market Data
  - Real-Time Data
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-applications/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: bloomberg-applications:bloomberg-data-api
    name: Bloomberg Data API
    description: Provides programmatic access to Bloomberg's financial market data including real-time and historical pricing, reference data, and analytics.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Financial Data
      - Historical Data
      - Market Data
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-applications:bloomberg-terminal-connect-api
    name: Bloomberg Terminal Connect API
    description: Desktop API for accessing Bloomberg Terminal functionality programmatically through Excel, custom applications, and third-party systems.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Desktop API
      - Excel Integration
      - Financial Analytics
      - Terminal
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: SDKs
        url: https://bloomberg.github.io/blpapi-docs/
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Terms of Service
    url: https://www.bloomberg.com/notices/tos/
  - type: Privacy Policy
    url: https://www.bloomberg.com/notices/privacy/
  - type: Getting Started
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
