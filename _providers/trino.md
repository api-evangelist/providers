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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trino Agentic Access
  operation_count: 6
  slug: trino-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: Cluster status and node information
  name: Trino Cluster API
  slug: trino-cluster-api
- description: Submit and manage SQL queries
  name: Trino Queries API
  slug: trino-queries-api
artifact_total: 182
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trino Client REST API
  slug: open-trino-client-api
- collection_type: open
  name: Trino Client REST Cluster API
  slug: open-trino-cluster-api
- collection_type: open
  name: Trino Client REST Cluster Queries API
  slug: open-trino-queries-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trino-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trino-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trinodb
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/trinodb/trino-python-client
- group: build
  title: ''
  type: GoSDK
  url: https://github.com/trinodb/trino-go-client
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/trinodb/trino-js-client
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/trinodb/charts
- group: build
  title: ''
  type: CLI
  url: https://github.com/trinodb/trino-admin
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/trino-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trino-query-results-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trino-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/trino-rules.yml
- group: company
  title: ''
  type: Website
  url: https://trino.io/
- group: docs
  title: ''
  type: Documentation
  url: https://trino.io/docs/current/
- group: auth
  title: ''
  type: Security
  url: https://trino.io/docs/current/security.html
- group: other
  title: ''
  type: Glossary
  url: https://trino.io/docs/current/glossary.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://trino.io/docs/current/release.html
- group: start
  title: ''
  type: GettingStarted
  url: https://trino.io/download
- group: other
  title: ''
  type: Events
  url: https://trino.io/community#events
- group: company
  title: ''
  type: Blog
  url: https://trino.io/blog/
- group: operate
  title: ''
  type: Forums
  url: https://trino.io/community
created: '2025-06-05'
description: Trino is an open-source, distributed SQL query engine built for lightning-fast analytics over large, heterogeneous data sets. Originally forked from Presto (which emerged at Facebook), it supports ANSI-compliant SQL across a wide range of storage systems from data lakes (S3, HDFS, Iceberg) to relational and NoSQL databases (MySQL, PostgreSQL, Cassandra, MongoDB, Elasticsearch, Kafka, and more).
examples:
- key_count: 2
  name: Trino Cancel Query Example
  slug: trino-cancel-query-example
- key_count: 2
  name: Trino Get Cluster Info Example
  slug: trino-get-cluster-info-example
- key_count: 2
  name: Trino Submit Statement Example
  slug: trino-submit-statement-example
features:
- name: C# Client Driver
- name: Go Client Driver
- name: JDBC
- name: ODBC
- name: Python Client Driver
- name: Elixir Client Driver
- name: Simba JDBC Client Driver
- name: R Client Driver
- name: Ruby Client Driver
- name: Rust Client Driver
- name: Command Line Interface
- name: Grafana
- name: Apache Airflow
- name: Apache DolphinScheduler
- name: Coginiti
- name: Cube
- name: DBeaver
- name: dbt
- name: DbVisualizer
- name: Emacs
- name: FugueSQL
- name: Great Expectations
- name: Harlequin
- name: Hue
- name: Ibis
- name: IBM Cognos Analytics
- name: JetBrains Datagrip
- name: Jupy SQL
- name: Logi Symphony
- name: Looker
- name: Metabase
- name: Microstrategy
- name: Mitzu
- name: Mode
- name: PopSQL
- name: Power BI
- name: Querybook
- name: Quix
- name: Redash
- name: SQuirrel SQL
- name: Tableau
- name: VSCode
- name: waii
- name: Wren AI
- name: yanagishima
- name: Zing Data
- name: Spill to disk
- name: Resource groups
- name: Session property managers
- name: Distributed sort
- name: Dynamic filtering
- name: Graceful shutdown
- name: Fault-tolerant execution
- name: HTTP event listener
- name: Kafka event listener
- name: MySQL event listener
- name: OpenLineage event listener
- name: Client protocol
- name: HTTP server
- name: Resource management
- name: Query management
- name: Catalog management
- name: SQL environment
- name: Spilling
- name: Exchange
- name: Task
- name: Write partitioning
- name: Writer scaling
- name: Node scheduler
- name: Optimizer
- name: Logging
- name: Web UI
- name: Regular expression function
- name: HTTP client
- name: Table statistics
- name: Cost in EXPLAIN
- name: Cost-based optimizations
- name: Pushdown
- name: Adaptive plan optimizations
- name: Amazon Redshift
- name: Apache Cassandra
- name: Apache Druid
- name: Apache Ignite
- name: Apache Kafka
- name: Apache Pinot
- name: Clickhouse
- name: Datafaker
- name: Elasticsearch
- name: Exasol
- name: Google BigQuery
- name: Google Sheets
- name: MariaDB
- name: Microsoft SQL Server
- name: MongoDB
- name: MySQL
- name: OpenSearch
- name: Oracle
- name: PostgreSQL
- name: Prometheus
- name: Redis
- name: SingleStore
- name: Snowflake
- name: TPC
- name: Vertica
- name: Amazon Kinesis
- name: Apache Accumulo
- name: Apache Kudu
- name: Apache Phoenix
- name: Git
- name: OpenAPI
- name: VAST
- name: JMX
- name: Kubernetes
- name: OpenLineage
- name: Open Policy Agent
- name: OpenTelemetry
- name: Trino Gateway
- name: Datadog
- name: Gurubase
- name: jOOQ
- name: Minitrino
- name: RudderStack
- name: SQL Formatter
- name: Testcontainers
- name: Trino-lb
- name: Workload Analyzer
finops:
- name: Trino Finops
  service_category: API
  slug: trino-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trino.png
integrations:
- name: BigQuery
- name: Black Hole
- name: Cassandra
- name: ClickHouse
- name: Delta Lake
- name: Druid
- name: DuckDB
- name: Elasticsearch
- name: Exasol
- name: Faker
- name: Google Sheets
- name: Hive
- name: Hudi
- name: Iceberg
- name: Ignite
- name: JMX
- name: Kafka
- name: Loki
- name: MariaDB
- name: Memory
- name: MongoDB
- name: MySQL
- name: OpenSearch
- name: Oracle
- name: Pinot
- name: PostgreSQL
- name: Prometheus
- name: Redis
- name: Redshift
- name: SingleStore
- name: Snowflake
- name: SQL Server
- name: System
- name: Thrift
- name: TPC-DS
- name: TPC-H
- name: Vertica
json_schemas:
- name: Trino Query Results
  property_count: 10
  slug: trino-query-results
json_structures:
- name: Trino Query Results Structure
  property_count: 0
  slug: trino-query-results-structure
jsonld:
- class_count: 25
  name: Trino Context
  property_count: 21
  slug: trino-context
layout: provider
modified: '2026-05-19'
name: Trino
nav: Providers
network: true
overview: 'Trino publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cluster API and Queries API. Tagged areas include Analytics, Big Data, Distributed SQL, MySQL, and NoSQL.


  The Trino catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trino''s developer surface includes CLI, documentation, changelog, getting-started guide, engineering blog, and 16 more developer resources.'
plans:
- name: Trino Plans Pricing
  plan_count: 3
  slug: trino-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Trino Rate Limits
  slug: trino-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trino API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trino-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Trino API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: trino-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 55.4
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trino/refs/heads/main/screenshots/trino-2026-06-20T195720.png
security:
- kind: domain-security
  name: Trino Domain Security
  slug: trino-domain-security
  summary_line: TLSv1.3
slug: trino
tags:
- Analytics
- Big Data
- Distributed SQL
- MySQL
- NoSQL
- Query
- SQL
website: https://trino.io/
---
