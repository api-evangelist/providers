---
aid: citizens-financial
name: Citizens Financial
url: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Accounts
  - ATMs
  - Banking
  - Open Banking
  - Payments
  - Point of Sale
  - Transactions
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations. Citizens exposes its programmable surface through the Citizens developer portal at developer.citizensbank.com, with REST APIs for deposit account and transaction data, ATM location services, and point-of-sale consumer financing through Citizens Pay. Authentication is OAuth 2.0 and the portal provides both sandbox and production environments.
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
common:
  - type: Website
    url: https://www.citizensbank.com/
  - type: Portal
    url: https://developer.citizensbank.com/
  - type: Sandbox
    url: https://sandboxdeveloper.citizensbank.com/api
  - type: Support
    url: https://developer.citizensbank.com/support
  - type: Privacy Policy
    url: https://www.citizensbank.com/privacy
  - type: JSON-LD
    url: json-ld/citizens-financial-context.jsonld
  - type: Spectral
    url: rules/citizens-financial-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/citizens-financial-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
