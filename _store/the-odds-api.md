---
aid: the-odds-api
name: The Odds API
description: The Odds API provides sports betting odds from over 40 major bookmakers worldwide. Access current and historical odds for head-to-head, spreads, totals, and outrights markets across 100+ sports. Endpoints cover live scores, event listings, participants, and historical odds snapshots dating back to June 2020. Quota is consumed per request based on the number of regions and markets requested. All requests require an API key.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Betting
  - Odds
  - Sports
  - Scores
  - Historical Data
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/the-odds-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-odds-api:the-odds-api
    name: The Odds API
    description: 'Sports betting API providing current and historical odds from major bookmakers for 100+ sports. Access head-to-head, spreads, totals, and outrights markets. Also provides live scores, event listings, and participant data. Quota: 1 credit per region per market for current odds, 10 credits for historical odds.'
    humanURL: https://the-odds-api.com/
    baseURL: https://api.the-odds-api.com/v4
    tags:
      - Betting
      - Odds
      - Sports
      - Scores
      - Bookmakers
    properties:
      - type: Documentation
        url: https://the-odds-api.com/liveapi/guides/v4/
      - type: Getting Started
        url: https://the-odds-api.com/liveapi/guides/v4/
      - type: Sign Up
        url: https://the-odds-api.com/#get-access
      - type: OpenAPI
        url: openapi/the-odds-api-openapi.yml
common:
  - type: Website
    url: https://the-odds-api.com/
  - type: Documentation
    url: https://the-odds-api.com/liveapi/guides/v4/
  - type: Sign Up
    url: https://the-odds-api.com/#get-access
  - type: GitHub Organization
    url: https://github.com/the-odds-api
  - type: SpectralRuleset
    url: rules/the-odds-api-rules.yml
  - type: NaftikoCapability
    url: capabilities/sports-betting-intelligence.yaml
  - type: JSONSchema
    url: json-schema/the-odds-api-event-schema.json
  - type: JSONLDContext
    url: json-ld/the-odds-api-context.jsonld
  - type: Vocabulary
    url: vocabulary/the-odds-api-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
