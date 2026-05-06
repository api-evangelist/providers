---
aid: code-first
url: https://raw.githubusercontent.com/api-evangelist/code-first/refs/heads/main/apis.yml
name: Code First
tags:
  - API Design
  - Code Generation
  - Code-First
  - Decorators
  - Development Methodology
  - Software Architecture
  - Type Safety
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: topic
created: '2025-01-01'
modified: '2026-04-26'
position: Consumer
description: Code-first is an API design and software development approach where the application's source code is the primary source of truth and the API contract (OpenAPI document, GraphQL schema, gRPC proto, type definitions) is generated from that code via decorators, annotations, type inference, or runtime introspection. It contrasts with the design-first (or contract-first) approach in which a hand-authored OpenAPI/GraphQL/Proto contract is written first and code is scaffolded from it. Code-first approaches are widely used in TypeScript, Python, Java, Go, and C# ecosystems where strong type systems make schema generation reliable.
x-related-topics:
  - design-first
  - api-design
  - openapi
  - graphql
  - trpc
  - type-safety
  - schema-generation
x-key-frameworks:
  - name: FastAPI
    language: Python
    contract: OpenAPI 3.x generated from Pydantic models and type hints
    url: https://fastapi.tiangolo.com/
  - name: NestJS
    language: TypeScript
    contract: OpenAPI generated via @nestjs/swagger decorators
    url: https://docs.nestjs.com/openapi/introduction
  - name: tRPC
    language: TypeScript
    contract: End-to-end TypeScript types, no separate IDL
    url: https://trpc.io/
  - name: Hono RPC
    language: TypeScript
    contract: TypeScript inference, optional OpenAPI via @hono/zod-openapi
    url: https://hono.dev/docs/guides/rpc
  - name: Spring Boot + springdoc-openapi
    language: Java/Kotlin
    contract: OpenAPI generated from JAX-RS/Spring annotations
    url: https://springdoc.org/
  - name: Quarkus
    language: Java/Kotlin
    contract: MicroProfile OpenAPI from JAX-RS annotations
    url: https://quarkus.io/guides/openapi-swaggerui
  - name: Micronaut
    language: Java/Kotlin
    contract: OpenAPI from compile-time AST inspection
    url: https://micronaut-projects.github.io/micronaut-openapi/
  - name: ASP.NET Core (Minimal APIs / Controllers)
    language: C#
    contract: OpenAPI via Microsoft.AspNetCore.OpenApi or Swashbuckle
    url: https://learn.microsoft.com/aspnet/core/fundamentals/openapi
  - name: Go - chi-openapi / go-swagger / huma
    language: Go
    contract: OpenAPI from struct tags and reflection
    url: https://huma.rocks/
  - name: Encore
    language: Go/TypeScript
    contract: API contract inferred from typed handlers
    url: https://encore.dev/
  - name: Express + zod-openapi
    language: TypeScript
    contract: OpenAPI generated from zod schemas
    url: https://github.com/asteasolutions/zod-to-openapi
  - name: Ruby on Rails + rswag
    language: Ruby
    contract: OpenAPI from RSpec request specs
    url: https://github.com/rswag/rswag
  - name: Laravel - Scribe
    language: PHP
    contract: OpenAPI from controller introspection and PHPDoc
    url: https://scribe.knuckles.wtf/
  - name: GraphQL Nexus / Pothos
    language: TypeScript
    contract: GraphQL SDL generated from typed builders
    url: https://pothos-graphql.dev/
  - name: gRPC + tonic / grpc-gateway
    language: Rust/Go
    contract: Proto + code; debate over which is "first"
    url: https://github.com/grpc-ecosystem/grpc-gateway
x-tradeoffs:
  pros:
    - Single source of truth eliminates contract/code drift
    - Faster iteration - no separate OpenAPI editing step
    - Strong type safety end-to-end (especially in TS/Python)
    - Familiar to backend engineers; lower onboarding cost
    - Tooling-friendly - IDEs surface routes and types natively
  cons:
    - Contract changes are implicit; harder to review independently
    - Risk of leaking implementation details into the public contract
    - Cross-team or cross-organization governance is harder
    - Generated specs sometimes lack examples, descriptions, security
    - Frontend or partner teams cannot start integration before code is written
x-when-to-use:
  - Internal services where backend team owns producer and consumer
  - Rapid product development with tight feedback loops
  - TypeScript monorepos using tRPC or shared types
  - Python / FastAPI services where Pydantic already models domain
x-when-to-avoid:
  - Public APIs with diverse external consumers
  - Government, banking, or other contract-bound API programs
  - Multi-team programs where contract review precedes implementation
  - SDK generation pipelines that need stable, reviewed schemas
apis: []
common:
  - type: Reference
    url: https://en.wikipedia.org/wiki/Code_first
  - type: Article
    url: https://blog.postman.com/api-first-vs-code-first/
  - type: Article
    url: https://blog.stoplight.io/api-design-first-vs-code-first
  - type: Article
    url: https://swagger.io/blog/code-first-vs-design-first-api/
  - type: Specification
    url: https://spec.openapis.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
