---
aid: api-sports
name: API-Sports
description: API-Sports is a leading provider of real-time sports data and statistics APIs for businesses and developers. They offer 35+ APIs covering football, basketball, baseball, tennis, rugby, volleyball, handball, ice hockey, MMA, and more, with live scores, fixtures, standings, player statistics, and historical data accessible via a unified API key authentication model.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Baseball
  - Basketball
  - Cricket
  - Football
  - Ice Hockey
  - MMA
  - Real-Time
  - Rugby
  - Sports Data
  - Statistics
  - Tennis
url: https://raw.githubusercontent.com/api-evangelist/api-sports/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-sports:api-football
    name: API-Football
    description: API-Football provides real-time and historical football (soccer) data including fixtures, live scores, standings, player statistics, team information, injuries, transfers, and predictions across 900+ leagues and cups worldwide.
    humanURL: https://api-sports.io/
    tags:
      - Football
      - Live Scores
      - Soccer
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://api-sports.io/documentation/football/v3
  - aid: api-sports:api-basketball
    name: API-Basketball
    description: API-Basketball provides real-time and historical basketball data including games, standings, player statistics, team information, and injuries across NBA, EuroLeague, and 400+ leagues worldwide.
    humanURL: https://api-sports.io/
    tags:
      - Basketball
      - NBA
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://api-sports.io/documentation/basketball/v1
  - aid: api-sports:api-baseball
    name: API-Baseball
    description: API-Baseball provides real-time and historical baseball data including games, standings, player statistics, and team information across MLB and international leagues.
    humanURL: https://api-sports.io/
    tags:
      - Baseball
      - MLB
      - Sports Data
      - Statistics
    properties:
      - type: Documentation
        url: https://api-sports.io/documentation/baseball/v1
  - aid: api-sports:api-tennis
    name: API-Tennis
    description: API-Tennis provides real-time tennis data including match results, rankings, player statistics, and tournament information across ATP, WTA, and ITF circuits.
    humanURL: https://api-sports.io/
    tags:
      - Sports Data
      - Statistics
      - Tennis
    properties:
      - type: Documentation
        url: https://api-sports.io/documentation/tennis/v1
common:
  - type: Website
    url: https://api-sports.io/
  - type: Documentation
    url: https://api-sports.io/documentation/
  - type: Pricing
    url: https://api-sports.io/#pricing
  - type: SignUp
    url: https://dashboard.api-sports.io/register
  - type: Login
    url: https://dashboard.api-sports.io/
  - type: Features
    data:
      - name: 35+ Sports APIs
        description: Comprehensive coverage spanning football, basketball, baseball, tennis, rugby, ice hockey, volleyball, handball, MMA, and more.
      - name: Real-Time Live Scores
        description: Live score updates, fixture statuses, and in-play event data across all supported sports.
      - name: Historical Data
        description: Access to historical match results, player statistics, and standings going back multiple seasons.
      - name: API Key Authentication
        description: Unified API key authentication model across all sports APIs with rate limiting by plan.
      - name: Fixtures and Schedules
        description: Upcoming and past fixtures with dates, venues, teams, and competition information.
      - name: Player and Team Statistics
        description: Comprehensive player and team performance statistics including goals, assists, ratings, and more.
      - name: RapidAPI Integration
        description: All APIs available through the RapidAPI marketplace for simplified subscription management.
  - type: UseCases
    data:
      - name: Sports Betting Platforms
        description: Integrate live scores, odds data, and historical statistics to power sports betting applications.
      - name: Fantasy Sports Apps
        description: Build fantasy sports platforms with real-time player statistics, injury data, and performance metrics.
      - name: Sports News Portals
        description: Automate sports content generation with live scores, match results, and team standings.
      - name: Sports Analytics
        description: Conduct in-depth sports analysis using historical data, player statistics, and match performance metrics.
      - name: Mobile Sports Apps
        description: Build mobile sports companion apps with live scores, notifications, and statistics dashboards.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
