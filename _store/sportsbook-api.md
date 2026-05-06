---
aid: sportsbook-api
name: Sportsbook API
description: Sportsbook API provides real-time sports betting odds data from major US sportsbooks including FanDuel, DraftKings, BetMGM, Kalshi, theScore, Fanatics, BetRivers, Polymarket, Bovada, and BetOnline. The API aggregates spreads, moneylines, totals, halves, quarters, player props, and futures for NFL, NBA, MLB, NHL, NCAA football, NCAA basketball, and soccer leagues. Includes tools to identify positive expected value (+EV) bets, arbitrage opportunities, and middling situations. Odds update once per minute, with live odds available during games.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports Betting
  - Odds
  - Sports Data
  - Gambling
created: '2026-03-16'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sportsbook-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sportsbook-api:sportsbook-api
    name: Sportsbook API
    description: Real-time sports betting odds aggregator providing data from 10+ major US sportsbooks. Covers NFL, NBA, MLB, NHL, NCAA, and soccer with spread, moneyline, total, and prop markets. Features automated detection of arbitrage opportunities, positive EV bets, and middle opportunities. Hosted on RapidAPI with tiered pricing from free (50 req/day) to enterprise (50K req/day).
    humanURL: https://sportsbookapi.com/
    baseURL: https://api.sportsbookapi.com
    tags:
      - Sports Betting
      - Odds
      - NFL
      - NBA
      - MLB
      - NHL
      - Soccer
      - Arbitrage
      - Expected Value
    properties:
      - type: Documentation
        url: https://sportsbookapi.com/documentation/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sportsbook-api/refs/heads/main/openapi/sportsbook-api-openapi.yml
      - type: Pricing
        url: https://sportsbookapi.com/pricing/
common:
  - type: Website
    url: https://sportsbookapi.com/
  - type: Portal
    url: https://sportsbookapi.com/documentation/
  - type: Pricing
    url: https://sportsbookapi.com/pricing/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
