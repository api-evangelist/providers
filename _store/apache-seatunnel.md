---
aid: apache-seatunnel
name: Apache SeaTunnel
description: Apache SeaTunnel is a high-performance, distributed data integration platform that supports real-time and batch data synchronization. It provides a connector API with support for over 100 data sources and sinks.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Integration
  - ETL
  - ELT
  - Batch
  - Streaming
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-seatunnel/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-seatunnel:apache-seatunnel-rest-api
    name: Apache SeaTunnel REST API
    description: SeaTunnel provides a REST API for job management and monitoring, a Connector API for building custom data sources and sinks, and a Transform API for data transformation, supporting over 100 built-in connectors.
    humanURL: https://seatunnel.apache.org/docs/
    tags:
      - Data Integration
      - Job Management
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://seatunnel.apache.org/docs/
      - type: OpenAPI
        url: openapi/apache-seatunnel-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/seatunnel
  - type: Documentation
    url: https://seatunnel.apache.org/
  - type: SpectralRules
    url: rules/apache-seatunnel-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-seatunnel-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/seatunnel-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-seatunnel-context.jsonld
  - type: Features
    data:
      - name: 200+ Connectors
        description: Over 200 built-in connectors for databases, warehouses, and file systems
      - name: Batch and Streaming
        description: Unified API for both batch ETL and real-time streaming jobs
      - name: Schema Evolution
        description: Automatic schema detection and evolution support
      - name: Distributed Execution
        description: Zeta execution engine with no external dependencies
      - name: CDC Support
        description: Change Data Capture for real-time database synchronization
      - name: Transform Layer
        description: Built-in SQL and custom transform functions
  - type: UseCases
    data:
      - name: Database Migration
        description: Migrate data between databases with schema mapping
      - name: Data Warehouse Loading
        description: Load and sync data into data warehouses
      - name: Real-Time Synchronization
        description: CDC-based real-time sync between source and target systems
      - name: Data Lake Ingestion
        description: Ingest data from multiple sources into a data lake
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Kafka source and sink connector for streaming pipelines
      - name: Apache Flink
        description: Run SeaTunnel jobs on Flink execution engine
      - name: Apache Spark
        description: Run SeaTunnel jobs on Spark execution engine
      - name: ClickHouse
        description: High-performance ClickHouse sink connector
      - name: Doris
        description: Apache Doris connector for analytical workloads
---
