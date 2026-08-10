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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Search and retrieve English-language poems by author, title, line content, and line count. Returns structured JSON with title, author, lines array, and linecount fields. No authentication required.
  name: PoetryDB API
  slug: poetry-db
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/poetry-db-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poetry-db-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poetrydb.org
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/thundercomb/poetrydb/blob/master/README.md
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/thundercomb
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/thundercomb/poetrydb
- group: other
  title: ''
  type: X
  url: https://x.com/po3db
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/poetry-db/refs/heads/main/plans/poetry-db-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/poetry-db/refs/heads/main/rate-limits/poetry-db-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/poetry-db/refs/heads/main/finops/poetry-db-finops.yml
created: '2026-06-13'
description: PoetryDB is a public REST API providing programmatic access to a database of English-language poems. Developers can search the collection by author name, poem title, line content, and line count. The API requires no authentication or API key, returns JSON or plain text responses, and supports CORS. It is built on Ruby and Sinatra with a MongoDB datastore and is maintained as a free open-source resource for poets and developers.
examples:
- key_count: 4
  name: Get Poems By Author
  slug: get-poems-by-author
- key_count: 4
  name: Get Poems By Linecount
  slug: get-poems-by-linecount
- key_count: 4
  name: Get Random Poems
  slug: get-random-poems
finops:
- name: Poetry Db Finops
  service_category: ''
  slug: poetry-db-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poetry-db.png
json_schemas:
- name: Poem
  property_count: 4
  slug: poem
jsonld:
- class_count: 5
  name: context Context
  property_count: 1
  slug: context
layout: provider
modified: '2026-06-13'
name: PoetryDB
nav: Providers
network: true
overview: 'PoetryDB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Poetry, Literature, Public Domain, English Language, and Search.


  The PoetryDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PoetryDB''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Poetry Db Plans Pricing
  plan_count: 1
  slug: poetry-db-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 0
  name: Poetry Db Rate Limits
  slug: poetry-db-rate-limits
rules:
- name: PoetryDB API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: poetry-db-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.2
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 34.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poetry-db/refs/heads/main/screenshots/poetry-db-2026-06-20T191838.png
security:
- kind: domain-security
  name: Poetry Db Domain Security
  slug: poetry-db-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Poetry Db Vulnerability Disclosure
  slug: poetry-db-vulnerability-disclosure
  summary_line: disclosure policy published
slug: poetry-db
tags:
- Poetry
- Literature
- Public Domain
- English Language
- Search
- Open Data
website: https://poetrydb.org
---
