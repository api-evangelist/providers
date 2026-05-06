---
aid: bloomberg-apis
name: Bloomberg APIs
description: Collection of Bloomberg's financial data and news APIs for accessing market data, news content, data licensing, and enterprise connectivity.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Financial Data
  - Market Data
  - News
  - Terminal
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-apis/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: bloomberg-apis:bloomberg-market-data-feed
    name: Bloomberg Market Data Feed
    description: Real-time and historical market data for equities, fixed income, commodities, and currencies.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Equities
      - Fixed Income
      - Market Data
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-apis:bloomberg-news-api
    name: Bloomberg News API
    description: Access to Bloomberg's global news content, including articles, videos, and multimedia.
    humanURL: https://www.bloomberg.com/professional/product/news-data-feeds/
    tags:
      - Articles
      - Content
      - Media
      - News
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/news-data-feeds/
  - aid: bloomberg-apis:bloomberg-data-license-api
    name: Bloomberg Data License API
    description: Bulk data delivery service for historical and reference data.
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    tags:
      - Bulk Data
      - Enterprise
      - Historical Data
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Getting Started
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Terms of Service
    url: https://www.bloomberg.com/notices/tos/
  - type: Privacy Policy
    url: https://www.bloomberg.com/notices/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
