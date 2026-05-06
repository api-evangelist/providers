---
aid: metals-dev
name: Metals.Dev
description: Metals.Dev provides a developer-friendly JSON API for spot prices of precious metals, industrial metals, and currency conversion rates. It offers real-time prices from leading authorities including LBMA, LME, MCX, and IBJA, plus 5+ years of historical data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Data
  - Gold
  - Precious Metals
  - Silver
  - Spot Prices
url: https://raw.githubusercontent.com/api-evangelist/metals-dev/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: metals-dev:metals-dev-api
    name: Metals.Dev API
    description: The Metals.Dev API provides a simple, developer-friendly JSON API for real-time spot prices of precious metals and industrial metals, including bid, ask, low, high, change, and conversion rates against 170+ currencies.
    humanURL: https://metals.dev/docs
    baseURL: https://api.metals.dev/v1
    tags:
      - Financial Data
      - Precious Metals
      - Spot Prices
    properties:
      - type: Documentation
        url: https://metals.dev/docs
      - type: Getting Started
        url: https://metals.dev/docs#getting-started
      - type: OpenAPI
        url: openapi/metals-dev-openapi.yml
common:
  - type: Portal
    url: https://metals.dev/
  - type: Pricing
    url: https://metals.dev/pricing
  - type: Status
    url: https://metals.dev/status
  - type: Sign Up
    url: https://metals.dev/sign-up
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
