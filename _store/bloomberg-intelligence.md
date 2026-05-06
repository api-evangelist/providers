---
aid: bloomberg-intelligence
name: Bloomberg Intelligence
description: Bloomberg Intelligence provides research, data, and analytics on companies, industries, credit, government, litigation, and ESG. The Bloomberg developer platform offers BLPAPI (Bloomberg Open API) for real-time and reference data, BQL (Bloomberg Query Language) for flexible data queries, Data License for enterprise data delivery, and Server API / B-PIPE for high-performance data distribution.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-intelligence/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Company Analysis
  - Credit Research
  - ESG Data
  - Financial Data
  - Financial Research
  - Market Data
  - Market Intelligence
apis:
  - aid: bloomberg-intelligence:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: The core Bloomberg API providing real-time market data, reference data, historical data, and intraday tick data. SDKs available for C++, Java, Python, C#/.NET, and Perl. Connects to Bloomberg Terminal and Enterprise products.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - Core API
      - Market Data
      - Real-Time Data
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
  - aid: bloomberg-intelligence:bql
    name: Bloomberg Query Language (BQL)
    description: A powerful query language for requesting Bloomberg data with flexible filtering, aggregation, and calculation capabilities. Enables custom data requests beyond standard API fields.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: bql://bloomberg.com
    tags:
      - Analytics
      - Data Query
      - Query Language
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-intelligence:data-license
    name: Bloomberg Data License API
    description: Enterprise data delivery platform providing bulk financial data via SFTP and SOAP API. Supports requesting reference data, pricing data, corporate actions, and derived data for specified securities and data fields.
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    baseURL: https://dlws.bloomberg.com
    tags:
      - Bulk Data
      - Data License
      - Enterprise
      - SFTP
      - SOAP
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
  - aid: bloomberg-intelligence:server-api
    name: Bloomberg Server API (SAPI)
    description: High-performance server-side API for distributing Bloomberg data within enterprise environments. Supports B-PIPE for managed data distribution with authentication, authorization, and entitlement management.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: blpapi://server:8194
    tags:
      - B-PIPE
      - Enterprise
      - High Performance
      - Server API
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-intelligence:research-api
    name: Bloomberg Intelligence Research API
    description: Access to Bloomberg Intelligence research reports, analyst insights, industry analysis, and company research across equities, credit, government, and ESG.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-intelligence/
    baseURL: https://api.bloomberg.com/intelligence
    tags:
      - Analysis
      - ESG
      - Industry Research
      - Reports
      - Research
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-intelligence/
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: GettingStarted
    url: https://bloomberg.github.io/blpapi-docs/
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
        description: Streaming real-time prices, quotes, and market activity across global markets.
      - name: Reference Data
        description: Static and semi-static security attributes, corporate actions, and fundamentals.
      - name: Historical Data
        description: End-of-day and intraday historical pricing, volume, and analytics data.
      - name: Intraday Tick Data
        description: Tick-by-tick trade and quote data for detailed market microstructure analysis.
      - name: Bloomberg Query Language (BQL)
        description: Flexible query language for custom data requests with filtering and aggregation.
      - name: Data License
        description: Bulk enterprise data delivery via SFTP and SOAP for reference data, pricing, and analytics.
      - name: B-PIPE Data Distribution
        description: Managed high-performance data distribution with entitlement management for enterprise.
      - name: Intelligence Research
        description: Analyst research reports, industry analysis, and ESG insights from Bloomberg Intelligence.
      - name: Multi-Language SDKs
        description: Official SDKs for Python, Java, C++, C#/.NET, Node.js, and Perl.
      - name: Enterprise Authentication
        description: Authentication, authorization, and permissioning for enterprise data distribution.
  - type: UseCases
    data:
      - name: Trading Systems
        description: Feed real-time market data into trading and execution management systems.
      - name: Risk Management
        description: Source pricing and reference data for portfolio risk calculations.
      - name: Quantitative Research
        description: Access historical data and BQL for quantitative analysis and backtesting.
      - name: Portfolio Analytics
        description: Retrieve security attributes and pricing for portfolio valuation and attribution.
      - name: Compliance and Reporting
        description: Source reference data for regulatory reporting and compliance.
      - name: Data Warehousing
        description: Bulk load financial data via Data License for enterprise data warehouses.
      - name: ESG Analysis
        description: Access Bloomberg Intelligence ESG scores and research for sustainable investing.
      - name: Credit Research
        description: Access credit analysis, ratings data, and fixed income research.
  - type: Solutions
    data:
      - name: Bloomberg Terminal
        description: Professional terminal with integrated BLPAPI for desktop application development.
      - name: Bloomberg Enterprise
        description: Server API and B-PIPE for enterprise-wide data distribution.
      - name: Bloomberg Data License
        description: Bulk data delivery platform for enterprise data management.
      - name: Bloomberg Intelligence
        description: Research and analysis platform with proprietary data and expert insights.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
