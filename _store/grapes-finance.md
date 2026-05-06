---
aid: grapes-finance
name: Grapes Finance
description: Grapes is an all-in-one embedded stablecoin onramp and offramp solution that simplifies and streamlines financial transactions. The API enables businesses and developers to integrate fiat-to-stablecoin and stablecoin-to-fiat transactions into their applications, services, and platforms, including buying and selling stablecoins such as QCAD and USDC with CAD and USD across Ethereum, Algorand, and Stellar networks.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Stablecoin
  - Onramp
  - Offramp
  - Fiat
  - Payments
  - Cryptocurrency
  - Embedded Finance
created: '2025-02-24'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/grapes-finance/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: grapes-finance:grapes-finance-core-api
    name: Grapes Finance Core API (Master Vintner)
    description: The Core API enables businesses to manage their own Grapes or non-custodial wallets across Ethereum, Algorand, and Stellar blockchains. Supports stablecoin swaps (USDC/QCAD), fiat onramps from Canadian banks, and third-party payouts.
    humanURL: https://docs.grapesfinance.com/api-user-guide/
    baseURL: https://api.demo.grapesfinance.com
    tags:
      - Stablecoin
      - Wallet
      - Onramp
      - Offramp
      - Payouts
    properties:
      - type: Documentation
        url: https://docs.grapesfinance.com/api-user-guide/
      - type: OpenAPI
        url: openapi/grapes-finance-openapi.yml
  - aid: grapes-finance:grapes-finance-organizations-api
    name: Grapes Finance Organizations API (Vineyard Manager)
    description: The Organizations API enables businesses to embed Grapes functionality without requiring direct client authentication, allowing management of client wallets and submission of transactions on their behalf.
    humanURL: https://docs.grapesfinance.com/api-user-guide/
    baseURL: https://api.demo.grapesfinance.com
    tags:
      - Embedded Finance
      - Organizations
      - Wallet Management
    properties:
      - type: Documentation
        url: https://docs.grapesfinance.com/api-user-guide/
      - type: OpenAPI
        url: openapi/grapes-finance-openapi.yml
common:
  - type: Documentation
    url: https://docs.grapesfinance.com/api-user-guide/
  - type: OpenAPI
    url: openapi/grapes-finance-openapi.yml
  - type: JSONSchema
    url: json-schema/grapes-finance-order-schema.json
  - type: JSONLDContext
    url: json-ld/grapes-finance-context.jsonld
  - type: Rules
    url: grapes-finance-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
