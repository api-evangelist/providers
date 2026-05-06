---
aid: apache-hudi
name: Apache Hudi
description: Apache Hudi is a data lake platform that provides incremental data processing primitives including upserts and incremental queries. It manages storage of large analytical datasets on distributed file systems with ACID transactions, timeline-based versioning, and integrations for Spark, Flink, and Hive.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ACID
  - Apache
  - Big Data
  - Data Lake
  - Incremental Processing
  - Lakehouse
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-hudi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-hudi:apache-hudi-timeline-api
    name: Apache Hudi Timeline Server API
    description: REST API for the Apache Hudi Timeline Server providing table timeline management, commit metadata inspection, and table administration for Hudi data lake tables.
    humanURL: https://hudi.apache.org/docs/timeline
    baseURL: http://localhost:9090
    tags:
      - Commits
      - Data Lake
      - REST
      - Tables
      - Timeline
    properties:
      - type: Documentation
        url: https://hudi.apache.org/docs/timeline
      - type: OpenAPI
        url: openapi/apache-hudi-timeline-openapi.yml
      - type: JSONSchema
        url: json-schema/hudi-huditableconfig-schema.json
      - type: JSON-LD
        url: json-ld/apache-hudi-timeline-context.jsonld
  - aid: apache-hudi:apache-hudi-java-api
    name: Apache Hudi Java API
    description: Java API for writing Hudi tables with upserts, inserts, and deletes, plus timeline management, compaction, and Spark/Flink DataSource integration APIs.
    humanURL: https://hudi.apache.org/docs/writing_data
    tags:
      - Java
      - SDK
      - Spark
      - Flink
    properties:
      - type: Documentation
        url: https://hudi.apache.org/docs/writing_data
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.hudi/hudi-spark3.5-bundle_2.12
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://hudi.apache.org/docs/overview
  - type: GettingStarted
    url: https://hudi.apache.org/docs/quick-start-guide
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/hudi
  - type: SpectralRules
    url: rules/apache-hudi-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-hudi-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/hudi-lakehouse-management.yaml
  - type: Features
    data:
      - name: ACID Upserts
        description: Atomically insert or update records in data lake tables with ACID guarantees using record keys.
      - name: Hudi Timeline
        description: Immutable commit timeline tracking all mutations for time travel, rollback, and incremental queries.
      - name: Incremental Queries
        description: Query only the data changed since a given commit timestamp for efficient streaming ingestion.
      - name: Copy-On-Write Tables
        description: COW table type rewrites entire Parquet files on upsert for read-optimized query performance.
      - name: Merge-On-Read Tables
        description: MOR table type appends delta logs for fast writes with compaction-based read optimization.
      - name: Table Services
        description: Built-in cleaning, compaction, clustering, and indexing services for table maintenance.
      - name: Multi-Engine Support
        description: Read and write Hudi tables from Apache Spark, Flink, Hive, Presto, Trino, and Athena.
      - name: Schema Evolution
        description: Support for adding, renaming, and dropping columns with backward-compatible schema evolution.
  - type: UseCases
    data:
      - name: CDC Pipeline Ingestion
        description: Ingest change data capture (CDC) events from databases into data lake tables with upsert support.
      - name: Streaming Data Lake
        description: Build near-real-time data lake pipelines with Spark Structured Streaming or Flink.
      - name: Data Lake Maintenance
        description: Manage storage costs with automated cleaning, compaction, and clustering of Hudi tables.
      - name: Incremental ETL
        description: Build incremental ETL pipelines that process only changed data since the last run.
      - name: Regulatory Data Retention
        description: Implement GDPR right-to-erasure by deleting records from Hudi tables with delete operations.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Primary write and read engine with Hudi DataSource and Spark SQL extensions.
      - name: Apache Flink
        description: Flink sink and source connectors for streaming writes and incremental reads.
      - name: Apache Hive
        description: Hive Metastore sync for making Hudi tables queryable from HiveQL.
      - name: Presto / Trino
        description: Native Hudi input format support for querying Hudi tables from Presto and Trino.
      - name: AWS Athena
        description: Athena supports reading Hudi COW and MOR tables stored in Amazon S3.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
