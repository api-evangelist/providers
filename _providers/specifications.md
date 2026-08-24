---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 13
apis:
- description: The OpenAPI Specification (formerly Swagger) is the dominant industry standard for describing HTTP-based RESTful APIs. OAS describes endpoints, operations, parameters, request/response schemas, authen
  name: OpenAPI Specification (OAS)
  slug: openapi
- description: AsyncAPI is the open standard for describing event-driven and message-driven APIs across protocols such as Kafka, AMQP, MQTT, WebSocket, NATS, and SNS/SQS. AsyncAPI 3.0 (December 2023) decoupled opera
  name: AsyncAPI Specification
  slug: asyncapi
- description: JSON Schema is a declarative language for annotating and validating JSON documents. It is the foundational schema language for most modern API specifications (OpenAPI 3.1, AsyncAPI 3, and others embed
  name: JSON Schema
  slug: json-schema
- description: JSON Structure is an emerging open specification that extends and complements JSON Schema with a clearer, more code-generation-friendly type system designed for data contracts and modeling. It introdu
  name: JSON Structure
  slug: json-structure
- description: GraphQL is a query language and runtime for APIs, defined by the GraphQL Specification. The GraphQL Schema Definition Language (SDL) is the declarative format used to define types, queries, mutations,
  name: GraphQL SDL
  slug: graphql
- description: gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers (Protobuf) as its IDL and wire format. Service definitions are written in .proto files. gRPC is a CNCF graduated project; Pro
  name: gRPC and Protocol Buffers
  slug: grpc-protobuf
- description: Smithy is an open-source IDL and code-generation framework for defining services and SDKs, created and maintained by AWS. It is protocol-agnostic (HTTP REST, AWS JSON, MQTT, RPC), supports traits-base
  name: Smithy
  slug: smithy
- description: TypeSpec (formerly Cadl) is a language for describing API shapes developed by Microsoft. TypeSpec definitions emit OpenAPI 3.x, JSON Schema, Protobuf, and other artifacts, and serve as the upstream so
  name: TypeSpec
  slug: typespec
- description: RAML is a YAML-based modelling language for RESTful APIs, originally created by Mulesoft. RAML 1.0 (2016) is the current stable specification. RAML governance has effectively converged with Mulesoft /
  name: RAML (RESTful API Modeling Language)
  slug: raml
- description: 'API Blueprint is a Markdown-based specification language for describing web APIs, originally created by Apiary (acquired by Oracle). The spec is MIT licensed but development effectively stalled after '
  name: API Blueprint
  slug: api-blueprint
- description: The Web Services Description Language (WSDL) is the historical XML-based interface definition language for SOAP web services. WSDL 1.1 (2001) is the most widely deployed version; WSDL 2.0 is a W3C Rec
  name: WSDL / SOAP
  slug: wsdl-soap
- description: JSON-RPC 2.0 is a stateless, light-weight remote procedure call (RPC) protocol encoded in JSON. It is widely used in blockchain/Web3 APIs (Ethereum, Bitcoin), IDE language servers (LSP), and developer
  name: JSON-RPC 2.0
  slug: json-rpc
- description: The Tinybird API specification is a vendor-defined, declarative format for describing analytics endpoints (pipes), data sources, and parameters backed by ClickHouse. It is documented here as a represe
  name: Tinybird API Spec
  slug: tinybird
artifact_total: 49
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/specifications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/api-evangelist/specifications
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-evangelist/specifications
- group: docs
  title: Specification Record JSON Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/specifications/refs/heads/main/json-schema/specification-record-schema.json
- group: design
  title: Specification Record JSON Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/specifications/refs/heads/main/json-structure/specification-record-structure.json
- group: design
  title: API Specifications JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/specifications/refs/heads/main/json-ld/specifications-context.jsonld
- group: design
  title: API Specifications Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/specifications/refs/heads/main/vocabulary/specifications-vocabulary.yml
- group: build
  title: OpenAPI Initiative
  type: GitHubOrganization
  url: https://github.com/OAI
- group: build
  title: AsyncAPI Initiative
  type: GitHubOrganization
  url: https://github.com/asyncapi
- group: build
  title: JSON Schema Organization
  type: GitHubOrganization
  url: https://github.com/json-schema-org
- group: build
  title: JSON Structure Organization
  type: GitHubOrganization
  url: https://github.com/json-structure
- group: build
  title: GraphQL Foundation
  type: GitHubOrganization
  url: https://github.com/graphql
- group: build
  title: gRPC (CNCF)
  type: GitHubOrganization
  url: https://github.com/grpc
- group: build
  title: Protocol Buffers
  type: GitHubOrganization
  url: https://github.com/protocolbuffers
- group: build
  title: Smithy-Lang (AWS)
  type: GitHubOrganization
  url: https://github.com/smithy-lang
- group: build
  title: Microsoft (TypeSpec)
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: build
  title: RAML Workgroup
  type: GitHubOrganization
  url: https://github.com/raml-org
created: '2026-05-22'
description: Meta-index of the specification languages used to describe APIs, events, schemas, and service interfaces across the modern API landscape. This repo is the META layer above the topical repos that profile each individual specification — it catalogs every major HTTP, event-driven, schema, and service interface specification along with its current version, governing body, license, and tooling ecosystem.
examples:
- key_count: 17
  name: Api Blueprint Example
  slug: api-blueprint-example
- key_count: 19
  name: Asyncapi Example
  slug: asyncapi-example
- key_count: 17
  name: Graphql Example
  slug: graphql-example
- key_count: 17
  name: Grpc Protobuf Example
  slug: grpc-protobuf-example
- key_count: 17
  name: Json Rpc Example
  slug: json-rpc-example
- key_count: 19
  name: Json Schema Example
  slug: json-schema-example
- key_count: 18
  name: Json Structure Example
  slug: json-structure-example
- key_count: 19
  name: Openapi Example
  slug: openapi-example
- key_count: 17
  name: Raml Example
  slug: raml-example
- key_count: 17
  name: Smithy Example
  slug: smithy-example
- key_count: 17
  name: Tinybird Example
  slug: tinybird-example
- key_count: 17
  name: Typespec Example
  slug: typespec-example
- key_count: 17
  name: Wsdl Soap Example
  slug: wsdl-soap-example
features:
- description: Languages for describing synchronous HTTP APIs — paths, methods, parameters, request bodies, responses, and security. Includes OpenAPI, RAML, API Blueprint, and historically WSDL.
  name: HTTP Request/Response Specifications
- description: Languages for describing message-driven and event-driven APIs across brokers and protocols. Primarily AsyncAPI 3.x, plus protocol-specific schemas (Avro, Protobuf) used in concert.
  name: Event-Driven Specifications
- description: Languages that define language-agnostic service contracts intended for code generation across clients and servers. Includes gRPC/Protobuf, Smithy, TypeSpec, and historically WSDL.
  name: Service Interface Definition Languages (IDLs)
- description: Languages for describing data shapes independent of a specific transport. Includes JSON Schema (the de facto standard, embedded in OpenAPI and AsyncAPI) and the emerging JSON Structure.
  name: Schema Languages
- description: Specifications for remote procedure call protocols. Includes JSON-RPC 2.0 (used heavily in blockchain and LSP) and gRPC for high-performance RPC.
  name: RPC Protocol Specifications
- description: Vendor-specific specification formats that govern modern API products (e.g. Tinybird pipes). These often emit OpenAPI as a derived artifact while keeping a higher-level domain model as the source of truth.
  name: Vendor-Defined Specifications
graphqls:
- description: GraphQL is a query language and runtime for APIs, defined by the GraphQL Specification. The GraphQL Schema Definition Language (SDL) is the declarative format used to define types, queries, mutations,
  name: API Specifications GraphQL API
  slug: specifications-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/specifications.png
integrations:
- description: Open-source linting engine (Stoplight) for OpenAPI, AsyncAPI, and JSON Schema. The de facto governance engine across HTTP and event-driven specs.
  name: Spectral
- description: Open-source CLI for linting, bundling, and rendering OpenAPI specs; enforces style guides and integrates with CI.
  name: Redocly CLI
- description: Template-driven code and documentation generator for AsyncAPI specs across languages and brokers.
  name: AsyncAPI Generator
- description: The canonical Protobuf compiler and Buf's modern toolchain for linting, breaking-change detection, and code generation against .proto files.
  name: Protoc / Buf
- description: AWS-maintained CLI for compiling Smithy models and generating OpenAPI, JSON Schema, and SDK artifacts.
  name: Smithy CLI
- description: Microsoft-maintained compiler that emits OpenAPI 3, JSON Schema, Protobuf, and other artifacts from TypeSpec sources.
  name: TypeSpec Compiler
json_schemas:
- name: SpecificationRecord
  property_count: 19
  slug: specification-record
json_structures:
- name: Specification Record Structure
  property_count: 19
  slug: specification-record-structure
jsonld:
- class_count: 4
  name: Specifications Context
  property_count: 24
  slug: specifications-context
layout: provider
modified: '2026-05-22'
name: API Specifications
nav: Providers
network: true
overview: 'API Specifications publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Specification, Specification Languages, API Design, Contracts, and Schemas.


  The API Specifications catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 1
rules:
- effective_rule_count: 5
  extends: []
  name: API Specifications API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: specifications-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 19.7
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 2.6
  previous_composite: 15.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/specifications/refs/heads/main/screenshots/specifications-2026-06-20T194256.png
security:
- kind: domain-security
  name: Specifications Domain Security
  slug: specifications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: specifications
tags:
- API Specification
- Specification Languages
- API Design
- Contracts
- Schemas
- Interface Definitions
- Standards
use_cases:
- description: Maintaining an enterprise inventory of specifications used across internal and partner APIs, mapped to their governing bodies and tooling.
  name: Specification Discovery and Cataloging
- description: Choosing or layering specifications (TypeSpec or Smithy as a high-level model emitting OpenAPI, JSON Schema, and Protobuf) to generate SDKs across protocols.
  name: Multi-Format Code Generation
- description: Using AsyncAPI alongside Avro/Protobuf to define event schemas, channels, and operations for streaming and message-driven systems.
  name: Event-Driven Architecture Contracts
- description: Applying Spectral or other linting frameworks against OpenAPI, AsyncAPI, and JSON Schema artifacts as part of an API governance program.
  name: Governance and Linting Across Specs
- description: Migrating legacy WSDL/SOAP interfaces to OpenAPI-described REST or gRPC service contracts as part of modernization initiatives.
  name: Legacy SOAP/WSDL Modernization
---
