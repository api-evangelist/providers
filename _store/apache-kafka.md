---
aid: apache-kafka
name: Apache Kafka
description: Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. It provides a REST Proxy API, Kafka Connect REST API, and AsyncAPI for event streaming.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Systems
  - Event Streaming
  - Messaging
  - Open Source
  - Pub-Sub
created: '2025-06-05'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-kafka:kafka-rest-proxy-api
    name: Kafka REST Proxy API
    description: The Kafka REST Proxy provides a RESTful interface to a Kafka cluster for producing and consuming messages, managing topics, partitions, consumer groups, and viewing cluster state without native Kafka clients.
    humanURL: https://docs.confluent.io/platform/current/kafka-rest/
    baseURL: http://localhost:8082
    tags:
      - Consumer Groups
      - Proxy
      - REST
      - Topics
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/kafka-rest/api.html
      - type: OpenAPI
        url: openapi/kafka-rest-proxy.yml
  - aid: apache-kafka:kafka-connect-api
    name: Kafka Connect REST API
    description: Kafka Connect REST API for managing connectors, their configurations, tasks, and offsets for integrating Kafka with external data systems including databases, object stores, and search indexes.
    humanURL: https://kafka.apache.org/documentation/#connect_rest
    baseURL: http://localhost:8083
    tags:
      - Connect
      - Connectors
      - Integration
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/#connect_rest
      - type: OpenAPI
        url: openapi/kafka-connect.yml
  - aid: apache-kafka:kafka-messaging-api
    name: Apache Kafka Messaging API
    description: The core Kafka messaging protocol for producing and consuming records to/from topics using the native Kafka binary protocol, supporting exactly-once semantics, compaction, and partitioned log storage.
    humanURL: https://kafka.apache.org/documentation/#producerapi
    tags:
      - Messaging
      - Pub-Sub
      - Streaming
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/
      - type: AsyncAPI
        url: asyncapi/kafka-messaging.yml
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/kafka
  - type: Documentation
    url: https://kafka.apache.org/documentation/
  - type: GettingStarted
    url: https://kafka.apache.org/quickstart
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://kafka.apache.org/downloads
  - type: SpectralRules
    url: rules/apache-kafka-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-kafka-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/event-streaming.yaml
  - type: Features
    data:
      - name: High Throughput
        description: Handle millions of messages per second with low latency at massive scale.
      - name: Exactly-Once Semantics
        description: Guarantee exactly-once message delivery with idempotent producers and transactional APIs.
      - name: Distributed Replication
        description: Automatic replication across brokers for fault tolerance and high availability.
      - name: Stream Processing
        description: Real-time stream processing via Kafka Streams library and KSQL.
      - name: Connector Ecosystem
        description: 200+ pre-built Kafka Connect connectors for databases, clouds, and SaaS.
      - name: Log Compaction
        description: Retain the latest value for each key with topic log compaction.
      - name: Consumer Groups
        description: Horizontally scalable consumers with automatic partition rebalancing.
  - type: UseCases
    data:
      - name: Event-Driven Architecture
        description: Build event-driven microservices with reliable message delivery.
      - name: Data Pipeline
        description: Move data between systems at scale with exactly-once delivery guarantees.
      - name: Real-Time Analytics
        description: Process and analyze event streams in real time with Kafka Streams.
      - name: Log Aggregation
        description: Centralize application and infrastructure logs for analysis and alerting.
      - name: CDC (Change Data Capture)
        description: Capture database changes and stream them to data warehouses and caches.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Spark Structured Streaming integration for batch and streaming analytics.
      - name: Apache Flink
        description: Native Flink Kafka connector for low-latency stream processing.
      - name: Debezium
        description: CDC platform using Kafka Connect to capture database change events.
      - name: Elasticsearch
        description: Kafka Connect Elasticsearch sink for indexing event data.
      - name: Amazon S3
        description: Kafka Connect S3 sink for archiving event streams to object storage.
      - name: Apache Hadoop
        description: HDFS sink connector for streaming data into Hadoop data lake.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
