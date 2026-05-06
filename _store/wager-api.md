---
aid: wager-api
name: Wager API
description: Wager API is a modern sports betting data platform that enables developers to build sports betting applications, bots, and predictive models with a single API. The platform provides real-time sports odds including spreads, moneylines, totals, player props, and futures markets across NFL, NCAA, NBA, MLB, NHL, soccer, tennis, and golf. Wager API also delivers player statistics, projections, fantasy data, injury reports, lineup updates, game schedules, and depth charts, making it a comprehensive data source for sports betting and fantasy sports applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports Betting
  - Sports Odds
  - Fantasy Sports
  - Sports Data
  - NFL
  - NBA
  - MLB
  - NHL
  - NCAA
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wager-api:wager-api-odds
    name: Wager API - Sports Odds
    description: Real-time sports odds for game spreads, moneylines, totals, alternate spreads, alternate totals, half-time odds, winning margins, and player props across major sports including NFL, NCAA, NBA, MLB, NHL, soccer, tennis, and golf. Supports thousands of futures markets including Super Bowl, NCAA Playoffs, NBA Finals, Stanley Cup, Premier League, and major tennis tournaments.
    humanURL: https://wagerapi.com/
    baseURL: https://api.wagerapi.com
    tags:
      - Sports Odds
      - Sports Betting
      - NFL
      - NBA
      - MLB
      - NHL
      - Soccer
      - Tennis
      - Golf
    properties:
      - type: Documentation
        url: https://wagerapi.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/openapi/wager-api-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/json-schema/wager-api-game-odds-schema.json
  - aid: wager-api:wager-api-fantasy
    name: Wager API - Fantasy Sports Data
    description: Fantasy sports data feed providing player statistics, projections, historical records, injury reports, lineup updates, game results and schedules, and depth charts. Used by fantasy sports applications, daily fantasy platforms, and sports analytics models to access comprehensive player and team data.
    humanURL: https://wagerapi.com/
    baseURL: https://api.wagerapi.com
    tags:
      - Fantasy Sports
      - Sports Data
      - Player Statistics
      - Injury Reports
    properties:
      - type: Documentation
        url: https://wagerapi.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/openapi/wager-api-openapi.yml
common:
  - type: Website
    url: https://wagerapi.com/
  - type: Contact
    url: https://wagerapi.com/#contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
