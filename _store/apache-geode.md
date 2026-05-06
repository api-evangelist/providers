---
aid: apache-geode
name: Apache Geode
description: Apache Geode is an in-memory data management platform that provides real-time, consistent access to data-intensive applications throughout widely distributed cloud architectures. It pools memory, CPU, network resources, and local disk storage across multiple processes, offering a REST API for data access, OQL queries, function execution, and cluster management.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Caching
  - Data Grid
  - Distributed Systems
  - In-Memory
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-geode/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-geode:apache-geode-rest-api
    name: Apache Geode REST API
    description: REST API for accessing and managing data in Apache Geode in-memory data grid, including region operations, OQL queries, function execution, and cluster monitoring.
    humanURL: https://geode.apache.org/docs/guide/latest/rest_apps/chapter_overview.html
    baseURL: http://localhost:8080
    tags:
      - Cache
      - Data Grid
      - In-Memory
      - OQL
      - REST
    properties:
      - type: Documentation
        url: https://geode.apache.org/docs/guide/latest/rest_apps/chapter_overview.html
      - type: OpenAPI
        url: openapi/apache-geode-rest-openapi.yml
      - type: JSONSchema
        url: json-schema/geode-rest-region-info-schema.json
      - type: JSON-LD
        url: json-ld/apache-geode-rest-context.jsonld
  - aid: apache-geode:apache-geode-java-api
    name: Apache Geode Java Client API
    description: Java API for cache operations, continuous queries, function execution, and data serialization in Apache Geode clusters.
    humanURL: https://geode.apache.org/docs/guide/latest/developing/book_intro.html
    tags:
      - Java
      - SDK
      - Cache
      - Continuous Query
    properties:
      - type: Documentation
        url: https://geode.apache.org/docs/guide/latest/developing/book_intro.html
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.geode/geode-core
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://geode.apache.org/docs/
  - type: GettingStarted
    url: https://geode.apache.org/docs/guide/latest/getting_started/book_intro.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/geode
  - type: Blog
    url: https://geode.apache.org/blog/
  - type: SpectralRules
    url: rules/apache-geode-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-geode-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/geode-data-management.yaml
  - type: Features
    data:
      - name: In-Memory Data Grid
        description: Pool memory across distributed nodes for consistent sub-millisecond data access at scale.
      - name: REST Data API
        description: HTTP REST API for language-agnostic CRUD operations on Geode regions using JSON.
      - name: OQL Query Language
        description: SQL-like Object Query Language for executing complex queries against in-memory data.
      - name: Continuous Queries
        description: Register interest in data changes meeting OQL criteria for real-time event notification.
      - name: Server-Side Functions
        description: Deploy and execute Java functions on the cluster nodes to co-locate compute with data.
      - name: ACID Transactions
        description: Full ACID transaction support for consistent multi-region data operations.
      - name: WAN Replication
        description: Asynchronous and synchronous WAN gateway replication for geo-distributed data consistency.
      - name: Eviction and Expiration
        description: Configurable eviction policies (LRU, heap, disk) and TTL-based entry expiration.
      - name: Persistence
        description: Disk persistence option for data recovery after restart without network re-loading.
      - name: Native Clients
        description: High-performance C++ and .NET native client libraries for non-JVM applications.
  - type: UseCases
    data:
      - name: Session Caching
        description: Replace Redis or Memcached with Geode for distributed session caching with ACID guarantees.
      - name: Real-Time Analytics
        description: Perform OQL queries on in-flight event data for real-time analytical processing.
      - name: Financial Transaction Processing
        description: Low-latency transaction processing with ACID guarantees for financial trading and payments.
      - name: Microservices Shared State
        description: Share state between microservices with consistent in-memory data across distributed nodes.
      - name: IoT Data Aggregation
        description: Aggregate and query high-velocity IoT telemetry data in memory for real-time responses.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Geode-Spark connector for using Geode regions as Spark RDD/DataFrame data sources.
      - name: Spring Data Geode
        description: Spring Data integration for repository-based data access and caching annotations.
      - name: Kubernetes
        description: Kubernetes operator for deploying and managing Geode clusters on Kubernetes.
      - name: Pivotal Cloud Foundry
        description: Cloud Foundry service broker for provisioning Geode instances as managed services.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
