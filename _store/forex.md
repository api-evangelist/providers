---
aid: forex
name: Forex
description: A collection of foreign exchange and currency conversion APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Currency
  - Exchange Rates
  - Financial Data
  - Forex
  - Trading
apis:
  - aid: forex:open-exchange-rates
    name: Open Exchange Rates API
    description: Real-time and historical exchange rates with simple JSON API.
    humanURL: https://openexchangerates.org
    baseURL: https://openexchangerates.org/api
    tags:
      - Currency Conversion
      - Exchange Rates
      - Historical Data
    properties:
      - type: Documentation
        url: https://docs.openexchangerates.org
      - type: Pricing
        url: https://openexchangerates.org/signup
      - type: Authentication
        url: https://docs.openexchangerates.org/authentication
  - aid: forex:fixer
    name: Fixer.io API
    description: Foreign exchange rates and currency conversion API.
    humanURL: https://fixer.io
    baseURL: https://api.fixer.io
    tags:
      - Currency
      - Exchange Rates
    properties:
      - type: Documentation
        url: https://fixer.io/documentation
      - type: Pricing
        url: https://fixer.io/product
  - aid: forex:exchangerate-api
    name: ExchangeRate-API
    description: Free currency conversion API with 161 currencies.
    humanURL: https://www.exchangerate-api.com
    baseURL: https://v6.exchangerate-api.com/v6
    tags:
      - Currency Conversion
      - Exchange Rates
    properties:
      - type: Documentation
        url: https://www.exchangerate-api.com/docs
      - type: Pricing
        url: https://www.exchangerate-api.com/pricing
      - type: Terms of Service
        url: https://www.exchangerate-api.com/terms
  - aid: forex:currencyapi
    name: CurrencyAPI
    description: Accurate and reliable foreign exchange rates API.
    humanURL: https://currencyapi.com
    baseURL: https://api.currencyapi.com/v3
    tags:
      - Forex
      - Historical Data
      - Real-Time Rates
    properties:
      - type: Documentation
        url: https://currencyapi.com/docs
      - type: Pricing
        url: https://currencyapi.com/pricing
      - type: Status
        url: https://status.currencyapi.com
  - aid: forex:frankfurter
    name: Frankfurter API
    description: Free and open-source API for current and historical forex rates.
    humanURL: https://www.frankfurter.app
    baseURL: https://api.frankfurter.app
    tags:
      - Exchange Rates
      - Free
      - Open Source
    properties:
      - type: Documentation
        url: https://www.frankfurter.app/docs
      - type: GitHub Organization
        url: https://github.com/hakanensari/frankfurter
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
