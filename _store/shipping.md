---
aid: shipping
name: Shipping.com
description: Shipping.com is a shipping intelligence and marketplace platform that provides inside information on the best deals across the shipping industry worldwide. The platform enables carriers, shippers, and third-party logistics companies (3PLs) to access reduced shipping rates, improve revenue opportunities, and optimize transportation supply chain operations. Shipping.com is headquartered in New York City and connects members of the transportation and logistics industry with competitive pricing and market intelligence across all major ocean freight trade lanes.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Shipping
  - Freight
  - Logistics
  - Transportation
  - Marketplace
  - Rate Intelligence
  - Ocean Freight
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/shipping/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: shipping:shipping-platform
    name: Shipping.com Rate Intelligence Platform
    description: Shipping.com provides a marketplace and intelligence platform for the ocean freight and logistics industry. The platform aggregates freight rates from major carriers and provides rate comparison, market analytics, and procurement tools. Carriers publish their rates on the platform while shippers and freight forwarders use it to find the best deals across major trade lanes. No public developer API is currently available; the platform is accessed via the web portal at shipping.com.
    humanURL: https://www.shipping.com/
    tags:
      - Shipping
      - Freight
      - Rate Intelligence
      - Marketplace
      - Ocean Freight
    properties:
      - type: Website
        url: https://www.shipping.com/
      - type: Documentation
        url: https://www.shipping.com/
  - aid: shipping:freightos-baltic-index
    name: Freightos Baltic Index (FBX)
    description: The Freightos Baltic Index is the global benchmark for container freight rates, providing weekly assessments of freight rates across major trade lanes. The FBX provides spot market freight rate data for routes including Trans-Pacific, Asia-Europe, and Transatlantic lanes. Used by Shipping.com and the broader industry for rate benchmarking.
    humanURL: https://fbx.freightos.com/
    tags:
      - Rate Index
      - Benchmarking
      - Ocean Freight
      - Market Data
    properties:
      - type: Documentation
        url: https://fbx.freightos.com/
      - type: Reference
        url: https://fbx.freightos.com/api
  - aid: shipping:world-bank-commodity-markets
    name: World Bank Commodity Markets Data
    description: The World Bank provides commodity price data including shipping-related indices such as the Baltic Dry Index (BDI) and fuel prices that affect freight rates. This data is used for freight market analysis and rate forecasting.
    humanURL: https://www.worldbank.org/en/research/commodity-markets
    tags:
      - Market Data
      - Commodity Prices
      - Economic Data
      - Open Data
    properties:
      - type: Documentation
        url: https://www.worldbank.org/en/research/commodity-markets
      - type: Reference
        url: https://api.worldbank.org/v2/
common:
  - type: Website
    url: https://www.shipping.com/
  - type: Blog
    url: https://www.shipping.com/blog/
  - type: LinkedIn
    url: https://www.linkedin.com/company/shipping-com/
  - type: JSONSchema
    url: json-schema/shipping-rate-schema.json
  - type: JSONStructure
    url: json-structure/shipping-rate-structure.json
  - type: JSONLDContext
    url: json-ld/shipping-context.jsonld
  - type: Examples
    url: examples/shipping-rate-example.json
  - type: Vocabulary
    url: vocabulary/shipping-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
