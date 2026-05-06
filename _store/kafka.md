---
aid: kafka
name: Apache Kafka
description: Apache Kafka is a distributed event streaming platform for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. It provides high-throughput, fault-tolerant, publish-subscribe messaging.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Systems
  - Event Driven
  - Messaging
  - Real-Time
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/kafka/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kafka:producer-api
    name: Kafka Producer API
    description: API for publishing streams of records to Kafka topics.
    humanURL: https://kafka.apache.org/documentation/#producerapi
    tags:
      - Messaging
      - Producer
      - Streaming
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/#producerapi
  - aid: kafka:consumer-api
    name: Kafka Consumer API
    description: API for subscribing to topics and processing streams of records.
    humanURL: https://kafka.apache.org/documentation/#consumerapi
    tags:
      - Consumer
      - Messaging
      - Streaming
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/#consumerapi
  - aid: kafka:streams-api
    name: Kafka Streams API
    description: API for building stream processing applications and microservices on top of Kafka.
    humanURL: https://kafka.apache.org/documentation/streams/
    tags:
      - Processing
      - Streaming
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/streams/
  - aid: kafka:connect-api
    name: Kafka Connect REST API
    description: REST API for integrating Kafka with external systems through connectors.
    humanURL: https://kafka.apache.org/documentation/#connect
    baseURL: http://localhost:8083
    tags:
      - Connectors
      - Integration
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/#connect_rest
  - aid: kafka:admin-api
    name: Kafka Admin API
    description: API for managing and inspecting topics, brokers, configurations, and ACLs.
    humanURL: https://kafka.apache.org/documentation/#adminapi
    tags:
      - Administration
      - Management
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/#adminapi
common:
  - type: Website
    url: https://kafka.apache.org
  - type: Documentation
    url: https://kafka.apache.org/documentation/
  - type: Getting Started
    url: https://kafka.apache.org/quickstart
  - type: GitHub Organization
    url: https://github.com/apache/kafka
  - type: Blog
    url: https://kafka.apache.org/blog
  - type: Community
    url: https://kafka.apache.org/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
