---
aid: financial-modeling-prep
name: Financial Modeling Prep
description: Financial Modeling Prep (FMP) provides financial market data via REST APIs, including real-time and historical stock quotes, company fundamentals, income statements, balance sheets, cash flow statements, financial ratios, insider transactions, earnings, dividends, ETF and mutual fund data, and economic indicators - with up to 30 years of historical coverage.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-24'
modified: '2026-04-28'
position: Consumer
tags:
  - Financial Data
  - Market Data
  - Stocks
  - Quotes
  - Fundamentals
  - Financial Statements
  - Historical
url: https://raw.githubusercontent.com/api-evangelist/financial-modeling-prep/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: financial-modeling-prep:financial-modeling-prep
    name: Financial Modeling Prep API
    description: REST API offering real-time and historical stock quotes, financial statements, company profiles, ratios, insider trading, ETFs, and economic data. Authentication via API key passed as the apikey query parameter.
    humanURL: https://site.financialmodelingprep.com/
    baseURL: https://financialmodelingprep.com/api/v3
    tags:
      - Financial Data
      - Market Data
      - Stocks
      - Fundamentals
    properties:
      - type: Documentation
        url: https://site.financialmodelingprep.com/developer/docs
      - type: SignUp
        url: https://site.financialmodelingprep.com/register
      - type: Pricing
        url: https://site.financialmodelingprep.com/developer/docs/pricing
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/financial-modeling-prep/refs/heads/main/openapi/financial-modeling-prep-openapi.yml
common:
  - type: Website
    url: https://site.financialmodelingprep.com/
  - type: Documentation
    url: https://site.financialmodelingprep.com/developer/docs
  - type: SignUp
    url: https://site.financialmodelingprep.com/register
  - type: Pricing
    url: https://site.financialmodelingprep.com/developer/docs/pricing
  - type: Blog
    url: https://site.financialmodelingprep.com/market-news
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
