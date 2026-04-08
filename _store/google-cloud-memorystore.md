---
aid: google-cloud-memorystore
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-memorystore/refs/heads/main/apis.yml
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
name: Google Cloud Memorystore
tags:
- Cache
- Google Cloud
- In-Memory
- Memcached
- Redis
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Memorystore is a fully managed in-memory data store service for Redis and Memcached. It provides a scalable, secure, and highly available caching layer that helps accelerate application performance. Memorystore automates complex tasks like provisioning, replication, failover, and patching, enabling developers to focus on building applications without managing infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

