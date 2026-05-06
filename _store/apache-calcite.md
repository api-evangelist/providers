---
aid: apache-calcite
name: Apache Calcite
description: Apache Calcite is a dynamic data management framework developed by the Apache Software Foundation that provides SQL parsing, query planning and optimization, and data federation capabilities. It serves as the SQL engine and query optimizer for many big data systems including Apache Hive, Druid, Flink, Kafka Streams, and others. Calcite provides a Java API for embedding SQL capabilities into applications, a JDBC adapter for connecting heterogeneous data sources, and an extensible relational algebra framework for building custom query optimizers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Data Federation
  - Framework
  - Open Source
  - Query Optimization
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-calcite/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-calcite:apache-calcite-java-api
    name: Apache Calcite Java API
    description: The Apache Calcite Java API provides SQL parsing, validation, query planning, and optimization capabilities for embedding in JVM applications. It exposes a relational algebra framework and pluggable optimizer rules for building custom query engines.
    humanURL: https://calcite.apache.org/docs/
    tags:
      - Java
      - Query Engine
      - SQL
    properties:
      - type: Documentation
        url: https://calcite.apache.org/docs/
      - type: APIReference
        url: https://calcite.apache.org/javadocAggregate/
      - type: GettingStarted
        url: https://calcite.apache.org/docs/tutorial.html
  - aid: apache-calcite:apache-calcite-jdbc-api
    name: Apache Calcite JDBC API
    description: The Apache Calcite JDBC adapter provides a standard JDBC interface over heterogeneous data sources. Applications use it to issue SQL queries across multiple data formats and storage systems through a unified SQL interface.
    humanURL: https://calcite.apache.org/docs/adapter.html
    tags:
      - JDBC
      - SQL
    properties:
      - type: Documentation
        url: https://calcite.apache.org/docs/adapter.html
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.calcite/calcite-core
  - aid: apache-calcite:apache-calcite-avatica-api
    name: Apache Calcite Avatica API
    description: Apache Avatica is a framework for building database drivers derived from Apache Calcite. It provides a JSON/Protobuf-over-HTTP remote protocol for JDBC clients to connect to Calcite-based query engines.
    humanURL: https://calcite.apache.org/avatica/docs/
    tags:
      - Avatica
      - HTTP
      - JDBC
    properties:
      - type: Documentation
        url: https://calcite.apache.org/avatica/docs/
      - type: APIReference
        url: https://calcite.apache.org/avatica/javadocAggregate/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/calcite
  - type: Documentation
    url: https://calcite.apache.org/
  - type: GettingStarted
    url: https://calcite.apache.org/docs/tutorial.html
  - type: Support
    url: https://calcite.apache.org/community/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://github.com/apache/calcite/releases
  - type: SDK
    url: https://search.maven.org/artifact/org.apache.calcite/calcite-core
    title: Java SDK (Maven)
  - type: Vocabulary
    url: vocabulary/apache-calcite-vocabulary.yaml
  - type: Features
    data:
      - name: SQL Parsing and Validation
        description: Parse and validate SQL queries using an extensible SQL grammar with support for SQL:2003 and beyond.
      - name: Query Optimization
        description: Cost-based and rule-based query optimization using a volcano-style optimizer with pluggable optimization rules.
      - name: Relational Algebra
        description: Extensible relational algebra framework for representing and transforming query plans as expression trees.
      - name: Data Federation
        description: Federate queries across heterogeneous data sources including CSV, JSON, JDBC databases, and Elasticsearch.
      - name: Adapter Framework
        description: Pluggable adapter API for connecting new data sources to the Calcite SQL engine.
      - name: Materialized Views
        description: Automatic materialized view recognition and query rewriting for query acceleration.
      - name: Streaming SQL
        description: SQL extensions for querying streaming data sources with window functions and temporal predicates.
      - name: Lattices and Tiles
        description: Summary table recommendation and query rewriting using lattice structures for OLAP workloads.
      - name: JDBC Driver
        description: Standard JDBC driver for issuing SQL queries against Calcite-connected data sources.
      - name: Avatica Remote Protocol
        description: JSON/Protobuf-over-HTTP remote JDBC protocol for connecting clients to Calcite-based query servers.
  - type: UseCases
    data:
      - name: Embedding SQL in Applications
        description: Add SQL querying capability to Java applications using the Calcite Java API without a full database.
      - name: Building Query Engines
        description: Use Calcite as the SQL parsing and optimization layer in custom query engine implementations.
      - name: Data Virtualization
        description: Federate queries across multiple heterogeneous data sources using Calcite adapters.
      - name: OLAP Query Optimization
        description: Accelerate analytical queries using materialized view rewriting and lattice-based summary tables.
      - name: SQL Dialect Translation
        description: Parse SQL in one dialect and transpile it to another using Calcite's SQL generation framework.
  - type: Integrations
    data:
      - name: Apache Flink
        description: Flink uses Calcite for SQL parsing and query optimization in Flink SQL and Table API.
      - name: Apache Hive
        description: Hive uses Calcite for cost-based query optimization in HiveQL query planning.
      - name: Apache Druid
        description: Druid uses Calcite for SQL query parsing and planning against its time-series data store.
      - name: Apache Kafka
        description: ksqlDB and Kafka Streams use Calcite for SQL stream processing query planning.
      - name: Apache Beam
        description: Beam SQL uses Calcite for query planning on PCollection-based streaming and batch pipelines.
      - name: Elasticsearch
        description: Calcite provides a SQL adapter for querying Elasticsearch indices using standard SQL.
      - name: Apache Kylin
        description: Kylin uses Calcite as its SQL engine for OLAP cube query planning and execution.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
