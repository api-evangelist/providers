---
aid: apache-hbase
name: Apache HBase
description: Apache HBase is an open-source, distributed, versioned, non-relational database modeled after Google's Bigtable. It provides random, real-time read/write access to big data and runs on top of Apache Hadoop HDFS, offering a REST API (Stargate), Thrift API, and Java client API for table and cell-level operations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Big Data
  - Bigtable
  - Database
  - Hadoop
  - NoSQL
  - Open Source
  - Wide Column
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-hbase/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-hbase:apache-hbase-rest-api
    name: Apache HBase REST API
    description: REST API (Stargate) for Apache HBase distributed NoSQL database, providing table management, row and cell operations, and table scanning via HTTP with JSON or XML encoding.
    humanURL: https://hbase.apache.org/book.html#_rest
    baseURL: http://localhost:8080
    tags:
      - Cells
      - NoSQL
      - REST
      - Rows
      - Tables
    properties:
      - type: Documentation
        url: https://hbase.apache.org/book.html#_rest
      - type: OpenAPI
        url: openapi/apache-hbase-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/hbase-rest-tableschema-schema.json
      - type: JSON-LD
        url: json-ld/apache-hbase-rest-context.jsonld
  - aid: apache-hbase:apache-hbase-java-api
    name: Apache HBase Java Client API
    description: Java client API for all HBase data operations including table administration, filters, coprocessors, batch operations, and async client for high-throughput workloads.
    humanURL: https://hbase.apache.org/apidocs/
    tags:
      - Java
      - NoSQL
      - SDK
    properties:
      - type: Documentation
        url: https://hbase.apache.org/apidocs/
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.hbase/hbase-client
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://hbase.apache.org/book.html
  - type: GettingStarted
    url: https://hbase.apache.org/book.html#quickstart
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/hbase
  - type: SpectralRules
    url: rules/apache-hbase-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-hbase-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/hbase-data-access.yaml
  - type: Features
    data:
      - name: Wide-Column NoSQL Storage
        description: Store sparse, semi-structured data in a distributed wide-column table model inspired by Google Bigtable.
      - name: REST API (Stargate)
        description: HTTP REST gateway for language-agnostic table and row operations using JSON or XML.
      - name: Thrift API
        description: High-performance Thrift interface for cross-language HBase access with compact binary encoding.
      - name: Row-Level Consistency
        description: Strong consistency guarantees for single-row get, put, and delete operations.
      - name: Coprocessors
        description: Server-side coprocessor framework for custom observers and endpoints analogous to stored procedures.
      - name: HBase Shell
        description: JRuby-based interactive shell for administrative and data manipulation operations.
      - name: Scanner API
        description: Flexible server-side scan API with filters, time ranges, and column family projections.
      - name: Replication
        description: Asynchronous multi-cluster replication for disaster recovery and geographic distribution.
  - type: UseCases
    data:
      - name: Time-Series Data Storage
        description: Store high-velocity time-series sensor or log data with row keys designed for time range scans.
      - name: Event Logging
        description: Persist event streams from web applications or IoT devices for analytics and audit.
      - name: User Profile Storage
        description: Store sparse user profile attributes at scale with efficient random access by user ID.
      - name: Graph Storage Backend
        description: Use HBase as a backend storage engine for graph databases like Apache TinkerPop/JanusGraph.
      - name: Machine Learning Feature Store
        description: Store and serve pre-computed ML features at low latency for online prediction.
  - type: Integrations
    data:
      - name: Apache Hadoop HDFS
        description: HBase uses HDFS as its underlying distributed file system for WAL and HFile storage.
      - name: Apache Phoenix
        description: SQL skin over HBase providing JDBC access, secondary indexes, and query optimization.
      - name: Apache Spark
        description: Spark-HBase connector for reading and writing HBase tables as Spark DataFrames.
      - name: Apache Hive
        description: HBase storage handler for using HBase tables as external Hive tables.
      - name: Apache Flink
        description: Flink HBase connector for reading and writing HBase tables in streaming pipelines.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
