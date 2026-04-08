---
aid: redis-streams
url: https://raw.githubusercontent.com/api-evangelist/redis-streams/refs/heads/main/apis.yml
apis:
- aid: redis-streams:redis-streams-api
  name: Redis Streams
  description: Redis Streams is a Redis data structure that acts as an append-only log, supporting consumer groups, range queries, and message acknowledgment for building event-driven architectures and real-time data processing pipelines.
  humanURL: https://redis.io/docs/latest/develop/data-types/streams/
  tags:
  - Consumer Groups
  - Event-Driven
  - In-Memory
  - Messaging
  - Redis
  - Streaming
  properties:
  - type: Documentation
    url: https://redis.io/docs/latest/develop/data-types/streams/
  - type: JSONSchema
    url: json-schema/redis-stream-entry.json
  - type: JSONSchema
    url: json-schema/redis-consumer-group.json
  - type: JSONSchema
    url: json-schema/redis-stream-info.json
name: Redis Streams
tags:
- Consumer Groups
- Event-Driven
- In-Memory
- Messaging
- Redis
- Streaming
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Redis Streams is a data structure in Redis that models an append-only log for managing streams of data, providing consumer groups, message acknowledgment, and the ability to process data in real time with high throughput and low latency.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

