---
aid: clickhouse
name: ClickHouse
url: https://raw.githubusercontent.com/api-evangelist/clickhouse/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-26'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: opensource
tags:
  - Analytics
  - Cloud Database
  - Column-Oriented
  - Database
  - OLAP
  - Open Source
  - Real-Time
  - SQL
description: ClickHouse is a fast open-source column-oriented database management system that enables real-time analytical reporting using SQL. ClickHouse exposes multiple interfaces - an HTTP interface for SQL queries, native TCP, MySQL and PostgreSQL wire-compatible interfaces, and a gRPC interface - and the ClickHouse Cloud management plane offers a public OpenAPI-described REST API for provisioning and managing services, organizations, members, API keys, backups, and private endpoints.
apis:
  - aid: clickhouse:clickhouse-http-interface
    name: ClickHouse HTTP Interface
    tags:
      - Database
      - HTTP
      - SQL
    humanURL: https://clickhouse.com/docs/en/interfaces/http
    baseURL: http://localhost:8123
    properties:
      - url: https://clickhouse.com/docs/en/interfaces/http
        type: Documentation
    description: HTTP interface (default port 8123, HTTPS 8443) for executing SQL queries against ClickHouse. Supports SELECT via GET, mutations via POST, multiple output formats (JSON, CSV, XML, TabSeparated), and authentication via HTTP Basic, URL parameters, or X-ClickHouse-User/X-ClickHouse-Key headers. Helper paths include /ping and /replicas_status.
  - aid: clickhouse:clickhouse-cloud-api
    name: ClickHouse Cloud API
    tags:
      - Cloud
      - Management
      - REST
    humanURL: https://clickhouse.com/docs/en/cloud/manage/api/api-overview
    baseURL: https://api.clickhouse.cloud
    properties:
      - url: https://clickhouse.com/docs/en/cloud/manage/api/api-overview
        type: Documentation
      - url: https://clickhouse.com/docs/cloud/manage/api/swagger
        type: Swagger
      - url: https://api.clickhouse.cloud/v1
        type: OpenAPI
    description: OpenAPI 3.1-described REST API for managing ClickHouse Cloud organizations, services, API keys, members, backups, private endpoints, and ClickHouse settings. Endpoints under /v1 with consistent envelope responses (status, requestId, result, error) and authentication via API key.
  - aid: clickhouse:clickhouse-native
    name: ClickHouse Native TCP Interface
    tags:
      - Native
      - TCP
    humanURL: https://clickhouse.com/docs/en/interfaces/tcp
    properties:
      - url: https://clickhouse.com/docs/en/interfaces/tcp
        type: Documentation
    description: Native binary TCP protocol used by ClickHouse client libraries for maximum throughput between client and server (default port 9000).
  - aid: clickhouse:clickhouse-mysql
    name: ClickHouse MySQL Interface
    tags:
      - MySQL
      - Wire Protocol
    humanURL: https://clickhouse.com/docs/en/interfaces/mysql
    properties:
      - url: https://clickhouse.com/docs/en/interfaces/mysql
        type: Documentation
    description: MySQL wire protocol compatibility allowing existing MySQL clients and BI tools to query ClickHouse without driver changes.
  - aid: clickhouse:clickhouse-postgresql
    name: ClickHouse PostgreSQL Interface
    tags:
      - PostgreSQL
      - Wire Protocol
    humanURL: https://clickhouse.com/docs/en/interfaces/postgresql
    properties:
      - url: https://clickhouse.com/docs/en/interfaces/postgresql
        type: Documentation
    description: PostgreSQL wire protocol compatibility for connecting psql, JDBC and other PostgreSQL clients to ClickHouse.
  - aid: clickhouse:clickhouse-grpc
    name: ClickHouse gRPC Interface
    tags:
      - gRPC
      - Protocol Buffers
    humanURL: https://clickhouse.com/docs/en/interfaces/grpc
    properties:
      - url: https://clickhouse.com/docs/en/interfaces/grpc
        type: Documentation
      - url: https://github.com/ClickHouse/ClickHouse/blob/master/src/Server/grpc_protos/clickhouse_grpc.proto
        type: Protocol Buffers
    description: gRPC interface defined by clickhouse_grpc.proto for efficient binary communication.
common:
  - type: Website
    url: https://clickhouse.com/
  - type: Documentation
    url: https://clickhouse.com/docs
  - type: Getting Started
    url: https://clickhouse.com/docs/en/getting-started
  - type: GitHub
    url: https://github.com/ClickHouse/ClickHouse
  - type: Blog
    url: https://clickhouse.com/blog
  - type: Community
    url: https://clickhouse.com/community
  - type: Slack
    url: https://clickhouse.com/slack
  - type: Pricing
    url: https://clickhouse.com/pricing
  - type: Support
    url: https://clickhouse.com/support
  - type: Status
    url: https://status.clickhouse.com/
  - type: Privacy Policy
    url: https://clickhouse.com/legal/privacy-policy
  - type: Terms of Service
    url: https://clickhouse.com/legal/terms-of-service
  - type: JSON-LD
    url: json-ld/clickhouse-context.jsonld
  - type: Spectral
    url: rules/clickhouse-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clickhouse-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
