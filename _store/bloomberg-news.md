---
aid: bloomberg-news
name: Bloomberg News
description: Bloomberg News is a leading global provider of financial news, data, and analysis, delivering breaking news and insights on markets, economics, politics, and business. Bloomberg provides APIs through the Bloomberg Professional Services platform including BLPAPI, Server API, Data License, and market data services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-news/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Analytics
  - Business Intelligence
  - Financial Services
  - Market Data
  - News
apis:
  - aid: bloomberg-news:market-data-api
    name: Bloomberg Market Data API
    description: Provides access to real-time and historical market data including stocks, bonds, commodities, and currencies through the Bloomberg Terminal and enterprise data feeds.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: https://api.bloomberg.com/v1
    tags:
      - Financial Data
      - Historical Data
      - Market Data
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Authentication
        url: https://www.bloomberg.com/professional/support/api-library/#authentication
      - type: GettingStarted
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-news:news-api
    name: Bloomberg News API
    description: Access to Bloomberg's breaking news, articles, and multimedia content covering global markets and business through the Bloomberg Professional platform.
    humanURL: https://www.bloomberg.com/professional/support/news-api/
    baseURL: https://api.bloomberg.com/news/v1
    tags:
      - Articles
      - Business News
      - Financial News
      - News
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/news-api/
      - type: Pricing
        url: https://www.bloomberg.com/professional/pricing/
      - type: GettingStarted
        url: https://developer.bloomberg.com/
  - aid: bloomberg-news:server-api
    name: Bloomberg Server API (SAPI)
    description: Lightweight server-side API that delivers real-time market, historical, and key reference data as well as calculation engine capabilities for proprietary and third-party applications. Available in C, C++, .NET, Python, and Java.
    humanURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
    tags:
      - Enterprise
      - Real-Time Data
      - Reference Data
      - Server API
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
      - type: APIReference
        url: https://bloomberg.github.io/blpapi-docs/
      - type: GettingStarted
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-news:data-license-api
    name: Bloomberg Data License API
    description: Provides programmatic access to Data License content via REST API, SFTP, or cloud providers, with available content including reference, pricing, regulatory, and alternative data for over 50 million securities and 30 thousand fields.
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    tags:
      - Alternative Data
      - Data License
      - Enterprise Data
      - Pricing Data
      - Reference Data
      - Regulatory Data
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
      - type: APIReference
        url: https://developer.bloomberg.com/
      - type: GettingStarted
        url: https://developer.bloomberg.com/
  - aid: bloomberg-news:blpapi
    name: Bloomberg BLPAPI
    description: Core Bloomberg API providing a unified programming interface for Desktop API, Server API, B-PIPE, and Platform products. Available as SDKs for C++, C# (.NET), Java, and Python.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    tags:
      - Core API
      - Desktop API
      - Integration
      - SDK
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
      - type: APIReference
        url: https://bloomberg.github.io/blpapi-docs/
      - type: GettingStarted
        url: https://data.bloomberglp.com/professional/sites/10/2017/03/BLPAPI-Core-Developer-Guide.pdf
      - type: GitHubOrganization
        url: https://github.com/bloomberg
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Documentation
    url: https://bloomberg.github.io/blpapi-docs/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Blog
    url: https://www.bloomberg.com/company/stories/category/tech-at-bloomberg/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/notices/
  - type: Contact
    url: https://www.bloomberg.com/professional/contact-menu/
  - type: Login
    url: https://bba.bloomberg.net/
  - type: Features
    data:
      - name: Real-Time Market Data
        description: Access streaming real-time market data for equities, fixed income, commodities, and currencies.
      - name: Historical Data Services
        description: Query historical pricing, volume, and fundamental data for backtesting and analysis.
      - name: Reference Data
        description: Access comprehensive reference data for securities identification, corporate actions, and classifications.
      - name: News and Research
        description: Programmatic access to Bloomberg breaking news, articles, and research content.
      - name: Enterprise Data Distribution
        description: Server-side APIs for distributing Bloomberg data to internal applications and trading systems.
      - name: Multi-Language SDK Support
        description: SDKs available in Python, Java, C++, C#, and C for cross-platform integration.
  - type: UseCases
    data:
      - name: Quantitative Trading
        description: Build algorithmic trading strategies using real-time and historical market data feeds.
      - name: Risk Management
        description: Calculate portfolio risk metrics using Bloomberg's pricing and analytics data.
      - name: Financial Research
        description: Automate financial research workflows with news, fundamental data, and analytics.
      - name: Regulatory Reporting
        description: Generate regulatory compliance reports using reference data and pricing services.
      - name: Portfolio Management
        description: Integrate Bloomberg data into portfolio management systems for real-time monitoring.
  - type: Integrations
    data:
      - name: Excel
        description: Bloomberg Excel Add-In for spreadsheet-based data analysis and modeling.
      - name: Python
        description: Python SDK (blpapi) for data science and quantitative finance applications.
      - name: MATLAB
        description: Bloomberg Datafeed Toolbox for MATLAB for financial modeling and analysis.
      - name: R
        description: Rblpapi package for accessing Bloomberg data in R statistical computing.
      - name: Trading Platforms
        description: Integration with order management and execution management systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
