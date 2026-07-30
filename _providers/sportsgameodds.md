---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  name: Sportsgameodds Agentic Access
  operation_count: 11
  slug: sportsgameodds-agentic-access
  summary_line: 11 operations
api_count: 8
apis:
- description: The Account API from SportsGameOdds — 1 operation(s) for account.
  name: SportsGameOdds Account API
  slug: sportsgameodds-account-api
- description: The Events API from SportsGameOdds — 2 operation(s) for events.
  name: SportsGameOdds Events API
  slug: sportsgameodds-events-api
- description: The Leagues API from SportsGameOdds — 1 operation(s) for leagues.
  name: SportsGameOdds Leagues API
  slug: sportsgameodds-leagues-api
- description: The Markets API from SportsGameOdds — 1 operation(s) for markets.
  name: SportsGameOdds Markets API
  slug: sportsgameodds-markets-api
- description: The Players API from SportsGameOdds — 2 operation(s) for players.
  name: SportsGameOdds Players API
  slug: sportsgameodds-players-api
- description: The Sports API from SportsGameOdds — 1 operation(s) for sports.
  name: SportsGameOdds Sports API
  slug: sportsgameodds-sports-api
- description: The Stats API from SportsGameOdds — 1 operation(s) for stats.
  name: SportsGameOdds Stats API
  slug: sportsgameodds-stats-api
- description: The Teams API from SportsGameOdds — 2 operation(s) for teams.
  name: SportsGameOdds Teams API
  slug: sportsgameodds-teams-api
artifact_total: 23
collections:
- collection_type: open
  name: SportsGameOdds API
  slug: open-sportsgameodds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportsgameodds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportsgameodds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportsgameodds-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sportsgameodds.com/
- group: start
  title: ''
  type: Portal
  url: https://sportsgameodds.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sportsgameodds.com/docs/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://sportsgameodds.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SportsGameOdds
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-ruby
- group: agent
  title: ''
  type: LlmsText
  url: https://sportsgameodds.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://sportsgameodds.com/blog
created: '2025-02-08'
description: SportsGameOdds API provides real-time sports betting odds data from 80+ sportsbooks across 50+ leagues. The API delivers live and pre-match odds across 3,000+ markets including moneylines, spreads, over/unders, team props, and player props for NFL, NBA, MLB, NHL, NCAAF, NCAAB, EPL, UCL, UFC, PGA, ATP and more. Features include consensus odds calculations, streaming for live data, an interactive data explorer, and official SDKs for JavaScript/TypeScript and Python.
examples:
- key_count: 4
  name: Sportsgameodds List Events Example
  slug: sportsgameodds-list-events-example
- key_count: 4
  name: Sportsgameodds List Markets Example
  slug: sportsgameodds-list-markets-example
finops:
- name: Sportsgameodds Finops
  service_category: API
  slug: sportsgameodds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportsgameodds.png
json_schemas:
- name: SportsGameOdds Event
  property_count: 8
  slug: sportsgameodds-event
- name: SportsGameOdds Market
  property_count: 7
  slug: sportsgameodds-market
json_structures:
- name: Sportsgameodds Event Structure
  property_count: 0
  slug: sportsgameodds-event-structure
jsonld:
- class_count: 36
  name: Sportsgameodds Context
  property_count: 5
  slug: sportsgameodds-context
layout: provider
modified: '2026-05-19'
name: SportsGameOdds
nav: Providers
network: true
overview: 'SportsGameOdds publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Events API, Leagues API, and 5 more. Tagged areas include Sports Betting, Odds, Sports Data, Fantasy Sports, and Gambling.


  The SportsGameOdds catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SportsGameOdds'' developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Sportsgameodds Plans Pricing
  plan_count: 3
  slug: sportsgameodds-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Sportsgameodds Rate Limits
  slug: sportsgameodds-rate-limits
rules:
- name: SportsGameOdds API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sportsgameodds-jsonschema-spectral-rules
- name: SportsGameOdds API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: sportsgameodds-rules
score:
  band: developing
  composite: 55.1
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.9
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportsgameodds/refs/heads/main/screenshots/sportsgameodds-2026-06-20T194349.png
security:
- kind: authentication
  name: Sportsgameodds Authentication
  slug: sportsgameodds-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sportsgameodds Domain Security
  slug: sportsgameodds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportsgameodds
tags:
- Sports Betting
- Odds
- Sports Data
- Fantasy Sports
- Gambling
website: https://sportsgameodds.com/
---
