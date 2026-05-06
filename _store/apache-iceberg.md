---
aid: apache-iceberg
name: Apache Iceberg
description: Apache Iceberg is an open table format for large analytic datasets that provides ACID transactions, schema evolution, hidden partitioning, and time travel. It works with Spark, Flink, Hive, Presto, Trino, DuckDB, ClickHouse, and many more compute engines. Governed by the Apache Software Foundation under the Apache 2.0 license.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ACID
  - Analytics
  - Apache
  - Data Lake
  - Lakehouse
  - Open Source
  - Table Format
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-iceberg/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-iceberg:rest-catalog-api
    name: Apache Iceberg REST Catalog API
    description: The Iceberg REST Catalog API defines the specification for catalog server implementations, enabling table discovery, creation, metadata management, namespace management, and multi-table transactions over HTTP. It is the standard integration point for compute engines connecting to Iceberg catalogs.
    humanURL: https://iceberg.apache.org/rest-catalog-spec/
    tags:
      - Catalog
      - Namespace
      - REST
      - Table Format
    properties:
      - type: Documentation
        url: https://iceberg.apache.org/rest-catalog-spec/
      - type: OpenAPI
        url: openapi/apache-iceberg-rest-catalog-open-api.yaml
  - aid: apache-iceberg:java-api
    name: Apache Iceberg Java API
    description: The Iceberg Java API provides programmatic access to table operations, schema management, partition management, and catalog implementations. It is the primary library for integrating Iceberg with JVM-based compute engines including Spark, Flink, Hive, Trino, and Presto.
    humanURL: https://iceberg.apache.org/javadoc/latest/
    tags:
      - Java
      - JVM
      - SDK
      - Table Format
    properties:
      - type: Documentation
        url: https://iceberg.apache.org/javadoc/latest/
      - type: GettingStarted
        url: https://iceberg.apache.org/docs/latest/java-api-quickstart/
  - aid: apache-iceberg:python-api
    name: PyIceberg Python API
    description: PyIceberg is the official Python implementation of the Apache Iceberg table specification. It provides programmatic access to Iceberg table metadata and data, with integrations for PyArrow, Pandas, DuckDB, Ray, Polars, and multiple catalog backends.
    humanURL: https://py.iceberg.apache.org/
    tags:
      - Python
      - SDK
      - Table Format
    properties:
      - type: Documentation
        url: https://py.iceberg.apache.org/
      - type: SDK
        url: https://pypi.org/project/pyiceberg/
      - type: GitHubRepository
        url: https://github.com/apache/iceberg-python
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/iceberg
  - type: Documentation
    url: https://iceberg.apache.org/docs/latest/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Blog
    url: https://iceberg.apache.org/blogs/
  - type: YouTube
    url: https://www.youtube.com/@ApacheIceberg
  - type: Versioning
    url: https://iceberg.apache.org/releases/
  - type: ReleaseNotes
    url: https://iceberg.apache.org/releases/
  - type: SpectralRules
    url: rules/apache-iceberg-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-iceberg-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/catalog-management.yaml
  - type: Features
    data:
      - name: ACID Transactions
        description: Full ACID transaction support with serializable isolation for concurrent readers and writers.
      - name: Schema Evolution
        description: Add, drop, update, or rename columns without rewriting existing data files.
      - name: Hidden Partitioning
        description: Automatic partition management that prevents common user mistakes and silently incorrect results.
      - name: Partition Evolution
        description: Change partition layout over time without rewriting existing data.
      - name: Time Travel
        description: Query historical snapshots of tables and roll back to any prior version.
      - name: Row-Level Updates
        description: Supports upserts, deletes, and updates at the row level via merge-on-read and copy-on-write modes.
      - name: Multi-Engine Support
        description: Works with Spark, Flink, Hive, Trino, Presto, Impala, DuckDB, ClickHouse, and more.
      - name: Cloud-Native Storage
        description: Native support for S3, ADLS, GCS, and HDFS with no filesystem dependencies.
  - type: UseCases
    data:
      - name: Lakehouse Analytics
        description: Build open lakehouse architectures with ACID guarantees across petabyte-scale datasets.
      - name: Real-Time Data Pipelines
        description: Stream data into Iceberg tables via Flink or Kafka Connect with exactly-once semantics.
      - name: Data Versioning and Auditing
        description: Use time travel to audit historical data states and implement regulatory compliance.
      - name: Multi-Engine Query Federation
        description: Query the same Iceberg tables from multiple engines (Spark, Trino, DuckDB) without data duplication.
      - name: Cloud Data Migration
        description: Migrate on-premises Hive workloads to cloud-native Iceberg tables with full compatibility.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Full read/write support for Iceberg tables in Spark batch and streaming workloads.
      - name: Apache Flink
        description: Streaming and batch integration with exactly-once write support.
      - name: Apache Hive
        description: Read and write Iceberg tables from Hive queries using the Iceberg Hive integration.
      - name: Trino
        description: Query Iceberg tables from Trino with full partition pruning and predicate pushdown.
      - name: AWS Glue Catalog
        description: Use AWS Glue as the Iceberg catalog backend with full metadata management.
      - name: AWS Athena
        description: Query Iceberg tables stored in S3 using Amazon Athena.
      - name: Project Nessie
        description: Git-like catalog branching and versioning via Nessie catalog integration.
      - name: DuckDB
        description: Local analytics on Iceberg tables via the DuckDB Iceberg extension.
      - name: ClickHouse
        description: Query Iceberg tables from ClickHouse via the ClickHouse Iceberg integration.
      - name: Snowflake
        description: Access Iceberg tables managed in Snowflake's Polaris catalog.
      - name: Google BigQuery
        description: Use BigQuery as a compute engine over Iceberg tables with BigLake Metastore.
      - name: Databricks
        description: Create and query Iceberg tables on Databricks using Unity Catalog.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
