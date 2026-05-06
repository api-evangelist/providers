---
aid: apache-kylin
name: Apache Kylin
description: Apache Kylin is an open-source distributed analytics engine designed to provide a SQL interface and multi-dimensional analysis (OLAP) on large-scale datasets. It provides sub-second query latency on trillion-record datasets via pre-computed cubes and works on top of Hadoop, Spark, and cloud storage.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Big Data
  - Cube
  - OLAP
  - Open Source
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-kylin/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-kylin:rest-api
    name: Apache Kylin REST API
    description: The Kylin REST API provides endpoints for SQL query execution, model management, project management, job management, and table management for administering the Kylin OLAP engine.
    humanURL: https://kylin.apache.org/docs/restapi/
    tags:
      - JDBC
      - OLAP
      - REST
      - SQL
    properties:
      - type: Documentation
        url: https://kylin.apache.org/docs/restapi/
      - type: OpenAPI
        url: openapi/apache-kylin-rest-api.yaml
  - aid: apache-kylin:jdbc-driver
    name: Apache Kylin JDBC Driver
    description: The Kylin JDBC driver provides SQL-over-Kylin access for BI tools and SQL clients, enabling standard JDBC connectivity to Kylin OLAP cubes.
    humanURL: https://kylin.apache.org/docs/tutorial/jdbc.html
    tags:
      - JDBC
      - SQL
    properties:
      - type: Documentation
        url: https://kylin.apache.org/docs/tutorial/jdbc.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/kylin
  - type: Documentation
    url: https://kylin.apache.org/docs/
  - type: GettingStarted
    url: https://kylin.apache.org/docs/tutorial/kylin_sample.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://kylin.apache.org/download/
  - type: SpectralRules
    url: rules/apache-kylin-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-kylin-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/olap-analytics.yaml
  - type: Features
    data:
      - name: Sub-Second OLAP Queries
        description: Pre-computed cubes enable sub-second query response on trillion-record datasets.
      - name: SQL Interface
        description: ANSI SQL interface for business analysts using existing SQL skills.
      - name: Cube Pre-computation
        description: Build cubes with aggregates pre-calculated for instant query response.
      - name: Hadoop and Cloud Integration
        description: Works on top of Hadoop, Spark, and cloud object storage.
      - name: JDBC/ODBC Drivers
        description: Standard JDBC and ODBC drivers for BI tool integration.
      - name: Segment Management
        description: Incremental cube building with date-range segment management.
      - name: Multi-Tenancy
        description: Project-based multi-tenancy for isolating datasets and access.
  - type: UseCases
    data:
      - name: Data Warehouse Query Acceleration
        description: Accelerate slow Hive or Spark queries with Kylin cube pre-computation.
      - name: BI Tool Integration
        description: Connect Tableau, PowerBI, and Superset to Kylin via JDBC for analytics.
      - name: Real-Time OLAP
        description: Stream data into Kylin incrementally for near-real-time OLAP analytics.
      - name: Large-Scale Reporting
        description: Generate business reports over trillion-record datasets in seconds.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Reads from HDFS and executes MapReduce cube builds on Hadoop.
      - name: Apache Spark
        description: Spark-based cube building for faster and more efficient data processing.
      - name: Apache Hive
        description: Hive metastore integration for table schema and metadata.
      - name: Apache HBase
        description: HBase storage for pre-computed cube data.
      - name: Tableau
        description: Native Tableau connector via Kylin JDBC driver.
      - name: Apache Superset
        description: Apache Superset integration via JDBC for self-service analytics.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
