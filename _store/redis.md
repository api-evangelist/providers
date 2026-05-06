---
aid: redis
name: Redis
description: Redis is an open source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It supports strings, hashes, lists, sets, sorted sets, streams, JSON, and more. Redis is used by millions of developers for caching, session management, leaderboards, pub/sub messaging, real-time analytics, and event streaming. The Redis project is governed by the Redis Community and maintained by Redis Inc.
type: Index
image: https://redis.io/images/redis-logo.png
url: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/apis.yml
tags:
  - Cache
  - Database
  - In-Memory
  - Key-Value Store
  - NoSQL
  - Open Source
  - Streaming
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: redis:redis-core
    name: Redis Core
    description: Core Redis commands and data structure operations. Redis supports strings, hashes, lists, sets, sorted sets, streams, and more. The primary interface is the Redis Serialization Protocol (RESP) over TCP, with client libraries for all major programming languages.
    humanURL: https://redis.io/docs/latest/commands/
    tags:
      - Cache
      - Commands
      - Core
      - Database
      - Key-Value
    properties:
      - type: Documentation
        url: https://redis.io/docs/latest/commands/
      - type: GettingStarted
        url: https://redis.io/docs/latest/get-started/
      - type: GitHub
        url: https://github.com/redis/redis
      - type: JSONSchema
        url: json-schema/redis-key-value-schema.json
      - type: JSONSchema
        url: json-schema/redis-command-schema.json
      - type: JSONSchema
        url: json-schema/redis-server-info-schema.json
      - type: JSONStructure
        url: json-structure/redis-key-value-structure.json
      - type: JSONStructure
        url: json-structure/redis-server-info-structure.json
      - type: JSONLd
        url: json-ld/redis-context.jsonld
      - type: Vocabulary
        url: vocabulary/redis-vocabulary.yml
  - aid: redis:redis-cloud-api
    name: Redis Cloud API
    description: The Redis Cloud REST API for managing subscriptions, databases, cloud accounts, access control, and logs on the Redis Cloud platform. Available at api.redislabs.com/v1 with API key authentication.
    humanURL: https://redis.io/docs/latest/operate/rc/api/
    tags:
      - Cloud
      - Management
      - REST
      - Subscriptions
    properties:
      - type: Documentation
        url: https://redis.io/docs/latest/operate/rc/api/
      - type: Authentication
        url: https://redis.io/docs/latest/operate/rc/api/get-started/
      - type: Examples
        url: https://redis.io/docs/latest/operate/rc/api/examples/
  - aid: redis:redis-enterprise-api
    name: Redis Enterprise API
    description: REST API for managing Redis Enterprise Software clusters. Provides endpoints for cluster configuration, database creation and management, user access control, and monitoring. Available at the cluster's port 9443.
    humanURL: https://redis.io/docs/latest/operate/rs/references/rest-api/
    tags:
      - Cluster
      - Enterprise
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://redis.io/docs/latest/operate/rs/references/rest-api/
      - type: APIReference
        url: https://redis.io/docs/latest/operate/rs/references/rest-api/requests/
  - aid: redis:redis-insight
    name: Redis Insight
    description: Redis Insight is a free GUI management tool for Redis. Provides database browsing, query execution, memory analysis, slow log inspection, and Redis Streams visualization. Available as a desktop app and Docker image.
    humanURL: https://redis.io/docs/latest/develop/tools/insight/
    tags:
      - Developer Tools
      - Management
      - Visualization
    properties:
      - type: Documentation
        url: https://redis.io/docs/latest/develop/tools/insight/
      - type: Download
        url: https://redis.io/insight/
      - type: Docker
        url: https://hub.docker.com/r/redis/redisinsight
common:
  - name: Redis Website
    url: https://redis.io/
    type: Website
  - name: Redis Documentation
    url: https://redis.io/docs/
    type: Documentation
  - name: Redis GitHub Organization
    url: https://github.com/redis
    type: GitHubOrg
  - name: Redis Blog
    url: https://redis.io/blog/
    type: Blog
  - name: Redis Community
    url: https://redis.io/community/
    type: Community
  - name: Redis on LinkedIn
    url: https://www.linkedin.com/company/redis/
    type: LinkedIn
  - name: Redis on X
    url: https://twitter.com/redisinc
    type: X
  - name: Redis YouTube
    url: https://www.youtube.com/c/Redisinc
    type: YouTube
  - name: Redis Status
    url: https://status.redis.com/
    type: Status
  - name: Redis Support
    url: https://redis.io/support/
    type: Support
  - name: Redis Terms of Service
    url: https://redis.io/legal/terms/
    type: TermsOfService
  - name: Redis Privacy Policy
    url: https://redis.io/legal/privacy/
    type: PrivacyPolicy
  - name: Redis Command Reference
    url: https://redis.io/docs/latest/commands/
    type: Documentation
  - name: Redis Client Libraries
    url: https://redis.io/docs/latest/develop/connect/clients/
    type: SDKs
  - name: Redis npm Package
    url: https://www.npmjs.com/package/redis
    type: npm
  - name: Redis PyPI Package
    url: https://pypi.org/project/redis/
    type: PyPI
  - type: Features
    data:
      - 'Free: 30 MB shared cloud DB'
      - 'Essentials from $0.007/hr ($5/mo min): 250 MB-100 GB DB, SSO/RBAC'
      - 'Pro from $0.014/hr ($200/mo min): dedicated, multi-region active-active'
      - 'Enterprise: self-managed Redis Enterprise Software, hybrid, on-prem'
      - 'Multi-cloud: AWS, GCP, Azure'
      - Cloud API for cluster management at 60 req/min
      - 'Redis Stack modules: RediSearch, RedisJSON, RedisGraph, RedisTimeSeries, RedisBloom'
      - Vector similarity search (RediSearch)
      - Redis Flex (RAM:Flash ratio for cost reduction)
      - Auto-tiering for hot/cold data
      - Active-active geo-distribution (Pro)
      - Up to 99.999% uptime (Pro)
      - Encryption in transit and at rest (Essentials+)
      - Private connectivity (Pro)
      - OAuth + API keys
      - Open-source self-managed Redis OSS alternative
    sources:
      - https://redis.io/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
