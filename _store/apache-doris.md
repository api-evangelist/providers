---
aid: apache-doris
name: Apache Doris
description: Apache Doris is a high-performance, real-time analytical database based on MPP (Massively Parallel Processing) architecture, governed by the Apache Software Foundation. It provides MySQL-protocol-compatible SQL queries, sub-second query latency on large-scale data, columnar storage with vectorized execution, real-time upsert via Stream Load and Routine Load APIs, and federated querying over data lakes (Hive, Iceberg, Hudi). It supports both shared-nothing and storage/compute-separated deployment modes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Apache
  - Database
  - Lakehouse
  - MPP
  - OLAP
  - Open Source
  - Real-Time
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-doris:apache-doris
    name: Apache Doris
    description: Apache Doris provides a MySQL-compatible protocol for SQL queries, a REST API for cluster management and monitoring, Stream Load HTTP API for real-time bulk data ingestion, Routine Load for continuous Kafka ingestion, and connectors for Flink, Spark, and Kafka. An MCP server is also available for AI-assisted analytics.
    humanURL: https://doris.apache.org/docs/dev/summary/basic-summary
    tags:
      - Analytics
      - Connectors
      - Data Ingestion
      - Flink
      - Kafka
      - MySQL
      - REST
      - SQL
      - Spark
      - Stream Load
    properties:
      - type: Documentation
        url: https://doris.apache.org/docs/dev/summary/basic-summary
      - type: GettingStarted
        url: https://doris.apache.org/docs/dev/install/
      - type: APIReference
        url: https://doris.apache.org/docs/dev/admin-manual/http-actions/
      - type: GitHubRepository
        url: https://github.com/apache/doris
      - type: Tools
        url: https://github.com/apache/doris-mcp-server
        title: MCP Server
      - type: SDK
        url: https://github.com/apache/doris-flink-connector
        title: Flink Connector
      - type: SDK
        url: https://github.com/apache/doris-spark-connector
        title: Spark Connector
      - type: SDK
        url: https://github.com/apache/doris-kafka-connector
        title: Kafka Connector
      - type: Tools
        url: https://github.com/apache/doris-operator
        title: Kubernetes Operator
      - type: Tools
        url: https://github.com/apache/doris-streamloader
        title: Stream Loader CLI
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-schema/apache-doris-routine-load-job-schema.json
        title: Routine Load Job
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-schema/apache-doris-stream-load-response-schema.json
        title: Stream Load Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-schema/apache-doris-table-schema-schema.json
        title: Table Schema
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-structure/apache-doris-routine-load-job-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-structure/apache-doris-stream-load-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-structure/apache-doris-table-schema-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/json-ld/apache-doris-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/examples/apache-doris-routine-load-job-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/examples/apache-doris-stream-load-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/examples/apache-doris-table-schema-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://doris.apache.org/
  - type: Documentation
    url: https://doris.apache.org/docs/dev/
  - type: GettingStarted
    url: https://doris.apache.org/docs/dev/install/
  - type: Blog
    url: https://doris.apache.org/blog/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/doris
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-doris
  - type: Features
    data:
      - name: MPP Columnar Analytics
        description: Massively parallel processing with columnar storage and vectorized execution engine for high-concurrency sub-second analytical queries.
      - name: Stream Load API
        description: HTTP-based bulk data ingestion API that loads CSV, JSON, and Parquet data in real time with transactional guarantees.
      - name: MySQL Protocol Compatibility
        description: Fully MySQL-wire-protocol compatible, enabling use of standard MySQL clients, drivers, and BI tools without modification.
      - name: Federated Data Lakehouse Queries
        description: Query external data in Hive, Iceberg, Hudi, and Delta Lake tables without data movement using Multi-Catalog.
      - name: Real-Time Upsert (Unique Key Model)
        description: Primary key based upsert model supports real-time CDC data ingestion with micro-second latency row-level updates.
      - name: Routine Load from Kafka
        description: Continuous data ingestion from Apache Kafka topics with automatic offset management and exactly-once semantics.
      - name: Tiered Storage
        description: Hot/warm/cold data tiering with object storage (S3, HDFS) for cost-optimized storage at scale.
      - name: MCP Server
        description: Model Context Protocol (MCP) server enabling AI agents to query Doris databases through natural language.
  - type: UseCases
    data:
      - name: Real-Time Dashboards and Reporting
        description: Power business intelligence dashboards with sub-second query latency on live data updated continuously.
      - name: Log and Event Analytics
        description: Ingest and analyze high-volume log, metric, and event data in real time using inverted indexes and full-text search.
      - name: Customer Data Platform
        description: Consolidate customer behavioral and transactional data from multiple sources for real-time segmentation and analytics.
      - name: Data Lakehouse Analytics
        description: Federate queries across data lake (Hive, Iceberg) and operational databases without ETL movement.
      - name: Ad-Hoc Analytics
        description: Enable data analysts to run complex exploratory SQL queries on petabyte-scale datasets with fast response times.
  - type: Integrations
    data:
      - name: Apache Flink
        description: Official Flink Connector for reading from and writing to Doris in real-time Flink streaming pipelines.
      - name: Apache Spark
        description: Official Spark Connector for batch ETL and analytics workflows using Apache Spark.
      - name: Apache Kafka
        description: Kafka Connector and Routine Load for continuous real-time data ingestion from Kafka topics.
      - name: Apache Iceberg / Hudi / Hive
        description: Multi-Catalog feature enables federated queries over Iceberg, Hudi, and Hive Metastore data lakes.
      - name: Kubernetes
        description: Official Kubernetes Operator for automated Doris cluster lifecycle management.
      - name: OpenTelemetry
        description: OpenTelemetry demo integration for observability and tracing in Doris deployments.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-doris/refs/heads/main/vocabulary/apache-doris-vocabulary.yaml
---
