---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Game Of Thrones Agentic Access
  operation_count: 7
  slug: game-of-thrones-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: Books from the A Song of Ice and Fire series
  name: An API of Ice and Fire books API
  slug: game-of-thrones-books-api
- description: Characters from A Song of Ice and Fire and Game of Thrones
  name: An API of Ice and Fire characters API
  slug: game-of-thrones-characters-api
- description: Noble houses from the A Song of Ice and Fire universe
  name: An API of Ice and Fire houses API
  slug: game-of-thrones-houses-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/game-of-thrones-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/game-of-thrones-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anapioficeandfire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/wiki
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/joakimskoog
- group: commercial
  title: ''
  type: Plans
  url: plans/game-of-thrones-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/game-of-thrones-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/game-of-thrones-finops.yml
created: '2026-06-13'
description: An API of Ice and Fire is a free, open REST API providing comprehensive Game of Thrones and A Song of Ice and Fire data including books, characters, and houses from George R.R. Martin's universe. No authentication is required. The API offers structured, quantified data about the HBO series and book series covering all named characters, their allegiances, relationships, book appearances, TV season appearances, and details on every noble house and published book in the series.
examples:
- key_count: 11
  name: Book
  slug: book
- key_count: 16
  name: Character
  slug: character
- key_count: 16
  name: House
  slug: house
finops:
- name: Game Of Thrones Finops
  service_category: ''
  slug: game-of-thrones-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/game-of-thrones.png
json_schemas:
- name: Book
  property_count: 11
  slug: book
- name: Character
  property_count: 16
  slug: character
- name: House
  property_count: 16
  slug: house
jsonld:
- class_count: 21
  name: context Context
  property_count: 20
  slug: context
layout: provider
modified: '2026-06-13'
name: An API of Ice and Fire
nav: Providers
network: true
overview: 'An API of Ice and Fire publishes 3 APIs on the [APIs.io](https://apis.io/) network: books API, characters API, and houses API. Tagged areas include Game of Thrones, ASOIAF, A Song of Ice and Fire, Books, and Characters.


  The An API of Ice and Fire catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  An API of Ice and Fire''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Game Of Thrones Plans Pricing
  plan_count: 1
  slug: game-of-thrones-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Game Of Thrones Rate Limits
  slug: game-of-thrones-rate-limits
rules:
- name: An API of Ice and Fire API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: game-of-thrones-jsonschema-spectral-rules
score:
  band: thin
  composite: 43.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.3
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 43.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/game-of-thrones/refs/heads/main/screenshots/game-of-thrones-2026-06-20T181637.png
security:
- kind: domain-security
  name: Game Of Thrones Domain Security
  slug: game-of-thrones-domain-security
  summary_line: TLSv1.3 · HSTS
slug: game-of-thrones
tags:
- Game of Thrones
- ASOIAF
- A Song of Ice and Fire
- Books
- Characters
- Houses
- Fantasy
- Entertainment
- Open API
- Free API
website: https://anapioficeandfire.com/
---
