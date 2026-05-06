---
aid: redis-streams
name: Redis Streams
description: Redis Streams is a data structure in Redis that models an append-only log for managing streams of data, providing consumer groups, message acknowledgment, and the ability to process data in real time with high throughput and low latency.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Consumer Groups
  - Event-Driven
  - In-Memory
  - Messaging
  - Redis
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/redis-streams/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
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
      - type: JSONStructure
        url: json-structure/redis-stream-entry-structure.json
      - type: JSONStructure
        url: json-structure/redis-consumer-group-structure.json
      - type: JSONStructure
        url: json-structure/redis-stream-info-structure.json
      - type: JSONLd
        url: json-ld/redis-streams-context.jsonld
      - type: Vocabulary
        url: vocabulary/redis-streams-vocabulary.yml
common:
  - type: Website
    url: https://redis.io/
  - type: Documentation
    url: https://redis.io/docs/latest/develop/data-types/streams/
  - type: Getting Started
    url: https://redis.io/docs/latest/get-started/
  - type: GitHub
    url: https://github.com/redis/redis
  - type: Blog
    url: https://redis.io/blog/
  - type: Community
    url: https://redis.io/community/
  - type: Commands Reference
    url: https://redis.io/docs/latest/commands/?group=stream
  - type: Tutorial
    url: https://redis.io/docs/latest/develop/data-types/streams-tutorial/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
