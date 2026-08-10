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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: 'API-Football provides real-time and historical football (soccer) data including fixtures, live scores, standings, player statistics, team information, injuries, transfers, and predictions across 900+ '
  name: API-Football
  slug: api-football
- description: API-Basketball provides real-time and historical basketball data including games, standings, player statistics, team information, and injuries across NBA, EuroLeague, and 400+ leagues worldwide.
  name: API-Basketball
  slug: api-basketball
- description: API-Baseball provides real-time and historical baseball data including games, standings, player statistics, and team information across MLB and international leagues.
  name: API-Baseball
  slug: api-baseball
- description: API-Tennis provides real-time tennis data including match results, rankings, player statistics, and tournament information across ATP, WTA, and ITF circuits.
  name: API-Tennis
  slug: api-tennis
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-sports-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-sports
- group: company
  title: ''
  type: Website
  url: https://api-sports.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api-sports.io/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://api-sports.io/#pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.api-sports.io/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.api-sports.io/
created: '2025-03-01'
description: API-Sports is a leading provider of real-time sports data and statistics APIs for businesses and developers. They offer 35+ APIs covering football, basketball, baseball, tennis, rugby, volleyball, handball, ice hockey, MMA, and more, with live scores, fixtures, standings, player statistics, and historical data accessible via a unified API key authentication model.
features:
- description: Comprehensive coverage spanning football, basketball, baseball, tennis, rugby, ice hockey, volleyball, handball, MMA, and more.
  name: 35+ Sports APIs
- description: Live score updates, fixture statuses, and in-play event data across all supported sports.
  name: Real-Time Live Scores
- description: Access to historical match results, player statistics, and standings going back multiple seasons.
  name: Historical Data
- description: Unified API key authentication model across all sports APIs with rate limiting by plan.
  name: API Key Authentication
- description: Upcoming and past fixtures with dates, venues, teams, and competition information.
  name: Fixtures and Schedules
- description: Comprehensive player and team performance statistics including goals, assists, ratings, and more.
  name: Player and Team Statistics
- description: All APIs available through the RapidAPI marketplace for simplified subscription management.
  name: RapidAPI Integration
finops:
- name: Api Sports Finops
  service_category: API
  slug: api-sports-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-sports.png
layout: provider
modified: '2026-04-19'
name: API-Sports
nav: Providers
network: true
overview: 'API-Sports publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Baseball, Basketball, Cricket, Football, and Ice Hockey.


  API-Sports'' developer surface includes documentation, pricing, signup flow, and 4 more developer resources.'
plans:
- name: Api Sports Plans Pricing
  plan_count: 3
  slug: api-sports-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: Api Sports Rate Limits
  slug: api-sports-rate-limits
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Api Sports Domain Security
  slug: api-sports-domain-security
  summary_line: TLSv1.3 · DMARC
slug: api-sports
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
use_cases:
- description: Integrate live scores, odds data, and historical statistics to power sports betting applications.
  name: Sports Betting Platforms
- description: Build fantasy sports platforms with real-time player statistics, injury data, and performance metrics.
  name: Fantasy Sports Apps
- description: Automate sports content generation with live scores, match results, and team standings.
  name: Sports News Portals
- description: Conduct in-depth sports analysis using historical data, player statistics, and match performance metrics.
  name: Sports Analytics
- description: Build mobile sports companion apps with live scores, notifications, and statistics dashboards.
  name: Mobile Sports Apps
website: https://api-sports.io/
---
