---
aid: trino
url: https://raw.githubusercontent.com/api-evangelist/trino/refs/heads/main/apis.yml
apis:
  - aid: trino:trino-client-api
    name: Trino Client REST API
    tags:
      - Analytics
      - Big Data
      - Queries
      - SQL
    humanURL: https://trino.io/docs/current/develop/client-protocol.html
    baseURL: http://localhost:8080
    properties:
      - url: https://trino.io/docs/current/develop/client-protocol.html
        type: Documentation
      - url: openapi/trino-client-api-openapi.yml
        type: OpenAPI
    description: The Trino Client REST API enables clients to submit SQL queries to a Trino coordinator and retrieve results. Clients POST SQL to /v1/statement, then poll GET on the returned nextUri, and may DELETE nextUri to cancel. Used by all Trino client drivers (Python, Go, Java, JavaScript) and data tools like dbt, Grafana, and Apache Superset.
name: Trino
tags:
  - Analytics
  - Big Data
  - Distributed SQL
  - MySQL
  - NoSQL
  - Queries
  - SQL
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://github.com/trinodb
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/trinodb/trino-python-client
    name: Trino Python Client
    type: PythonSDK
  - url: https://github.com/trinodb/trino-go-client
    name: Trino Go Client
    type: GoSDK
  - url: https://github.com/trinodb/trino-js-client
    name: Trino JavaScript Client
    type: JavaScriptSDK
  - url: https://github.com/trinodb/charts
    name: Trino Helm Charts
    type: HelmChart
  - url: https://github.com/trinodb/trino-admin
    name: Trino Admin Tool
    type: CLI
  - url: json-ld/trino-context.jsonld
    name: Trino JSON-LD Context
    type: JSONLDContext
  - url: json-schema/trino-query-results-schema.json
    name: Trino Query Results Schema
    type: JSONSchema
  - url: vocabulary/trino-vocabulary.yml
    name: Trino Vocabulary
    type: Vocabulary
  - url: rules/trino-rules.yml
    name: Trino Spectral Rules
    type: SpectralRules
  - url: https://trino.io/
    name: "Trino |\_Distributed SQL query engine for big data"
    type: Website
    description: 'null'
  - url: https://trino.io/docs/current/
    name: Trino documentation  Trino 476 Documentation
    type: Documentation
    description: 'null'
  - url: https://trino.io/docs/current/security.html
    name: Security  Trino 476 Documentation
    type: Security
    description: 'null'
  - url: https://trino.io/docs/current/connector.html
    name: Connectors  Trino 476 Documentation
    type: Integrations
    description: 'null'
  - url: https://trino.io/docs/current/glossary.html
    name: Glossary  Trino 476 Documentation
    type: Glossary
    description: 'null'
  - url: https://trino.io/docs/current/release.html
    name: Release notes  Trino 476 Documentation
    type: ChangeLog
    description: 'null'
  - url: https://trino.io/download
    name: "Trino |\_Get started with Trino"
    type: GettingStarted
    description: 'null'
  - url: https://trino.io/community#events
    name: "Trino |\_Trino Community"
    type: Events
    description: 'null'
  - url: https://trino.io/blog/
    name: Trino | Trino blog
    type: Blog
    description: 'null'
  - url: https://trino.io/community
    name: "Trino |\_Trino Community"
    type: Discussions
    description: 'null'
  - name: Features
    type: Features
    data:
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
  - name: Integrations
    type: Integrations
    data:
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
created: '2025-06-05'
modified: '2026-05-03'
description: Trino is an open-source, distributed SQL query engine built for lightning-fast analytics over large, heterogeneous data sets. Originally forked from Presto (which emerged at Facebook), it supports ANSI-compliant SQL across a wide range of storage systems from data lakes (S3, HDFS, Iceberg) to relational and NoSQL databases (MySQL, PostgreSQL, Cassandra, MongoDB, Elasticsearch, Kafka, and more).
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
