---
aid: finnhub
name: Finnhub
description: With the sole mission of democratizing financial data, we are proud to offer a FREE realtime API for stocks, forex and cryptocurrency. With this API, you can access realtime market data from stock exchanges, 10 forex brokers, and 15+ crypto exchanges.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-28'
position: Consumer
tags:
  - Financial
  - Market Data
  - Stocks
url: https://raw.githubusercontent.com/api-evangelist/finnhub/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: finnhub:finnhub
    name: Finnhub
    tags:
      - Financial
      - Market Data
      - Stocks
    humanURL: https://finnhub.io/docs/api
    baseURL: https://finnhub.io/api/v1
    properties:
      - url: https://finnhub.io/docs/api
        type: Documentation
      - url: https://github.com/Finnhub-Stock-API
        type: GitHubOrg
      - url: https://finnhub.io/docs/api/websocket-trades
        type: WebSocket
    description: With the sole mission of democratizing financial data, Finnhub offers a realtime REST API for stocks, forex, and cryptocurrency, including market data, company fundamentals, economic data, and alternative datasets.
common:
  - type: Website
    url: https://finnhub.io/
  - type: Documentation
    url: https://finnhub.io/docs/api
  - type: Pricing
    url: https://finnhub.io/pricing
  - type: Sign Up
    url: https://finnhub.io/register
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
