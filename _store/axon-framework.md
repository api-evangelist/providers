---
aid: axon-framework
name: Axon Framework
description: Axon Framework is a Java framework for building event-driven microservices using CQRS (Command Query Responsibility Segregation) and event sourcing patterns, providing the building blocks to implement scalable and maintainable distributed systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CQRS
  - Event Sourcing
  - Event-Driven
  - Java
  - Messaging
  - Microservices
url: https://raw.githubusercontent.com/api-evangelist/axon-framework/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: axon-framework:axon-framework
    name: Axon Framework
    description: Axon Framework is a Java framework for building event-driven microservices using CQRS and event sourcing patterns, providing infrastructure components for command handling, event processing, and query handling in distributed systems.
    humanURL: https://www.axoniq.io/products/axon-framework
    tags:
      - CQRS
      - Event Sourcing
      - Event-Driven
      - Java
      - Messaging
      - Microservices
    properties:
      - type: OpenAPI
        url: openapi/axon-server-api.yml
      - type: APIReference
        url: https://docs.axoniq.io/axon-server/administration/axon-server-api
    baseURL: https://axonserver:8024
common:
  - type: Website
    url: https://www.axoniq.io/
  - type: Documentation
    url: https://docs.axoniq.io/
  - type: GettingStarted
    url: https://docs.axoniq.io/axon-framework/getting-started
  - type: GitHubRepository
    url: https://github.com/AxonFramework/AxonFramework
  - type: Blog
    url: https://www.axoniq.io/blog
  - type: Pricing
    url: https://www.axoniq.io/pricing
  - type: TermsOfService
    url: https://www.axoniq.io/terms-and-conditions
  - type: StatusPage
    url: https://status.axoniq.io/
  - type: SpectralRules
    url: rules/axon-framework-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/axon-framework-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/event-driven-workflow.yaml
  - type: Features
    data:
      - name: CQRS Pattern
        description: Separate command and query models for scalable, maintainable architecture.
      - name: Event Sourcing
        description: Store application state as a sequence of events for full audit trail and time-travel debugging.
      - name: Domain-Driven Design
        description: First-class support for DDD patterns including aggregates, sagas, and bounded contexts.
      - name: Axon Server Integration
        description: Zero-configuration event store and message router with Axon Server.
      - name: Distributed Systems Support
        description: Built-in routing for commands, events, and queries across distributed services.
      - name: Spring Boot Integration
        description: Seamless Spring Boot auto-configuration for rapid application development.
      - name: Testing Support
        description: Built-in testing fixtures for validating aggregate behavior without infrastructure.
      - name: Saga Management
        description: Manage long-running business processes with durable saga state.
  - type: UseCases
    data:
      - name: Microservices Architecture
        description: Build event-driven microservices with reliable message routing.
      - name: Audit Trail
        description: Maintain complete audit trails by storing all state changes as events.
      - name: Temporal Queries
        description: Reconstruct system state at any point in time from the event store.
      - name: Collaborative Domains
        description: Build complex collaborative domains with CQRS separation.
      - name: Workflow Automation
        description: Automate multi-step business workflows with event-driven sagas.
  - type: Integrations
    data:
      - name: Spring Boot
        description: Auto-configuration and starter dependency for Spring Boot integration.
      - name: Apache Kafka
        description: Route events through Kafka as an alternative to Axon Server.
      - name: RabbitMQ
        description: Route commands and events through AMQP with RabbitMQ extension.
      - name: JPA/Hibernate
        description: Persist saga state and event-sourced entities with JPA.
      - name: Micrometer
        description: Expose framework metrics via Micrometer for Prometheus and Grafana.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
