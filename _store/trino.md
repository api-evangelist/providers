---
aid: trino
url: https://raw.githubusercontent.com/api-evangelist/trino/refs/heads/main/apis.yml
apis:
- aid: trino:trino
  name: Trino
  tags:
  - MySQL
  - NoSQL
  - SQL
  humanURL: ' https://trino.io/'
  properties:
  - url: ' https://trino.io/'
    type: Documentation
  description: Fast distributed SQL query engine for big data analytics that helps you explore your data universe.
name: Trino
tags:
- MySQL
- NoSQL
- Queries
- SQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://github.com/trinodb
  name: GitHub Organization
  type: GitHubOrganization
- url: https://trino.io/
  name: Trino | Distributed SQL query engine for big data
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
  name: Trino | Get started with Trino
  type: GettingStarted
  description: 'null'
- url: https://trino.io/community#events
  name: Trino | Trino Community
  type: Events
  description: 'null'
- url: https://trino.io/blog/
  name: Trino | Trino blog
  type: Blog
  description: 'null'
- url: https://trino.io/community
  name: Trino | Trino Community
  type: Discussions
  description: 'null'
- data:
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
  name: Features
  type: Features
- data:
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
  name: Integrations
  type: Integrations
created: '2025-06-05'
modified: '2026-04-07'
position: Consuming
description: Trino is an open-source, distributed SQL query engine built for lightning-fast analytics over large, heterogeneous data sets. Originally forked from Presto (which emerged at Facebook), it supports ANSI-compliant SQL across a wide range of storage systemsfrom data lakes (S3, HDFS, Iceberg) to relational and NoSQL databases (MySQL, PostgreSQL, Cassandra, MongoDB, Elasticsearch, Kafka, and more) .
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

