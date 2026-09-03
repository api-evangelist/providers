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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stats Perform Agentic Access
  operation_count: 12
  slug: stats-perform-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Retrieve editorial content including news articles, previews, and recaps associated with events, teams, and players.
  name: Stats Perform Editorial API
  slug: stats-perform-editorial-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Access event (game/match) data including live scores, box scores, play-by-play, and results across all supported sports.
  name: Stats Perform Events API
  slug: stats-perform-events-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Access player profiles, career statistics, and game-level performance data.
  name: Stats Perform Players API
  slug: stats-perform-players-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Access reference data including league definitions, network types, and decode tables for API response values.
  name: Stats Perform Reference Data API
  slug: stats-perform-reference-data-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Retrieve league and conference standings with win/loss records and tiebreaker data.
  name: Stats Perform Standings API
  slug: stats-perform-standings-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Access cumulative season statistics for teams and players across all supported sports.
  name: Stats Perform Statistics API
  slug: stats-perform-statistics-api
- baseURL: https://api.stats.com/v1
  baseurl_source: declared
  description: Retrieve team rosters, statistics, and metadata for all supported sports and leagues.
  name: Stats Perform Teams API
  slug: stats-perform-teams-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stats Perform STATS Editorial API
  slug: open-stats-perform-editorial-api
- collection_type: open
  name: Stats Perform STATS Editorial Events API
  slug: open-stats-perform-events-api
- collection_type: open
  name: Stats Perform STATS Editorial Players API
  slug: open-stats-perform-players-api
- collection_type: open
  name: Stats Perform STATS Editorial Reference Data API
  slug: open-stats-perform-reference-data-api
- collection_type: open
  name: Stats Perform STATS Editorial Standings API
  slug: open-stats-perform-standings-api
- collection_type: open
  name: Stats Perform STATS Editorial Statistics API
  slug: open-stats-perform-statistics-api
- collection_type: open
  name: Stats Perform STATS API
  slug: open-stats-perform-stats-api
- collection_type: open
  name: Stats Perform STATS Editorial Teams API
  slug: open-stats-perform-teams-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stats-perform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stats-perform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stats-perform-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/statsperform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stats-perform
- group: company
  title: ''
  type: Website
  url: https://developer.stats.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stats.com/docs/get_started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.stats.com/docs/get_started
- group: other
  title: ''
  type: Glossary
  url: https://developer.stats.com/docs/Glossary
- group: docs
  title: ''
  type: InteractiveDocs
  url: https://developer.stats.com/io-docs
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stats-perform-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stats-perform-team-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stats-perform-event-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/stats-perform-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/stats-perform-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stats-perform-vocabulary.yml
created: '2025-03-01'
description: Stats Perform is the world's leading sports data and AI-powered sports intelligence company. The STATS API provides access to a vast collection of sports data through a unified REST API, including live sports data, cumulative season data, and historical data for leagues from around the world. Data covers American Football, Baseball, Basketball, Hockey, Soccer, Golf, Tennis, and more with in-depth player and team statistics, editorial coverage, live scores, standings, schedules, and play-by-play data.
examples:
- key_count: 2
  name: Stats Perform Get Event Score Example
  slug: stats-perform-get-event-score-example
- key_count: 2
  name: Stats Perform List Teams Example
  slug: stats-perform-list-teams-example
finops:
- name: Stats Perform Finops
  service_category: API
  slug: stats-perform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stats-perform.png
json_schemas:
- name: Stats Perform Event
  property_count: 12
  slug: stats-perform-event
- name: Stats Perform Team
  property_count: 11
  slug: stats-perform-team
json_structures:
- name: Stats Perform Event Structure
  property_count: 0
  slug: stats-perform-event-structure
jsonld:
- class_count: 42
  name: Stats Perform Context
  property_count: 0
  slug: stats-perform-context
layout: provider
modified: '2026-05-19'
name: Stats Perform
nav: Providers
network: true
overview: 'Stats Perform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Editorial API, Events API, Players API, and 4 more. Tagged areas include Sports, Sports Data, Football, Baseball, and Basketball.


  The Stats Perform catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stats Perform''s developer surface includes authentication, documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Stats Perform Plans Pricing
  plan_count: 3
  slug: stats-perform-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Stats Perform Rate Limits
  slug: stats-perform-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stats Perform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stats-perform-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Stats Perform API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 3
  slug: stats-perform-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 60.5
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stats-perform/refs/heads/main/screenshots/stats-perform-2026-06-20T194526.png
security:
- kind: authentication
  name: Stats Perform Authentication
  slug: stats-perform-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stats Perform Domain Security
  slug: stats-perform-domain-security
  summary_line: TLSv1.3
slug: stats-perform
tags:
- Sports
- Sports Data
- Football
- Baseball
- Basketball
- Hockey
- Soccer
- Golf
- Tennis
- Live Scores
- Statistics
- Sports Analytics
website: https://developer.stats.com/
---
