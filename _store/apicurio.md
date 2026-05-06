---
aid: apicurio
name: Apicurio
description: Apicurio is an open source API and schema tooling platform maintained by Red Hat under the Apache 2.0 license. It includes Apicurio Registry (a high-performance schema and API design registry), Apicurio Studio (a visual API designer for OpenAPI and AsyncAPI), Apicurio Data Models (a data modeling library), Apicurio Codegen (Java code generation from OpenAPI), and Apicurito (an embedded API editor).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache License
  - API Design
  - API Registry
  - Avro
  - AsyncAPI
  - Java
  - Open Source
  - OpenAPI
  - Red Hat
  - Schema Registry
url: https://raw.githubusercontent.com/api-evangelist/apicurio/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apicurio:apicurio-registry
    name: Apicurio Registry
    description: Apicurio Registry is a high-performance, runtime registry for schemas and API designs. It stores and manages OpenAPI, AsyncAPI, Avro, JSON Schema, Protobuf, and other artifact types, providing a REST API for schema management with compatibility checking and content versioning.
    humanURL: https://www.apicur.io/registry/
    tags:
      - Avro
      - AsyncAPI
      - Open Source
      - OpenAPI
      - Protobuf
      - Schema Registry
    properties:
      - type: Documentation
        url: https://www.apicur.io/registry/docs/
      - type: GitHubRepository
        url: https://github.com/Apicurio/apicurio-registry
  - aid: apicurio:apicurio-studio
    name: Apicurio Studio
    description: 'Apicurio Studio is a visual, zero-code API design tool for creating and editing OpenAPI and AsyncAPI specifications. Note: Apicurio Studio is deprecated in favor of the integrated design capabilities in Apicurio Registry.'
    humanURL: https://www.apicur.io/studio/
    tags:
      - API Design
      - AsyncAPI
      - Deprecated
      - OpenAPI
      - Visual Designer
    properties:
      - type: Documentation
        url: https://www.apicur.io/studio/docs/
      - type: GitHubRepository
        url: https://github.com/Apicurio/apicurio-studio
  - aid: apicurio:apicurio-data-models
    name: Apicurio Data Models
    description: Apicurio Data Models is a Java and TypeScript library for parsing, validating, and manipulating OpenAPI and AsyncAPI specification documents programmatically.
    humanURL: https://github.com/Apicurio/apicurio-data-models
    tags:
      - AsyncAPI
      - Data Modeling
      - Java
      - Library
      - OpenAPI
      - TypeScript
    properties:
      - type: GitHubRepository
        url: https://github.com/Apicurio/apicurio-data-models
  - aid: apicurio:apicurio-codegen
    name: Apicurio Codegen
    description: Apicurio Codegen generates Java JAX-RS server stubs and client code from OpenAPI specifications, enabling design-first API development workflows.
    humanURL: https://github.com/Apicurio/apicurio-codegen
    tags:
      - Code Generation
      - JAX-RS
      - Java
      - OpenAPI
    properties:
      - type: GitHubRepository
        url: https://github.com/Apicurio/apicurio-codegen
common:
  - type: Website
    url: https://www.apicur.io
  - type: Documentation
    url: https://www.apicur.io/registry/docs/
  - type: GitHubOrganization
    url: https://github.com/Apicurio
  - type: License
    url: https://github.com/Apicurio/apicurio-registry/blob/main/LICENSE
  - type: Features
    data:
      - name: Schema Registry
        description: High-performance registry for storing and versioning schemas including Avro, JSON Schema, Protobuf, OpenAPI, and AsyncAPI.
      - name: Schema Compatibility Checking
        description: Enforce backward, forward, or full compatibility rules when evolving schemas to prevent breaking changes.
      - name: Visual API Design
        description: Zero-code visual editor for creating OpenAPI and AsyncAPI specifications without writing raw YAML or JSON.
      - name: REST API for Schema Management
        description: Full REST API for programmatic schema registration, retrieval, and version management.
      - name: Java Code Generation
        description: Generate JAX-RS server stubs and client code from OpenAPI specifications for design-first Java development.
      - name: Multi-Format Support
        description: Support for OpenAPI, AsyncAPI, Avro, JSON Schema, Protobuf, WSDL, XSD, and GraphQL artifact types.
      - name: Apache License 2.0
        description: Open source under the Apache License 2.0, maintained by Red Hat with community contributions.
  - type: UseCases
    data:
      - name: Schema Governance
        description: Centrally manage and version schemas across microservices with compatibility enforcement to prevent breaking changes.
      - name: Design-First API Development
        description: Design OpenAPI and AsyncAPI specifications visually before writing code for design-first development.
      - name: Event-Driven Architecture
        description: Manage Avro and Protobuf schemas for Kafka and other messaging systems in event-driven architectures.
      - name: API Contract Management
        description: Store and version API specifications as the system of record for API contracts across teams.
      - name: Java Code Scaffolding
        description: Generate JAX-RS server stubs from OpenAPI specs to accelerate Java API implementation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
