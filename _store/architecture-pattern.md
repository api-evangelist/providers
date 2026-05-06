---
aid: architecture-pattern
name: Architecture Pattern
description: Architecture Patterns provide reusable solutions to commonly occurring software and system design problems. They offer proven templates for organizing code, components, and interactions across distributed systems, microservices, cloud-native applications, and enterprise software.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Architecture Patterns
  - Software Architecture
  - Design Patterns
  - System Design
  - Microservices
  - Cloud Native
url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: architecture-pattern:architecture-pattern-api
    name: Architecture Pattern API
    description: API providing access to a curated reference library of architecture patterns for distributed systems, microservices, cloud-native applications, and enterprise software.
    humanURL: https://microservices.io/patterns/
    tags:
      - Architecture Patterns
      - Reference Library
      - Microservices
      - Cloud Native
    properties:
      - type: Documentation
        url: https://microservices.io/patterns/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/openapi/architecture-pattern-api.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/json-schema/architecture-pattern-api-pattern-schema.json
common:
  - type: Portal
    url: https://microservices.io/patterns/
  - type: Documentation
    url: https://microservices.io/patterns/
  - type: GitHubOrganization
    url: https://github.com/api-evangelist
  - type: Features
    data:
      - name: Pattern Catalog
        description: Comprehensive catalog of architecture patterns for microservices, distributed systems, and cloud-native applications.
      - name: Problem-Solution Framework
        description: Each pattern includes problem statement, solution approach, and known trade-offs.
      - name: Pattern Language
        description: Related patterns organized into a coherent pattern language for navigating complex architecture decisions.
      - name: Real-World Examples
        description: Patterns illustrated with real-world implementations from production systems.
      - name: Decision Support
        description: Guidance for selecting appropriate patterns based on context and constraints.
  - type: UseCases
    data:
      - name: Microservices Design
        description: Apply patterns for decomposing monolithic applications into microservices.
      - name: Distributed Systems
        description: Reference patterns for handling distributed computing challenges like consistency and availability.
      - name: Cloud Migration
        description: Select cloud-native patterns when migrating on-premises applications to cloud platforms.
      - name: Architecture Review
        description: Evaluate architecture decisions against proven patterns and identify improvement areas.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/rules/architecture-pattern-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/vocabulary/architecture-pattern-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/architecture-pattern/refs/heads/main/json-ld/architecture-pattern-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
