---
aid: nasdaq-omx-group
name: Nasdaq
description: Nasdaq is a global technology company serving capital markets and other industries, providing trading, clearing, exchange technology, listing, information, and public company services. Nasdaq Data Link offers REST APIs for accessing financial, economic, and alternative data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://data.nasdaq.com/
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Financial Services
  - Capital Markets
  - Stock Exchange
  - Market Data
  - Economics
apis:
  - aid: nasdaq-omx-group:data-link-time-series
    name: Nasdaq Data Link Time-series API
    description: REST API for retrieving time-series financial data including dataset values, metadata, and combined data and metadata responses across thousands of databases of historical financial and economic data.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.data.nasdaq.com/docs/in-depth-usage
    baseURL: https://data.nasdaq.com/api/v3
    tags:
      - Time Series
      - Financial Data
      - Market Data
      - Datasets
    properties:
      - type: Documentation
        url: https://docs.data.nasdaq.com/docs/in-depth-usage
      - type: GettingStarted
        url: https://docs.data.nasdaq.com/docs
      - type: SignUp
        url: https://data.nasdaq.com/sign-up
  - aid: nasdaq-omx-group:data-link-tables
    name: Nasdaq Data Link Tables API
    description: REST API for retrieving Tables-style datasets, supporting filtering by column, query parameters, and large result sets via pagination or bulk download.
    humanURL: https://docs.data.nasdaq.com/docs/tables-1
    baseURL: https://data.nasdaq.com/api/v3
    tags:
      - Tables
      - Financial Data
      - Datasets
    properties:
      - type: Documentation
        url: https://docs.data.nasdaq.com/docs/tables-1
      - type: SignUp
        url: https://data.nasdaq.com/sign-up
  - aid: nasdaq-omx-group:data-link-streaming
    name: Nasdaq Data Link Streaming API
    description: Streaming API providing real-time delivery of market data through persistent connections.
    humanURL: https://docs.data.nasdaq.com/docs
    baseURL: https://data.nasdaq.com/api/v3
    tags:
      - Streaming
      - Real Time
      - Market Data
    properties:
      - type: Documentation
        url: https://docs.data.nasdaq.com/docs
      - type: SignUp
        url: https://data.nasdaq.com/sign-up
common:
  - type: Website
    url: https://www.nasdaq.com/
  - type: Portal
    url: https://data.nasdaq.com/
  - type: Documentation
    url: https://docs.data.nasdaq.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
