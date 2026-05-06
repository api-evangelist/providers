---
aid: apache-flume
name: Apache Flume
description: Apache Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log and event data. It provides a simple and flexible architecture based on streaming data flows with pluggable sources, channels, and sinks, plus a REST monitoring API for agent metrics.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Data Collection
  - ETL
  - Log Aggregation
  - Open Source
  - Streaming
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-flume/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-flume:apache-flume-monitoring-api
    name: Apache Flume Monitoring API
    description: REST API for monitoring Apache Flume agents, retrieving component metrics for sources, channels, and sinks, and accessing agent health information.
    humanURL: https://flume.apache.org/FlumeUserGuide.html
    baseURL: http://localhost:41414
    tags:
      - Monitoring
      - Metrics
      - REST API
    properties:
      - type: Documentation
        url: https://flume.apache.org/FlumeUserGuide.html
      - type: OpenAPI
        url: openapi/apache-flume-monitoring-openapi.yml
      - type: JSONSchema
        url: json-schema/flume-monitoring-agent-metrics-schema.json
      - type: JSON-LD
        url: json-ld/apache-flume-monitoring-context.jsonld
  - aid: apache-flume:apache-flume-java-api
    name: Apache Flume Java API
    description: Java API for building custom Flume sources, channels, sinks, and interceptors. Provides interfaces for developing pluggable data ingestion components.
    humanURL: https://flume.apache.org/FlumeDeveloperGuide.html
    tags:
      - Java
      - SDK
      - Extension
    properties:
      - type: Documentation
        url: https://flume.apache.org/FlumeDeveloperGuide.html
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.flume/flume-ng-core
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://flume.apache.org/documentation.html
  - type: GettingStarted
    url: https://flume.apache.org/FlumeUserGuide.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/flume
  - type: SpectralRules
    url: rules/apache-flume-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-flume-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/flume-log-collection.yaml
  - type: Features
    data:
      - name: Pluggable Sources
        description: Extensible source architecture supporting Avro, Thrift, Exec, Taildir, Kafka, HTTP, Syslog, and custom sources.
      - name: Durable Channels
        description: Multiple channel implementations including memory, file-backed, and Kafka-backed channels for different durability requirements.
      - name: Multi-Destination Sinks
        description: Write events to HDFS, HBase, Solr, Elasticsearch, Kafka, and custom sink destinations.
      - name: Fan-In Consolidation
        description: Aggregate events from multiple agent sources into a single destination for centralized log collection.
      - name: Fan-Out Distribution
        description: Route events from a single source to multiple channel/sink combinations for parallel processing.
      - name: Interceptors
        description: Event transformation interceptors for filtering, enrichment, and routing based on event content.
      - name: SSL/TLS Security
        description: TLS encryption support across Avro, Thrift, Kafka, HTTP, and Syslog components.
      - name: Monitoring REST API
        description: HTTP monitoring endpoint exposing source, channel, and sink metrics for agent health monitoring.
      - name: Multi-Hop Flows
        description: Chain multiple Flume agents via Avro/Thrift RPC for tiered log aggregation architectures.
  - type: UseCases
    data:
      - name: Centralized Log Aggregation
        description: Collect application logs from hundreds of servers and aggregate them into HDFS, Kafka, or Elasticsearch.
      - name: Real-Time Log Tailing
        description: Tail application log files in real time using Taildir source for immediate event processing.
      - name: Syslog Ingestion
        description: Ingest RFC-3164 and RFC-5424 syslog events from network devices into centralized storage.
      - name: Kafka Event Ingestion
        description: Bridge Kafka topics to HDFS or other storage for batch analytics on streaming event data.
      - name: Multi-Tier Architectures
        description: Build tiered data collection with edge collectors forwarding to aggregation agents and final destinations.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Kafka source and channel for consuming events, and Kafka sink for writing events to topics.
      - name: Apache HDFS
        description: Primary sink for writing log data to Hadoop Distributed File System for batch analytics.
      - name: Apache HBase
        description: HBase sink for writing events directly to HBase tables for random-access analytics.
      - name: Apache Solr
        description: Solr sink for indexing log events for full-text search capabilities.
      - name: Elasticsearch
        description: Elasticsearch sink for indexing and searching aggregated log data.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
