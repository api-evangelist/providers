---
aid: akka
name: Akka
description: Akka is a toolkit and runtime for building highly concurrent, distributed, and resilient message-driven applications on the JVM using the actor model for Java and Scala. Maintained by Lightbend, Akka provides a comprehensive set of libraries including actors, HTTP, streams, cluster, persistence, and gRPC for building reactive, microservice-based architectures.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Actor Model
  - Distributed Systems
  - Frameworks
  - Java
  - Microservices
  - Reactive
  - Scala
url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: akka:akka-management
    name: Akka Management
    description: Akka Management provides a suite of utilities for operating Akka-based distributed systems, including an HTTP management API for cluster management, health checks, and cluster bootstrap. The HTTP API exposes endpoints for liveness probes, readiness probes, cluster member management, and seed node discovery.
    humanURL: https://doc.akka.io/libraries/akka-management/current/
    tags:
      - Actor Model
      - Cluster Management
      - Distributed Systems
      - Health Checks
    properties:
      - type: Documentation
        url: https://doc.akka.io/libraries/akka-management/current/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/openapi/akka-management.json
  - aid: akka:akka-http
    name: Akka HTTP
    description: Akka HTTP is a full HTTP stack (client and server-side) built on Akka actors and streams. It provides a routing DSL for building REST and WebSocket services, with built-in JSON marshalling, TLS support, and HTTP/2 capabilities.
    humanURL: https://doc.akka.io/libraries/akka-http/current/
    tags:
      - HTTP
      - REST API
      - Reactive
      - Streaming
    properties:
      - type: Documentation
        url: https://doc.akka.io/libraries/akka-http/current/
      - type: GettingStarted
        url: https://doc.akka.io/libraries/akka-http/current/introduction.html
  - aid: akka:akka-streams
    name: Akka Streams
    description: Akka Streams is a library to process and transfer a sequence of elements using bounded buffer space, implementing the Reactive Streams specification for asynchronous stream processing with non-blocking backpressure.
    humanURL: https://doc.akka.io/libraries/akka/current/stream/index.html
    tags:
      - Backpressure
      - Data Streaming
      - Reactive
      - Reactive Streams
    properties:
      - type: Documentation
        url: https://doc.akka.io/libraries/akka/current/stream/index.html
  - aid: akka:akka-grpc
    name: Akka gRPC
    description: Akka gRPC provides support for building streaming gRPC servers and clients on top of Akka Streams, with code generation from protobuf definitions for both Java and Scala.
    humanURL: https://doc.akka.io/libraries/akka-grpc/current/
    tags:
      - gRPC
      - Protobuf
      - Streaming
    properties:
      - type: Documentation
        url: https://doc.akka.io/libraries/akka-grpc/current/
common:
  - type: Website
    url: https://akka.io/
  - type: Documentation
    url: https://doc.akka.io/
  - type: GettingStarted
    url: https://doc.akka.io/libraries/akka/current/typed/guide/introduction.html
  - type: GitHubOrganization
    url: https://github.com/akka
  - type: Blog
    url: https://akka.io/blog/
  - type: Pricing
    url: https://akka.io/pricing/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/json-schema/akka-config.json
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/rules/akka-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/vocabulary/akka-vocabulary.yaml
  - type: Features
    data:
      - name: Actor Model
        description: Lightweight concurrent entities (actors) that communicate via asynchronous message passing, enabling high-throughput distributed computation.
      - name: Cluster Sharding
        description: Distributes actors across a cluster and automatically rebalances them when nodes join or leave the cluster.
      - name: Persistence and Event Sourcing
        description: Durable actor state through event sourcing with pluggable journal backends (Cassandra, PostgreSQL, DynamoDB, etc.).
      - name: Distributed Data
        description: Conflict-free replicated data types (CRDTs) for sharing data across cluster nodes without coordination overhead.
      - name: HTTP and WebSocket
        description: Full HTTP/1.1 and HTTP/2 server and client stack with routing DSL, JSON support, and WebSocket upgrades.
      - name: Reactive Streams
        description: Backpressure-aware stream processing compliant with the Reactive Streams specification, integrating with RxJava, Project Reactor, and others.
  - type: UseCases
    data:
      - name: Microservices
        description: Teams build resilient, location-transparent microservices using Akka actors and HTTP with built-in backpressure and supervision.
      - name: Real-Time Data Processing
        description: Organizations process high-throughput event streams using Akka Streams with exactly-once processing guarantees.
      - name: Distributed State Management
        description: Applications maintain distributed mutable state using cluster sharding and distributed data without external coordination systems.
      - name: Event Sourcing
        description: Systems implement event sourcing and CQRS patterns using Akka Persistence with pluggable journal backends.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Alpakka Kafka connector for consuming and producing Kafka messages
      - name: Cassandra
        description: Alpakka Cassandra connector and Akka Persistence journal
      - name: AWS
        description: Alpakka connectors for S3, SQS, SNS, DynamoDB, and other AWS services
      - name: gRPC
        description: Akka gRPC for code generation from protobuf and streaming gRPC services
      - name: Spring Boot
        description: Integration with Spring Boot for mixed Akka and Spring applications
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
