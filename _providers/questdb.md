---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Questdb Agentic Access
  operation_count: 6
  slug: questdb-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: HTTP REST endpoints for SQL execution (/exec), CSV import (/imp), CSV export (/exp), health/metrics (/chk, /metrics) and runtime settings (/settings). Default port 9000.
  name: QuestDB HTTP REST API
  slug: rest-http
- description: InfluxDB Line Protocol over TCP for high-throughput, low-latency time-series ingestion. Default port 9009. Supports authentication and TLS in Enterprise.
  name: QuestDB ILP TCP Ingestion
  slug: ilp-tcp
- description: Influx Line Protocol over HTTP /write endpoint for ingestion clients that prefer HTTP (TLS, auth and ack semantics easier than the TCP variant). Served on the same port (9000) as the REST API.
  name: QuestDB ILP HTTP Ingestion
  slug: ilp-http
- description: PostgreSQL wire-protocol compatibility for queries via psql, JDBC and any Postgres-compatible client. Default port 8812. Supports a subset of Postgres features sufficient for SQL analytics on QuestDB.
  name: QuestDB PostgreSQL Wire Interface
  slug: postgres-wire
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Chk API from QuestDB — 1 operation(s) for chk.
  name: QuestDB Chk API
  slug: questdb-chk-api
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Exec API from QuestDB — 1 operation(s) for exec.
  name: QuestDB Exec API
  slug: questdb-exec-api
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Exp API from QuestDB — 1 operation(s) for exp.
  name: QuestDB Exp API
  slug: questdb-exp-api
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Imp API from QuestDB — 1 operation(s) for imp.
  name: QuestDB Imp API
  slug: questdb-imp-api
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Settings API from QuestDB — 1 operation(s) for settings.
  name: QuestDB Settings API
  slug: questdb-settings-api
- baseURL: http://<host>:9000
  baseurl_source: declared
  description: The Write API from QuestDB — 1 operation(s) for write.
  name: QuestDB Write API
  slug: questdb-write-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QuestDB HTTP REST Chk API
  slug: open-questdb-chk-api
- collection_type: open
  name: QuestDB HTTP REST Chk Exec API
  slug: open-questdb-exec-api
- collection_type: open
  name: QuestDB HTTP REST Chk Exp API
  slug: open-questdb-exp-api
- collection_type: open
  name: QuestDB HTTP REST Chk Imp API
  slug: open-questdb-imp-api
- collection_type: open
  name: QuestDB HTTP REST Chk Settings API
  slug: open-questdb-settings-api
- collection_type: open
  name: QuestDB HTTP REST Chk Write API
  slug: open-questdb-write-api
- collection_type: open
  name: QuestDB HTTP REST API
  slug: open-questdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/questdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/questdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/questdb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/questdb
- group: company
  title: ''
  type: Website
  url: https://questdb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://questdb.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://questdb.com/enterprise/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/questdb/questdb
- group: other
  title: ''
  type: BYOC
  url: https://questdb.com/byoc/
- group: commercial
  title: ''
  type: Plans
  url: plans/questdb-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://questdb.com/rss.xml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/questdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/questdb-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://questdb.com/llms.txt
created: '2026-05-08'
description: QuestDB is a high-performance open-source time-series database. It exposes three programmatic surfaces — an HTTP REST API for SQL queries and CSV import/export, the InfluxDB Line Protocol (ILP) over TCP and HTTP for high-throughput ingestion, and the PostgreSQL wire protocol for compatibility with existing tooling. QuestDB is offered as open-source, Enterprise (self-hosted) and Bring-Your-Own-Cloud (BYOC).
finops:
- name: Questdb Finops
  service_category: Database (Time-Series)
  slug: questdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/questdb.png
layout: provider
modified: '2026-05-08'
name: QuestDB
nav: Providers
network: true
overview: 'QuestDB publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chk API, Exec API, Exp API, and 3 more. Tagged areas include Database, Time Series, SQL, Open-Source, and Performance.


  QuestDB''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Questdb Plans Pricing
  plan_count: 4
  slug: questdb-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Questdb Rate Limits
  slug: questdb-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 52.8
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/questdb/refs/heads/main/screenshots/questdb-2026-06-20T192429.png
security:
- kind: authentication
  name: Questdb Authentication
  slug: questdb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Questdb Domain Security
  slug: questdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: questdb
tags:
- Database
- Time Series
- SQL
- Open-Source
- Performance
- ILP
- PostgreSQL
website: https://questdb.com/
---
