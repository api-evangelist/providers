---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 18.3
  scored_at: '2026-07-27'
api_count: 6
apis:
- description: The TypeSpec compiler processes `.tsp` TypeSpec files and emits output for configured emitters (OpenAPI, JSON Schema, Protobuf, etc.). It provides a programmatic Node.js/TypeScript API for building Ty
  name: TypeSpec Compiler
  slug: typespec-compiler
- description: The TypeSpec OpenAPI emitter converts TypeSpec definitions to OpenAPI 3.0 specifications. It supports HTTP operations, request/response bodies, security schemes, and API versioning decorators.
  name: TypeSpec OpenAPI Emitter
  slug: typespec-openapi-emitter
- description: Emits JSON Schema documents from TypeSpec model definitions, enabling data validation and type documentation workflows.
  name: TypeSpec JSON Schema Emitter
  slug: typespec-json-schema-emitter
- description: Emits Protocol Buffer `.proto` files from TypeSpec service definitions, enabling gRPC service generation from a single TypeSpec source.
  name: TypeSpec Protobuf Emitter
  slug: typespec-protobuf-emitter
- description: The TypeSpec HTTP library provides decorators and types for describing HTTP REST APIs including routes, operations, request bodies, query parameters, headers, and response codes.
  name: TypeSpec HTTP Library
  slug: typespec-http-library
- description: The TypeSpec REST library provides decorators for REST API patterns including resource operations (CRUD), collection operations, and standardized error response shapes.
  name: TypeSpec REST Library
  slug: typespec-rest-library
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typespec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://typespec.io
- group: docs
  title: ''
  type: Documentation
  url: https://typespec.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/typespec
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/@typespec/compiler
- group: other
  title: ''
  type: Playground
  url: https://typespec.io/playground
- group: company
  title: ''
  type: Blog
  url: https://typespec.io/blog
- group: operate
  title: ''
  type: Community
  url: https://github.com/microsoft/typespec/discussions
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/microsoft/typespec/releases
- group: design
  title: ''
  type: JSONLD
  url: json-ld/typespec-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/typespec-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typespec-program-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/typespec-mcp
created: '2026-03-25'
description: TypeSpec is an API description language developed by Microsoft for defining API shapes that compile to OpenAPI, JSON Schema, Protobuf, and other output formats. It provides a language and toolchain for describing REST APIs, gRPC services, and data schemas in a type-safe, composable way with built-in support for versioning, metadata, and extensibility via decorators and libraries.
finops:
- name: Typespec Finops
  service_category: API
  slug: typespec-finops
image: https://typespec.io/img/favicon.svg
json_schemas:
- name: TypeSpec Program
  property_count: 3
  slug: typespec-program
json_structures:
- name: Typespec Model Structure
  property_count: 8
  slug: typespec-model-structure
jsonld:
- class_count: 15
  name: Typespec Context
  property_count: 11
  slug: typespec-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: TypeSpec
nav: Providers
network: true
overview: 'TypeSpec publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Code Generation, OpenAPI, Protocol Buffers, and Specification Language.


  The TypeSpec catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TypeSpec''s developer surface includes documentation, engineering blog, release notes, and 10 more developer resources.'
plans:
- name: Typespec Plans Pricing
  plan_count: 3
  slug: typespec-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Typespec Rate Limits
  slug: typespec-rate-limits
rules:
- name: TypeSpec API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: typespec-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 20.8
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 45.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/typespec/refs/heads/main/screenshots/typespec-2026-06-20T195906.png
security:
- kind: domain-security
  name: Typespec Domain Security
  slug: typespec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: typespec
tags:
- API Design
- Code Generation
- OpenAPI
- Protocol Buffers
- Specification Language
website: https://typespec.io
---
