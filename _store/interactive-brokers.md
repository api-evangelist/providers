---
aid: interactive-brokers
name: Interactive Brokers
description: Interactive Brokers is an online brokerage firm providing trading access to stocks, options, futures, currencies, bonds, and funds across 150+ markets worldwide. IBKR offers comprehensive REST APIs that enable developers and traders to programmatically access trading, portfolio management, market data, and account management capabilities through the IBKR Web API and Client Portal API.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Brokerage
  - Market Data
  - Orders
  - Portfolio
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/interactive-brokers/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: interactive-brokers:web-api
    name: Interactive Brokers Web API
    description: The Interactive Brokers Web API is a RESTful API that provides programmatic access to IBKR trading, portfolio management, market data, and account information. The API consolidates the Client Portal Web API, Digital Account Management, and Flex Web Service into a unified interface. It supports OAuth 2.0 authentication and provides endpoints for order placement, portfolio monitoring, real-time and historical market data, and account management across global markets.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
    baseURL: https://localhost:5000/v1/api
    tags:
      - Brokerage
      - Market Data
      - Orders
      - Portfolio
      - Trading
    properties:
      - type: Documentation
        url: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
      - type: OpenAPI
        url: openapi/interactive-brokers-web-api-openapi.yml
  - aid: interactive-brokers:client-portal-api
    name: Interactive Brokers Client Portal API
    description: The Interactive Brokers Client Portal API is a REST API accessed through a locally running Java gateway that routes authenticated requests to IBKR systems. It provides a lightweight interface for trading, viewing portfolio information, accessing market data, and managing authentication. The API uses a two-tiered session structure with read-only and brokerage session levels.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://interactivebrokers.github.io/cpwebapi/
    baseURL: https://localhost:5000/v1/api
    tags:
      - Authentication
      - Brokerage
      - Gateway
      - Trading
    properties:
      - type: Documentation
        url: https://interactivebrokers.github.io/cpwebapi/
common:
  - type: Portal
    url: https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/
  - type: Documentation
    url: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
  - type: Website
    url: https://www.interactivebrokers.com/
  - type: GitHub
    url: https://github.com/nicholasgasior/interactive-brokers-api
  - type: Login
    url: https://www.interactivebrokers.com/sso/Login
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
