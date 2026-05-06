---
aid: technical-specifications
name: Technical Specifications
description: Technical specifications are detailed technical requirements, standards, and parameters that define the characteristics and performance criteria of a product, system, or service. In the API and software domain, technical specifications include formal API description formats (OpenAPI, AsyncAPI, JSON Schema), data exchange formats (JSON, XML, CSV, Protobuf), communication protocols (HTTP, gRPC, WebSocket, GraphQL), and encoding standards. Organizations adopt technical specifications to address interoperability, consistency, and governance challenges in their technology environments. Key specifications in the API economy include the OpenAPI Specification, AsyncAPI Specification, JSON Schema, RAML, API Blueprint, and GraphQL SDL.
url: https://raw.githubusercontent.com/api-evangelist/technical-specifications/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Documentation
  - Engineering
  - Requirements
  - Specifications
  - Standards
apis:
  - aid: technical-specifications:openapi-specification
    name: OpenAPI Specification
    description: The OpenAPI Specification (OAS) is a vendor-neutral, language-agnostic interface to HTTP APIs that allows both humans and computers to discover and understand the capabilities of a service. An OpenAPI document describes or is used to generate clients, servers, documentation, test cases, and tooling. Maintained by the OpenAPI Initiative under the Linux Foundation.
    humanURL: https://www.openapis.org/
    baseURL: https://spec.openapis.org/oas/v3.1.0
    tags:
      - API Description
      - Documentation
      - HTTP
      - OpenAPI
      - REST
    properties:
      - type: Documentation
        url: https://spec.openapis.org/oas/latest.html
      - type: Website
        url: https://www.openapis.org/
      - type: GitHub
        url: https://github.com/OAI/OpenAPI-Specification
  - aid: technical-specifications:asyncapi-specification
    name: AsyncAPI Specification
    description: AsyncAPI is an open source initiative that seeks to improve the current state of event-driven architectures (EDA). The AsyncAPI Specification is used to describe and document message-driven APIs in a machine-readable format. It supports protocols such as AMQP, MQTT, Kafka, WebSocket, and HTTP.
    humanURL: https://www.asyncapi.com/
    baseURL: https://spec.asyncapi.com/versions/3.0.0
    tags:
      - AsyncAPI
      - Event-Driven
      - Messaging
      - Streaming
    properties:
      - type: Documentation
        url: https://www.asyncapi.com/docs
      - type: Website
        url: https://www.asyncapi.com/
      - type: GitHub
        url: https://github.com/asyncapi/spec
  - aid: technical-specifications:json-schema
    name: JSON Schema
    description: JSON Schema is a vocabulary that allows you to annotate and validate JSON documents. It is used to define the structure, constraints, and semantics of JSON data, and underpins both OpenAPI and AsyncAPI for data model definitions. The current stable version is Draft 2020-12.
    humanURL: https://json-schema.org/
    baseURL: https://json-schema.org/draft/2020-12
    tags:
      - Data Validation
      - JSON
      - Schema
      - Validation
    properties:
      - type: Documentation
        url: https://json-schema.org/learn/getting-started-step-by-step
      - type: Website
        url: https://json-schema.org/
      - type: GitHub
        url: https://github.com/json-schema-org/json-schema-spec
  - aid: technical-specifications:graphql
    name: GraphQL Specification
    description: GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need, and makes it easier to evolve APIs over time. Maintained by the GraphQL Foundation under the Linux Foundation.
    humanURL: https://graphql.org/
    baseURL: https://spec.graphql.org/October2021
    tags:
      - GraphQL
      - Query Language
      - Schema
    properties:
      - type: Documentation
        url: https://graphql.org/learn/
      - type: Website
        url: https://graphql.org/
      - type: GitHub
        url: https://github.com/graphql/graphql-spec
  - aid: technical-specifications:grpc
    name: gRPC
    description: gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It uses Protocol Buffers as the interface description language and supports bidirectional streaming and flow control. Originally developed by Google, now a CNCF project.
    humanURL: https://grpc.io/
    baseURL: https://grpc.io/docs/
    tags:
      - gRPC
      - Protocol Buffers
      - RPC
      - Streaming
    properties:
      - type: Documentation
        url: https://grpc.io/docs/
      - type: Website
        url: https://grpc.io/
      - type: GitHub
        url: https://github.com/grpc/grpc
  - aid: technical-specifications:raml
    name: RAML Specification
    description: RAML (RESTful API Modeling Language) is a YAML-based language for describing RESTful APIs. RAML enables you to manage the whole API lifecycle from design to sharing. It provides a human-readable format that describes RESTful API models and supports reuse via includes and libraries.
    humanURL: https://raml.org/
    baseURL: https://raml.org/spec
    tags:
      - API Description
      - Modeling
      - RAML
      - REST
    properties:
      - type: Documentation
        url: https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md
      - type: Website
        url: https://raml.org/
      - type: GitHub
        url: https://github.com/raml-org/raml-spec
common:
  - type: Website
    url: https://en.wikipedia.org/wiki/Specification_(technical_standard)
  - type: About
    url: https://en.wikipedia.org/wiki/Technical_standard
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/technical-specifications/refs/heads/main/vocabulary/technical-specifications-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/technical-specifications/refs/heads/main/json-ld/technical-specifications-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
