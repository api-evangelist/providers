---
aid: apache-rocketmq
name: Apache RocketMQ
description: Apache RocketMQ is a distributed messaging and streaming platform with low latency, high performance, and reliability. It provides trillion-level message capacity with rich message types including normal, transactional, delayed, and ordered messages.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Messaging
  - Message Queue
  - Pub-Sub
  - Streaming
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-rocketmq/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-rocketmq:apache-rocketmq
    name: Apache RocketMQ
    description: RocketMQ provides producer and consumer APIs with client SDKs in Java, Go, Python, C++, C#, Node.js, and Rust, along with a REST API and gRPC-based remoting for message operations, topic management, and cluster administration.
    humanURL: https://rocketmq.apache.org/docs/
    tags:
      - Cloud Native
      - Messaging
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://rocketmq.apache.org/docs/
      - type: OpenAPI
        url: openapi/apache-rocketmq-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/rocketmq
  - type: Documentation
    url: https://rocketmq.apache.org/
  - type: SpectralRules
    url: rules/apache-rocketmq-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-rocketmq-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/rocketmq-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-rocketmq-context.jsonld
  - type: Features
    data:
      - name: High Throughput
        description: Billion-level message throughput with low latency
      - name: Multiple Message Types
        description: Normal, ordered, delayed, transactional, and batch messages
      - name: Message Filtering
        description: Server-side tag and SQL expression filtering
      - name: Exactly-Once Semantics
        description: Transactional messages for exactly-once delivery
      - name: Delayed Messages
        description: Schedule messages with configurable delay levels
      - name: Dead Letter Queue
        description: Automatic dead letter queue for failed messages
      - name: Message Tracing
        description: End-to-end message tracing for debugging and monitoring
  - type: UseCases
    data:
      - name: Order Processing
        description: Ensure ordered processing of e-commerce order events
      - name: Event-Driven Microservices
        description: Decouple microservices with reliable asynchronous messaging
      - name: Log Aggregation
        description: Aggregate application logs from distributed services
      - name: Financial Transactions
        description: Reliable transactional messaging for financial systems
  - type: Integrations
    data:
      - name: Spring Boot
        description: RocketMQ Spring Boot starter for easy integration
      - name: Apache Flink
        description: Flink connector for stream processing from RocketMQ
      - name: Apache Spark
        description: Spark Streaming connector for RocketMQ
      - name: Kubernetes
        description: RocketMQ Operator for Kubernetes-native deployment
---
