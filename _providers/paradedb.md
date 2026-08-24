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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: BM25 full-text search inside Postgres via the pg_search extension, built on Tantivy. Consumed as SQL over the PostgreSQL wire protocol - BM25 indexes are created with CREATE INDEX ... USING bm25, quer
  name: ParadeDB pg_search (Full-Text Search)
  slug: pg_search
- description: Columnar storage, fast aggregates, and OLAP-style analytics over Postgres data, powered by Apache DataFusion and Postgres parallel workers. Accessed entirely through standard SQL aggregate queries ove
  name: ParadeDB Analytics (pg_analytics)
  slug: analytics
- description: The primary integration surface for ParadeDB - the PostgreSQL wire protocol itself. Any standard Postgres client, driver, or ORM (psql, libpq, Drizzle, Django, SQLAlchemy, Rails, EF Core) connects ove
  name: ParadeDB Postgres SQL Interface
  slug: postgres-sql-interface
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ParadeDB SQL Interface (No REST API)
  slug: open-paradedb
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paradedb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paradedb-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://paradedb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paradedb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paradedb
- group: company
  title: ''
  type: Website
  url: https://www.paradedb.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paradedb.com
- group: commercial
  title: ''
  type: Plans
  url: plans/paradedb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paradedb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paradedb-finops.yml
created: '2026-06-20'
description: ParadeDB is an open-source Postgres extension stack (pg_search for BM25 full-text search and pg_analytics for columnar OLAP) that turns PostgreSQL into a real-time search and analytics engine, positioned as an Elasticsearch alternative. Its interface is SQL over the PostgreSQL wire protocol - custom operators (@@@) and paradedb.* functions - not a REST API.
finops:
- name: Paradedb Finops
  service_category: Databases
  slug: paradedb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paradedb.png
layout: provider
modified: '2026-06-20'
name: ParadeDB
nav: Providers
network: true
overview: 'ParadeDB publishes 3 APIs on the [APIs.io](https://apis.io/) network: pg_search (Full-Text Search), Analytics (pg_analytics), and Postgres SQL Interface. Tagged areas include Search, Full-Text Search, Analytics, PostgreSQL, and Database.


  ParadeDB''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Paradedb Plans Pricing
  plan_count: 4
  slug: paradedb-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Paradedb Rate Limits
  slug: paradedb-rate-limits
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 28.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paradedb/refs/heads/main/screenshots/paradedb-2026-06-20T191455.png
security:
- kind: domain-security
  name: Paradedb Domain Security
  slug: paradedb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paradedb Vulnerability Disclosure
  slug: paradedb-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: paradedb
tags:
- Search
- Full-Text Search
- Analytics
- PostgreSQL
- Database
- Elasticsearch Alternative
website: https://www.paradedb.com
---
