---
aid: wine-vybe
name: Wine Vybe
description: Wine Vybe is a wine, beer, and liquor database API platform that provides access to comprehensive beverage data including wine regions, grape varieties, tasting notes, food pairing recommendations, awards, producer information, brewery and distillery details, and custom taste profiles. The platform serves app developers and businesses through RESTful APIs hosted on RapidAPI.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Beverages
  - Beer
  - Database
  - Food Pairing
  - Liquor
  - Recommendations
  - Wine
url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wine-vybe:wine-vybe-api
    name: Wine Vybe Wine API
    description: The Wine Vybe Wine API provides access to thousands of wines with data including wine regions, grape varieties, tasting notes, food pairing recommendations, awards, producer details, and custom taste profiles. Available through RapidAPI with per-request pricing.
    humanURL: https://winevybe.com/wine-api/
    baseURL: https://winevybe.com
    tags:
      - Beverages
      - Database
      - Tasting Notes
      - Wine
    properties:
      - type: Documentation
        url: https://winevybe.com/wine-api/
      - type: Portal
        url: https://winevybe.com/apis/
      - type: RapidAPI
        url: https://rapidapi.com/user/winevybe
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-schema/wine-vybe-wine-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-structure/wine-vybe-wine-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/examples/wine-vybe-wine-example.json
  - aid: wine-vybe:wine-vybe-beer-api
    name: Wine Vybe Beer API
    description: The Wine Vybe Beer API provides access to brewery details, ABV data, beer descriptions, food pairing recommendations, awards, packaging specifications, and tasting profiles for thousands of popular beers. Available through RapidAPI starting at $0.02 per request.
    humanURL: https://winevybe.com/beer-api/
    baseURL: https://winevybe.com
    tags:
      - Beer
      - Beverages
      - Brewery
      - Database
    properties:
      - type: Documentation
        url: https://winevybe.com/beer-api/
      - type: Portal
        url: https://winevybe.com/apis/
      - type: RapidAPI
        url: https://rapidapi.com/winevybe/api/beer9
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-schema/wine-vybe-beer-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-structure/wine-vybe-beer-structure.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/examples/wine-vybe-beer-example.json
  - aid: wine-vybe:wine-vybe-liquor-api
    name: Wine Vybe Liquor API
    description: The Wine Vybe Liquor API provides access to spirits and liquor data including distillery information, tasting notes, food pairing, and product details for whisky, cognac, tequila, vodka, rum, gin, brandy, armagnac, and more. Available through RapidAPI.
    humanURL: https://winevybe.com/
    baseURL: https://winevybe.com
    tags:
      - Beverages
      - Database
      - Distillery
      - Liquor
      - Spirits
    properties:
      - type: Documentation
        url: https://winevybe.com/apis/
      - type: Portal
        url: https://winevybe.com/apis/
      - type: RapidAPI
        url: https://rapidapi.com/user/winevybe
common:
  - url: https://winevybe.com/
    name: Wine Vybe
    type: Website
    description: Main website for Wine Vybe beverage database platform.
  - url: https://winevybe.com/wine-api/
    name: Wine API Documentation
    type: Documentation
    description: Documentation for the Wine Vybe Wine API.
  - url: https://winevybe.com/beer-api/
    name: Beer API Documentation
    type: Documentation
    description: Documentation for the Wine Vybe Beer API.
  - url: https://winevybe.com/apis/
    name: Wine Vybe APIs Portal
    type: Portal
    description: Portal listing all available Wine Vybe APIs.
  - url: https://rapidapi.com/user/winevybe
    name: Wine Vybe on RapidAPI
    type: RapidAPI
    description: Wine Vybe API listings on the RapidAPI marketplace.
  - url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-ld/wine-vybe-context.jsonld
    name: Wine Vybe JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context for Wine Vybe beverage domain vocabulary.
  - url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/vocabulary/wine-vybe-vocabulary.yml
    name: Wine Vybe Vocabulary
    type: Vocabulary
    description: Domain vocabulary for the Wine Vybe beverage platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
