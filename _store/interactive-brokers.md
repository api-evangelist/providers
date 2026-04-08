---
aid: interactive-brokers
url: https://raw.githubusercontent.com/api-evangelist/interactive-brokers/refs/heads/main/apis.yml
apis:
- aid: interactive-brokers:web-api
  name: Interactive Brokers Web API
  tags:
  - Brokerage
  - Market Data
  - Orders
  - Portfolio
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:5000/v1/api
  humanURL: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
  properties:
  - url: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
    type: Documentation
  - url: openapi/interactive-brokers-web-api-openapi.yml
    type: OpenAPI
  description: The Interactive Brokers Web API is a RESTful API that provides programmatic access to IBKR trading, portfolio management, market data, and account information. The API consolidates the Client Portal Web API, Digital Account Management, and Flex Web Service into a unified interface. It supports OAuth 2.0 authentication and provides endpoints for order placement, portfolio monitoring, real-time and historical market data, and account management across global markets.
- aid: interactive-brokers:client-portal-api
  name: Interactive Brokers Client Portal API
  tags:
  - Authentication
  - Brokerage
  - Gateway
  - Trading
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:5000/v1/api
  humanURL: https://interactivebrokers.github.io/cpwebapi/
  properties:
  - url: https://interactivebrokers.github.io/cpwebapi/
    type: Documentation
  description: The Interactive Brokers Client Portal API is a REST API accessed through a locally running Java gateway that routes authenticated requests to IBKR systems. It provides a lightweight interface for trading, viewing portfolio information, accessing market data, and managing authentication. The API uses a two-tiered session structure with read-only and brokerage session levels.
name: Interactive Brokers
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Interactive Brokers’ Client Portal API utilizes a HTTP structure alongside a localhost client to manage requests for market data, orders, and account...
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

