---
aid: bloomberg-terminals
name: Bloomberg Terminals
description: Bloomberg Terminals (Bloomberg Professional Service) are financial software systems providing real-time financial market data, news, analytics, and trading capabilities to financial professionals worldwide. The Terminal offers access to over 35,000 different data types for financial instruments globally, integrated analytics, messaging, and the Bloomberg Open API (BLPAPI) for programmatic data access.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-terminals/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Terminal
  - Bloomberg Professional
  - Market Data
  - Financial Data
  - Trading
  - Analytics
  - Bloomberg
apis:
  - aid: bloomberg-terminals:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: The Bloomberg Open API provides programmatic access to data available in the Bloomberg Terminal including real-time prices, reference data, historical data, news, and analytics. SDKs for C++, Java, Python, C#/.NET, and Perl.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - BLPAPI
      - Market Data
      - Real-Time
      - Terminal API
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
      - type: GitHubRepository
        url: https://github.com/bloomberg/blpapi-node
      - type: SDK
        url: https://pypi.org/project/blpapi/
        title: Python SDK
  - aid: bloomberg-terminals:bloomberg-anywhere-api
    name: Bloomberg Anywhere
    description: Remote access service extending Bloomberg Terminal functionality to any internet-connected device. Provides authentication and secure remote access to Terminal data, analytics, and messaging.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-anywhere/
    baseURL: https://bba.bloomberg.net
    tags:
      - Remote Access
      - Mobile
      - Anywhere
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-anywhere/
  - aid: bloomberg-terminals:bloomberg-launchpad
    name: Bloomberg Launchpad
    description: Customizable Bloomberg Terminal display consisting of smaller panels for monitoring multiple securities, markets, and data streams simultaneously. Supports custom configurations for different workflow types.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-terminal/
    baseURL: blpapi://localhost:8194
    tags:
      - Launchpad
      - Terminal Dashboard
      - Monitoring
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-terminal/
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
        description: Live prices, quotes, and market data for 35,000+ data types globally.
      - name: Reference Data
        description: Static and semi-static security attributes, corporate actions, and fundamentals.
      - name: Historical Data
        description: Historical pricing, volume, and analytics data.
      - name: Bloomberg Analytics
        description: Fixed income, equity, and derivatives analytics functions.
      - name: Bloomberg IB Messaging
        description: Secure messaging for the Bloomberg professional community.
      - name: Bloomberg Anywhere
        description: Remote and mobile access to Terminal capabilities.
  - type: UseCases
    data:
      - name: Trading
        description: Monitor markets and execute trades using Terminal data and analytics.
      - name: Research
        description: Conduct fundamental and quantitative research using Bloomberg data.
      - name: Risk Management
        description: Monitor and manage portfolio risk using Terminal analytics.
      - name: Fixed Income Analysis
        description: Analyze bonds and credit using Bloomberg fixed income functions.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
