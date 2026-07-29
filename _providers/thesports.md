---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  name: Thesports Agentic Access
  operation_count: 13
  slug: thesports-agentic-access
  summary_line: 13 operations
api_count: 9
apis:
- description: Real-time basketball data feeds including NBA, EuroLeague, and other major leagues. Covers teams, players, matches, live scores, box scores, and season statistics.
  name: TheSports Basketball API
  slug: basketball-api
- description: Tennis data feeds covering ATP, WTA, and Grand Slam tournaments. Includes player profiles, match results, live scores, rankings, and tournament brackets.
  name: TheSports Tennis API
  slug: tennis-api
- description: Esports data feeds for CS:GO, League of Legends, and other major titles. Covers teams, players, tournaments, matches, live scores, and statistics.
  name: TheSports Esports API
  slug: esports-api
- description: Football competition and league data
  name: TheSports Competitions API
  slug: thesports-competitions-api
- description: Football match fixtures, results, and live data
  name: TheSports Matches API
  slug: thesports-matches-api
- description: Football player profiles and statistics
  name: TheSports Players API
  slug: thesports-players-api
- description: League tables and competition standings
  name: TheSports Standings API
  slug: thesports-standings-api
- description: Match and player statistics
  name: TheSports Statistics API
  slug: thesports-statistics-api
- description: Football team information and statistics
  name: TheSports Teams API
  slug: thesports-teams-api
artifact_total: 25
collections:
- collection_type: open
  name: TheSports Football API
  slug: open-thesports-football
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thesports-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thesports-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thesports-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thesportsapi
- group: company
  title: ''
  type: Website
  url: https://www.thesports.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thesports.com/docs
- group: start
  title: ''
  type: Signup
  url: https://www.thesports.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thesports.com/api
- group: start
  title: ''
  type: FreeTrial
  url: https://www.thesports.com/api
- group: operate
  title: ''
  type: Support
  url: https://www.thesports.com/
- group: company
  title: ''
  type: Blog
  url: https://www.thesports.com/newsroom
created: '2025-03-01'
description: TheSports provides real-time sports data feeds, live trackers, and widgets covering football, basketball, tennis, esports, and other major sports worldwide. Their API delivers live scores, match statistics, player data, standings, and comprehensive sports analytics for media, broadcasters, OTT platforms, and developers.
examples:
- key_count: 2
  name: Thesports Get Match Details Example
  slug: thesports-get-match-details-example
- key_count: 2
  name: Thesports Get Standings Example
  slug: thesports-get-standings-example
- key_count: 2
  name: Thesports List Competitions Example
  slug: thesports-list-competitions-example
finops:
- name: Thesports Finops
  service_category: Sports Data
  slug: thesports-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thesports.png
json_schemas:
- name: Match
  property_count: 12
  slug: thesports-match
- name: Team
  property_count: 8
  slug: thesports-team
json_structures:
- name: Thesports Match Structure
  property_count: 0
  slug: thesports-match-structure
jsonld:
- class_count: 27
  name: Thesports Context
  property_count: 0
  slug: thesports-context
layout: provider
modified: '2026-05-19'
name: TheSports
nav: Providers
network: true
overview: 'TheSports publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Competitions API, Matches API, Players API, and 3 more. Tagged areas include Sports, Football, Basketball, Tennis, and Esports.


  The TheSports catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TheSports'' developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 5 more developer resources.'
plans:
- name: Thesports Plans Pricing
  plan_count: 1
  slug: thesports-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Thesports Rate Limits
  slug: thesports-rate-limits
rules:
- name: TheSports API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thesports-jsonschema-spectral-rules
- name: TheSports API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: thesports-rules
score:
  band: developing
  composite: 48.7
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.7
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thesports/refs/heads/main/screenshots/thesports-2026-06-20T195259.png
security:
- kind: authentication
  name: Thesports Authentication
  slug: thesports-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Thesports Domain Security
  slug: thesports-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thesports
tags:
- Sports
- Football
- Basketball
- Tennis
- Esports
- Data
- Real-Time
website: https://www.thesports.com/
---
