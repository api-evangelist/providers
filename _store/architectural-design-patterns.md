---
aid: architectural-design-patterns
name: Architectural Design Patterns
description: Architectural Design Patterns are reusable solutions to commonly occurring problems in software architecture. They provide templates for designing system structure, component interactions, and overall organization of applications across a range of industries and technical contexts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Design Patterns
  - Software Architecture
  - Best Practices
  - Software Engineering
  - System Design
  - Microservices
url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: architectural-design-patterns:architectural-design-patterns-api
    name: Architectural Design Patterns API
    description: API providing access to a catalog of architectural design patterns, their descriptions, use cases, implementation examples, and relationships between patterns.
    humanURL: https://en.wikipedia.org/wiki/Architectural_pattern
    tags:
      - Design Patterns
      - Software Architecture
      - Pattern Catalog
      - Best Practices
    properties:
      - type: Documentation
        url: https://en.wikipedia.org/wiki/Architectural_pattern
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/openapi/architectural-design-patterns-api.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/json-schema/architectural-design-patterns-api-pattern-schema.json
common:
  - type: Portal
    url: https://en.wikipedia.org/wiki/Architectural_pattern
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Architectural_pattern
  - type: GitHubOrganization
    url: https://github.com/api-evangelist
  - type: Features
    data:
      - name: Pattern Catalog
        description: Comprehensive catalog of architectural patterns including MVC, Event-Driven, Microservices, CQRS, Saga, and more.
      - name: Pattern Relationships
        description: Documented relationships and interactions between architectural patterns.
      - name: Implementation Examples
        description: Code examples and implementation guidance for each architectural pattern.
      - name: Use Case Mapping
        description: Maps architectural patterns to common software design problems and use cases.
      - name: Anti-Patterns
        description: Documentation of common anti-patterns and how to avoid them.
  - type: UseCases
    data:
      - name: System Design
        description: Reference patterns when designing new software systems or microservices architectures.
      - name: Architecture Review
        description: Evaluate existing systems against established patterns for improvement opportunities.
      - name: Developer Education
        description: Teach software engineers and architects about proven design approaches.
      - name: Documentation
        description: Communicate architectural decisions using shared vocabulary from established patterns.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/rules/architectural-design-patterns-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/vocabulary/architectural-design-patterns-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/architectural-design-patterns/refs/heads/main/json-ld/architectural-design-patterns-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
