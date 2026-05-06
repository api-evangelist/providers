---
aid: eodhd
url: https://raw.githubusercontent.com/api-evangelist/eodhd/refs/heads/main/apis.yml
name: EODHD
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial
  - Market Data
  - Stock Options
  - Stocks
access: 3rd-Party
created: '2025-02-24'
modified: '2026-04-28'
position: Consumer
specificationVersion: '0.19'
description: Access historical end-of-day stock prices, intraday data, US stock options, and real-time prices with free and advanced plans. EODHD provides financial data for 150,000+ tickers, including stocks, ETFs, funds, and currencies worldwide.
apis:
  - aid: eodhd:eod-historical-data-api
    name: EODHD End-Of-Day Historical Data API
    tags:
      - End Of Day
      - Financial
      - Historical Data
      - Stocks
    humanURL: https://eodhd.com/financial-apis/api-for-historical-data-and-volumes
    properties:
      - url: openapi/eodhd-eod-historical-data-openapi.yml
        type: OpenAPI
      - url: https://eodhd.com/financial-apis/api-for-historical-data-and-volumes
        type: Documentation
    description: Returns end-of-day historical OHLCV data for stocks, ETFs, funds, indices, and currencies across global exchanges. Supports daily, weekly, and monthly periods with both raw and split/dividend-adjusted close prices.
  - aid: eodhd:intraday-historical-data-api
    name: EODHD Intraday Historical Data API
    tags:
      - Financial
      - Historical Data
      - Intraday
      - Stocks
    humanURL: https://eodhd.com/financial-apis/intraday-historical-data-api
    properties:
      - url: https://eodhd.com/financial-apis/intraday-historical-data-api
        type: Documentation
    description: Provides intraday historical OHLCV data at 1-minute, 5-minute, and 1-hour intervals for US stocks and other supported markets, with multi-year lookbacks depending on the resolution.
  - aid: eodhd:live-prices-api
    name: EODHD Live (Delayed) Stock Prices API
    tags:
      - Financial
      - Live Data
      - Real Time
      - Stocks
    humanURL: https://eodhd.com/financial-apis/live-realtime-stocks-api
    properties:
      - url: https://eodhd.com/financial-apis/live-realtime-stocks-api
        type: Documentation
    description: Returns live or 15-20 minute delayed stock quotes including last price, change, volume, and bid/ask data for stocks, ETFs, indices, and forex pairs across global exchanges.
  - aid: eodhd:websockets-api
    name: EODHD WebSockets Real-Time API
    tags:
      - Financial
      - Real Time
      - Streaming
      - WebSockets
    humanURL: https://eodhd.com/financial-apis/new-real-time-data-api-websockets
    properties:
      - url: https://eodhd.com/financial-apis/new-real-time-data-api-websockets
        type: Documentation
    description: Streams real-time trade and quote updates over WebSockets for US stocks, forex, and cryptocurrencies, allowing low-latency consumption of live market data.
  - aid: eodhd:fundamental-data-api
    name: EODHD Fundamental Data API
    tags:
      - Financial
      - Fundamentals
      - Stocks
    humanURL: https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds
    properties:
      - url: https://eodhd.com/financial-apis/stock-etfs-fundamental-data-feeds
        type: Documentation
    description: Provides company fundamentals including general info, financial statements (income statement, balance sheet, cash flow), earnings, valuation ratios, ETF holdings, and mutual fund details.
  - aid: eodhd:options-data-api
    name: EODHD Stock Options API
    tags:
      - Derivatives
      - Financial
      - Options
    humanURL: https://eodhd.com/financial-apis/stock-options-data
    properties:
      - url: https://eodhd.com/financial-apis/stock-options-data
        type: Documentation
    description: Returns US stock options chain data with strikes, expirations, bid/ask, open interest, implied volatility, and Greeks (delta, gamma, theta, vega).
  - aid: eodhd:technical-indicators-api
    name: EODHD Technical Indicators API
    tags:
      - Analytics
      - Financial
      - Technical Indicators
    humanURL: https://eodhd.com/financial-apis/technical-indicators-api
    properties:
      - url: https://eodhd.com/financial-apis/technical-indicators-api
        type: Documentation
    description: Computes common technical indicators server-side, including SMA, EMA, RSI, MACD, Bollinger Bands, ATR, and stochastic oscillators, on top of the EODHD historical price database.
  - aid: eodhd:economic-events-api
    name: EODHD Economic Events Calendar API
    tags:
      - Calendar
      - Economic Data
      - Financial
    humanURL: https://eodhd.com/financial-apis/economic-events-data-api
    properties:
      - url: https://eodhd.com/financial-apis/economic-events-data-api
        type: Documentation
    description: Provides a global economic calendar of macroeconomic releases including country, event name, scheduled time, prior, forecast, and actual values.
  - aid: eodhd:news-sentiment-api
    name: EODHD Financial News and Sentiment API
    tags:
      - Financial
      - News
      - Sentiment
    humanURL: https://eodhd.com/financial-apis/stock-market-financial-news-api
    properties:
      - url: https://eodhd.com/financial-apis/stock-market-financial-news-api
        type: Documentation
    description: Delivers financial news articles tagged by ticker symbol with sentiment scoring (positive, negative, neutral) for use in research, trading signals, and news-driven workflows.
  - aid: eodhd:exchanges-and-tickers-api
    name: EODHD Exchanges and Symbols API
    tags:
      - Exchanges
      - Financial
      - Reference Data
      - Symbols
    humanURL: https://eodhd.com/financial-apis/list-supported-exchanges
    properties:
      - url: https://eodhd.com/financial-apis/list-supported-exchanges
        type: Documentation
    description: Lists supported exchanges and instruments with metadata including ticker, exchange code, name, type, and identifier mappings (CUSIP, ISIN, FIGI) to support symbol lookup and reference data workflows.
common:
  - url: https://eodhd.com/
    name: Website
    type: Website
  - url: https://eodhd.com/financial-apis/
    name: API Documentation
    type: Documentation
  - url: https://eodhd.com/pricing
    name: Pricing
    type: Pricing
  - url: https://eodhd.com/marketplace
    name: Marketplace for the Global Financial Data APIs
    type: Marketplace
  - url: https://eodhd.com/financial-apis-blog/
    name: Financial Blog | EODHD APIs
    type: Blog
  - url: https://forum.eodhd.com/
    name: Financial Data Forum
    type: Forums
  - url: https://eodhd.com/financial-apis/eodhd-affiliate-program
    name: EODHD Affiliate Program
    type: Affiliate
  - url: https://eodhd.com/financial-apis/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://eodhd.com/financial-apis/terms-conditions
    name: Terms and Conditions
    type: TermsOfService
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
