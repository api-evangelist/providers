---
aid: brapi
url: https://raw.githubusercontent.com/api-evangelist/brapi/refs/heads/main/apis.yml
name: brapi
tags:
  - Finance
  - Brazilian Financial Data
  - Stock Market
  - Investments
  - Economic Indicators
  - Cryptocurrency
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-21'
position: Consumer
description: brapi.dev is a Brazilian financial data REST API aggregating public market data from B3 (stock exchange), CVM (securities commission), and Banco Central (central bank). It provides real-time and historical stock quotes, fundamentals, dividends, cryptocurrency prices in BRL, foreign exchange rates, and economic indicators such as IPCA, IGPM, and SELIC. With over 20,000 active developers, brapi.dev offers tiered subscription plans from free to Pro, with up to 500,000 requests per month and data updated every 5 minutes.
apis:
  - aid: brapi:quotes-api
    name: brapi Quotes API
    tags:
      - Stock Quotes
      - B3
      - Real-Time Data
      - Historical Data
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Retrieve real-time and historical OHLCV (Open, High, Low, Close, Volume) quote data for securities listed on the B3 Brazilian stock exchange. Supports bulk asset requests and returns standardized JSON without web scraping.
  - aid: brapi:fundamentals-api
    name: brapi Fundamentals API
    tags:
      - Fundamentals
      - Balance Sheet
      - Income Statement
      - Financial Statements
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Access structured financial statement data for Brazilian listed companies including balance sheets (BP), income statements (DRE), cash flow (DFC), and value added statements (DVA). Historical data available from 2009.
  - aid: brapi:dividends-api
    name: brapi Dividends API
    tags:
      - Dividends
      - Distributions
      - Corporate Actions
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Retrieve complete dividend and earnings distribution history for B3-listed securities, enabling portfolio yield analysis and income tracking.
  - aid: brapi:crypto-api
    name: brapi Cryptocurrency API
    tags:
      - Cryptocurrency
      - BRL
      - Digital Assets
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Access cryptocurrency prices denominated in Brazilian Reals (BRL), supporting investment analysis and portfolio management for Brazilian digital asset investors.
  - aid: brapi:exchange-api
    name: brapi Exchange Rates API
    tags:
      - Foreign Exchange
      - Currency
      - BRL
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Retrieve Brazilian Real (BRL) exchange rates against major global currencies, sourced from Banco Central do Brasil data.
  - aid: brapi:indicators-api
    name: brapi Economic Indicators API
    tags:
      - Inflation
      - Interest Rates
      - Economic Data
      - SELIC
    humanURL: https://brapi.dev/docs
    properties:
      - url: https://brapi.dev/docs
        type: Documentation
    description: Access Brazilian macroeconomic indicators including IPCA (consumer price index), IGPM (market general price index), INPC, and SELIC interest rate data published by Banco Central do Brasil.
common:
  - type: Website
    url: https://brapi.dev
  - type: Documentation
    url: https://brapi.dev/docs
  - type: Pricing
    url: https://brapi.dev/pricing
  - type: Authentication
    url: https://brapi.dev/docs
  - type: SignUp
    url: https://brapi.dev/register
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
