---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-11'
api_count: 21
apis:
- description: Distributed, partitioned, replicated log. The reference open-source streaming platform; durable, ordered topics with consumer groups, exactly -once semantics, and the de facto wire protocol for the st
  name: Apache Kafka
  slug: apache-kafka
- description: Cloud-native, multi-tenant pub/sub and streaming platform with a tiered storage architecture (BookKeeper) that separates compute from storage, native geo-replication, and built-in Functions for lightw
  name: Apache Pulsar
  slug: apache-pulsar
- description: Kafka-API-compatible streaming platform implemented in C++ with no ZooKeeper/JVM dependency. Single binary, thread-per-core architecture, Raft consensus; positioned as a drop-in for Kafka workloads.
  name: Redpanda
  slug: redpanda
- description: Persistence layer for the NATS messaging system providing at-least-once and exactly-once streaming, key/value and object stores, and durable consumers — designed for edge, IoT, and microservice topolo
  name: NATS JetStream
  slug: nats-jetstream
- description: 'AWS managed family for real-time streaming: Kinesis Data Streams (shards, partition keys, 24h–365d retention), Kinesis Data Firehose (delivery to S3/Redshift/OpenSearch), and Kinesis Video Streams for'
  name: Amazon Kinesis
  slug: aws-kinesis
- description: GCP's managed messaging (Pub/Sub) and stream-processing (Dataflow, built on Apache Beam) stack. Pub/Sub provides at-least-once and exactly-once delivery with push/pull subscribers; Dataflow runs windo
  name: Google Cloud Pub/Sub and Dataflow
  slug: gcp-pubsub
- description: Microsoft's managed big-data streaming platform; Kafka-protocol compatible, partitioned, with Capture (delivery to ADLS/Blob) and tight integration with Azure Stream Analytics and Functions.
  name: Azure Event Hubs
  slug: azure-event-hubs
- description: Managed Kafka by the original Kafka authors. Cluster, topic, connector, KSQL, Schema Registry, Stream Governance, and Flink offerings exposed via a Confluent Cloud REST API and Terraform provider.
  name: Confluent Cloud
  slug: confluent-cloud
- description: Managed Apache Pulsar as a service from Pulsar's original contributors, with multi-cloud clusters, Functions, sources/sinks, and a control-plane REST API.
  name: StreamNative
  slug: streamnative
- description: One-directional HTTP-based streaming from server to client using the `text/event-stream` media type. Defined by the HTML Living Standard EventSource API; widely used for LLM token streams, dashboards,
  name: Server-Sent Events (SSE)
  slug: server-sent-events
- description: Full-duplex, bidirectional streaming protocol over a single TCP connection, upgraded from HTTP. RFC 6455. Foundation for chat, collaborative apps, market data, and real-time control planes.
  name: WebSocket
  slug: websocket
- description: 'gRPC defines four RPC styles, three of which are streaming: server streaming, client streaming, and bidirectional streaming, all multiplexed over HTTP/2. The default streaming surface for service-to-s'
  name: gRPC Streaming
  slug: grpc-streaming
- description: The GraphQL operation type for receiving a stream of updates over a long-lived transport (typically WebSocket via the graphql-ws or graphql-transport-ws sub-protocols, or SSE). Used to push schema- de
  name: GraphQL Subscriptions
  slug: graphql-subscriptions
- description: Framework and runtime for source/sink connectors that move data into and out of Kafka. Distributed mode runs a REST-controlled cluster of workers managing connector and task lifecycle.
  name: Kafka Connect
  slug: kafka-connect
- description: Change-data-capture (CDC) platform that streams row-level database changes (Postgres, MySQL, MongoDB, SQL Server, Oracle, Cassandra) as Kafka records using each database's native replication log.
  name: Debezium
  slug: debezium
- description: Distributed, stateful stream-processing engine with event-time semantics, windowing, watermarks, and exactly-once state. SQL, DataStream, and Table APIs; reference engine for sub-second latency analyt
  name: Apache Flink
  slug: apache-flink
- description: Stream-processing API built on Spark SQL using a micro-batch (and experimental continuous) execution model. Treats a stream as an unbounded table.
  name: Spark Structured Streaming
  slug: spark-structured-streaming
- description: Operational data warehouse and streaming SQL database built on Differential Dataflow. Maintains incrementally updated materialized views over streaming sources with millisecond freshness.
  name: Materialize
  slug: materialize
- description: Real-time analytics platform built on ClickHouse; ingests streams via HTTP, Kafka, or CDC, exposes SQL pipes as parameterized HTTP API endpoints with auth tokens.
  name: Tinybird
  slug: tinybird
- description: Open-source Python-native stream-processing framework built on Timely Dataflow; targets data scientists and Python teams building real-time ML and data pipelines.
  name: Bytewax
  slug: bytewax
- description: Unified batch and streaming programming model. Beam pipelines run on multiple runners (Dataflow, Flink, Spark, Samza), defining the canonical event-time / watermark / window / trigger semantics for st
  name: Apache Beam
  slug: apache-beam
artifact_total: 33
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/kafka/blob/trunk/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/streaming-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streaming-domain-security.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/streaming-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/streaming-stream-record-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/streaming-stream-platform-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/streaming-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/streaming-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/streaming-stream-example.json
- group: build
  title: ''
  type: Examples
  url: examples/streaming-stream-record-example.json
- group: build
  title: ''
  type: Examples
  url: examples/streaming-stream-platform-example.json
created: '2026-05-22'
description: 'Streaming is a topic catalog of the protocols, platforms, and processing engines used to move and transform real-time, high-volume, often bidirectional data over the network. It indexes the canonical log-structured and broker systems (Apache Kafka, Apache Pulsar, Redpanda, NATS JetStream, AWS Kinesis, GCP Pub/Sub + Dataflow, Azure Event Hubs, Confluent Cloud, StreamNative), the over-the-wire streaming protocols exposed to API consumers (Server-Sent Events, WebSocket, gRPC streaming, GraphQL subscriptions), the change-data capture and connector frameworks that feed them (Kafka Connect, Debezium), and the stream-processing engines that consume them (Apache Flink, Spark Structured Streaming, Materialize, Tinybird, Bytewax, Apache Beam). This topic is distinguished from `events` and `async-apis`: streaming emphasizes real-time, high-throughput, partitioned, and often bidirectional pipes, rather than discrete event envelopes or static contract documents.'
examples:
- key_count: 16
  name: Streaming Stream Example
  slug: streaming-stream-example
- key_count: 16
  name: Streaming Stream Platform Example
  slug: streaming-stream-platform-example
- key_count: 12
  name: Streaming Stream Record Example
  slug: streaming-stream-record-example
graphqls:
- description: The GraphQL operation type for receiving a stream of updates over a long-lived transport (typically WebSocket via the graphql-ws or graphql-transport-ws sub-protocols, or SSE). Used to push schema- de
  name: Streaming GraphQL API
  slug: streaming-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streaming.png
json_schemas:
- name: Stream Platform
  property_count: 16
  slug: streaming-stream-platform
- name: Stream Record
  property_count: 12
  slug: streaming-stream-record
- name: Stream
  property_count: 16
  slug: streaming-stream
json_structures:
- name: Streaming Stream Structure
  property_count: 15
  slug: streaming-stream-structure
jsonld:
- class_count: 49
  name: Streaming Context
  property_count: 11
  slug: streaming-context
layout: provider
modified: '2026-05-22'
name: Streaming
nav: Providers
network: true
overview: 'Streaming publishes 21 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Streaming, Real Time, Event Streaming, Change Data Capture, and Stream Processing.


  The Streaming catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Streaming''s developer surface includes code examples and 10 more developer resources.'
random_paper: 42
rules:
- name: Streaming API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: streaming-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 19.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/streaming/refs/heads/main/screenshots/streaming-2026-06-20T194618.png
security:
- kind: domain-security
  name: Streaming Domain Security
  slug: streaming-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Streaming Vulnerability Disclosure
  slug: streaming-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: streaming
tags:
- Streaming
- Real Time
- Event Streaming
- Change Data Capture
- Stream Processing
- Server Sent Events
- WebSocket
- gRPC
- GraphQL Subscriptions
- Kafka
- Pulsar
- Kinesis
- Flink
---
