---
aid: stockdata
name: StockData
description: StockData.org provides real-time, intraday, and historical stock, forex, and cryptocurrency data along with global financial news and sentiment analysis. The REST API delivers market data for US-listed stocks including OHLCV data, splits, dividends, and entity-level news sentiment from 5,000+ sources in 30+ languages.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Financial Data
  - Stock Market
  - Market Data
  - News
  - Sentiment Analysis
url: https://raw.githubusercontent.com/api-evangelist/stockdata/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stockdata:stockdata
    name: StockData API
    description: The StockData REST API provides free and paid access to real-time stock quotes, intraday price data (adjusted and unadjusted), end-of-day historical data, splits, dividends, financial news with sentiment analysis, trending entities, and entity search. All endpoints require an api_token parameter.
    humanURL: https://www.stockdata.org/
    tags:
      - Finance
      - Financial Data
      - Stock Market
      - Market Data
      - News
      - Sentiment Analysis
    properties:
      - type: Documentation
        url: https://www.stockdata.org/documentation
      - type: Website
        url: https://www.stockdata.org/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stockdata/refs/heads/main/openapi/stockdata-openapi.yml
common:
  - type: Portal
    url: https://www.stockdata.org/
  - type: Documentation
    url: https://www.stockdata.org/documentation
  - type: Sign Up
    url: https://www.stockdata.org/register
  - type: Website
    url: https://www.stockdata.org/
  - type: Pricing
    url: https://www.stockdata.org/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
