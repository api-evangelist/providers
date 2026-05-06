---
aid: bloomberg-aim
name: Bloomberg AIM
description: Bloomberg's Asset and Investment Manager (AIM) is a comprehensive buy-side solution offering global, multi-asset capabilities for portfolio management, trading, compliance, and operations. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Data
  - Market Data
  - Order Management
  - Portfolio Management
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-aim/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: bloomberg-aim:bloomberg-data-license-api
    name: Bloomberg Data License API
    description: Provides programmatic access to Bloomberg's comprehensive financial, pricing, reference, regulatory, and alternative data covering over 50 million securities and 56,000 fields via the Hypermedia API (HAPI).
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    baseURL: https://api.bloomberg.com/eap
    tags:
      - Financial Data
      - Market Data
      - Pricing Data
      - Reference Data
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Authentication
        url: https://console.bloomberg.com/about/82
      - type: OpenAPI
        url: openapi/bloomberg-data-license-api.yml
  - aid: bloomberg-aim:bloomberg-server-api
    name: Bloomberg Server API (SAPI)
    description: Server API delivers real-time market data, historical data, premium reference data, and calculation tools from the Bloomberg Terminal into front-office applications.
    humanURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
    tags:
      - Financial Analytics
      - Market Data
      - Real-Time Data
      - Server API
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-aim:bloomberg-emsx-api
    name: Bloomberg EMSX API
    description: The Execution Management System API allows developers to manage and automate trading for equities, futures, and options.
    humanURL: https://www.bloomberg.com/professional/products/trading/execution-management-system/
    baseURL: https://localhost:3000
    tags:
      - Equities
      - Execution Management
      - Order Management
      - Trading
    properties:
      - type: Documentation
        url: https://emsx-api-doc.readthedocs.io/
      - type: OpenAPI
        url: openapi/bloomberg-emsx-api.yml
  - aid: bloomberg-aim:bloomberg-http-api
    name: Bloomberg HTTP API
    description: Makes the Bloomberg Open API available via HTTP and WebSockets, allowing clients to access reference and historical request-response data as well as subscribe to live streaming market data.
    humanURL: https://github.com/bloomberg/blpapi-http
    baseURL: https://localhost:3000
    tags:
      - Historical Data
      - HTTP API
      - Market Data
      - Reference Data
      - Streaming
    properties:
      - type: Documentation
        url: https://github.com/bloomberg/blpapi-http
      - type: OpenAPI
        url: openapi/bloomberg-http-api.yml
      - type: GitHubRepository
        url: https://github.com/bloomberg/blpapi-http
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Documentation
    url: https://bloomberg.github.io/blpapi-docs/
  - type: GettingStarted
    url: https://data.bloomberglp.com/professional/sites/10/2017/03/BLPAPI-Core-Developer-Guide.pdf
  - type: Console
    url: https://console.bloomberg.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/notices/
  - type: Blog
    url: https://www.bloomberg.com/company/stories/category/tech-at-bloomberg/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: SDK
    url: https://github.com/bloomberg/blpapi-node
  - type: SDK
    url: https://github.com/bloomberg/blpapi-python
  - type: SDK
    url: https://github.com/bloomberg/blpapi-java
  - type: Features
    url: https://www.bloomberg.com/professional/products/data/
    data:
      - Access to 50M+ Securities and 56K+ Data Fields
      - Real-Time and Historical Market Data
      - Hypermedia-Driven REST API (HAPI)
      - Execution Management for Equities, Futures, and Options
      - WebSocket Streaming for Live Market Data
      - Instrument and Field Search
      - Scheduled Data Delivery via Triggers
  - type: UseCases
    url: https://www.bloomberg.com/professional/
    data:
      - Automated Portfolio Data Retrieval
      - Algorithmic Trading Order Management
      - Regulatory Compliance Data Extraction
      - Real-Time Market Data Integration
      - Historical Data Analysis and Backtesting
      - Multi-Asset Trade Execution Automation
  - type: Integrations
    url: https://www.bloomberg.com/professional/
    data:
      - Bloomberg Terminal
      - Excel via Bloomberg Add-In
      - Python (blpapi-python)
      - Java (blpapi-java)
      - Node.js (blpapi-node)
      - .NET (blpapi-dotnet)
      - Order Management Systems
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
