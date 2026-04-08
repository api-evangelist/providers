---
aid: bloomberg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg/refs/heads/main/apis.yml
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
  - type: SDKs
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
  - type: SDKs
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
  - type: SDKs
    url: https://bloomberg.github.io/blpapi-docs/
  - type: Core Developer Guide (PDF)
    url: https://raw.githubusercontent.com/api-evangelist/bloomberg/main/BLPAPI-Core-Developer-Guide%20(1).pdf
  - type: Core User Guide (PDF)
    url: https://raw.githubusercontent.com/api-evangelist/bloomberg/main/BLPAPI-Core-User-Guide.pdf
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/bloomberg/main/openapi/blpapi-core.yml
  - type: JSON Schema
    url: https://raw.githubusercontent.com/api-evangelist/bloomberg/main/json-schema/blpapi-core-messages-schema.json
name: Bloomberg
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
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

