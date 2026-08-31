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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 4
apis:
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
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postgres-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postgresql.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.postgresql.org/docs/
- group: other
  title: ''
  type: Download
  url: https://www.postgresql.org/download/
- group: build
  title: ''
  type: Source Code
  url: https://git.postgresql.org/gitweb/?p=postgresql.git
- group: build
  title: ''
  type: GitHub Mirror
  url: https://github.com/postgres/postgres
- group: other
  title: ''
  type: Mailing Lists
  url: https://www.postgresql.org/list/
- group: operate
  title: ''
  type: Community
  url: https://www.postgresql.org/community/
- group: commercial
  title: ''
  type: License
  url: https://www.postgresql.org/about/licence/
- group: company
  title: ''
  type: Blog
  url: https://www.postgresql.org/news.rss
created: '2026-05-11'
description: PostgreSQL is a powerful, open-source object-relational database system with over 35 years of active development that has earned a strong reputation for reliability, feature robustness, and performance. It supports advanced SQL features, JSON, full-text search, custom data types, extensions, and transactional DDL. PostgreSQL does not expose a native HTTP REST API; client applications connect via the libpq C client library, JDBC, ODBC, or one of dozens of language-specific drivers using the PostgreSQL wire protocol (default port 5432).
graphqls:
- description: ''
  name: PostgreSQL GraphQL API
  slug: postgres-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postgres.png
layout: provider
modified: '2026-05-11'
name: PostgreSQL
nav: Providers
network: true
overview: 'PostgreSQL publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Relational Database, SQL, Open-Source, and PostgreSQL.


  PostgreSQL''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postgres/refs/heads/main/screenshots/postgres-2026-06-20T191955.png
security:
- kind: domain-security
  name: Postgres Domain Security
  slug: postgres-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: postgres
tags:
- Database
- Relational Database
- SQL
- Open-Source
- PostgreSQL
- Object-Relational
- Data Storage
website: https://www.postgresql.org
---
