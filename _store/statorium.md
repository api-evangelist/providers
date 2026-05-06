---
aid: statorium
name: Statorium
description: Statorium is a sports data API provider delivering live scores, statistics, schedules, standings, and news across 6+ sports including Soccer, American Football, Basketball, Hockey, Volleyball, and Handball. The API provides JSON-format responses covering over 200 football leagues, NBA, NFL, and other major competitions with full coverage of live data, historical data, player stats, team stats, lineups, and predictions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Sports Data
  - Football
  - Soccer
  - Basketball
  - American Football
  - Live Scores
  - Statistics
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/statorium/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: statorium:football-api
    name: Statorium Football API
    description: The Statorium Football API delivers comprehensive football/soccer data including live scores, match results, standings, fixtures, lineups, player and team statistics for over 200 football leagues worldwide including the English Premier League, Champions League, World Cup, and Major League Soccer. The API uses JSON format with token-based authentication and supports head-to-head data, translated names, and league logos.
    humanURL: https://statorium.com/football-api
    baseURL: https://api.statorium.com/api/v1
    tags:
      - Football
      - Soccer
      - Live Scores
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://statorium.com/stats-api-documentation
      - type: OpenAPI
        url: openapi/statorium-football-api-openapi.yml
    contact:
      - FN: Statorium Support
        url: https://statorium.com/
  - aid: statorium:basketball-api
    name: Statorium Basketball API
    description: The Statorium Basketball API provides live basketball data including NBA live scores, game results, standings, player statistics, and team information delivered in JSON format. The API covers major basketball leagues and competitions with real-time updates.
    humanURL: https://statorium.com/basketball-api
    baseURL: https://api.statorium.com/api/v1
    tags:
      - Basketball
      - NBA
      - Live Scores
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://statorium.com/stats-api-documentation
      - type: OpenAPI
        url: openapi/statorium-basketball-api-openapi.yml
    contact:
      - FN: Statorium Support
        url: https://statorium.com/
  - aid: statorium:american-football-api
    name: Statorium American Football API
    description: The Statorium American Football API provides NFL data including live game data, scores, schedules, player news, team statistics, and historical records. The API delivers unique daily news feeds linked to NFL players and teams in JSON format.
    humanURL: https://statorium.com/american-football-nfl-api
    baseURL: https://api.statorium.com/api/v1
    tags:
      - American Football
      - NFL
      - Live Scores
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://statorium.com/stats-api-documentation
      - type: OpenAPI
        url: openapi/statorium-american-football-api-openapi.yml
    contact:
      - FN: Statorium Support
        url: https://statorium.com/
common:
  - type: Website
    url: https://statorium.com/
  - type: Documentation
    url: https://statorium.com/stats-api-documentation
  - type: Pricing
    url: https://statorium.com/
  - type: JSONSchema
    url: json-schema/statorium-match-schema.json
  - type: JSONSchema
    url: json-schema/statorium-team-schema.json
  - type: JSONSchema
    url: json-schema/statorium-player-schema.json
  - type: JSONStructure
    url: json-structure/statorium-match-structure.json
  - type: JSONStructure
    url: json-structure/statorium-team-structure.json
  - type: JSON-LD
    url: json-ld/statorium-context.jsonld
  - type: SpectralRules
    url: rules/statorium-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/sports-data.yaml
  - type: Vocabulary
    url: vocabulary/statorium-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
