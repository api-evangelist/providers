---
aid: lowes
name: Lowe's
description: Lowe's Companies, Inc. is an American retail company specializing in home improvement. Lowe's operates a developer portal built on Microsoft Azure API Management that provides partners and developers access to product, inventory, pricing, and store APIs for integration with Lowe's retail operations. Discover APIs, learn how to use them, try them out interactively, and sign up to acquire keys.
type: Index
position: Provider
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/lowes/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Ecommerce
  - Home Improvement
  - Products
  - Retail
apis:
  - aid: lowes:product-api
    name: Lowe's Product API
    description: The Lowe's Product API provides programmatic access to Lowe's product catalog, inventory, and pricing data. Built on Microsoft Azure API Management, the Lowe's developer portal allows partners and developers to discover APIs, learn how to use them, test them interactively, and obtain API keys. The platform supports integration with Lowe's home improvement retail operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://portal.apim.lowes.com/
    baseURL: https://apis.lowes.com
    tags:
      - Ecommerce
      - Home Improvement
      - Inventory
      - Products
      - Retail
      - Stores
    properties:
      - type: Documentation
        url: https://portal.apim.lowes.com/apis
      - type: OpenAPI
        url: openapi/lowes-product-api-openapi.yml
      - type: Sign Up
        url: https://portal.apim.lowes.com/signup
      - type: Login
        url: https://portal.apim.lowes.com/signin
common:
  - type: Portal
    url: https://portal.apim.lowes.com/
  - type: Website
    url: https://www.lowes.com/
  - type: Sign Up
    url: https://portal.apim.lowes.com/signup
  - type: Login
    url: https://portal.apim.lowes.com/signin
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
