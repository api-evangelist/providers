---
aid: zestful
name: Zestful
description: Zestful provides a machine-learning-powered ingredient parser API that turns plain recipe ingredient strings into structured JSON data. The API extracts quantity, unit, product name, preparation notes, and USDA FoodData Central database matches from free-form recipe text. Designed for recipe app developers building searchable recipes, shopping lists, and ingredient databases.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Food
  - Ingredients
  - Parsers
  - Recipes
  - USDA
created: '2024-11-14'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/zestful/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zestful:zestful
    name: Zestful Ingredient Parser API
    tags:
      - Food
      - Ingredients
      - Parsers
      - Recipes
      - USDA
    baseURL: https://zestfuldata.com
    humanURL: https://zestfuldata.com/docs/
    properties:
      - url: https://zestfuldata.com/docs/
        type: Documentation
      - url: https://zestfuldata.com/pricing/
        type: Pricing
      - url: openapi/zestful-openapi.yml
        type: OpenAPI
      - url: json-schema/zestful-ingredient-schema.json
        type: JSONSchema
      - url: json-schema/zestful-parse-response-schema.json
        type: JSONSchema
      - url: json-ld/zestful-context.jsonld
        type: JSONLD
      - url: rules/zestful-rules.yml
        type: SpectralRules
      - url: capabilities/recipe-data-enrichment.yaml
        type: NaftikoCapabilities
    description: 'The Zestful Ingredient Parser API uses machine learning to convert plain recipe ingredient strings into structured JSON data. It parses ingredient names, quantities, units, preparation notes, and matches each ingredient against the USDA FoodData Central database. Accepts up to 100 ingredients per request. Pricing: free tier (30 parses/day), professional ($0.02 per parse), and enterprise (flat fee, private server).'
common:
  - url: https://zestfuldata.com/
    name: Zestful Website
    type: Website
    description: Main Zestful website with API overview.
  - url: https://zestfuldata.com/docs/
    name: API Reference
    type: Documentation
    description: Full API documentation and reference.
  - url: https://zestfuldata.com/pricing/
    name: Pricing
    type: Pricing
    description: Pricing plans for the Zestful API.
  - url: https://rapidapi.com/zestfuldata/api/recipe-and-ingredient-analysis
    name: Zestful on RapidAPI
    type: Integrations
    description: Zestful API available on the RapidAPI marketplace.
  - url: https://github.com/mtlynch/zestful-client
    name: Zestful Client
    type: SDKs
    description: Official Zestful API client library on GitHub.
  - url: vocabulary/zestful-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Domain vocabulary for Zestful ingredient parsing concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
