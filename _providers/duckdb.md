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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: DuckDB ships as a library with first-class bindings for Python, R, Java (JDBC), Node.js, C/C++, Go, Rust, Swift, Julia, and the browser via DuckDB-Wasm. There is no network REST API; clients call Duck
  name: DuckDB In-Process Library
  slug: duckdb-library
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duckdb-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duckdb
- group: company
  title: ''
  type: Website
  url: https://duckdb.org/
- group: start
  title: ''
  type: Portal
  url: https://duckdb.org/docs/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/duckdb/duckdb
- group: other
  title: ''
  type: Foundation
  url: https://duckdb.org/foundation/
- group: other
  title: MotherDuck (cloud DuckDB)
  type: CommercialOffering
  url: https://motherduck.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/duckdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/duckdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/duckdb-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://duckdb.org/feed.xml
- group: agent
  title: ''
  type: LlmsText
  url: https://duckdb.org/llms.txt
created: '2026-05-08'
description: DuckDB is an in-process, MIT-licensed analytical SQL database with no external dependencies. It runs as a library embedded in the host application (CLI, Python, Node.js, R, Java/JDBC, Go, Wasm, etc.) and does not expose a network REST API.
finops:
- name: Duckdb Finops
  service_category: API
  slug: duckdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duckdb.png
layout: provider
modified: '2026-05-08'
name: DuckDB
nav: Providers
network: true
overview: 'DuckDB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Analytics, OLAP, Embedded, and Open Source.


  DuckDB''s developer surface includes developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Duckdb Plans Pricing
  plan_count: 3
  slug: duckdb-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Duckdb Rate Limits
  slug: duckdb-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duckdb/refs/heads/main/screenshots/duckdb-2026-06-20T180308.png
security:
- kind: domain-security
  name: Duckdb Domain Security
  slug: duckdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: duckdb
tags:
- Database
- Analytics
- OLAP
- Embedded
- Open Source
website: https://duckdb.org/
---
