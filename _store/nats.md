---
aid: nats
url: https://raw.githubusercontent.com/api-evangelist/nats/refs/heads/main/apis.yml
apis:
- aid: nats:nats-monitoring-api
  name: NATS Monitoring API
  description: HTTP monitoring API providing real-time server status, connection information, route details, subscription statistics, JetStream metrics, and health check endpoints for observability and operations.
  humanURL: https://docs.nats.io/running-a-nats-service/nats_admin/monitoring
  baseURL: http://localhost:8222
  tags:
  - Health
  - Metrics
  - Monitoring
  properties:
  - url: https://docs.nats.io/running-a-nats-service/nats_admin/monitoring
    type: Documentation
  - url: properties/nats-monitoring-api-openapi.yml
    type: OpenAPI
  - url: openapi/nats-monitoring.yml
    type: OpenAPI
- aid: nats:nats-messaging-api
  name: NATS Messaging API
  description: Asynchronous messaging API supporting core pub-sub, request-reply, queue groups, and JetStream persistent messaging with streams, consumers, key-value stores, and object stores.
  humanURL: https://docs.nats.io/nats-concepts/core-nats
  tags:
  - JetStream
  - Messaging
  - Pub Sub
  - Streaming
  properties:
  - url: https://docs.nats.io/nats-concepts/core-nats
    type: Documentation
  - url: properties/nats-messaging-asyncapi.yml
    type: AsyncAPI
  - url: asyncapi/nats-messaging.yml
    type: AsyncAPI
  - url: json-schema/nats-stream-config.json
    type: JSONSchema
- aid: nats:nats-jetstream-api
  name: NATS JetStream Management API
  description: The JetStream wire API provides a protocol-level management interface for configuring and operating JetStream streams, consumers, key-value buckets, and object stores. Requests are made by publishing to well-known $JS.API.* subjects and responses are returned as typed JSON payloads. This API underlies all official NATS client SDKs and the nats CLI.
  humanURL: https://docs.nats.io/reference/reference-protocols/nats_api_reference
  tags:
  - JetStream
  - Management
  - Streaming
  properties:
  - url: https://docs.nats.io/reference/reference-protocols/nats_api_reference
    type: Documentation
  - url: https://docs.nats.io/nats-concepts/jetstream
    type: Reference
  - url: properties/nats-jetstream-api-asyncapi.yml
    type: AsyncAPI
  - url: properties/nats-jetstream-config-json-schema.json
    type: JSONSchema
- aid: nats:nats-kv-api
  name: NATS Key-Value Store API
  description: The NATS Key-Value Store API is a JetStream-backed abstraction that provides immediately consistent, persistent associative array semantics. Clients can create buckets, get, put, delete, and watch keys, and receive real-time change notifications. Buckets are implemented as JetStream streams with the KV_ prefix.
  humanURL: https://docs.nats.io/nats-concepts/jetstream/key-value-store
  tags:
  - JetStream
  - Key-Value
  - Storage
  properties:
  - url: https://docs.nats.io/nats-concepts/jetstream/key-value-store
    type: Documentation
  - url: https://docs.nats.io/using-nats/developer/develop_jetstream/kv
    type: Reference
  - url: properties/nats-kv-schema.json
    type: JSONSchema
- aid: nats:nats-object-store-api
  name: NATS Object Store API
  description: The NATS Object Store API is a JetStream-backed abstraction for storing and retrieving arbitrarily large binary objects using a chunking mechanism. Objects are identified by a bucket and a name, and the API supports put, get, delete, and watch operations for managing stored files and blobs.
  humanURL: https://docs.nats.io/nats-concepts/jetstream/obj_store
  tags:
  - JetStream
  - Object Store
  - Storage
  properties:
  - url: https://docs.nats.io/nats-concepts/jetstream/obj_store
    type: Documentation
  - url: https://docs.nats.io/using-nats/developer/develop_jetstream/object
    type: Reference
  - url: properties/nats-object-store-schema.json
    type: JSONSchema
name: NATS
tags:
- Cloud Native
- IoT
- Message Broker
- Microservices
- Pub Sub
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A high-performance, cloud-native messaging system for microservices, IoT, and edge computing. Provides pub-sub, request-reply, and queue-based messaging patterns with at-most-once and at-least-once delivery guarantees.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

