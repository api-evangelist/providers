---
aid: dsg-sports-analytics
name: DSG Sports Analytics
description: DSG Sports Analytics, operated by Data Sports Group, is a sports data provider offering live scores, statistics, historical data, fixtures, player and team information, and odds across more than 80 sports including soccer, basketball, American football, cricket, tennis, ice hockey, e-sports, and Olympic disciplines. The DSG Sports Data API delivers this content in JSON and XML over HTTPS using credential-based authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analysis
  - Insights
  - Sports
  - Sports Data
  - Live Scores
  - Statistics
url: https://raw.githubusercontent.com/api-evangelist/dsg-sports-analytics/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
position: Consumer
access: 3rd-Party
apis:
  - aid: dsg-sports-analytics:sports-data-api
    name: DSG Sports Data API
    humanURL: https://datasportsgroup.com/products-api/
    baseURL: https://dsg-api.com
    tags:
      - Sports Data
      - Live Scores
      - Statistics
      - Fixtures
      - Odds
    properties:
      - type: Documentation
        url: https://datasportsgroup.com/products-api/
      - type: APIReference
        url: https://dsg-api.com/
      - type: Login
        url: https://dsg-api.com/login/
    description: The DSG Sports Data API exposes live scores, statistics, historical data, player and team information, fixtures, results, and odds across 80-plus sports through a per-sport documentation tree at dsg-api.com. Operations follow a get_* convention (for example get_areas, get_competitions, get_matches, get_tables, get_teams, get_peoples, get_news, get_odds) and responses are available in JSON and XML.
common:
  - type: Website
    url: https://datasportsgroup.com/
  - type: Products
    url: https://datasportsgroup.com/products-api/
  - type: Widgets
    url: https://datasportsgroup.com/sports-data-widgets-showcase/
  - type: PrivacyPolicy
    url: https://datasportsgroup.com/privacy-policy/
  - type: APIReference
    url: https://dsg-api.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
