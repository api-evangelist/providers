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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: Open-source relational database with advanced SQL compliance and extensibility. Client libraries available in many languages.
  name: PostgreSQL
  slug: postgresql
- description: The PostgreSQL frontend/backend protocol is the low-level message-based protocol used by all client drivers (libpq, JDBC, ODBC, psycopg, pgx, node-postgres, etc.) to communicate with the PostgreSQL se
  name: PostgreSQL Wire Protocol
  slug: wire-protocol
- description: libpq is the official C application programmer's interface to PostgreSQL and the underlying library used by most other PostgreSQL client interfaces. It provides connection management, query execution,
  name: libpq C Client Library
  slug: libpq
- description: The official Type 4 JDBC driver for PostgreSQL enables Java applications to connect to PostgreSQL using the standard JDBC API. It supports connection pooling, prepared statements, batched updates, LOB
  name: PostgreSQL JDBC Driver
  slug: jdbc
- description: The official ODBC driver for PostgreSQL providing Open Database Connectivity for Windows, Linux, and macOS applications including Microsoft Office, Tableau, Power BI, and other BI/ETL tools that consu
  name: PostgreSQL ODBC Driver (psqlODBC)
  slug: odbc
artifact_total: 10
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
graphqls:
- description: ''
  name: PostgreSQL GraphQL API
  slug: postgres-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postgresql.png
layout: provider
modified: '2026-04-28'
name: PostgreSQL
nav: Providers
network: true
overview: 'PostgreSQL publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Open-Source, Relational Database, and SQL.


  PostgreSQL''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Postgresql Plans Pricing
  plan_count: 3
  slug: postgresql-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Postgresql Rate Limits
  slug: postgresql-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postgresql/refs/heads/main/screenshots/postgresql-2026-06-20T191957.png
security:
- kind: domain-security
  name: Postgresql Domain Security
  slug: postgresql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: postgresql
tags:
- Database
- Open-Source
- Relational Database
- SQL
website: https://www.postgresql.org/
---
