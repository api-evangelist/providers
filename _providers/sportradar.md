---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sportradar Agentic Access
  operation_count: 25
  slug: sportradar-agentic-access
  summary_line: 25 operations
api_count: 14
apis:
- description: Provides comprehensive NBA data including real-time play-by-play, box scores, standings, team and player statistics, schedules, and injury reports. Covers both regular season and playoffs with live ga
  name: Sportradar NBA API
  slug: nba-api
- description: Delivers detailed NFL data including game summaries, play-by-play, drive charts, team and player statistics, schedules, standings, and depth charts. Supports live feeds and historical season data.
  name: Sportradar NFL API
  slug: nfl-api
- description: Covers 500+ soccer competitions globally, providing live match data, match timelines, team and player statistics, standings, tournament coverage, and detailed competition data for leagues like Premier
  name: Sportradar Soccer API
  slug: soccer-api
- description: Provides pre-match and live odds comparison data from major sportsbooks worldwide, including opening lines, closing lines, and line movement history for sports betting applications and analytics platf
  name: Sportradar Odds API
  slug: odds-api
- description: Team and player profiles, rosters, and biographical information.
  name: Sportradar Competitors API
  slug: sportradar-competitors-api
- description: NBA Push Feeds deliver real-time play-by-play events, statistics, clock updates, and draft activity over HTTP chunked streaming.
  name: Sportradar NBA Push API
  slug: sportradar-nba-push-api
- description: NFL Push Feeds deliver real-time game events, statistics, pulse messages, and draft activity over HTTP chunked streaming.
  name: Sportradar NFL Push API
  slug: sportradar-nfl-push-api
- description: NHL Push Feeds deliver real-time game events, statistics, and enriched clock data over HTTP chunked streaming.
  name: Sportradar NHL Push API
  slug: sportradar-nhl-push-api
- description: Retrieve daily, weekly, and seasonal schedules for sports competitions.
  name: Sportradar Schedules API
  slug: sportradar-schedules-api
- description: Access live and historical game scores and match results.
  name: Sportradar Scores API
  slug: sportradar-scores-api
- description: Soccer Push Feeds deliver real-time match events and statistics over HTTP chunked streaming for 500+ competitions worldwide.
  name: Sportradar Soccer Push API
  slug: sportradar-soccer-push-api
- description: League and tournament standings, rankings, and tables.
  name: Sportradar Standings API
  slug: sportradar-standings-api
- description: Team and player performance statistics across competitions and seasons.
  name: Sportradar Statistics API
  slug: sportradar-statistics-api
- description: WNBA Push Feeds deliver real-time game events, statistics, and clock updates over HTTP chunked streaming.
  name: Sportradar WNBA Push API
  slug: sportradar-wnba-push-api
artifact_total: 47
collections:
- collection_type: open
  name: Sportradar Push Feeds API
  slug: open-sportradar-push-feeds
- collection_type: open
  name: Sportradar Sports Data API
  slug: open-sportradar-sports-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportradar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportradar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportradar-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sportradar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sportradar
- group: start
  title: ''
  type: Portal
  url: https://developer.sportradar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sportradar.com/docs/read/Home
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sportradar.com/getting-started/docs/get-started
- group: company
  title: ''
  type: Website
  url: https://sportradar.com/
- group: company
  title: ''
  type: Blog
  url: https://sportradar.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.sportradar.com/getting-started/docs/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sportradar.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.sportradar.com/docs/read/Home#support
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportradar-sport-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportradar-competitor-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sportradar-sport-event-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sportradar-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/sportradar-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sportradar-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.sportradar.com/llms.txt
created: '2024-12-25'
description: Sportradar is the world's leading sports technology company, providing comprehensive sports data APIs delivering real-time scores, statistics, odds, and content for over 80 sports and 500 leagues worldwide. Their APIs serve media companies, sportsbooks, fantasy sports platforms, and sports technology companies with structured data covering NBA, NFL, MLB, NHL, soccer, tennis, golf, esports, and hundreds of other sports. Sportradar APIs use REST with API key authentication and deliver JSON and XML responses.
examples:
- key_count: 2
  name: Sportradar Get Nba Daily Schedule Example
  slug: sportradar-get-nba-daily-schedule-example
- key_count: 2
  name: Sportradar Get Nba Game Summary Example
  slug: sportradar-get-nba-game-summary-example
- key_count: 2
  name: Sportradar Get Soccer Match Summary Example
  slug: sportradar-get-soccer-match-summary-example
finops:
- name: Sportradar Finops
  service_category: Sports Data Licensing
  slug: sportradar-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Sportradar Sports Data API. Sportradar is the world's leading sports technology company, providing comprehensive sports data APIs delivering
  name: Sportradar GraphQL Schema
  slug: sportradar-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportradar.png
json_schemas:
- name: Competition
  property_count: 3
  slug: sportradar-competition
- name: Sportradar Competitor
  property_count: 11
  slug: sportradar-competitor
- name: ConferenceStandings
  property_count: 3
  slug: sportradar-conferencestandings
- name: DailySchedule
  property_count: 2
  slug: sportradar-dailyschedule
- name: GameSummary
  property_count: 6
  slug: sportradar-gamesummary
- name: PlayerProfile
  property_count: 8
  slug: sportradar-playerprofile
- name: ScheduledGame
  property_count: 6
  slug: sportradar-scheduledgame
- name: Sportradar Sport Event
  property_count: 10
  slug: sportradar-sport-event
- name: SportEvent
  property_count: 4
  slug: sportradar-sportevent
- name: SportEventStatus
  property_count: 4
  slug: sportradar-sporteventstatus
- name: SportEventSummary
  property_count: 2
  slug: sportradar-sporteventsummary
- name: Standings
  property_count: 2
  slug: sportradar-standings
- name: TeamRef
  property_count: 3
  slug: sportradar-teamref
- name: TeamScore
  property_count: 4
  slug: sportradar-teamscore
- name: TeamStanding
  property_count: 6
  slug: sportradar-teamstanding
- name: Venue
  property_count: 5
  slug: sportradar-venue
json_structures:
- name: Sportradar Sport Event Structure
  property_count: 0
  slug: sportradar-sport-event-structure
- name: Sportradar Structure
  property_count: 0
  slug: sportradar-structure
jsonld:
- class_count: 42
  name: Sportradar Context
  property_count: 3
  slug: sportradar-context
layout: provider
modified: '2026-05-29'
name: Sportradar
nav: Providers
network: true
overview: 'Sportradar publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Competitors API, NBA Push API, NFL Push API, and 7 more. Tagged areas include Data, Esports, Fantasy Sports, HTTP Chunked, and Media.


  The Sportradar catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sportradar''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Sportradar Plans Pricing
  plan_count: 1
  slug: sportradar-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Sportradar Rate Limits
  slug: sportradar-rate-limits
rules:
- name: Sportradar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: sportradar-jsonschema-spectral-rules
- name: Sportradar API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 5
  slug: sportradar-rules
score:
  band: developing
  composite: 55.5
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportradar/refs/heads/main/screenshots/sportradar-2026-06-20T194345.png
security:
- kind: authentication
  name: Sportradar Authentication
  slug: sportradar-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sportradar Domain Security
  slug: sportradar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportradar
tags:
- Data
- Esports
- Fantasy Sports
- HTTP Chunked
- Media
- Push
- Real-Time
- Sports
- Sports Data
- Statistics
- Streaming
website: https://sportradar.com/
---
