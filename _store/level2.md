---
aid: level2
url: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/apis.yml
apis:
- aid: level2:strategy-builder-api
  name: Level2 Strategy Builder API
  tags:
  - Automation
  - Backtesting
  - No-Code
  - Strategies
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://learn.trylevel2.com/docs/overview
  properties:
  - url: https://learn.trylevel2.com/docs/overview
    type: Documentation
  - type: OpenAPI
    url: openapi/level2-strategy-builder-openapi.yml
  description: Level2 provides a visual, no-code strategy builder that allows active traders to create, backtest, and deploy systematic trading strategies using a drag-and-drop interface. The platform enables users to transform trading concepts into fully automated strategies without writing code. It includes real-time backtesting against historical market data, interactive chart analysis, and community-powered strategy sharing. Level2 is developed by Bytemine Technologies Ltd.
- aid: level2:tradestation-integration-api
  name: Level2 TradeStation Integration API
  tags:
  - Automation
  - Brokerage
  - Execution
  - TradeStation
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.trylevel2.com/
  properties:
  - url: https://learn.trylevel2.com/docs/overview
    type: Documentation
  - type: OpenAPI
    url: openapi/level2-tradestation-integration-openapi.yml
  description: Level2 offers a strategic API integration with TradeStation Securities that connects the Level2 visual strategy builder directly to TradeStation user accounts. This integration enables traders to build automated strategies using Level2's drag-and-drop interface and execute them in real time through their TradeStation brokerage accounts.
name: Level2
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Level2 provides an accessible, intuitive platform for anyone to create, backtest, and deploy fully automated trading strategies—no coding or knowledge of proprietary programming languages required.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

