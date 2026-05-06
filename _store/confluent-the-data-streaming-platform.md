---
aid: confluent-the-data-streaming-platform
name: Confluent | the Data Streaming Platform
description: Confluent is a fully managed data streaming platform built by the original creators of Apache Kafka. It lets organizations stream, connect, process, and govern data in motion through a cloud-native service (Confluent Cloud) and the on-prem/self-managed Confluent Platform. Confluent's developer surface includes the Confluent Cloud REST API for managing clusters, environments, and access; the Kafka REST Proxy for producing and consuming events over HTTP; the Schema Registry REST API for governance of Avro, JSON Schema, and Protobuf schemas; the Kafka Connect REST API for managing connectors; the ksqlDB REST API for stream processing; and managed Apache Flink. Authentication is API-key based (Cloud) or HTTP/mTLS/OAuth (Platform).
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/apis.yml
created: '2025-08-19'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Apache Flink
  - Apache Kafka
  - Confluent Cloud
  - Connectors
  - Data Streaming
  - Event Streaming
  - Kafka Connect
  - ksqlDB
  - Real-Time Data
  - REST
  - Schema Registry
  - Stream Processing
apis:
  - aid: confluent-the-data-streaming-platform:cloud-rest-api
    name: Confluent Cloud REST API
    description: The Confluent Cloud REST API is the management plane for Confluent Cloud. It is used to manage organizations, environments, Kafka and Flink clusters, service accounts, API keys, role bindings, networking, schema registry clusters, and connector instances. The API uses Cloud API keys for authentication and follows Confluent's resource-oriented v2 conventions.
    humanURL: https://docs.confluent.io/cloud/current/api.html
    baseURL: https://api.confluent.cloud
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Confluent Cloud
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://docs.confluent.io/cloud/current/api.html
      - type: API Reference
        url: https://docs.confluent.io/cloud/current/api.html
    x-features:
      - Cluster Lifecycle Management
      - Environments and Organizations
      - API Key Management
      - RBAC and Service Accounts
      - Networking and Private Link
      - Schema Registry Cluster Management
      - Connector Provisioning
      - Flink Compute Pools
    x-use-cases:
      - Provision Kafka clusters in Confluent Cloud
      - Automate environment and access management
      - Rotate API keys and manage service accounts
      - Wire up private networking for clusters
      - Manage Flink compute pools and statements
  - aid: confluent-the-data-streaming-platform:kafka-rest-api
    name: Confluent Kafka REST API
    description: The Kafka REST API (Confluent REST Proxy in self-managed deployments, Kafka REST in Cloud) provides HTTP access to Apache Kafka topics, consumers, partitions, brokers, and ACLs. Clients without a native Kafka library can produce and consume records, manage topics, and inspect metadata over HTTP. Cloud variants additionally enforce RBAC and Confluent Cloud authentication.
    humanURL: https://docs.confluent.io/platform/current/kafka-rest/api.html
    baseURL: https://pkc-XXXXX.region.aws.confluent.cloud
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Apache Kafka
      - Producer
      - Consumer
      - REST
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/kafka-rest/api.html
      - type: Cloud Documentation
        url: https://docs.confluent.io/cloud/current/kafka-rest/index.html
    x-features:
      - Topic Management
      - Produce and Consume over HTTP
      - Partition Inspection
      - Consumer Group Management
      - Broker Metadata
      - ACL Management
    x-use-cases:
      - Produce events from clients without a Kafka library
      - Bridge legacy systems to Kafka over HTTP
      - Inspect topic and partition metadata from web tools
      - Manage ACLs from automation scripts
  - aid: confluent-the-data-streaming-platform:schema-registry-api
    name: Confluent Schema Registry REST API
    description: The Schema Registry REST API stores and serves Avro, JSON Schema, and Protobuf schemas with versioning and compatibility enforcement. It is available both as a managed Confluent Cloud service and as a self-managed component of Confluent Platform. The full developer profile lives in the api-evangelist/confluent-schema-registry repository.
    humanURL: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
    baseURL: https://psrc-XXXXX.region.aws.confluent.cloud
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Avro
      - JSON Schema
      - Protobuf
      - Schema Registry
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
      - type: Companion Repo
        url: https://github.com/api-evangelist/confluent-schema-registry
    x-features:
      - Avro/JSON Schema/Protobuf Support
      - Compatibility Enforcement
      - Schema Versioning
      - Schema References
      - Schema Linking
    x-use-cases:
      - Govern data contracts across producers and consumers
      - Evolve schemas with backward and forward compatibility
      - Share schemas across environments via Schema Linking
  - aid: confluent-the-data-streaming-platform:connect-rest-api
    name: Kafka Connect REST API
    description: The Kafka Connect REST API manages connectors, tasks, and worker configuration. Operators use it to deploy, configure, pause, resume, and delete source and sink connectors, inspect task status, and restart failed tasks. In Confluent Cloud, managed connectors are provisioned through the Cloud REST API while runtime status is exposed via the Connect REST surface.
    humanURL: https://docs.confluent.io/platform/current/connect/references/restapi.html
    baseURL: https://localhost:8083
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Connectors
      - Kafka Connect
      - REST
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/connect/references/restapi.html
    x-features:
      - Connector Lifecycle Management
      - Task Status and Restart
      - Plugin Discovery
      - Configuration Validation
    x-use-cases:
      - Deploy and operate source/sink connectors
      - Restart failed tasks programmatically
      - Validate connector configurations in CI
  - aid: confluent-the-data-streaming-platform:ksqldb-rest-api
    name: ksqlDB REST API
    description: The ksqlDB REST API exposes ksqlDB, Confluent's streaming SQL engine, over HTTP. Clients submit streaming SQL statements, query streams and tables (push and pull queries), and inspect server status.
    humanURL: https://docs.ksqldb.io/en/latest/developer-guide/api/
    baseURL: https://localhost:8088
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - ksqlDB
      - REST
      - Streaming SQL
    properties:
      - type: Documentation
        url: https://docs.ksqldb.io/en/latest/developer-guide/api/
    x-features:
      - Push and Pull Queries
      - Streaming SQL Execution
      - Server Health and Status
    x-use-cases:
      - Run streaming SQL from web applications
      - Build real-time materialized views
      - Power dashboards with push queries
  - aid: confluent-the-data-streaming-platform:flink-rest-api
    name: Confluent Cloud for Apache Flink REST API
    description: The Confluent Cloud for Apache Flink REST API manages Flink compute pools, statements, and workspaces for stateful stream processing on Confluent Cloud. It is part of the Confluent Cloud REST surface.
    humanURL: https://docs.confluent.io/cloud/current/flink/index.html
    baseURL: https://flink.region.aws.confluent.cloud
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Apache Flink
      - Stream Processing
    properties:
      - type: Documentation
        url: https://docs.confluent.io/cloud/current/flink/index.html
    x-features:
      - Flink Compute Pools
      - Flink SQL Statements
      - Workspace Management
    x-use-cases:
      - Run stateful stream processing on Confluent Cloud
      - Deploy Flink SQL jobs through automation
common:
  - type: Website
    url: https://www.confluent.io/
  - type: Developer Portal
    url: https://developer.confluent.io/
  - type: Documentation
    url: https://docs.confluent.io/
  - type: Cloud API Reference
    url: https://docs.confluent.io/cloud/current/api.html
  - type: GitHub
    url: https://github.com/confluentinc
  - type: Blog
    url: https://www.confluent.io/blog/
  - type: Pricing
    url: https://www.confluent.io/pricing/
  - type: Status
    url: https://status.confluent.cloud/
  - type: Login
    url: https://confluent.cloud/login
  - type: Marketplace
    url: https://www.confluent.io/hub/
  - type: Training
    url: https://training.confluent.io/
  - type: Terms of Service
    url: https://www.confluent.io/terms-of-service/
  - type: Privacy Policy
    url: https://www.confluent.io/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
