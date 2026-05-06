---
aid: apache-hive
name: Apache Hive
description: Apache Hive is a data warehouse software that facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. It provides a SQL-like interface called HiveQL for querying data stored in Hadoop, along with a WebHCat REST API for job submission and metastore access.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Big Data
  - Data Warehouse
  - ETL
  - Hadoop
  - Open Source
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-hive/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-hive:apache-hive-webhcat-api
    name: Apache Hive WebHCat REST API
    description: WebHCat (Templeton) REST API for Apache Hive providing DDL operations, HiveQL job submission, and Hive Metastore metadata access over HTTP.
    humanURL: https://cwiki.apache.org/confluence/display/Hive/WebHCat
    baseURL: http://localhost:50111/templeton/v1
    tags:
      - Databases
      - Jobs
      - Metastore
      - REST
      - Tables
    properties:
      - type: Documentation
        url: https://cwiki.apache.org/confluence/display/Hive/WebHCat
      - type: OpenAPI
        url: openapi/apache-hive-webhcat-openapi.yml
      - type: JSONSchema
        url: json-schema/hive-webhcat-table-schema.json
      - type: JSON-LD
        url: json-ld/apache-hive-webhcat-context.jsonld
  - aid: apache-hive:apache-hive-jdbc
    name: Apache Hive JDBC API
    description: JDBC interface to HiveServer2 for standard SQL client connectivity, supporting parameterized queries, result sets, and connection pooling from Java and ODBC-bridge applications.
    humanURL: https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-JDBC
    tags:
      - JDBC
      - SQL
      - SDK
    properties:
      - type: Documentation
        url: https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-JDBC
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.hive/hive-jdbc
        title: Java JDBC Driver (Maven Central)
common:
  - type: Documentation
    url: https://cwiki.apache.org/confluence/display/Hive/Home
  - type: GettingStarted
    url: https://cwiki.apache.org/confluence/display/Hive/GettingStarted
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/hive
  - type: SpectralRules
    url: rules/apache-hive-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-hive-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/hive-data-querying.yaml
  - type: Features
    data:
      - name: HiveQL SQL Interface
        description: SQL-like query language for reading, writing, and aggregating data stored in distributed storage.
      - name: WebHCat REST API
        description: HTTP REST API (Templeton) for DDL operations, job submission, and metastore metadata access.
      - name: HiveServer2 JDBC/ODBC
        description: Thrift-based server with JDBC and ODBC drivers for standard SQL client connectivity.
      - name: Hive Metastore
        description: Central repository for table schema, partition metadata, and storage location information.
      - name: Partitioning
        description: Partition tables by column values for efficient query pruning and data organization.
      - name: ORC and Parquet Storage
        description: Optimized columnar storage formats with predicate pushdown and compression support.
      - name: ACID Transactions
        description: Full ACID transaction support for inserts, updates, and deletes on managed ORC tables.
      - name: Vectorized Query Execution
        description: Batch processing of rows in CPU register-width vectors for improved query throughput.
  - type: UseCases
    data:
      - name: Data Warehouse Analytics
        description: Run SQL analytics on petabyte-scale datasets stored in HDFS or object storage.
      - name: ETL Pipeline Orchestration
        description: Use HiveQL scripts to transform and load data between raw and curated data lake zones.
      - name: Ad-Hoc Data Exploration
        description: Query structured data interactively using Beeline or JDBC-connected BI tools.
      - name: Log Analysis
        description: Parse and aggregate application logs stored as text or JSON in HDFS using Hive SerDes.
      - name: Data Catalog Integration
        description: Use the Hive Metastore as a shared schema registry for Spark, Flink, and Presto.
  - type: Integrations
    data:
      - name: Apache Hadoop HDFS
        description: Hive reads and writes data stored in HDFS as the primary storage layer.
      - name: Apache Spark
        description: Spark uses the Hive Metastore for table discovery and supports Hive UDFs.
      - name: Apache HBase
        description: Hive HBase storage handler enables HiveQL queries against HBase tables.
      - name: Apache Tez
        description: Apache Tez DAG execution engine replaces MapReduce for faster Hive query processing.
      - name: Presto / Trino
        description: Presto and Trino use the Hive Metastore for table metadata in federated SQL queries.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
