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
  name: Clickhouse Agentic Access
  operation_count: 5
  slug: clickhouse-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 9
apis:
- description: HTTP interface (default port 8123, HTTPS 8443) for executing SQL queries against ClickHouse. Supports SELECT via GET, mutations via POST, multiple output formats (JSON, CSV, XML, TabSeparated), and au
  name: ClickHouse HTTP Interface
  slug: clickhouse-http-interface
- description: Native binary TCP protocol used by ClickHouse client libraries for maximum throughput between client and server (default port 9000).
  name: ClickHouse Native TCP Interface
  slug: clickhouse-native
- description: MySQL wire protocol compatibility allowing existing MySQL clients and BI tools to query ClickHouse without driver changes.
  name: ClickHouse MySQL Interface
  slug: clickhouse-mysql
- description: PostgreSQL wire protocol compatibility for connecting psql, JDBC and other PostgreSQL clients to ClickHouse.
  name: ClickHouse PostgreSQL Interface
  slug: clickhouse-postgresql
- description: gRPC interface defined by clickhouse_grpc.proto for efficient binary communication.
  name: ClickHouse gRPC Interface
  slug: clickhouse-grpc
- description: The ClickHouse HTTP Interface API from ClickHouse — 1 operation(s) for clickhouse http interface.
  name: ClickHouse ClickHouse HTTP Interface API
  slug: clickhouse-clickhouse-http-interface-api
- description: The Ping API from ClickHouse — 1 operation(s) for ping.
  name: ClickHouse Ping API
  slug: clickhouse-ping-api
- description: The Play API from ClickHouse — 1 operation(s) for play.
  name: ClickHouse Play API
  slug: clickhouse-play-api
- description: The Replicas Status API from ClickHouse — 1 operation(s) for replicas status.
  name: ClickHouse Replicas Status API
  slug: clickhouse-replicas-status-api
artifact_total: 25
asyncapis:
- description: AsyncAPI description of the documented streaming surface that ClickHouse offers through the Kafka table engine. ClickHouse itself does NOT publish a public WebSocket, Server-Sent Events, or push-style
  name: ClickHouse Kafka Table Engine (Consumer-Side Streaming)
  slug: clickhouse-kafka-engine-asyncapi
collections:
- collection_type: postman
  name: ClickHouse HTTP Interface API
  slug: postman-clickhouse-clickhouse-http-interface-api
- collection_type: postman
  name: ClickHouse HTTP Interface Ping API
  slug: postman-clickhouse-ping-api
- collection_type: postman
  name: ClickHouse HTTP Interface Play API
  slug: postman-clickhouse-play-api
- collection_type: postman
  name: ClickHouse HTTP Interface Replicas Status API
  slug: postman-clickhouse-replicas-status-api
- collection_type: open
  name: ClickHouse HTTP Interface
  slug: open-clickhouse
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/clickhouse/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickhouse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clickhouse-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickhouse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickhouse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickhouseinc
- group: company
  title: ''
  type: Website
  url: https://clickhouse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clickhouse.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://clickhouse.com/docs/en/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ClickHouse/ClickHouse
- group: company
  title: ''
  type: Blog
  url: https://clickhouse.com/blog
- group: operate
  title: ''
  type: Community
  url: https://clickhouse.com/community
- group: operate
  title: ''
  type: Slack
  url: https://clickhouse.com/slack
- group: commercial
  title: ''
  type: Pricing
  url: https://clickhouse.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://clickhouse.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickhouse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickhouse.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickhouse.com/legal/terms-of-service
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clickhouse-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clickhouse-rules.yml
created: '2024-01-01'
description: ClickHouse is a fast open-source column-oriented database management system that enables real-time analytical reporting using SQL. ClickHouse exposes multiple interfaces - an HTTP interface for SQL queries, native TCP, MySQL and PostgreSQL wire-compatible interfaces, and a gRPC interface - and the ClickHouse Cloud management plane offers a public OpenAPI-described REST API for provisioning and managing services, organizations, members, API keys, backups, and private endpoints.
finops:
- name: Clickhouse Finops
  service_category: API
  slug: clickhouse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickhouse.png
jsonld:
- class_count: 0
  name: Clickhouse Context
  property_count: 5
  slug: clickhouse-context
layout: provider
modified: '2026-04-26'
name: ClickHouse
nav: Providers
network: true
overview: 'ClickHouse publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ClickHouse HTTP Interface API, Ping API, Play API, and 1 more. Tagged areas include Analytics, Cloud Database, Column-Oriented, Database, and OLAP.


  The ClickHouse catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ClickHouse''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Clickhouse Plans Pricing
  plan_count: 3
  slug: clickhouse-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Clickhouse Rate Limits
  slug: clickhouse-rate-limits
rules:
- name: ClickHouse API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: clickhouse-asyncapi-spectral-rules
- name: ClickHouse API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: clickhouse-rules
score:
  band: strong
  composite: 58.4
  delta: -3.7
  facets:
    commercial_clarity: 78.9
    contract_quality: 59.3
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickhouse/refs/heads/main/screenshots/clickhouse-2026-06-20T174515.png
security:
- kind: authentication
  name: Clickhouse Authentication
  slug: clickhouse-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clickhouse Domain Security
  slug: clickhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clickhouse Trust Center
  slug: clickhouse-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: clickhouse
tags:
- Analytics
- Cloud Database
- Column-Oriented
- Database
- OLAP
- Open Source
- Real-Time
- SQL
website: https://clickhouse.com/
---
