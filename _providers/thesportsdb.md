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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Thesportsdb Agentic Access
  operation_count: 17
  slug: thesportsdb-agentic-access
  summary_line: 17 operations
api_count: 5
apis:
- description: Sports event scheduling and results.
  name: TheSportsDB Events API
  slug: thesportsdb-events-api
- description: List leagues, teams, players, and events.
  name: TheSportsDB Lists API
  slug: thesportsdb-lists-api
- description: Look up detailed data by ID.
  name: TheSportsDB Lookup API
  slug: thesportsdb-lookup-api
- description: Search for teams, players, events, and venues.
  name: TheSportsDB Search API
  slug: thesportsdb-search-api
- description: Season standings and results.
  name: TheSportsDB Seasons API
  slug: thesportsdb-seasons-api
artifact_total: 18
collections:
- collection_type: open
  name: TheSportsDB API
  slug: open-thesportsdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thesportsdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thesportsdb-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thesportsapi
- group: company
  title: ''
  type: Website
  url: https://www.thesportsdb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thesportsdb.com/documentation
- group: start
  title: ''
  type: Signup
  url: https://www.thesportsdb.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thesportsdb.com/patreon
- group: build
  title: ''
  type: Examples
  url: https://www.thesportsdb.com/docs_api_examples
created: '2025-03-01'
description: An open, crowd-sourced sports database of artwork and metadata with a free sports API in JSON format. TheSportsDB provides data on sports leagues, teams, players, events, venues, and season standings across a wide range of sports worldwide including soccer, basketball, baseball, American football, hockey, tennis, and more.
examples:
- key_count: 2
  name: Thesportsdb Get Next Team Events Example
  slug: thesportsdb-get-next-team-events-example
- key_count: 2
  name: Thesportsdb Search Teams Example
  slug: thesportsdb-search-teams-example
finops:
- name: Thesportsdb Finops
  service_category: API
  slug: thesportsdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thesportsdb.png
json_schemas:
- name: TheSportsDB Team
  property_count: 16
  slug: thesportsdb-team
json_structures:
- name: Thesportsdb Structure
  property_count: 0
  slug: thesportsdb-structure
jsonld:
- class_count: 0
  name: Thesportsdb Context
  property_count: 4
  slug: thesportsdb-context
layout: provider
modified: '2026-05-19'
name: TheSportsDB
nav: Providers
network: true
overview: 'TheSportsDB publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, Lists API, Lookup API, and 2 more. Tagged areas include Sports, Database, Free, Open Data, and Teams.


  The TheSportsDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TheSportsDB''s developer surface includes documentation, signup flow, pricing, code examples, and 4 more developer resources.'
plans:
- name: Thesportsdb Plans Pricing
  plan_count: 3
  slug: thesportsdb-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Thesportsdb Rate Limits
  slug: thesportsdb-rate-limits
rules:
- name: TheSportsDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thesportsdb-jsonschema-spectral-rules
- name: TheSportsDB API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: thesportsdb-rules
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.7
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thesportsdb/refs/heads/main/screenshots/thesportsdb-2026-06-20T195300.png
security:
- kind: domain-security
  name: Thesportsdb Domain Security
  slug: thesportsdb-domain-security
  summary_line: TLSv1.3
slug: thesportsdb
tags:
- Sports
- Database
- Free
- Open Data
- Teams
- Players
- Events
website: https://www.thesportsdb.com/
---
