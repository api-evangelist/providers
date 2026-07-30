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
  name: Statorium Agentic Access
  operation_count: 22
  slug: statorium-agentic-access
  summary_line: 22 operations
api_count: 8
apis:
- description: Access NFL game data including live scores, results, and schedules.
  name: Statorium Games API
  slug: statorium-games-api
- description: Access basketball league listings and metadata.
  name: Statorium Leagues API
  slug: statorium-leagues-api
- description: Access match data including live scores, results, schedules, lineups, and head-to-head information.
  name: Statorium Matches API
  slug: statorium-matches-api
- description: Access daily news feeds for NFL players and teams.
  name: Statorium News API
  slug: statorium-news-api
- description: Access NFL player profiles, news, and statistics.
  name: Statorium Players API
  slug: statorium-players-api
- description: Retrieve season information, current and historical seasons for specific leagues.
  name: Statorium Seasons API
  slug: statorium-seasons-api
- description: Retrieve AFC and NFC standings.
  name: Statorium Standings API
  slug: statorium-standings-api
- description: Retrieve NFL team information, rosters, and statistics.
  name: Statorium Teams API
  slug: statorium-teams-api
artifact_total: 28
collections:
- collection_type: open
  name: Statorium American Football API
  slug: open-statorium-american-football-api
- collection_type: open
  name: Statorium Basketball API
  slug: open-statorium-basketball-api
- collection_type: open
  name: Statorium Football API
  slug: open-statorium-football-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/statorium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/statorium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/statorium-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statorium2
- group: company
  title: ''
  type: Website
  url: https://statorium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://statorium.com/stats-api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://statorium.com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statorium-match-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statorium-team-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/statorium-player-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/statorium-match-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/statorium-team-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/statorium-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/statorium-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/statorium-vocabulary.yml
created: '2025-03-01'
description: Statorium is a sports data API provider delivering live scores, statistics, schedules, standings, and news across 6+ sports including Soccer, American Football, Basketball, Hockey, Volleyball, and Handball. The API provides JSON-format responses covering over 200 football leagues, NBA, NFL, and other major competitions with full coverage of live data, historical data, player stats, team stats, lineups, and predictions.
examples:
- key_count: 2
  name: Statorium Get Match Example
  slug: statorium-get-match-example
- key_count: 2
  name: Statorium Get Standings Example
  slug: statorium-get-standings-example
- key_count: 2
  name: Statorium List Leagues Example
  slug: statorium-list-leagues-example
finops:
- name: Statorium Finops
  service_category: Sports Data
  slug: statorium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statorium.png
json_schemas:
- name: Statorium Match
  property_count: 12
  slug: statorium-match
- name: Statorium Player
  property_count: 10
  slug: statorium-player
- name: Statorium Team
  property_count: 10
  slug: statorium-team
json_structures:
- name: Statorium Match Structure
  property_count: 0
  slug: statorium-match-structure
- name: Statorium Team Structure
  property_count: 0
  slug: statorium-team-structure
jsonld:
- class_count: 37
  name: Statorium Context
  property_count: 0
  slug: statorium-context
layout: provider
modified: '2026-05-19'
name: Statorium
nav: Providers
network: true
overview: 'Statorium publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Games API, Leagues API, Matches API, and 5 more. Tagged areas include Sports, Sports Data, Football, Soccer, and Basketball.


  The Statorium catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Statorium''s developer surface includes authentication, documentation, pricing, and 12 more developer resources.'
plans:
- name: Statorium Plans Pricing
  plan_count: 1
  slug: statorium-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Statorium Rate Limits
  slug: statorium-rate-limits
rules:
- name: Statorium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: statorium-jsonschema-spectral-rules
- name: Statorium API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 4
  slug: statorium-rules
score:
  band: developing
  composite: 47.4
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 51.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/statorium/refs/heads/main/screenshots/statorium-2026-06-20T194526.png
security:
- kind: authentication
  name: Statorium Authentication
  slug: statorium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Statorium Domain Security
  slug: statorium-domain-security
  summary_line: TLSv1.3
slug: statorium
tags:
- Sports
- Sports Data
- Football
- Soccer
- Basketball
- American Football
- Live Scores
- Statistics
website: https://statorium.com/
---
