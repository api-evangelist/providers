---
name: Bloomberg Professional Service
description: Bloomberg Professional Service is a comprehensive financial data, news, and analytics platform serving investment professionals worldwide. It provides real-time and historical market data, trading capabilities, news, research, and analytical tools for financial markets.
image: https://www.bloomberg.com/company/press/wp-content/uploads/sites/40/2018/02/Bloomberg_Logo_2018.png
url: https://www.bloomberg.com/professional/
created: 2024-01-20T00:00:00.000Z
modified: '2026-04-18'
apis:
  - name: Bloomberg Data License API
    description: Provides programmatic access to Bloomberg's comprehensive financial data including pricing, reference data, fundamentals, and historical information. Content can be accessed via a REST API, SFTP, or natively in all major cloud providers, with bulk datasets available daily spanning 20+ years of history.
    baseURL: https://www.bloomberg.com/professional/product/data-license/
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/data-license/
      - type: Pricing
        url: https://www.bloomberg.com/professional/product/data-license/#pricing
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    tags:
      - Cloud
      - ESG
      - Financial Data
      - Fundamentals
      - Historical Data
      - Market Data
      - Reference Data
  - name: Bloomberg API (BLPAPI)
    description: Desktop API enabling custom applications to access Bloomberg data and functionality programmatically through the Bloomberg Terminal. Supports development in C++, Java, C# (.NET), Python, and other languages, providing 24x7 programmatic access to streaming real-time and delayed data, reference data, historical data, and intraday data.
    baseURL: https://www.bloomberg.com/professional/support/api-library/
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
      - type: SDK
        url: https://www.bloomberg.com/professional/support/software-updates/
      - type: CodeExamples
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: SDK
        url: https://github.com/bloomberg/blpapi-node
      - type: SDK
        url: https://github.com/bloomberg/blpapi-hs
    tags:
      - Desktop API
      - Real-Time Data
      - SDK
      - Terminal Integration
      - Trading
  - name: Bloomberg SAPI (Server API)
    description: Server-side API delivering the same real-time market data, historical data, premium reference data, and calculation tools available with the Bloomberg Terminal for seamless use in proprietary and Bloomberg-approved client server applications. Supports C++, .NET, VBA via COM, Java, and Python, and leverages existing Bloomberg Terminal exchange entitlements.
    baseURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
    humanURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
      - type: Documentation
        url: https://www.bloomberg.com/professional/insights/data/bloombergs-server-api-what-you-need-to-know/
      - type: Support
        url: https://www.bloomberg.com/professional/support/
    tags:
      - Cloud
      - Enterprise
      - Integration
      - Market Data
      - Server API
  - name: Bloomberg B-PIPE
    description: Real-time streaming market data feed providing access to 35 million instruments across all asset classes, aggregated from 330+ exchanges and 5,000+ contributors. Supports Bloomberg composite tickers and market indices with low latency delivery for algorithmic trading, quantitative analysis, and non-display applications. Available via cloud connectivity on AWS and Azure.
    baseURL: https://www.bloomberg.com/professional/product/b-pipe/
    humanURL: https://www.bloomberg.com/professional/product/b-pipe/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/b-pipe/
      - type: Marketplace
        url: https://aws.amazon.com/financial-services/partner-solutions/bloomberg-b-pipe/
    tags:
      - Algorithmic Trading
      - Cloud
      - Low Latency
      - Market Data Feed
      - Real-Time
      - Streaming
  - name: Bloomberg Hypermedia API (HAPI)
    description: Provides programmatic access to Data License content with a combination of request-response and subscription-based services. Available content includes reference, pricing, regulatory, and alternative data. Uses JWT authentication and supports both bulk subscription-based datasets and per-security datasets.
    baseURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    tags:
      - Alternative Data
      - Data License
      - Pricing Data
      - Reference Data
      - Regulatory Data
      - REST API
  - name: Bloomberg HTTP API
    description: HTTP wrapper making the Bloomberg Open API available via HTTP and WebSockets, allowing clients to access reference and historical request/response data as well as make subscriptions for live data without native BLPAPI SDK integration.
    baseURL: https://github.com/bloomberg/blpapi-http
    humanURL: https://github.com/bloomberg/blpapi-http
    properties:
      - type: Documentation
        url: https://github.com/bloomberg/blpapi-http/blob/develop/doc/http-api-guide.md
      - type: GitHubRepository
        url: https://github.com/bloomberg/blpapi-http
    tags:
      - Historical Data
      - HTTP
      - Open Source
      - Real-Time Data
      - REST API
      - WebSockets
  - name: Bloomberg Terminal Connect API
    description: Enables synchronization of actions across third-party applications and the Bloomberg Terminal. Allows developers to initiate Bloomberg functions within external applications and synchronize with Bloomberg Launchpad for seamless Terminal integration workflows.
    baseURL: https://www.bloomberg.com/professional/support/api-library/
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: DeveloperPortal
        url: https://developer.bloomberg.com/
    tags:
      - Desktop
      - Launchpad
      - Synchronization
      - Terminal Integration
  - name: Bloomberg App Portal
    description: Platform for building, connecting, and scaling third-party applications within the Bloomberg Terminal ecosystem. Developers can create extensions published and distributed to Bloomberg Terminal subscribers across categories including data analysis, portfolio management, risk analysis, and data visualization.
    baseURL: https://www.bloomberg.com/professional/solutions/asset-management/developer/
    humanURL: https://www.bloomberg.com/professional/solutions/asset-management/developer/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
      - type: DeveloperPortal
        url: https://developer.bloomberg.com/
    tags:
      - App Marketplace
      - Developer Platform
      - Terminal Extensions
      - Third Party Apps
  - name: Bloomberg Data License Plus (DL+)
    description: Fully managed, public cloud-based data management solution that brings Bloomberg data together in a centralized platform for easier and more consistent delivery to downstream systems.
    baseURL: https://www.bloomberg.com/professional/products/data/data-management/dms/
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/dms/
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/dms/
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Cloud
      - Data License
      - Data Management
      - Enterprise
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: DeveloperPortal
    url: https://developer.bloomberg.com/
  - type: DeveloperPortal
    url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
  - type: Documentation
    url: https://bloomberg.github.io/blpapi-docs/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: StatusPage
    url: https://www.bloomberg.com/professional/support/software-updates/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: Resources
    url: https://bloomberg.github.io/
  - type: Resources
    url: https://www.bloomberg.com/professional/products/data/data-connectivity/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/notices/
  - type: Contact
    url: https://www.bloomberg.com/professional/request-demo/
  - type: Features
    data:
      - Real-time and historical market data access
      - Desktop API for Bloomberg Terminal integration
      - Server-side API for enterprise applications
      - B-PIPE low-latency streaming data feed
      - Hypermedia API for Data License content
      - HTTP/WebSocket wrapper for BLPAPI
      - Terminal Connect for third-party app synchronization
      - App Portal for Terminal ecosystem extensions
  - type: UseCases
    data:
      - Algorithmic and quantitative trading
      - Portfolio management and risk analysis
      - Financial data integration and reporting
      - Real-time market data distribution
      - Custom Terminal application development
      - Enterprise data management and analytics
  - type: Integrations
    data:
      - Bloomberg Terminal
      - AWS
      - Microsoft Azure
      - Python
      - Java
      - C++ / .NET
      - Node.js
      - Haskell
tags:
  - Analytics
  - Cloud
  - Data Management
  - Enterprise
  - Financial Services
  - Market Data
  - Open Source
  - Real-Time Data
  - Trading
---
