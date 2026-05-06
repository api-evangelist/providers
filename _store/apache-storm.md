---
aid: apache-storm
name: Apache Storm
description: Apache Storm is a free and open-source distributed real-time computation system that makes it easy to reliably process unbounded streams of data at scale. It provides a simple programming model (topologies with spouts and bolts), guaranteed message processing, horizontal scalability, and fault tolerance. Storm integrates with queuing and database technologies including Apache Kafka and Apache Cassandra and is governed by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Computing
  - Event Processing
  - Real-Time
  - Stream Processing
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-storm/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-storm:apache-storm-rest-api
    name: Apache Storm REST API
    description: The Storm UI REST API provides HTTP endpoints for monitoring and managing Storm clusters, topologies, and components. It exposes cluster summary, topology listing, topology detail, component statistics, supervisor info, nimbus info, and topology actions (activate, deactivate, rebalance, kill). The API serves the Storm UI dashboard and can be used programmatically.
    humanURL: https://storm.apache.org/releases/current/STORM-UI-REST-API.html
    tags:
      - REST
      - Monitoring
      - Cluster Management
      - Topologies
    properties:
      - type: Documentation
        url: https://storm.apache.org/releases/current/STORM-UI-REST-API.html
  - aid: apache-storm:apache-storm-topology-api
    name: Apache Storm Topology API
    description: The Storm Topology API provides Java and other language bindings for building real-time processing topologies composed of spouts (data sources) and bolts (processing units). It supports various stream groupings, windowing operations, Trident micro-batch processing, and DRPC (Distributed Remote Procedure Calls) for synchronous request/response patterns.
    humanURL: https://storm.apache.org/documentation/Tutorial.html
    tags:
      - Java
      - Topology
      - Streaming
      - Processing
    properties:
      - type: Documentation
        url: https://storm.apache.org/documentation/Tutorial.html
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.storm
        title: Maven Java SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/storm
  - type: Documentation
    url: https://storm.apache.org/documentation/Home.html
  - type: Portal
    url: https://storm.apache.org/
  - type: GettingStarted
    url: https://storm.apache.org/releases/current/Setting-up-development-environment.html
  - type: ReleaseNotes
    url: https://github.com/apache/storm/releases
  - type: Support
    url: https://storm.apache.org/contribute/People.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Guaranteed Message Processing
        description: At-least-once processing guarantees through ack/fail tracking mechanism.
      - name: Scalable Topologies
        description: Horizontally scalable stream processing topologies with configurable parallelism.
      - name: Trident API
        description: High-level micro-batch processing abstraction with stateful streaming and exactly-once semantics.
      - name: DRPC
        description: Distributed Remote Procedure Calls for synchronous distributed computation.
      - name: Windowing Operations
        description: Tumbling and sliding window processing over bounded time or count windows.
      - name: Multi-Language Support
        description: Topology components written in Java, Python, Ruby, and other languages via Multilang protocol.
  - type: UseCases
    data:
      - name: Real-Time Analytics
        description: Continuous computation over live event streams for operational dashboards.
      - name: ETL Processing
        description: Real-time data transformation and enrichment pipelines.
      - name: Machine Learning Scoring
        description: Online scoring of ML models against streaming feature data.
      - name: Fraud Detection
        description: Low-latency fraud detection rules applied to transaction streams.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Kafka Spout for consuming messages from Kafka topics as Storm data sources.
      - name: Apache Cassandra
        description: CassandraBolt for writing processed stream data to Cassandra.
      - name: Apache Hive
        description: HiveBolt for streaming inserts into Apache Hive tables.
      - name: Redis
        description: Redis integration for stateful lookups and caching in Storm bolts.
      - name: Elasticsearch
        description: ElasticsearchBolt for indexing stream data into Elasticsearch.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
