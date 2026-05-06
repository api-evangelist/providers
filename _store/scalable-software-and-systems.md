---
aid: scalable-software-and-systems
name: Scalable Software and Systems
description: A topic collection exploring the APIs, design patterns, frameworks, and platforms that enable scalable software and systems engineering. Covers architectural patterns such as CQRS, event sourcing, saga, MACH architecture, API-first design, and modular monoliths, as well as the tooling ecosystems that support building maintainable, high-scale software. Relevant to software architects, platform teams, and senior engineers building enterprise-grade distributed systems.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API First
  - Architecture Patterns
  - CQRS
  - Distributed Systems
  - Enterprise
  - Event Driven
  - Microservices
  - Scalable Architecture
  - Software Engineering
  - Systems Design
type: Index
created: '2025-01-20'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalable-software-and-systems:backstage
    name: Backstage Software Catalog API
    description: Backstage by Spotify provides a software catalog API and developer portal platform for managing all software components, services, websites, and infrastructure at scale. Its catalog API enables registering, tracking, and discovering software components across an organization.
    tags:
      - Developer Portal
      - Internal Developer Platform
      - Software Catalog
      - Systems Design
    humanURL: https://backstage.io/docs/features/software-catalog/software-catalog-api
    properties:
      - type: Documentation
        url: https://backstage.io/docs/features/software-catalog/software-catalog-api
      - type: GitHub
        url: https://github.com/backstage/backstage
  - aid: scalable-software-and-systems:cloudevents
    name: CloudEvents API
    description: CloudEvents is a CNCF specification for describing event data in a common way. It defines a core data model and HTTP, AMQP, MQTT, and Kafka bindings enabling interoperable event-driven system design across cloud providers and middleware.
    tags:
      - CNCF
      - Event Driven
      - Events
      - Integration
      - Standards
    humanURL: https://cloudevents.io/
    properties:
      - type: Documentation
        url: https://cloudevents.io/
      - type: GitHub
        url: https://github.com/cloudevents/spec
      - type: Specification
        url: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
  - aid: scalable-software-and-systems:kafka-admin
    name: Apache Kafka Admin API
    description: Apache Kafka's Admin REST API enables creating and managing topics, partitions, consumer groups, and cluster configurations for high-throughput event streaming pipelines used in scalable, event-driven architectures.
    tags:
      - Event Driven
      - Event Streaming
      - High Throughput
      - Messaging
    humanURL: https://kafka.apache.org/documentation/
    properties:
      - type: Documentation
        url: https://kafka.apache.org/documentation/
      - type: GitHub
        url: https://github.com/apache/kafka
  - aid: scalable-software-and-systems:nats
    name: NATS Management API
    description: NATS is a lightweight, high-performance messaging system for distributed applications. Its management API provides monitoring, subject inspection, and JetStream (persistent streams) management for building scalable event-driven systems.
    tags:
      - Cloud Native
      - Event Driven
      - High Performance
      - Messaging
      - Microservices
    humanURL: https://docs.nats.io/
    properties:
      - type: Documentation
        url: https://docs.nats.io/
      - type: GitHub
        url: https://github.com/nats-io/nats-server
  - aid: scalable-software-and-systems:temporal
    name: Temporal API
    description: Temporal is a durable execution platform that provides an API for defining and running long-running, fault-tolerant workflows. Implements the saga pattern with full activity retry semantics, enabling reliable orchestration in distributed systems.
    tags:
      - Distributed Systems
      - Durable Execution
      - Saga Pattern
      - Workflow Orchestration
    humanURL: https://docs.temporal.io/
    properties:
      - type: Documentation
        url: https://docs.temporal.io/
      - type: GitHub
        url: https://github.com/temporalio/temporal
      - type: OpenAPI
        url: https://github.com/temporalio/api/blob/master/openapi/openapi.yml
  - aid: scalable-software-and-systems:dapr
    name: Dapr API
    description: Dapr (Distributed Application Runtime) provides building block APIs for service invocation, pub/sub messaging, state management, bindings, actors, and distributed tracing. Abstracts away infrastructure complexity for portable, scalable software.
    tags:
      - Distributed Systems
      - Event Driven
      - Microservices
      - Scalable Architecture
    humanURL: https://docs.dapr.io/reference/api/
    properties:
      - type: Documentation
        url: https://docs.dapr.io/reference/api/
      - type: GitHub
        url: https://github.com/dapr/dapr
  - aid: scalable-software-and-systems:opentelemetry
    name: OpenTelemetry API
    description: OpenTelemetry provides vendor-neutral APIs, SDKs, and instrumentation for generating traces, metrics, and logs. Essential for observability in scalable distributed software systems, enabling performance analysis and root cause diagnosis.
    tags:
      - Distributed Tracing
      - Logs
      - Metrics
      - Observability
      - Telemetry
    humanURL: https://opentelemetry.io/docs/
    properties:
      - type: Documentation
        url: https://opentelemetry.io/docs/
      - type: GitHub
        url: https://github.com/open-telemetry/opentelemetry-specification
  - aid: scalable-software-and-systems:argocd
    name: Argo CD API
    description: Argo CD provides a declarative GitOps continuous delivery API for Kubernetes applications. Enables teams to manage application deployments at scale using Git as the source of truth for system state.
    tags:
      - CD
      - GitOps
      - Kubernetes
      - Platform Engineering
    humanURL: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
    properties:
      - type: Documentation
        url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
      - type: GitHub
        url: https://github.com/argoproj/argo-cd
common:
  - type: Guide
    url: https://microservices.io/patterns/data/cqrs.html
    name: CQRS Pattern
  - type: Guide
    url: https://microservices.io/patterns/data/event-sourcing.html
    name: Event Sourcing Pattern
  - type: Guide
    url: https://microservices.io/patterns/data/saga.html
    name: Saga Pattern
  - type: Guide
    url: https://www.cncf.io/projects/
    name: CNCF Projects Landscape
  - type: Guide
    url: https://12factor.net/
    name: The Twelve-Factor App
  - type: JSONSchema
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/json-schema/scalable-software-and-systems-event-schema.json
    name: Domain Event JSON Schema
  - type: JSONStructure
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/json-structure/scalable-software-and-systems-event-structure.json
    name: Domain Event JSON Structure
  - type: JSONLDContext
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/json-ld/scalable-software-and-systems-context.jsonld
    name: Scalable Software and Systems JSON-LD Context
  - type: Vocabulary
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/vocabulary/scalable-software-and-systems-vocabulary.yml
    name: Scalable Software and Systems Vocabulary
  - type: Examples
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/examples/scalable-software-and-systems-order-placed-event-example.json
    name: Order Placed Event Example
  - type: Examples
    url: https://github.com/api-evangelist/scalable-software-and-systems/blob/main/examples/scalable-software-and-systems-temporal-workflow-example.json
    name: Temporal Order Saga Workflow Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
