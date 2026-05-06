---
aid: sportradar
name: Sportradar
description: Sportradar is the world's leading sports technology company, providing comprehensive sports data APIs delivering real-time scores, statistics, odds, and content for over 80 sports and 500 leagues worldwide. Their APIs serve media companies, sportsbooks, fantasy sports platforms, and sports technology companies with structured data covering NBA, NFL, MLB, NHL, soccer, tennis, golf, esports, and hundreds of other sports. Sportradar APIs use REST with API key authentication and deliver JSON and XML responses.
url: https://raw.githubusercontent.com/api-evangelist/sportradar/refs/heads/main/apis.yml
created: '2024-12-25'
modified: '2026-05-02'
specificationVersion: '0.19'
type: Index
tags:
  - Data
  - Esports
  - Fantasy Sports
  - Media
  - Real-Time
  - Sports
  - Sports Data
  - Statistics
apis:
  - aid: sportradar:sports-data-api
    name: Sportradar Sports Data API
    description: Comprehensive sports data API providing real-time scores, statistics, odds, and content covering 80+ sports, 500+ leagues, and 750,000+ annual events in JSON and XML formats. Supports live score feeds, historical statistics, player and team profiles, schedules, standings, and odds comparison across markets.
    humanURL: https://developer.sportradar.com/
    tags:
      - Data
      - Real-Time
      - Sports
      - Statistics
    properties:
      - type: Documentation
        url: https://developer.sportradar.com/docs/read/Home
      - type: Getting Started
        url: https://developer.sportradar.com/getting-started/docs/get-started
      - type: OpenAPI
        url: openapi/sportradar-sports-data-openapi.yml
  - aid: sportradar:nba-api
    name: Sportradar NBA API
    description: Provides comprehensive NBA data including real-time play-by-play, box scores, standings, team and player statistics, schedules, and injury reports. Covers both regular season and playoffs with live game feeds and historical data.
    humanURL: https://developer.sportradar.com/docs/read/basketball/NBA_v8
    tags:
      - Basketball
      - NBA
      - Real-Time
      - Sports
    properties:
      - type: Documentation
        url: https://developer.sportradar.com/docs/read/basketball/NBA_v8
  - aid: sportradar:nfl-api
    name: Sportradar NFL API
    description: Delivers detailed NFL data including game summaries, play-by-play, drive charts, team and player statistics, schedules, standings, and depth charts. Supports live feeds and historical season data.
    humanURL: https://developer.sportradar.com/docs/read/american_football/NFL_v7
    tags:
      - American Football
      - NFL
      - Real-Time
      - Sports
    properties:
      - type: Documentation
        url: https://developer.sportradar.com/docs/read/american_football/NFL_v7
  - aid: sportradar:soccer-api
    name: Sportradar Soccer API
    description: Covers 500+ soccer competitions globally, providing live match data, match timelines, team and player statistics, standings, tournament coverage, and detailed competition data for leagues like Premier League, La Liga, Bundesliga, Champions League, and more.
    humanURL: https://developer.sportradar.com/docs/read/soccer/Soccer_v4
    tags:
      - Real-Time
      - Soccer
      - Sports
      - Statistics
    properties:
      - type: Documentation
        url: https://developer.sportradar.com/docs/read/soccer/Soccer_v4
  - aid: sportradar:odds-api
    name: Sportradar Odds API
    description: Provides pre-match and live odds comparison data from major sportsbooks worldwide, including opening lines, closing lines, and line movement history for sports betting applications and analytics platforms.
    humanURL: https://developer.sportradar.com/docs/read/odds_comparison/Odds_Comparison_v2
    tags:
      - Betting
      - Odds
      - Sports
      - Sportsbook
    properties:
      - type: Documentation
        url: https://developer.sportradar.com/docs/read/odds_comparison/Odds_Comparison_v2
common:
  - type: Portal
    url: https://developer.sportradar.com/
  - type: Documentation
    url: https://developer.sportradar.com/docs/read/Home
  - type: Getting Started
    url: https://developer.sportradar.com/getting-started/docs/get-started
  - type: Website
    url: https://sportradar.com/
  - type: Blog
    url: https://sportradar.com/blog/
  - type: Pricing
    url: https://developer.sportradar.com/getting-started/docs/pricing
  - type: Status
    url: https://status.sportradar.com/
  - type: Support
    url: https://developer.sportradar.com/docs/read/Home#support
  - type: JSONSchema
    url: json-schema/sportradar-sport-event-schema.json
  - type: JSONSchema
    url: json-schema/sportradar-competitor-schema.json
  - type: JSONStructure
    url: json-structure/sportradar-sport-event-structure.json
  - type: JSON-LD
    url: json-ld/sportradar-context.jsonld
  - type: SpectralRules
    url: rules/sportradar-rules.yml
  - type: Vocabulary
    url: vocabulary/sportradar-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
