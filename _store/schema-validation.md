---
aid: schema-validation
name: Schema Validation
description: Schema validation is the practice of verifying that data structures conform to a defined schema, contract, or specification. In API development, schema validation ensures API requests and responses match declared OpenAPI, JSON Schema, AsyncAPI, or GraphQL specifications, enabling contract testing, governance, and runtime integrity. Key tools include AJV, Hyperjump JSON Schema, Spectral, and Schemathesis, each addressing different validation contexts from CLI pipelines to runtime API testing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Governance
  - Contract Testing
  - JSON Schema
  - OpenAPI
  - Schema Validation
url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/apis.yml
created: '2025'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: schema-validation:ajv
    name: AJV JSON Schema Validator
    description: AJV (Another JSON Validator) is the fastest JSON Schema validator for JavaScript and Node.js. It supports JSON Schema drafts 04/06/07/2019-09/ 2020-12 and JSON Type Definition (RFC 8927). AJV compiles schemas to highly optimized JavaScript functions for maximum runtime performance.
    humanURL: https://ajv.js.org/
    tags:
      - JSON Schema
      - JavaScript
      - Schema Validation
      - Node.js
    properties:
      - type: Documentation
        url: https://ajv.js.org/
      - type: GitHub Repository
        url: https://github.com/ajv-validator/ajv
      - type: npm Package
        url: https://www.npmjs.com/package/ajv
      - type: API Reference
        url: https://ajv.js.org/api.html
  - aid: schema-validation:hyperjump-json-schema
    name: Hyperjump JSON Schema
    description: Hyperjump is a JSON Schema validation, annotation, and bundling library for JavaScript. It supports JSON Schema drafts 04, 06, 07, 2019-09, 2020-12, OpenAPI 3.0, and OpenAPI 3.1 vocabularies. It also provides an OAS Schema Validator for OpenAPI-specific validation.
    humanURL: https://json-schema.hyperjump.io/
    tags:
      - JSON Schema
      - JavaScript
      - OpenAPI
      - Schema Validation
    properties:
      - type: Documentation
        url: https://json-schema.hyperjump.io/
      - type: GitHub Repository
        url: https://github.com/hyperjump-io/json-schema
      - type: npm Package
        url: https://www.npmjs.com/package/@hyperjump/json-schema
  - aid: schema-validation:spectral
    name: Spectral
    description: Spectral is an open-source JSON/YAML linter and schema validator from Stoplight. It provides customizable rulesets for validating OpenAPI, AsyncAPI, JSON Schema, and any custom schema format, enabling API governance at the CLI, IDE, and CI/CD pipeline level.
    humanURL: https://stoplight.io/open-source/spectral
    tags:
      - API Governance
      - API Linting
      - JSON Schema
      - OpenAPI
      - Schema Validation
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/spectral/
      - type: GitHub Repository
        url: https://github.com/stoplightio/spectral
      - type: npm Package
        url: https://www.npmjs.com/package/@stoplight/spectral-core
  - aid: schema-validation:openapi-schema-validator
    name: OpenAPI Schema Validator
    description: A Node.js library for validating OpenAPI schemas against the OpenAPI specification for versions 2.0 (Swagger), 3.0.x, and 3.1.x. Available as both a library and CLI tool.
    humanURL: https://github.com/seriousme/openapi-schema-validator
    tags:
      - OpenAPI
      - Schema Validation
      - Node.js
    properties:
      - type: GitHub Repository
        url: https://github.com/seriousme/openapi-schema-validator
      - type: npm Package
        url: https://www.npmjs.com/package/@seriousme/openapi-schema-validator
  - aid: schema-validation:blaze-validator
    name: Blaze JSON Schema Validator
    description: An ultra high-performance JSON Schema validator for C++ with support for JSON Schema Draft 4, Draft 6, Draft 7, 2019-09, and 2020-12. Suitable for high-throughput server-side validation scenarios.
    humanURL: https://github.com/sourcemeta/blaze
    tags:
      - C++
      - JSON Schema
      - Performance
      - Schema Validation
    properties:
      - type: GitHub Repository
        url: https://github.com/sourcemeta/blaze
  - aid: schema-validation:alterschema
    name: AlterSchema
    description: A tooling library for upgrading JSON Schema documents from previous versions (Draft 4, 6, 7, 2019-09) to the latest draft 2020-12, enabling schema modernization pipelines.
    humanURL: https://github.com/sourcemeta/alterschema
    tags:
      - JSON Schema
      - Schema Migration
      - Schema Validation
    properties:
      - type: GitHub Repository
        url: https://github.com/sourcemeta/alterschema
common:
  - type: Website
    url: https://json-schema.org/
  - type: Documentation
    url: https://json-schema.org/learn
  - type: Blog
    url: https://apievangelist.com/archive/
  - type: GitHub Organization
    url: https://github.com/json-schema-org
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/json-schema/schema-validation-config-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/json-structure/schema-validation-config-structure.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/json-ld/schema-validation-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/vocabulary/schema-validation-vocabulary.yml
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/schema-validation/refs/heads/main/examples/schema-validation-ajv-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
