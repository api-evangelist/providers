---
aid: citizens-financial
url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/apis.yml
apis:
- aid: citizens-financial:accounts-api
  name: Citizens Bank Accounts API
  tags:
  - Accounts
  - Banking
  - Open Banking
  - Transactions
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.citizensbank.com
  humanURL: https://developer.citizensbank.com/
  properties:
  - url: https://developer.citizensbank.com/
    type: Portal
  - url: https://developer.citizensbank.com/product/35/api/26
    type: Documentation
  - url: openapi/citizens-bank-accounts-api-openapi.yml
    type: OpenAPI
  description: The Citizens Bank Accounts API enables authenticated consumers to programmatically retrieve deposit account and transaction data for Citizens Bank customers. Designed exclusively for Savings and Checking accounts, it provides structured access to account metadata and detailed transaction histories through a RESTful interface.
- aid: citizens-financial:atm-locator-api
  name: Citizens Bank ATM Locator API
  tags:
  - ATMs
  - Banking
  - Geolocation
  - Locations
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.citizensbank.com
  humanURL: https://developer.citizensbank.com/
  properties:
  - url: https://developer.citizensbank.com/
    type: Documentation
  - url: openapi/citizens-bank-atm-locator-api-openapi.yml
    type: OpenAPI
  description: The Citizens Bank ATM Locator API enables users to locate all Citizens Bank ATMs throughout the USA. The API supports queries by zip code, street address, or latitude and longitude coordinates, returning ATM location details including hours of operation and whether the location is a standalone ATM or part of another entity.
- aid: citizens-financial:citizens-pay-api
  name: Citizens Pay API
  tags:
  - Financing
  - Lending
  - Payments
  - Point of Sale
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.citizenspay.com
  humanURL: https://developer-citizenspay.citizensbank.com/
  properties:
  - url: https://developer-citizenspay.citizensbank.com/
    type: Portal
  description: The Citizens Pay API enables merchants and partners to integrate Citizens Pay point-of-sale financing into their applications and checkout experiences. Citizens Pay provides consumer financing solutions that allow customers to pay over time for purchases through participating retailers.
name: Citizens Financial
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

