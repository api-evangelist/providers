---
aid: api-football
name: API Football
description: API-Football is a RESTful API providing comprehensive football (soccer) data covering 1,200+ leagues and cups worldwide. Operated by API-Sports, the platform delivers live scores, fixtures, standings, events, line-ups, player statistics, pre-match odds, and historical data. The API supports 9+ sports total including soccer, Formula 1, basketball, baseball, hockey, rugby, volleyball, and handball. Data is returned in JSON format and updates every 15 seconds during live matches.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sports
  - Football
  - Soccer
  - Live Scores
  - Statistics
url: https://raw.githubusercontent.com/api-evangelist/api-football/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-football:api-football
    name: API-Football
    description: API-Football provides comprehensive football data including leagues, fixtures, standings, events, line-ups, players, pre-match odds, live odds, and historical statistics for 1,200+ leagues and cups worldwide.
    humanURL: https://www.api-football.com/
    tags:
      - Sports
      - Football
      - Soccer
      - Live Scores
    properties:
      - type: Documentation
        url: https://www.api-football.com/documentation-v3
      - type: GettingStarted
        url: https://www.api-football.com/documentation-v3#section/Introduction
      - type: Pricing
        url: https://www.api-football.com/pricing
      - type: Authentication
        url: https://www.api-football.com/documentation-v3#section/Authentication
      - type: RateLimits
        url: https://www.api-football.com/documentation-v3#section/Rate-limit
common:
  - type: Website
    url: https://www.api-football.com/
  - type: Documentation
    url: https://www.api-football.com/documentation-v3
  - type: Pricing
    url: https://www.api-football.com/pricing
  - type: SignUp
    url: https://dashboard.api-football.com/register
  - type: Login
    url: https://dashboard.api-football.com/login
  - type: Support
    url: https://www.api-football.com/contact
  - type: Features
    data:
      - name: 1200+ Leagues and Cups
        description: Comprehensive coverage of over 1,200 football leagues and cups worldwide including major leagues, cups, and international competitions.
      - name: Live Scores
        description: Real-time match data updated every 15 seconds during live matches, including scores, events, and match statistics.
      - name: Fixtures and Results
        description: Complete fixture schedules and match results including past, present, and upcoming matches with full event details.
      - name: Standings
        description: League standings and tables for all supported competitions with points, wins, draws, losses, and goal difference.
      - name: Player Statistics
        description: Individual player statistics including goals, assists, cards, appearances, and detailed performance metrics.
      - name: Pre-Match and Live Odds
        description: Pre-match betting odds and live odds from major bookmakers available in all pricing tiers.
      - name: Historical Data
        description: Multiple years of historical match data available for statistical analysis, fantasy football, and predictive modeling.
      - name: Multi-Sport Coverage
        description: Beyond football/soccer, API-Sports covers Formula 1, basketball, baseball, hockey, rugby, volleyball, and handball.
  - type: UseCases
    data:
      - name: Sports Applications
        description: Build mobile and web apps displaying live scores, fixtures, standings, and player statistics for football fans.
      - name: Fantasy Football Platforms
        description: Power fantasy football platforms with player statistics, injury updates, match results, and historical performance data.
      - name: Sports Betting
        description: Integrate pre-match odds, live odds, and real-time match events into sports betting and prediction platforms.
      - name: Sports Analytics
        description: Analyze historical match data, player performance, and team statistics for sports analytics and scouting platforms.
      - name: Widgets and Embeds
        description: Embed live score widgets and statistics panels into websites using API-Football's data and widget integrations.
  - type: Integrations
    data:
      - name: RapidAPI
        description: API-Football is available on the RapidAPI hub enabling discovery and access through the RapidAPI marketplace.
      - name: Stripe and PayPal
        description: Subscriptions managed via Stripe or PayPal with no auto-renewal and prepaid plan options.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
