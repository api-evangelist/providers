---
aid: j-quants
name: J-Quants
description: J-Quants is a financial data API service operated by Japan Exchange Group (JPX) that makes it easy for retail investors to obtain cleansed financial data such as stock prices and financials in historical format. The service democratizes access to raw financial data for investment analysis.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Data
  - Investment
  - Japan
  - Stock Market
created: '2025-02-12'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/j-quants/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: j-quants:j-quants-api
    name: J-Quants API
    description: The J-Quants API (V2) is a data distribution service operated by Japan Exchange Group (JPX) that makes it easy to obtain cleansed financial data such as Japanese stock prices and financials in historical format, enabling investment analysis. Authentication is via API key passed in the x-api-key header.
    humanURL: https://jpx-jquants.com/
    baseURL: https://api.jquants.com/
    tags:
      - Financial Data
      - Japan
      - Stock Market
      - Equities
    properties:
      - type: Documentation
        url: https://jpx-jquants.com/
common:
  - type: Website
    url: https://jpx-jquants.com/
  - type: Documentation
    url: https://jpx-jquants.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
