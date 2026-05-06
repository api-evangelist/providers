---
aid: apache-pinot
name: Apache Pinot
description: Apache Pinot is a real-time distributed OLAP datastore designed to deliver scalable real-time analytics with low latency. It ingests data from batch and streaming sources and provides fast analytical queries for user-facing applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Database
  - Low Latency
  - OLAP
  - Real-Time
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-pinot/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-pinot:apache-pinot-rest-api
    name: Apache Pinot REST API
    description: The Pinot API provides REST endpoints for SQL queries, schema management, table management, segment management, cluster administration, and task management, along with a JDBC driver for SQL access.
    humanURL: https://docs.pinot.apache.org/
    tags:
      - Analytics
      - OLAP
      - REST
      - SQL
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.pinot.apache.org/
      - type: OpenAPI
        url: openapi/apache-pinot-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/pinot
  - type: Documentation
    url: https://docs.pinot.apache.org/
  - type: SpectralRules
    url: rules/apache-pinot-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-pinot-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/pinot-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-pinot-context.jsonld
  - type: Features
    data:
      - name: Real-Time OLAP
        description: Sub-second analytical queries over real-time and historical data
      - name: SQL Support
        description: Standard SQL query interface with Pinot-specific extensions
      - name: Streaming Ingestion
        description: Real-time data ingestion from Kafka, Kinesis, and Pulsar
      - name: Batch Ingestion
        description: Offline data ingestion from HDFS, S3, GCS, and local files
      - name: Columnar Storage
        description: Column-oriented storage with bitmap indexing for fast queries
      - name: Multi-Tenancy
        description: Tenant isolation for broker and server resources
      - name: Star-Tree Index
        description: Pre-aggregated star-tree index for metric rollup queries
  - type: UseCases
    data:
      - name: User-Facing Analytics
        description: Power user-facing dashboards like LinkedIn Who Viewed Profile
      - name: Real-Time Dashboards
        description: Business intelligence dashboards over streaming data
      - name: Anomaly Detection
        description: Real-time anomaly detection over metric time series
      - name: A/B Testing
        description: Real-time experiment analysis and statistical significance
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Real-time stream ingestion from Kafka topics
      - name: Apache Flink
        description: Flink connector for streaming data into Pinot
      - name: Apache Superset
        description: Visual analytics and dashboards via SQL
      - name: Presto/Trino
        description: Federated query access to Pinot via Presto connector
      - name: Grafana
        description: Grafana data source plugin for Pinot metrics
---
