---
aid: apache-beam
name: Apache Beam
description: Apache Beam is a unified, open-source programming model developed by the Apache Software Foundation for defining both batch and streaming data processing pipelines. It provides a portable API layer that lets developers write pipeline logic once in Java, Python, or Go and deploy it to multiple execution engines (runners) including Apache Flink, Apache Spark, Google Cloud Dataflow, and the direct runner for local testing. The Beam portability framework enables cross-language pipelines and runner-agnostic execution.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Batch Processing
  - Data Pipeline
  - ETL
  - Open Source
  - Python
  - Streaming
  - Unified Model
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-beam/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-beam:apache-beam-sdk
    name: Apache Beam SDK
    description: The Apache Beam SDK provides the programming model for constructing data processing pipelines. Available in Java, Python, and Go, it provides PCollections, PTransforms, and Runners for batch and streaming data processing.
    humanURL: https://beam.apache.org/documentation/
    tags:
      - Batch
      - Pipeline
      - SDK
      - Streaming
    properties:
      - type: Documentation
        url: https://beam.apache.org/documentation/
      - type: APIReference
        url: https://beam.apache.org/releases/pydoc/current/
      - type: GettingStarted
        url: https://beam.apache.org/get-started/wordcount-example/
  - aid: apache-beam:apache-beam-job-service
    name: Apache Beam Job Service API
    description: The Beam Job Service API provides a gRPC-based interface for submitting, managing, and monitoring Apache Beam pipeline jobs on supported runners. It is part of the Beam portability framework and enables cross-runner job management.
    humanURL: https://beam.apache.org/documentation/runtime/environments/
    tags:
      - gRPC
      - Job Management
      - Portability
    properties:
      - type: Documentation
        url: https://beam.apache.org/documentation/runtime/environments/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/beam
  - type: Documentation
    url: https://beam.apache.org/
  - type: GettingStarted
    url: https://beam.apache.org/get-started/
  - type: Tutorials
    url: https://beam.apache.org/get-started/wordcount-example/
  - type: Support
    url: https://beam.apache.org/community/contact-us/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://beam.apache.org/blog/
  - type: SDK
    url: https://pypi.org/project/apache-beam/
    title: Python SDK (PyPI)
  - type: SDK
    url: https://search.maven.org/artifact/org.apache.beam/beam-sdks-java-core
    title: Java SDK (Maven)
  - type: SDK
    url: https://pkg.go.dev/github.com/apache/beam/sdks/v2/go/pkg/beam
    title: Go SDK
  - type: Features
    data:
      - name: Unified Batch and Streaming
        description: Single programming model for both batch and streaming data processing with consistent semantics.
      - name: Runner Portability
        description: Write pipeline logic once and execute on Apache Flink, Spark, Google Dataflow, Samza, or the local direct runner.
      - name: Multi-Language Support
        description: Native SDKs for Java, Python, and Go with cross-language transform support for mixing languages.
      - name: Windowing and Triggers
        description: Flexible windowing (fixed, sliding, session, global) and trigger strategies for streaming data processing.
      - name: I/O Connectors
        description: Built-in connectors for BigQuery, Kafka, Pub/Sub, GCS, HDFS, databases, and many other sources and sinks.
      - name: Beam SQL
        description: SQL-based data processing on Beam PCollections using Apache Calcite for query planning.
      - name: ML Integration
        description: RunInference transform for integrating ML model inference into Beam pipelines with TensorFlow, PyTorch, and sklearn.
      - name: Schema-Aware Processing
        description: Schema inference and typed PCollections for structured data processing with automatic serialization.
      - name: Cross-Language Transforms
        description: Call Java transforms from Python pipelines and vice versa via the Beam portability framework.
      - name: Metrics and Monitoring
        description: Built-in metrics API and integration with runner-specific monitoring dashboards.
  - type: UseCases
    data:
      - name: ETL Pipelines
        description: Extract, transform, and load data between storage systems using portable, reusable pipeline components.
      - name: Real-Time Stream Processing
        description: Process high-throughput event streams with low-latency windowing and triggering strategies.
      - name: Batch Data Analytics
        description: Compute aggregate statistics, joins, and group-by operations on large historical datasets.
      - name: ML Model Inference at Scale
        description: Run ML model inference in distributed pipelines using the RunInference transform.
      - name: Log and Event Processing
        description: Parse, filter, and enrich log events from Kafka or Pub/Sub for operational analytics.
      - name: Data Migration
        description: Migrate data between cloud providers and storage systems using Beam's portable I/O connectors.
  - type: Integrations
    data:
      - name: Google Cloud Dataflow
        description: Managed Apache Beam runner on Google Cloud with autoscaling and monitoring.
      - name: Apache Flink
        description: Apache Flink runner for stateful stream processing with exactly-once semantics.
      - name: Apache Spark
        description: Apache Spark runner for batch and streaming processing on Spark clusters.
      - name: Apache Kafka
        description: Kafka I/O connector for reading and writing Kafka topics in Beam pipelines.
      - name: Google BigQuery
        description: BigQuery I/O connector for reading and writing BigQuery tables in Beam pipelines.
      - name: Apache Hadoop
        description: HDFS I/O connector for reading and writing files on Hadoop HDFS.
      - name: TensorFlow Extended (TFX)
        description: TFX uses Beam as the runtime for ML data validation and preprocessing components.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
