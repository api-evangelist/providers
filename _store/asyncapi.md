---
aid: asyncapi
name: AsyncAPI
description: AsyncAPI is a Linux Foundation project that improves the state of event-driven architectures by providing an open specification and tooling ecosystem for defining asynchronous and event-driven APIs. It enables developers to document, validate, generate code, and manage message-driven APIs across protocols including Kafka, MQTT, WebSocket, AMQP, and others. The AsyncAPI specification serves as the industry standard for describing asynchronous messaging interfaces, similar to how OpenAPI serves REST APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Event-Driven
  - Linux Foundation
  - Messaging
  - Standards
  - Specification
url: https://raw.githubusercontent.com/api-evangelist/asyncapi/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: asyncapi:asyncapi-spec
    name: AsyncAPI Specification
    description: The AsyncAPI Specification is an open standard for describing asynchronous and event-driven APIs. It provides a machine-readable format for defining messaging interfaces across protocols like Kafka, MQTT, WebSocket, and AMQP, enabling documentation generation, code generation, and validation tooling for event-driven architectures.
    humanURL: https://www.asyncapi.com/docs
    tags:
      - Event-Driven
      - Messaging
      - Specification
      - Standards
    properties:
      - type: Documentation
        url: https://www.asyncapi.com/docs
      - type: GettingStarted
        url: https://www.asyncapi.com/docs/tutorials/getting-started
      - type: AsyncAPI
        url: https://github.com/asyncapi/spec/blob/master/spec/asyncapi.md
common:
  - type: Portal
    url: https://www.asyncapi.com/
    title: AsyncAPI Website
  - type: Documentation
    url: https://www.asyncapi.com/docs
    title: Documentation
  - type: GitHubOrganization
    url: https://github.com/asyncapi
    title: AsyncAPI GitHub Organization
  - type: Blog
    url: https://www.asyncapi.com/blog
    title: Blog
  - type: Features
    data:
      - name: AsyncAPI Specification
        description: An open specification standard for describing asynchronous and event-driven APIs, supporting multiple messaging protocols including Kafka, MQTT, WebSocket, AMQP, and more.
      - name: AsyncAPI Generator
        description: Code and documentation generation tool that uses AsyncAPI definitions to produce boilerplate code, documentation, and other artifacts in multiple programming languages.
      - name: AsyncAPI CLI
        description: Command-line interface tool for working with AsyncAPI files including validation, generation, and conversion operations from the terminal.
      - name: AsyncAPI Studio
        description: Web-based editor and visualization tool for creating, editing, and previewing AsyncAPI specification documents with real-time validation.
      - name: Protocol Support
        description: Broad protocol support covering Kafka, MQTT, WebSocket, AMQP, NATS, JMS, and other messaging protocols through a unified specification format.
  - type: UseCases
    data:
      - name: Event-Driven API Documentation
        description: Development teams use AsyncAPI to create machine-readable documentation for their message-driven APIs, making it easier for consumers to understand and integrate with event streams.
      - name: Code Generation for Messaging
        description: Engineers generate boilerplate code for Kafka consumers, MQTT publishers, and other messaging clients directly from AsyncAPI specifications to accelerate development.
      - name: API Governance for Event-Driven Systems
        description: Platform teams apply AsyncAPI specifications to enforce standards and governance across microservices architectures using event-driven communication.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: AsyncAPI supports defining Kafka-based event-driven APIs with topic, message schema, and broker configuration documentation.
      - name: MQTT Brokers
        description: IoT and messaging platforms using MQTT can document their pub/sub interfaces using AsyncAPI specifications for device and service integration.
      - name: CI/CD Pipelines
        description: AsyncAPI CLI integrates into continuous integration pipelines for automated validation and linting of AsyncAPI specification files.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
