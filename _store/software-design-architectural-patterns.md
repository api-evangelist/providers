---
aid: software-design-architectural-patterns
name: Software Design Architectural Patterns
description: Software architectural patterns are reusable solutions and best practices for organizing software system architecture. Key patterns include MVC (Model-View-Controller), Microservices, Layered Architecture, Event-Driven Architecture, CQRS (Command Query Responsibility Segregation), Hexagonal Architecture, and Service-Oriented Architecture. These patterns are documented by Microsoft Azure Architecture Center, AWS Well-Architected Framework, and the broader software engineering community.
url: https://raw.githubusercontent.com/api-evangelist/software-design-architectural-patterns/refs/heads/main/apis.yml
tags:
  - Best Practices
  - Design Patterns
  - Software Architecture
  - System Design
  - Microservices
  - MVC
  - CQRS
  - Event-Driven
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: software-design-architectural-patterns:azure-architecture-center-api
    name: Azure Architecture Center
    description: Microsoft Azure Architecture Center provides guidance, patterns, and best practices for building cloud-native architectures. It documents architectural patterns including CQRS, Event Sourcing, Strangler Fig, Circuit Breaker, Bulkhead, and Retry patterns with implementation guidance.
    humanURL: https://learn.microsoft.com/en-us/azure/architecture/patterns/
    baseURL: https://learn.microsoft.com/
    tags:
      - Cloud Architecture
      - Architectural Patterns
      - Microsoft Azure
      - Best Practices
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/architecture/patterns/
      - type: Website
        url: https://learn.microsoft.com/en-us/azure/architecture/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/software-design-architectural-patterns/refs/heads/main/json-schema/architectural-pattern-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/software-design-architectural-patterns/refs/heads/main/json-structure/architectural-pattern-structure.json
  - aid: software-design-architectural-patterns:microservices-patterns
    name: Microservices.io Patterns Catalog
    description: Microservices.io is a pattern language for microservices architectures, documenting patterns for decomposition, data management, communication, deployment, and cross-cutting concerns. It covers API Gateway, Saga, Event Sourcing, CQRS, and Strangler Application patterns.
    humanURL: https://microservices.io/patterns/
    baseURL: https://microservices.io/
    tags:
      - Microservices
      - Architectural Patterns
      - API Gateway
      - Event Sourcing
      - CQRS
    properties:
      - type: Documentation
        url: https://microservices.io/patterns/
      - type: Website
        url: https://microservices.io/
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Architectural_pattern
  - type: Reference
    url: https://learn.microsoft.com/en-us/azure/architecture/patterns/
  - type: Reference
    url: https://microservices.io/patterns/
  - type: Reference
    url: https://refactoring.guru/design-patterns
  - type: Reference
    url: https://martinfowler.com/architecture/
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/software-design-architectural-patterns/refs/heads/main/json-ld/software-design-architectural-patterns-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/software-design-architectural-patterns/refs/heads/main/vocabulary/software-design-architectural-patterns-vocabulary.yml
---
