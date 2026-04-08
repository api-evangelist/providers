---
aid: bloomberg-tradebook
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-tradebook/refs/heads/main/apis.yml
apis:
- name: Bloomberg Tradebook Trading API
  description: API for electronic order submission, management, and execution for equities and options trading.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/03/bloomberg-logo.png
  humanURL: https://www.bloombergtradebook.com/solutions/electronic-trading/
  baseURL: https://api.bloombergtradebook.com
  tags:
  - Equities
  - Execution
  - Options
  - Orders
  - Trading
  properties:
  - type: Documentation
    url: https://www.bloombergtradebook.com/api-documentation/
  - type: OpenAPI
    url: https://api.bloombergtradebook.com/v1/openapi.json
  - type: OpenAPI
    url: openapi/bloomberg-tradebook-trading-openapi.yml
  contact:
  - FN: Bloomberg Tradebook API Support
    email: api-support@bloombergtradebook.com
- name: Bloomberg Tradebook Market Data API
  description: Real-time and historical market data including quotes, trades, and reference data.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/03/bloomberg-logo.png
  humanURL: https://www.bloombergtradebook.com/solutions/market-data/
  baseURL: https://api.bloombergtradebook.com/marketdata
  tags:
  - Market-Data
  - Quotes
  - Real-Time
  - Trades
  properties:
  - type: Documentation
    url: https://www.bloombergtradebook.com/marketdata-api-docs/
  - type: Swagger
    url: https://api.bloombergtradebook.com/marketdata/swagger.json
  - type: OpenAPI
    url: openapi/bloomberg-tradebook-market-data-openapi.yml
- name: Bloomberg Tradebook Analytics API
  description: Access to trading analytics, performance metrics, and TCA (Transaction Cost Analysis).
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/03/bloomberg-logo.png
  humanURL: https://www.bloombergtradebook.com/solutions/analytics/
  baseURL: https://api.bloombergtradebook.com/analytics
  tags:
  - Analytics
  - Metrics
  - Performance
  - Tca
  properties:
  - type: Documentation
    url: https://www.bloombergtradebook.com/analytics-api-docs/
  - type: OpenAPI
    url: openapi/bloomberg-tradebook-analytics-openapi.yml
name: Bloomberg Tradebook
tags:
- Algorithms
- Broker
- Equities
- Execution
- Financial Services
- Options
- Trading
type: Contract
image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2021/03/bloomberg-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg Tradebook is an agency broker that provides advanced electronic and high-touch trading services, algorithms, and analytics for equities and options trading.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

