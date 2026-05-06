---
aid: bloomberg-terminal
name: Bloomberg Terminal
description: The Bloomberg Terminal (Bloomberg Professional Service) is the flagship product of Bloomberg LP, providing financial professionals with real-time market data, news, analytics, trading capabilities, and secure messaging through a unified workstation. The Terminal connects over 325,000 subscribers globally and is the standard infrastructure for financial markets professionals. Developers can access Terminal data programmatically via the Bloomberg Open API (BLPAPI).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-terminal/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Terminal
  - Bloomberg Professional Service
  - Market Data
  - Financial Workstation
  - Trading
  - Analytics
  - Bloomberg
apis:
  - aid: bloomberg-terminal:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: The Bloomberg Open API (BLPAPI) enables programmatic access to Bloomberg Terminal data from applications running on the same machine or connecting via Bloomberg's network. Provides real-time data subscriptions, reference data requests, historical data, and Bloomberg analytics. SDKs for Python, Java, C++, C#, and Perl.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - BLPAPI
      - Core API
      - Market Data
      - Real-Time Subscriptions
      - Reference Data
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
      - type: GettingStarted
        url: https://data.bloomberglp.com/professional/sites/10/2017/03/BLPAPI-Core-Developer-Guide.pdf
      - type: GitHubRepository
        url: https://github.com/bloomberg/blpapi-node
      - type: SDK
        url: https://pypi.org/project/blpapi/
        title: Python SDK
      - type: SDK
        url: https://www.npmjs.com/package/blpapi
        title: Node.js SDK
  - aid: bloomberg-terminal:bloomberg-excel-addin
    name: Bloomberg Excel Add-in
    description: Extends Bloomberg Terminal functionality into Microsoft Excel with BDP, BDH, BDS, and BQL formula functions for retrieving real-time, historical, and reference data directly in spreadsheet cells.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-excel/
    baseURL: https://bloomberg.com/excel
    tags:
      - Excel
      - Add-in
      - BDP
      - BDH
      - Formulas
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-excel/
  - aid: bloomberg-terminal:bloomberg-ib
    name: Bloomberg IB (Instant Bloomberg)
    description: Secure messaging platform built into the Bloomberg Terminal enabling real-time communication between financial professionals globally, with compliance archiving and monitoring capabilities.
    humanURL: https://www.bloomberg.com/professional/product/bloomberg-messaging/
    baseURL: blpapi://localhost:8194
    tags:
      - IB
      - Messaging
      - Compliance
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/bloomberg-messaging/
  - aid: bloomberg-terminal:bloomberg-emsx
    name: Bloomberg EMSX
    description: Electronic trading and order management system integrated in the Bloomberg Terminal for routing orders to brokers across equities, fixed income, FX, and derivatives with FIX connectivity and algorithmic trading support.
    humanURL: https://www.bloomberg.com/professional/solution/emsx/
    baseURL: blpapi://localhost:8194
    tags:
      - EMSX
      - Order Management
      - Electronic Trading
      - FIX
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/emsx/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: SDK
    url: https://pypi.org/project/blpapi/
    title: Python SDK (blpapi)
  - type: SDK
    url: https://www.npmjs.com/package/blpapi
    title: Node.js SDK
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Real-Time Market Data
        description: Streaming real-time prices and quotes across global markets.
      - name: Reference Data
        description: Security attributes, identifiers, corporate actions, and fundamentals.
      - name: Historical Data
        description: End-of-day and intraday historical data for all asset classes.
      - name: Fixed Income Analytics
        description: Bond pricing, yield calculations, risk analytics, and scenario analysis.
      - name: Equity Analytics
        description: Equity valuation, relative value, and quantitative screening tools.
      - name: News and Research
        description: Bloomberg News, analyst research, and Bloomberg Intelligence.
      - name: IB Messaging
        description: Compliant secure messaging for the Bloomberg professional network.
      - name: Electronic Trading
        description: EMSX for order routing and execution across asset classes.
      - name: Bloomberg Excel Add-in
        description: BDP, BDH, BDS formulas for Excel integration.
      - name: Bloomberg Anywhere
        description: Mobile and remote access to Terminal capabilities.
  - type: UseCases
    data:
      - name: Market Monitoring
        description: Track real-time price movements and market events across global markets.
      - name: Fixed Income Research
        description: Analyze bonds using Bloomberg's fixed income analytics functions.
      - name: Equity Research
        description: Screen, analyze, and value equities using Terminal data and functions.
      - name: FX Trading
        description: Monitor FX rates and execute currency trades through EMSX.
      - name: Portfolio Management
        description: Manage and analyze investment portfolios with Bloomberg data.
      - name: Quantitative Development
        description: Build quantitative models and strategies using BLPAPI data access.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
