---
aid: thesports
name: TheSports
description: TheSports provides real-time sports data feeds, live trackers, and widgets covering football, basketball, tennis, esports, and other major sports worldwide. Their API delivers live scores, match statistics, player data, standings, and comprehensive sports analytics for media, broadcasters, OTT platforms, and developers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Football
  - Basketball
  - Tennis
  - Esports
  - Data
  - Real-Time
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/thesports/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thesports:football-api
    name: TheSports Football API
    description: Real-time football data feeds covering competitions, teams, players, matches, live scores, lineups, statistics, standings, and match analysis worldwide including major leagues and international tournaments.
    humanURL: https://www.thesports.com/
    baseURL: https://api.thesports.com/v1
    tags:
      - Football
      - Soccer
      - Sports
      - Real-Time
      - Data
    properties:
      - type: Documentation
        url: https://www.thesports.com/docs
      - type: Website
        url: https://www.thesports.com/
      - type: Pricing
        url: https://www.thesports.com/api
      - type: FreeTrial
        url: https://www.thesports.com/api
      - type: OpenAPI
        url: openapi/thesports-football-openapi.yml
      - type: JSONSchema
        url: json-schema/thesports-match-schema.json
      - type: JSONSchema
        url: json-schema/thesports-team-schema.json
    contact:
      - FN: TheSports API Support
        url: https://www.thesports.com/
  - aid: thesports:basketball-api
    name: TheSports Basketball API
    description: Real-time basketball data feeds including NBA, EuroLeague, and other major leagues. Covers teams, players, matches, live scores, box scores, and season statistics.
    humanURL: https://www.thesports.com/
    baseURL: https://api.thesports.com/v1
    tags:
      - Basketball
      - NBA
      - Sports
      - Real-Time
    properties:
      - type: Documentation
        url: https://www.thesports.com/docs
  - aid: thesports:tennis-api
    name: TheSports Tennis API
    description: Tennis data feeds covering ATP, WTA, and Grand Slam tournaments. Includes player profiles, match results, live scores, rankings, and tournament brackets.
    humanURL: https://www.thesports.com/
    baseURL: https://api.thesports.com/v1
    tags:
      - Tennis
      - ATP
      - WTA
      - Sports
    properties:
      - type: Documentation
        url: https://www.thesports.com/docs
  - aid: thesports:esports-api
    name: TheSports Esports API
    description: Esports data feeds for CS:GO, League of Legends, and other major titles. Covers teams, players, tournaments, matches, live scores, and statistics.
    humanURL: https://www.thesports.com/
    baseURL: https://api.thesports.com/v1
    tags:
      - Esports
      - CS:GO
      - League of Legends
      - Gaming
    properties:
      - type: Documentation
        url: https://www.thesports.com/docs
common:
  - type: Website
    url: https://www.thesports.com/
  - type: Documentation
    url: https://www.thesports.com/docs
  - type: SignUp
    url: https://www.thesports.com/register
  - type: Pricing
    url: https://www.thesports.com/api
  - type: FreeTrial
    url: https://www.thesports.com/api
  - type: Support
    url: https://www.thesports.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
