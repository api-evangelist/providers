---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: API-Football provides comprehensive football data including leagues, fixtures, standings, events, line-ups, players, pre-match odds, live odds, and historical statistics for 1,200+ leagues and cups wo
  name: API-Football
  slug: api-football
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-football-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.api-football.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.api-football.com/documentation-v3
- group: commercial
  title: ''
  type: Pricing
  url: https://www.api-football.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.api-football.com/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.api-football.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.api-football.com/contact
created: '2025-03-01'
description: API-Football is a RESTful API providing comprehensive football (soccer) data covering 1,200+ leagues and cups worldwide. Operated by API-Sports, the platform delivers live scores, fixtures, standings, events, line-ups, player statistics, pre-match odds, and historical data. The API supports 9+ sports total including soccer, Formula 1, basketball, baseball, hockey, rugby, volleyball, and handball. Data is returned in JSON format and updates every 15 seconds during live matches.
features:
- description: Comprehensive coverage of over 1,200 football leagues and cups worldwide including major leagues, cups, and international competitions.
  name: 1200+ Leagues and Cups
- description: Real-time match data updated every 15 seconds during live matches, including scores, events, and match statistics.
  name: Live Scores
- description: Complete fixture schedules and match results including past, present, and upcoming matches with full event details.
  name: Fixtures and Results
- description: League standings and tables for all supported competitions with points, wins, draws, losses, and goal difference.
  name: Standings
- description: Individual player statistics including goals, assists, cards, appearances, and detailed performance metrics.
  name: Player Statistics
- description: Pre-match betting odds and live odds from major bookmakers available in all pricing tiers.
  name: Pre-Match and Live Odds
- description: Multiple years of historical match data available for statistical analysis, fantasy football, and predictive modeling.
  name: Historical Data
- description: Beyond football/soccer, API-Sports covers Formula 1, basketball, baseball, hockey, rugby, volleyball, and handball.
  name: Multi-Sport Coverage
finops:
- name: Api Football Finops
  service_category: API
  slug: api-football-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-football.png
integrations:
- description: API-Football is available on the RapidAPI hub enabling discovery and access through the RapidAPI marketplace.
  name: RapidAPI
- description: Subscriptions managed via Stripe or PayPal with no auto-renewal and prepaid plan options.
  name: Stripe and PayPal
layout: provider
modified: '2026-04-19'
name: API Football
nav: Providers
network: true
overview: 'API Football publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Football, Soccer, Live Scores, and Statistics.


  API Football''s developer surface includes documentation, pricing, signup flow, support, and 3 more developer resources.'
plans:
- name: Api Football Plans Pricing
  plan_count: 3
  slug: api-football-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Api Football Rate Limits
  slug: api-football-rate-limits
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Api Football Domain Security
  slug: api-football-domain-security
  summary_line: TLSv1.3 · DMARC
slug: api-football
tags:
- Sports
- Football
- Soccer
- Live Scores
- Statistics
use_cases:
- description: Build mobile and web apps displaying live scores, fixtures, standings, and player statistics for football fans.
  name: Sports Applications
- description: Power fantasy football platforms with player statistics, injury updates, match results, and historical performance data.
  name: Fantasy Football Platforms
- description: Integrate pre-match odds, live odds, and real-time match events into sports betting and prediction platforms.
  name: Sports Betting
- description: Analyze historical match data, player performance, and team statistics for sports analytics and scouting platforms.
  name: Sports Analytics
- description: Embed live score widgets and statistics panels into websites using API-Football's data and widget integrations.
  name: Widgets and Embeds
website: https://www.api-football.com/
---
