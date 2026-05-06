---
aid: tinybird
name: Tinybird
description: Tinybird is a real-time data platform that allows you to ingest, process, and expose data through low-latency, high-concurrency APIs. The platform supports real-time analytics at scale with a SQL-based transformation layer and instant REST API endpoint publishing.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Data
  - Real-Time
  - SQL
  - Streaming
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tinybird:tinybird
    name: Tinybird API
    description: Tinybird provides a real-time data platform with comprehensive REST APIs for managing data sources, executing SQL queries, managing pipes and transformations, ingesting events, managing authentication tokens, monitoring jobs, and administering organizations and workspaces.
    humanURL: https://www.tinybird.co/docs/api-reference
    baseURL: https://api.tinybird.co
    tags:
      - Analytics
      - Data
      - Real-Time
      - SQL
      - Streaming
    properties:
      - type: Documentation
        url: https://www.tinybird.co/docs/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/openapi/tinybird-openapi.yml
      - type: Getting Started
        url: https://www.tinybird.co/docs/get-started
      - type: Authentication
        url: https://www.tinybird.co/docs/api-reference/token-api
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/json-schema/tinybird-data-source-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/json-structure/tinybird-data-source-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/json-ld/tinybird-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/rules/tinybird-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/capabilities/real-time-analytics.yaml
features:
  - Real-time data ingestion via Events API
  - SQL-based data transformation with Pipes
  - Instant REST API endpoint publishing
  - Multi-region deployment support
  - Materialized views for query optimization
  - Sink pipes for data export
  - Token-based access control with scopes
  - Job tracking for async operations
  - Organization and workspace management
  - Environment variables for pipeline configuration
useCases:
  - Real-time analytics dashboards
  - User-facing analytics APIs
  - Event stream processing
  - Log analytics and monitoring
  - A/B testing and experimentation data
  - Financial data processing
  - IoT sensor data analytics
integrations:
  - Kafka data ingestion
  - DynamoDB connector
  - S3 data sources
  - Snowflake
  - Confluent
  - dbt transformations
  - TypeScript SDK
  - Python SDK
solutions:
  - Real-time API publishing
  - Analytics backend infrastructure
  - Data pipeline management
  - Multi-tenant data analytics
common:
  - type: Website
    url: https://www.tinybird.co/
  - type: Documentation
    url: https://www.tinybird.co/docs/api-reference
  - type: Getting Started
    url: https://www.tinybird.co/docs/get-started
  - type: Sign Up
    url: https://www.tinybird.co/signup
  - type: Blog
    url: https://www.tinybird.co/blog
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/openapi/tinybird-openapi.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/json-ld/tinybird-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/vocabulary/tinybird-vocabulary.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/rules/tinybird-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/tinybird/refs/heads/main/capabilities/real-time-analytics.yaml
  - type: GitHub Organization
    url: https://github.com/tinybirdco
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
