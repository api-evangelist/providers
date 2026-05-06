---
aid: apache-samza
name: Apache Samza
description: Apache Samza is a distributed stream processing framework that provides a simple API for building stateful stream processing applications. It integrates with Apache Kafka for messaging and supports both stream and batch processing.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Hadoop
  - Kafka
  - Stream Processing
  - Streaming
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-samza/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-samza:apache-samza
    name: Apache Samza
    description: Samza provides a high-level Streams API and low-level Task API in Java/Scala for stateful stream processing, with a REST API for job management and integration with Kafka, HDFS, and other data systems.
    humanURL: https://samza.apache.org/learn/documentation/latest/
    tags:
      - Job Management
      - REST
      - Stream Processing
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://samza.apache.org/learn/documentation/latest/
      - type: Documentation
        url: https://samza.apache.org/learn/documentation/
      - type: OpenAPI
        url: openapi/apache-samza-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/samza
  - type: Documentation
    url: https://samza.apache.org/
  - type: SpectralRules
    url: rules/apache-samza-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-samza-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/samza-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-samza-context.jsonld
  - type: Features
    data:
      - name: Kafka Integration
        description: Native Apache Kafka consumer/producer for stream processing
      - name: YARN Execution
        description: Runs on Apache YARN for resource management and fault tolerance
      - name: Stateful Processing
        description: Local state stores with RocksDB for low-latency stateful computations
      - name: Exactly-Once Processing
        description: Transactional state stores for exactly-once semantics
      - name: Flexible Deployment
        description: Run on YARN, Kubernetes, or standalone
      - name: High Level API
        description: Fluent API and SQL support for stream transformations
  - type: UseCases
    data:
      - name: Event Stream Processing
        description: Real-time processing of Kafka event streams
      - name: Stateful Aggregations
        description: Windowed aggregations over streaming data
      - name: Stream Joins
        description: Join multiple Kafka streams for enrichment
      - name: Change Data Capture
        description: Process CDC events from databases in real time
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Primary messaging system for Samza input and output streams
      - name: Apache YARN
        description: Resource management and job scheduling on Hadoop
      - name: Apache Hadoop
        description: HDFS integration for checkpoint storage
      - name: RocksDB
        description: Embedded state store for local stateful processing
---
