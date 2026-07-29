---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Materialize Agentic Access
  operation_count: 1
  slug: materialize-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 4
apis:
- description: Session-less HTTP API for executing SQL statements against a Materialize region. Authenticates with HTTP Basic (email + app password). Supports a simple mode with a single query and an extended mode t
  name: Materialize HTTP API
  slug: materialize-http-api
- description: Materialize speaks the PostgreSQL wire protocol on port 6875, so any psql or libpq-based client (Go, Java, Node.js, PHP, Python, Ruby, Rust) can connect and run streaming SQL.
  name: Materialize PostgreSQL Wire Protocol
  slug: materialize-pgwire
- description: 'AsyncAPI 2.6 description of Materialize''s event-driven integration surface: Kafka sources (CREATE SOURCE ... FROM KAFKA), Kafka sinks (CREATE SINK ... INTO KAFKA), and HTTP webhook sources (CREATE SOU'
  name: Materialize Streaming Sources and Sinks (AsyncAPI)
  slug: materialize-streaming-asyncapi
- description: The Sql API from Materialize — 1 operation(s) for sql.
  name: Materialize Sql API
  slug: materialize-sql-api
artifact_total: 14
asyncapis:
- description: AsyncAPI description of Materialize's streaming integration surface. Materialize is an operational data warehouse that ingests events from external message brokers and HTTP webhooks (sources) and emit
  name: Materialize Streaming Sources and Sinks
  slug: materialize-asyncapi
collections:
- collection_type: open
  name: Materialize HTTP API
  slug: open-materialize
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/materialize-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/materialize-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/materialize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/materialize-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MaterializeInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/materializeinc
- group: company
  title: ''
  type: Website
  url: https://materialize.com/
- group: start
  title: ''
  type: Portal
  url: https://materialize.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://materialize.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/materialize-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/materialize-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/materialize-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://materialize.com/rss.xml
created: '2026-05-08'
description: Materialize is an operational data warehouse that uses streaming SQL views maintained with sub-second latency. It exposes a PostgreSQL wire-compatible interface and a session-less HTTP API for SQL execution.
finops:
- name: Materialize Finops
  service_category: API
  slug: materialize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/materialize.png
layout: provider
modified: '2026-05-29'
name: Materialize
nav: Providers
network: true
overview: 'Materialize publishes 2 APIs on the [APIs.io](https://apis.io/) network: Streaming Sources and Sinks (AsyncAPI) and Sql API. Tagged areas include Streaming, Data Warehouse, SQL, Real-Time, and PostgreSQL Compatible.


  The Materialize catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Materialize''s developer surface includes authentication, developer portal, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Materialize Plans Pricing
  plan_count: 3
  slug: materialize-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Materialize Rate Limits
  slug: materialize-rate-limits
rules:
- name: Materialize API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: materialize-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.1
  delta: -4.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 59.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/materialize/refs/heads/main/screenshots/materialize-2026-06-20T185034.png
security:
- kind: authentication
  name: Materialize Authentication
  slug: materialize-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Materialize Domain Security
  slug: materialize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Materialize Trust Center
  slug: materialize-trust-center
  summary_line: SOC 2
slug: materialize
tags:
- Streaming
- Data Warehouse
- SQL
- Real-Time
- PostgreSQL Compatible
website: https://materialize.com/
---
