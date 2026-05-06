---
aid: bloomberg
name: Bloomberg
description: Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Data License
  - Enterprise
  - Execution Management
  - Financial Services
  - Market Data
  - News
  - Quantitative Analysis
  - Trading
  - Transaction Cost Analysis
url: https://raw.githubusercontent.com/api-evangelist/bloomberg/refs/heads/main/apis.yml
created: '2024-01-20'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: bloomberg:bloomberg-market-data-api
    name: Bloomberg Market Data API
    description: Provides real-time and historical market data, including stock prices, indices, commodities, and currencies.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - Financial Data
      - Indices
      - Market Data
      - Real-Time
      - Stocks
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: SDK
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg:bloomberg-server-api
    name: Bloomberg Server API (SAPI)
    description: Delivers real-time market data, historical data, reference data, and calculation engine capabilities from the Bloomberg Terminal for server applications.
    humanURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
    tags:
      - Enterprise
      - Historical Data
      - Market Data
      - Real-Time
      - Reference Data
      - Server API
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: SDK
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg:bloomberg-data-license-api
    name: Bloomberg Data License API
    description: Provides programmatic access to Bloomberg Data License content including reference, pricing, regulatory, ESG, corporate actions, fundamentals, and alternative data.
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    tags:
      - Data License
      - Enterprise
      - ESG
      - Pricing Data
      - Reference Data
      - Regulatory Data
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
  - aid: bloomberg:bloomberg-emsx-api
    name: Bloomberg EMSX API
    description: Enables programmatic management and automation of equities, futures, and options trading through the Bloomberg Execution Management System.
    humanURL: https://www.bloomberg.com/professional/products/trading/execution-management-system/
    tags:
      - Equities
      - Execution Management
      - Futures
      - Options
      - Orders
      - Trading
    properties:
      - type: Documentation
        url: https://emsx-api-doc.readthedocs.io/
  - aid: bloomberg:bloomberg-blpapi-core
    name: Bloomberg BLPAPI Core
    description: The Bloomberg Open API (BLPAPI) Core — the foundational service-oriented, socket-based API used by the Desktop API, Server API (SAPI), B-PIPE, and Bloomberg Platform products. Provides Request/Response, Subscription, and Publishing paradigms across services including //blp/refdata, //blp/mktdata, //blp/mktbar, //blp/mktvwap, //blp/mktdepthdata, //blp/apiflds, //blp/instruments, //blp/pagedata, and //blp/tasvc.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    tags:
      - B-PIPE
      - BLPAPI
      - Desktop API
      - Historical Data
      - Intraday Bars
      - Intraday Ticks
      - Market Data
      - Open API
      - Reference Data
      - Request Response
      - Server API
      - Subscription
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
      - type: SDK
        url: https://bloomberg.github.io/blpapi-docs/
      - type: OpenAPI
        url: openapi/blpapi-core.yml
      - type: JSONSchema
        url: json-schema/blpapi-core-messages-schema.json
      - type: JSONSchema
        url: json-schema/blpapi-core-error-message-schema.json
      - type: JSONSchema
        url: json-schema/blpapi-core-market-data-event-schema.json
      - type: JSONSchema
        url: json-schema/blpapi-core-subscription-schema.json
      - type: JSONSchema
        url: json-schema/blpapi-core-subscription-list-schema.json
      - type: JSONSchema
        url: json-schema/bloomberg-market-data-schema.json
      - type: JSONSchema
        url: json-schema/bloomberg-security-schema.json
      - type: JSONLD
        url: json-ld/bloomberg-context.jsonld
      - type: JSONLD
        url: json-ld/blpapi-core-context.jsonld
common:
  - type: Portal
    url: https://developer.bloomberg.com/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: SDK
    url: https://bloomberg.github.io/blpapi-docs/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: GettingStarted
    url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
  - type: Login
    url: https://console.bloomberg.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: SpectralRules
    url: rules/bloomberg-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bloomberg-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/market-data.yaml
  - type: Features
    data:
      - name: Real-Time Market Data
        description: Stream live market data for equities, fixed income, commodities, and currencies via subscription.
      - name: Historical Data
        description: Access end-of-day historical time series with periodicity, currency, and corporate-action adjustments.
      - name: Intraday Tick Data
        description: Retrieve raw tick-by-tick trade and quote data for granular intraday analysis.
      - name: Reference Data
        description: Query current reference, descriptive, fundamental, and pricing field values for securities.
      - name: Field Discovery
        description: Search and discover Bloomberg field mnemonics and metadata via the API Data Dictionary.
      - name: Multi-Language SDK
        description: Access BLPAPI through C, C++, Java, .NET, Python, Perl, and COM Excel SDKs.
  - type: UseCases
    data:
      - name: Quantitative Research
        description: Build quantitative models using historical and real-time market data for alpha generation.
      - name: Risk Management
        description: Monitor portfolio risk exposure using real-time pricing and reference data feeds.
      - name: Algorithmic Trading
        description: Feed market data into trading algorithms via EMSX for automated order execution.
      - name: Regulatory Reporting
        description: Access regulatory and compliance data through Data License for reporting requirements.
  - type: Integrations
    data:
      - name: Bloomberg Terminal
        description: Extend Bloomberg Terminal capabilities through the Desktop API integration.
      - name: Excel
        description: Access BLPAPI data directly from Excel spreadsheets using the COM Excel SDK.
      - name: Python
        description: Build data analytics and machine learning pipelines with the Python BLPAPI SDK.
      - name: B-PIPE
        description: Distribute Bloomberg data across enterprise infrastructure using the B-PIPE product.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
