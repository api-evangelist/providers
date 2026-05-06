---
aid: stats-perform
name: Stats Perform
description: Stats Perform is the world's leading sports data and AI-powered sports intelligence company. The STATS API provides access to a vast collection of sports data through a unified REST API, including live sports data, cumulative season data, and historical data for leagues from around the world. Data covers American Football, Baseball, Basketball, Hockey, Soccer, Golf, Tennis, and more with in-depth player and team statistics, editorial coverage, live scores, standings, schedules, and play-by-play data.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Sports Data
  - Football
  - Baseball
  - Basketball
  - Hockey
  - Soccer
  - Golf
  - Tennis
  - Live Scores
  - Statistics
  - Sports Analytics
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/stats-perform/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: stats-perform:stats-api
    name: STATS API
    description: The STATS API from Stats Perform provides a comprehensive REST interface for accessing sports data including live scores, box scores, standings, schedules, player and team statistics, play-by-play data, editorial content, and historical records. The API supports sports including American Football (NFL, NCAAF), Baseball (MLB, MiLB), Basketball (NBA, NCAAB), Hockey (NHL), Soccer (MLS, EPL, Champions League), Golf (PGA), and Tennis (ATP, WTA). Authentication requires an API key and secret.
    humanURL: https://developer.stats.com/
    baseURL: https://api.stats.com/v1
    tags:
      - Sports Data
      - Live Scores
      - Statistics
      - Football
      - Baseball
      - Basketball
      - Hockey
      - Soccer
    properties:
      - type: Documentation
        url: https://developer.stats.com/docs/get_started
      - type: OpenAPI
        url: openapi/stats-perform-stats-api-openapi.yml
    contact:
      - FN: Stats Perform Support
        email: help@support.statsperform.com
        url: https://developer.stats.com/
common:
  - type: Website
    url: https://developer.stats.com/
  - type: Documentation
    url: https://developer.stats.com/docs/get_started
  - type: GettingStarted
    url: https://developer.stats.com/docs/get_started
  - type: Glossary
    url: https://developer.stats.com/docs/Glossary
  - type: InteractiveDocs
    url: https://developer.stats.com/io-docs
  - type: JSONSchema
    url: json-schema/stats-perform-event-schema.json
  - type: JSONSchema
    url: json-schema/stats-perform-team-schema.json
  - type: JSONStructure
    url: json-structure/stats-perform-event-structure.json
  - type: JSON-LD
    url: json-ld/stats-perform-context.jsonld
  - type: SpectralRules
    url: rules/stats-perform-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/sports-analytics.yaml
  - type: Vocabulary
    url: vocabulary/stats-perform-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
