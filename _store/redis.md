---
aid: redis
url: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/apis.yml
apis:
- name: Redis Core API
  description: Core Redis commands and operations for data manipulation.
  image: https://redis.io/images/redis-logo.png
  humanURL: https://redis.io/docs/
  baseURL: redis://localhost:6379
  tags:
  - Cache
  - Database
  - Key-Value
  properties:
  - type: Documentation
    url: https://redis.io/docs/latest/commands/
  - type: OpenAPI
    url: https://redis.io/docs/api/
  - type: Getting Started
    url: https://redis.io/docs/getting-started/
  - type: GitHub
    url: https://github.com/redis/redis
  contact:
  - type: Support
    url: https://redis.io/support/
  - type: Community
    url: https://redis.io/community/
- name: Redis REST API
  description: REST API interface for Redis operations via HTTP.
  humanURL: https://redis.io/docs/stack/rest/
  baseURL: https://api.redis.com
  tags:
  - HTTP
  - REST
  properties:
  - type: Documentation
    url: https://redis.io/docs/stack/rest/
  - type: Swagger
    url: https://redis.io/docs/stack/rest/swagger/
- name: Redis Enterprise API
  description: Management API for Redis Enterprise clusters.
  humanURL: https://redis.io/docs/latest/operate/rs/references/rest-api/
  baseURL: https://localhost:9443/v1
  tags:
  - Cluster
  - Enterprise
  - Management
  properties:
  - type: Documentation
    url: https://redis.io/docs/latest/operate/rs/references/rest-api/
  - type: API Reference
    url: https://redis.io/docs/latest/operate/rs/references/rest-api/requests/
- name: Redis Cloud API
  description: API for managing Redis Cloud resources and subscriptions.
  humanURL: https://redis.io/docs/latest/operate/rc/api/
  baseURL: https://api.redislabs.com/v1
  tags:
  - Cloud
  - Management
  - Subscriptions
  properties:
  - type: Documentation
    url: https://redis.io/docs/latest/operate/rc/api/
  - type: Authentication
    url: https://redis.io/docs/latest/operate/rc/api/get-started/
  - type: Examples
    url: https://redis.io/docs/latest/operate/rc/api/examples/
- name: Redis Insight API
  description: API for Redis Insight visualization and management tool.
  humanURL: https://redis.io/docs/latest/develop/tools/insight/
  baseURL: http://localhost:5540/api
  tags:
  - Management
  - Tools
  - Visualization
  properties:
  - type: Documentation
    url: https://redis.io/docs/latest/develop/tools/insight/
  - type: Download
    url: https://redis.io/insight/
name: Redis
tags:
- Cache
- Database
- In-Memory
- Key-Value Store
- NoSQL
type: Contract
image: https://redis.io/images/redis-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Redis is an open source, in-memory data structure store used as a database, cache, message broker, and streaming engine.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

