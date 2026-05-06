---
aid: wine-searcher
name: Wine-Searcher
description: Wine-Searcher is the world's leading wine search engine and marketplace, providing access to prices, availability, and data on over 15 million wines from retailers worldwide. The Wine-Searcher API allows developers to integrate wine pricing data, merchant listings, critic scores, vintage availability, and wine details directly into websites and applications. Typical API consumers include wine apps, websites, blogs, market research companies, wine investment platforms, and insurance services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data
  - Marketplace
  - Wine
  - Prices
  - Merchants
  - Vintages
  - Critics
created: '2025-02-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wine-searcher:wine-searcher-api
    name: Wine-Searcher API
    description: The Wine-Searcher API provides wine pricing data, aggregated critic scores, grape variety, region, and merchant listings for any wine in the Wine-Searcher database. The API uses HTTP GET requests with query parameters. Responses are available in JSON or XML format. Includes a Wine Check endpoint for aggregated wine data and a Market Price endpoint for individual merchant listings.
    humanURL: https://www.wine-searcher.com/trade/ws-api
    baseURL: https://www.wine-searcher.com/ws_api.php
    tags:
      - Wine
      - Prices
      - Data
      - Marketplace
    properties:
      - type: Documentation
        url: https://www.wine-searcher.com/trade/ws-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/openapi/wine-searcher-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/rules/wine-searcher-rules.yml
common:
  - type: Website
    url: https://www.wine-searcher.com
  - type: Documentation
    url: https://www.wine-searcher.com/trade/ws-api
  - type: DeveloperPortal
    url: https://www.wine-searcher.com/trade/developer
  - type: Pricing
    url: https://www.wine-searcher.com/trade/api
  - type: FAQ
    url: https://www.wine-searcher.com/trade/faq
  - type: DataFeed
    url: https://www.wine-searcher.com/trade/datafeed
  - type: Linking
    url: https://www.wine-searcher.com/trade/ws-link
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/json-ld/wine-searcher-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/vocabulary/wine-searcher-vocabulary.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/capabilities/wine-data.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
