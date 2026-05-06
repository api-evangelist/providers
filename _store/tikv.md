---
aid: tikv
name: TiKV
description: TiKV is a CNCF-graduated distributed transactional key-value database built in Rust with Raft consensus. Originally created to complement TiDB, it provides horizontal scalability, strong consistency, and high availability with ACID transaction support. Client APIs are available for Java, Rust, Python, Go, and C++. An HTTP management API provides status, configuration, and monitoring endpoints.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/tikv/refs/heads/main/apis.yml
tags:
  - ACID
  - CNCF
  - Database
  - Distributed Systems
  - Key-Value Store
  - Open Source
  - Rust
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tikv:tikv-http-api
    name: TiKV HTTP Management API
    description: TiKV exposes an HTTP API for cluster management, status monitoring, configuration retrieval and updates, and Prometheus metrics collection.
    humanURL: https://tikv.org/docs/dev/deploy/monitor/api/
    baseURL: http://localhost:20160
    tags:
      - Database
      - Distributed Systems
      - Monitoring
      - Operations
    properties:
      - type: Documentation
        url: https://tikv.org/docs/dev/deploy/monitor/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tikv/refs/heads/main/openapi/tikv-http-api-openapi.yml
  - aid: tikv:tikv-client-java
    name: TiKV Java Client
    description: The official Java client for TiKV. Supports raw key-value operations and transactional operations via gRPC. Available on Maven Central.
    humanURL: https://github.com/tikv/client-java
    tags:
      - Database
      - Java
      - Key-Value
      - SDK
    properties:
      - type: Documentation
        url: https://github.com/tikv/client-java
      - type: GitHub
        url: https://github.com/tikv/client-java
  - aid: tikv:tikv-client-rust
    name: TiKV Rust Client
    description: The official Rust client for TiKV providing raw and transactional key-value access to TiKV clusters.
    humanURL: https://github.com/tikv/client-rust
    tags:
      - Database
      - Key-Value
      - Rust
      - SDK
    properties:
      - type: Documentation
        url: https://github.com/tikv/client-rust
      - type: GitHub
        url: https://github.com/tikv/client-rust
  - aid: tikv:tikv-client-python
    name: TiKV Python Client
    description: The official Python client for TiKV supporting raw and transactional key-value operations.
    humanURL: https://github.com/tikv/client-py
    tags:
      - Database
      - Key-Value
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://github.com/tikv/client-py
      - type: GitHub
        url: https://github.com/tikv/client-py
common:
  - type: Website
    url: https://tikv.org/
  - type: Documentation
    url: https://tikv.org/docs/
  - type: Getting Started
    url: https://tikv.org/docs/7.1/concepts/overview/
  - type: GitHub Organization
    url: https://github.com/tikv
  - type: GitHub Repository
    url: https://github.com/tikv/tikv
  - type: Governance
    url: https://github.com/tikv/tikv/blob/master/GOVERNANCE.md
  - type: CNCF
    url: https://www.cncf.io/projects/tikv/
  - type: Blog
    url: https://tikv.org/blog/
  - type: Community
    url: https://tikv.org/community/
  - type: Roadmap
    url: https://github.com/tikv/tikv/blob/master/ROADMAP.md
  - type: License
    url: https://github.com/tikv/tikv/blob/master/LICENSE
  - type: Slack
    url: https://slack.tidb.io/invite?team=tikv-wg
  - type: Forum
    url: https://internals.tidb.io/
  - type: SDK
    url: https://github.com/tikv/client-java
  - type: SDK
    url: https://github.com/tikv/client-rust
  - type: SDK
    url: https://github.com/tikv/client-py
  - type: SDK
    url: https://github.com/tikv/client-go
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
