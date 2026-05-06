---
aid: apache-pulsar
name: Apache Pulsar
description: Apache Pulsar is a cloud-native, distributed messaging and streaming platform that provides server-to-server messaging with multi-tenancy, high performance, and geo-replication. It combines messaging and stream processing in a single platform.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Messaging
  - Multi-Tenant
  - Pub-Sub
  - Streaming
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-pulsar/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-pulsar:apache-pulsar-admin-rest-api
    name: Apache Pulsar Admin REST API
    description: The Pulsar Admin API provides REST endpoints for managing tenants, namespaces, topics, subscriptions, functions, connectors, and cluster configuration.
    humanURL: https://pulsar.apache.org/admin-rest-api/
    baseURL: http://localhost:8080/admin/v2
    tags:
      - Administration
      - Multi-Tenant
      - REST
    properties:
      - type: Documentation
        url: https://pulsar.apache.org/admin-rest-api/
      - type: OpenAPI
        url: openapi/pulsar-admin.yml
  - aid: apache-pulsar:apache-pulsar-messaging-api
    name: Apache Pulsar Messaging API
    description: Pulsar messaging protocol for producing and consuming messages on topics, with support for multiple subscription types (Exclusive, Shared, Failover, Key_Shared), schema enforcement, and both persistent and non-persistent topics.
    humanURL: https://pulsar.apache.org/docs/next/client-libraries/
    tags:
      - Messaging
      - Pub-Sub
      - Streaming
    properties:
      - type: Documentation
        url: https://pulsar.apache.org/docs/next/client-libraries/
      - type: AsyncAPI
        url: asyncapi/pulsar-messaging.yml
      - type: JSONSchema
        url: json-schema/pulsar-message.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/pulsar
  - type: Documentation
    url: https://pulsar.apache.org/
  - type: SpectralRules
    url: rules/apache-pulsar-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-pulsar-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/pulsar-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-pulsar-context.jsonld
  - type: Features
    data:
      - name: Multi-Tenancy
        description: Native multi-tenancy with tenant and namespace isolation
      - name: Persistent Messaging
        description: Durable message storage with Apache BookKeeper
      - name: Geo-Replication
        description: Built-in geo-replication across data centers and clouds
      - name: Pulsar Functions
        description: Lightweight serverless compute natively integrated with messaging
      - name: Tiered Storage
        description: Offload old data to object storage (S3, GCS) for cost efficiency
      - name: Schema Registry
        description: Built-in schema registry for producers and consumers
      - name: Multiple Subscription Types
        description: Exclusive, Shared, Failover, and Key_Shared subscription modes
  - type: UseCases
    data:
      - name: Real-Time Event Streaming
        description: Stream events between microservices with guaranteed delivery
      - name: Message Queue
        description: Use Shared subscription as a traditional message queue
      - name: Event Sourcing
        description: Store and replay event streams for event-driven architectures
      - name: IoT Data Ingestion
        description: Ingest high-volume IoT telemetry into Pulsar topics
  - type: Integrations
    data:
      - name: Apache Flink
        description: Pulsar connector for Flink stream processing
      - name: Apache Spark
        description: Spark Streaming integration via Pulsar connector
      - name: Apache Kafka
        description: Kafka-compatible protocol support for migration
      - name: Kubernetes
        description: Native Kubernetes deployment via Helm charts
      - name: Grafana
        description: Built-in metrics exposed to Prometheus and Grafana
---
