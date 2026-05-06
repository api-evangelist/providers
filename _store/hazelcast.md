---
aid: hazelcast
name: Hazelcast
description: Hazelcast is a real-time data platform that helps businesses accelerate their applications with data caching, data integration, and distributed computing. Hazelcast provides in-memory computing capabilities for high-performance, low-latency applications, exposing a REST API for managing maps, queues, cluster state, configuration, and health.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Caching
  - Distributed Computing
  - In-Memory Computing
  - Real-Time
  - REST
url: https://raw.githubusercontent.com/api-evangelist/hazelcast/refs/heads/main/apis.yml
created: '2025-08-19'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hazelcast:hazelcast-rest-api
    name: Hazelcast REST API
    description: Hazelcast provides a REST API for interacting with the distributed data grid, supporting operations for maps, queues, cluster management, configuration reload, and health checks over HTTP.
    humanURL: https://docs.hazelcast.com/hazelcast/latest/maintain-cluster/rest-api
    baseURL: http://localhost:5701/hazelcast/rest
    tags:
      - Distributed Computing
      - In-Memory Computing
      - REST
      - Maps
      - Queues
      - Cluster Management
    properties:
      - type: Documentation
        url: https://docs.hazelcast.com/hazelcast/latest/maintain-cluster/rest-api
      - type: Getting Started
        url: https://docs.hazelcast.com/hazelcast/latest/getting-started/get-started-docker
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/hazelcast/refs/heads/main/openapi/hazelcast-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/hazelcast/refs/heads/main/hazelcast-rules.yml
common:
  - type: Website
    url: https://hazelcast.com/
  - type: Documentation
    url: https://docs.hazelcast.com/
  - type: Getting Started
    url: https://docs.hazelcast.com/hazelcast/latest/getting-started/get-started-docker
  - type: Support
    url: https://hazelcast.com/support/
  - type: Blog
    url: https://hazelcast.com/blog/
  - type: GitHub Organization
    url: https://github.com/hazelcast
  - type: Community
    url: https://slack.hazelcast.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
