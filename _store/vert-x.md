---
aid: vert-x
name: Vert.x
description: Eclipse Vert.x is a toolkit for building reactive applications on the JVM, providing support for multiple languages including Java, JavaScript, Groovy, Ruby, and Kotlin with an event-driven, non-blocking architecture. Part of the Eclipse Foundation under the Eclipse Public License 2.0. Vert.x follows a polyglot, unopinionated model allowing developers to build microservices, web applications, IoT backends, and event-driven systems with high concurrency using a small memory footprint.
type: Index
image: https://vertx.io/images/logo-wide.png
tags:
  - Event-Driven
  - Frameworks
  - Java
  - JVM
  - Microservices
  - Polyglot
  - Reactive
  - Eclipse Foundation
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vert-x:vert-x-core
    name: Vert.x Core
    description: The core toolkit for building reactive, event-driven applications on the JVM. Provides the event loop, verticle deployment, event bus, HTTP server and client, TCP/UDP networking, and the fundamental async programming model used by all Vert.x components.
    humanURL: https://vertx.io/docs/vertx-core/java/
    tags:
      - Event-Driven
      - Event Loop
      - Verticles
      - Event Bus
      - Reactive
      - JVM
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-core/java/
      - type: GettingStarted
        url: https://vertx.io/get-started/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vert.x
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-core
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-schema/vertx-config.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-structure/vertx-config-structure.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-schema/vertx-deployment-descriptor.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-structure/vertx-deployment-descriptor-structure.json
  - aid: vert-x:vertx-web
    name: Vert.x Web
    description: A set of building blocks for building web applications and RESTful HTTP microservices with Vert.x. Provides routing, request handling, session management, template engine support, and WebSocket handling on top of Vert.x Core HTTP server.
    humanURL: https://vertx.io/docs/vertx-web/java/
    tags:
      - REST
      - HTTP
      - Web Framework
      - Routing
      - WebSocket
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-web/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vert.x
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-web
  - aid: vert-x:vertx-openapi
    name: Vert.x OpenAPI
    description: Vert.x OpenAPI provides OpenAPI 3.1 specification support for Vert.x, enabling contract-driven API development with automatic request/response validation, routing, and API specification serving for Vert.x Web applications.
    humanURL: https://vertx.io/docs/vertx-openapi/java/
    tags:
      - OpenAPI
      - API Specification
      - Validation
      - Contract-Driven
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-openapi/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vertx-openapi
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-openapi
  - aid: vert-x:vertx-grpc
    name: Vert.x gRPC
    description: A Vert.x-native gRPC implementation providing a reactive, non-blocking gRPC client and server built on top of Vert.x HTTP/2. Supports protobuf service definitions with Vert.x Future and stream-based APIs.
    humanURL: https://vertx.io/docs/vertx-grpc/java/
    tags:
      - gRPC
      - Protocol Buffers
      - HTTP/2
      - Streaming
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-grpc/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vertx-grpc
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-grpc
  - aid: vert-x:vertx-sql-client
    name: Vert.x SQL Client
    description: A high-performance reactive SQL client for Vert.x supporting PostgreSQL, MySQL, Microsoft SQL Server, IBM DB2, and Oracle databases. Provides a non-blocking, fully reactive API for executing queries, transactions, and batch operations.
    humanURL: https://vertx.io/docs/vertx-pg-client/java/
    tags:
      - SQL
      - Database
      - PostgreSQL
      - MySQL
      - Reactive
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-pg-client/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vertx-sql-client
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-pg-client
  - aid: vert-x:vertx-auth
    name: Vert.x Auth
    description: Authentication and authorization support for Vert.x applications. Provides JWT, OAuth2, JDBC, MongoDB, and WebAuthn/FIDO2 authentication providers with a unified async security API that integrates with Vert.x Web routing.
    humanURL: https://vertx.io/docs/vertx-auth-common/java/
    tags:
      - Authentication
      - Authorization
      - JWT
      - OAuth2
      - Security
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-auth-common/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vertx-auth
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-auth-common
  - aid: vert-x:vertx-health-check
    name: Vert.x Health Check
    description: A Vert.x component for implementing health check endpoints for Kubernetes liveness and readiness probes. Provides a composable health procedure mechanism that aggregates multiple health checks into a single HTTP endpoint response.
    humanURL: https://vertx.io/docs/vertx-health-check/java/
    tags:
      - Health Check
      - Kubernetes
      - Observability
      - Liveness
      - Readiness
    properties:
      - type: Documentation
        url: https://vertx.io/docs/vertx-health-check/java/
      - type: GitHubRepository
        url: https://github.com/eclipse-vertx/vertx-health-check
      - type: MavenPackage
        url: https://central.sonatype.com/artifact/io.vertx/vertx-health-check
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-schema/vertx-health-check-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-structure/vertx-health-check-structure.json
common:
  - type: Website
    url: https://vertx.io/
  - type: Documentation
    url: https://vertx.io/docs/
  - type: GettingStarted
    url: https://vertx.io/get-started/
  - type: GitHubOrganization
    url: https://github.com/eclipse-vertx
  - type: Blog
    url: https://vertx.io/blog/
  - type: PrivacyPolicy
    url: https://www.eclipse.org/legal/privacy.php
  - type: TermsOfService
    url: https://www.eclipse.org/legal/termsofuse.php
  - type: License
    url: https://www.eclipse.org/legal/epl-2.0/
  - type: Changelog
    url: https://github.com/eclipse-vertx/vert.x/blob/master/CHANGELOG.adoc
  - type: MavenCentral
    url: https://central.sonatype.com/search?q=io.vertx
  - type: Forums
    url: https://groups.google.com/forum/#!forum/vertx
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/vert.x
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/vocabulary/vert-x-vocabulary.yaml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/rules/vert-x-spectral-rules.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-ld/vert-x-context.jsonld
  - type: Features
    data:
      - name: Event-Driven Architecture
        description: Non-blocking event loop model with verticles for concurrent request handling without traditional threading overhead.
      - name: Polyglot Support
        description: Write Vert.x applications in Java, JavaScript, Groovy, Kotlin, Scala, and Ruby on the same JVM platform.
      - name: Event Bus
        description: Distributed message-passing backbone enabling communication between verticles across nodes in a cluster.
      - name: Reactive HTTP Client and Server
        description: High-performance HTTP/1.1 and HTTP/2 server and client with WebSocket, SSE, and gRPC support.
      - name: OpenAPI Contract Validation
        description: Automatic request and response validation against OpenAPI 3.1 specifications using vertx-openapi.
      - name: Reactive SQL Clients
        description: Non-blocking, fully reactive SQL clients for PostgreSQL, MySQL, MSSQL, DB2, and Oracle.
      - name: Authentication and Authorization
        description: Pluggable security providers for JWT, OAuth2, JDBC, MongoDB, LDAP, and WebAuthn/FIDO2.
      - name: Health Checks
        description: Composable health check procedures for Kubernetes liveness and readiness probe endpoints.
      - name: Clustering
        description: Built-in cluster support via Hazelcast, Infinispan, Zookeeper, or Apache Ignite for distributed deployments.
      - name: Virtual Threads
        description: Java 21 virtual thread support enabling synchronous-style code in Vert.x worker verticles.
  - type: UseCases
    data:
      - name: Microservices Backend
        description: Build lightweight, high-concurrency microservices with Vert.x Web routing, service proxy patterns, and event bus communication.
      - name: API Gateway
        description: Implement reactive API gateways using vertx-http-proxy with routing, authentication, and rate limiting.
      - name: Real-Time Applications
        description: Build WebSocket and SSE-based real-time applications for live dashboards, chat, and notification systems.
      - name: IoT Data Ingestion
        description: Handle high-volume MQTT and TCP data streams from IoT devices using Vert.x non-blocking networking.
      - name: Contract-First REST APIs
        description: Develop OpenAPI 3.1 contract-first REST APIs with automatic validation using vertx-openapi and vertx-web.
  - type: Integrations
    data:
      - name: Quarkus
        description: Vert.x is the reactive engine underlying Quarkus, providing the event loop and HTTP server for Quarkus applications.
      - name: Kubernetes
        description: Deploy Vert.x verticles on Kubernetes with health check endpoints, clustering, and horizontal pod autoscaling.
      - name: Apache Kafka
        description: Vert.x Kafka Client provides reactive, non-blocking Kafka producer and consumer integration.
      - name: Redis
        description: Vert.x Redis Client enables async Redis operations for caching, pub/sub, and session storage.
      - name: Hazelcast
        description: Hazelcast cluster manager for distributed Vert.x deployments with shared data and event bus clustering.
      - name: Micrometer
        description: Vert.x Micrometer Metrics provides application metrics integration with Prometheus and Grafana.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
