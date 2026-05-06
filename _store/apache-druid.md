---
aid: apache-druid
name: Apache Druid
description: Apache Druid is a high-performance, real-time analytics database governed by the Apache Software Foundation, designed for fast slice-and-dice OLAP queries on event-time data. It features a distributed, column-oriented storage engine with automatic rollup, supports both streaming (Kafka, Kinesis) and batch (S3, HDFS, local) data ingestion, and provides a SQL query interface plus a native JSON query API via REST. Druid is optimized for sub-second queries at petabyte scale with high concurrency.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Apache
  - Database
  - Kafka
  - OLAP
  - Open Source
  - Real-Time
  - SQL
  - Time Series
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-druid:apache-druid-rest-api
    name: Apache Druid REST API
    description: Druid exposes REST APIs for Druid SQL (POST /druid/v2/sql), native JSON queries (POST /druid/v2), batch and streaming data ingestion tasks, supervisor management for Kafka/Kinesis ingestion, data segment management, coordinator and overlord operations, process status, and dynamic configuration. A JDBC driver is also available for SQL access via JDBC clients.
    humanURL: https://druid.apache.org/docs/latest/api-reference/
    tags:
      - Analytics
      - Data Ingestion
      - Datasources
      - JSON Query
      - Kafka
      - OLAP
      - REST
      - SQL
      - Segments
      - Supervisors
    properties:
      - type: Documentation
        url: https://druid.apache.org/docs/latest/api-reference/
      - type: GettingStarted
        url: https://druid.apache.org/docs/latest/tutorials/tutorial-batch-hadoop
      - type: APIReference
        url: https://druid.apache.org/docs/latest/api-reference/
      - type: GitHubRepository
        url: https://github.com/apache/druid
      - type: Tools
        url: https://github.com/apache/druid-operator
        title: Kubernetes Operator
      - type: SDK
        url: https://mvnrepository.com/artifact/org.apache.druid/druid-sql
        title: JDBC Driver (Maven)
      - type: SDK
        url: https://pypi.org/project/pydruid/
        title: pydruid Python Client
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-schema/apache-druid-ingestion-task-schema.json
        title: Ingestion Task
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-schema/apache-druid-sql-query-request-schema.json
        title: Sql Query Request
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-schema/apache-druid-sql-query-response-schema.json
        title: Sql Query Response
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-schema/apache-druid-supervisor-schema.json
        title: Supervisor
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-structure/apache-druid-ingestion-task-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-structure/apache-druid-sql-query-request-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-structure/apache-druid-sql-query-response-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-structure/apache-druid-supervisor-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/json-ld/apache-druid-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/examples/apache-druid-ingestion-task-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/examples/apache-druid-sql-query-request-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/examples/apache-druid-sql-query-response-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/examples/apache-druid-supervisor-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://druid.apache.org/
  - type: Documentation
    url: https://druid.apache.org/docs/latest/
  - type: GettingStarted
    url: https://druid.apache.org/docs/latest/tutorials/
  - type: Blog
    url: https://druid.apache.org/blog/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/druid
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/druid
  - type: Features
    data:
      - name: Sub-Second OLAP Queries
        description: Columnar storage with bitmap indexes, dictionary encoding, and pre-aggregation (rollup) enables sub-second queries on billions of events.
      - name: Druid SQL API
        description: REST endpoint for submitting standard SQL queries with ANSI SQL support, time-based filtering, and streaming response options.
      - name: Native JSON Query API
        description: Druid-native query format (Timeseries, TopN, GroupBy, Scan, Search) for maximum control and performance.
      - name: Streaming Ingestion
        description: Real-time data ingestion from Apache Kafka and Amazon Kinesis with supervisor-managed offset tracking and exactly-once semantics.
      - name: Batch Ingestion
        description: Parallel batch indexing tasks from local files, S3, GCS, HDFS, and other external storage systems.
      - name: Automatic Rollup
        description: Pre-aggregates metrics at ingestion time to reduce storage and query time, configurable per datasource.
      - name: Time-Based Partitioning
        description: All data is partitioned by time interval (segments), enabling efficient time-range query pruning.
      - name: Multi-Tenancy
        description: Query isolation and resource management via query lanes, scheduler priorities, and row-level access control.
  - type: UseCases
    data:
      - name: Real-Time Event Analytics
        description: Analyze click streams, IoT events, application logs, and user behavior data with sub-second query latency.
      - name: Business Intelligence Dashboards
        description: Power interactive BI dashboards with high-concurrency low-latency queries backed by Druid's columnar engine.
      - name: Network and Security Monitoring
        description: Ingest and analyze network flow data and security events in real time for threat detection and capacity planning.
      - name: Ad Tech Analytics
        description: Process advertising impression, click, and conversion events at high volume with real-time aggregation.
      - name: Operational Analytics
        description: Monitor application performance metrics and operational data with drilldown and filtering capabilities.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: KafkaSupervisor for real-time continuous ingestion from Kafka topics into Druid datasources.
      - name: Amazon Kinesis
        description: KinesisSupervisor for real-time data ingestion from AWS Kinesis data streams.
      - name: Apache Hadoop / HDFS
        description: Native Hadoop batch indexing task for bulk loading data from HDFS or MapReduce job outputs.
      - name: Amazon S3 / GCS
        description: Batch and streaming ingestion from object storage (S3, GCS, Azure Blob) using index tasks.
      - name: Apache Hive
        description: Druid-Hive integration for querying Druid datasources from HiveQL and performing joins.
      - name: Kubernetes
        description: Official Kubernetes operator for deploying and managing Druid clusters on Kubernetes.
      - name: Imply (Commercial)
        description: Imply provides a commercial managed Druid service with additional features and enterprise support.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-druid/refs/heads/main/vocabulary/apache-druid-vocabulary.yaml
---
