---
aid: argus-investor
url: https://raw.githubusercontent.com/api-evangelist/argus-investor/refs/heads/main/apis.yml
apis:
- name: Argus Research API
  description: Access to equity research reports, stock ratings, and analyst recommendations.
  image: https://www.argusinvestor.com/api-logo.png
  humanURL: https://www.argusinvestor.com/research
  baseURL: https://api.argusinvestor.com/v1
  tags:
  - Analysis
  - Ratings
  - Research
  - Stocks
  properties:
  - type: Documentation
    url: https://developer.argusinvestor.com/docs
  - type: OpenAPI
    url: https://api.argusinvestor.com/openapi.json
  - type: Authentication
    url: https://developer.argusinvestor.com/authentication
  - type: Pricing
    url: https://www.argusinvestor.com/api-pricing
  - type: Terms of Service
    url: https://www.argusinvestor.com/terms
  - type: Support
    url: https://support.argusinvestor.com
  contact:
  - type: Email
    url: api-support@argusinvestor.com
  - type: Twitter
    url: https://twitter.com/argusinvestor
- name: Stock Ratings API
  description: Real-time access to Argus stock ratings and recommendations.
  baseURL: https://api.argusinvestor.com/v1/ratings
  tags:
  - Buy-Sell-Hold
  - Ratings
  - Recommendations
  properties:
  - type: Documentation
    url: https://developer.argusinvestor.com/docs/ratings
  - type: Rate Limits
    url: https://developer.argusinvestor.com/rate-limits
- name: Company Data API
  description: Access fundamental company data, financials, and metrics.
  baseURL: https://api.argusinvestor.com/v1/companies
  tags:
  - Company Data
  - Financials
  - Fundamentals
  properties:
  - type: Documentation
    url: https://developer.argusinvestor.com/docs/companies
name: Argus Investor
tags:
- Equity Analysis
- Financial Data
- Financial Services
- Investment Ratings
- Stock Research
type: Contract
image: https://www.argusinvestor.com/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for accessing Argus Investor research, ratings, and financial data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

