---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jservice Agentic Access
  operation_count: 6
  slug: jservice-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 3
apis:
- description: Category collections of clues.
  name: jService Categories API
  slug: jservice-categories-api
- description: Jeopardy! questions, answers, and metadata.
  name: jService Clues API
  slug: jservice-clues-api
- description: User-driven reporting of invalid clues.
  name: jService Moderation API
  slug: jservice-moderation-api
artifact_total: 19
collections:
- collection_type: open
  name: jService Trivia API
  slug: open-jservice
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jservice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jservice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/sottenad/jService
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/sottenad/jService
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: License
  url: https://github.com/sottenad/jService/blob/master/LICENSE.txt
- group: other
  title: ''
  type: DataSource
  url: https://j-archive.com
created: '2026-05-28'
description: jService is an open source Ruby on Rails trivia API that serves approximately 200,000 Jeopardy! questions, answers, and categories scraped from the J! Archive fan site. The original public deployment at jservice.io is no longer operational, but the project (sottenad/jService, MIT licensed) remains available for self-hosting against PostgreSQL. The API exposes random clues, final Jeopardy clues, filtered clue queries, category listings, single-category lookup, and invalid-clue reporting under /api/*.
examples:
- key_count: 4
  name: Jservice Categories Example
  slug: jservice-categories-example
- key_count: 4
  name: Jservice Category Example
  slug: jservice-category-example
- key_count: 4
  name: Jservice Clues Example
  slug: jservice-clues-example
- key_count: 4
  name: Jservice Final Example
  slug: jservice-final-example
- key_count: 4
  name: Jservice Invalid Example
  slug: jservice-invalid-example
- key_count: 4
  name: Jservice Random Example
  slug: jservice-random-example
image: https://avatars.githubusercontent.com/u/957383?v=4
json_schemas:
- name: jService Category
  property_count: 6
  slug: jservice-category
- name: jService Clue
  property_count: 9
  slug: jservice-clue
json_structures:
- name: Jservice Category Structure
  property_count: 5
  slug: jservice-category-structure
- name: Jservice Clue Structure
  property_count: 8
  slug: jservice-clue-structure
jsonld:
- class_count: 4
  name: Jservice Context
  property_count: 12
  slug: jservice-context
layout: provider
modified: '2026-05-30'
name: jService
nav: Providers
network: true
overview: 'jService publishes 3 APIs on the [APIs.io](https://apis.io/) network: Categories API, Clues API, and Moderation API. Tagged areas include Games And Comics, Trivia, Jeopardy, Open Source, and Ruby.


  The jService catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 4
rules:
- name: jService API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jservice-jsonschema-spectral-rules
- name: jService API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: jservice-rules
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 68.7
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jservice/refs/heads/main/screenshots/jservice-2026-06-20T183813.png
security:
- kind: domain-security
  name: Jservice Domain Security
  slug: jservice-domain-security
  summary_line: no transport/DNS hardening detected
slug: jservice
tags:
- Games And Comics
- Trivia
- Jeopardy
- Open Source
- Ruby
- Rails
- Public APIs
---
