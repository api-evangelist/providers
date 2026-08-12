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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Open-source relational database with advanced SQL compliance and extensibility. Client libraries available in many languages.
  name: PostgreSQL
  slug: postgresql
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postgresql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postgresql.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.postgresql.org/docs/
- group: operate
  title: ''
  type: Community
  url: https://www.postgresql.org/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postgres/postgres
- group: company
  title: ''
  type: Blog
  url: https://www.postgresql.org/news.rss
created: '2026-03-16'
description: PostgreSQL is a powerful, open-source object-relational database system with over 35 years of active development. It provides advanced SQL compliance, ACID transactions, and extensibility. PostgreSQL exposes a binary wire protocol via libpq and language bindings rather than a public HTTP REST API, so there is no canonical OpenAPI specification. HTTP access is typically layered on top via PostgREST, Hasura, or application code.
finops:
- name: Postgresql Finops
  service_category: API
  slug: postgresql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postgresql.png
layout: provider
modified: '2026-04-28'
name: PostgreSQL
nav: Providers
network: true
overview: 'PostgreSQL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Open Source, Relational Database, and SQL.


  PostgreSQL''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Postgresql Plans Pricing
  plan_count: 3
  slug: postgresql-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Postgresql Rate Limits
  slug: postgresql-rate-limits
score:
  band: minimal
  composite: 12.9
  delta: -7.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 20.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/postgresql/refs/heads/main/screenshots/postgresql-2026-06-20T191957.png
security:
- kind: domain-security
  name: Postgresql Domain Security
  slug: postgresql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: postgresql
tags:
- Database
- Open Source
- Relational Database
- SQL
website: https://www.postgresql.org/
---
