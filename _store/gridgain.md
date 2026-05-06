---
aid: gridgain
name: GridGain
description: GridGain is a unified real-time data platform that provides in-memory computing for transactions, analytics, and AI workloads. Built on top of Apache Ignite, it offers distributed database, caching, and computing capabilities for high-performance data-intensive applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Caching
  - Data Grid
  - Distributed Database
  - In-Memory Computing
  - Real-Time
url: https://raw.githubusercontent.com/api-evangelist/gridgain/refs/heads/main/apis.yml
created: '2025-08-19'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: gridgain:gridgain-rest-api
    name: GridGain REST API
    description: Legacy GridGain 8 / Apache Ignite REST API for cache operations, SQL and scan queries, cluster activation, and node management over HTTP.
    humanURL: https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi
    baseURL: http://localhost:8080/ignite
    tags:
      - Caching
      - Distributed Database
      - In-Memory Computing
      - REST
    properties:
      - type: Documentation
        url: https://www.gridgain.com/docs/gridgain8/latest/developers-guide/restapi
      - type: Getting Started
        url: https://www.gridgain.com/docs/gridgain8/latest/getting-started/quick-start/restapi
  - aid: gridgain:gridgain-management-api
    name: GridGain 9 Management API
    description: The GridGain 9 management API exposes cluster initialization, node and cluster configuration, authentication and JWT, RBAC, snapshots, CDC, compute jobs, recovery, deployment units, SQL monitoring, and license management for production GridGain 9 clusters.
    humanURL: https://www.gridgain.com/sdk/gridgain9/latest/openapi.html
    baseURL: http://localhost:10300/management/v1
    tags:
      - Cluster Management
      - In-Memory Computing
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://www.gridgain.com/sdk/gridgain9/latest/openapi.html
      - type: OpenAPI
        url: openapi/gridgain-openapi.yml
      - type: Capabilities
        url: capabilities/gridgain-capabilities.yml
      - type: Rules
        url: rules/gridgain-rules.yml
      - type: JSONSchema
        url: json-schema/gridgain-schema-index.yml
common:
  - type: Website
    url: https://www.gridgain.com/
  - type: Documentation
    url: https://www.gridgain.com/docs/latest/
  - type: Getting Started
    url: https://www.gridgain.com/docs/latest/getting-started/quick-start/java
  - type: Support
    url: https://www.gridgain.com/support
  - type: Blog
    url: https://www.gridgain.com/resources/blog
  - type: GitHub Organization
    url: https://github.com/gridgain
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
