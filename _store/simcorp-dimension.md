---
name: SimCorp Dimension
description: Investment management software solution providing APIs for portfolio management, accounting, risk management, and investment operations. SimCorp Dimension is part of the SimCorp One integrated platform, offering Web APIs, Data Distribution APIs, and Streaming APIs through the SimCorp Integration Model (SIM) for front-to-back office investment management.
image: https://www.simcorp.com/logo.png
url: https://www.simcorp.com
created: '2024'
modified: '2026-04-18'
apis:
  - name: SimCorp Dimension Data API
    description: RESTful API for accessing portfolio data, positions, transactions, and market data from SimCorp Dimension.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/products/simcorp-dimension
    baseURL: https://api.simcorp.com/dimension/v1
    tags:
      - Asset Management
      - Financial Services
      - Investment Data
      - Portfolio Management
    properties:
      - type: Documentation
        url: https://developer.simcorp.com/dimension/data-api
      - type: OpenAPI
        url: https://api.simcorp.com/dimension/v1/openapi.json
      - type: Authentication
        url: https://developer.simcorp.com/dimension/authentication
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
  - name: SimCorp Dimension Integration API
    description: API for integrating third-party systems with SimCorp Dimension for data synchronization and workflow automation.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/products/simcorp-dimension/integration
    baseURL: https://api.simcorp.com/dimension/integration/v1
    tags:
      - Data Synchronization
      - Financial Services
      - Integration
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://developer.simcorp.com/dimension/integration-api
      - type: OpenAPI
        url: https://api.simcorp.com/dimension/integration/v1/openapi.json
      - type: Webhooks
        url: https://developer.simcorp.com/dimension/webhooks
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
  - name: SimCorp Dimension Analytics API
    description: API for accessing analytics, performance metrics, risk calculations, and reporting data.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/products/simcorp-dimension/analytics
    baseURL: https://api.simcorp.com/dimension/analytics/v1
    tags:
      - Analytics
      - Performance
      - Reporting
      - Risk Management
    properties:
      - type: Documentation
        url: https://developer.simcorp.com/dimension/analytics-api
      - type: OpenAPI
        url: https://api.simcorp.com/dimension/analytics/v1/openapi.json
      - type: RateLimits
        url: https://developer.simcorp.com/dimension/rate-limits
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
  - name: SimCorp Dimension Web API
    description: Web API providing HTTP-based interfaces for accessing and manipulating SimCorp Dimension data in real-time, supporting stateless RESTful operations across the investment management lifecycle.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/solutions/simcorp-one
    baseURL: https://api.simcorp.com/dimension/web/v1
    tags:
      - Investment Management
      - Real-Time Data
      - REST
      - Web API
    properties:
      - type: Documentation
        url: https://thesim.dev/
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
  - name: SimCorp Dimension Data Distribution API
    description: API for distributing and sharing investment data across integrated systems, supporting event streaming channels and direct data access from SimCorp Dimension.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/solutions/simcorp-one/data-management
    baseURL: https://api.simcorp.com/dimension/datadistribution/v1
    tags:
      - Data Distribution
      - Data Sharing
      - Event Streaming
      - Integration
    properties:
      - type: Documentation
        url: https://thesim.dev/
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
  - name: SimCorp Dimension Streaming API
    description: Real-time streaming API for delivering live investment data, market updates, and event-driven notifications from SimCorp Dimension.
    image: https://www.simcorp.com/api-logo.png
    humanURL: https://www.simcorp.com/solutions/simcorp-one/data-management
    baseURL: https://api.simcorp.com/dimension/streaming/v1
    tags:
      - Event-Driven
      - Market Data
      - Real-Time Data
      - Streaming
    properties:
      - type: Documentation
        url: https://thesim.dev/
    contact:
      - FN: SimCorp API Support
        email: apisupport@simcorp.com
        url: https://www.simcorp.com/support
common:
  - type: Portal
    url: https://www.simcorp.com/solutions/simcorp-one
  - type: Documentation
    url: https://thesim.dev/
  - type: Portfolio Management
    url: https://www.simcorp.com/solutions/simcorp-one/portfolio-management
  - type: Trading and Compliance
    url: https://www.simcorp.com/solutions/simcorp-one/trading-and-compliance
  - type: Risk and Performance
    url: https://www.simcorp.com/solutions/simcorp-one/risk-and-performance
  - type: Operations
    url: https://www.simcorp.com/solutions/simcorp-one/operations
  - type: Accounting
    url: https://www.simcorp.com/solutions/simcorp-one/accounting
  - type: Data Management
    url: https://www.simcorp.com/solutions/simcorp-one/data-management
  - type: Reporting
    url: https://www.simcorp.com/solutions/simcorp-one/reporting
  - type: Client Communications
    url: https://www.simcorp.com/solutions/simcorp-one/Client-Communications-and-Regulatory-Reporting
  - type: Partners
    url: https://www.simcorp.com/partners/open-platform-partners
  - type: Resources
    url: https://en.wikipedia.org/wiki/SimCorp
  - type: Resources
    url: https://www.simcorp.com/about-us/news/2024/simcorp-introduces-new-flagship-platform-simcorp-one
  - type: Support
    url: https://www.dimensionalcommunity.com/insights
  - type: JSONLD
    url: json-ld/simcorp-dimension-context.jsonld
  - type: JSONSchema
    url: json-schema/simcorp-dimension-portfolio-schema.json
  - type: JSONSchema
    url: json-schema/simcorp-dimension-instrument-schema.json
  - type: Features
    data:
      - Front-to-back investment management
      - Real-time portfolio data and analytics
      - Event-driven streaming data distribution
      - Risk and performance measurement
      - Accounting and operations management
      - Trading and compliance monitoring
      - Client communications and regulatory reporting
      - Open platform integration model
  - type: UseCases
    data:
      - Portfolio management and analysis
      - Investment data integration and distribution
      - Risk and performance reporting
      - Regulatory compliance and reporting
      - Real-time market data streaming
      - Multi-asset investment operations
  - type: Integrations
    data:
      - Bloomberg
      - Reuters/Refinitiv
      - SWIFT
      - Clearstream
      - Euroclear
      - Microsoft Excel
      - Tableau
      - Power BI
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Accounting
  - Asset Management
  - Compliance
  - Data Distribution
  - Enterprise Software
  - Financial Data
  - Financial Technology
  - Investment Management
  - Portfolio Management
  - Risk Management
  - SimCorp One
  - Streaming
  - Trading
include:
  - name: Developer Portal
    url: https://developer.simcorp.com
  - name: API Status
    url: https://status.simcorp.com
  - name: Release Notes
    url: https://developer.simcorp.com/changelog
  - name: SimCorp Data Model Portal
    url: https://thesim.dev/
  - name: Dimensional Community
    url: https://www.dimensionalcommunity.com/insights
---
