---
aid: apache-flink
name: Apache Flink
description: Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. It provides a REST API for job management, cluster operations, metrics collection, and checkpoint management for real-time streaming and batch processing workloads.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Batch Processing
  - Big Data
  - Open Source
  - Real-Time Analytics
  - Stateful Computing
  - Stream Processing
url: https://raw.githubusercontent.com/api-evangelist/apache-flink/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apache-flink:apache-flink-rest-api
    name: Apache Flink REST API
    description: The REST API provides programmatic access to monitor and control Flink jobs and clusters. It supports job submission, cluster management, metrics retrieval, checkpoint management, and TaskManager administration.
    humanURL: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
    baseURL: http://localhost:8081
    tags:
      - Big Data
      - Distributed Computing
      - Job Management
      - Real-Time Processing
      - REST API
      - Streaming
    properties:
      - type: Documentation
        url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
      - type: OpenAPI
        url: openapi/apache-flink-rest-openapi-original.yml
      - type: JSONSchema
        url: json-schema/flink-rest-job-details-info-schema.json
      - type: JSON-LD
        url: json-ld/apache-flink-rest-context.jsonld
  - aid: apache-flink:apache-flink-monitoring
    name: Apache Flink Monitoring API
    description: Monitoring REST API for accessing job metrics, checkpoints, and cluster statistics for Apache Flink deployments.
    humanURL: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/monitoring/
    baseURL: http://localhost:8081
    tags:
      - Metrics
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/monitoring/
      - type: Documentation
        url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/metrics/
        title: Metrics Reference
common:
  - type: GettingStarted
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/local_installation/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/flink
  - type: Blog
    url: https://flink.apache.org/blog/
  - type: Support
    url: https://flink.apache.org/community.html
  - type: Training
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-flink
  - type: X
    url: https://twitter.com/apacheflink
  - type: SpectralRules
    url: rules/apache-flink-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-flink-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/flink-job-management.yaml
  - type: Features
    data:
      - name: Unified Stream and Batch Processing
        description: Single engine for both unbounded stream processing and bounded batch workloads with a unified API.
      - name: Stateful Computations
        description: Rich stateful processing with managed state backends (RocksDB, heap), exactly-once guarantees, and state versioning.
      - name: Exactly-Once Semantics
        description: End-to-end exactly-once processing guarantees with distributed snapshots and transactional sinks.
      - name: Event Time Processing
        description: Native event-time support with watermarks for out-of-order event handling in streaming workloads.
      - name: Checkpointing and Savepoints
        description: Automatic fault-tolerance via checkpointing and manual savepoints for job migration and upgrades.
      - name: High Availability
        description: JobManager HA via ZooKeeper or Kubernetes for zero-downtime cluster operations.
      - name: Scalable Architecture
        description: Horizontally scalable TaskManagers with fine-grained resource management and dynamic slot allocation.
      - name: REST API Management
        description: Comprehensive REST API for job submission, monitoring, metrics collection, and cluster administration.
      - name: SQL and Table API
        description: Declarative SQL and Table API for streaming analytics with connector ecosystem support.
  - type: UseCases
    data:
      - name: Real-Time Analytics
        description: Process and analyze event streams in real time for dashboards, alerts, and operational intelligence.
      - name: ETL Pipelines
        description: Build scalable ETL pipelines for data lake ingestion, transformation, and enrichment.
      - name: Fraud Detection
        description: Detect fraudulent transactions in real time using stateful pattern matching over event streams.
      - name: IoT Data Processing
        description: Process high-volume IoT device telemetry with stateful aggregations and time-window computations.
      - name: Machine Learning Inference
        description: Serve ML model predictions at scale with streaming feature computation and online inference.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Kafka source and sink connectors for high-throughput event streaming ingestion and output.
      - name: Apache Hadoop / HDFS
        description: HDFS integration for batch data reading and writing in distributed storage.
      - name: Apache Hive
        description: Hive catalog integration and batch SQL queries over Hive tables.
      - name: Kubernetes
        description: Native Kubernetes deployment with FlinkDeployment CRD and the Flink Kubernetes Operator.
      - name: Apache Iceberg
        description: Iceberg table format integration for lakehouse workloads with ACID guarantees.
      - name: Elasticsearch
        description: Elasticsearch sink connector for real-time search index updates from Flink jobs.
      - name: Amazon Kinesis
        description: Kinesis source and sink connectors for AWS-native streaming pipelines.
maintainers:
  - FN: Apache Software Foundation
    email: user@flink.apache.org
---
