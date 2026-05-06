---
aid: intercontinental-exchange
name: Intercontinental Exchange
description: Intercontinental Exchange (ICE) operates global exchanges, clearing houses, and data services for financial and commodity markets, including the New York Stock Exchange (NYSE). ICE provides multiple developer portals including the Developer Center at developer.theice.com for market data APIs, the IDS Portal for real-time data integration, and the ICE Mortgage Technology Developer Portal for lending application development.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commodities
  - Financial Exchanges
  - Market Data
  - NYSE
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/intercontinental-exchange/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: intercontinental-exchange:consolidated-feed-api
    name: ICE Consolidated Feed API
    description: The ICE Consolidated Feed API provides developers with access to ICE Data Services real-time and delayed market data. The API delivers consolidated market data feeds from exchanges operated by Intercontinental Exchange including ICE Futures, NYSE, and other trading venues. The Developer Center provides detailed API documentation, samples, and SDK downloads.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.theice.com/hc/en-us
    baseURL: https://api.theice.com
    tags:
      - Exchanges
      - Financial Data
      - Market Data
      - Real-Time Data
      - Trading
    properties:
      - type: Portal
        url: https://developer.theice.com/hc/en-us
      - type: Documentation
        url: https://developer.theice.com/hc/en-us/articles/200717514-About-the-Consolidated-Feed-API
      - type: OpenAPI
        url: openapi/ice-consolidated-feed-api-openapi.yml
  - aid: intercontinental-exchange:data-services-api
    name: ICE Data Services API
    description: The ICE Data Services API provides access to market data, reference data, and analytics from Intercontinental Exchange. The IDS Portal provides documentation, tools, and software required for integrating with ICE Data Services real-time market data solutions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://idsportal.icedataservices.com/marketdata
    baseURL: https://idsportal.icedataservices.com
    tags:
      - Analytics
      - Financial Services
      - Market Data
      - Reference Data
    properties:
      - type: Portal
        url: https://idsportal.icedataservices.com/marketdata
      - type: Documentation
        url: https://idsportal.icedataservices.com/marketdata
  - aid: intercontinental-exchange:mortgage-technology-api
    name: ICE Mortgage Technology Developer Portal
    description: The ICE Mortgage Technology Developer Portal is a self-service solution providing developers with resources and documentation to build and deploy mortgage lending applications. It includes a comprehensive integration catalog representing the servicing life cycle for mortgage origination and servicing workflows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://mortgagetech.ice.com/products/developer-portal
    baseURL: https://api.mortgagetech.ice.com
    tags:
      - Financial Services
      - Lending
      - Mortgage
      - Real Estate
    properties:
      - type: Portal
        url: https://mortgagetech.ice.com/products/developer-portal
      - type: Documentation
        url: https://mortgagetech.ice.com/products/developer-portal
common:
  - type: Portal
    url: https://developer.theice.com/hc/en-us
  - type: Website
    url: https://www.ice.com/
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
