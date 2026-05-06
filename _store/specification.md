---
aid: specification
url: https://raw.githubusercontent.com/api-evangelist/specification/refs/heads/main/apis.yml
name: Specification
description: A subject-matter collection covering API specifications, specification formats, specification-driven development, and the broader specification landscape. This includes OpenAPI, AsyncAPI, JSON Schema, GraphQL SDL, Arazzo, gRPC Protocol Buffers, RAML, API Blueprint, and other machine-readable API description formats. Specification-first development treats the API contract as the source of truth for code generation, documentation, testing, and governance.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - API Design
  - API Governance
  - AsyncAPI
  - Contract Testing
  - JSON Schema
  - OpenAPI
  - Specifications
  - Standards
created: '2025-01-01'
modified: '2026-05-02'
position: Consumer
segments:
  - Specifications
  - API Design
apis:
  - aid: specification:openapi
    name: OpenAPI Specification
    tags:
      - API Design
      - Code Generation
      - Documentation
      - HTTP
      - OpenAPI
      - REST
      - Standards
    humanURL: https://www.openapis.org/
    properties:
      - url: https://www.openapis.org/
        type: Website
      - url: https://spec.openapis.org/oas/latest.html
        type: Specification
      - url: https://github.com/OAI/OpenAPI-Specification
        type: GitHubRepo
      - url: https://openapi.tools/
        type: Tools
    description: The OpenAPI Specification (OAS) is the industry-standard format for describing REST/HTTP APIs. Maintained by the OpenAPI Initiative under the Linux Foundation, it enables code generation, interactive documentation, mock servers, contract testing, and governance tooling from a single machine-readable API contract. Current version is OpenAPI 3.1, which achieves full JSON Schema alignment.
  - aid: specification:asyncapi
    name: AsyncAPI Specification
    tags:
      - AsyncAPI
      - Event-Driven
      - Kafka
      - Messaging
      - Standards
      - WebSocket
    humanURL: https://www.asyncapi.com/
    properties:
      - url: https://www.asyncapi.com/
        type: Website
      - url: https://www.asyncapi.com/docs/reference/specification/latest
        type: Specification
      - url: https://github.com/asyncapi/spec
        type: GitHubRepo
    description: AsyncAPI is the standard for defining event-driven and message-based APIs. Modeled on the OpenAPI Specification but extended for asynchronous protocols including Kafka, AMQP, MQTT, WebSocket, and SNS/SQS. Used for generating documentation, code, and governance tooling for async API surfaces.
  - aid: specification:json-schema
    name: JSON Schema
    tags:
      - Data Validation
      - JSON
      - JSON Schema
      - Standards
    humanURL: https://json-schema.org/
    properties:
      - url: https://json-schema.org/
        type: Website
      - url: https://json-schema.org/specification
        type: Specification
      - url: https://github.com/json-schema-org/json-schema-spec
        type: GitHubRepo
    description: JSON Schema is a vocabulary for annotating and validating JSON documents. It is the foundation of OpenAPI 3.1 schema definitions and used across the API ecosystem for request/response validation, code generation, and data contract enforcement.
  - aid: specification:arazzo
    name: Arazzo Specification
    tags:
      - API Workflows
      - Arazzo
      - Contract Testing
      - OpenAPI
      - Sequences
      - Standards
    humanURL: https://spec.openapis.org/arazzo/latest.html
    properties:
      - url: https://spec.openapis.org/arazzo/latest.html
        type: Specification
      - url: https://github.com/OAI/Arazzo-Specification
        type: GitHubRepo
    description: The Arazzo Specification (formerly OpenAPI Workflows) describes multi-step API sequences, enabling documentation and automated testing of complex API interactions that span multiple operations. Used for contract testing and API workflow documentation by tools like Speakeasy.
common:
  - url: https://www.openapis.org/
    name: OpenAPI Initiative
    type: Organization
    description: 'null'
  - url: https://www.asyncapi.com/
    name: AsyncAPI Initiative
    type: Organization
    description: 'null'
  - url: https://json-schema.org/
    name: JSON Schema Organization
    type: Organization
    description: 'null'
  - url: https://openapi.tools/
    name: OpenAPI Tools Directory
    type: Tools
    description: 'null'
  - url: https://spec.openapis.org/oas/latest.html
    name: OpenAPI Specification Latest
    type: Specification
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: API Description
      - name: Request Validation
      - name: Response Validation
      - name: Code Generation
      - name: Mock Servers
      - name: Interactive Documentation
      - name: Contract Testing
      - name: API Governance
      - name: Schema Reuse
      - name: Security Definitions
      - name: Path Templates
      - name: Content Negotiation
      - name: Webhook Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
