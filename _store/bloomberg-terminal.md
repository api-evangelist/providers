---
aid: bloomberg-terminal
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-terminal/refs/heads/main/apis.yml
apis:
- name: Bloomberg Data API
  description: Provides programmatic access to Bloomberg data including real-time market data, reference data, historical data, and pricing information through the BLPAPI protocol.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://www.bloomberg.com/professional/support/api-library/
  baseURL: https://api.bloomberg.com
  tags:
  - Financial Data
  - Market Data
  - Pricing
  - Real-Time
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Authentication
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://bloomberg.github.io/blpapi-docs/
  - type: SDKs
    url: https://bloomberg.github.io/blpapi-docs/
  - type: Change Log
    url: https://github.com/msitt/blpapi-python/blob/master/changelog.txt
  - type: OpenAPI
    url: openapi/bloomberg-terminal-data-api-openapi.yml
  contact:
  - FN: Bloomberg API Support
    email: apisupport@bloomberg.net
- name: Bloomberg SAPI
  description: Server API (SAPI) providing server-side access to Bloomberg data for institutional clients and enterprise applications. The SDK supports C++, .NET Framework, VBA via COM Data Control, Java, and Python.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
  baseURL: https://api.bloomberg.com/sapi
  tags:
  - Data Feeds
  - Enterprise
  - Institutional
  - Server API
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Getting Started
    url: https://www.bloomberg.com/professional/products/data/data-connectivity/server-api/
  - type: Reference
    url: https://bloomberg.github.io/blpapi-docs/
  - type: SDKs
    url: https://bloomberg.github.io/blpapi-docs/
  - type: OpenAPI
    url: openapi/bloomberg-terminal-sapi-openapi.yml
- name: Bloomberg Desktop API
  description: Desktop API enabling custom applications to integrate directly with Bloomberg Terminal for accessing market data, executing functions, and building custom workflows on the desktop.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://www.bloomberg.com/professional/support/api-library/
  tags:
  - Custom Applications
  - Desktop
  - Excel
  - Terminal Integration
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: SDKs
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://bloomberg.github.io/blpapi-docs/
  - type: Getting Started
    url: https://bloomberg.github.io/blpapi-docs/
  - type: OpenAPI
    url: openapi/bloomberg-terminal-desktop-api-openapi.yml
- name: Bloomberg BPIPE
  description: Bloomberg Market Data Feed (B-PIPE) delivers real-time and reference data from more than 330 exchanges and 5,000 pricing contributors globally, covering 35 million instruments across all asset classes.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://www.bloomberg.com/professional/products/data/enterprise-catalog/real-time-data-feed/
  tags:
  - Market Data Feed
  - Real-Time Data
  - Streaming
  - Systematic Trading
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/products/data/enterprise-catalog/real-time-data-feed/
  - type: Product Info
    url: https://www.bloomberg.com/professional/product/bpipe/
  - type: Getting Started
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://bloomberg.github.io/blpapi-docs/
  - type: OpenAPI
    url: openapi/bloomberg-terminal-bpipe-openapi.yml
- name: Bloomberg Terminal Connect API
  description: Terminal Connect enables developers to create collaborative workflows between third-party systems and the Bloomberg Terminal using a GraphQL API, allowing applications to launch Terminal functions and synchronize with Bloomberg Launchpad.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://github.com/bloomberg/terminal-connect
  baseURL: https://graph.bloomberg.com
  tags:
  - GraphQL
  - Launchpad
  - Terminal Integration
  - Workflow Automation
  properties:
  - type: Documentation
    url: https://github.com/bloomberg/terminal-connect
  - type: GitHubRepository
    url: https://github.com/bloomberg/terminal-connect
  - type: Getting Started
    url: https://github.com/bloomberg/terminal-connect/blob/main/README.md
  - type: OpenAPI
    url: openapi/bloomberg-terminal-terminal-connect-api-openapi.yml
- name: Bloomberg Data License API
  description: The Hypermedia API (HAPI) gives firms programmatic access to Data License content with request-response and subscription-based services, covering reference, pricing, regulatory, and alternative data.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
  tags:
  - Alternative Data
  - Data License
  - Reference Data
  - Regulatory Data
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
  - type: Getting Started
    url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
  - type: Reference
    url: https://bloomberg.github.io/blpapi-docs/
  - type: OpenAPI
    url: openapi/bloomberg-terminal-data-license-api-openapi.yml
- name: Bloomberg BLPAPI HTTP API
  description: The Bloomberg HTTP API makes the Open API available via HTTP and WebSockets, allowing clients to access reference and historical request-response data as well as make subscriptions for live data.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
  humanURL: https://github.com/bloomberg/blpapi-http
  tags:
  - HTTP API
  - Real-Time Data
  - REST
  - WebSockets
  properties:
  - type: Documentation
    url: https://github.com/bloomberg/blpapi-http/blob/develop/doc/http-api-guide.md
  - type: GitHubRepository
    url: https://github.com/bloomberg/blpapi-http
  - type: Getting Started
    url: https://github.com/bloomberg/blpapi-http/blob/develop/doc/http-api-guide.md
  - type: OpenAPI
    url: openapi/bloomberg-terminal-blpapi-http-api-openapi.yml
name: Bloomberg Terminal
tags:
- Analytics
- Enterprise
- Financial Services
- Market Data
- Trading
type: Contract
image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/09/bloomberg-logo-1.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg Terminal is a computer software system provided by Bloomberg L.P. that enables professionals in the financial service sector and other industries to access the Bloomberg Professional service through which users can monitor and analyze real-time financial market data and place trades.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

