---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The core toolkit for building reactive, event-driven applications on the JVM. Provides the event loop, verticle deployment, event bus, HTTP server and client, TCP/UDP networking, and the fundamental a
  name: Vert.x Core
  slug: vert-x-core
- description: A set of building blocks for building web applications and RESTful HTTP microservices with Vert.x. Provides routing, request handling, session management, template engine support, and WebSocket handli
  name: Vert.x Web
  slug: vertx-web
- description: Vert.x OpenAPI provides OpenAPI 3.1 specification support for Vert.x, enabling contract-driven API development with automatic request/response validation, routing, and API specification serving for Ve
  name: Vert.x OpenAPI
  slug: vertx-openapi
- description: A Vert.x-native gRPC implementation providing a reactive, non-blocking gRPC client and server built on top of Vert.x HTTP/2. Supports protobuf service definitions with Vert.x Future and stream-based A
  name: Vert.x gRPC
  slug: vertx-grpc
- description: 'A high-performance reactive SQL client for Vert.x supporting PostgreSQL, MySQL, Microsoft SQL Server, IBM DB2, and Oracle databases. Provides a non-blocking, fully reactive API for executing queries, '
  name: Vert.x SQL Client
  slug: vertx-sql-client
- description: Authentication and authorization support for Vert.x applications. Provides JWT, OAuth2, JDBC, MongoDB, and WebAuthn/FIDO2 authentication providers with a unified async security API that integrates wit
  name: Vert.x Auth
  slug: vertx-auth
- description: 'A Vert.x component for implementing health check endpoints for Kubernetes liveness and readiness probes. Provides a composable health procedure mechanism that aggregates multiple health checks into a '
  name: Vert.x Health Check
  slug: vertx-health-check
artifact_total: 45
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vert-x-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vert-x-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vertx.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vertx.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://vertx.io/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eclipse-vertx
- group: company
  title: ''
  type: Blog
  url: https://vertx.io/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eclipse.org/legal/privacy.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eclipse.org/legal/termsofuse.php
- group: commercial
  title: ''
  type: License
  url: https://www.eclipse.org/legal/epl-2.0/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/eclipse-vertx/vert.x/blob/master/CHANGELOG.adoc
- group: other
  title: ''
  type: MavenCentral
  url: https://central.sonatype.com/search?q=io.vertx
- group: operate
  title: ''
  type: Forums
  url: https://groups.google.com/forum/#!forum/vertx
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/vert.x
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/vocabulary/vert-x-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/rules/vert-x-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/json-ld/vert-x-context.jsonld
created: '2026-03-26'
description: Eclipse Vert.x is a toolkit for building reactive applications on the JVM, providing support for multiple languages including Java, JavaScript, Groovy, Ruby, and Kotlin with an event-driven, non-blocking architecture. Part of the Eclipse Foundation under the Eclipse Public License 2.0. Vert.x follows a polyglot, unopinionated model allowing developers to build microservices, web applications, IoT backends, and event-driven systems with high concurrency using a small memory footprint.
examples:
- key_count: 13
  name: Vertx Config Example
  slug: vertx-config-example
- key_count: 2
  name: Vertx Deployment Descriptor Example
  slug: vertx-deployment-descriptor-example
- key_count: 3
  name: Vertx Health Check Example
  slug: vertx-health-check-example
features:
- description: Non-blocking event loop model with verticles for concurrent request handling without traditional threading overhead.
  name: Event-Driven Architecture
- description: Write Vert.x applications in Java, JavaScript, Groovy, Kotlin, Scala, and Ruby on the same JVM platform.
  name: Polyglot Support
- description: Distributed message-passing backbone enabling communication between verticles across nodes in a cluster.
  name: Event Bus
- description: High-performance HTTP/1.1 and HTTP/2 server and client with WebSocket, SSE, and gRPC support.
  name: Reactive HTTP Client and Server
- description: Automatic request and response validation against OpenAPI 3.1 specifications using vertx-openapi.
  name: OpenAPI Contract Validation
- description: Non-blocking, fully reactive SQL clients for PostgreSQL, MySQL, MSSQL, DB2, and Oracle.
  name: Reactive SQL Clients
- description: Pluggable security providers for JWT, OAuth2, JDBC, MongoDB, LDAP, and WebAuthn/FIDO2.
  name: Authentication and Authorization
- description: Composable health check procedures for Kubernetes liveness and readiness probe endpoints.
  name: Health Checks
- description: Built-in cluster support via Hazelcast, Infinispan, Zookeeper, or Apache Ignite for distributed deployments.
  name: Clustering
- description: Java 21 virtual thread support enabling synchronous-style code in Vert.x worker verticles.
  name: Virtual Threads
finops:
- name: Vert X Finops
  service_category: API
  slug: vert-x-finops
image: https://vertx.io/images/logo-wide.png
integrations:
- description: Vert.x is the reactive engine underlying Quarkus, providing the event loop and HTTP server for Quarkus applications.
  name: Quarkus
- description: Deploy Vert.x verticles on Kubernetes with health check endpoints, clustering, and horizontal pod autoscaling.
  name: Kubernetes
- description: Vert.x Kafka Client provides reactive, non-blocking Kafka producer and consumer integration.
  name: Apache Kafka
- description: Vert.x Redis Client enables async Redis operations for caching, pub/sub, and session storage.
  name: Redis
- description: Hazelcast cluster manager for distributed Vert.x deployments with shared data and event bus clustering.
  name: Hazelcast
- description: Vert.x Micrometer Metrics provides application metrics integration with Prometheus and Grafana.
  name: Micrometer
json_schemas:
- name: Vert.x Application Configuration
  property_count: 13
  slug: vertx-config
- name: Vert.x Verticle Deployment Descriptor
  property_count: 2
  slug: vertx-deployment-descriptor
- name: Vert.x Health Check Response
  property_count: 3
  slug: vertx-health-check
json_structures:
- name: Vertx Config Structure
  property_count: 13
  slug: vertx-config-structure
- name: Vertx Deployment Descriptor Structure
  property_count: 2
  slug: vertx-deployment-descriptor-structure
- name: Vertx Health Check Structure
  property_count: 3
  slug: vertx-health-check-structure
jsonld:
- class_count: 7
  name: Vert X Context
  property_count: 44
  slug: vert-x-context
layout: provider
modified: '2026-05-03'
name: Vert.x
nav: Providers
network: true
overview: 'Vert.x publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Event-Driven, Frameworks, Java, JVM, and Microservices.


  The Vert.x catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vert.x''s developer surface includes documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 12 more developer resources.'
plans:
- name: Vert X Plans Pricing
  plan_count: 3
  slug: vert-x-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Vert X Rate Limits
  slug: vert-x-rate-limits
rules:
- name: Vert.x API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vert-x-jsonschema-spectral-rules
- name: Vert.x API Rules
  rule_count: 26
  severity_counts:
    error: 7
    hint: 4
    info: 0
    warn: 15
  slug: vert-x-spectral-rules
score:
  band: developing
  composite: 46.5
  delta: -5.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 33.9
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 52.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/vert-x/refs/heads/main/screenshots/vert-x-2026-06-20T200945.png
security:
- kind: domain-security
  name: Vert X Domain Security
  slug: vert-x-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Vert X Vulnerability Disclosure
  slug: vert-x-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vert-x
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
use_cases:
- description: Build lightweight, high-concurrency microservices with Vert.x Web routing, service proxy patterns, and event bus communication.
  name: Microservices Backend
- description: Implement reactive API gateways using vertx-http-proxy with routing, authentication, and rate limiting.
  name: API Gateway
- description: Build WebSocket and SSE-based real-time applications for live dashboards, chat, and notification systems.
  name: Real-Time Applications
- description: Handle high-volume MQTT and TCP data streams from IoT devices using Vert.x non-blocking networking.
  name: IoT Data Ingestion
- description: Develop OpenAPI 3.1 contract-first REST APIs with automatic validation using vertx-openapi and vertx-web.
  name: Contract-First REST APIs
website: https://vertx.io/
---
