---
aid: apache-ignite
name: Apache Ignite
description: Apache Ignite is a distributed database for mission-critical high-velocity applications requiring in-memory performance. It provides ACID transactions, SQL queries, key-value storage, compute grid, and backpressured streaming across distributed clusters. Governed by the Apache Software Foundation under the Apache 2.0 license.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Caching
  - Compute Grid
  - Distributed Database
  - In-Memory
  - Open Source
  - SQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-ignite/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-ignite:rest-api
    name: Apache Ignite REST API
    description: The Ignite 3 REST API provides HTTP endpoints for cluster initialization, cluster management, node management, SQL query execution, configuration management, and deployment unit management.
    humanURL: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/rest/rest-api
    tags:
      - Cluster Management
      - Configuration
      - REST
      - SQL
    properties:
      - type: Documentation
        url: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/rest/rest-api
      - type: OpenAPI
        url: openapi/apache-ignite-rest-api.yaml
  - aid: apache-ignite:java-api
    name: Apache Ignite Java Client API
    description: The Ignite Java client API provides native Java access to Ignite clusters for table operations, SQL queries, transactions, and compute task execution.
    humanURL: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/clients/java
    tags:
      - Java
      - SDK
    properties:
      - type: Documentation
        url: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/clients/java
      - type: GettingStarted
        url: https://ignite.apache.org/docs/ignite3/3.1.0/getting-started/quick-start
  - aid: apache-ignite:dotnet-api
    name: Apache Ignite .NET Client API
    description: The Ignite .NET client API provides native C# and .NET access to Ignite clusters for table operations, SQL queries, and distributed computing.
    humanURL: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/clients/dotnet
    tags:
      - .NET
      - C#
      - SDK
    properties:
      - type: Documentation
        url: https://ignite.apache.org/docs/ignite3/3.1.0/developers-guide/clients/dotnet
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/ignite-3
  - type: Documentation
    url: https://ignite.apache.org/docs/ignite3/3.1.0/
  - type: GettingStarted
    url: https://ignite.apache.org/docs/ignite3/3.1.0/getting-started/quick-start
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://ignite.apache.org/releases/
  - type: SpectralRules
    url: rules/apache-ignite-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-ignite-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cluster-management.yaml
  - type: Features
    data:
      - name: In-Memory Speed
        description: Memory-first storage with MVCC for consistent high-velocity performance.
      - name: ACID Transactions
        description: Full ACID transactions across distributed cluster nodes.
      - name: SQL Support
        description: ANSI SQL-compliant queries across distributed tables with JDBC/ODBC drivers.
      - name: Key-Value Storage
        description: Native key-value API for direct cache access without SQL overhead.
      - name: Compute Grid
        description: Distributed compute tasks co-located with data for low-latency processing.
      - name: Multi-Language Clients
        description: Native clients for Java, .NET, C++, and Python.
      - name: Schema Evolution
        description: Online schema changes without cluster downtime.
      - name: Backpressured Streaming
        description: Event stream ingestion and enrichment with flow control.
  - type: UseCases
    data:
      - name: Event Stream Processing
        description: Ingest, enrich, and process high-velocity event streams with in-memory speed.
      - name: Microservices State Management
        description: Distributed state store for microservices with ACID guarantees.
      - name: Session Management
        description: High-speed session caching for web applications.
      - name: AI/ML Feature Store
        description: Low-latency feature serving for machine learning model inference.
      - name: Real-Time Analytics
        description: SQL analytics over continuously updated distributed datasets.
  - type: Integrations
    data:
      - name: Spring Boot
        description: Native Spring Boot integration for Ignite cluster connectivity.
      - name: Apache Kafka
        description: Stream data from Kafka topics into Ignite tables for real-time processing.
      - name: JDBC
        description: Standard JDBC driver for connecting SQL tools to Ignite clusters.
      - name: ODBC
        description: ODBC driver for BI tool integration with Ignite SQL engine.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
