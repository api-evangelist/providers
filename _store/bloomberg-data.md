---
aid: bloomberg-data
name: Bloomberg Data
description: Bloomberg provides financial, software, data, and media services. Their APIs offer access to real-time and historical market data, analytics, and financial information.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Financial Services
  - Market Data
  - News
  - Real-Time Data
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-data/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: bloomberg-data:bloomberg-data-license-api
    name: Bloomberg Data License API
    description: Provides access to Bloomberg's extensive financial data including real-time quotes, historical data, reference data, and analytics.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Analytics
      - Financial Data
      - Historical Data
      - Market Data
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-data:bloomberg-b-pipe-api
    name: Bloomberg B-PIPE API
    description: Real-time streaming market data API delivering quotes, trades, and market depth.
    humanURL: https://www.bloomberg.com/professional/products/data/enterprise-catalog/real-time-data-feed/
    tags:
      - Market Data
      - Quotes
      - Real-Time
      - Streaming
      - Trades
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/enterprise-catalog/real-time-data-feed/
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Terms of Service
    url: https://www.bloomberg.com/notices/tos/
  - type: Privacy Policy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
