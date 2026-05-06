---
aid: google-cloud-memorystore
name: Google Cloud Memorystore
description: Google Cloud Memorystore is a fully managed in-memory data store service for Redis and Memcached. It provides a scalable, secure, and highly available caching layer that helps accelerate application performance. Memorystore automates complex tasks like provisioning, replication, failover, and patching, enabling developers to focus on building applications without managing infrastructure.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-memorystore/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Cache
  - Google Cloud
  - In-Memory
  - Memcached
  - Redis
apis:
  - name: Memorystore for Redis API
    description: The Memorystore for Redis API enables programmatic management of fully managed Redis instances on Google Cloud. It supports creating, updating, deleting, and scaling Redis instances, configuring high availability with automatic failover, managing data persistence, and performing version upgrades. The API provides operations for both basic single-node and standard high-availability configurations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/memorystore/docs/redis
    baseURL: https://redis.googleapis.com/v1
    tags:
      - Cache
      - In-Memory
      - Instances
      - Redis
    properties:
      - type: Documentation
        url: https://cloud.google.com/memorystore/docs/redis/reference/rest
      - type: OpenAPI
        url: openapi/cloud-memorystore-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/memorystore/docs/redis/auth-overview
      - type: Getting Started
        url: https://cloud.google.com/memorystore/docs/redis/quickstart
      - type: JSONSchema
        url: json-schema/instance-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/memorystore
  - type: Getting Started
    url: https://cloud.google.com/memorystore/docs/redis/quickstart
  - type: Documentation
    url: https://cloud.google.com/memorystore/docs/redis
  - type: Authentication
    url: https://cloud.google.com/memorystore/docs/redis/auth-overview
  - type: Pricing
    url: https://cloud.google.com/memorystore/docs/redis/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/memorystore/docs/redis/support
  - type: JSON-LD
    url: json-ld/google-cloud-memorystore-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
