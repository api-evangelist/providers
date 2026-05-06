---
aid: whisky-hunter
name: Whisky Hunter
description: Whisky Hunter is a market research and data platform for whisky collectors, investors, traders, and enthusiasts that aggregates historical auction data from 28 online whisky auction sites into a single database. It tracks trading volumes, winning bids, lot counts, and per-distillery statistics. All trading volumes and winning bids are stated in GBP (£). The Whisky Hunter API provides free, public access to this auction data with no authentication required.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Whisky
  - Spirits
  - Auctions
  - Market Data
  - Collectors
  - Investors
url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: whisky-hunter:whisky-hunter
    name: Whisky Hunter API
    description: The Whisky Hunter API provides free, public access to historical whisky auction data aggregated from 28 online whisky auction platforms. Endpoints cover aggregated auction statistics, distillery listings, and per-distillery historical auction data. No authentication is required. All monetary values are in GBP (£). Only lots actually sold (meeting reserve price) are included in trading volume calculations.
    humanURL: https://whiskyhunter.net/api/
    baseURL: https://whiskyhunter.net/api
    tags:
      - Whisky
      - Auctions
      - Market Data
      - Distilleries
      - Price Tracking
      - Public API
    properties:
      - type: Documentation
        url: https://whiskyhunter.net/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/openapi/whisky-hunter-openapi.yml
      - type: AuctionsData
        url: https://whiskyhunter.net/api/auctions_data/?format=json
      - type: DistilleriesInfo
        url: https://whiskyhunter.net/api/distilleries_info/?format=json
common:
  - type: Website
    url: https://whiskyhunter.net
  - type: API
    url: https://whiskyhunter.net/api/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/openapi/whisky-hunter-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/vocabulary/whisky-hunter-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/json-ld/whisky-hunter-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/rules/whisky-hunter-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/whisky-hunter/refs/heads/main/capabilities/whisky-market-intelligence.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
