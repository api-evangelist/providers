---
aid: typespec
name: TypeSpec
description: TypeSpec is an API description language developed by Microsoft for defining API shapes that compile to OpenAPI, JSON Schema, Protobuf, and other output formats. It provides a language and toolchain for describing REST APIs, gRPC services, and data schemas in a type-safe, composable way with built-in support for versioning, metadata, and extensibility via decorators and libraries.
type: Index
image: https://typespec.io/img/favicon.svg
tags:
  - API Design
  - Code Generation
  - OpenAPI
  - Protocol Buffers
  - Specification Language
url: https://raw.githubusercontent.com/api-evangelist/typespec/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: typespec:typespec-compiler
    name: TypeSpec Compiler
    description: The TypeSpec compiler processes `.tsp` TypeSpec files and emits output for configured emitters (OpenAPI, JSON Schema, Protobuf, etc.). It provides a programmatic Node.js/TypeScript API for building TypeSpec tooling, custom emitters, and compilers.
    humanURL: https://typespec.io/docs
    tags:
      - API Design
      - Code Generation
      - Compiler
      - Specification Language
    properties:
      - type: Documentation
        url: https://typespec.io/docs
      - type: GitHub Repository
        url: https://github.com/microsoft/typespec
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/compiler
      - type: Getting Started
        url: https://typespec.io/docs/getting-started/getting-started-rest
      - type: Language Reference
        url: https://typespec.io/docs/language-basics/overview
  - aid: typespec:typespec-openapi-emitter
    name: TypeSpec OpenAPI Emitter
    description: The TypeSpec OpenAPI emitter converts TypeSpec definitions to OpenAPI 3.0 specifications. It supports HTTP operations, request/response bodies, security schemes, and API versioning decorators.
    humanURL: https://typespec.io/docs/emitters/openapi3/reference
    tags:
      - Code Generation
      - OpenAPI
      - REST API
    properties:
      - type: Documentation
        url: https://typespec.io/docs/emitters/openapi3/reference
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/openapi3
      - type: GitHub Repository
        url: https://github.com/microsoft/typespec/tree/main/packages/openapi3
  - aid: typespec:typespec-json-schema-emitter
    name: TypeSpec JSON Schema Emitter
    description: Emits JSON Schema documents from TypeSpec model definitions, enabling data validation and type documentation workflows.
    humanURL: https://typespec.io/docs/emitters/json-schema/reference
    tags:
      - Code Generation
      - JSON Schema
      - Validation
    properties:
      - type: Documentation
        url: https://typespec.io/docs/emitters/json-schema/reference
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/json-schema
  - aid: typespec:typespec-protobuf-emitter
    name: TypeSpec Protobuf Emitter
    description: Emits Protocol Buffer `.proto` files from TypeSpec service definitions, enabling gRPC service generation from a single TypeSpec source.
    humanURL: https://typespec.io/docs/emitters/protobuf/reference
    tags:
      - Code Generation
      - gRPC
      - Protocol Buffers
    properties:
      - type: Documentation
        url: https://typespec.io/docs/emitters/protobuf/reference
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/protobuf
  - aid: typespec:typespec-http-library
    name: TypeSpec HTTP Library
    description: The TypeSpec HTTP library provides decorators and types for describing HTTP REST APIs including routes, operations, request bodies, query parameters, headers, and response codes.
    humanURL: https://typespec.io/docs/libraries/http/reference
    tags:
      - Decorators
      - HTTP
      - REST API
    properties:
      - type: Documentation
        url: https://typespec.io/docs/libraries/http/reference
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/http
  - aid: typespec:typespec-rest-library
    name: TypeSpec REST Library
    description: The TypeSpec REST library provides decorators for REST API patterns including resource operations (CRUD), collection operations, and standardized error response shapes.
    humanURL: https://typespec.io/docs/libraries/rest/reference
    tags:
      - Decorators
      - Resource Pattern
      - REST API
    properties:
      - type: Documentation
        url: https://typespec.io/docs/libraries/rest/reference
      - type: npm Package
        url: https://www.npmjs.com/package/@typespec/rest
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://typespec.io
  - type: Documentation
    url: https://typespec.io/docs
  - type: GitHub Organization
    url: https://github.com/microsoft/typespec
  - type: npm
    url: https://www.npmjs.com/package/@typespec/compiler
  - type: Playground
    url: https://typespec.io/playground
  - type: Blog
    url: https://typespec.io/blog
  - type: Community
    url: https://github.com/microsoft/typespec/discussions
  - type: Release Notes
    url: https://github.com/microsoft/typespec/releases
  - type: JSON-LD
    url: json-ld/typespec-context.jsonld
  - type: Vocabulary
    url: vocabulary/typespec-vocabulary.yml
  - type: JSONSchema
    url: json-schema/typespec-program-schema.json
---
