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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wager Api Agentic Access
  operation_count: 9
  slug: wager-api-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: Season and championship futures markets
  name: Wager API Futures API
  slug: wager-api-futures-api
- description: Game schedules, results, and team information
  name: Wager API Games API
  slug: wager-api-games-api
- description: Real-time game odds including spreads, moneylines, and totals
  name: Wager API Odds API
  slug: wager-api-odds-api
- description: Player statistics, projections, and injury information
  name: Wager API Players API
  slug: wager-api-players-api
- description: Player proposition odds
  name: Wager API Props API
  slug: wager-api-props-api
artifact_total: 19
collections:
- collection_type: open
  name: Wager API
  slug: open-wager-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wager-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wager-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wager-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wagerapi.com/
- group: operate
  title: ''
  type: Contact
  url: https://wagerapi.com/#contact
created: '2025-02-08'
description: Wager API is a modern sports betting data platform that enables developers to build sports betting applications, bots, and predictive models with a single API. The platform provides real-time sports odds including spreads, moneylines, totals, player props, and futures markets across NFL, NCAA, NBA, MLB, NHL, soccer, tennis, and golf. Wager API also delivers player statistics, projections, fantasy data, injury reports, lineup updates, game schedules, and depth charts, making it a comprehensive data source for sports betting and fantasy sports applications.
examples:
- key_count: 2
  name: Wager Api Get Game Odds Example
  slug: wager-api-get-game-odds-example
- key_count: 2
  name: Wager Api Get Player Props Example
  slug: wager-api-get-player-props-example
finops:
- name: Wager Api Finops
  service_category: API
  slug: wager-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wager-api.png
json_schemas:
- name: Wager API Game Odds
  property_count: 8
  slug: wager-api-game-odds
json_structures:
- name: Wager Api Game Odds Structure
  property_count: 0
  slug: wager-api-game-odds-structure
jsonld:
- class_count: 34
  name: Wager Api Context
  property_count: 4
  slug: wager-api-context
layout: provider
modified: '2026-05-19'
name: Wager API
nav: Providers
network: true
overview: 'Wager API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Futures API, Games API, Odds API, and 2 more. Tagged areas include Sports Betting, Sports Odds, Fantasy Sports, Sports Data, and NFL.


  The Wager API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wager API''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Wager Api Plans Pricing
  plan_count: 3
  slug: wager-api-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Wager Api Rate Limits
  slug: wager-api-rate-limits
rules:
- name: Wager API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wager-api-jsonschema-spectral-rules
- name: Wager API API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: wager-api-rules
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/screenshots/wager-api-2026-06-20T201159.png
security:
- kind: authentication
  name: Wager Api Authentication
  slug: wager-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wager Api Domain Security
  slug: wager-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wager-api
tags:
- Sports Betting
- Sports Odds
- Fantasy Sports
- Sports Data
- NFL
- NBA
- MLB
- NHL
- NCAA
website: https://wagerapi.com/
---
