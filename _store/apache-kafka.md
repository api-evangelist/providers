---
aid: apache-kafka
url: https://raw.githubusercontent.com/api-evangelist/apache-kafka/refs/heads/main/apis.yml
apis:
- aid: apache-kafka:kafka-rest-proxy-api
  name: Kafka REST Proxy API
  description: The Kafka REST Proxy provides a RESTful interface to a Kafka cluster for producing and consuming messages, managing topics, partitions, consumer groups, ACLs, and viewing cluster state.
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
  description: Kafka Connect REST API for managing connectors, their configurations, tasks, and offsets. Used for integrating Kafka with external data systems.
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
  description: The core Kafka messaging protocol for producing and consuming records to/from topics using the native Kafka binary protocol.
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
  - type: JSONSchema
    url: json-schema/kafka-record.json
  - type: JSONSchema
    url: json-schema/kafka-topic-config.json
name: Apache Kafka
tags:
- Distributed Systems
- Event Streaming
- Messaging
- Pub-Sub
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-06-05'
modified: '2026-04-07'
position: Consumer
description: Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

