---
aid: tidb
url: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/apis.yml
apis:
  - aid: tidb:tidb-cloud-api
    name: TiDB Cloud API
    tags:
      - Cloud
      - Cluster Management
      - Database
      - Distributed SQL
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.tidbcloud.com
    humanURL: https://docs.pingcap.com/tidbcloud/api-overview/
    properties:
      - url: https://docs.pingcap.com/tidbcloud/api-overview/
        type: Documentation
      - url: https://docs.pingcap.com/tidbcloud/api/v1beta/
        type: Documentation
      - url: openapi/tidb-cloud-api-openapi.yml
        type: OpenAPI
      - url: json-schema/tidb-cluster-schema.json
        type: JSONSchema
    description: The TiDB Cloud API is a REST interface that provides programmatic access to manage administrative objects within TiDB Cloud. It supports managing projects, clusters, backups, restores, data imports, billing, and private endpoint connections across both TiDB Cloud Serverless and TiDB Cloud Dedicated tiers. The API uses digest authentication with public and private API keys and returns JSON-formatted responses.
  - aid: tidb:tidb-cloud-data-service-api
    name: TiDB Cloud Data Service API
    tags:
      - Cloud
      - Data Access
      - Database
      - REST
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://data.tidbcloud.com
    humanURL: https://docs.pingcap.com/tidbcloud/data-service-overview/
    properties:
      - url: https://docs.pingcap.com/tidbcloud/data-service-overview/
        type: Documentation
      - url: https://docs.pingcap.com/tidbcloud/data-service-get-started/
        type: Documentation
      - url: openapi/tidb-cloud-data-service-openapi.yml
        type: OpenAPI
      - url: json-schema/tidb-data-service-schema.json
        type: JSONSchema
    description: TiDB Cloud Data Service enables developers to access TiDB Cloud data via HTTPS requests using custom API endpoints backed by SQL queries. Developers define endpoints within a Data App, specifying the HTTP method, path, and the SQL logic that the endpoint executes against a linked TiDB Cloud cluster. Endpoints support GET, POST, PUT, and DELETE methods, return JSON-formatted results, and can be configured with pagination, rate limiting, and caching.
  - aid: tidb:tidb-cloud-chat2query-api
    name: TiDB Cloud Chat2Query API
    tags:
      - AI
      - Cloud
      - Database
      - Natural Language
      - SQL Generation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://data.tidbcloud.com
    humanURL: https://docs.pingcap.com/tidbcloud/use-chat2query-api/
    properties:
      - url: https://docs.pingcap.com/tidbcloud/use-chat2query-api/
        type: Documentation
      - url: openapi/tidb-cloud-chat2query-openapi.yml
        type: OpenAPI
    description: The TiDB Cloud Chat2Query API is an AI-powered interface that allows developers to generate and execute SQL statements against TiDB Cloud clusters using natural language instructions. It is exposed as a special Data App within TiDB Cloud and authenticated via API keys scoped to the Chat2Query Data App.
  - aid: tidb:tidb-http-api
    name: TiDB HTTP API
    tags:
      - Database
      - Monitoring
      - Operations
      - Self-Managed
      - Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://localhost:10080
    humanURL: https://github.com/pingcap/tidb/blob/master/docs/tidb_http_api.md
    properties:
      - url: https://github.com/pingcap/tidb/blob/master/docs/tidb_http_api.md
        type: Documentation
      - url: https://docs.pingcap.com/tidb/stable/tidb-monitoring-api/
        type: Documentation
      - url: openapi/tidb-http-api-openapi.yml
        type: OpenAPI
    description: The TiDB HTTP API is a built-in administrative interface available on self-managed TiDB server instances, accessible on port 10080 by default. It exposes endpoints for retrieving server status, database and table schema information, region metadata, MVCC key details, DDL job history, and hot region data. Operators and monitoring systems use this API to inspect the internal state of a running TiDB node, integrate with observability tooling, and troubleshoot distributed SQL execution.
common:
  - type: JSON-LD
    url: json-ld/tidb-context.jsonld
  - type: JSONSchema
    url: json-schema/tidb-cluster-schema.json
  - type: JSONSchema
    url: json-schema/tidb-data-service-schema.json
  - type: Spectral
    url: rules/tidb-rules.yml
  - type: Vocabulary
    url: vocabulary/tidb-vocabulary.yml
modified: '2026-05-03'
description: TiDB is an open-source distributed SQL database that supports Hybrid Transactional and Analytical Processing workloads, with horizontal scalability, strong consistency, and high availability.
---
