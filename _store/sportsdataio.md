---
aid: sportsdataio
name: SportsDataIO
description: SportsDataIO is an award-winning sports data and content provider producing millions of data points across thousands of games annually. The platform offers robust REST APIs, responsive widgets, database downloads, and fantasy sports tools covering 14+ major sports including NFL, MLB, NBA, NHL, Soccer, Golf, NASCAR, MMA/UFC, Tennis, Formula 1, College Football, College Basketball, WNBA, and Olympics. Data includes live scores, statistics, odds feeds, fantasy projections, injuries, lineups, depth charts, standings, and player news.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports Data
  - Statistics
  - Live Scores
  - Fantasy Sports
  - Odds
  - NFL
  - NBA
  - MLB
  - NHL
  - Soccer
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sportsdataio:sportsdataio-nfl
    name: SportsDataIO NFL API
    description: Comprehensive NFL data API providing live scores, team statistics, player stats, fantasy projections, injuries, depth charts, standings, schedules, and betting odds. Covers all 32 teams and all NFL regular season, preseason, and playoff games with 136 endpoints for detailed analysis.
    humanURL: https://sportsdata.io/developers/api-documentation/nfl
    baseURL: https://api.sportsdata.io
    tags:
      - NFL
      - Football
      - Sports Data
      - Live Scores
      - Statistics
      - Fantasy Sports
    properties:
      - type: Documentation
        url: https://sportsdata.io/developers/api-documentation/nfl
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/openapi/sportsdataio-nfl-openapi.yml
  - aid: sportsdataio:sportsdataio-mlb
    name: SportsDataIO MLB API
    description: Complete MLB data API with live scores, box scores, player statistics, fantasy projections, injuries, lineups, standings, schedules, and odds for all Major League Baseball games. Includes Statcast data, pitch-by-pitch data, and real-time game events.
    humanURL: https://sportsdata.io/developers/api-documentation/mlb
    baseURL: https://api.sportsdata.io
    tags:
      - MLB
      - Baseball
      - Sports Data
      - Live Scores
      - Statistics
      - Fantasy Sports
    properties:
      - type: Documentation
        url: https://sportsdata.io/developers/api-documentation/mlb
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/openapi/sportsdataio-mlb-openapi.yml
  - aid: sportsdataio:sportsdataio-nba
    name: SportsDataIO NBA API
    description: NBA data API providing live scores, play-by-play, player statistics, fantasy projections, injuries, lineups, standings, and odds. Covers all NBA regular season, playoff, and in-season tournament games with real-time data feeds.
    humanURL: https://sportsdata.io/developers/api-documentation/nba
    baseURL: https://api.sportsdata.io
    tags:
      - NBA
      - Basketball
      - Sports Data
      - Live Scores
      - Statistics
      - Fantasy Sports
    properties:
      - type: Documentation
        url: https://sportsdata.io/developers/api-documentation/nba
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/openapi/sportsdataio-nba-openapi.yml
  - aid: sportsdataio:sportsdataio-nhl
    name: SportsDataIO NHL API
    description: NHL data API with live scores, play-by-play, goalie stats, skater statistics, fantasy projections, injuries, line combinations, standings, and odds for all NHL regular season and playoff games.
    humanURL: https://sportsdata.io/developers/api-documentation/nhl
    baseURL: https://api.sportsdata.io
    tags:
      - NHL
      - Hockey
      - Sports Data
      - Live Scores
      - Statistics
      - Fantasy Sports
    properties:
      - type: Documentation
        url: https://sportsdata.io/developers/api-documentation/nhl
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/openapi/sportsdataio-nhl-openapi.yml
  - aid: sportsdataio:sportsdataio-soccer
    name: SportsDataIO Soccer API
    description: Soccer data API providing live scores, player statistics, team standings, match schedules, lineups, and odds for major leagues including EPL, MLS, La Liga, Bundesliga, Serie A, Champions League, and more.
    humanURL: https://sportsdata.io/developers/api-documentation/soccer
    baseURL: https://api.sportsdata.io
    tags:
      - Soccer
      - Football
      - EPL
      - MLS
      - Champions League
      - Sports Data
      - Live Scores
    properties:
      - type: Documentation
        url: https://sportsdata.io/developers/api-documentation/soccer
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsdataio/refs/heads/main/openapi/sportsdataio-soccer-openapi.yml
common:
  - type: Website
    url: https://sportsdata.io/
  - type: Portal
    url: https://sportsdata.io/developers
  - type: Documentation
    url: https://sportsdata.io/developers
  - type: Pricing
    url: https://sportsdata.io/pricing
  - type: Login
    url: https://sportsdata.io/login
  - type: SignUp
    url: https://sportsdata.io/signup
  - type: Support
    url: https://support.sportsdata.io/
  - type: SDKs
    url: https://sportsdata.io/developers/integration-tools
  - type: OpenAPI
    url: https://sportsdata.io/developers/sports-data-open-api-swagger-files
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
