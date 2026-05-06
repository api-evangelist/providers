---
aid: cassandra
url: https://raw.githubusercontent.com/api-evangelist/cassandra/refs/heads/main/apis.yml
name: Apache Cassandra
tags:
  - Apache
  - Big Data
  - Database
  - Distributed
  - NoSQL
  - Open Source
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-23'
position: Consumer
description: Apache Cassandra is a highly scalable, distributed open-source NoSQL database designed to handle massive amounts of data across many commodity servers, providing high availability with no single point of failure. It is governed by the Apache Software Foundation (ASF) under the Apache License 2.0 and is used in production by Netflix, Apple, Bloomberg, Backblaze, and many others. Cassandra exposes its CQL native protocol for clients and a family of HTTP, REST, GraphQL, Document, and gRPC APIs via the Stargate data gateway.
apis:
  - aid: cassandra:cassandra-cql-native-protocol
    name: Apache Cassandra CQL Native Protocol
    tags:
      - CQL
      - Database
      - Native Protocol
      - Query
    humanURL: https://cassandra.apache.org/doc/latest/cassandra/cql/
    properties:
      - url: https://cassandra.apache.org/doc/latest/cassandra/cql/
        type: Documentation
      - url: https://github.com/apache/cassandra/blob/trunk/doc/native_protocol_v5.spec
        type: Specification
      - url: https://cassandra.apache.org/doc/latest/cassandra/cql/ddl.html
        type: Reference
    description: Cassandra Query Language (CQL) is the primary interface to Apache Cassandra. Clients speak the binary CQL native protocol over TCP (default port 9042). Official drivers are maintained for Java, Python, Go, C/C++, C#, Node.js, Ruby, and Rust.
  - aid: cassandra:cassandra-rest-api-stargate
    name: Cassandra REST API (Stargate)
    tags:
      - Database
      - REST
      - Stargate
    humanURL: https://stargate.io/docs/latest/develop/api-rest/
    properties:
      - url: https://stargate.io/docs/latest/develop/api-rest/
        type: Documentation
      - url: https://stargate.io/docs/latest/develop/api-rest/swagger.html
        type: Swagger
      - url: https://github.com/stargate/stargate
        type: SourceCode
    description: HTTP/JSON REST API for Cassandra provided by the Stargate data gateway. Enables CRUD operations and SQL-like query via REST without the CQL driver.
  - aid: cassandra:cassandra-graphql-api-stargate
    name: Cassandra GraphQL API (Stargate)
    tags:
      - Database
      - GraphQL
      - Stargate
    humanURL: https://stargate.io/docs/latest/develop/api-graphql/
    properties:
      - url: https://stargate.io/docs/latest/develop/api-graphql/
        type: Documentation
      - url: https://stargate.io/docs/latest/develop/api-graphql/graphql-using.html
        type: Reference
    description: GraphQL endpoint for Cassandra, enabling flexible, typed queries and mutations against Cassandra tables through the Stargate gateway.
  - aid: cassandra:cassandra-document-api-stargate
    name: Cassandra Document API (Stargate)
    tags:
      - Database
      - Document
      - JSON
      - Stargate
    humanURL: https://stargate.io/docs/latest/develop/api-doc/
    properties:
      - url: https://stargate.io/docs/latest/develop/api-doc/
        type: Documentation
      - url: https://stargate.io/docs/latest/develop/api-doc/doc-using.html
        type: Reference
    description: Schemaless Document API that stores JSON documents in Cassandra, offering a MongoDB-like developer experience backed by Cassandra.
  - aid: cassandra:cassandra-grpc-api-stargate
    name: Cassandra gRPC API (Stargate)
    tags:
      - Database
      - gRPC
      - Stargate
    humanURL: https://stargate.io/docs/latest/develop/api-grpc/
    properties:
      - url: https://stargate.io/docs/latest/develop/api-grpc/
        type: Documentation
      - url: https://github.com/stargate/stargate/tree/main/grpc/proto
        type: Protocol
    description: High-performance gRPC API for Cassandra through Stargate, designed for low-latency service-to-service communication.
  - aid: cassandra:cassandra-jmx-metrics
    name: Cassandra JMX Management Interface
    tags:
      - JMX
      - Management
      - Metrics
      - Monitoring
    humanURL: https://cassandra.apache.org/doc/latest/cassandra/operating/metrics.html
    properties:
      - url: https://cassandra.apache.org/doc/latest/cassandra/operating/metrics.html
        type: Documentation
      - url: https://cassandra.apache.org/doc/latest/cassandra/operating/
        type: OperationsGuide
    description: Java Management Extensions (JMX) interface for monitoring and administering Cassandra nodes, including metrics, compaction, repairs, and configuration.
common:
  - type: Website
    url: https://cassandra.apache.org/
  - type: Documentation
    url: https://cassandra.apache.org/doc/latest/
  - type: GettingStarted
    url: https://cassandra.apache.org/doc/latest/cassandra/getting_started/
  - type: Download
    url: https://cassandra.apache.org/download/
  - type: SourceCode
    url: https://github.com/apache/cassandra
  - type: GitHub
    url: https://github.com/apache/cassandra
  - type: IssueTracker
    url: https://issues.apache.org/jira/projects/CASSANDRA
  - type: Blog
    url: https://cassandra.apache.org/blog/
  - type: Community
    url: https://cassandra.apache.org/community/
  - type: MailingList
    url: https://cassandra.apache.org/community/#discussions
  - type: Slack
    url: https://cassandra.apache.org/community/#slack
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/cassandra
  - type: X
    url: https://twitter.com/cassandra
  - type: LinkedIn
    url: https://www.linkedin.com/company/apache-cassandra/
  - type: YouTube
    url: https://www.youtube.com/@PlanetCassandra
  - type: DockerHub
    url: https://hub.docker.com/_/cassandra
  - type: PackageRegistry
    url: https://central.sonatype.com/artifact/org.apache.cassandra/cassandra-all
  - type: License
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Governance
    url: https://www.apache.org/foundation/governance/
  - type: SecurityPolicy
    url: https://cassandra.apache.org/_/security.html
  - type: PrivacyPolicy
    url: https://www.apache.org/privacy/
  - type: TermsOfService
    url: https://www.apache.org/foundation/license-faq.html
  - type: Ecosystem
    url: https://cassandra.apache.org/_/ecosystem.html
  - type: ThirdParty
    url: https://cassandra.apache.org/_/ecosystem.html
  - name: Features
    type: Features
    data:
      - name: Distributed
      - name: Masterless
      - name: Linear Scalability
      - name: Multi-Datacenter Replication
      - name: High Availability
      - name: Fault Tolerance
      - name: Tunable Consistency
      - name: CQL Query Language
      - name: Secondary Indexes
      - name: Materialized Views
      - name: User Defined Types
      - name: User Defined Functions
      - name: Vector Search
      - name: Time Series Storage
      - name: Cross-Region Replication
      - name: Role Based Access Control
      - name: TLS/SSL Encryption
      - name: At-Rest Encryption
      - name: Snapshot Backups
      - name: Incremental Repairs
      - name: Apache License 2.0
  - name: UseCases
    type: UseCases
    data:
      - name: Event Logging
      - name: IoT Telemetry
      - name: Time Series Data
      - name: Product Catalogs
      - name: Messaging Platforms
      - name: Fraud Detection
      - name: Recommendation Engines
      - name: Activity Feeds
      - name: Audit Logs
      - name: Real-Time Analytics
      - name: Mobile Application Backends
      - name: Vector Similarity Search
maintainers:
  - FN: Apache Cassandra Community
    email: dev@cassandra.apache.org
specificationVersion: '0.19'
---
